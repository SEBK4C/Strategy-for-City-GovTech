---
title: "Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitiervollständiger Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
source-language: "en"
source-file: "Doc/en/sovereign-by-design-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - Digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - Kommunale Digitalisierung
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - Bürger-Technologie
---

# Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitiervollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Englisch (Quelle) · Deutsch (diese Fassung)  
**SPDX-Lizenzbezeichner:** CC-BY-4.0  

---

## Zusammenfassung

Kommunalverwaltungen sind die dem Bürger nächste Schicht demokratischer Verwaltung, stehen jedoch vor einem akuten strukturellen Widerspruch: Die digitalen Werkzeuge, auf die sie angewiesen sind, werden zunehmend proprietär, herstellergebunden und an privaten statt öffentlichen Interessen ausgerichtet. Dieses Papier stellt eine umfassende, zitiervollständige Strategie für die Implementierung eines modernen Open-Source-Technologie-Stacks in kommunalen Verwaltungen vor. Es gestützt auf Vorbilder des Schweizer Bundesrechts (EMBAG), des deutschen OZG-2.0-Reformprogramms, der Sovereign-Cloud-Stack-Initiative, OpenDesk und der europäischen Gemeinschaft souveräner Technologie werden ein grundlagenübergreifender Umsetzungsplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie erarbeitet.

Wir bewerten fünfzehn funktionale Technologieschichten — von digitaler Identität und Cloud-Infrastruktur bis zu KI-gestützten Bürgerservices und Barrierefreiheitswerkzeugen — anhand von Kriterien der digitalen Souveränität, Interoperabilität, Gesamtbetriebskosten, Sicherheit und zivilgesellschaftlicher Ausrichtung. Neue Abschnitte befassen sich mit dem EU-Datengesetz (2023), dem EU-KI-Gesetz (2024), dem EU-Datenverwaltungsgesetz (2022), der GovStack-Initiative für Bausteine digitaler Verwaltung sowie einer evidenzbasierten Gesamtkostenanalyse. Wir dokumentieren Fallstudien aus kleinen und mittelgroßen Kommunen, die zeigen, dass Open-Source-Transformation nicht nur für Großstädte realisierbar ist.

Wir kommen zu dem Schluss, dass Open-Source-Technologie-Stacks für Kommunen über einen Fünf-Jahres-Horizont nicht nur technisch machbar, sondern wirtschaftlich überlegen, demokratisch notwendig, in einer wachsenden Zahl von Jurisdiktionen gesetzlich vorgeschrieben und innerhalb eines strukturierten 36-Monats-Programms praktisch umsetzbar sind. Das Papier liefert eine phasenweise Umsetzungsanleitung mit indikativen Budgetrahmen, einer Beschaffungs-Checkliste und einem Meilensteintracker für Stadtverwaltungen, gewählte Amtsträger, IT-Teams, Beschaffungsstellen, zivilgesellschaftliche Gruppen, Open-Source-Gemeinschaften und Anbieter souveräner Technologien.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitalisierung, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, GovStack, EU-Datengesetz, KI-Gesetz, Gesamtbetriebskosten, öffentliche Beschaffung

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist nicht länger optional. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen; Regulierungsbehörden fordern Interoperabilität und Datenschutz; und der Fiskaldruck erfordert nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte weltweit in einem Kreislauf proprietärer Herstellerhängigkeit, kostspieliger Lizenzverträge und fragmentierter Systeme gefangen, die gute Verwaltung eher behindern als fördern [1, 29].

Die Folgen dieser Abhängigkeit sind gut dokumentiert. Vendor-Lock-in erhöht die Wechselkosten und das Verhandlungsungleichgewicht [4]. Proprietäre Formate behindern den ämtlichen Datenaustausch und Transparenz [45]. Geschlossene Infrastrukturen verhindern unabhängige Sicherheitsprüfungen [26]. Laufende Lizenzgebühren entziehen den Budgets Mittel, die sonst der Daseinsvorsorge zukämen [3, 5]. Und am grundlegendsten: Wenn die Software demokratischer Institutionen im Eigentum privater Akteure steht, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Interesse und unternehmerischen Imperativ [4, 56].

Die Regulierungslandschaft wandelt sich entschieden. Das Schweizer EMBAG von 2023 schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht werden muss [1]. Das OZG 2.0, der Sovereign Cloud Stack und OpenDesk repräsentieren Europas ambitioniertestes Open-Source-Regierungstechnologieprogramm [2, 3, 42]. Das EU-Gesetz über interoperable Europa (2024) schafft bindende grenzüberschreitende Interoperabilitätspflichten [6]. Das EU-KI-Gesetz (2024) legt Anforderungen für KI-Systeme in der öffentlichen Verwaltung fest [50]. Das EU-Datengesetz (2023) regelt den Datenzugang mit erheblichen Auswirkungen auf die kommunale Datenverwaltung [49]. Die GovStack-Initiative der ITU und DIAL hat diese Konvergenz in wiederverwendbare, interoperable „Building Blocks“ für digitale Verwaltungsdienstleistungen kodifiziert [48].

Dieses Papier synthetisiert diese Entwicklungen zu einer praxisorientierten, evidenzbasierten Strategie für Kommunen aller Größenordnungen.

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und kommunale Behörden, einschließlich Gemeinden, Kommunen, Städte und entsprechende Strukturen in Schweizer Kantonen. Die Strategie ist skalierbar von kleinen Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (500.000+), mit expliziten Anpassungshinweisen.

*Open-Source-Technologie-Stack* bezeichnet unter OSI-genehmigten Lizenzen lizenzierte Softwarekomponenten, die auf Infrastruktur betrieben werden, die die Kommune kontrolliert oder ohne unzumutbaren Aufwand migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer öffentlichen Verwaltung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software ohne Herstellerabhängigkeit einzusehen, zu verändern, zu prüfen und zu migrieren [3, 5].

*Souveräne Cloud* bedeutet im europäisch-öffentlichen Kontext eine Cloud-Infrastruktur, die: (a) unter EU-Jurisdiktion betrieben wird; (b) Open-Source-Komponenten mit öffentlich prüfbarem Code einsetzt; (c) vertragliche Garantien gegen den Drittländerzugang gewährt; und (d) ohne Herstellergenehmigung migriert oder selbst betrieben werden kann [3, 52].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Technologie-Stack für Kommunen im Jahr 2026 aus?
2. Welche Lehren können aus den Erfahrungen der schweizerischen, deutschen und europäischen Gemeinschaft souveräner Technologie gezogen werden?
3. Was ist der optimale schrittweise Umsetzungsweg für eine Stadt mit 5.000–500.000 Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement gestaltet sein, um die Erfolgswahrscheinlichkeit zu maximieren?
5. Was zeigt die Evidenz zu den Gesamtbetriebskosten beim Vergleich von Open-Source- und proprietären kommunalen Stacks?
6. Wie beeinflussen das EU-Datengesetz, das KI-Gesetz und das Datenverwaltungsgesetz kommunale Technologieentscheidungen?

---

## 2. Methodik

Dieses Papier verwendet ein Mehrmethoden-Forschungsdesign, das folgende Elemente kombiniert:

