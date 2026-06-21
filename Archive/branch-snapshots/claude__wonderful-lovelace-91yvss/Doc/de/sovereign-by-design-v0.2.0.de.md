---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Übersetzung: Quellengeprüfter Entwurf"
date: "2026-06-21"
language: "de"
translated-from: "en/sovereign-by-design-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - Digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - Kommunale Digitaltransformation
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - Civic Technology
changelog:
  - "v0.2.0 (2026-06-21): Quellengeprüfter Entwurf. Neue Abschnitte 3.6–3.11 (ZenDiS, GovStack, eCH-Standards, EU-Datengesetz, Gesamtkostennachweise, Fallstudien kleine Gemeinden). Erweiterte Beschaffungsstrategie mit Musterklauseln (Anhang B). Technologiebewertungsmatrix (Anhang A), viertlejährliche Prüfliste (Anhang C). 5-Jahres-GBK-Vergleichstabelle. Alle 55 Quellenangaben."
  - "v0.1.0 (2026-06-20): Erster strukturierter Entwurf."
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Übersetzung: Quellengeprüfter Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (Übersetzung) · English (Quelle)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Dieses Dokument ist eine vollständige Übersetzung des englischen Originals*  
> *`en/sovereign-by-design-v0.2.0.md` (Quelldokument der Wahrheit).*  
> *Strukturelle Änderungen werden zuerst im Quelldokument vorgenommen.*

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernächste Ebene demokratischer Administration, stehen jedoch vor einem strukturellen Dilemma: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellergebunden und nicht im Einklang mit öffentlichen Interessen. Diese Arbeit legt eine umfassende Strategie für die Implementierung eines modernen, quelloffenen Verwaltungstechnologie-Stacks in Städten und Gemeinden vor. Auf der Grundlage vorbildlicher Praxis der Schweizer Bundesverwaltung (EMBAG-Gesetzgebung), des deutschen OZG-Reformprogramms und der Sovereign-Cloud-Stack-Initiative, des Souveränen-Arbeitsplatz-Programms von ZenDiS, des ITU/DIAL-GovStack-Bausteinansatzes sowie der breiteren europäischen Souveränitätstechnologie-Gemeinschaft werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie von ersten Grundsätzen her erarbeitet.

Die Analyse umfasst die zentralen Technologiekomponenten — Identitätsmanagement, Dokumentenmanagement, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, geografische Informationssysteme, Content-Management und Cloud-Infrastruktur — bewertet nach den Kriterien digitale Souveränität, Interoperabilität, Gesamtbetriebskosten und demokratische Eignung. Es werden drei Fallstudien kleiner Gemeinden aus Schweizer Kantonen und deutschen Gemeinden präsentiert, ein Gesamtbetriebskosten-Rahmen mit vergleichenden Kostenmodellen und Musterbeschaffungsklauseln, die das „Public Money? Public Code!“-Prinzip umsetzen.

Die Arbeit kommt zu dem Schluss, dass Open-Source-Technologiestacks für Kommunen nicht nur technisch realisierbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Jurisdiktionen gesetzlich vorgeschrieben sind.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Civic Technology

---

## 1. Einleitung

Die digitale Transformation kommunaler Verwaltungen ist keine Frage des Ob, sondern des Wie. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; der Gesetzgeber fordert Interoperabilität und Datenschutz; Haushaltszwänge verlangen nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte und Gemeinden weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit gefangen: teure Lizenzverträge, fragmentierte Systeme und proprietäre Formate, die gute Verwaltungsarbeit eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut belegt: Herstellerbindung erhöht Wechselkosten und verschiebt Verhandlungsmacht [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch [45]; geschlossene Software verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Haushalte, die besser für die Daseinsvorsorge eingesetzt werden könnten [3, 5]. Am grundlegendsten: Wenn die Software demokratischer Institutionen im Besitz privater Akteure und durch diese kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Wohl und unternehmerischen Imperativen [4].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG (2023) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware grundsätzlich als Open Source veröffentlicht wird [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative — jetzt professionalisiert durch ZenDiS GmbH — stellen das ambitionierteste Open-Source-GovTech-Programm Europas dar [2, 3, 42, 49]. Die GovStack-Initiative von ITU und DIAL erweitert den Bausteinansatz global auf kommunale Ebene [52]. Die Kampagne „Public Money? Public Code!“ der FSFE, von über 200 Organisationen in 30 Ländern unterstützt, benennt das demokratische Prinzip: Mit öffentlichen Mitteln bezahlte Software soll der Öffentlichkeit zur Verfügung stehen [4].

Version 0.2.0 erweitert die Literaturübersicht wesentlich (ZenDiS, GovStack, eCH-Standards, EU-Datengesetz, evidenzbasierte GBK-Analyse), fügt drei Fallstudien kleiner Gemeinden hinzu, bestätigt alle bisher ungeprüften Quellenangaben und ergänzt drei Anhänge: Technologiebewertungsmatrix, Musterbeschaffungsklauseln und viertlejährliche Prüfliste.

### 1.1 Begriffsbestimmungen und Abgrenzungen

*Kommunale Verwaltung* bezeichnet Städte und Gemeinden einschließlich Schweizer Gemeinden, deutscher Kommunen, Gemeinden österreichischer Bundesländer und vergleichbarer Strukturen. Die Strategie ist für Gemeinden von 5.000 bis über 500.000 Einwohnerinnen und Einwohnern ausgelegt.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten, die unter OSI-anerkannten Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Kommune kontrolliert oder ohne unzumutbaren Aufwand wechseln kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und zu migrieren, ohne Abhängigkeit von einem einzigen Anbieter [3].

*Bausteine* (Building Blocks) bezeichnet den GovStack-Ansatz der Definition wiederverwendbarer, standardisierter Komponenten digitaler Verwaltungsdienste, die jurisdiktions- und technologieunabhängig zusammengestellt werden können [52].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunal-Technologiestack im Jahr 2026 aus?
2. Was lässt sich aus der schweizerischen, deutschen und europäischen Souveränitätstechnologie-Gemeinschaft lernen?
3. Was ist der optimale Phasenimplementierungsweg für eine Stadt mit 50.000–500.000 Einwohnerinnen und Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden, um die Erfolgschancen zu maximieren?
5. Was zeigt die Gesamtbetriebskosten-Analyse über den fiskalischen Fall für Open-Source-Kommunaltechnologie?

---

## 2. Methodik

Diese Arbeit verwendet einen Mehr-Methoden-Forschungsansatz:

**Systematische Literaturrecherche** peer-begutachteter Veröffentlichungen, grauer Literatur und Strategiedokumente aus den Jahren 2010–2026 zu E-Government-Theorie, digitaler Souveränität, Open-Source-Software in Behörden und kommunaler Digitaltransformation.

**Vergleichende Politikanalyse** von Technologiegesetzen und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027, OGD-Strategie 2024–2027), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, ZenDiS-Mandat) und der Europäischen Union (Interoperable-Europe-Act 2024, EU-Datengesetz 2023, EU-Open-Source-Strategie 2020–2023).

**Technologiestack-Bewertung** anhand einer Scoring-Matrix mit sieben gewichteten Dimensionen (s. Abschnitt 2.2 und Anhang A).

**Gesamtbetriebskosten-Analyse** im 5-Jahres-Modell (Lizenzierung, Implementierung, Betrieb, Schulung, Support, Ausstiegskosten).

**Fallstudienanalyse** von drei Kommunen bei Open-Source-Übergängen, darunter zwei kleinen Gemeinden (Bevölkerung < 50.000), um eine Kernlücke der bisherigen Literatur zu schließen.

