---
title: "Souverän von Anfang an — Anhänge v0.2.0"
author: "Sebastian Graf, Autonomes Büro für Zivile Digitale Infrastruktur"
version: "0.2.0"
date: "2026-06-20"
language: "de"
source-of-truth: false
source-language: "en"
source-file: "Doc/en/appendices-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
---

# Anhänge — Souverän von Anfang an v0.2.0

Diese Anhänge ergänzen `Doc/de/sovereign-by-design-v0.2.0.de.md`. Sie stellen operative Werkzeuge bereit: ein Begriffsglosssar, ein TCO-Berechnungsblatt und ein viertteljährliches Literaturrecherche-Protokoll.

Verbindlich ist die englische Fassung: `Doc/en/appendices-v0.2.0.md`.

---

## Anhang A — Glossar der Schlüsselbegriffe

| Begriff | Definition | Kontext |
|---|---|---|
| **AGPL-3.0** | GNU Affero General Public License v3.0. Starkes Copyleft, das Quellcode-Offenlegung auch bei Netzwerkdiensten verlangt. | Bevorzugte Lizenz für behördliche SaaS-Deployments. |
| **AKDB** | Anstalt für Kommunale Datenverarbeitung in Bayern. | Primärer IT-Dienstleister für bayerische Kommunen. |
| **API** | Application Programming Interface. Definierter Vertrag für Maschine-zu-Maschine-Kommunikation. | Voraussetzung für Interoperabilität zwischen Stack-Komponenten. |
| **BITV 2.0** | Barrierefreie-Informationstechnik-Verordnung. Deutsche Bundesverordnung zur Umsetzung von WCAG 2.1 AA für öffentliche Webdienste. | Verpflichtend für deutsche Bundesbehörden; Modell für Länder/Kommunen. |
| **BPMN 2.0** | Business Process Model and Notation 2.0. ISO 19510-Standard für graphische Prozessmodellierung. | Erforderlich für OZG-Prozessautomation und Interoperabilität. |
| **BSI** | Bundesamt für Sicherheit in der Informationstechnik. | Gibt IT-Grundschutz, C5-Kriterien und Sicherheitsempfehlungen heraus. |
| **BundID** | Das deutsche Bundeskonto für Bürger. OIDC-basiert, länderübergreifend föderiert. | Pflicht-Integrationsziel für OZG-Online-Dienste. |
| **BöB** | Bundesgesetz über das öffentliche Beschaffungswesen (CH, SR 172.056.1). | Schweizerisches Äquivalent zur deutschen VgV/GWB für Bundesebene. |
| **C5** | Cloud Computing Compliance Criteria Catalogue (BSI). Sicherheitsbaseline für Cloud-Dienste. | Referenz für Auswahl SCS-zertifizierter Hosting-Anbieter. |
| **CKAN** | Comprehensive Knowledge Archive Network. Open-Source-Datenportal-Plattform. | Betreibt opendata.swiss, data.gov, EU Open Data Portal. |
| **CoP** | Community of Practice. Gruppe von Praktikern mit gemeinsamem Wissensaustausch. | Interkommunales Open-Source-Kooperationsmodell. |
| **CONSUL** | Open-Source-Plattform für Bürgerbeteiligung (Madrid). AGPL-3.0. | Alternative zu Decidim; über 40 Länder. |
| **CVE** | Common Vulnerabilities and Exposures. Standardkennung für öffentlich bekannte Sicherheitslücken. | Grundlage für Patch-Management-SLA-Definitionen. |
| **DCAT-AP** | Data Catalog Vocabulary — Application Profile. EU-Metadatenstandard für Datenportale. | Erforderlich für CKAN-Interoperabilität mit GovData.de und EU Open Data Portal. |
| **Decidim** | Open-Source-Plattform für partizipative Demokratie. AGPL-3.0. Ursprung: Barcelona. | 400+ globale Deployments, u.a. NYC, Helsinki, Schaffhausen. |
| **Digitale Souveränität** | Die Fähigkeit einer Organisation, ihre digitalen Systeme und Daten zu kontrollieren, zu prüfen und anzupassen, ohne Abhängigkeit von einzelnen Anbietern. | Kernbegriff dieser Strategie. |
| **DMS** | Dokumentenverwaltungssystem. Software für Erstellung, Speicherung, Abruf und Verwaltung digitaler Dokumente. | Nextcloud ist das empfohlene DMS für Kommunen. |
| **DSGVO** | Datenschutz-Grundverordnung (EU) 2016/679. | Pflichtkonformität für alle kommunalen Datenverarbeitungen. |
| **DVS** | Digitale Verwaltung Schweiz. Bundeskantonale Koordinationsstelle für digitale Verwaltung. | Schweizer Pendant zu FITKO. |
| **E2E** | Ende-zu-Ende-Verschlüsselung. Verschlüsselung beim Sender, nur vom Empfänger entschlüsselbar. | CryptPad und Matrix/Element bieten E2E standardmäßig. |
| **eCH** | E-Government-Standards Schweiz. Schweizer Interoperabilitätsstandards-Gremium. | Schweizer Äquivalent zu deutschen XÖV-Standards. |
| **EfA** | Einer für Alle. OZG-Prinzip: ein Dienst, vom Land entwickelt, von allen nutzbar. | Zentrales OZG 2.0-Umsetzungsprinzip. |
| **eID** | Elektronischer Identitätsnachweis. In CH: staatliche digitale Identität auf Basis W3C Verifiable Credentials (BGEID). | SSI-basierte Wallet-Architektur. |
| **EMBAG** | Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (SR 172.019). | Weltweit stärkstes OSS-Mandat auf Bundesebene. |
| **FITKO** | Föderale IT-Kooperation. Deutsch-föderales Koordinationsgremium für OZG-Umsetzung. | Betreibt FIT-Store; primäres OZG-technisches Governance-Gremium. |
| **Forgejo** | Gemeinschafts-gesteuerter Gitea-Fork. Git-Hosting-Plattform. MIT/GPL-2.0. | Empfohlen für kommunales Code- und Konfigurationsmanagement. |
| **FSFE** | Free Software Foundation Europe. Advocacy-Organisation für freie Software. | Kampagne „Öffentliches Geld? Öffentlicher Code!“ |
| **FUD** | Fear, Uncertainty and Doubt (Angst, Unsicherheit, Zweifel). Marketingstrategie zur Abschreckung von Wettbewerbsadoption. | Vgl. Abschnitt 7.3 des Hauptdokuments. |
| **GAIA-X** | Europäische Initiative für föderierte, sichere Cloud-Infrastruktur. | Policy-Rahmen; SCS ist die technische Umsetzung. |
| **GIS** | Geoinformationssystem. | QGIS + GeoServer + PostGIS ist der empfohlene Open-Source-GIS-Stack. |
| **govdigital eG** | Deutsche Genossenschaft öffentlich-rechtlicher IT-Dienstleister. | Rahmenverträge für Kommunen; SCS-basierter Cloud-Betrieb. |
| **GovStack** | ITU/DIAL-Initiative für wiederverwendbare digitale Governance-Bausteine. | API-Spezifikationen für Identität, Zahlungen, Registrierung u.a. |
| **GWB** | Gesetz gegen Wettbewerbsbeschränkungen. | Vergaberechtliche Grundlage für öffentliche Beschaffung in Deutschland. |
| **IAM** | Identitäts- und Zugangsverwaltung. | Keycloak ist die empfohlene IAM-Plattform. |
| **INSPIRE** | Infrastructure for Spatial Information in Europe. EU-Richtlinie für Geodaten-Interoperabilität. | Pflicht für kommunale Geodaten-Publikation. |
| **IT-Grundschutz** | BSI-Sicherheitsbaseline-Methodik. | Pflichtiger Referenzrahmen für deutsche öffentliche IT-Sicherheit. |
| **Keycloak** | Open-Source-IAM-Plattform. Apache-2.0. | Empfohlen für alle kommunalen Identitäts- und SSO-Anforderungen. |
| **LibreOffice** | Open-Source-Office-Suite. LGPL-3.0/MPL-2.0. The Document Foundation. | Desktop-Komponente; Collabora Online ist die Browser-/Serverversion. |
| **Matrix** | Offenes dezentrales Kommunikationsprotokoll. Apache-2.0. | Basis für BundesMessenger (DE), Tchap (FR). |
| **nDSG** | Neues Datenschutzgesetz (CH), SR 235.1. In Kraft seit 01.09.2023. | Schweizer Äquivalent zur DSGVO. |
| **NIS2** | Richtlinie (EU) 2022/2555. Netz- und Informationssicherheitsrichtlinie 2. | Erweitert Cybersicherheitspflichten auf kommunale kritische Infrastruktur. |
| **OIDC** | OpenID Connect. Authentifizierungsschicht über OAuth 2.0. | Standard für Single-Sign-On; Keycloak implementiert es nativ. |
| **OpenSlides** | Open-Source-Konferenz- und Sitzungsverwaltungssystem. MIT. Intevation GmbH. | Empfohlen für kommunale Rats- und Gremienarbeit. |
| **OSI** | Open Source Initiative. Hüter der Open Source Definition. | Referenz für Lizenz-Compliance-Bewertung. |
| **OSOR** | Open Source Observatory. Europäische Kommission — Dokumentation von OSS in der öffentlichen Verwaltung. | Quelle für europaweite Deployment-Statistiken. |
| **OZG** | Onlinezugangsgesetz (2017, geändert 2024). | Gesetzliches Mandat für digitale kommunale Dienste in Deutschland. |
| **SAML 2.0** | Security Assertion Markup Language 2.0. Föderiertes Identitätsprotokoll. | Erforderlich für Altsystem-Integration neben OIDC. |
| **SCS** | Sovereign Cloud Stack. Open-Source-IaaS/PaaS-Referenzarchitektur. Apache-2.0. OSBA. | Empfohlene Infrastrukturschicht für Kommunen. |
| **SSI** | Self-Sovereign Identity. Identitätsmodell, bei dem der Nutzer seine Credentials in einer Wallet kontrolliert. | Architektur der Schweizer eID (BGEID). |
| **TCO** | Total Cost of Ownership / Gesamtbetriebskosten. Vollständige Lebenszykluskosten inkl. Lizenzen, Hosting, Support, Schulung, Migration. | Wirtschaftlichkeitsrahmen in Abschnitt 3.6 und Anhang B. |
| **TYPO3** | Open-Source-Enterprise-CMS. GPL-2.0. TYPO3 Association. | Dominierendes CMS für deutschsprachige Behördenwebsites. |
| **VgV** | Vergabeverordnung. Deutsche Beschaffungsverordnung zur Umsetzung der EU-Vergaberichtlinien. | Gilt für öffentliche Beschaffungen oberhalb der Schwellenwerte in Deutschland. |
| **WCAG** | Web Content Accessibility Guidelines. W3C-Standard (aktuell v2.1; v2.2 veröffentlicht 2023). | Barrierefreiheits-Baseline für alle öffentlichen digitalen Dienste. |
| **XÖV** | XML in der öffentlichen Verwaltung. Familie deutscher XML-Interoperabilitätsstandards. | KoSIT-gepflegt; verpflichtend für OZG-Datenaustausch. |
| **ZenDiS** | Zentrum für Digitale Souveränität der öffentlichen Verwaltung. GmbH des Bundes. | Koordiniert OpenDesk; Schlüsselakteur für bundesweite/kommunale OSS-Strategie. |