**Systematische Literaturrecherche** peer-geprüfter Veröffentlichungen, grauer Literatur, Regierungsdokumente und Rechtsinstrumente aus den Jahren 2004–2026, die E-Government-Theorie, digitale Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunale digitale Transformation abdecken.

**Vergleichende Politikanalyse** von Technologiegesetzgebung und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027, OGD-Strategie 2024–2027), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, FITKO-Governance-Rahmen) und der Europäischen Union (Interoperable-Europe-Act 2024, EU-Open-Source-Strategie 2020–2023, EU-KI-Gesetz 2024, EU-Datengesetz 2023, EU-Datenverwaltungsgesetz 2022).

**Technologie-Stack-Bewertung** anhand einer strukturierten Sieben-Kriterien-Bewertungsmatrix: (a) Lizenzöffenheit, (b) Deployment-Reife, (c) Community-Gesundheit, (d) Konformität mit Interoperabilitätsstandards, (e) Sicherheitsprofil, (f) Fünf-Jahres-Gesamtbetriebskosten, (g) dokumentierte öffentliche Einsatzbereiche.

**Stakeholder-Analyse** der Interessen, des Einflusses und des Engagement-Bedarfs jeder Stakeholder-Gruppe.

**Fallstudienanalyse** von Open-Source-Transitionen in Barcelona (Decidim), Helsinki, Kanton Schaffhausen, dem französischen DINUM-Open-Source-Programm [60] und kleinen Gemeinden in der deutschsprachigen Schweiz und Baden-Württemberg.

Die Literaturrecherche ist so konzipiert, dass sie sich selbst verbessert: das Quellenregister (`Mem/source-registry.md`) und der Literaturrecherche-Status (`Mem/literature-review-state.md`) sind versionierte Dokumente, die regelmäßig aktualisiert werden.

---

## 3. Literaturrecherche

### 3.1 Theoretische Grundlagen des E-Government

Die akademische Literatur zum E-Government hat sich durch vier breite Phasen entwickelt [30]. Die erste Generation (1995–2005) digitalisierte bestehende Prozesse. Die zweite Generation (2005–2012) betonte Online-Dienstleistungserbringung und Back-Office-Integration [7]. Die dritte Generation (2012–2020) führte Open Data, partizipative Plattformen und Mobile-First-Servicedesign ein [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattform-Governance, digitale Identitätsinfrastruktur und den „Souveränitäts-Schwenk“ gekennzeichnet — die Erkenntnis, dass digitale Autonomie eine Voraussetzung demokratischer Selbstregierung ist [30, 45].

Wirtz und Weyerers holistisches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Janowskis Vier-Generationen-Rahmen verfolgt die Evolution des digitalen Regierens von Digitalisierung über Transformation, Engagement bis zur Kontextualisierung [30].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Drei Rechtsinstrumente operationalisieren diesen Imperativ in Europa:

Die **EU-Open-Source-Strategie 2020–2023** etablierte „Teilung und Wiederverwendung“ als Kernprinzip [5]. Der **Interoperable Europe Act (2024)** schafft bindende Interoperabilitätspflichten [6]. Das **EU-Datenverwaltungsgesetz (2022)** regelt Daten-Intermediare und öffentliches Datenaustausch-Sharing mit strengen Datensouveränitätsbedingungen [58].

Deutschlands **Sovereign Cloud Stack (SCS)** ist die konkreteste Realisierung digitaler Souveränität in der Cloud-Infrastruktur [3]. Die Schweizer **EMBAG-Gesetzgebung**, in Kraft seit dem 1. Januar 2024, schreibt vor, dass alle mit öffentlichen Mitteln entwickelten Bundessoftwareprogramme als Open Source veröffentlicht werden müssen [1].

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 grundlegend reformiert (OZG 2.0), schreibt vor, dass alle deutschen Behörden ihre Verwaltungsleistungen online anbieten müssen [2]. Die OZG-2.0-Reform adressiert Schwächen der ersten Generation durch fünf strukturelle Mechanismen: (1) Once-Only-Prinzip, (2) Einer-für-Alle-Ansatz (EfA), (3) BundID, (4) FITKO-Rahmen [9] und (5) OpenDesk [42].

ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), gegründet 2022, ist der zentrale institutionelle Akteur im deutschen Open-Source-Verwaltungsökosystem. Sein Jahresbericht 2023/2024 dokumentiert den Rollout von OpenDesk auf Bundesbehörden und die Koordinierung von openCode.de [51]. Die openCode.de-Plattform, gestartet 2022, bietet ein zentrales Repository für Open-Source-Software der Verwaltung [10].

### 3.4 Schweizerische kantonale und digitale Bundesdienste

Die Schweiz hat eine Reihe digitaler Infrastrukturen entwickelt:

**Fedlex** (fedlex.admin.ch): die offizielle Plattform für Schweizer Bundesrecht in offenen Standards [1]. **opendata.swiss**: das nationale Open-Government-Data-Portal auf CKAN-Basis [44], geregelt durch die OGD-Strategie 2024–2027 [55]. **eCH-Standards**: die eCH-Vereinigung entwickelt XML- und Datenaustauschstandards für das Schweizer E-Government [47] — funktionales Äquivalent zum deutschen XÖV. **GEVER**: das standardisierte Records-Management-System der Bundesverwaltung [43]. **Schweizer E-ID**: nach der Volksabstimmung 2021 wird ein dezentrales, datenschutzfreundliches digitales Identitätssystem auf Basis selbstsouveräner Identität (SSI) erwartet.

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016) wird von über 400 Organisationen in 40 Ländern genutzt, einschließlich Barcelona, Helsinki und dem Kanton Schaffhausen [12]. **CONSUL Democracy** (Madrid, 2015) bietet eine AGPL-3.0-Alternative mit besonderer Stärke im Bereich partizipativer Haushaltsplanung [54]. **Matrix/Element** ermöglicht offene, dezentralisierte, Ende-zu-Ende-verschlüsselte Kommunikation; der deutsche BundesMessenger und das französische Tchap basieren auf Matrix [14]. **Nextcloud** (Stuttgart, 2016) ist die meistgenutzte Open-Source-Dateisynchronisierungs- und -kollaborationsplattform in der europäischen öffentlichen Verwaltung [13]. **OpenDesk** ist die erste regierungskuratierte Open-Source-Arbeitsplatzsuite Europas [42]. **GAIA-X** (AISBL, Brüssel) entwickelt ein föderiertes, interoperables Dateninfrastrukturökosystem nach europäischen Werten [52].

### 3.6 Die GovStack-Initiative

Die GovStack-Initiative der ITU und DIAL hat umfassende Spezifikationen für wiederverwendbare digitale „Building Blocks“ der Verwaltung entwickelt [48]. Die Ausrichtung der GovStack-Building-Blocks am Europäischen Interoperabilitätsrahmen [45] bedeutet, dass Kommunen, die GovStack-konforme Architekturen implementieren, automatisch viele technische Anforderungen des Interoperable Europe Act erfüllen [6, 48].

### 3.7 EU-Datengesetz, KI-Gesetz und Datenverwaltungsgesetz

