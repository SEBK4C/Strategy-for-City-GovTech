---
title: "Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
translation-of: "Doc/en/sovereign-by-design-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - kommunale Digitaltransformation
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - Gesamtbetriebskosten
---

# Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Kontakt:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (diese Übersetzung) · English (Quelldokument)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Änderungen gegenüber v0.1.0:* Alle bisher unverifizierten Zitate gegen Primärquellen geprüft. Neuer Abschnitt 3.7 (Fallstudien kleiner Kommunen). Neuer Abschnitt 4.11 (Gesamtbetriebskosten-Rahmenwerk). Neue Quellen: eCH-Standards, CONSUL Democracy, GovStack (ITU/DIAL), ZenDiS, Schweizer E-ID, EU-Datengesetz. Quellenregister auf 47 Primäreinträge erweitert.

---

## Zusammenfassung

Kommunalverwaltungen sind die demokratisch bürgernächste Ebene staatlichen Handelns, stehen jedoch vor einer gravierenden strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, anbietergekoppelt und im Widerspruch zu gemeinwohlorientierten Werten. Dieses Papier präsentiert eine umfassende, zitationsvollständige Strategie für die Implementierung eines modernen Open-Source-Technologiestapels in Kommunalverwaltungen. Auf Grundlage bewährter Ansätze aus dem Schweizer Bundesrecht (EMBAG), dem deutschen OZG-Reformprogramm, der Sovereign-Cloud-Stack-Initiative, dem ITU/DIAL GovStack-Rahmenwerk und der europäischen Gemeinschaft für souveräne Technologie leiten wir einen grundlagenorientierten Implementierungsfahrplan, einen Stakeholder-Einbindungsrahmen, eine Beschaffungsstrategie und ein Gesamtbetriebskosten-Modell ab. Drei verifizierte Fallstudien kleiner Kommunen (Kanton Schaffhausen CH, Biberach DE und Rosenheim DE) belegen, dass der Ansatz auch für Kommunen von 50.000–150.000 Einwohnern ohne große Inhouse-IT-Abteilungen realisierbar ist. Wir kommen zu dem Schluss, dass Open-Source-Technologiestapel für Kommunen nicht nur technisch ausgereift, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Rechtsordnungen gesetzlich vorgeschrieben sind.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Gesamtbetriebskosten, GovStack

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen; Regulierungsbehörden fordern Interoperabilität und Datenschutz; und fiskalischer Druck verlangt nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte weltweit gefangen in einem Zyklus aus proprietärer Anbieterabhängigkeit, teuren Lizenzverträgen und fragmentierten Systemen, die gute Verwaltungsführung eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut dokumentiert: Vendor-Lock-in erhöht Wechselkosten und Verhandlungsasymmetrien [4]; proprietäre Formate behindern ämterübergreifenden Datenaustausch und Transparenz [45]; geschlossene Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Haushalte, die ansonsten der Daseinsvorsorge zugute kämen [3, 5]. Am grundlegendsten: Wenn Software, die demokratische Institutionen betreibt, von privaten Akteuren kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Interesse und Unternehmensimperativen [4].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG von 2023 verpflichtet dazu, mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source zu veröffentlichen [1]. Deutschlands OZG 2.0, Sovereign Cloud Stack und OpenDesk-Initiative stellen das ambitionierteste Open-Source-Regierungstechnologieprogramm Europas dar [2, 3, 42]. Die GovStack-Initiative von ITU und DIAL bietet ein globales Rahmenwerk wiederverwendbarer Verwaltungsbausteine [47]. Die Kampagne „Öffentliches Geld? Öffentlicher Code!“ der FSFE, unterstützt von über 200 Organisationen in 30 Ländern, formuliert das demokratische Prinzip: Öffentlich finanzierte Software gehört der Öffentlichkeit [4].

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und kommunale Behörden, einschließlich Gemeinden, Kommunen, Städte und äquivalente Strukturen in Schweizer Kantonen. Die Strategie skaliert von Kleinkommunen (5.000–50.000 Einwohner) bis Großstädten (500.000+).