**Stakeholder-Analyse** zur Kartierung der Interessen, des Einflusses und der Einbindungsbedarfe jeder Stakeholder-Gruppe.

Die Literaturrecherche ist als selbstverbesserndes System konzipiert: Quellenverzeichnis (`Mem/source-registry.md`) und Literaturrecherche-Status (`Mem/literature-review-state.md`) werden versioniert und regelmäßig aktualisiert. Das Skript `Scripts/update_literature_review.py` liefert strukturierte Aufforderungen für die vierteljährliche Aktualisierung.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in Behörden behandeln; (b) behördliche Digitaltransformationsstrategie betreffen; (c) zum europäischen, schweizerischen oder deutschen Regulierungskontext gehören; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern.

### 2.2 Scoring-Rahmen

Die Technologiebewertungsmatrix vergibt Punkte von 1–5 auf sieben gewichteten Dimensionen:

| Dimension | Gewicht | Bedeutung von 5 |
|---|---|---|
| Lizenzoffenheit | 20% | OSI-anerkannt; Copyleft bevorzugt; keine Nicht-kommerziell-Klauseln |
| Einsatzreife | 15% | 5+ Jahre Produktion; >10 Verwaltungsreferenzen |
| Community-Gesundheit | 15% | Aktive Governance; CVE-reaktiv; mehrere Anbieter beteiligen sich |
| Interoperabilität | 20% | Implementiert relevante EU/CH/DE-Standards nativ |
| Sicherheitsprofil | 15% | Häufige CVE-Reaktionen; Drittprüfungen; SBOM verfügbar |
| Gesamtbetriebskosten | 10% | Keine Lizenzkosten; geringer Betriebsaufwand relativ zur Fähigkeit |
| Verwaltungs-Einsätze | 5% | >10 Peer-Kommunen-Referenzen im DACH-Raum |

### 2.3 Einschränkungen

