---
title: "Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.3.0"
status: "Erweiterter Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
translation-of: "Doc/en/sovereign-by-design-v0.3.0.md"
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
  - GovStack
  - EU KI-Gesetz
  - GAIA-X
---

# Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Kontakt:** sebk4c@tuta.com  
**Version:** 0.3.0 — Erweiterter Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (diese Übersetzung) · English (Quelldokument)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Änderungen gegenüber v0.2.0:* Neuer Abschnitt 3.8 (Europäische Open-Source-Adoptionstrends — OSOR-Jahresbericht 2023 [54]). Neuer Abschnitt 4.12 (GovStack-Bausteine: Formales Compliance-Mapping gegen GovStack Spec v1.0 [56]). Neuer Abschnitt 4.13 (KI-Governance — EU KI-Gesetz 2024, kommunaler Compliance-Rahmen [60]). Abschnitt 6.2 erweitert (AKDB-Kooperationsmodell detailliert [57]). Neuer Abschnitt 7.5 (GAIA-X als europäische Cloud-Vertrauensschicht [59]). Abschnitt 3.1 ergänzt (Lathrop & Ruma — „Government as a Platform“ [58]). Quellenregister auf 53 Primäreinträge erweitert. Fazit um zwei neue Erkenntnisse ergänzt.

---

## Zusammenfassung

Kommunalverwaltungen sind die demokratisch bürgernächste Ebene staatlichen Handelns, stehen jedoch vor einer gravierenden strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, anbietergekoppelt und im Widerspruch zu gemeinwohlorientierten Werten. Dieses Papier präsentiert eine umfassende, zitationsvollständige Strategie für die Implementierung eines modernen Open-Source-Technologiestapels in Kommunalverwaltungen. Auf Grundlage bewährter Ansätze aus dem Schweizer Bundesrecht (EMBAG), dem deutschen OZG-Reformprogramm, der Sovereign-Cloud-Stack-Initiative, dem ITU/DIAL GovStack-Rahmenwerk und der europäischen Gemeinschaft für souveräne Technologie leiten wir einen grundlagenorientierten Implementierungsfahrplan, einen Stakeholder-Einbindungsrahmen, eine Beschaffungsstrategie und ein Gesamtbetriebskosten-Modell ab. Drei verifizierte Fallstudien kleiner Kommunen (Kanton Schaffhausen CH, Biberach DE und Rosenheim DE) belegen, dass der Ansatz auch für Kommunen von 50.000–150.000 Einwohnern ohne große Inhouse-IT-Abteilungen realisierbar ist. Wir kommen zu dem Schluss, dass Open-Source-Technologiestapel für Kommunen nicht nur technisch ausgereift, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Rechtsordnungen gesetzlich vorgeschrieben sind.

v0.3.0-Erweiterungen vertiefen die Analyse in vier Richtungen: (1) formales GovStack-Spec-v1.0-Bausteine-Compliance-Mapping, das zeigt, dass der Stapel in sieben von neun Bausteinen volle oder substanzielle Konformität erreicht; (2) kommunaler Compliance-Rahmen für das EU KI-Gesetz (Verordnung (EU) 2024/1689), der automatisierte Sozialleistungsentscheidungen als primäre Hochrisiko-KI-Kategorie für Kommunen identifiziert; (3) Positionierung von GAIA-X als aufkommende europäische Cloud-Vertrauensschicht als Komplement zur SCS-Infrastrukturempfehlung; und (4) europäische Open-Source-Adoptionstrends aus dem OSOR-Jahresbericht 2023 der EU. Quellenregister umfasst nun 53 verifizierte Primäreinträge.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Gesamtbetriebskosten, GovStack, EU KI-Gesetz, GAIA-X

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen; Regulierungsbehörden fordern Interoperabilität und Datenschutz; und fiskalischer Druck verlangt nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte weltweit gefangen in einem Zyklus aus proprietärer Anbieterabhängigkeit, teuren Lizenzverträgen und fragmentierten Systemen, die gute Verwaltungsführung eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut dokumentiert: Vendor-Lock-in erhöht Wechselkosten und Verhandlungsasymmetrien [4]; proprietäre Formate behindern ämterübergreifenden Datenaustausch und Transparenz [45]; geschlossene Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Haushalte, die ansonsten der Daseinsvorsorge zugute kämen [3, 5]. Am grundlegendsten: Wenn Software, die demokratische Institutionen betreibt, von privaten Akteuren kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Interesse und Unternehmensimperativen [4].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG von 2023 verpflichtet dazu, mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source zu veröffentlichen [1]. Deutschlands OZG 2.0, Sovereign Cloud Stack und OpenDesk-Initiative stellen das ambitionierteste Open-Source-Regierungstechnologieprogramm Europas dar [2, 3, 42]. Die GovStack-Initiative von ITU und DIAL bietet ein globales Rahmenwerk wiederverwendbarer Verwaltungsbausteine [47]. Die Kampagne „Öffentliches Geld? Öffentlicher Code!“ der FSFE, unterstützt von über 200 Organisationen in 30 Ländern, formuliert das demokratische Prinzip [4].

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und kommunale Behörden, einschließlich Gemeinden, Kommunen, Städte und äquivalente Strukturen in Schweizer Kantonen. Die Strategie skaliert von Kleinkommunen (5.000–50.000 Einwohner) bis Großstädten (500.000+).

*Open-Source-Technologiestapel* bezeichnet Softwarekomponenten, die unter OSI-zugelassenen Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder ohne unzumutbare Kosten migrieren kann.

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

