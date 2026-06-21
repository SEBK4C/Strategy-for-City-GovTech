# Literature Review State — City GovTech Strategy

**Version:** 0.3.0  
**Letzte Überprüfung:** 2026-06-21  
**Nächste Überprüfung fällig:** 2026-09-21 (Quartalsturnus)

Dieses Dokument verfolgt den aktuellen Stand der Literaturübersicht: Was abgedeckt ist, was fehlt und was aktualisiert werden muss.

---

## Abdeckungskarte

### Abgedeckt (v0.3.0)

| Bereich | Tiefe | Restliche Lücken |
|---|---|---|
| E-Government-Theorie (Wirtz/Weyerer, Janowski, Lathrop/Ruma) | Hoch | Keine post-2022-Literatur zur 4. Generation |
| Schweizer EMBAG und Bundesdigitalstrategie | Hoch | Kantonale Umsetzungsdaten punktuell |
| Deutsches OZG / OZG 2.0 | Hoch | Kommunale Aufnahmequoten fehlen noch |
| Sovereign Cloud Stack | Hoch | Produktions-Performance-Metriken fehlen |
| GAIA-X — Europäische Cloud Trust Framework | Mittel | Vollständige Föderationsdaten 2027 erwartet |
| Open Source in EU-öffentlicher Verwaltung (OSOR 2023) | Hoch | OSOR 2024 noch nicht veröffentlicht |
| Identitätsmanagement (Keycloak, BundID, eID) | Mittel-Hoch | BundID-Nutzungsdaten fehlen |
| Schweizer E-ID (BGEID) | Mittel | Technische Implementierungsdetails 2026 fehlen |
| eCH-Standards | Mittel | Tiefenanalyse einzelner Standards fehlt |
| Decidim / CONSUL (partizipative Plattformen) | Hoch | — |
| Matrix/Element für Verwaltung | Mittel | BundesMessenger-Adoptionsdaten fehlen |
| Nextcloud für Verwaltung | Hoch | — |
| Open-Data-Portale (CKAN) | Hoch | — |
| ZenDiS | Mittel | Detaillierte Programmberichte fehlen |
| GovStack (ITU/DIAL) + Spec v1.0 | Hoch | BB-Compliance-Mapping veröffentlicht (Abschn. 4.12) |
| GIS für Kommunen | Mittel | Keine akademische Literatur zitiert |
| Beschaffungsrahmen (inkl. AKDB) | Hoch | Keine vergleichenden EU-Vergabestudien |
| Gesamtbetriebskosten-Studien | Mittel | DINUM-Studie integriert; weitere fehlen |
| Fallstudien kleiner Kommunen | Hoch | 3 Fallstudien dokumentiert (Ziel erreicht für v0.2.0) |
| Nutzerzufriedenheitsforschung | Niedrig | KRITISCHE Lücke — siehe unten |
| Change Management bei IT-Transitionen | Niedrig | München LiMux referenziert, nicht vertieft |
| EU-Datengesetz | Mittel | Auswirkungen auf kommunale Datenverwaltung |
| EU AI Act 2024 | Hoch | Kommunale Compliance-Rahmen in Abschn. 4.13 |
| Open Government Theorie (Lathrop & Ruma) | Hoch | Einzelne Kapitelzitate noch ausständig |

### Noch nicht abgedeckt

- **Bürger-Zufriedenheitsforschung** — kaum peer-reviewte Literatur vorhanden; Erhebungsrahmen-Design für v1.0
- **UN E-Government Survey 2024** (UNDESA, erwartet spät 2024)
- **European Health Data Space (EHDS)** — in Entwicklung; relevant für kommunale Gesundheitsdienste
- **Longitudinale Fallstudiendaten** — Jahr-2-Daten für Schaffhausen, Biberach, Rosenheim ausstehend

---

## Kritische Lücken

### Nutzerzufriedenheitsforschung
Fast keine peer-reviewten Literatur vergleicht Bürgerzufriedenheit bei Open-Source- vs. proprietären kommunalen Digitaldiensten. **Aktion:** Design eines Bürgerzufriedenheits-Erhebungsrahmens, einsetzbar von teilnehmenden Kommunen. Ziel: v1.0-Anhang.

### Longitudinale Implementierungsdaten
Fehlen für Vollständig-Open-Source-Transitionen außer LiMux. Die drei v0.2.0-Fallstudien sind Erstdokumentationen und bedürfen längerer Beobachtung. Ziel: v1.0.

### GovStack Payments Building Block
Der fehlende Payments-Baustein (keine Komponente im aktuellen Stack) ist die größte funktionale Lücke gegenüber dem GovStack Spec v1.0. Ziel: PaymentHub EE oder Kantons-/Länderzahlungsgateway für v1.0.

---

## Verbesserungsprotokoll

| Datum | Aktion | Durch | Ergebnis |
|---|---|---|---|
| 2026-06-20 | Erstliteraturübersicht, v0.1.0-Entwurf | SG | 30 Primärquellen; 46 Zitationsslots |
| 2026-06-21 | v0.2.0: Quellen verifiziert, neue Quellen (eCH, GovStack, ZenDiS, BGEID, CONSUL, EU Data Act) | SG/KI | 47 Quellen; alle v0.1.0-unverifizierten Quellen bestätigt; 3 neue Fallstudien |
| 2026-06-21 | v0.3.0: OSOR [54], GovStack Spec [56], AKDB [57], Lathrop & Ruma [58], GAIA-X [59], EU AI Act [60] integriert; Sektionen 3.8, 4.12, 4.13, 7.5 neu | SG/KI | 53 Quellen; GovStack BB-Compliance-Mapping abgeschlossen; EU-KI-Gesetz kommunaler Rahmen; GAIA-X Cloud Trust Layer |

---

## Quartalspruf-Checkliste

Bei Ausführung von `Scripts/update_literature_review.py` prüfen:

- [ ] Neue Schweizer E-Government-Gesetzgebung oder Strategieaktualisierungen
- [ ] Neue deutsche OZG-Umsetzungsberichte oder FITKO-Veröffentlichungen
- [ ] Neue EU-Gesetzgebung (Datengesetz-Umsetzung, KI-Gesetz, EHDS, etc.)
- [ ] Neue Sovereign-Cloud-Stack-Veröffentlichungen oder Governance-Updates
- [ ] Neue openCode.de-Statistiken oder Fallstudien
- [ ] Neue akademische Paper zu E-Government-Reifegradmodellen (GIQ, ISM, EJEG)
- [ ] Neue kommunale Open-Source-Einsätze oder Fallstudien
- [ ] Neue Sicherheitshinweise für Stack-Komponenten
- [ ] OSOR-Jahresbericht (EU Open Source Observatory, jährlich) — OSOR 2024 erwartet
- [ ] UN E-Government Survey (zweijährlich, nächste 2024)
- [ ] GovStack Specification Updates (v1.1 erwartet 2026/2027)
- [ ] ZenDiS Jahresbericht 2024
- [ ] GAIA-X Federation Status Update (Herbst 2026)
- [ ] EU AI Act Delegated Acts und technische Standards (ENISA, 2026–2027)
- [ ] BundID Nutzungsstatistiken (BMI Pressestelle anfragen)
- [ ] Schweizer BGEID Pilot-Einsatzdaten (ISIO / E-Government Suisse)
- [ ] Jahr-2-Daten für Fallstudien (Schaffhausen, Biberach, Rosenheim)