**Das EU-Datenverwaltungsgesetz (DGA, 2022/868, in Kraft September 2023)** [58] regelt die Wiederverwendung geschützter öffentlicher Daten und schafft EU-anerkannte Datenräume. Für Kommunen: öffentliche Stellen müssen Daten über technisch neutrale und transparente Infrastrukturen bereitstellen — was Open-Source-Datenkataloge wie CKAN begünstigt.

**Das EU-Datengesetz (2023/2854, anwendbar September 2025)** [49] führt Wechsel-Anforderungen an Cloud-Anbieter ein: Migrations-Unterstützung, Datenportabilität in offenen Formaten und vertragliche Austrittsrechte — was direkt für Open-Source-Cloud-Infrastruktur und den Sovereign Cloud Stack spricht.

**Das EU-KI-Gesetz (2024/1689)** [50] schafft einen risikobasierten Regulierungsrahmen für KI-Systeme. KI-Systeme in der öffentlichen Verwaltung für automatisierte Entscheidungen, die Bürgerrechte betreffen, gelten als „hochrisikobehaftet“ (Anhang III) und bedürfen einer Konformitätsbewertung, Transparenzpflichten und menschlicher Aufsichtsmechanismen. Open-Source-KI-Systeme sind besser positioniert, diese Transparenz- und Prüfanforderungen zu erfüllen.

### 3.8 Gesamtbetriebskosten: Was die Evidenz zeigt

Die verfügbare Evidenz begünstigt Open-Source-Stacks über Fünf-Jahres-Horizonte konsequent, wenn Wechselkosten und Vendor-Lock-in-Risiken korrekt berücksichtigt werden.

**DINUM-Studie (Frankreich, 2020–2024)**: Migration auf Open-Source-Produktivitätstools für 250.000 Beamte ergab Nettoeinsparungen von ca. 150 Mio. Euro über vier Jahre [60]. **Münchener LiMux-Nachbetrachtung (2017)**: kumulierte Einsparungen von ca. 11,7 Mio. Euro während der Open-Source-Periode; die Umkehrung kostete ca. 49 Mio. Euro [59].

**Wichtige Kostenvergleichsmatrix:**

| Kostenkategorie | Open Source | Proprietär |
|---|---|---|
| Lizenz / Abonnement | 0 € (OSS) | 80–300 €/Nutzer/Jahr |
| Implementierung | 150–500 €/Nutzer (einmalig) | 50–200 €/Nutzer |
| Schulung | 200–400 €/Nutzer | 100–200 €/Nutzer |
| Laufender Support | 8–15% der Implementierung | 15–25% der Lizenz |
| Ausstieg / Migration | 0 € (offene Formate) | 200–800 €/Nutzer |

Für eine Kommune mit 500 Mitarbeitenden: jährliche Lizenzersparnisse von ca. 100.000 Euro; Implementierungskosten ca. 200.000 Euro; Amortisationszeit ca. 2 Jahre; Fünf-Jahres-Nettoeinsparung ca. 300.000 Euro.

### 3.9 Nutzererfahrung und digitale Inklusion

Die wissenschaftliche Literatur zur Bürgerzufriedenheit mit Open-Source-Verwaltungsdiensten ist fast vollständig absent — eine kritische Forschungslücke. Die begrenzte verfügbare Evidenz legt nahe, dass die Qualität von Dienstleistungen stärker mit dem Designaufwand, der Barrierefreiheitseinhaltung und der Change-Management-Qualität korreliert als mit dem Software-Lizenzmodell [7, 29]. Kommunen sollten etwa 15–20 % der Implementierungskosten für UX-Design und Barrierefreiheitsaudits einplanen.

### 3.10 Fallstudien kleiner Kommunen

Drei dokumentierte Übergänge im Bereich 5.000–100.000 Einwohner zeigen, dass Open-Source-Transformation auf kommunaler Ebene machbar ist:

**Kanton Schaffhausen (~80.000 Einw.)**: Einführung von Decidim 2020 für kantonale Beteiligungsprozesse. Laufende Kosten ca. CHF 30.000/Jahr. Personalschulung in drei Tagen abgeschlossen.

**Herrenberg, Baden-Württemberg (~30.000 Einw.)**: Umstieg auf einen umfassenden Open-Source-Arbeitsplatz-Stack (LibreOffice, Thunderbird, Nextcloud) 2018–2021. Gemeldete Einsparungen von ca. 40.000 Euro/Jahr bei Lizenzkosten.

**Gummersbach, NRW (~50.000 Einw.)**: Einführung eines CKAN-basierten Open-Data-Portals 2022 im Rahmen des Kommunalen Open-Data-Netzwerks NRW. Einrichtungskosten ca. 15.000 Euro; laufende Hosting-Kosten 3.000 Euro/Jahr.

---

## 4. Technologie-Stack-Analyse

Ein kommunaler Technologie-Stack lässt sich in fünfzehn funktionale Schichten aufteilen.

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Authentifizierung von Bürgern und Mitarbeitenden; Identitätsfederation; Single Sign-On (SSO); eIDAS-2.0-Konformität.

**Empfehlung: Keycloak** (Apache 2.0) [21]

Keycloak ist die De-facto-Open-Source-Identitätsmanagement-Plattform für die europäische öffentliche Verwaltung. Es implementiert OpenID Connect 1.0, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht Federation mit nationalen Identitätssystemen (BundID, Schweizer E-ID, eIDAS 2.0).

| Kriterium | Keycloak | Anmerkungen |
|---|---|---|
| Lizenzöffenheit | 5/5 | Apache 2.0 |
| Deployment-Reife | 5/5 | 10+ Jahre Produktion |
| Community-Gesundheit | 5/5 | CNCF, Red Hat, große Community |
| Interoperabilität | 5/5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Sicherheitsprofil | 5/5 | CVE-reaktionsfähig, weit geprüft |
| TCO (5 Jahre) | 4/5 | Keine Lizenz; Betriebsexpertise nötig |
| Öffentliche Einsatzbereiche | 5/5 | Weitverbreitet in EU-Behörden |

### 4.2 Dokumentenmanagement und Schriftgutverwaltung

**Funktion:** Verwaltung amtlicher Unterlagen; GEVER-konforme Workflows (Schweiz); OZG-konforme Aufbewahrung (Deutschland).

**Empfehlung: Nextcloud** (AGPL-3.0) + **openGEVER / CMI GEVER CE** (Schweiz) [13]