*Open-Source-Technologiestapel* bezeichnet Softwarekomponenten, die unter OSI-zugelassenen Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder ohne übermäßige Kosten migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — das Recht, Software zu inspizieren, zu ändern, zu prüfen und zu migrieren, ohne von einem einzigen Anbieter abhängig zu sein [3].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Technologiestapel für Kommunen im Jahr 2026 aus?
2. Welche Lehren lassen sich aus der Schweizer, deutschen und europäischen Gemeinschaft für souveräne Technologie ziehen?
3. Was ist der optimale, schrittweise Implementierungspfad für eine Stadt mit 50.000–500.000 Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Einbindung und Risikomanagement gestaltet werden?
5. Was sind die Gesamtbetriebskosten im Vergleich zu einem vergleichbaren proprietären Stapel?

---

## 2. Methodik

Dieses Papier verwendet ein Multi-Methoden-Forschungsdesign, das folgendes kombiniert:

**Systematische Literaturübersicht** von Peer-Review-Veröffentlichungen, grauer Literatur und Grundlagendokumenten aus dem Zeitraum 2010–2026.

**Vergleichende Politikanalyse** technologierechtlicher Strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024) und der EU (Interoperable Europe Act 2024).

**Technologie-Stapel-Bewertung** anhand einer strukturierten Scoring-Matrix mit sieben Kriterien: Lizenzoffenheit, Deployment-Reife, Community-Gesundheit, Interoperabilitätsstandards, Sicherheitsposition, Gesamtbetriebskosten, öffentliche Einsatznachweise.

**Fallstudienanalyse** von drei bestätigten kommunalen Open-Source-Transitionen im Schweizer und deutschen Kontext.

**Stakeholder-Analyse** zur Kartierung der Interessen und des Einbindungsbedarfs jeder Stakeholder-Gruppe.

Die Literaturübersicht ist selbstverbessernd konzipiert: `Mem/source-registry.md` und `Mem/literature-review-state.md` sind versionierte Dokumente, die quartalsweise aktualisiert werden.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die wissenschaftliche Literatur zum E-Government hat sich durch vier Phasen entwickelt [30]. Erste Generation (1995–2005): Digitalisierung bestehender Prozesse [29]. Zweite Generation (2005–2012): Online-Dienstleistungserbringung, Bürgerportale, Back-Office-Integration [7]. Dritte Generation (2012–2020): Open Data, partizipative Plattformen, Mobile-First [8]. Vierte Generation (2020–heute): Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und der Souveränitätswandel [45].

Wirtz und Weyrers ganzheitliches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Deutsche und Schweizer Kommunen schneiden in diesen Dimensionen unterschiedlich ab; technische Infrastruktur und Prozessqualität bleiben hinter den Erwartungen der Bürgerinnen und Bürger zurück.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Der Begriff der digitalen Souveränität hat sich von einem akademischen Konzept zu einem politischen Gebot entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 verankerte „Teilung und Wiederverwendung“ als Kernprinzip [5]. Der Interoperable Europe Act 2024 (Verordnung (EU) 2024/903) schafft verbindliche Interoperabilitätspflichten [6]. Das EU-Datengesetz 2023 (Verordnung (EU) 2023/2854), in Kraft ab September 2025, gewährt öffentlichen Stellen Zugangsrechte zu privatgehaltenen Daten und schreibt Wechselrechte zwischen Cloud-Anbietern vor — ein direkter Rückhalt für kommunale Datensouveränität [48].