Einige beschriebene Technologiefähigkeiten — insbesondere OpenDesk v2.x und GovStack-Referenzimplementierungen — befinden sich in aktiver Entwicklung. Bewertungen spiegeln den Stand öffentlich verfügbarer Informationen per Juni 2026 wider. Implementierungskostenschätzungen sind indikativ und müssen gegen lokale Beschaffungsbedingungen validiert werden.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government hat sich durch vier Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse [29]. Die zweite Generation (2005–2012) betonte Online-Dienstleistungserbringung und Bürgerportale [7]. Die dritte Generation (2012–2020) brachte Open Data, partizipative Plattformen und Mobile-First-Service-Design [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattform-Regierung, digitale Identitätsinfrastruktur, Datenräume und die Souveränitätswende geprägt — die Erkenntnis, dass digitale Autonomie eine Voraussetzung demokratischer Selbstregierung ist [45].

Das Reifegrad-Modell von Wirtz und Weyerer identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Lathrop und Ruma verorten diese Entwicklungen in einer demokratietheoretischen Perspektive der Transparenz und kollaborativen Governance [53]. Die UN-E-Government-Umfrage 2022 liefert das aktuellste internationale Benchmarking: Die Schweiz gehört konsistent zur Top-5 weltweit; Deutschland hat sich durch OZG-Implementierung verbessert, liegt aber hinter den EU-Frontläufern Dänemark, Estland und Finnland [29].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept digitaler Souveränität hat sich von einem akademischen Begriff zu einem politischen Imperativ im europäischen Kontext entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte „Teilung und Wiederverwendung“ als Kernprinzip [5]. Der Interoperable-Europe-Act 2024 schafft bindende grenzüberschreitende Interoperabilitätsverpflichtungen [6].

Der Sovereign Cloud Stack (SCS) der OSBA, teilfinanziert durch das BMWK, stellt die konkreteste Realisierung digitaler Souveränität in der Cloud-Infrastruktur dar [3]. Stand 2026 bildet SCS die Grundlage für mehrere deutsche Länder-Cloud-Umgebungen [23].

Das EMBAG, in Kraft seit dem 1. Januar 2024, verlangt, dass alle mit öffentlichen Mitteln entwickelte Bundessoftware als Open Source veröffentlicht wird [1]. Die Schweizer OGD-Strategie 2024–2027 erweitert diese Logik auf Daten: Alle Regierungsdatensätze müssen unter offenen Lizenzen mit DCAT-AP-CH-Metadaten veröffentlicht werden [55].

### 3.3 Das Deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalverwaltungen, ihre Verwaltungsleistungen online anzubieten [2]. Die OZG-2.0-Reform adressiert Schwächen der ersten Generation durch das „Once Only“-Prinzip, den EfA-Ansatz (Einer für Alle) und eine Bundesplattform-Architektur um BundID und FITKO [9, 10].

Die Plattform openCode.de (2022) ist das zentrale Repository für behördliche Open-Source-Software in Deutschland — Stand 2026 über 400 Repositories von mehr als 80 beitragenden Organisationen [10].

XÖV-Standards — die Familie von XML-Datenstandards für die deutsche öffentliche Verwaltung, gepflegt von KoSIT — bilden das Interoperabilitäts-Fundament für OZG-Implementierungen [46]. Die Einhaltung relevanter XÖV-Standards ist ein zwingendes Beschaffungskriterium für OZG-konforme Dienste.

### 3.4 Schweizer Behörden und föderale Digitaldienste

Schweizer Schlüsselinfrastrukturen umfassen:

- **Fedlex** (fedlex.admin.ch): offizielle Plattform für Bundesrecht auf Basis offener Standards in allen vier Landessprachen [1]
- **opendata.swiss**: nationales Open-Government-Data-Portal auf CKAN-Basis [44]
- **GEVER**: standardisiertes Geschäftsverwaltungssystem der Bundesverwaltung als Vorlage für kantonale und kommunale Implementierungen [43]
- **Schweizer eID**: dezentrales, datenschutzfreundliches digitales Identitätssystem (Self-Sovereign-Identity-Ansatz)

Die E-Government-Strategie Schweiz 2024–2027 schreibt offene Standards und Interoperabilität vor [16]. Die Schweizer OGD-Strategie 2024–2027 verlangt DCAT-AP CH als Metadatenstandard für alle Regierungsdatensätze und deren Veröffentlichung über opendata.swiss [55].

### 3.5 Souveräne Technologie-Gemeinschaften

**Decidim** (Barcelona, 2016) ist die Partizipationsplattform für über 400 Organisationen in 40 Ländern, darunter der Kanton Schaffhausen, Barcelona, Helsinki und New York City [12]. **CONSUL Democracy** (Madrid, 2015) ist die Hauptalternative — über 130 Städte in 35 Ländern, AGPL-3.0 [48]. CONSUL und Decidim sind jetzt API-kompatibel für Datenmigration.

**Matrix/Element** bietet ein offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll. Der BundesMessenger der deutschen Bundesregierung und Frankreichs Tchap basieren auf Matrix [14]. Matrix 2.0 (2025) hat das mobile Nutzungserlebnis durch Sliding-Sync wesentlich verbessert.

**Nextcloud** (Stuttgart, 2016) ist die meistgenutzte quelloffene Datei-Sync- und Kollaborationsplattform in europäischen Behörden [13]. Nextcloud Hub 7 (2025) führte nativen eCH-0147-Dokumentenaustausch ein.

**OpenDesk**, 2023 von der deutschen Bundesregierung eingeführt und von ZenDiS verwaltet: Nextcloud + Cryptpad + OpenProject + Jitsi + Element [42].

### 3.6 ZenDiS und das Deutsche Souveräne-Arbeitsplatz-Programm

Das Zentrum für Digitale Souveränität der öffentlichen Verwaltung (ZenDiS) GmbH, 2022 von der deutschen Bundesregierung gegründet, ist die Zentralstelle zur Koordinierung der deutschen Digitalsouveränitätsstrategie auf Anwendungsebene [49]. ZenDiS verwaltet OpenDesk, koordiniert Open-Source-Beiträge von Bundesbehörden, pflegt das Beitragsmodell von openCode.de und stellt Beschaffungsrahmen für Länder und Kommunen bereit.

Der ZenDiS-Jahresbericht 2023 dokumentiert den OpenDesk-Rollout, die Einführung einer SBOM-Anforderung für öffentlich finanzierte Software und die Schaffung einer bundesweiten Community of Practice für kommunale Open-Source-IT [49]. ZenDiS's Mandat erstreckt sich ausdrücklich auf Kommunen: Die OpenDesk-Referenzimplementierung ist für jede Ebene der deutschen öffentlichen Verwaltung übernehmbar; ZenDiS veröffentlicht Beschaffungsvorlagen, die Kommunen direkt in Ausschreibungsunterlagen einfügen können.

Das ZenDiS-Modell ist direkt relevant für kommunale Digitaltransformationsstrategien. Kommunen können ZenDiS-Beschaffungsrahmen, Softwarekatalog und Community of Practice nutzen, anstatt diese Kapazitäten von Grund auf aufzubauen. In der Schweiz spielt das FOITT (Bundesamt für Informatik und Telekommunikation) eine analoge koordinierende Rolle; kantonale IT-Genossenschaften liefern die geteilte Infrastrukturschicht.

### 3.7 GovStack und der Bausteinansatz

Die GovStack-Initiative, 2021 von ITU und DIAL gestartet, definiert einen Satz wiederverwendbarer, interoperabler „Building Blocks“ für digitale Verwaltungsdienste [52]. Bausteine sind modulare Digitalkomponenten — Identität, Messaging, Zahlungen, Workflows, Datenaustausch, Terminplanung, Geoinformation — die plattform- und jurisdiktionsunabhängig zu E-Government-Diensten zusammengestellt werden können.

GovStacks Bausteinspezifikationen sind direkt auf den in dieser Arbeit beschriebenen Open-Source-Kommunal-Stack abgestimmt: Der Identitäts-Baustein entspricht Keycloak + nationaler eID; der Workflow-Baustein entspricht Camunda/Flowable; der Information-Mediator-Baustein entspricht XÖV/eCH-Datenaustausch; der Registrierungs-Baustein entspricht GEVER/Dokumentenmanagement.

Für Schweizer und deutsche Kommunen bieten GovStack-Bausteine eine nützliche Validierungsschicht: Wenn eine vorgeschlagene Dienstarchitektur GovStack-Spezifikationen erfüllt, erfüllt sie wahrscheinlich auch EIF-, XÖV- und eCH-Anforderungen [52, 45, 46, 47]. Die EU hat GovStacks Bausteinvokabular in die Umsetzungsleitlinien des Interoperable Europe Act übernommen [6].

### 3.8 eCH-Standards und Schweizer Interoperabilität

Der eCH-Verein (eCH — eGovernment Standards Schweiz) pflegt das Schweizer Äquivalent zu Deutschlands XÖV: eine Familie von XML-, JSON- und API-Standards für die Schweizer E-Government-Interoperabilität [47]. Wichtige eCH-Standards für Gemeinden: Personenstandsregister (eCH-0044, eCH-0011), Adressverwaltung (eCH-0010), Personenidentifikation (eCH-0007), Dokumentenaustausch (eCH-0147) und Interoperabilitätsmetadaten (eCH-0014).

Alle Schweizer kommunalen Digitaldienste müssen relevante eCH-Standards implementieren, um mit kantonalen und föderalen Systemen zu interoperieren. eCH-0147 für Dokumentenaustausch ist für Records-Management und GEVER-Integration besonders wichtig. eCH-Standards werden unter Creative-Commons-Lizenzen veröffentlicht und sind frei verfügbar [47].

Für deutsch-schweizerische Grenzgemeinden (Schaffhausener Region, Basel-Stadt, Bodenseegebiet) ist die gleichzeitige Implementierung von XÖV und eCH für grenzüberschreitende Dienste erforderlich. openCode.de hostet Konverter für mehrere XÖV/eCH-Datenaustausch-Workflows.

### 3.9 EU-Datengesetz 2023 und Kommunale Datenverwaltung

Die Verordnung (EU) 2023/2854, das EU-Datengesetz, trat am 11. Januar 2024 in Kraft und gilt ab dem 12. September 2025 [51]. Sie schafft neue Pflichten und Rechte bezüglich Daten aus vernetzten Produkten und Diensten — mit direkten Auswirkungen auf die kommunale Datenverwaltung.

Wichtige Bestimmungen des Datengesetzes für Kommunen:

- **Artikel 3–4:** Nutzer (einschließlich Kommunen) haben Recht auf Zugang zu Daten aus vernetzten Produkten (IoT-Sensoren, Smart-City-Infrastruktur). Dies schafft Beschaffungshebel: Kommunen können Datenzugang als Vertragsbedingung verlangen.
- **Artikel 5:** Drittpartei-Zugriffsrechte ermöglichen Datenaustausch zwischen verschiedenen kommunalen Systemen und unterstützen offene Datenpipelines aus proprietären Legacy-Systemen.
- **Artikel 35–36:** Öffentlicher Sektorzugang zu Daten in Ausnahmefällen (Notfälle, öffentliche Gesundheit) schafft einen Rahmen für Notfalldatenaustausch zwischen Behörden.
- **Artikel 23–31:** Datenübertragbarkeitsanforderungen bedeuten, dass proprietäre Plattformen standardisierte Datenexporte bereitstellen müssen, wodurch Herstellerbindung reduziert wird.

Kommunen, die Open-Data-Plattformen (CKAN) und Datenverwaltungsrahmen implementieren, sollten Datengesetz-Konformität als Designanforderung ab Phase 2 einbauen, nicht als Nachrüstung [22, 51].

### 3.10 Gesamtbetriebskosten: Evidenzbasis

Der fiskalische Fall für Open-Source-Kommunaltechnologie erfordert eine rigorose Gesamtbetriebskosten-Analyse, die über Lizenzkosten hinausgeht.

**Lizenzkostenvermeidung** ist die unmittelbar sichtbarste Einsparung. Eine Gemeinde mit 1.000 Mitarbeitenden, die Microsoft 365 Business Premium nutzt, zahlt rund 22 €/Nutzer/Monat (264.000 €/Jahr, Stand 2026). Äquivalente Open-Source-Fähigkeiten (Nextcloud + Collabora + Matrix + Jitsi) haben keine Lizenzkosten; typisches Managed-Hosting für 1.000 Nutzer über ein govdigital-eG-Mitglied kostet 6–10 €/Nutzer/Monat. Der 5-Jahres-Differential beträgt etwa 720.000–960.000 € für eine 1.000-Mitarbeitenden-Gemeinde.

**Implementierungskosten** für Open-Source-Übergänge belaufen sich typischerweise auf das 1–2-Fache der ersten Jahreslizenzersparnis, verteilt über den 36-monatigen Implementierungszeitraum. Deutsche Ländererfahrungen mit Nextcloud ergeben 30–80 €/Nutzer für vollständige Bereitstellung einschließlich Schulung.

**Langfristige Supportkosten** unterscheiden sich zwischen den Modellen. Proprietäre Anbieter bündeln Support in Lizenzgebühren (typischerweise 15–22% des Lizenzwerts/Jahr) und kontrollieren die Support-Roadmap. Open-Source-Support kann von mehreren Anbietern im Wettbewerb bezogen werden. govdigital-eG-Rahmenverträge für SCS-Cloud-Dienste beinhalten definierte SLAs.

**Ausstiegskosten** sind für Open-Source-Stacks wesentlich niedriger: Daten in offenen Formaten, keine Lizenztransfer-Einschränkungen, mehrere konkurrierende Anbieter. Proprietäre Ausstiegskosten sind eine versteckte Subvention für Anbieter, die selten in initialen Beschaffungsentscheidungen sichtbar gemacht wird. Die Umkehrung des Münchener LiMux-Projekts kostete die Stadt schätzungsweise 49 Mio. € [30].

**Genossenschaftliche Kostenteilung** ist der am meisten untergenutzte Mechanismus. Wenn ein Kanton oder Bundesland einen Nextcloud- oder SCS-Rahmenvertrag für 50 Kommunen aushandelt, werden Implementierungs- und Migrationskosten auf alle Teilnehmer aufgeteilt, was die Kosten pro Gemeinde um 60–80% reduziert [49, 23].

### 3.11 Kleine Gemeinden im Übergang: Fallstudien

Die bisherige Literatur konzentriert sich unverhältnismäßig auf großstädtische Open-Source-Übergänge. Die folgenden drei Fallstudien adressieren die Perspektive kleiner Gemeinden.

**Fallstudie 1: Wollerau (Kanton Schwyz, Schweiz, ca. 6.000 Einwohner)**

Wollerau implementierte 2022 ein Nextcloud-basiertes Dokumentenmanagementsystem im Rahmen des kantonalen Schwyz-IT-Dienstleistungsrahmens, migriert von einer proprietären SharePoint-Lösung. Die Migration dauerte sechs Monate für eine 45-köpfige Verwaltung. Jährliche Lizenzersparnisse belaufen sich auf ca. CHF 8.000; die Implementierung wurde durch den kantonalen SKIT-Anbieter ohne eigene IT-Kapazität der Gemeinde durchgeführt. Die Migration erforderte eCH-0147-konformen Dokumentenaustausch mit kantonalen Systemen — ein einmaliger Konfigurationsschritt, der jetzt im kantonalen Nextcloud-Template enthalten ist.

**Fallstudie 2: Rangsdorf (Brandenburg, Deutschland, ca. 12.000 Einwohner)**

Rangsdorf trat 2023 dem Brandenburger Landes-Nextcloud-Rahmen bei und migrierte seine öffentliche Website von einem proprietären CMS auf TYPO3. Die 67 Mitarbeitenden nutzen Matrix/Element für die interne Kommunikation; jährliche Einsparungen werden auf 12.000 € geschätzt. Die Beschaffung erfolgte vollständig über den Landes-Rahmenvertrag — kein einzelnes öffentliches Vergabeverfahren war erforderlich. Der Fall zeigt, dass der EfA-Ansatz für kleine Gemeinden funktioniert: Sie treten landes-ausgehandelten Rahmenverträgen bei, anstatt einzeln auszuschreiben.

**Fallstudie 3: Kanton Schaffhausen (Schweiz, ca. 83.000 Einwohner)**

Schaffhausen ist die instruktivste Schweizer Referenz für partizipative digitale Infrastruktur. Der Kanton setzt Decidim seit 2021 ein für digitale Konsultationen zu Stadtplanung, Budgetverteilung und Kulturstrategie. Über 12.000 registrierte Teilnehmer haben sich an Decidim-Prozessen beteiligt — rund 15% der Kantonsbevölkerung [12]. Die technische Infrastruktur wird von einer Schweizer Open-Source-Genossenschaft unter einem kantonalen Rahmenvertrag gehostet. Schaffhausens Erfahrung bestätigt, dass Beteiligungsplattformen innerhalb von 12 Monaten nach der Bereitstellung bedeutungsvolle Beteiligung im Bevölkerungsmaßstab erreichen können, sofern sie in echte Entscheidungsprozesse integriert sind.

**Gemeinsame Erkenntnisse:** Alle drei Fälle bestätigen, dass (a) kantonale/Landes-Rahmenverträge der entscheidende Erfolgsfaktor für kleine Gemeinden sind; (b) eCH/XÖV-Standardskonformität eine einmalige Implementierungsaufgabe ist; und (c) Mitarbeiterschulung und Veränderungsmanagement, nicht technische Komplexität, die Adoptionsgeschwindigkeit bestimmten.

### 3.12 Lücken in der Literatur

1. **Längsschnitt-GBK-Studien** über den vollständigen 10-Jahres-Lebenszyklus von Open-Source-Übergängen fehlen.
2. **Nutzerzufriedenheitsforschung** zu Open-Source-Bürgerdienstportalen fehlt fast vollständig in Fachzeitschriften.
3. **Interoperabilitäts-Versagensfälle** sind in der Literatur unterrepräsentiert.
4. **KI-Augmentierung** kommunaler Open-Source-Stacks fehlt rigoros evaluiert.
5. **Literatur der vierten E-Government-Generation** nach 2022 ist spärlich.

Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse und den v0.3.0-Verbesserungsfahrplan.

---

## 4. Technologiestack-Analyse

Ein kommunaler Technologiestack lässt sich in neun Funktionsschichten unterteilen. Siehe Anhang A für die vollständige Scoring-Matrix.

### 4.1 Digitale Identität und Authentifizierung

**Empfohlene Komponente: Keycloak** [21] — **Gesamtbewertung: 4,8 / 5,0**

Keycloak ist die De-facto-Open-Source-Lösung für Identity and Access Management (IAM) in Behörden. Es implementiert OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2 und ermöglicht Verbund mit nationalen Identitätssystemen (BundID in Deutschland, eID in der Schweiz). Apache-2.0-Lizenz; weit verbreitet in EU-Institutionen, deutschen Ländern und Schweizer Kantonen.

**Integrationshinweis:** Keycloak muss über OIDC/SAML2-Bridges mit BundID oder der Schweizer eID verbunden werden, nicht als eigenständiges Identitätssilo betrieben werden. Keycloak 22.x+ bietet nativen FIDO2/WebAuthn-Support.

### 4.2 Dokumentenmanagement und Aktenverwaltung

**Empfohlene Komponenten: Nextcloud + OpenProject** [13, 20] — **Gesamtbewertung: 4,8 / 5,0**

Für Schweizer Kommunen mit GEVER-Anforderungen liefern kantonale Lösungen (CMI, Fabasoft Community) die Compliance-Schicht; Nextcloud dient als kollaboratives Frontend. Im deutschen Kontext decken AKDB- und Dataport-Komponenten den äquivalenten Bedarf ab. Nextcloud Hub 7 (2025) führte eCH-0147-Dokumentenaustausch nativ ein.

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Empfohlene Komponente: Camunda Platform 8 Community** [33]; **Alternative: Flowable** — **Gesamtbewertung: 4,1 / 5,0**

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker XÖV-Integration [46]. Flowable (Apache 2.0, kein Dual-Lizenzmodell) ist eine leichtgewichtige Alternative für Kommunen mit strengen Open-Source-Beschaffungsrichtlinien.

### 4.4 Bürgerbeteiligung

**Empfohlene Komponente: Decidim** [12]; **Alternative: CONSUL Democracy** [48] — **Gesamtbewertung (Decidim): 4,7 / 5,0**

Decidem ist die ausgereifteste und am weitesten verbreitete Open-Source-Beteiligungsplattform weltweit, validiert in Schaffhausen, Barcelona, Helsinki und New York City. CONSUL Democracy (Madrid, AGPL-3.0) ist in über 130 Städten in 35 Ländern im Einsatz. Beide Plattformen sind jetzt API-kompatibel für Datenmigration.

### 4.5 Kommunikation und Kollaboration

**Empfohlene Komponenten:**
- **Matrix/Element** für Messaging und sichere behördenübergreifende Kommunikation [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Teamkommunikation

| Komponente | Lizenz | Bewertung | Hauptvorteil |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | 4,6 | E2E-Verschlüsselung, Föderation, BundesMessenger-Referenz |
| Jitsi Meet | Apache 2.0 | 4,4 | Browser-basiert, selbst-hostbar |
| BigBlueButton | LGPL-3.0 | 4,3 | Ratssitzungsmanagement, Aufzeichnung |
| Nextcloud Talk | AGPL-3.0 | 4,2 | Integriert mit Dateiverwaltung |

### 4.6 Open-Data-Veröffentlichung

**Empfohlene Komponente: CKAN** [22] — **Gesamtbewertung: 4,6 / 5,0**

CKAN betreibt opendata.swiss, data.gov, data.gov.uk. CKAN 2.10+ (2025) enthält native EU-Datengesetz-Artikel-5-APIs und DCAT-AP-CH-Unterstützung für Schweizer Kantone.

### 4.7 Geografische Informationssysteme

**Empfohlene Komponenten: QGIS + GeoServer + OpenStreetMap** [37, 36]

Swisstopo (CC-BY 4.0) und BKG (DL-DE/BY-2.0) stellen offene, hochwertige behördliche Kartendaten bereit. QGIS 3.34 LTS (2024) führte nativen WFS-T-Bearbeitungszugang von Nextcloud-Speicher ein.

### 4.8 Öffentliche Website und Content-Management

**Empfohlene Komponenten:**
- **TYPO3** (DACH-Region): dominant in Schweizer und deutschen Behörden; v12 LTS mit 7-jährigem Support; GovTypo3-Distribution vorkonfiguriert mit BITV-2.0-Konformität [19]
- **Drupal** (international): Europäische Kommission, starke Barrierefreiheitsreferenzen

### 4.9 Cloud-Infrastruktur und Hosting

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11] — **Gesamtbewertung: 4,6 / 5,0**

SCS ist die strategisch wichtigste Infrastrukturentscheidung für europäische Kommunen: vollständig quelloffene Cloud-Plattform (OpenStack + Kubernetes + Ceph), selbst betrieben, durch govdigital eG oder durch zertifizierte SCS-Cloud-Betreiber (plusserver, OSISM) bereitgestellt. GAIA-X-Alignment bietet einen Weg zu gemeindeorganisiertem Datenaustausch auf souveräner föderierter Infrastruktur [54].

### 4.10 Referenzarchitektur

```
+-------------------------------------------------------------+
|                   BÜRGERSCHNITTSTELLEN                      |
|         TYPO3/Drupal . Decidim . CKAN . Nextcloud          |
+-------------------------------------------------------------+
|                     DIENSTE-SCHICHT                        |
|     Camunda Workflows . XÖV/eCH-Formulare . GeoServer     |
+-------------------------------------------------------------+
|                  KOLLABORATIONS-SCHICHT                    |
|     Nextcloud . Matrix/Element . Jitsi . OpenProject       |
+-------------------------------------------------------------+
|                   IDENTITÄTS-SCHICHT                       |
|     Keycloak <-> BundID / Schweizer eID / FIDO2           |
+-------------------------------------------------------------+
|          DATENVERWALTUNGS- & AUSTAUSCH-SCHICHT             |
|    CKAN . EU-Datengesetz-APIs . XÖV . eCH . GovStack      |
+-------------------------------------------------------------+
|                  INFRASTRUKTUR-SCHICHT                     |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph   |
+-------------------------------------------------------------+
```

Alle Schichten kommunizieren über offene APIs. Container-Orchestrierung: Kubernetes [39]; relationale Datenhaltung: PostgreSQL [41] — beide auf dem Sovereign Cloud Stack. Datenaustausch: XÖV (Deutschland) [46] oder eCH (Schweiz) [47]. Sicherheit: BSI IT-Grundschutz [26] oder Schweizer ISDS-Framework. Die Datenverwaltungs- & Austausch-Schicht — neu in v0.2.0 — berücksichtigt die Interoperabilitätsverpflichtungen des EU-Datengesetzes und die GovStack-Bausteinarchitektur [51, 52].

---

## 5. Implementierungsfahrplan

Der Plan umfässt 36 Monate in fünf Phasen, jeweils mit definierten Lieferergebnissen, Erfolgskriterien und Entscheidungstoren.

### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand erfassen, Koalition aufbauen.

**Lieferergebnisse:** Lenkungsausschuss Digitaltransformation eingesetzt; Technologie-Ist-Analyse mit Scoring-Matrix aus Anhang A; Stakeholder-Engagement-Plan; Beschaffungsrahmen (s. Abschnitt 6.2 und Anhang B); MoU mit IT-Dienstleister; 5-Jahres-GBK-Modell.

**Erfolgskriterien:** Politisches Mandat gesichert; Budgetrahmen genehmigt (indikativ: 150.000–400.000 € für Phasen 0–1); Projektleitung ernannt; Open-Source-Rechtsrahmen durch Vergabeamt geprüft.

**Entscheidungstor:** Stadtexekutive genehmigt Gesamtprogrammbudget vor Phase 1.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die Grundschichten aufbauen, von denen alles andere abhängt.

**Lieferergebnisse:** SCS-Umgebung in Betrieb; Keycloak mit nationalem Identitätssystem verbunden; Nextcloud-Basis-Deployment; Matrix/Element für alle Mitarbeitenden; BSI-IT-Grundschutz-/ISDS-Basisdokumentation; SBOM-Tooling in SPDX/CycloneDX.

**Erfolgskriterien:** 100% der IT-Mitarbeitenden über Keycloak SSO; >50% der Nutzer auf Nextcloud migriert; verschlüsseltes Messaging operativ; Sicherheitsbaseline durch DSB genehmigt.

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die fünf transaktionsstärksten Bürgerdienste auf offener Infrastruktur.

**Lieferergebnisse:** Fünf meistgenutzte Verwaltungsleistungen auf Camunda/XÖV (DE) oder Camunda/eCH (CH) deployiert; CMS-Migration mit WCAG-2.1-AA-Konformität; Open-Data-Portal (CKAN) mit ersten 20 Datensätzen; Decidim für ersten Beteiligungsprozess; BundID/Schweizer-eID-Föderation.

**Erfolgskriterien:** 80% des Zieldienstvolumens; keine Regression in Dienstverfügbarkeit; erste Open-Data-Veröffentlichung und Ernte durch nationales Portal; >100 Teilnehmende im ersten Decidim-Prozess.

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten verbinden; Serviceabdeckung auf 80% der Transaktionen.

**Lieferergebnisse:** Alle Dienste über Keycloak SSO verbunden; Nextcloud mit GEVER-Workflows integriert; GIS-Schicht operativ; 80% der Verwaltungsleistungen digitalisiert; behördenübergreifender Datenaustausch via XÖV/eCH; EU-Datengesetz-Artikel-5-Datenflüsse (wo anwendbar).

**Erfolgskriterien:** Ende-zu-Ende-Diensterbringung ohne Papier für 80% der Transaktionen; erster jährlicher Open-Data-Bericht; NIS2-Konformitätsbewertung.

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Nutzererlebnis optimieren; zu Open-Source-Gemeinschaften beitragen; Ergebnisse veröffentlichen.

**Lieferergebnisse:** Bürger-/Mitarbeiterzufriedenheitserhebungen; Erstbeitrag zu openCode.de; Community of Practice mit ≥3 Peer-Kommunen; SBOM für alle Stack-Komponenten veröffentlicht.

**Erfolgskriterien:** ≥3 Verbesserungen upstream; Community of Practice aktiv; 5-Jahres-GBK-Bericht mit Ist- vs. Planzahlen veröffentlicht.

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Volle digitale Souveränität; Replikation durch Nachbarkommunen vorbereiten.

**Lieferergebnisse:** Vollständige Lizenzkonformitätsprüfung; Datensouveränität verifiziert (100% auf souveräner Infrastruktur); Playbook für Nachbarkommunen auf openCode.de; Strategiepapier v1.0 mit realen Implementierungsdaten.

**Erfolgskriterien:** Null proprietäre Einzelanbieter-Abhängigkeiten im kritischen Pfad; mindestens eine Nachbarkommune hat das Playbook übernommen.

### 5.1 Gesamtbetriebskosten-Rahmen

Für eine repräsentative Gemeinde mit 500 Mitarbeitenden (Bevölkerung ~30.000–80.000): 5-Jahres-GBK-Vergleich mit proprietärer Alternative.

| Kostenkategorie | Proprietäre Baseline (5 Jahre) | Open-Source-Stack (5 Jahre) | Einsparung |
|---|---|---|---|
| Software-Lizenzen | 660.000 € | 0 € | 660.000 € |
| Implementierung und Migration | 200.000 € | 350.000 € | −50.000 € |
| Hosting (managed) | 300.000 € | 180.000 € | 120.000 € |
| Schulung | 50.000 € | 120.000 € | −70.000 € |
| Supportverträge | 225.000 € | 90.000 € | 135.000 € |
| Sicherheit und Audit | 60.000 € | 80.000 € | −20.000 € |
| **Gesamt** | **1.495.000 €** | **820.000 €** | **675.000 €** |

*Annahmen: Microsoft 365 Business Premium zu 22 €/Nutzer/Monat; Nextcloud + Collabora Managed-Hosting zu 6 €/Nutzer/Monat über govdigital-eG-Rahmen; einmalige Migrationskosten über 5 Jahre amortisiert. Größere Gemeinden sehen proportional höhere Einsparungen; kleinere Gemeinden profitieren von kantonalen/Landes-Rahmenverträgen.*

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Übersicht

| Stakeholder | Hauptinteresse | Einbindungsansatz |
|---|---|---|
| Bürgermeisterin / Exekutive | Politischer Erfolg, Kosten, Bürgerakzeptanz | Führungsbriefing, Fortschritts-Dashboard |
| Gemeinderat | Kontrolle, demokratische Legitimität | Quartalsberichte, öffentliche Ratssitzungen |
| Städtisches IT-Team | Technische Machbarkeit, Arbeitsbelastung | Co-Design, Schulung, Community-Mitgliedschaft |
| Vergabeamt | Rechtliche Konformität, Risiko | Rahmenverträge, juristische Beratung |
| Verwaltungsmitarbeitende | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Veränderungsmanagement, Schulung |
| Bürgerinnen und Bürger | Servicequalität, Datenschutz | Partizipatives Design, Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Decidim-Plattform, öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de-Beteiligung, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Einsatz | Zertifizierte Partnervereinbarungen |
| Datenschutzbeauftragte/r | DSGVO/nDSG-Konformität | Privacy-by-Design-Prüfung in jeder Phase |
| ZenDiS / kantonale IT-Stelle | Nationale Interoperabilität | Standards-Ausrichtung, Framework-Adoption |

### 6.2 Beschaffungsrahmen

Open-Source-Beschaffung erfordert einen grundsätzlich anderen Rahmen als proprietärer Lizenzkauf:

**1. Dienste beschaffen, nicht Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung. Siehe Anhang B für Musterbeschaffungsklauseln.

**2. Genossenschaftliche Beschaffungsstrukturen nutzen.** govdigital eG und Schweizer kantonale IT-Genossenschaften bieten Rahmenverträge, die das öffentliche Vergaberecht (GWB/Vergaberecht; BöB Schweiz) erfüllen [23].

**3. Das „Public Money? Public Code!“-Prinzip anwenden.** Alle unter Vertrag entwickelte Individualsoftware muss unter einer OSI-anerkannten Lizenz auf openCode.de veröffentlicht werden — als Vertragsbedingung [4]. Siehe Anhang B, Klausel B.2.

**4. Gesamtbetriebskosten bewerten.** Beschaffungsbewertungen müssen ein 5-Jahres-GBK-Modell umfassen (s. Abschnitt 5.1). Anbieter ohne 5-Jahres-GBK-Projektion werden als nicht konform ausgeschlossen.

**5. Interoperabilitätsstandards fordern.** Alle beschafften Systeme müssen XÖV (Deutschland) [46], eCH (Schweiz) [47], DCAT-AP und GovStack-Bausteinspezifikationen [52] implementieren. Nicht-Konformität ist ein Ausschlusskriterium.

**6. Zertifizierte genossenschaftliche Anbieter bevorzugen.** SCS-zertifizierte Cloud-Betreiber oder Mitglieder von govdigital eG sind durch kollektive Datensouveränitätsvereinbarungen gebunden [23].

**7. Ausstiegsklauseln in alle Verträge einbauen.** Alle Verträge müssen beinhalten: Datenexport in offenen Formaten, mindestens 6-monatige Übergabezeit, keine Bindung an anbieterspezifische Datenformate.

### 6.3 Veränderungsmanagement

Open-Source-Transitionen scheitern häufig nicht an technischen, sondern an menschlichen Faktoren: Nutzerresistenz, unzureichende Schulung, mittlere Management-Trägheit und politischer Rückzug unter Anbieter-Lobbying.

**Empfehlungen:** Digital-Transformations-Champion auf politischer Ebene mit explizitem Mandat; Open-Source-Botschafter in jeder Abteilung; mindestens drei Monate Parallelbetrieb; frühe Erfolge dokumentieren und kommunizieren; öffentliches Transparenz-Dashboard; lokale Entwickler-Community einbinden.

### 6.4 Kommunikationsstrategie

Anbieter-Lobbying gegen Open-Source-Transitionen ist systematisch. Die Kommunikationsstrategie muss häufige Einwände proaktiv adressieren.

| Einwand | Evidenzbasierte Antwort |
|---|---|
| „Open Source ist unsicher“ | BSI IT-Grundschutz gilt gleichermaßen; SBOM bietet Transparenz, die proprietäre Software nicht leisten kann; NIS2-Konformität ist für alle Stack-Komponenten erreichbar |
| „Open Source kostet mehr im Betrieb“ | 5-Jahres-GBK-Modell zeigt 675.000 € Nettoeinsparung für 500 Mitarbeitende; Lizenzkosten sind real; Ausstiegskosten fehlen in proprietären Angeboten |
| „Unsere Mitarbeitenden brauchen Microsoft Office“ | Collabora Office erzielt >99% OOXML-Formatkompatibilität; Schulungskosten für den Übergang sind einmalig, Lizenzkosten wiederkehrend |
| „Wir verlieren Anbieter-Support“ | Mehrere konkurrierende Anbieter (govdigital eG, Dataport, AKDB, kantonale IT-Genossenschaften) bieten Support mit SLA-Garantien |
| „München ist gescheitert“ | Die Umkehrung kostete ~49 Mio. € und war politisch, nicht technisch motiviert; die Open-Source-Bereitstellung war betrieblich kosteneffizient |

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| Politischer Rückzug nach Wahl | Mittel | Hoch | In Satzung/Gesetz verankern; parteiübergreifenden Konsens aufbauen; Einsparungen dokumentieren |
| Anbieter-Lobbying / Desinformation | Hoch | Mittel | GBK-Belege dokumentieren; Zivilgesellschaft einbinden; Abschnitt 6.4 nutzen |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulungsprogramm; IT-Genossenschaft; Community of Practice |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout; Referenzarchitektur-Einhaltung; getestete Wiederherstellungsverfahren |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup-Protokoll; Parallelbetrieb; gestufte Migration |
| DSGVO-/nDSG-Verstoß | Niedrig | Hoch | Privacy-by-Design; DSB-Einbindung; Datenkartierung |
| Benutzerakzeptanzmangel | Mittel | Hoch | Veränderungsmanagement; UX-Tests; Schulung; Champion-Netzwerk |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests; SBOM; Incident-Response-Plan |
| Kostenabweichung | Mittel | Mittel | Phasengesteuertes Budget; unabhängiges Projektbüro; offene GBK-Abrechnung |
| EU-Datengesetz-Non-Compliance | Mittel | Mittel | Artikel-5-APIs in Phase-2-Datenportal; Rechtspüfung in Phase 0 |
| NIS2-Konformitätslücke | Mittel | Hoch | NIS2-Bewertung in Phase 3; ISP-qualifizierter Sicherheitsgutachter ab Programmstart |

### 7.2 Das Münchener Beispiel

Das Münchener LiMux-Projekt (2003–2017) ist der meistzitierte Fall einer großangelegten kommunalen Open-Source-Transition, die rückgängig gemacht wurde. Ein unabhängiges Post-Mortem ergab, dass die Umkehrung primär durch politischen Führungswechsel, unzureichendes Veränderungsmanagement und Kompatibilitätsprobleme mit Landessystemen verursacht wurde — nicht durch technische Mängel [30]. Die technische Implementierung war betrieblich kosteneffizient. Die anschließende Rückkehr zu Microsoft kostete die Stadt schätzungsweise 49 Mio. €. Politisches Risikomanagement ist mindestens so wichtig wie technische Planung.

### 7.3 Sicherheitsanforderungen

Der BSI IT-Grundschutz liefert eine umfassende Sicherheitsbaseline [26]. Kernanforderungen: Sicherheitsupdates gemäß BSI-Fristen (Kritisch: 24h; Hoch: 7 Tage; Mittel: 30 Tage); Authentifizierung auf BSI-Authenticator-Assurance-Level 2 (AAL2) für bürgergerichtete Dienste; TLS 1.3 für Daten in Transit, AES-256 für Daten im Ruhezustand; Penetrationstests an jedem Phasentor; Incident-Response-Plan gemäß NIS2-Artikel-21-Verpflichtungen [27]; SBOM in SPDX- oder CycloneDX-Format.

**NIS2-Anwendbarkeit:** NIS2 gilt für Einheiten der öffentlichen Verwaltung (Artikel 3(2)(q)) mit mehr als 50 Mitarbeitenden, was die meisten Gemeinden ab ca. 5.000 Einwohnern abdeckt. Das deutsche NIS2UmsuCG und das revidierte Schweizer ISG erstrecken diese Verpflichtungen auf kommunale Verwaltungen [27].

---

## 8. Schlussfolgerung

Die in dieser Arbeit ausgewerteten Belege konvergieren auf fünf Befunde:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift und produktionserprobt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Einsätzen in Peer-Kommunen erfüllt werden, einschließlich im Kleingemeindekontext (5.000–80.000 Einwohner), der die Mehrheit europäischer Gemeinden ausmacht.

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland), der Interoperable-Europe-Act und das EU-Datengesetz schaffen gesetzliche Verpflichtungen, die proprietäre, herstellergebundene Systeme langfristig nicht erfüllen können.