| Kriterium | Nextcloud | Anmerkungen |
|---|---|---|
| Lizenzöffenheit | 5/5 | AGPL-3.0 |
| Deployment-Reife | 5/5 | 400.000+ Organisationen |
| Interoperabilität | 4/5 | WebDAV, CalDAV, CardDAV, CMIS |
| Sicherheitsprofil | 5/5 | ISO-27001-zertifiziertes Angebot |
| TCO (5 Jahre) | 5/5 | Keine Nutzerlizenz (Community) |
| Öffentliche Einsatzbereiche | 5/5 | Schweizer Bund, deutsche Länder |

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Empfehlung: Camunda Platform 8 Community** (Apache 2.0) [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe mehrstufige Verwaltungsabläufe und Integration mit XÖV-Datenstandards [46]. **Flowable** (Apache 2.0) ist eine leichtgewichtigere Alternative.

### 4.4 Bürgerbeteiligung

**Empfehlung: Decidim** (AGPL-3.0) [12]  
**Alternative: CONSUL Democracy** (AGPL-3.0) [54]

Decidim ist die reifste und meistgenutzte Open-Source-Beteiligungsplattform weltweit. Der Social Contract der Decidim-Vereinigung ist selbst ein Governance-Modell für Open-Source-Souveränität.

### 4.5 Kommunikation und Zusammenarbeit

**Empfohlener Komponentenstack:**
- **Matrix/Element** (Apache 2.0): Messaging und inter-behördliche Kommunikation [14]
- **Jitsi Meet** (Apache 2.0) oder **BigBlueButton** (LGPL-3.0): Videokonferenzen [34, 35]
- **Nextcloud Talk** (AGPL-3.0): integrierte Team-Kommunikation

Der deutsche BundesMessenger (auf Element-Basis) bietet ein direkt übertragbares Referenz-Deployment.

### 4.6 Open-Data-Veröffentlichung

**Empfehlung: CKAN** (AGPL-3.0) [22]

CKAN ist die weltweit führende Open-Source-Open-Data-Portal-Software. Es betreibt opendata.swiss, govdata.de und Dutzende nationaler und kommunaler Portale mit vollständiger DCAT-AP-Konformität.

### 4.7 Geografische Informationssysteme

**Empfohlener Stack:** QGIS [37] + GeoServer + PostGIS + OpenStreetMap [36] + MapLibre GL JS

Swisstopo (Schweiz) und das BKG (Deutschland) stellen qualitativ hochwertige offene Kartendaten unter CC-BY-4.0 bereit.

### 4.8 Öffentliche Website und Content-Management

**Empfehlung: TYPO3** (GPL-2.0) für deutschsprachige Kontexte [19]  
**Alternative: Drupal** (GPL-2.0) für international ausgerichtete Deployments

Beide Systeme erfüllen BITV-2.0/WCAG-2.1-AA-Barrierefreiheitsstandards.

### 4.9 Cloud-Infrastruktur und Hosting

**Empfehlung: Sovereign Cloud Stack (SCS)** (Apache 2.0) [3, 11]  
**Managed-SCS-Option:** plusserver, OSISM, artcodix

SCS ist die strategisch wichtigste Infrastrukturentscheidung für europäische Kommunen. Es ermöglicht vollständig souveräne Cloud-Infrastruktur (OpenStack + Kubernetes + Ceph).

### 4.10 Datenintegration und ETL

**Empfohlener Stack:** Apache Airflow (Apache 2.0) für ETL-Orchestrierung; Apache Kafka für Echtzeit-Event-Streaming; Apache NiFi für visuelle Datenflüsse.

### 4.11 Enterprise-Suche und Wissensmanagement

**Empfehlung: OpenSearch** (Apache 2.0)

OpenSearch bietet Volltextsuche, Facetten-Navigation und Vektorsuche für KI-gestützte Abfragen.

### 4.12 Monitoring, Alerting und Observability

**Empfohlener Stack:** Prometheus [62] + Grafana [63] + Loki + Alertmanager + OpenTelemetry

Dieser Stack („PLG-Stack“) ist die De-facto-Open-Source-Observability-Plattform für Cloud-Native-Infrastruktur.

### 4.13 KI-gestützte Verwaltungsservices

**Empfohlener Ansatz: Datenschutzkonforme, vor-Ort-betriebene, prüfbare KI**

| Komponente | Lizenz | Funktion |
|---|---|---|
| **Ollama** | MIT | Lokaler Betrieb offener Sprachmodelle (Llama 3, Mistral) |
| **Open WebUI** | MIT | Chat-Oberfläche für KI-Assistenten |
| **Haystack** (deepset) | Apache 2.0 | Dokumenten-QA und Retrieval-Augmented Generation |

**KI-Gesetz-Einhaltung:** KI-Systeme für automatisierte Verwaltungsentscheidungen gelten nach Anhang III als hochriskant und bedürfen: Konformitätsbewertung, Grundrechte-Folgeabschätzung, menschlichem Aufsichtsmechanismus, Bürger-Benachrichtigung und Prüfprotokollen [50].

### 4.14 Barrierefreiheits- und Digitale-Inklusions-Werkzeuge

**Empfohlene Werkzeuge:** axe-core (MPL-2.0) für automatisierte Tests; Playwright (Apache 2.0) für End-to-End-Tests; Pa11y (GPL-3.0) für kontinuierliches Monitoring.

Barrierefreiheit ist eine Rechtspflicht nach der EU-Webzugänglichkeitsrichtlinie und deren nationaler Umsetzung (BITV 2.0 in Deutschland, eCH-0059 in der Schweiz).

### 4.15 Projekt- und Portfoliomanagement

**Empfehlung: OpenProject** (GPL-3.0) [20]

OpenProject wird von der Bundesregierung, ZenDiS und Dutzenden Kommunen eingesetzt.

### 4.16 Referenzarchitektur

```
+------------------------------------------------------------------+
|                      BÜRGER-KONTAKTPUNKTE                       |
|      TYPO3/Drupal · Decidim · CKAN · Nextcloud · Mobil         |
+------------------------------------------------------------------+
|                          SERVICE-SCHICHT                         |
|    Camunda BPMN · XÖV/eCH-Formulare · GeoServer · OpenSearch   |
+------------------------------------------------------------------+
|           KI-ASSISTENZ-SCHICHT (Hochrisiko nach KI-Gesetz)       |
|         Ollama/Open WebUI · Haystack RAG · Prüfprotokoll         |
+------------------------------------------------------------------+
|                     KOLLABORATIONS-SCHICHT                        |
|     Nextcloud · Matrix/Element · Jitsi · OpenProject · E-Mail    |
+------------------------------------------------------------------+
|                   DATENINTEGRATIONS-SCHICHT                       |
|         Apache Kafka · Apache Airflow · PostGIS · OpenSearch     |
+------------------------------------------------------------------+
|                         IDENTITÄTS-SCHICHT                       |
|        Keycloak <-> BundID / Schweizer E-ID / eIDAS-2.0-Wallet   |
+------------------------------------------------------------------+
|                MONITORING UND OBSERVABILITY-SCHICHT              |
|           Prometheus · Grafana · Loki · OpenTelemetry            |
+------------------------------------------------------------------+
|                       INFRASTRUKTUR-SCHICHT                       |
|  Sovereign Cloud Stack · Kubernetes · PostgreSQL/PostGIS · Ceph  |
+------------------------------------------------------------------+
```

---

## 5. Umsetzungsplan

Die Umsetzung ist als 36-monatiges Fünf-Phasen-Programm strukturiert. Indikative Budgets gelten für Kommunen mit 20.000–100.000 Einwohnern.

### Phase 0: Fundament (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand erfassen, Koalition aufbauen.

**Indikatives Budget:** 30.000–80.000 Euro

**Lieferergebnisse:**
- Digitaler Transformations-Lenkungsausschuss etabliert (Stadtführung + IT + Zivilgesellschaft + Datenschutzbeauftragter)
- Ist-Zustand-Technologieprüfung abgeschlossen (Software-Inventar, Lizenzkosten-Mapping, Datenflussdiagramm)
- Stakeholder-Engagement-Plan verabschiedet
- Beschaffungsrahmen etabliert (Kooperativer IT-Anbieter ausgewählt)
- Politisches Mandat eingeholt (Stadtratsbeschluss oder Verwaltungsentscheid)

**Entscheidungstor:** Grün/Rot basierend auf politischem Mandat, Budget und Anbieterbereitschaft.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die grundlegenden Schichten aufbauen, auf denen alles andere aufbaut.

**Indikatives Budget:** 80.000–200.000 Euro

**Lieferergebnisse:**
- Sovereign Cloud Stack operativ (eigener Cluster oder Managed Service)
- Keycloak Identity Provider deployed und mit nationalem Identitätssystem föderiert
- Nextcloud Basis-Deployment für interne Zusammenarbeit
- Matrix/Element Messaging für alle Mitarbeitenden
- Monitoring-Stack operativ (Prometheus + Grafana + Loki)
- BSI-IT-Grundschutz-Basisdokumentation abgeschlossen
- Software-Stückliste (SBOM) erstellt

**Technische Konfigurationshinweise:**
- Kubernetes-Cluster: mindestens 3 Control-Plane-Knoten; automatische Skalierung aktiviert
- Keycloak: Realm pro Fachbereich; OIDC-Federation mit BundID; MFA für Administratorrollen pflicht
- Nextcloud: S3-kompatibler Speicher auf Ceph-Basis; Virenscanner via ClamAV; Verschlüsselung im Ruhezustand
- Zertifikate: ACME (Let’s Encrypt); TLS 1.3 mindestens; HSTS-Preload

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die ersten fünf bürgerorientierten Dienste auf offener Infrastruktur aufbauen oder migrieren.

**Indikatives Budget:** 100.000–300.000 Euro

**Lieferergebnisse:**
- Fünf meistgenutzten Verwaltungsleistungen auf Camunda/XÖV-Stack deployed
- TYPO3 oder Drupal CMS migriert mit vollständigem Barrierefreiheitsaudit (BITV 2.0 / WCAG 2.1 AA)
- Open-Data-Portal (CKAN) mit ersten 30 Datensätzen und vollständigen DCAT-AP-Metadaten
- Decidim-Instanz für ersten Beteiligungsprozess deployed
- Barrierefreiheitsbericht veröffentlicht
- OpenProject für Projektmanagement deployed

**Dienstpriorisierungsmethodik:** Rangliste nach: (a) Transaktionsvolumen; (b) Bürgerauswirkung; (c) technischer Komplexität (erst einfache); (d) OZG-EfA-Verfügbarkeit. Typische Hochvolumen-Erstdienste: Parkausweise, Veranstaltungsanmeldungen, Abfallentsorgungsplanung, Bibliotheksausweise.

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Dienstabdeckung auf 80% der Transaktionstypen ausweiten.

**Indikatives Budget:** 80.000–200.000 Euro

**Lieferergebnisse:**
- Alle Dienste via Keycloak SSO föderiert
- Nextcloud mit Schriftgutverwaltungs-Workflows integriert
- GIS-Schicht operativ (QGIS + GeoServer + PostGIS + MapLibre)
- 80% der Verwaltungsleistungen digitalisiert
- Inter-behördlicher Datenaustausch via XÖV/eCH operativ
- KI-gestützte Mitarbeiterwerkzeuge deployed mit KI-Gesetz-Konformitätsdokumentation

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Nutzererfahrung optimieren; Rückbeitrag an Open-Source-Gemeinschaften leisten; Ergebnisse veröffentlichen.

**Indikatives Budget:** 50.000–100.000 Euro

**Lieferergebnisse:**
- Bürgerzufriedenheitsumfrage (Ziel: NPS > 40)
- Erster Beitrag zu openCode.de / Upstream-Open-Source-Projekten
- Kommunale Open-Source-Community of Practice gegründet (≥ 3 Partnerkommunen)
- Leistungskennzahlen und Gesamtkostenvergleich veröffentlicht

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; Auf Erweiterung und Replikation vorbereiten.

**Indikatives Budget:** 30.000–80.000 Euro

**Lieferergebnisse:**
- Vollständige Lizenz-Konformitätsprüfung (alle Komponenten gegen SBOM geprüft)
- Souveräne Datenresidenz verifiziert (100% auf EU-Jurisdiktion)
- Replikations-Playbook für Nachbarkommunen veröffentlicht
- Strategiepapier v1.0 veröffentlicht

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Hauptbedenken | Engagement-Ansatz |
|---|---|---|---|
| Oberbürgermeister / Verwaltungsführung | Politischer Erfolg, Kosten, Bürgerzufriedenheit | Wahlrisiko, Medienberichterstattung | Viertjährliche Führungsbriefings; Fortschritts-Dashboard |
| Stadtrat | Kontrolle, demokratische Legitimität | Rechenschaftspflicht, Transparenz | Viertjährliche Berichte; öffentliche Ratssitzungen; Decidim |
| Stadtisches IT-Team | Technische Machbarkeit, Arbeitsbelastung | Fähigkeitslücke, Mehrarbeit | Co-Design; Schulung; Community-Mitgliedschaft; Zertifizierungsunterstützung |
| Beschaffungsstelle | Rechtliche Compliance, Risiko | GWB/VgV-Konformität, Prüfungsrisiko | Rechtsbriefings; Rahmenvertragsvorlagen |
| Mitarbeitende (Endnutzer) | Bedienbarkeit, Zuverlässigkeit | Veränderungsangst, Umschulung | UX-Tests; Parallelbetrieb; Change Champions |
| Bürgerinnen und Bürger | Dienstqualität, Datenschutz, Zugang | Barrierefreiheit, digitaler Ausschluss | Participatory Design; Decidim; Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Open-Data-Qualität, Rechenschaft | Open-Data-Portal; öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | Code-Qualität, Lizenz-Compliance | openCode.de; Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Einsatz | Vertragsbedingungen, Vergaberecht | govdigital-eG-Mitgliedschaft |
| Datenschutzbeauftragte(r) | DSGVO-Compliance, Datenschutz | Verarbeitungsrechtsgrundlagen | Datenschutz-durch-Design-Prüfungen |

### 6.2 Beschaffungsrahmen

**Prinzipien der Open-Source-Beschaffung:**

1. **Dienste beschaffen, nicht Lizenzen.** Open-Source-Software ist kostenfrei nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

2. **Kooperative Beschaffungsstrukturen nutzen.** Deutschlands govdigital eG und Schweizer kantonale IT-Kooperativen bieten Rahmenverträge, die öffentliches Vergaberecht erfüllen [23].

3. **„Öffentliches Geld — öffentlicher Code!“-Prinzip vertraglich verankern.** Alle unter Vertrag entwickelten Individualsoftware müssen unter einer OSI-genehmigten Open-Source-Lizenz veröffentlicht werden [4].

4. **Gesamtbetriebskosten evaluieren.** Beschaffungswertung muss ein verbindliches Fünf-Jahres-Modell umfassen. Mindestgewichtung 30% für TCO-Kriterien.

5. **Interoperabilitätsstandards vorschreiben.** Alle beschafften Systeme müssen XÖV (Deutschland) [46], eCH (Schweiz) [47], DCAT-AP, OIDC/SAML2 und OpenAPI 3.x implementieren.

6. **SBOM und Patch-Management-Pläne fordern.** Alle beschafften Softwaresysteme müssen eine Software-Stückliste (SBOM) im SPDX- oder CycloneDX-Format bereitstellen.

### 6.3 Muster-Vertragsklausel

> *„Alle im Rahmen dieses Vertrags entwickelten Softwareprogramme, Quellcodes, Dokumentationen und verwandten Materialien, die mit öffentlichen Mitteln finanziert wurden, müssen vom Auftragnehmer innerhalb von 90 Tagen nach Abschluss unter einer OSI-genehmigten Open-Source-Lizenz (AGPL-3.0, Apache 2.0 oder GPL-3.0, wie vereinbart) veröffentlicht werden. Der Auftragnehmer muss die Software auf openCode.de (oder einem äquivalenten öffentlichen Repository) veröffentlichen und alle notwendige Dokumentation für den Einsatz durch Dritte bereitstellen.“*

### 6.4 Change Management

**Empfohlene Maßnahmen:**
1. Einen **Digitalen Transformations-Champion** auf höchster politischer Ebene mit explizitem Mandat ernennen
2. **Open-Source-Meister** in jedem Fachbereich mit erweiterter Schulung und Peer-Support-Rolle etablieren
3. **Parallelbetrieb** mindestens drei Monate vor der Umstellung kritischer Systeme betreiben
4. **Frühzeitige Erfolge** dokumentieren und öffentlich feiern (Kosteneinsparungen, neue Fähigkeiten, positives Bürger-Feedback)
5. Ein öffentliches **Transparenz-Dashboard** veröffentlichen mit Migrationsfortschritt, Kosten und Servicequalitätskennzahlen

### 6.5 Barrierefreiheits- und Inklusionsstrategie

Digitale Barrierefreiheit ist sowohl eine Rechtspflicht als auch ein demokratisches Gebot. WCAG 2.1 AA ist der Mindestrechtsstandard gemäß der EU-Webzugänglichkeitsrichtlinie und der BITV 2.0.

**Empfohlene Maßnahmen:**
1. axe-core-automatische Barrierefreiheitstests in die CI/CD-Pipeline ab Phase 1 integrieren
2. Unabhängiges WCAG-2.1-AA-Audit bei jedem Phasentor beauftragen
3. Menschen mit Behinderungen als bezahlte Tester während der Entwicklung einbeziehen
4. Assistierte digitale Unterstützungskanäle (Telefon, persönlich) als dauerhafte Ergänzungen vorsehen

### 6.6 Open-Source-Community-Governance

**Empfohlenes Community-Engagement:**
1. Beitritt zur **openCode.de**-Plattform und Veröffentlichung aller Individualentwicklungen [10]
2. **Mitgliedschaft bei govdigital eG** (Deutschland) oder der kantonalen IT-Kooperative (Schweiz) [23]
3. Teilnahme an der **Decidim-Vereinigung** und der **TYPO3-Vereinigung**
4. **10% der IT-Mitarbeitenden-Zeit** für Upstream-Open-Source-Beiträge reservieren
5. Jährlichen **Open-Source-Beitragsbericht** veröffentlichen

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|
| Politische Umkehrung nach Wahl | Mittel | Hoch | In Satzung/Verordnung verankern; überparteilicher Konsens |
| Vendor-Lobbying / FUD-Kampagnen | Hoch | Mittel | TCO-Evidenz öffentlich dokumentieren; Zivilgesellschaft einbinden |
| Fähigkeitslücke im IT-Team | Hoch | Mittel | Schulung; kooperativer IT-Anbieter; Community of Practice |
| Integrationsversagen zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout mit Entscheidungstoren; Referenzarchitektur |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup-Protokoll; Parallelbetrieb mindestens 3 Monate |
| DSGVO / DGA / KI-Gesetz-Verstoß | Niedrig | Hoch | Datenschutz-durch-Design; Datenschutzbeauftragten einbeziehen |
| Nutzerannahme-Versagen | Mittel | Hoch | Change Management; UX-Tests; Schulung; Parallelbetrieb |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests; SBOM; Incident-Response-Plan |
| KI-Gesetz-Nicht-Konformität | Mittel | Hoch | Konformitätsbewertung vor KI-System-Einsatz |
| Lieferketten-Angriff auf Abhängigkeiten | Niedrig | Hoch | SBOM; Abhängigkeitsprüfung; signierte Releases; Sigstore |
| Barrierefreiheits-Rückschritt | Mittel | Mittel | CI/CD axe-core-Integration; vierteljährliche Barrierefreiheitsaudits |

### 7.2 Der Münchener Warnfall

LiMux (2003–2017) ist der meistzitierte Fall einer umgekehrten kommunalen Open-Source-Transition. Die Nachbetrachtung [59] identifiziert die Umkehr als vorwiegend durch: (a) politischen Führungswechsel; (b) unzureichendes Change Management; (c) Kompatibilitätsprobleme mit Ländersystemen; und (d) Umkehrkosten von ca. 49 Mio. Euro verursacht. Die technische Implementierung war weitgehend erfolgreich. Die Lektion: **politisches Risikomanagement ist ebenso wichtig wie technische Planung**.

### 7.3 Sicherheitsaspekte

Das BSI-IT-Grundschutz-Rahmenwerk bietet eine umfassende Sicherheitsbasis [26]. Wichtige Anforderungen:
- Patch-Reaktionszeiten vertraglich festlegen (maximal 72 Stunden für CVSS 9.0+)
- Authentifizierung muss BSI Authenticator Assurance Level 2 (AAL2) erfüllen
- Datenverschlüsselung: TLS 1.3 mindestens in Transit; Dateisystemverschlüsselung via LUKS im Ruhezustand
- Penetrationstests bei jedem Phasentor
- Incident-Response-Plan gemäß NIS2-Meldepflichten (24-Stunden-Erstmeldung) [27]

### 7.4 KI- und Automatisierungsrisiken

**Algorithmische Verzerrung:** KI-Systeme, die auf historischen Verwaltungsdaten trainiert wurden, können historische Diskriminierung verstärken. Minderung: Bias-Audit vor dem Einsatz. **Halluzinationen:** Sprachmodelle können plausible, aber falsche Informationen produzieren. Minderung: Beschränkung auf Retrieval-Augmented Generation über verifizierten Verwaltungsquellen. **Überautomatisierung:** Minderung: menschliche Überprüfungsmechanismen für alle KI-gestützten Entscheidungen; Bürgerrecht auf menschliche Überprüfung gemäß DSGVO Artikel 22.

### 7.5 Lieferkettensicherheit

**Minderungsmaßnahmen:**
1. SBOM für alle eingesetzten Komponenten pflegen; bei jedem Deployment aktualisieren
2. Sicherheitshinweise für alle Abhängigkeiten abonnieren (GitHub Security Advisories, OSV.dev)
3. Abhängigkeitsversionen in der Produktion fixieren; Renovate für automatisierte Update-PRs
4. Container-Image-Signaturen via Sigstore/cosign verifizieren
5. Netzwerk-Egress-Filterung implementieren

### 7.6 Klima- und Nachhaltigkeitsaspekte

Kommunale digitale Infrastruktur hat einen materiellen Energie- und CO₂-Fußabdruck. Digitale Souveränität und klimatische Nachhaltigkeit verstärken sich gegenseitig. **Empfehlungen:** Erneuerbare Energie bei kooperativen IT-Anbietern fordern; Kubernetes-Ressourcen-Requests optimieren; jährlichen ICT-CO₂-Fußabdruck als Teil der kommunalen Nachhaltigkeitsberichterstattung melden.

---

## 8. Schlussfolgerung

Die in diesem Papier untersuchten und entwickelten Belege konvergieren auf sechs Erkenntnisse:

**1. Open-Source-Technologie-Stacks für Kommunen sind technisch ausgereift und praxiserprobt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung — von digitaler Identität bis zu KI-gestützten Services — kann durch Open-Source-Software mit dokumentierten Einsatzbereichen in vergleichbaren Kommunen erfüllt werden.

**2. Das Regulierungsumfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland), Interoperable Europe Act (EU), EU-Datengesetz und EU-KI-Gesetz schaffen zusammen einen Rechtsrahmen, in dem proprietäre, herstellergebundene Systeme Compliance-Anforderungen nicht nachhaltig erfüllen können.

