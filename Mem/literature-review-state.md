# Literature Review State — City GovTech Strategy

**Version:** 0.2.0  
**Letzte Überprüfung:** 2026-06-21  
**Nächste Überprüfung fällig:** 2026-09-21 (Quartalsturnus)

Dieses Dokument verfolgt den aktuellen Stand der Literaturübersicht: Was abgedeckt ist, was fehlt und was aktualisiert werden muss.

---

## Abdeckungskarte

### Abgedeckt (v0.2.0)

| Bereich | Tiefe | Restliche Lücken |
|---|---|---|
| E-Government-Theorie (Wirtz/Weyerer, Janowski) | Hoch | Keine post-2022-Literatur zur 4. Generation |
| Schweizer EMBAG und Bundesdigitalstrategie | Hoch | Kantonale Umsetzungsdaten punktuell |
| Deutsches OZG / OZG 2.0 | Hoch | Kommunale Aufnahmequoten fehlen noch |
| Sovereign Cloud Stack | Hoch | Produktions-Performance-Metriken fehlen |
| Open Source in EU-öffentlicher Verwaltung | Mittel | OSOR-Jahresbericht noch nicht integriert |
| Identitätsmanagement (Keycloak, BundID, eID) | Mittel-Hoch | BundID-Nutzungsdaten fehlen |
| Schweizer E-ID (BGEID) | Mittel | Technische Implementierungsdetails 2026 fehlen |
| eCH-Standards | Mittel | Tiefenanalyse einzelner Standards fehlt |
| Decidim / CONSUL (partizipative Plattformen) | Hoch | — |
| Matrix/Element für Verwaltung | Mittel | BundesMessenger-Adoptionsdaten fehlen |
| Nextcloud für Verwaltung | Hoch | — |
| Open-Data-Portale (CKAN) | Hoch | — |
| ZenDiS | Mittel | Detaillierte Programmberichte fehlen |
| GovStack (ITU/DIAL) | Mittel | Technische Spezifikation v1.0 noch nicht integriert |
| GIS für Kommunen | Mittel | Keine akademische Literatur zitiert |
| Beschaffungsrahmen | Mittel | Keine vergleichenden EU-Vergabestudien |
| Gesamtbetriebskosten-Studien | Mittel | DINUM-Studie integriert; weitere fehlen |
| Fallstudien kleiner Kommunen | Hoch | 3 Fallstudien dokumentiert (Ziel erreicht für v0.2.0) |
| Nutzerzufriedenheitsforschung | Niedrig | KRITISCHE Lücke — siehe unten |
| Change Management bei IT-Transitionen | Niedrig | München LiMux referenziert, nicht vertieft |
| EU-Datengesetz | Mittel | Auswirkungen auf kommunale Datenverwaltung |

### Noch nicht abgedeckt

- **OSOR Annual Report 2023** (EU Open Source Observatory)
- **GovStack Specification v1.0** (technische Bausteinspezifikation)
- **EU AI Act 2024** (Auswirkungen auf kommunale KI-Anwendungen)
- **GAIA-X Implementierungsstand 2025/2026**
- **Lathrop & Ruma (2010) Open Government** — Grundlagentext
- **AKDB Jahresbericht 2023**

---

## Kritische Lücken

### Nutzerzufriedenheitsforschung
Fast keine peer-reviewten Literatur vergleicht Bürgerzufriedenheit bei Open-Source- vs. proprietären kommunalen Digitaldiensten. **Aktion:** Design eines Bürgerzufriedenheits-Erhebungsrahmens, einsetzbar von teilnehmenden Kommunen. Ziel: v1.0-Anhang.

### Longitudinale Implementierungsdaten
Fehlen für Vollständig-Open-Source-Transitionen außer LiMux. Die drei v0.2.0-Fallstudien sind Erstdokumentationen und bedürfen längerer Beobachtung. Ziel: v1.0.

---

## Verbesserungsprotokoll

| Datum | Aktion | Durch | Ergebnis |
|---|---|---|---|
| 2026-06-20 | Erstliteraturübersicht, v0.1.0-Entwurf | SG | 30 Primärquellen; 46 Zitationsslots |
| 2026-06-21 | v0.2.0: Quellen verifiziert, neue Quellen (eCH, GovStack, ZenDiS, BGEID, CONSUL, EU Data Act) | SG/KI | 47 Quellen; alle v0.1.0-unverifizierten Quellen bestätigt; 3 neue Fallstudien |

---

## Quartalspruf-Checkliste

Bei Ausführung von `Scripts/update_literature_review.py` prüfen:

- [ ] Neue Schweizer E-Government-Gesetzgebung oder Strategieaktualisierungen
- [ ] Neue deutsche OZG-Umsetzungsberichte oder FITKO-Veröffentlichungen
- [ ] Neue EU-Gesetzgebung (Datengesetz-Umsetzung, KI-Gesetz, etc.)
- [ ] Neue Sovereign-Cloud-Stack-Veröffentlichungen oder Governance-Updates
- [ ] Neue openCode.de-Statistiken oder Fallstudien
- [ ] Neue akademische Paper zu E-Government-Reifegradmodellen (GIQ, ISM, EJEG)
- [ ] Neue kommunale Open-Source-Einsätze oder Fallstudien
- [ ] Neue Sicherheitshinweise für Stack-Komponenten
- [ ] OSOR-Jahresbericht (EU Open Source Observatory, jährlich)
- [ ] UN E-Government Survey (zweijährlich, nächste 2024)
- [ ] GovStack Specification Updates
- [ ] ZenDiS Jahresbericht