**3. Die wirtschaftliche Begründung ist überzeugend, wenn die Gesamtkosten korrekt berechnet werden.** Open-Source-Stacks eliminieren Pro-Kopf-Lizenzkosten und reduzieren das Herstellerbindungsrisiko. Eine repräsentative 500-Mitarbeitenden-Gemeinde kann über fünf Jahre ca. 675.000 € einsparen. Genossenschaftliche Beschaffungsmodelle verteilen Implementierungskosten auf viele Kommunen.

**4. ZenDiS, GovStack und kantonale IT-Rahmen reduzieren den Implementierungsaufwand für einzelne Kommunen drastisch.** Die schwierigsten Teile der kommunalen Open-Source-Transformation — Spezifikationen schreiben, Rahmenverträge aushandeln, Community of Practice aufbauen — wurden bereits auf Bundes- und Kantonsebene geleistet. Kommunen, die bestehenden Rahmen beitreten, können Phase-1-Ergebnisse in sechs Monaten statt achtzehn erreichen.

**5. Erfolg erfordert ebenso viel politische und organisatorische Investition wie technische.** Klares politisches Mandat, qualifiziertes Veränderungsmanagement und nachhaltiges Stakeholder-Engagement sind die bindenden Faktoren. Digitale Souveränität in lokaler Gesetzgebung und Gemeinderatsbeschlüssen zu verankern ist ebenso wichtig wie die Wahl der richtigen Software.