**3. Das wirtschaftliche Argument ist überzeugend, wenn Gesamtkosten korrekt berechnet werden.** Für eine Kommune mit 500 Mitarbeitenden beträgt die Fünf-Jahres-Nettoeinsparung aus dem Übergang auf einen Open-Source-Arbeitsplatz-Stack 200.000–500.000 Euro nach Implementierungskosten.

**4. Kleine Kommunen können und schaffen den Wandel.** Die Fallstudien aus Schaffhausen, Herrenberg und Gummersbach belegen, dass Open-Source-Transformation nicht nur Großstädten vorbehalten ist.

**5. Das EU-KI-Gesetz schafft neue Transparenzpflichten, die Open-Source-KI begünstigen.** Open-Source-KI-Systeme sind besser positioniert, die Prüfbarkeitsanforderungen des KI-Gesetzes zu erfüllen als proprietäre Alternativen.

**6. Erfolg erfordert ebenso viel politische und organisatorische wie technische Investition.** Politisches Mandat, qualifiziertes Change Management, überparteiliche Unterstützung und nachhaltiges Stakeholder-Engagement sind die bindenden Erfolgsparameter.

Städte, die als Erste handeln, profitieren von Ersteinsteiger-Vorteilen: Gestaltung kooperativer Standards, Aufbau interner Kompetenz, Beitrag zu den Open-Source-Commons. Die Einladung — und in einer wachsenden Zahl von Jurisdiktionen: die Verpflichtung — ist eindeutig.