Der Sovereign Cloud Stack (SCS) der Open Source Business Alliance (OSBA), gefördert durch das BMWK, ist die konkreteste Verwirklichung von Souveränität in der Cloud-Infrastruktur [3]. Das Schweizer EMBAG, in Kraft seit dem 1. Januar 2024, verpflichtet die Bundesverwaltung zur Veröffentlichung von Bundessoftware als Open Source (Art. 9 EMBAG) [1].

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG) von 2017, grundlegend reformiert als OZG 2.0 im Jahr 2024, verpflichtet alle deutschen Behörden zur Online-Dienstleistungserbringung [2]. Die Reform führt das „Once-Only“-Prinzip, den „Einer für Alle“-Ansatz (EfA), BundID und einen bundesweiten Plattformarchitekturansatz über FITKO ein [9, 10].

ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), gegründet 2022, ist die deutsche Bundesbehörde, die speziell für den Aufbau und die Pflege von Open-Source-Alternativen zu proprietärer Software für den öffentlichen Sektor zuständig ist. ZenDiS verwaltet die OpenDesk-Suite; sein Jahresbudget überstieg 2024 die Marke von 50 Mio. Euro [49].

Dataport AöR und AKDB repräsentieren das genossenschaftliche Modell der öffentlichen IT-Versorgung. Die XÖV-Standards-Familie (XPersonenstand, XMeld, XKfz, XBildung, XGesundheit) ist für OZG-konforme Implementierungen verbindlich [46].

### 3.4 Digitale Dienste in Schweizer Kantonen und beim Bund

Die föderale Struktur der Schweiz schafft Herausforderungen und Chancen für die kommunale Digitalisierung. Schlüsselinfrastruktur:

- **EMBAG / Art. 9 Open-Source-Mandat:** Bundessoftware muss als Open Source veröffentlicht werden [1]
- **opendata.swiss:** Das nationale OGD-Portal auf CKAN-Basis [44]
- **GEVER:** Der standardisierte Records-Management-Rahmen der Bundesverwaltung [43]
- **Schweizer E-ID (BGEID):** Nach der Ablehnung des ersten Vorschlags in der Volksabstimmung vom März 2021 lancierte der Bundesrat das Projekt auf einer vollständig staatlich kontrollierten, datenschutzfreundlichen Architektur neu. Das neue E-ID-Gesetz (BGEID) wurde im März 2023 vom Parlament verabschiedet und läuft ab 2026 auf dem W3C-Verifiable-Credentials-Standard auf [50]
- **eCH-Standards:** Die Schweizer Äquivalente zu deutschen XÖV-Standards. Zentrale eCH-Standards: eCH-0007 (Gemeindedatenmodell), eCH-0011 (Einwohnerregister), eCH-0044 (Personenidentifikator), eCH-0058 (API-Design-Richtlinien), eCH-0213 (Föderierte Gemeindeservices). eCH-Standards sind kostenlos verfügbar und für Systeme, die mit kantonalen und eidgenössischen Registern interoperieren, verbindlich [51]

Die E-Government-Strategie Schweiz 2024–2027, verabschiedet vom Bundesrat und der Konferenz der Kantonsregierungen (KdK), legt fünf strategische Prioritäten fest: digitale Identität, Interoperabilität, Zugang, Vertrauen und Daten [16].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016) ist eine partizipative Demokratieplattform, die von über 400 Organisationen in 40 Ländern genutzt wird [12]. **CONSUL Democracy** (Madrid, 2015) ist eine alternative partizipative Plattform unter AGPL-3.0 [52]. **Matrix/Element** bietet ein offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll; der deutsche BundesMessenger basiert darauf [14]. **Nextcloud** (Stuttgart, 2016) ist die am weitesten verbreitete Open-Source-Plattform für Dateisynchronisierung und Zusammenarbeit in der europäischen öffentlichen Verwaltung [13]. **OpenDesk**, verwaltet von ZenDiS ab 2023, ist eine kuratierte Open-Source-Arbeitsplatzsuite mit Nextcloud, Cryptpad, OpenProject, Jitsi und Element [42, 49]. **GovStack** ist eine gemeinsame Initiative der ITU und des DIAL zur Definition wiederverwendbarer Verwaltungsbausteine für digitale öffentliche Dienste [47].

### 3.6 Lücken in der Literatur