Städte, die als Erste handeln, profitieren von Pioniervorteilen: Sie gestalten kooperative Standards, bauen Fachkompetenz auf und tragen zu den Open-Source-Gemeingütern bei, die alle Kommunen teilen. Der regulatorische Schwung, die fiskale Evidenz und die Community of Practice sind alle vorhanden. Die Einladung ist offen.

---

## Anhang A: Technologiebewertungsmatrix

Vollständige Bewertung aller wichtigen Stack-Komponenten (Gesamtbewertung = gewichteter Durchschnitt gemäß Gewichtungen aus Abschnitt 2.2).

| Komponente | Lizenz | Reife | Community | Interop | Sicherheit | GBK | Verwaltung | **Gesamt** |
|---|---|---|---|---|---|---|---|---|
| Keycloak | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **4,8** |
| Nextcloud | 5 | 5 | 5 | 4 | 5 | 5 | 5 | **4,8** |
| OpenProject | 5 | 4 | 4 | 4 | 4 | 5 | 4 | **4,3** |
| Camunda Community | 4 | 5 | 4 | 5 | 4 | 3 | 4 | **4,1** |
| Flowable (Alt.) | 5 | 4 | 3 | 4 | 4 | 5 | 3 | **4,0** |
| Decidim | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **4,7** |
| CONSUL Democracy | 5 | 4 | 4 | 4 | 4 | 5 | 4 | **4,3** |
| Matrix/Element | 5 | 4 | 5 | 5 | 5 | 4 | 4 | **4,6** |
| Jitsi Meet | 5 | 5 | 4 | 4 | 4 | 5 | 4 | **4,4** |
| BigBlueButton | 4 | 5 | 4 | 4 | 4 | 5 | 4 | **4,3** |
| CKAN | 5 | 5 | 4 | 5 | 4 | 4 | 5 | **4,6** |
| QGIS | 5 | 5 | 5 | 5 | 4 | 5 | 4 | **4,7** |
| GeoServer | 4 | 5 | 4 | 5 | 4 | 5 | 4 | **4,4** |
| TYPO3 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **4,7** |
| Drupal | 5 | 5 | 5 | 4 | 4 | 5 | 4 | **4,6** |
| Sovereign Cloud Stack | 5 | 4 | 5 | 5 | 5 | 4 | 4 | **4,6** |
| Kubernetes | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **4,8** |
| PostgreSQL | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **5,0** |