---

## Anhang B — TCO-Berechnungsblatt

Dieses Berechnungsblatt bietet eine strukturierte Methode zur Berechnung und Dokumentation der Gesamtbetriebskosten (TCO/GBK) beim Vergleich eines Open-Source-Stacks mit einem proprietären Bestandssystem.

### B.1 Szenario-Parameter

| Parameter | Wert |
|---|---|
| Gemeindename | ________________ |
| Einwohnerzahl | ________________ |
| Anzahl betroffener Beschäftigter | ________________ |
| Analysezeitraum (Jahre) | 5 |
| Kalkulationszinssatz (%) | 3 |
| Berechnungsdatum | ________________ |
| Erstellt von | ________________ |

### B.2 Bestandssystem (Proprietär) — Kosten

**Jährlich wiederkehrende Kosten (€/Jahr):**

| Kategorie | Aktuelle Kosten (€/Jahr) | Anmerkungen |
|---|---|---|
| Softwarelizenzen (Office-Produktivität) | | |
| Softwarelizenzen (E-Mail/Kollaboration) | | |
| Softwarelizenzen (Videokonferenz) | | |
| Softwarelizenzen (IAM/SSO) | | |
| Softwarelizenzen (CMS/Web) | | |
| Softwarelizenzen (Sonstige) | | |
| Hosting-/Cloud-Gebühren | | |
| Anbieter-Supportverträge | | |
| Externe IT-Dienstleistungsverträge | | |
| Interne IT-Stellen (VZÄ × Jahresgehalt) | | |
| Schulungen (jährlich) | | |
| **Summe jährlich wiederkehrend (A1)** | | |