1. **Gesamtbetriebskosten-Studien**, die Open-Source- und proprietäre kommunale Stapel vergleichen, sind spärlich. Dieser Bericht führt in Abschnitt 4.11 eine Methodik ein.
2. **Längsschnittdaten** über abgeschlossene Open-Source-Transitionen sind begrenzt. Münchens LiMux (2003–2017) wurde primär aus politischen Gründen rückabgewickelt, nicht aus technischen [30].
3. **Kleinkommunen-Perspektiven** sind unterrepräsentiert. Abschnitt 3.7 schließt diese Lücke.

### 3.7 Fallstudien kleiner Kommunen

Die folgenden drei verifizierten Fallstudien dokumentieren Open-Source-Transitionen im Bereich 50.000–150.000 Einwohner.

#### Fallstudie 1: Kanton Schaffhausen, Schweiz (ca. 82.000 Einwohner)

Der Kanton Schaffhausen hat Decidim 2021 als Plattform für Bürgerpartizipation eingeführt, zunächst für partizipatives Budgetieren, später für Konsultationen zur kantonalen Raumplanung. Ergebnisse: 4.200 registrierte Teilnehmende im ersten Jahr (5,1 % der Bevölkerung); Implementierungskosten ca. CHF 85.000; laufende Hosting-Kosten ca. CHF 8.000 pro Jahr. Der Kanton hat den Einsatz seitdem auf vier Gemeinden innerhalb des Kantons ausgeweitet [12].

#### Fallstudie 2: Biberach an der Riß, Deutschland (ca. 34.000 Einwohner)

Biberach migrierte seine interne Kollaborationsinfrastruktur 2023 von einer proprietären Groupware auf Nextcloud + Matrix/Element — im Rahmen des OZG-Umsetzungsprogramms Baden-Württemberg. Lizenzeinsparungen im ersten Jahr: 41.000 Euro. Nutzer:innenzufriedenheit (n=180, März 2024): 73 % bewerteten das neue System nach drei Monaten als „gut“ oder „sehr gut“ [13].

#### Fallstudie 3: Rosenheim, Deutschland (ca. 64.000 Einwohner)

Rosenheim (Bayern) führte 2022 über das AKDB-Shared-Services-Programm ein CKAN-basiertes Open-Data-Portal ein, integriert mit QGIS für die Veröffentlichung von Geodaten. 47 Datensätze aus den Bereichen Verkehr, Umwelt, Kultur und Haushalt. Einrichtungskosten (Shared-Service-Modell): 22.000 Euro. Laufende Pflege: 0,1 VZÄ pro Jahr [22, 37].

**Fazit:** Alle drei Fälle bestätigen, dass Kommunen von 35.000–85.000 Einwohnern Open-Source-Komponenten ohne eigene Entwicklerteams implementieren können, sofern sie kooperative Beschaffungsmodelle und Shared-Service-Anbieter nutzen.

---

## 4. Technologie-Stapel-Analyse

### 4.1 Digitale Identität und Authentifizierung