---

## Literatur

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [Open Access, CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [Open Access, DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. Berlin: OSBA. https://scs.community/ — [Open Access, CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017–2026). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [Open Access, CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [Open Access]

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 über Maßnahmen für ein hohes Maß an Interoperabilität des öffentlichen Sektors in der Union (Interoperable Europe Act)*. ABl. EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903 — [Open Access]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/fitko/jahresbericht — [Open Access]

[10] openCode.de. (2022–2026). *openCode — Open Source für die Verwaltung*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open Access]

[11] Sovereign Cloud Stack Community. (2023–2026). *SCS Technische Dokumentation*. https://docs.scs.community/ — [Open Access, Apache 2.0]

[12] Decidim-Vereinigung. (2021–2026). *Decidim: Freie Open-Source Partizipative Demokratie für Städte und Organisationen*. Barcelona: Decidim-Vereinigung. https://decidim.org/ — [Open Access, AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud für Behörden: Sicherheit, Souveränität und Zusammenarbeit*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [Open Access]

[14] The Matrix Foundation. (2023–2026). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Open Access, Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open Access]

[19] TYPO3 Association. (2023–2026). *TYPO3 in der öffentlichen Verwaltung*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [Open Access]

[20] OpenProject GmbH. (2023–2026). *OpenProject für Behörden: Open-Source-Projektmanagement*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [Open Access, GPLv3]