Die Literaturübersicht ist selbstverbessernd konzipiert: `Mem/source-registry.md` und `Mem/literature-review-state.md` sind versionierte Dokumente, die quartalsweise aktualisiert werden. `Scripts/update_literature_review.py` stellt den strukturierten Quartals-Review-Workflow bereit.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in der öffentlichen Verwaltung behandeln; (b) staatliche Digitaltransformationsstrategie behandeln; (c) den europäischen, schweizerischen oder deutschen Regulierungskontext betreffen; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern.

### 2.2 Einschränkungen

Alle Zitate in diesem Entwurf v0.3.0 wurden gegen Primärquellen verifiziert, sofern nicht ausdrücklich anders angegeben. Technologiebewertungen spiegeln öffentlich verfügbare Informationen zum Stand Juni 2026 wider.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die wissenschaftliche Literatur zum E-Government hat sich durch vier Phasen entwickelt [30]. Erste Generation (1995–2005): Digitalisierung bestehender Prozesse [29]. Zweite Generation (2005–2012): Online-Dienstleistungserbringung, Bürgerportale, Back-Office-Integration [7]. Dritte Generation (2012–2020): Open Data, partizipative Plattformen, Mobile-First [8]. Vierte Generation (2020–heute): Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und der Souveränitätswandel [45].

Wirtz und Weyrers ganzheitliches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Deutsche und Schweizer Kommunen schneiden in diesen Dimensionen unterschiedlich ab; technische Infrastruktur und Prozessqualität bleiben hinter den Erwartungen der Bürgerinnen und Bürger zurück.

Janowskis Viergenerationen-Evolutionsrahmen bietet eine komplementäre Perspektive: von Substitution über Transformation, Engagement bis zur Kontextualisierung [30]. Die meisten Schweizer und deutschen Kommunen befinden sich im Übergang von Transformation zu Engagement — ein günstiger Moment für eine Open-Source-Stapel-Transition.

Lathrop und Rumas grundlegendes Sammelwerk [58] etablierte das „Government as a Platform“-Paradigma: den Vorschlag, dass der Staat offene Dateninfrastruktur und APIs bereitstellen soll, auf deren Basis Bürgerinnen, Unternehmen und Behörden Dienste aufbauen können. Tim O'Reillys Beitrag zu diesem Band argumentierte, dass das Wertvollste, was der Staat tun kann, darin besteht, seine Daten und Prozesse offen verfügbar zu machen — um ein Gemeingut bürgerlicher Dienste zu ermöglichen statt eines monolithischen Portals. Dieses Prinzip antizipiert direkt den Baustein-Architekturansatz des GovStack [47] und die Datenteilungspflichten des EU-Datengesetzes [48]. EMBAG Art. 9 kann als gesetzlicher Ausdruck desselben Prinzips auf Software gelesen werden.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Der Begriff der digitalen Souveränität hat sich von einem akademischen Konzept zu einem politischen Gebot entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 verankerte „Teilung und Wiederverwendung“ als Kernprinzip [5]. Der Interoperable Europe Act 2024 (Verordnung (EU) 2024/903) schafft verbindliche Interoperabilitätspflichten [6]. Das EU-Datengesetz 2023 (Verordnung (EU) 2023/2854), in Kraft ab September 2025, gewährt öffentlichen Stellen Zugangsrechte zu privatgehaltenen Daten und schreibt Wechselrechte zwischen Cloud-Anbietern vor — ein direkter Rükhalt für kommunale Datensouveränität [48].

Der Sovereign Cloud Stack (SCS) der OSBA, gefördert durch das BMWK, ist die konkreteste Verwirklichung von Souveränität in der Cloud-Infrastruktur [3]. Das Schweizer EMBAG, in Kraft seit dem 1. Januar 2024, verpflichtet die Bundesverwaltung zur Veröffentlichung von Bundessoftware als Open Source (Art. 9 EMBAG) [1].

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG) von 2017, grundlegend reformiert als OZG 2.0 im Jahr 2024, verpflichtet alle deutschen Behörden zur Online-Dienstleistungserbringung [2]. Die Reform führt das „Once-Only“-Prinzip, den „Einer für Alle“-Ansatz (EfA), BundID und einen bundesweiten Plattformarchitekturansatz über FITKO ein [9, 10].

ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), gegründet 2022, ist die deutsche Bundesbehörde für Open-Source-Alternativen zu proprietärer Software. ZenDiS verwaltet die OpenDesk-Suite; sein Jahresbudget überstieg 2024 die Marke von 50 Mio. Euro [49]. Dataport AöR und AKDB repräsentieren das genossenschaftliche Modell der öffentlichen IT-Versorgung [24, 57]. Die XÖV-Standards-Familie ist für OZG-konforme Implementierungen verbindlich [46].

### 3.4 Digitale Dienste in Schweizer Kantonen und beim Bund

Schlüsselinfrastruktur der Schweiz:
- **EMBAG / Art. 9:** Bundessoftware muss als Open Source veröffentlicht werden [1]
- **opendata.swiss:** Nationales OGD-Portal auf CKAN-Basis [44]
- **GEVER:** Standardisiertes Records-Management [43]
- **Schweizer E-ID (BGEID):** W3C-Verifiable-Credentials-Basis, Einführung ab 2026 [50]
- **eCH-Standards:** Schweizer Äquivalent zu XÖV (eCH-0007, eCH-0011, eCH-0044, eCH-0058, eCH-0213) [51]

Die E-Government-Strategie Schweiz 2024–2027 mandatiert offene Standards und anbieter-neutrale Schnittstellen für alle digitalen öffentlichen Dienste [16].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (400+ Einsätze, u. a. Kanton Schaffhausen) [12]. **CONSUL Democracy** (Alternative, stärker in Süd- und Lateinamerika verbreitet) [52]. **Matrix/Element** (BundesMessenger, Tchap FR, UK MoD) [14]. **Nextcloud** (schweizweit, EU-Institutionen) [13]. **OpenDesk** von ZenDiS: produktionsreif für die Bundesverwaltung seit 2024 [42, 49]. **GovStack** (ITU/DIAL): globale Bausteinspezifikationen [47, 56].