### B.3 Open-Source-Stack — Kosten

**Einmalige Migrationskosten (€, Jahr 0–1):**

| Kategorie | Geschätzte Kosten (€) | Anmerkungen |
|---|---|---|
| Bestandsaufnahme und Planung (Phase 0) | | |
| Infrastrukturaufbau (Phase 1) | | |
| Kernstack-Deployment (Phase 2) | | |
| Fachverfahren-Integration (Phase 3) | | |
| Bürgerservices (Phase 4) | | |
| Risikopuffer (15 %) | | |
| **Einmalige Gesamtkosten (B0)** | | |

**Jährlich wiederkehrende Kosten (€/Jahr, Jahre 2–5):**

| Kategorie | Geschätzte Kosten (€/Jahr) | Anmerkungen |
|---|---|---|
| Hosting (SCS-zertifizierter Anbieter oder eigenes RZ) | | |
| Software-Supportverträge (Nextcloud, Collabora usw.) | | |
| Interne IT-Stellen (VZÄ × Jahresgehalt) | | |
| Externe Managed Services | | |
| Jährliche Schulungen | | |
| Community-Beiträge/Upstream-Sponsoring | | |
| Sicherheitsaudits (jährlich) | | |
| **Summe jährlich wiederkehrend (B1)** | | |