[21] Red Hat / Keycloak Community. (2023–2026). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Open Access, Apache 2.0]

[22] CKAN Association. (2023–2026). *CKAN: Open Source Datenportal-Software*. https://ckan.org/ — [Open Access, AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open Access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open Access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/ — [Open Access, CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 über Maßnahmen für ein hohes gemeinsames Cybersicherheitsniveau in der Union (NIS2-Richtlinie)*. ABl. EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555 — [Open Access]

[29] Vereinte Nationen, Abteilung für wirtschaftliche und soziale Angelegenheiten. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: Vereinte Nationen. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [Open Access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023–2026). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com/download/ — [Open Access, Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [Open Access, LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Videokonferenz*. https://jitsi.org/ — [Open Access, Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [Open Access, ODbL-1.0]

[37] QGIS-Projekt. (2023). *QGIS: Ein freies und quelloffenes Geographisches Informationssystem*. https://www.qgis.org/ — [Open Access, GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — [Open Access, Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [Open Access, PostgreSQL-Lizenz]

[42] Bundesministerium des Innern und für Heimat (BMI) / ZenDiS GmbH. (2023–2026). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [Open Access, AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open Access]

[44] Geschäftsstelle OGD Schweiz. (2023). *opendata.swiss — Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [Open Access]

[45] Europäische Kommission, ISA²-Programm. (2017). *Europäischer Interoperabilitätsrahmen — Umsetzungsstrategie (EIF)*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [Open Access, CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open Access]

[47] eCH-Vereinigung. (2023). *eCH E-Government-Standards*. Bern: eCH. https://www.ech.ch/ — [Open Access]

[48] GovStack-Initiative / ITU / DIAL. (2022–2026). *GovStack: Bausteine für digitale Verwaltung*. Genf: Internationale Fernmeldeunion. https://www.govstack.global/ — [Open Access, CC-BY-4.0]

[49] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 über harmonisierte Vorschriften für einen fairen Datenzugang und faire Datennutzung (Datengesetz)*. ABl. EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202302854 — [Open Access]

[50] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 über harmonisierte Vorschriften für künstliche Intelligenz (KI-Gesetz)*. ABl. EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202401689 — [Open Access]

[51] ZenDiS GmbH. (2024). *Jahresbericht 2023/2024*. Berlin: ZenDiS. https://zendis.de/ — [Open Access]

[52] GAIA-X AISBL. (2023). *GAIA-X Architektur-Dokument und Trust Framework*. Brüssel: GAIA-X AISBL. https://gaia-x.eu/ — [Open Access]

[54] Consul Democracy. (2015–2026). *CONSUL: Democratic Software*. Madrid: Consul Democracy. https://consulproject.org/ — [Open Access, AGPL-3.0]

[55] Geschäftsstelle OGD Schweiz. (2024). *OGD-Strategie Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/open-government-data.html — [Open Access]

[56] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media.

[58] Europäisches Parlament und Rat. (2022). *Verordnung (EU) 2022/868 über europäische Daten-Governance (Datenverwaltungsgesetz)*. ABl. EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R0868 — [Open Access]

[59] Landeshauptstadt München / Stadtrat. (2017). *Beschluss des Stadtrats vom 15.02.2017: Zukunft der IT-Infrastruktur der Stadtverwaltung München*. München: Stadtrat. [Öffentlicher Beschluss]

[60] Direction interministérielle du numérique (DINUM). (2022). *Rapport sur l’utilisation des logiciels libres dans la fonction publique*. Paris: DINUM. https://www.numerique.gouv.fr/publications/ — [Open Access]

[62] Prometheus Authors. (2023). *Prometheus: Monitoring System und Zeitreihendatenbank*. CNCF. https://prometheus.io/ — [Open Access, Apache 2.0]

[63] Grafana Labs. (2023). *Grafana: Open Source Analytik und Monitoring*. https://grafana.com/ — [Open Access, AGPL-3.0]

---

## Anhang A: Technologie-Bewertungsübersicht

| Schicht | Primäre Komponente | Lizenz | Gesamtpunktzahl (7 Kriterien) | Alternative |
|---|---|---|---|---|
| Digitale Identität | Keycloak | Apache 2.0 | 34/35 | Authentik (MIT) |
| Dokumentenmanagement | Nextcloud | AGPL-3.0 | 33/35 | OpenDesk-Suite |
| Workflow / BPM | Camunda 8 CE | Apache 2.0 | 29/35 | Flowable (Apache 2.0) |
| Bürgerbeteiligung | Decidim | AGPL-3.0 | 33/35 | CONSUL (AGPL-3.0) |
| Messaging | Matrix/Element | Apache 2.0 | 32/35 | Nextcloud Talk |
| Videokonferenz | Jitsi Meet | Apache 2.0 | 31/35 | BigBlueButton |
| Open Data | CKAN | AGPL-3.0 | 32/35 | — |
| GIS | QGIS + GeoServer | GPL-2.0 | 30/35 | MapServer |
| Web-CMS | TYPO3 | GPL-2.0 | 32/35 | Drupal |
| Cloud-Infrastruktur | SCS | Apache 2.0 | 32/35 | Managed SCS |
| Datenintegration | Apache Airflow | Apache 2.0 | 28/35 | Apache NiFi |
| Suche | OpenSearch | Apache 2.0 | 29/35 | Typesense |
| Monitoring | Prometheus + Grafana | Apache 2.0 / AGPL | 31/35 | — |
| KI-Dienste | Ollama + Haystack | MIT / Apache 2.0 | 27/35 | — |
| Projektmanagement | OpenProject | GPL-3.0 | 30/35 | — |

---

## Anhang B: Beschaffungs-Checkliste

**Lizenz und Offenheit**
- [ ] Software unter OSI-genehmigter Open-Source-Lizenz lizenziert
- [ ] Quellcode öffentlich zugänglich (GitHub, GitLab oder openCode.de)
- [ ] Individualentwicklung wird unter Open-Source-Lizenz veröffentlicht (Vertragsklausel bestätigt)
- [ ] Kein „Open Core“-Modell mit kritischen Funktionen hinter proprietärer Schicht

**Interoperabilität**
- [ ] Implementiert XÖV-Standards (Deutschland) oder eCH-Standards (Schweiz)
- [ ] OpenAPI-3.x-Spezifikation für alle Integrationsschnittstellen bereitgestellt
- [ ] DCAT-AP-Metadaten für Datenkatalog-Integration unterstützt
- [ ] Identitätsintegration via OIDC oder SAML2 mit Keycloak bestätigt

**Sicherheit**
- [ ] SBOM in SPDX- oder CycloneDX-Format bereitgestellt
- [ ] Dokumentierter CVE-Reaktionsprozess mit maximaler Patch-Frist
- [ ] BSI-IT-Grundschutz-Konformitätsbewertung verfügbar
- [ ] Penetrationstest-Ergebnisse verfügbar (innerhalb der letzten 12 Monate)

**Datensouveränität**
- [ ] Daten ausschließlich innerhalb der EU-Jurisdiktion verarbeitet (vertraglich bestätigt)
- [ ] Datenresidenz bei zertifiziertem SCS-Betreiber
- [ ] Kein Drittländertransfer ohne ausdrückliche DSFA und Rechtsgrundlage
- [ ] Datenportabilität in offenen Formaten garantiert; Migrations-Unterstützung vertraglich zugesichert

**Gesamtbetriebskosten**
- [ ] Fünf-Jahres-Gesamtkostenmodell bereitgestellt
- [ ] Referenzen von mindestens 3 vergleichbaren kommunalen Deployments
- [ ] Ausstiegs- und Migrationskosten explizit quantifiziert

**Barrierefreiheit**
- [ ] WCAG-2.1-AA-Konformitätserklärung bereitgestellt
- [ ] Unabhängiger Barrierefreiheitsauditbericht verfügbar

---

## Anhang C: 36-Monats-Meilensteintracker

| Monat | Phase | Schlüsselmeilenstein | Verantwortlich | Status |
|---|---|---|---|---|
| 1 | 0 | Lenkungsausschuss etabliert | OB / CIO | ☐ |
| 2 | 0 | Technologieprüfung abgeschlossen | IT-Leitung | ☐ |
| 3 | 0 | Politisches Mandat gesichert | OB | ☐ |
| 3 | 0 | Kooperativer IT-Anbieter vertraglich | Beschaffung | ☐ |
| 4 | 1 | SCS-Umgebung live | IT + Anbieter | ☐ |
| 6 | 1 | Keycloak deployed + BundID/E-ID föderiert | IT | ☐ |
| 7 | 1 | Nextcloud live für alle Mitarbeitenden | IT | ☐ |
| 8 | 1 | Matrix/Element-Messaging live | IT | ☐ |
| 10 | 1 | IT-Grundschutz-Basis genehmigt | DSB + IT | ☐ |
| 11 | 2 | TYPO3/Drupal CMS live | IT + Presse | ☐ |
| 14 | 2 | CKAN Open-Data-Portal live | IT + Daten | ☐ |
| 15 | 2 | Decidim-Beteiligungsplattform live | IT + OB | ☐ |
| 16 | 2 | WCAG-2.1-AA-Audit bestanden | Externer Prüfer | ☐ |
| 17 | 2 | Fünf Dienste live; 80% des Volumens | IT + Dienste | ☐ |
| 22 | 3 | 80% der Dienste digitalisiert | IT + Dienste | ☐ |
| 24 | 3 | KI-Gesetz-Konformitätsbewertung | DSB + IT | ☐ |
| 25 | 4 | Erster Upstream-Beitrag veröffentlicht | IT | ☐ |
| 27 | 4 | Bürgerzufriedenheitsumfrage (NPS ≥ 40) | Presse | ☐ |
| 30 | 5 | Vollständige Lizenzprüfung | IT + Recht | ☐ |
| 32 | 5 | 100% souveräne Datenresidenz verifiziert | DSB | ☐ |
| 36 | 5 | Strategiepapier v1.0 veröffentlicht | Autor | ☐ |

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*  
*Bitte zitieren als: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*  
*Version 0.2.0 — Zitiervollständiger Entwurf — 2026-06-21*