### 3.6 Lücken in der Literatur

1. **Gesamtbetriebskosten-Studien** — Methodik in Abschnitt 4.11 eingeführt; DINUM-Studie [53] bleibt rigoroseste verfügbare Quelle.
2. **Längsschnittdaten** — Drei v0.2.0-Fallstudien als Erstdokumentationen; Jahr-2-Daten für v1.0 angestrebt.
3. **Kleinkommunen-Perspektiven** — Abschnitt 3.7 schließt diese Lücke mit drei verifizierten Fallstudien.
4. **Nutzerzufriedenheitsforschung** — Kaum peer-reviewte Literatur verfügbar; Erhebungsrahmen-Design für v1.0 vorgesehen.
5. *(In v0.3.0 adressiert)* **GovStack-Compliance-Mapping** — formales Assessment in Abschnitt 4.12.
6. *(In v0.3.0 adressiert)* **EU KI-Gesetz kommunale Auswirkungen** — Compliance-Rahmen in Abschnitt 4.13.

### 3.7 Fallstudien kleiner Kommunen

#### Fallstudie 1: Kanton Schaffhausen, Schweiz (ca. 82.000 Einwohner)

Decidim-Einführung 2021 für partizipatives Budgetieren und Raumplanung. Ergebnisse: 4.200 registrierte Teilnehmende (5,1 % der Bevölkerung); Implementierungskosten ca. CHF 85.000; laufende Hosting-Kosten ca. CHF 8.000/Jahr. Seitdem Ausweitung auf vier Gemeinden [12].

#### Fallstudie 2: Biberach an der Riß, Deutschland (ca. 34.000 Einwohner)

Migration von proprietärer Groupware auf Nextcloud + Matrix/Element 2023 (OZG-Programm BW). Lizenzeinsparungen Jahr 1: 41.000 €. Nutzerzufriedenheit (n=180, März 2024): 73 % gut/sehr gut nach drei Monaten [13].

#### Fallstudie 3: Rosenheim, Deutschland (ca. 64.000 Einwohner)

CKAN-Open-Data-Portal 2022 über AKDB-Shared-Services-Programm, integriert mit QGIS. 47 Datensätze. Einrichtungskosten (Shared-Service-Modell): 22.000 €. Pflege: 0,1 VZÄ/Jahr. Erstes maschinenlesbares Jahresbudget veröffentlicht Januar 2023 [22, 37, 57].

**Fazit:** Alle drei Fälle bestätigen die Realisierbarkeit ohne eigene Entwicklerteams bei Nutzung kooperativer Beschaffungsmodelle.

### 3.8 Europäische Open-Source-Adoptionstrends

Das EU Open Source Observatory (OSOR), betrieben über die Joinup-Plattform der Europäischen Kommission, veröffentlicht Jahresberichte zu Open-Source-Adoptionstrends in EU-Mitgliedstaaten. Der OSOR-Jahresbericht 2023 dokumentiert einen beschleunigenden Trend, angetrieben durch drei konvergierende Faktoren: (1) der Interoperable Europe Act schafft regulatorischen Zug in Richtung offener Standards; (2) NIS2 und Cybersicherheitsanforderungen fördern prüfbaren, transparenten Code; (3) steigende proprietäre Lizenzkosten in Verbindung mit Cloud-Repatriierungsdruck infolge Schrems-II-Durchsetzung und DSGVO-Prüfung von US-Cloud-Datenverarbeitung [54].

**Zentrale OSOR-2023-Befunde für die kommunale Strategie:**

- **Open-Source-Politiken** existieren in 17 von 27 EU-Mitgliedstaaten; die Zahl mit aktiven Durchsetzungsmechanismen ist von 8 (2019) auf 14 (2023) gestiegen.
- **Kooperative Beschaffungsrahmen** für Open-Source-Dienste bestehen in mindestens 12 Mitgliedstaaten — dies bestätigt das govdigital-eG-/Kantonskoo-perationsmodell aus Abschnitt 6.2.
- **Deutschland und Frankreich** sind führend beim Einsatz von Open-Source-Software in internen Verwaltungstools; die Schweiz nimmt durch EMBAG eine einzigartige regulatorische Position ein.
- **Häufigste Barrieren** sind Beschaffungskompetenzlücken und Change-Management-Herausforderungen — dies bestätigt die Analyse in Abschnitten 5.3 und 6.3.
- **Nordische Länder** zeigen hohe Open-Data-Adoption (CKAN/DCAT), aber niedrigere OSS-Einsatzraten für interne Werkzeuge.

Die Joinup-Plattform der OSOR dient als EU-Niveau-Äquivalent zu Deutschlands openCode.de: ein Katalog mit über 5.000 wiederverwendbaren Lösungen von öffentlichen Verwaltungen. Kommunen sollten ihre Open-Source-Einsätze auf Joinup registrieren, um zum europäischen Gemeingut beizutragen.

---

## 4. Technologie-Stapel-Analyse

Der kommunale Technologiestapel lässt sich in neun Funktionsschichten plus Gesamtbetriebskosten-Analyse, GovStack-Compliance-Mapping und KI-Governance-Schicht untergliedern.

### 4.1 Digitale Identität und Authentifizierung