### B.4 Fünfjahres-Barwertberechnung

Kalkulationszinssatz r = 3 %:

**Proprietärer Stack — 5-Jahres-Barwert:**
```
BW_prop = A1 × [(1 - (1+r)^-5) / r]
         = A1 × 4,580
```

**Open-Source-Stack — 5-Jahres-Barwert:**
```
BW_oss = B0 + B1 × [(1 - (1+r)^-4) / r] × (1/(1+r))
       = B0 + B1 × 3,717
```

**Netto-Vorteil:**
```
Netto-Vorteil = BW_prop - BW_oss
```

| Kennzahl | Wert (€) |
|---|---|
| BW_prop | ________________ |
| BW_oss | ________________ |
| **5-Jahres-Netto-Vorteil** | ________________ |
| Amortisationsjahr | ________________ |
| Jährliche Einsparung (Jahre 3–5) | ________________ |
| Einsparung pro Arbeitsplatz/Jahr (Jahre 3–5) | ________________ |

### B.5 Nicht-quantifizierbare Vorteile (Narrativ)

Qualitative Vorteile, die das TCO-Modell nicht erfasst:

- **Regulatorische Konformität:** ________________
- **Lieferantenunabhängigkeit:** ________________
- **Datenschutzverbesserung:** ________________
- **Prüfbarkeit / demokratische Rechenschaftspflicht:** ________________
- **Interoperabilitätsverbesserungen:** ________________
- **Kompetenzentwicklung der Mitarbeitenden:** ________________
- **Erhaltene Community-Beiträge:** ________________