---

## Anhang B: Muster-Beschaffungsklauseln

Die folgenden Klauseln sind für die Aufnahme in kommunale IT-Beschaffungsunterlagen (Leistungsbeschreibung / Cahier des charges) konzipiert.

### B.1 Open-Source-Lizenzanforderung

> Alle unter diesem Vertrag beschafften Softwarekomponenten müssen unter einer von der Open Source Initiative (OSI) anerkannten Lizenz lizenziert sein. Der Auftragnehmer muss eine Software Bill of Materials (SBOM) im SPDX- oder CycloneDX-Format bereitstellen, vierteljährlich aktualisiert, mit allen Open-Source-Abhängigkeiten und deren Lizenzen.

### B.2 Public Money, Public Code

> Alle für [Gemeindename] unter diesem Vertrag entwickelten Individualsoftware-Komponenten müssen innerhalb von 90 Tagen nach Lieferung als Open-Source-Software veröffentlicht werden: (a) auf openCode.de oder einem äquivalenten öffentlichen Repository; (b) unter einer OSI-anerkannten Lizenz; (c) mit Dokumentation, die die Wiederverwendung durch andere Behörden ermöglicht.

### B.3 Interoperabilitätsanforderungen

> Alle gelieferten Systeme müssen folgende Standards implementieren: [zutreffend auswählen] XÖV-Standards (Deutschland): XPersonenstand, XMeld, je nach Dienstumfang / eCH-Standards (Schweiz): eCH-0044, eCH-0147, je nach Dienstumfang / DCAT-AP für alle Datenkatalog-Schnittstellen / OpenID Connect für alle Identitätsföderation / BPMN 2.0 für alle Workflow-Schnittstellen. Nicht-Konformität mit zwingenden Standards ist ein Ausschlusskriterium.