**Empfehlung: Keycloak** (Apache 2.0) [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für europäische öffentliche Verwaltungen (OIDC, OAuth 2.0, SAML 2.0, FIDO2). Föderation mit BundID und Schweizer E-ID-Infrastruktur unterstützt.

### 4.2 Dokumentenmanagement und Aktenführung

**Empfehlung: Nextcloud + OpenProject** [13, 20]

Für GEVER-konforme Schweizer Anforderungen bieten kantonal verfügbare GEVER-Lösungen die Compliance-Schicht; Nextcloud als kollaboratives Front-End. Für deutsche Kommunen: AKDB- und Dataport-Komponenten.

### 4.3 Workflow-Automatisierung

**Empfehlung: Camunda Platform 8 Community** [33]; Alternative: **Flowable** (Apache 2.0)

Native BPMN 2.0-Workflow-Automatisierung mit starker XÖV- und eCH-Integrationsunterstützung.

### 4.4 Bürgerpartizipation

**Empfehlung: Decidim** [12]; Alternative: **CONSUL Democracy** [52]

400+ Einsätze weltweit; CONSUL als Alternative für einfachere Erstimplementierung.

### 4.5 Kommunikation und Zusammenarbeit

- **Matrix/Element** für Messaging und sichere behördübergreifende Kommunikation [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Team-Kommunikation

### 4.6 Open-Data-Veröffentlichung

**Empfehlung: CKAN** (AGPL-3.0) [22]

Betreibt opendata.swiss, data.gov, data.gov.uk. Unterstützt DCAT-AP, DCAT-AP.de, OGD Switzerland.

### 4.7 Geografische Informationssysteme

**Empfehlung: QGIS + GeoServer + OpenStreetMap** [36, 37]

QGIS: Desktop-GIS; QGIS-Server: OGC-konforme WMS/WFS-Veröffentlichung; GeoServer: erweiterte Publikation.

### 4.8 Öffentliche Website und Content-Management

**Empfehlung: TYPO3** (deutschsprachiger Raum) oder **Drupal** (international) [19]

Beide unterstützen BITV 2.0 / WCAG 2.1 AA, Mehrsprachigkeit und Open-Data-Katalogintegration.

### 4.9 Cloud-Infrastruktur

**Empfehlung: Sovereign Cloud Stack (SCS)** [3, 11]

SCS (OpenStack + Kubernetes + Ceph) ist die wichtigste strategische Infrastrukturwahl für europäische Kommunen. GAIA-X-konform (siehe Abschnitt 7.5).

### 4.10 Referenzarchitektur

```
+---------------------------------------------------------------+
|               BÜRGERANLAUFSTELLEN                            |
|  TYPO3/Drupal · Decidim · CKAN · Nextcloud Web               |
+---------------------------------------------------------------+
|                  SERVICE-SCHICHT                              |
|  Camunda/Flowable · XÖV/eCH-Formulare · GeoServer           |
+---------------------------------------------------------------+
|             KOLLABORATIONS-SCHICHT                            |
|  Nextcloud · Matrix/Element · Jitsi · OpenProject · Talk    |
+---------------------------------------------------------------+
|              IDENTITÄTS-SCHICHT                              |
|    Keycloak ←→ BundID / Schweizer E-ID (BGEID/VCs)           |
+---------------------------------------------------------------+
|            INFRASTRUKTUR-SCHICHT                              |
| Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph       |
+---------------------------------------------------------------+
         ↕ GAIA-X Trust Framework ↕
```

### 4.11 Gesamtbetriebskosten-Rahmenwerk

Dieses Kapitel präsentiert ein Fünf-Jahres-GBK-Modell für eine Kommune von ca. 500 Mitarbeitenden / 50.000 Einwohnern.

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

### 4.12 GovStack-Bausteine: Compliance-Mapping

Dieses Kapitel liefert eine formale Compliance-Bewertung des empfohlenen Stapels gegenüber den GovStack-Spec-v1.0-Baustein-Definitionen [56]. GovStack definiert neun Grundbausteine; die Tabelle bildet jeden Baustein auf die empfohlene Komponente ab und bewertet den Erfüllungsgrad.

**Legende:** ✓ Volle Konformität · ◑ Substanzielle Konformität · ◔ Partielle Konformität · ✗ Nicht implementiert

| GovStack-Baustein | Spec-Referenz | Empfohlene Komponente | Konformität | Lücke / Maßnahme |
|---|---|---|---|---|
| Identität und Authentifizierung | BB-ID §4.1 | Keycloak (OIDC/OAuth2/FIDO2) + BundID/BGEID | ✓ Voll | — |
| Sicherheit | BB-Security §4.2 | Keycloak + BSI IT-Grundschutz-Baseline | ◑ Substanziell | Hardware-Sicherheitstoken (AAL3) optional |
| Einwilligungsmanagement | BB-Consent §4.3 | Keycloak Consent + Nextcloud Datenschutz-Dashboard | ◔ Partiell | Vollständiges Consent-Audit-Log erfordert Individualentwicklung (v1.0-Ziel) |
| Digitale Register | BB-DReg §4.4 | CKAN (offene Datenregister) | ◔ Partiell | Geschäfts-/Rechtsregister außerhalb CKAN-Scope; kantonale Register-APIs benötigt |
| Informationsvermittler | BB-InfoMed §4.5 | Camunda/Flowable + XÖV/eCH-Adapter | ◑ Substanziell | X-Road-ähnlicher Broker nicht nativ; XÖV/eCH deckt DE/CH-Kontext ab |
| Messaging | BB-Msg §4.6 | Matrix/Element | ◔ Partiell | SMS/Push-Benachrichtigungs-Gateway für bürgergerichtete Alarme erforderlich |
| Zahlungen | BB-Pay §4.7 | Nicht im aktuellen Stapel | ✗ Keine | Lücke kommunale Gebührenzahlung; PaymentHub EE oder Kantons-/Länderzahlungsgateway empfohlen für v1.0 |
| Terminplanung | BB-Sched §4.8 | OpenProject | ◔ Partiell | OpenProject deckt Mitarbeitendenplanung; bürgerseitige Terminbuchung nicht implementiert |
| Registrierung | BB-Reg §4.9 | Camunda/Flowable + XÖV/eCH-Formulare | ◑ Substanziell | GovStack-REST-API-Spec-Ausrichtung erforderlich; funktionale Abdeckung vollständig |

**Zusammenfassung:** Der empfohlene Stapel erreicht volle Konformität mit dem Identitätsbaustein und substanzielle Konformität bei Sicherheit, Informationsvermittler und Registrierung. Die drei partiell-konformen Bausteine (Einwilligung, Digitale Register, Messaging) erfordern Ergänzungskomponenten für volle GovStack-API-Kompatibilität. Der Zahlungsbaustein ist die bedeutendste funktionale Lücke.

**Empfohlene Maßnahmen für v1.0:**
1. Zahlungskomponente integrieren (PaymentHub EE oder kantonales/Länder-Zahlungsgateway)
2. Matrix-Deployment um SMS-Gateway erweitern für bürgergerichtete Benachrichtigungen
3. Einwilligungsmanagement-Microservice mit persistentem Audit-Log entwickeln
4. Formalen GovStack-API-Konformitätstest-Bericht für Identitätsbaustein veröffentlichen

### 4.13 Governance für Künstliche Intelligenz

Verordnung (EU) 2024/1689 (KI-Gesetz / AI Act) [60], in Kraft ab 1. August 2024 mit gestaffelter Anwendbarkeit bis 2027, schafft einen risikobasierten Rahmen für KI-Systeme mit direkten Auswirkungen auf kommunale Technologiebeschaffung, -einsatz und -dienstleistungserbringung.

#### 4.13.1 KI-Risikoklassen mit Relevanz für Kommunalverwaltungen

**Verbotene KI (Art. 5):** Soziale Bewertungssysteme („Social Scoring“) von Behörden sind ausdrücklich verboten. Kommunen dürfen keine KI-Systeme einsetzen, die das soziale Verhalten von Bürgerinnen und Bürgern in einer Weise bewerten, die nachteilige soziale Folgen erzeugt. Dieses Verbot ist sofortig und bedingungslos.

**Hochrisiko-KI (Anhang III):** Mehrere für Kommunen relevante KI-Anwendungen fallen unter die Hochrisiko-Kategorie, die eine Konformitätsbewertung vor der Inbetriebnahme erfordert:

| Anwendung | Anhang-III-Referenz | Kommunaler Kontext |
|---|---|---|
| Automatisierte Sozialleistungsentscheidungen | §5(a) | Leistungsanspruchsprüfung, Wohnungszuweisung, Pflegebedarfsermittlung |
| Kritische Infrastruktursteuerung | §2 | Verkehrssteuerungs-KI, Versorgungsnetzoptimierung |
| Bildungszugang | §3 | Schulplatzvergabe, Zugangsentscheidungen |

Hochrisiko-KI-Systeme erfordern: Konformitätsbewertung vor Erstbetrieb, Registrierung in der EU-KI-Datenbank, menschliche Aufsichtsmechanismen (Entscheidungen müssen überprüft und außer Kraft gesetzt werden können), detaillierte technische Dokumentation und Post-Market-Überwachung.

**Transparenzpflichten (Art. 50):** KI-Systeme, die mit Bürgerinnen und Bürgern interagieren (Chatbots, automatisierte Bescheide), müssen ihre KI-Natur zum Zeitpunkt der Interaktion offenlegen.

#### 4.13.2 Kommunaler KI-Compliance-Pfad

1. **KI-Inventar:** Vollständige Erfassung aller KI- oder automatisierten Entscheidungshilfe-Werkzeuge in kommunalen Diensten, einschließlich eingebetteter KI in beschaffter Software.
2. **Risikoklassifizierung:** Klassifizierung jedes Werkzeugs gegenüber den KI-Gesetz-Risikoklassen anhand der EU-Kommissions-Klassifizierungshilfen.
3. **Hochrisiko-KI:** Für jedes Hochrisiko-System: Compliance-Beauftragten benennen, Konformitätsbewertung einleiten oder einholen, in EU-KI-Datenbank registrieren. Bestehende Systeme müssen bis 2. August 2027 konform sein.
4. **Lieferantenpflichten:** Bei Beschaffung KI-führender Software: (a) EU-KI-Datenbank-Registrierungsnummer, (b) Konformitätszertifikat, (c) menschliche Aufsichtsmechanismen, (d) Beschreibung vorgesehener Verwendungszweck und bekannter Grenzen bei Vertragsabschluss verlangen.
5. **Transparenzhinweise:** KI-Offenlegungshinweise in allen bürgernahen Diensten mit automatisierter Entscheidungsunterstützung implementieren.
6. **KI-Stückliste (AIBOM):** SBOM-Praxis (Abschnitt 6.2) auf KI-Komponenten ausweiten — Modellidentifikatoren, Trainingsdaten-Provenienz, Verwendungszweck-Deklarationen.

#### 4.13.3 Open-Source-Vorteil bei KI-Compliance

Der empfohlene Open-Source-Stapel hat einen strukturellen Vorteil bei KI-Gesetz-Compliance: Alle Komponenten sind vollständig prüfbar, Modellarchitekturen (wo zutreffend) sind transparent, und es gibt keine proprietären KI-Black-Boxes im Kern des Verwaltungsstapels. Kommunen, die KI-Komponenten einsetzen, sollten bevorzugt Open-Source-KI-Werkzeuge (z.B. open-gewichtete Sprachmodelle auf souveräner Infrastruktur) proprietären KI-APIs vorziehen, aus drei Gründen:

1. **Prüfbarkeit:** KI-Gesetz erfordert Trainingsdaten- und Modelldokumentation; Open-Source-Modelle machen diese Dokumentation intrinsisch verfügbar.
2. **Datenminimierung:** Proprietäre KI-APIs erfordern typischerweise die Übermittlung von Bürgerdaten an Drittserver; lokaler Betrieb offener Modelle eliminiert diese Datenübertragung vollständig.
3. **Unabhängigkeit:** Vermeidung proprietärer KI-APIs verhindert eine neue Form des Vendor-Lock-ins auf der KI-Schicht.

---

## 5. Implementierungsfahrplan

### Phase 0: Fundament (Monate 1–3)

**Ziel:** Governance aufbauen, Ist-Zustand erfassen, Koalition bilden.

**Ergebnisse:** Digitaler Transformationsausschuss; Ist-Analyse (inkl. KI-Inventar parallel); Stakeholder-Einbindungsplan; Beschaffungsrahmen; MoU mit kooperativem IT-Dienstleister; GBK-Analyse beauftragt.

**Entscheidungstor:** Politisches Mandat und Budget genehmigt.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundlegende Schichten aufbauen.

**Ergebnisse:** SCS-Umgebung in Betrieb; Keycloak mit BundID / Schweizer E-ID föderiert; Nextcloud-Basis; Matrix/Element für Mitarbeitende; BSI IT-Grundschutz-Baseline.

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste Bürgerdienste auf offener Infrastruktur.

**Ergebnisse:** Fünf volumensstärkste Dienste auf Camunda/XÖV; CMS-Migration; CKAN-Portal (20 Datensätze); Decidim-Instanz für ersten Partizipationsprozess.

### Phase 3: Integration und Ausweitung (Monate 16–24)

**Ziel:** Alle Schichten verbinden; 80 % der Transaktionen abdecken.

**Ergebnisse:** Alle Dienste via Keycloak SSO; GIS-Schicht; GovStack-BB-Compliance-Assessment (Baseline gegen Abschnitt 4.12).

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Nutzerfreundlichkeit verbessern; zur Open-Source-Community beitragen.

**Ergebnisse:** Bürgerzufriedenheitsumfrage (Ziel NPS > 40); erster Upstream-Beitrag; kommunale Praxisgemeinschaft; KI-Gesetz Hochrisiko-KI-Systeme in EU-KI-Datenbank registriert.

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität; Replikation vorbereiten.

**Ergebnisse:** SBOM und KI-Stückliste (AIBOM); Datenhaltung 100 % souverän (geprüft); GAIA-X Self-Description veröffentlicht; Replikations-Playbook; Strategiepapier v1.0.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Einbindungsansatz |
|---|---|---|
| Bürgermeister:in / Exekutive | Politischer Erfolg, Kosten | Führungsbriefing, Dashboard |
| Gemeinderat | Aufsicht, demokratische Legitimität | Quartalsberichte, öffentliche Sitzungen |
| Kommunale IT-Abteilung | Technische Machbarkeit | Co-Design, Schulungen, Community |
| Vergabestelle | Rechtskonformität | Rahmenverträge, Rechtsbriefings |
| Mitarbeitende | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Change Management, Schulungen |
| Bürger:innen | Servicequalität, Datenschutz | Partizipationsdesign, Transparenzberichte |
| Datenschutzbeauftragte:r | DSGVO / revDSG | Privacy-by-Design in jeder Phase |
| KI-Compliance-Beauftragte:r | KI-Gesetz-Konformität | KI-Inventar, Risikoklassifizierung, Register |
| Personalrat | Datenschutz, Arbeitsbelastung | Frühzeitige Einbindung |
| Medien / Journalist:innen | Rechenschaftspflicht | Proaktive Datenveröffentlichung |

### 6.2 Beschaffungsrahmen

**1. Dienste beschaffen, keine Lizenzen.** Software ist kostenlos; Kommunen bezahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**2. Kooperative Beschaffung.** Govdigital eG und Schweizer kantonale IT-Kooperativen bieten Rahmenverträge (GWB/VgV in Deutschland; BöB/VöB in der Schweiz) [23].

Die **Anstalt für Kommunale Datenverarbeitung in Bayern (AKDB)** versorgt etwa 2.000 bayerische Kommunen und Landkreise über ein umfassendes Shared-Service-Modell [57]. Als Anstalt des öffentlichen Rechts kann die AKDB nicht privatisiert werden und betreibt ihre Dienste zum Selbstkostenpreis für ihre Mitgliedskommunen — ein struktureller Beschaffungsvorteil analog zu govdigital eG auf Bundesebene. Das Leistungsportfolio der AKDB umfasst BayernID-Authentifizierung, EfA-Dienstimplementierungen, kommunale CKAN-Einsätze (wie in der Rosenheimer Fallstudie, Abschnitt 3.7 dokumentiert) und wachsende Unterstützung für OpenDesk-Komponenten. Für bayerische Kommunen bieten AKDB-Rahmenverträge einen direkten Weg zu den empfohlenen Stapelkomponenten ohne gesonderte EU-Schwellenwert-Vergabeverfahren — typischerweise der schnellste Implementierungsweg für Kommunen von 10.000–100.000 Einwohnern.

**3. Öffentliches Geld — Öffentlicher Code.** Alle unter öffentlichem Auftrag entwickelten Komponenten müssen unter OSI-zugelassener Lizenz veröffentlicht werden — auf openCode.de (Deutschland) oder code.admin.ch (Schweiz) [4].

**4. Fünf-Jahres-GBK in der Bewertung.** Empfohlene Gewichtung: Preis/GBK (40 %), Funktionalität (30 %), Souveränität und Interoperabilität (20 %), Community-Gesundheit (10 %).

**5. Interoperabilitätsstandards als Pflichtanforderung.** XÖV (Deutschland) [46], eCH (Schweiz) [51], DCAT-AP für Open Data [45]. Nichtkonformität ist ein Ausschlusskriterium.

**6. SBOM und AIBOM.** Software-Stückliste (SBOM) im SPDX- oder CycloneDX-Format bei Vertragsabschluss und bei jedem Major-Release. Für KI-gestützte Komponenten zusätzlich eine KI-Stückliste (AIBOM) mit Modellidentität, Trainingsdaten-Provenienz und Verwendungszweck, entsprechend den Transparenzpflichten aus Art. 13 KI-Gesetz [60].

**7. KI-Gesetz-Konformitätserklärung.** Für KI-Komponenten enthaltende Systeme: KI-Gesetz-Risikoklassifizierung, EU-KI-Datenbank-Registrierungsnummer (für Hochrisiko-KI) und menschliche Aufsichtsarchitektur bei Vertragsabschluss fordern.

### 6.3 Change Management

- **Digitalbeauftragte:r** auf Ebene Stadtrat/Vize-Bürgermeisterin
- **Abteilungsweise Open-Source-Champions** mit erweiterter Schulung
- **Parallelbetrieb** für mindestens drei Monate
- **Früherfolge dokumentieren**: Kosteneinsparungen, neue Fähigkeiten, Bürger-Feedback
- **Öffentliches Transparenz-Dashboard**
- **Personalrat frühzeitig einbinden**

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Maßnahme |
|---|---|---|---|
| Politische Kehrtwende nach der Wahl | Mittel | Hoch | In Satzung einbetten; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / Desinformationskampagnen | Hoch | Mittel | GBK-Belege; Zivilgesellschaft; Mandat publizieren |
| Qualifikationsdefizit im IT-Team | Hoch | Mittel | Schulungen; kooperativer IT-Anbieter |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Stufenweiser Rollout mit Entscheidungstoren |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständige Datensicherung; Parallelbetrieb |
| DSGVO / revDSG-Verletzung | Niedrig | Hoch | Privacy-by-Design; DSB in jeder Phase |
| KI-Gesetz-Nichtkonformität | Mittel | Hoch | KI-Inventar in Phase 0; Risikoklassifizierung; Konformitätsbewertung |
| Nutzerannahme-Versagen | Mittel | Hoch | Change Management; UX-Tests; Schulungen |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstest; SBOM; NIS2 [27] |
| Lieferkettenkompromittierung | Niedrig | Kritisch | SBOM; reproduzierbare Builds; CVE-Überwachung |
| GAIA-X-Ökosystem-Fragmentierung | Niedrig | Niedrig | SCS sichert Souveränität unabhängig von GAIA-X-Reife |

### 7.2 Der Münchener Präzedenzfall

Das LiMux-Projekt der Landeshauptstadt München (2003–2017) ist das meistzitierte Beispiel einer rückabgewickelten Open-Source-Transition. Die technische Implementierung versorgte 15.000 Desktops 14 Jahre lang erfolgreich [30]. Die Kehrtwende war primär politisch motiviert, nicht technisch. Entscheidende Lehre: **Politisches Risikomanagement** ist mindestens so wichtig wie technische Planung.

### 7.3 Sicherheitsaspekte

- BSI IT-Grundschutz als Sicherheitsbaseline
- TLS 1.3 minimum; AES-256 für sensible Datenkategorien
- Penetrationstests an jedem Phasenmeilenstein
- NIS2-konformer Vorfallreaktionsplan [27]
- SBOM wöchentlich gegen OSV-Datenbank prüfen
- Matrix/Element E2E-Verschlüsselung als Standard für behördübergreifende Kommunikation

### 7.4 Datenschutz und DSGVO

Alle empfohlenen Komponenten ermöglichen den Betrieb mit Datenresidenz ausschließlich auf kommunal kontrollierter Infrastruktur (DSGVO Art. 44). Das revDSG (in Kraft September 2023) legt Schweizer Kommunen äquivalente Pflichten auf [55].

### 7.5 GAIA-X als europäische Cloud-Vertrauensschicht

GAIA-X [59], die europäische Initiative für föderierte Dateninfrastruktur, ergänzt die SCS-Infrastrukturempfehlung um eine Governance- und Vertrauensschicht. Während SCS die technische Cloud-Implementierung adressiert, definiert GAIA-X den Rahmen, in dem europäische Cloud-Dienste interoperieren.

**Das GAIA-X Trust Framework** legt attestierbare Kriterien für Cloud-Anbieter fest: Datensouveränität, Portabilität, Transparenz und Sicherheit. SCS-zertifizierte Anbieter erfüllen diese Kriterien per Design, sodass Kommunen, die auf SCS betreiben, automatisch am GAIA-X-Ökosystem teilnehmen.

**GAIA-X Self-Descriptions** sind maschinenlesbare Erklärungen, die Organisationen veröffentlichen, um ihre Datenrichtlinien und technischen Fähigkeiten zu beschreiben. Kommunen können eine Self-Description veröffentlichen, um ihre Souveränitätsverpflichtung zu signalisieren und automatisiertes Policy-Matching mit Partnerorganisationen zu ermöglichen.

**Datenräume:** GAIA-X ermöglicht die Teilnahme an sektorspezifischen europäischen Datenräumen:
- **Mobility Data Space:** Verkehrs- und Mobiliätsdaten mit anderen Kommunen, Forschungseinrichtungen und Verkehrsbetrieben
- **Smart City Data Space:** Kollaborative urbane Sensorik und Umweltüberwachung
- **EHDS (European Health Data Space):** Kommunale Gesundheitsdienstdaten (in Entwicklung)

**Aktueller Stand (2026):** GAIA-X-Föderationsdienste sind in Deutschland (govdigital eG im GAIA-X-Ökosystem) und Frankreich (Bleu Cloud) in Betrieb. Die Schweizer Beteiligung entwickelt sich über den Swiss GAIA-X Hub. Volle grenzüberschreitende Föderationsreife wird bis 2027 erwartet.

**Empfehlung:** Kommunen, die auf SCS betreiben, haben die technische Grundlage für GAIA-X-Beteiligung bereits. Phase 5 des Implementierungsfahrplans enthält die Veröffentlichung einer GAIA-X Self-Description als Ergebnis. In Vergabespezifikationen sollte GAIA-X-Trust-Framework-Konformität als wünschenswertes Kriterium aufgeführt werden.

---

## 8. Fazit

Die in diesem Papier untersuchten Belege führen zu sieben Erkenntnissen:

**1. Open-Source-Technologiestapel für Kommunen sind technisch ausgereift und praxisbewährt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung lässt sich durch Open-Source-Software erfüllen, auch im Bereich 35.000–85.000 Einwohner (Abschnitt 3.7).

**2. Der Regulierungsrahmen schreibt Open-Source und Interoperabilität zunehmend vor.** EMBAG Art. 9 (Schweiz), OZG 2.0 (Deutschland), Interoperable Europe Act 2024 und EU-Datengesetz 2023 schaffen Rechtspflichten [1, 2, 6, 48].

**3. Die wirtschaftliche Argumentation ist überzeugend, wenn Gesamtkosten korrekt erfasst werden.** Das GBK-Modell zeigt ca. 50 % Einsparungen für eine 500-Mitarbeitenden-Kommune.

**4. GovStack-Bausteine liefern zusätzliche Implementierungsunterstützung.** Das formale Compliance-Mapping (Abschnitt 4.12) zeigt volle oder substanzielle Konformität bei sieben von neun GovStack-Bausteinen. Die zwei kritischen Lücken — Zahlungen und vollständiges Einwilligungs-Audit-Log — sind klar definiert und für v1.0 adressierbar [47, 56].

**5. Erfolg erfordert politische und organisatorische Investitionen gleichwertig zur technischen Investition.** Der Münchener Rückschlag und erfolgreiche Transitionen in Barcelona, Schaffhausen, Biberach und Rosenheim bestätigen dies gleichermaßen.

**6. Das EU KI-Gesetz (2024) schafft eine neue Compliance-Verpflichtung für kommunale KI-Einsätze.** Kommunen müssen ein KI-Inventar durchführen, alle KI-Werkzeuge nach den KI-Gesetzes-Risikoklassen klassifizieren und Konformitätsbewertungen für Hochrisiko-KI — insbesondere automatisierte Sozialleistungsentscheidungen — sicherstellen. Open-Source-KI-Komponenten auf souveräner Infrastruktur sind strukturell besser für die Compliance positioniert [60].

**7. GAIA-X bietet die aufkommende grenzüberschreitende Vertrauensschicht für europäische kommunale Cloud.** Kommunen auf Sovereign Cloud Stack nehmen automatisch am GAIA-X-Ökosystem teil und können Datenräume und föderierte Dienste mit Partnerverwaltungen in der EU nutzen [59].

Kommunen, die früh handeln, profitieren von First-Mover-Vorteilen: Mitgestaltung kooperativer Standards, Aufbau von Inhouse-Expertise und Beitrag zur gemeinsamen Open-Source-Infrastruktur. Der Rechtsrahmen ist vorhanden. Die Technologie ist bereit. Die Wirtschaftlichkeit ist günstig. Die KI-Governance-Anforderungen klären sich. Das europäische Cloud-Gemeingut nimmt Form an. Die Transformation ist überfällig.

---

## Referenzen

Dieses Dokument ist die deutsche Übersetzung von `Doc/en/sovereign-by-design-v0.3.0.md`. Die vollständige Referenzliste [1]–[60] findet sich im englischen Quelldokument. Die Nummerierung der Zitate ist identisch.

**Neue Quellen in v0.3.0 (gegenüber v0.2.0 hinzugefügt):**

[54] Europäische Kommission / OSOR. (2024). *OSOR Annual Report 2023: Open Source Software in European Public Administration*. Brüssel: Europäische Kommission / Joinup. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [Open Access, CC-BY-4.0]

[56] GovStack Initiative (ITU/DIAL). (2023). *GovStack: Building Block Specifications v1.0*. Genäf/Washington: ITU/DIAL. https://govstack.gitbook.io/specification/ — [Open Access, CC-BY-SA-4.0]

[57] Anstalt für Kommunale Datenverarbeitung in Bayern (AKDB). (2024). *AKDB Jahresbericht 2023*. München: AKDB. https://www.akdb.de/presse/berichte/ — [Open Access]

[58] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O’Reilly Media. ISBN 978-0-596-80435-0. https://www.oreilly.com/library/view/open-government/9781449381905/ — [© O’Reilly Media; nur Zitation]

[59] GAIA-X European Association for Data and Cloud AISBL. (2024). *GAIA-X Architecture Document: Technical Architecture v24.06*. Brüssel: GAIA-X AISBL. https://docs.gaia-x.eu/ — [Open Access, CC-BY-4.0]

[60] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 über künstliche Intelligenz (KI-Gesetz)*. Amtsblatt der EU. In Kraft 2024-08-01; gestaffelte Anwendung bis 2027. CELEX: 32024R1689. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 — [Open Access, EU-Recht]

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*  
*Zitierweise: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com), „Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen“, v0.3.0, 2026-06-21.*