### B.6 Risikobereinigung

Für jedes hoch bewertete Risiko im Risikoregister (Abschnitt 7.1 des Hauptdokuments):

| Risiko-ID | Beschreibung | Wahrsch. | Auswirkung (€) | Erwartete Kosten (€) |
|---|---|---|---|---|
| R01 | Skill-Lücken | | | |
| R03 | Politischer Richtungswechsel | | | |
| R05 | Sicherheitsvorfall | | | |
| R06 | Nutzerwiderstand | | | |
| **Risikobereinigte Summe** | | | | |

### B.7 Berichtsvorlage

Zusammenfassungsabsatz für Gemeinderat/Stadtspitze:

> „Im Fünfjahreszeitraum erbringt die Migration von [N] Beschäftigten-Arbeitsplätzen auf einen Open-Source-Technologie-Stack einen Barwertvorteil von **€[X]** gegenüber der Verlängerung der aktuellen proprietären Verträge. Die einmaligen Migrationskosten von **€[B0]** werden im Jahr **[Y]** amortisiert. Die jährliche Einsparung ab Jahr 3 beträgt **€[Z]** (€[Z/N] pro Arbeitsplatz). Nicht-quantifizierbare Vorteile umfassen verbesserte regulatorische Konformität gemäß EMBAG/OZG 2.0, den Wegfall von Drittstaaten-Datenübermittlungsrisiken und die vollständige Prüfbarkeit kommunaler IT-Systeme.“

---

## Anhang C — Viertteljährliches Literaturrecherche-Protokoll

Dieses Protokoll steuert die wiederkehrende Aktualisierung der Literaturrecherche und des Quellenregisters. Es speist `Mem/literature-review-state.md` und wird durch `Scripts/update_literature_review.py` ausgeführt.

### C.1 Reviewrhythmus

| Review-Typ | Häufigkeit | Auslöser |
|---|---|---|
| Vollständiges Quartal-Review | Alle 3 Monate | Kalender: März, Juni, September, Dezember |
| Schnell-Update | Bei Bedarf | Wichtige Gesetzgebung, signifikante CVE, Community-Governance-Änderung |
| Jährliches Tiefenreview | Einmal jährlich (Dezember) | Versions-Bump auf nächste Minor-Version |

### C.2 Viertteljährliche Review-Checkliste

**Regulatorisches und gesetzgeberisches Monitoring:**
- [ ] Schweizer Bundesblatt — neue Verordnungen/Gesetze für digitale Verwaltung
- [ ] Deutscher Bundesanzeiger / BMI — OZG-Fortschritt, IT-Planungsrat-Beschlüsse
- [ ] EUR-Lex — neue Digitalgesetze (KI-Gesetz-Umsetzung, Datengesetz, IEA)
- [ ] BSI — neue IT-Grundschutz-Module, C5-Updates, Sicherheitsempfehlungen
- [ ] eCH — neue oder revidierte Standards
- [ ] KoSIT — neue XÖV-Standards

**Community- und Projekt-Monitoring:**
- [ ] Nextcloud — neue Hauptversion, Sicherheitshinweise, Behörden-Fallstudien
- [ ] Keycloak — neue Hauptversion, FIPS/BSI-Konformitäts-Updates
- [ ] Matrix — Spezifikationsänderungen, neue Behörden-Deployments
- [ ] Decidim/CONSUL — Haupt-Releases, neue Kommunal-Deployments
- [ ] OpenSlides — neue Releases, Ratsadoptionen
- [ ] CryptPad — neue Releases, NGI-Förderstatus
- [ ] Forgejo — Governance-Änderungen, Haupt-Releases
- [ ] Sovereign Cloud Stack — neue Releases, neue zertifizierte Anbieter
- [ ] CKAN — Haupt-Releases, DCAT-AP-Konformitäts-Updates
- [ ] TYPO3/Drupal — Sicherheits-Releases, Barrierefreiheitsverbesserungen