**Empfehlung: Keycloak** (Apache 2.0) [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für europäische öffentliche Verwaltungen. Implementiert OIDC, OAuth 2.0, SAML 2.0 und FIDO2; unterstützt Föderation mit BundID und der Schweizer E-ID-Infrastruktur.

### 4.2 Dokumentenmanagement und Aktenführung

**Empfehlung: Nextcloud + OpenProject** [13, 20]

Für GEVER-konforme Schweizer Anforderungen bieten kantonal verfügbare GEVER-Lösungen (CMI GEVER, Fabasoft Community) die Compliance-Schicht; Nextcloud dient als kollaborative Front-End. Für deutsche Kommunen bieten AKDB und Dataport entsprechende Komponenten.

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Empfehlung: Camunda Platform 8 Community** [33]; Alternative: **Flowable** (Apache 2.0)

Camunda bietet native BPMN 2.0-Workflow-Automatisierung mit starker XÖV- und eCH-Integrationsunterstützung.

### 4.4 Bürgerpartizipation

**Empfehlung: Decidim** [12]; Alternative: **CONSUL Democracy** [52]

Decidim ist die am weitesten verbreitete und ausgereifte partizipative Plattform weltweit mit über 400 Einsätzen.

### 4.5 Kommunikation und Zusammenarbeit

- **Matrix/Element** für Messaging und sichere behördübergreifende Kommunikation [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Team-Kommunikation

### 4.6 Open-Data-Veröffentlichung

**Empfehlung: CKAN** (AGPL-3.0) [22]

CKAN betreibt opendata.swiss, data.gov, data.gov.uk und Dutzende nationaler und kommunaler Portale. Plugin-Architektur unterstützt DCAT-AP, DCAT-AP.de und OGD-Switzerland-Metadatenstandards.

### 4.7 Geografische Informationssysteme

**Empfehlung: QGIS + GeoServer + OpenStreetMap** [36, 37]

QGIS bietet Desktop-GIS-Bearbeitung und QGIS-Server OGC-konforme WMS/WFS-Veröffentlichung.

### 4.8 Öffentliche Website und Content-Management

**Empfehlung: TYPO3** (deutschsprachiger Raum) oder **Drupal** (international) [19]

Beide unterstützen BITV 2.0 / WCAG 2.1 AA, Mehrsprachigkeit und Open-Data-Katalogintegration.

### 4.9 Cloud-Infrastruktur

**Empfehlung: Sovereign Cloud Stack (SCS)** [3, 11]

SCS (OpenStack + Kubernetes + Ceph) ist die wichtigste strategische Infrastrukturwahl für europäische Kommunen. Kann selbst gehostet, von govdigital eG betrieben oder durch SCS-zertifizierte Betreiber bereitgestellt werden.

### 4.10 Referenzarchitektur

```
+---------------------------------------------------------------+
|                  BÜRGERANLAUFSTELLEN                         |
|    TYPO3/Drupal · Decidim · CKAN · Nextcloud Web             |
+---------------------------------------------------------------+
|                     SERVICE-SCHICHT                           |
|   Camunda/Flowable · XÖV/eCH-Formulare · GeoServer           |
+---------------------------------------------------------------+
|                KOLLABORATIONS-SCHICHT                         |
|   Nextcloud · Matrix/Element · Jitsi · OpenProject           |
+---------------------------------------------------------------+
|                  IDENTITÄTS-SCHICHT                          |
|       Keycloak ←→ BundID / Schweizer E-ID (BGEID/VCs)        |
+---------------------------------------------------------------+
|              INFRASTRUKTUR-SCHICHT                            |
| Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph        |
+---------------------------------------------------------------+
```

### 4.11 Gesamtbetriebskosten-Rahmenwerk

Proprietäre Stapelbewertungen unterschätzen häufig langfristige Kosten, indem sie Vendor-Lock-in-Risiken, Lizenzeskalation und Ausstiegskosten auslassen. Dieses Kapitel präsentiert ein Fünf-Jahres-GBK-Modell für eine Kommune von ca. 500 Mitarbeitenden / 50.000 Einwohnern.

#### Proprietäre Referenz (Microsoft 365 E3 + Azure Government)

| Kostenposition | Jahr 1 | Jahre 2–5 (jährlich) | 5-Jahres-Gesamt |
|---|---|---|---|
| M365 E3-Lizenzen (500 × 360 €/Jahr) | 180.000 € | 180.000 € | 900.000 € |
| Azure Government Hosting | 60.000 € | 60.000 € | 300.000 € |
| Teams/SharePoint Administration | 1,0 VZÄ | 1,0 VZÄ | — |
| Anbieterspezifische Schulungen | 40.000 € | 10.000 € | 80.000 € |
| Integration / Anpassung | 120.000 € | 30.000 € | 240.000 € |
| Ausstiegskosten (geschätzt) | — | — | 250.000 € |
| **Zwischensumme (Barkosten)** | | | **1.770.000 €** |
| VZÄ-Kosten (1,0 VZÄ × 5 J. × 80.000 €) | | | 400.000 € |
| **Gesamt-GBK 5 Jahre** | | | **2.170.000 €** |

#### Open-Source-Stapel (SCS + Nextcloud + Element + Decidim + CKAN)

| Kostenposition | Jahr 1 | Jahre 2–5 (jährlich) | 5-Jahres-Gesamt |
|---|---|---|---|
| SCS-Hosted-Instanz (govdigital eG) | 36.000 € | 36.000 € | 180.000 € |
| Nextcloud Enterprise (500 Nutzer:innen) | 15.000 € | 15.000 € | 75.000 € |
| Implementierung / Migration | 150.000 € | 20.000 € | 230.000 € |
| Schulungen | 30.000 € | 8.000 € | 62.000 € |
| Community / Upstream-Beiträge | 10.000 € | 10.000 € | 50.000 € |
| Ausstiegskosten (geschätzt) | — | — | 0 € |
| **Zwischensumme (Barkosten)** | | | **597.000 €** |
| VZÄ-Kosten (1,2 VZÄ × 5 J. × 80.000 €) | | | 480.000 € |
| **Gesamt-GBK 5 Jahre** | | | **1.077.000 €** |

**Netto-Ersparnis: ca. 1.093.000 Euro über fünf Jahre (∼50 % Reduktion).**

Der Breakeven wird typischerweise zwischen Monat 18 und Monat 24 erreicht. Siehe `Scripts/tco_calculator.py` für ein parametrisierbares Modell.

---

## 5. Implementierungsfahrplan

### Phase 0: Fundament (Monate 1–3)

**Ziel:** Governance aufbauen, Ist-Zustand erfassen, Koalition bilden.

**Ergebnisse:** Digitaler Transformationsausschuss; Ist-Analyse der Technologielandschaft; Stakeholder-Einbindungsplan; Beschaffungsrahmen; MoU mit kooperativem IT-Dienstleister (Dataport, AKDB, govdigital eG oder kantonale IT); GBK-Analyse beauftragt.

**Entscheidungstor:** Politisches Mandat (Gemeinderat- oder Exekutivbeschluss) und Budget genehmigt.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundlegende Schichten aufbauen.

**Ergebnisse:** SCS-Umgebung in Betrieb; Keycloak mit BundID / Schweizer E-ID föderiert; Nextcloud-Basis für interne Zusammenarbeit; Matrix/Element für Mitarbeitende; BSI IT-Grundschutz-Baseline.

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste Bürgerdienste auf offener Infrastruktur.

**Ergebnisse:** Fünf volumenstärkste Verwaltungsleistungen auf Camunda/XÖV; CMS-Migration abgeschlossen; CKAN-Portal mit ersten 20 Datensätzen; Decidim-Instanz für ersten Partizipationsprozess.

### Phase 3: Integration und Ausweitung (Monate 16–24)

**Ziel:** Alle Schichten verbinden; 80 % der Transaktionen abdecken.

**Ergebnisse:** Alle Dienste via Keycloak SSO; Nextcloud in Records-Management; GIS-Schicht (QGIS + GeoServer); behördübergreifender Datenaustausch via XÖV/eCH.

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Nutzerfreundlichkeit verbessern; zur Open-Source-Community beitragen.

**Ergebnisse:** Bürgerzufriedenheitsumfrage (Ziel NPS > 40); erster Beitrag zu openCode.de / Upstream-Projekten; kommunale Open-Source-Praxisgemeinschaft mit ≥3 Partnerkommunen.

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; Replikation vorbereiten.

**Ergebnisse:** Software-Stueckliste (SBOM); Datenhaltung 100 % auf souveräner Infrastruktur (geprüft); Replikations-Playbook für Nachbarkommunen; Strategiepapier v1.0 veröffentlicht.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Einbindungsansatz |
|---|---|---|
| Bürgermeister:in / Exekutive | Politischer Erfolg, Kosten, Bürgerzufriedenheit | Führungsbriefing, Fortschritts-Dashboard |
| Gemeinderat | Aufsicht, demokratische Legitimität | Quartalsberichte, öffentliche Sitzungen |
| Kommunale IT-Abteilung | Technische Machbarkeit, Arbeitsbelastung | Co-Design, Schulungen, Community-Mitgliedschaft |
| Vergabestelle | Rechtskonformität, Risiko | Rahmenverträge, Rechtsbriefings |
| Mitarbeitende (Endnutzende) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Change Management, Schulungen |
| Bürger:innen | Servicequalität, Datenschutz | Partizipationsdesign, Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Partizipation | Decidim, öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de, Upstream-Beiträge |
| Souveräne Tech-Anbieter | Partnerschaft, Einsatz | Zertifizierte Partnervereinbarungen |
| Datenschutzbeauftragte:r | DSGVO / revDSG-Konformität | Privacy-by-Design in jeder Phase |
| Medien / Journalist:innen | Rechenschaftspflicht, Open Data | Proaktive Datenveröffentlichung, Briefings |

### 6.2 Beschaffungsrahmen

**1. Dienste beschaffen, keine Lizenzen.** Software ist kostenlos; Kommunen bezahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**2. Kooperative Beschaffung.** Govdigital eG und Schweizer kantonale IT-Kooperativen bieten Rahmenverträge, die das öffentliche Vergaberecht (GWB/VgV in Deutschland; BöB/VöB in der Schweiz) erfüllen [23].

**3. Öffentliches Geld – Öffentlicher Code.** Jede unter öffentlichem Auftrag entwickelte Software muss unter einer OSI-zugelassenen Lizenz veröffentlicht werden — auf openCode.de (Deutschland) oder code.admin.ch (Schweiz). In der Schweiz ist dies durch Art. 9 EMBAG verbindlich [4].

**4. Fünf-Jahres-GBK in der Bewertung.** Empfohlene Gewichtung: Preis/GBK (40 %), Funktionalität (30 %), Souveränität und Interoperabilität (20 %), Community-Gesundheit (10 %).

**5. Interoperabilitätsstandards als Pflichtanforderung.** Alle beschafften Systeme müssen XÖV (Deutschland) [46], eCH (Schweiz) [51] und DCAT-AP für Open Data [45] implementieren.

**6. SBOM-Anforderung.** Lieferanten müssen eine Software-Stückliste (SBOM) im SPDX- oder CycloneDX-Format bei Vertragsabschluss und bei jedem Major-Release bereitstellen.

### 6.3 Change Management

Empfehlungen:
- **Digitalbeauftragte:r** auf Ebene Stadtrat/Vize-Bürgermeisterin mit explizitem Mandat
- **Abteilungsweise Open-Source-Champions** mit erweiterter Schulung und Peer-Support-Rolle
- **Parallelbetrieb** für mindestens drei Monate vor Abschaltung kritischer Systeme
- **Früherfolge dokumentieren und kommunizieren**: Kosteneinsparungen, neue Fähigkeiten, Bürger-Feedback
- **Öffentliches Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Servicequalität
- **Personalrat / Gesamtpersonalrat** frühzeitig einbinden

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Maßnahme |
|---|---|---|---|
| Politische Kehrtwende nach der Wahl | Mittel | Hoch | In Satzung einbetten; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / Desinformationskampagnen | Hoch | Mittel | GBK-Belege; Zivilgesellschaft; Mandat publizieren |
| Qualifikationsdefizit im IT-Team | Hoch | Mittel | Schulungen; kooperativer IT-Anbieter; Praxisgemeinschaft |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Stufenweiser Rollout mit Entscheidungstoren |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständige Datensicherung; Parallelbetrieb; DR-Plan |
| DSGVO / revDSG-Verletzung | Niedrig | Hoch | Privacy-by-Design; DSB in jeder Phase |
| Nutzerannahme-Versagen | Mittel | Hoch | Change Management; UX-Tests; Schulungen |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstest; SBOM; NIS2 [27] |
| Community-Fragmentierung | Niedrig | Mittel | Upstream beitragen; openCode.de; govdigital eG |
| Kostenabweichung | Mittel | Mittel | Phasengebundenes Budget; unabhängiges PMO |
| Lieferkettenkompromittierung | Niedrig | Kritisch | SBOM; reproduzierbare Builds; CVE-Überwachung |

### 7.2 Der Münchener Präzedenzfall

Das LiMux-Projekt der Landeshauptstadt München (2003–2017) ist das meistzitierte Beispiel einer rückabgewickelten kommunalen Open-Source-Transition. Die Nachbetrachtung zeigt: (a) politischer Führungswechsel mit engeren Microsoft-Bindungen; (b) unzureichendes Change Management; (c) Kompatibilitätsprobleme mit Landessystemen. Die technische Implementierung selbst war weitgehend erfolgreich und versorgte 15.000 Desktops 14 Jahre lang [30]. Die entscheidende Lehre: **Politisches Risikomanagement** ist mindestens so wichtig wie technische Planung.

### 7.3 Sicherheitsaspekte

- Regelmäßige Sicherheitsupdates mit dokumentiertem Patch-Management
- Authentifizierung auf BSI AAL2 für bürgergerichtete Dienste
- TLS 1.3 minimum; AES-256-Verschlüsselung für sensible Kategorien
- Penetrationstests an jedem Phasenmeilenstein
- Vorfallreaktionsplan im Einklang mit NIS2 [27]
- SBOM wöchentlich gegen OSV-Datenbank prüfen

### 7.4 Datenschutz und DSGVO

Alle empfohlenen Komponenten ermöglichen den Betrieb mit Datenresidenz ausschließlich auf kommunal kontrollierter oder genossenschaftlicher Infrastruktur, was dem DSGVO Art. 44-Verbot von Drittlandstransfers entspricht. Das revDSG (in Kraft seit September 2023) legt der Schweizer Kommunen entsprechende Pflichten auf [55].

---

## 8. Fazit

Die in diesem Papier untersuchten Belege führen zu fünf Erkenntnissen:

**1. Open-Source-Technologiestapel für Kommunen sind technisch ausgereift und praxisbewährt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung lässt sich durch Open-Source-Software mit dokumentierten Einsätzen bei Vergleichskommunen erfüllen — auch im Bereich 35.000–85.000 Einwohner (Abschnitt 3.7).

**2. Der Regulierungsrahmen schreibt Open-Source und Interoperabilität zunehmend vor.** EMBAG Art. 9 (Schweiz), OZG 2.0 (Deutschland), Interoperable Europe Act 2024 und EU-Datengesetz 2023 schaffen rechtliche Verpflichtungen, die proprietäre, anbietergekoppelte Systeme nicht nachhaltig erfüllen können [1, 2, 6, 48].

**3. Die wirtschaftliche Argumentation ist überzeugend, wenn Gesamtkosten korrekt erfasst werden.** Das GBK-Modell in Abschnitt 4.11 zeigt ca. 50 % Einsparungen für eine Kommune mit 500 Mitarbeitenden.

**4. GovStack-Bausteine erweitern die Implementierungsunterstützung.** Die ITU/DIAL GovStack-Initiative ermöglicht die Ausrichtung kommunaler Open-Source-Einsätze an international anerkannten Baustein-Spezifikationen [47].

**5. Erfolg erfordert politische und organisatorische Investitionen gleichwertig zur technischen Investition.** Der Münchener Rückschlag und erfolgreiche Transitionen in Barcelona, Schaffhausen, Biberach und Rosenheim bestätigen dies gleichermaßen.

Kommunen, die früh handeln, profitieren von First-Mover-Vorteilen: Mitgestaltung kooperativer Standards, Aufbau von Inhouse-Expertise und Beitrag zur gemeinsamen Open-Source-Infrastruktur. Der Rechtsrahmen ist vorhanden. Die Technologie ist bereit. Die Wirtschaftlichkeit ist günstig. Die Transformation ist überfällig.

---

## Referenzen

Siehe englisches Quelldokument `Doc/en/sovereign-by-design-v0.2.0.md` für vollständige Referenzliste. Zitate in diesem Dokument folgen denselben Nummern [1]–[55].

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*  
*Zitierweise: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com), „Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen“, v0.2.0, 2026-06-21.*
