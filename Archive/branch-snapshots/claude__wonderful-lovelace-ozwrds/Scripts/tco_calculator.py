#!/usr/bin/env python3
"""
tco_calculator.py -- Five-year Total Cost of Ownership model for municipal GovTech stacks.

Usage:
    python3 Scripts/tco_calculator.py --staff 500 --population 50000
    python3 Scripts/tco_calculator.py --staff 2000 --population 200000 --output json

Outputs a side-by-side comparison of proprietary (Microsoft 365 / Azure Government)
vs. open-source (SCS + Nextcloud + Element + Decidim + CKAN) stacks over 5 years.
"""

import argparse
import json
import sys


def calculate_proprietary_tco(staff: int, years: int = 5) -> dict:
    """Microsoft 365 E3 + Azure Government reference model."""
    m365_per_seat_per_year = 360  # EUR, E3 tier
    azure_base_annual = 60_000
    azure_per_100_staff = 8_000
    admin_fte = max(1.0, staff / 500)
    admin_fte_cost = 80_000  # EUR per FTE per year
    training_year1 = 40_000 + (staff * 50)
    training_ongoing = 10_000 + (staff * 10)
    integration_year1 = 120_000 + (staff * 100)
    integration_ongoing = 30_000
    exit_cost = 250_000 + (staff * 200)

    licence_total = staff * m365_per_seat_per_year * years
    azure_total = (azure_base_annual + (staff // 100) * azure_per_100_staff) * years
    training_total = training_year1 + training_ongoing * (years - 1)
    integration_total = integration_year1 + integration_ongoing * (years - 1)
    fte_total = admin_fte * admin_fte_cost * years

    return {
        "model": "Proprietary (M365 E3 + Azure Government)",
        "staff": staff,
        "years": years,
        "licence_cost": licence_total,
        "hosting_cost": azure_total,
        "training_cost": training_total,
        "integration_cost": integration_total,
        "fte_cost": fte_total,
        "exit_cost": exit_cost,
        "total": licence_total + azure_total + training_total + integration_total + fte_total + exit_cost,
        "fte_count": admin_fte,
    }


def calculate_opensource_tco(staff: int, years: int = 5) -> dict:
    """SCS + Nextcloud + Element + Decidim + CKAN open-source model."""
    scs_base_annual = 36_000
    scs_per_100_staff = 5_000
    nextcloud_per_seat_per_year = 30  # Enterprise subscription
    admin_fte = max(1.2, staff / 400)  # Slightly higher in Y1-2, normalises
    admin_fte_cost = 80_000
    implementation_year1 = 150_000 + (staff * 120)
    implementation_ongoing = 20_000
    training_year1 = 30_000 + (staff * 40)
    training_ongoing = 8_000 + (staff * 8)
    community_annual = 10_000
    exit_cost = 0  # Data in open formats; components independently replaceable

    hosting_total = (scs_base_annual + (staff // 100) * scs_per_100_staff) * years
    nextcloud_total = staff * nextcloud_per_seat_per_year * years
    implementation_total = implementation_year1 + implementation_ongoing * (years - 1)
    training_total = training_year1 + training_ongoing * (years - 1)
    community_total = community_annual * years
    fte_total = admin_fte * admin_fte_cost * years

    return {
        "model": "Open-Source (SCS + Nextcloud + Element + Decidim + CKAN)",
        "staff": staff,
        "years": years,
        "hosting_cost": hosting_total,
        "subscription_cost": nextcloud_total,
        "implementation_cost": implementation_total,
        "training_cost": training_total,
        "community_cost": community_total,
        "fte_cost": fte_total,
        "exit_cost": exit_cost,
        "total": hosting_total + nextcloud_total + implementation_total + training_total + community_total + fte_total,
        "fte_count": admin_fte,
    }


def breakeven_month(prop: dict, oss: dict) -> int:
    """Estimate the month when cumulative OSS costs drop below proprietary."""
    # Simplified linear interpolation
    prop_monthly = prop["total"] / (prop["years"] * 12)
    oss_monthly = oss["total"] / (oss["years"] * 12)
    # OSS has higher up-front; lower steady-state
    prop_upfront = prop["integration_cost"] / prop["years"]
    oss_upfront = oss["implementation_cost"] / oss["years"]
    if oss_monthly >= prop_monthly:
        return -1  # No breakeven in period
    months = int((oss_upfront - prop_upfront) / (prop_monthly - oss_monthly))
    return max(1, min(months, prop["years"] * 12))


def print_comparison(prop: dict, oss: dict) -> None:
    saving = prop["total"] - oss["total"]
    pct = saving / prop["total"] * 100
    be = breakeven_month(prop, oss)

    print("\n" + "=" * 65)
    print(f"  Municipal GovTech TCO Model  |  Staff: {prop['staff']}  |  {prop['years']} years")
    print("=" * 65)

    def row(label, p_val, o_val):
        print(f"  {label:<35} {p_val:>10,.0f} EUR  {o_val:>10,.0f} EUR")

    print(f"  {'Item':<35} {'Proprietary':>13}  {'Open-Source':>13}")
    print("-" * 65)
    if "licence_cost" in prop:
        row("Software licences", prop["licence_cost"], 0)
    row("Hosting / cloud", prop.get("hosting_cost", 0), oss["hosting_cost"])
    if "subscription_cost" in oss:
        row("Subscriptions (support)", 0, oss["subscription_cost"])
    row("Implementation / migration", prop["integration_cost"], oss["implementation_cost"])
    row("Training", prop["training_cost"], oss["training_cost"])
    if "community_cost" in oss:
        row("Community / upstream contrib.", 0, oss["community_cost"])
    row("FTE staff cost", prop["fte_cost"], oss["fte_cost"])
    row("Exit cost (estimated)", prop["exit_cost"], oss["exit_cost"])
    print("-" * 65)
    print(f"  {'TOTAL':35} {prop['total']:>12,.0f}  {oss['total']:>12,.0f}")
    print("=" * 65)
    print(f"  Net saving (open-source):    {saving:>12,.0f} EUR  ({pct:.1f}%)")
    if be > 0:
        print(f"  Estimated breakeven:         month {be}")
    print("")
    print("  Note: Estimates based on 2024-2026 German public-sector pricing.")
    print("  Commission independent TCO analysis before procurement decisions.")
    print()


def main():
    parser = argparse.ArgumentParser(description="Municipal GovTech 5-year TCO calculator")
    parser.add_argument("--staff", type=int, default=500, help="Number of staff (default: 500)")
    parser.add_argument("--population", type=int, default=50_000, help="Municipality population (informational)")
    parser.add_argument("--years", type=int, default=5, help="Analysis period in years (default: 5)")
    parser.add_argument("--output", choices=["table", "json"], default="table")
    args = parser.parse_args()

    prop = calculate_proprietary_tco(args.staff, args.years)
    oss = calculate_opensource_tco(args.staff, args.years)

    if args.output == "json":
        print(json.dumps({"proprietary": prop, "open_source": oss, "saving": prop["total"] - oss["total"]}, indent=2))
    else:
        print_comparison(prop, oss)


if __name__ == "__main__":
    main()