**Forschungs- und Berichts-Monitoring:**
- [ ] OSOR — neue Veröffentlichungen, Fallstudien, Jahresbericht
- [ ] ZenDiS — OpenDesk-Updates, neue Publikationen
- [ ] Europ. Kommission — DESI-Index, eGovernment Benchmark
- [ ] GovStack — neue Building-Block-Spezifikationen
- [ ] Wissenschaftliche Zeitschriften: GIQ, EJEG, ISM — neue relevante Artikel
- [ ] Bertelsmann Stiftung, KGSt — Deutsche Kommunal-IT-Berichte
- [ ] Schweizer Bundeskanzlei/DVS — Strategie-Updates

### C.3 Quellenaufnahme-Protokoll

Bei Hinzufügen einer neuen Quelle zu `Mem/source-registry.md`:

1. Nächste fortlaufende ID ([N+1]) vergeben
2. Alle Metadatenfelder gemäß Vorlage ausfüllen
3. Status auf `Verification status: unverified` setzen
4. Zitat im relevanten Papierabschnitt mit `[ENTWURF]`-Annotation einfügen
5. URL-Zugänglichkeit und Inhaltübereinstimmung prüfen
6. Status auf `verified` aktualisieren
7. `[ENTWURF]`-Annotation entfernen
8. Abdeckungskarte in `Mem/literature-review-state.md` aktualisieren

### C.4 Versionierungskriterien

| Änderungstyp | Versions-Bump |
|---|---|
| ≥5 neue Quellen, ≥2 Papierabschnitte aktualisiert | Minor (z.B. 0.2.0 → 0.3.0) |
| Strukturelle Änderung am Papier oder größere Neuformulierung | Minor |
| Tippfehler-Korrekturen, URL-Updates, 1–2 neue Quellen | Patch (z.B. 0.2.0 → 0.2.1) |
| Peer-reviewed, extern validiert, breit geteilt | Major (z.B. 0.x.y → 1.0.0) |

### C.5 Lücken-Tracking-Vorlage

Für jede identifizierte Lücke in `Mem/literature-review-state.md` eintragen:

```markdown
### Lücke: [Kurzname]
- **Domäne:** [Technologie | Regulierung | Fallstudie | TCO | UX]
- **Schwere:** [kritisch | hoch | mittel | niedrig]
- **Beschreibung:** [1–2 Sätze]
- **Maßnahme:** [Was zu tun ist, um die Lücke zu schließen]
- **Zielversion:** [z.B. v0.3.0]
- **Zuständig:** [Name oder „nicht zugewiesen“]
- **Status:** [offen | in Bearbeitung | gelöst]
```

### C.6 Übersetzungs-Synchronisation

Nach Aktualisierung des englischen Quell-Dokuments:

1. `Scripts/translate_document.py --check-diff` ausführen, um geänderte Abschnitte zu identifizieren
2. Deutsche Übersetzung (`Doc/de/`) manuell für inhaltlich wesentliche Änderungen aktualisieren
3. Für Patch-Änderungen (URLs, Tippfehler): maschinell unterstützte Übersetzung mit menschlicher Kontrolle akzeptabel
4. Versionsnummer im YAML-Frontmatter des deutschen Dokuments anpassen
5. `changelog`-Block in beiden Dokumenten aktualisieren

---

*Anhänge v0.2.0 · CC-BY-4.0 · Sebastian Graf, Autonomes Büro für Zivile Digitale Infrastruktur*