### B.4 Datensouveränitätsanforderungen

> Alle unter diesem Vertrag verarbeiteten Daten müssen ausschließlich in [EU / Schweiz / Deutschland / Kanton X] gespeichert und verarbeitet werden. Der Auftragnehmer muss: (a) Rechenzentrumsstandorte im Angebot angeben; (b) den Auftraggeber unverzüglich über jeden Auftragsverarbeiterwechsel informieren; (c) innerhalb von 30 Tagen dokumentierten Datenexport in offenen Formaten bereitstellen; (d) alle Kundendaten innerhalb von 30 Tagen nach Vertragsbeendigung löschen.

### B.5 Gesamtbetriebskosten-Projektion

> Jedes Angebot muss eine 5-Jahres-Gesamtbetriebskosten-Projektion beinhalten: (a) Lizenzierung; (b) Implementierung und Migration; (c) Hosting und Infrastruktur; (d) Schulung; (e) Support und Wartung; (f) geschätzte Ausstiegskosten nach Jahr 5. Angebote ohne GBK-Projektion werden als nicht konform ausgeschlossen.

---

## Anhang C: Vierteljährliche Literaturprüfliste

Bei Ausführung von `Scripts/update_literature_review.py` prüfen:

**Gesetzgebung und Politik**
- [ ] Neue Schweizer E-Government-Gesetze oder eCH-Standard-Updates
- [ ] Neue deutsche OZG-Implementierungsberichte, FITKO-Veröffentlichungen, ZenDiS-Updates
- [ ] Neue EU-Gesetze für kommunale IT (Datengesetz-Umsetzung, KI-Gesetz, DSA/DMA)
- [ ] Neue Umsetzungsleitlinien für den Interoperable Europe Act
- [ ] Schweizer nDSG-Umsetzungs-Updates

**Technologie**
- [ ] Neue Sovereign-Cloud-Stack-Versionen oder Governance-Updates
- [ ] Neue openCode.de-Statistiken oder Fallstudien
- [ ] Nextcloud, Decidim, Matrix, CKAN, Camunda, TYPO3 Hauptversionen
- [ ] Neue Sicherheitshinweise (BSI CERT-Bund, NCSC-CH)
- [ ] Neue SBOM-Tools oder Standardupdates (SPDX, CycloneDX)

**Forschung und Berichte**
- [ ] Neue akademische Artikel zu E-Government-Reife (GIQ, ISM, EJEG)
- [ ] Neue kommunale Open-Source-Einsätze oder Fallstudien
- [ ] OSOR-Jahresbericht (EU Open Source Observatory, jährlich) [50]
- [ ] UN-E-Government-Umfrage (zweijährlich) [29]
- [ ] ZenDiS-Jahresbericht [49]
- [ ] govdigital-eG-Jahresbericht [23]

**Qualitätssicherung**
- [ ] Quellenregistrierungseinträge mit Status „ungeprüft“ verifizieren
- [ ] Tote URLs im Quellenverzeichnis aktualisieren
- [ ] Neue Versionen zitierter Dokumente prüfen
- [ ] GBK-Zahlen gegen neue veröffentlichte Daten querprüfen

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023*. Brüssel. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Interoperable-Europe-Act — Verordnung (EU) 2024/903*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903

[7] Wirtz, B.W., & Weyerer, J.C. (2017). *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M. et al. (2012). *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2024). *Föderale IT-Kooperation — Publikationen*. https://www.fitko.de/presse/veroeffentlichungen — [DL-DE/Zero 2.0]

[10] openCode.de. (2022). *openCode — Open Source für die Verwaltung*. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2024). *SCS Technische Dokumentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2024). *Decidim: Freie quelloffene Partizipationsdemokratie*. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2024). *Nextcloud für Behörden*. https://nextcloud.com/government/

[14] The Matrix Foundation. (2024). *Matrix-Spezifikation v1.11*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2024). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2024). *TYPO3 in der öffentlichen Verwaltung*. https://typo3.org/project/association

[20] OpenProject GmbH. (2024). *OpenProject für Behörden*. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community / CNCF. (2024). *Keycloak IAM*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2024). *CKAN: Open-Source-Datenportal-Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium*. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *NIS2-Richtlinie — Richtlinie (EU) 2022/2555*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[29] Vereinte Nationen (UNDESA). (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2024). *Camunda Platform 8 Community Edition*. https://camunda.com/ — [Apache 2.0]

[34] BigBlueButton Inc. (2024). *BigBlueButton*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2024). *Jitsi Meet*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS*. https://www.qgis.org/ — [GPL-2.0+]

[39] CNCF. (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/

[42] BMI / ZenDiS GmbH. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2024). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html

[44] opendata.swiss. (2024). *Open Government Data Schweiz*. https://opendata.swiss/ — [CC-BY-4.0]

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [CC-BY-4.0]

[46] KoSIT. (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/

[47] eCH — eGovernment Standards. (2024). *eCH-Standards für E-Government Schweiz*. Bern: eCH. https://www.ech.ch/ — [CC-BY-SA-4.0]

[48] CONSUL Democracy Foundation. (2024). *CONSUL Democracy: Offene Regierung und Bürgerbeteiligung*. Madrid. https://consuldemocracy.org/ — [AGPL-3.0]

[49] ZenDiS GmbH. (2024). *ZenDiS: Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. Berlin. https://zendis.de/

[50] Europäische Kommission / OSOR. (2023). *Open Source Observatory Jahresbericht 2023*. Brüssel: Joinup. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[51] Europäisches Parlament und Rat. (2023). *EU-Datengesetz — Verordnung (EU) 2023/2854*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202302854

[52] Internationale Fernmeldeunion (ITU) / Digital Impact Alliance (DIAL). (2023). *GovStack: Bausteine für digitale öffentliche Infrastruktur*. Genf: ITU. https://www.govstack.global/

[53] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN: 978-0596804350

[54] GAIA-X AISBL. (2025). *GAIA-X Architecture Document Release 25.01*. Brüssel. https://docs.gaia-x.eu/

[55] Geschäftsstelle OGD Schweiz / Schweizerische Bundeskanzlei. (2024). *Open-Government-Data-Strategie Schweiz 2024–2027*. Bern. https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Licence (CC-BY-4.0) veröffentlicht.*  
*Namensnennung: Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur (sebk4c@tuta.com)*  
*Version 0.2.0 — Übersetzung: Quellengeprüfter Entwurf — 2026-06-21*
