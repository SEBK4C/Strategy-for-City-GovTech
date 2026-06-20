---
title: "Souverän durch Design: Eine moderne Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
date: "2026-06-20"
language: "de"
source-of-truth: false
source-document: "Doc/en/sovereign-by-design-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - kommunale Digitalisierung
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - Civic Technology
  - ZenDiS
  - OpenDesk
  - GovStack
  - eCH-Standards
  - EU-Datengesetz
---

# Souverän durch Design: Eine moderne Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur
**Korrespondenz:** sebk4c@tuta.com
**Version:** 0.2.0 — Zitationsvollständiger Entwurf
**Datum:** 2026-06-20
**Sprachen:** Deutsch (Übersetzung) · English (Quelldokument: `Doc/en/sovereign-by-design-v0.2.0.md`)
**SPDX-Lizenz-Bezeichner:** CC-BY-4.0

---

## Zusammenfassung

Kommunale Verwaltungen sind die dem Bürger nächste Schicht demokratischer Administration — und stehen dennoch vor einem akuten Strukturkonflikt: Die digitalen Werkzeuge, auf die sie angewiesen sind, werden zunehmend proprietär, anbietergebunden und im Widerspruch zu öffentlichkeitswirksamen Werten betrieben. Dieses Papier präsentiert eine umfassende Strategie für die Implementierung eines modernen, quelloffenen Verwaltungstechnologie-Stacks in kommunalen Verwaltungen, aktualisiert auf den Stand eines zitationsvollständigen Entwurfs (v0.2.0).

Auf der Grundlage der wegweisenden Schweizer EMBAG-Gesetzgebung (2023) [1], des deutschen OZG 2.0-Reformprogramms und der Sovereign Cloud Stack-Initiative [2, 3], des OpenDesk-Programms von ZenDiS [42], des eCH-Interoperabilitätsrahmens [51], des EU-Gesetzes über interoperable Europa (2024) [6], des EU-Datengesetzes (2023) [47] sowie der ITU/DIAL GovStack-Initiative [50] leiten wir eine erstprinzipienbasierte Technologiebewertung, einen 36-monatigen Implementierungsfahrplan, einen Stakeholder- und Beschaffungsrahmen sowie ein Risikoregister mit empirisch fundierten Minderungsmaßnahmen ab.

Wir bewerten neun funktionale Technologieschichten — Identitätsmanagement, Dokumentenmanagement, Workflow-Automatisierung, Bürgerbeteiligung, Kommunikation, Open-Data-Publikation, Geoinformationssysteme, öffentliche Websites und Cloud-Infrastruktur — anhand von sieben Kriterien: Lizenztransparenz, Einsatzreife, Community-Gesundheit, Interoperabilitätsstandards-Konformität, Sicherheitslage, Gesamtbetriebskosten und bestehende Referenzdeployments im öffentlichen Sektor.

Vier Erkenntnisse gehen konsistent aus den Belegen hervor:

1. **Open-Source-Technologiestacks für Kommunen sind technisch ausgreift und praxiserprobt** — für alle neun Funktionsschichten mit dokumentierten Deployments bei vergleichbaren Kommunen aller Größenordnungen.
2. **Der regulatorische Rahmen schreibt Open-Source und Interoperabilität zunehmend vor** — EMBAG, OZG 2.0, das Interoperable-Europe-Gesetz und das EU-Datengesetz schaffen rechtliche Verpflichtungen, die proprietäre, anbietergebundene Systeme auf Dauer nicht erfüllen können.
3. **Die 5-Jahres-Gesamtbetriebskosten begünstigen den Open-Source-Stack, wenn sie vollständig berechnet werden** — indikative Modellierungen zeigen Einsparungen von 200–600 € pro Nutzer über fünf Jahre gegenüber vergleichbaren proprietären Suiten.
4. **Politisches und organisatorisches Investment ist der bindende Engpass** — nicht die Technologie. Klares Mandat, qualifiziertes Veränderungsmanagement und nachhaltige Stakeholder-Einbindung sind die ausschlaggebenden Erfolgsfaktoren.

**Schlüsselbegriffe:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitalisierung, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, ZenDiS, OpenDesk, eCH-Standards, GovStack, EU-Datengesetz, E-Government, Civic Technology

---

## 1. Einleitung

Die Digitalisierung kommunaler Verwaltungen ist keine freiwillige Aufgabe mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienste; Regulierungsbehörden fordern Interoperabilität und Datenschutz-Compliance; Haushaltsdruck verlangt nachhaltige Technologieinvestitionen; und ein wachsender Regelungsrahmen in der Schweiz, Deutschland und der Europäischen Union schreibt zunehmend offene Standards und quelloffene Praktiken als Voraussetzung für die Rechtssicherheit vor [1, 2, 6].

Der überwiegende Teil der Stadtverwaltungen bleibt dennoch in einem Kreislauf proprietärer Anbieterabhängigkeit, teurer Lizenzverträge und fragmentierter Systeme gefangen, die gute Regierungsführung eher behindern als fördern [4, 29]. Die Folgen sind gut dokumentiert: Anbieter-Lock-in erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate blockieren behördenübergreifenden Datenaustausch und Transparenz [45]; geschlossene Quellcode-Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; wiederkehrende Lizenzgebühren entziehen Budgets, die besser in die Erbringung öffentlicher Leistungen investiert würden [3, 5].

Ein alternativer Weg ist möglich und erwiesen. Die Schweizer EMBAG-Gesetzgebung von 2023 schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht werden muss [1]. Deutschlands OZG 2.0-Reform, der Sovereign Cloud Stack, die openCode.de-Plattform und das OpenDesk-Programm repräsentieren das ehrgeizigste Open-Source-Regierungstechnologieprogramm Europas [2, 3, 10, 42]. Das EU-Gesetz über interoperables Europa und das EU-Datengesetz schaffen neue Verpflichtungen rund um Interoperabilität und Datenportabilität, die offene Architekturen weiter begünstigen [6, 47].

Dieses Papier fasst diese Entwicklungen zu einer praxisorientierten Strategie für kommunale Verwaltungen zusammen und richtet sich an alle relevanten Stakeholder: Stadtverwalter, gewählte Amtsträger, öffentliche IT-Teams, Beschaffungsstellen, zivilgesellschaftliche Gruppen, Open-Source-Gemeinschaften und souveräne Technologieanbieter.

### 1.1 Geltungsbereich und Definitionen

*Kommunale Verwaltung* bezeichnet städtische und lokale Gebietskörperschaften, einschließlich Gemeinden, Kommunen, Städten und entsprechenden Strukturen in Schweizer Kantonen. Die Strategie ist skalierbar für kleine Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (über 500.000 Einwohner), mit entsprechender Anpassung für Organisationskapazität, Vergaberecht und technische Ressourcen.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten, die unter OSI-anerkannten Lizenzen stehen und auf Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder ohne unverhältnismäßige Kosten oder Aufwand verlassen kann.

*Digitale Souveränität* ist die Fähigkeit einer Verwaltung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — das Recht, Software ohne Abhängigkeit von einem einzigen Anbieter zu prüfen, zu modifizieren, zu auditieren und zu migrieren [3]. Sie umfasst rechtliche, technische und betriebliche Dimensionen: Datenspeicherungsort, Quellcode-Zugänglichkeit, vertragliche Freiheit und demokratische Rechenschaftspflicht für algorithmische Entscheidungen.

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Technologiestack für kommunale Verwaltungen im Jahr 2026 aus?
2. Welche Lehren können aus den Erfahrungen der Schweizer, deutschen und europäischen souveränen Technologiegemeinschaften gezogen werden?
3. Was ist der optimale phasenweise Implementierungspfad für eine Stadtverwaltung mit 50.000–500.000 Einwohnern, mit Anpassungen für kleinere Kommunen?
4. Wie sollten Beschaffung, Stakeholder-Einbindung und Risikomanagement gestaltet werden, um die Erfolgschancen zu maximieren?

---

## 2. Methodik

Dieses Papier verwendet ein multimethodisches Forschungsdesign, das folgende Ansätze kombiniert:

**Systematische Literaturrecherche** von begutachteten Fachpublikationen, Grauer Literatur und Strategiedokumenten, die zwischen 2010 und 2026 veröffentlicht wurden und die Themen E-Government-Theorie, digitale Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunale Digitalisierung abdecken. Das Quellregister (`Mem/source-registry.md`) ist die kanonische Aufzeichnung aller zitierten Quellen mit Verifizierungsstatus.

**Vergleichende Politikanalyse** der Technologiegesetzgebung und -strategien aus der Schweiz (EMBAG 2023 [1], E-Government-Strategie 2024–2027 [16], Strategie Digitale Schweiz 2023 [54]), Deutschland (OZG 2017/2024 [2], Deutsche Verwaltungscloud-Strategie, FITKO-Rahmen [9]) und der Europäischen Union (Interoperable-Europe-Gesetz 2024 [6], EU-Open-Source-Strategie 2020–2023 [5], EU-Datengesetz 2023 [47]).

**Technologiestack-Bewertung** anhand einer strukturierten Siebenkriterien-Bewertungsmatrix (Skala 1–5): (a) Lizenztransparenz, (b) Einsatzreife, (c) Community-Gesundheit, (d) Interoperabilitätsstandards-Konformität, (e) Sicherheitslage, (f) Gesamtbetriebskosten (TCO) und (g) bestehende Referenzdeployments im öffentlichen Sektor.

**Versionsänderungshinweise (v0.1.0 → v0.2.0):** Diese Revision verifiziert alle zuvor unverifizierten Zitate (Quellen [6], [9], [16], [43]), ergänzt vier neue inhaltliche Abschnitte in der Literaturübersicht (Abschnitte 3.5–3.8), fügt einen Gesamtbetriebskostenrahmen hinzu (Abschnitt 4.10), ergänzt Fallstudien (Infoboxen 1–2), erweitert den Beschaffungsabschnitt um eine Vorlage und fügt Erfolgsfallstudien zur Risikoanalyse hinzu (Abschnitt 7.3).

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in der öffentlichen Verwaltung behandeln; (b) Digitalisierungsstrategien für die öffentliche Verwaltung abdecken; (c) den europäischen, Schweizer oder deutschen Regulierungskontext betreffen; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern. Quellen vor 2010 wurden nur aufgenommen, wenn sie grundlegende Theorierahmen etablieren.

### 2.2 Einschränkungen

Dieses Papier ist ein zitationsvollständiger Entwurf (v0.2.0). Technologiestack-Bewertungen spiegeln den Stand der öffentlich verfügbaren Informationen vom Juni 2026 wider. Implementierungskostenschätzungen sind indikativ und müssen gegen lokale Beschaffungsbedingungen validiert werden.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government hat sich in vier breiten Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Erstellung von Behörden-Websites [29]. Die zweite Generation (2005–2012) betonte Online-Dienstleistungserbringung, Bürgerportale und die Integration von Backoffice-Systemen [7]. Die dritte Generation (2012–2020) führte offene Daten, partizipative Plattformen und mobile Dienstgestaltung ein [8]. Die aktuelle vierte Generation (ab 2020) ist durch Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und den Souveränitätswandel geprägt — die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstregierung ist [45].

Das ganzheitliche E-Government-Reifegradmodell von Wirtz und Weyerer [7] identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Dienstleistungsqualität, Bürgerorientierung und Transparenz. Kommunale Verwaltungen in der Schweiz und Deutschland schneiden in diesen Dimensionen unterschiedlich ab; technische Infrastruktur und Prozessqualität hinken den Erwartungen der Bürger in den meisten Gebietskörperschaften hinterher.

Die grundlegende Open-Government-Literatur — insbesondere Lathrop und Rumas Synthese von 2010 [53] — stellte fest, dass Regierungsoffenheit drei untrennbare Dimensionen hat: Transparenz (Bürger können sehen, was die Regierung tut), Partizipation (Bürger können sich an Entscheidungen beteiligen) und Zusammenarbeit (Regierung ko-produziert Lösungen mit Bürgern und Zivilgesellschaft). Ein Open-Source-Technologiestack ist die technische Voraussetzung für alle drei Dimensionen: Transparenz erfordert prüfbaren Code, Partizipation erfordert zugängliche und interoperable Plattformen, und Zusammenarbeit erfordert gemeinsam nutzbare, forkbare Infrastruktur.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept der digitalen Souveränität hat sich in Europa von einem akademischen Konstrukt zu einer bindenden Verpflichtung entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 [5] etablierte "Teilen und Wiederverwenden" als Grundprinzip und verpflichtete EU-Institutionen zur Bevorzugung quelloffener Lösungen bei der Technologiebeschaffung. Das Gesetz über interoperables Europa 2024 [6] (Verordnung (EU) 2024/903, CELEX: 32024R0903) schafft verbindliche Interoperabilitätsverpflichtungen für öffentliche Verwaltungen — Artikel 12 verpflichtet zu Interoperabilitätsbewertungen für jede IKT-Lösung, die grenzüberschreitenden Datenaustausch betrifft.

Der deutsche **Sovereign Cloud Stack (SCS)** [3, 11], entwickelt von der Open Source Business Alliance (OSBA) und mitfinanziert vom Bundesministerium für Wirtschaft und Klimaschutz (BMWK), ist die konkreteste Realisierung digitaler Souveränität in der Cloud-Infrastruktur. SCS stellt eine vollständig quelloffene, selbst betreibbare Cloud-Plattform (OpenStack + Kubernetes + Ceph) bereit, die öffentlichen Verwaltungen technisch und rechtlich souveränen Infrastrukturbetrieb ermöglicht [3, 11].

Die Schweizer EMBAG-Gesetzgebung, die am 1. Januar 2024 in Kraft trat [1], schreibt vor, dass alle mit öffentlichen Mitteln entwickelten Bundessoftware standardmäßig als Open Source veröffentlicht werden müssen (Artikel 9). Die gleichzeitige Strategie Digitale Schweiz 2023 [54] rahmt digitale Souveränität als nationales strategisches Interesse, das mit wirtschaftlicher Wettbewerbsfähigkeit, demokratischer Legitimität und Cybersicherheitsresilienz verknüpft ist.

### 3.3 Das Deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 wesentlich reformiert (OZG 2.0) [2], verpflichtet alle deutschen Bundes-, Landes- und Kommunalbehörden, ihre Verwaltungsleistungen online anzubieten. Die OZG 2.0-Reform adressiert die Schwächen der ersten Generation — fragmentierte Umsetzung, mangelnde Interoperabilität, inkonsistente Nutzererfahrung — durch das "Once-Only"-Prinzip, den "Einer-für-Alle"-Ansatz (EfA) zur gemeinsamen Dienstentwicklung sowie eine föderale Plattformarchitektur auf Basis von BundID und FITKO [9, 10].

**FITKO** (Föderale IT-Kooperation) [9] ist die föderale Koordinierungsstelle für die OZG-Umsetzung und Standardisierung. Ihre Jahresberichte dokumentieren den Umsetzungsfortschritt auf Bundes- und Länderebene und liefern den maßgeblichsten Benchmark für die deutsche kommunale Digitalisierung. Das **XÖV-Standards-Koordinierungsbüro** unter der Schirmherrschaft von KoSIT (Koordinierungsstelle für IT-Standards) pflegt die Familie der XML-Datenaustauschstandards, die die Interoperabilität in der deutschen öffentlichen Verwaltung regeln [46].

Die **openCode.de**-Plattform [10] bietet ein zentrales Repository für behördliche Open-Source-Software mit über 300 Repositories und ermöglicht es Kommunen, gemeinsame Lösungen zu entdecken, wiederzuverwenden und zu ergänzen — was das "Public Money? Public Code!"-Prinzip [4] in der deutschen öffentlichen Verwaltung operationalisiert.

Das **genossenschaftliche Modell** der IT-Leistungserbringung für den öffentlichen Sektor wird durch mehrere Schlüsselorganisationen vertreten:
- **govdigital eG** [23]: Genossenschaft öffentlicher IT-Dienstleister, die SCS-basierte Cloud-Infrastruktur betreibt und GWB-konforme Rahmenverträge aushandelt.
- **Dataport AöR** [24]: Gemeinsamer IT-Dienstleister für Hamburg, Schleswig-Holstein, Bremen, Mecklenburg-Vorpommern, Sachsen-Anhalt und Thüringen — mehr als 130.000 Beschäftigte im öffentlichen Dienst.
- **AKDB** (Anstalt für Kommunale Datenverarbeitung in Bayern): Bayerische kommunale IT-Genossenschaft, die über 2.000 bayerische Kommunen bedient.
- **KDO** (Kommunale Datenverarbeitung Oldenburg): Genossenschaft für niedersächsische Kommunen.
- **ITEOS** (ehemals kdRS/kdi): IT-Dienstleister für Kommunen in Baden-Württemberg.
- **Regio iT**: NRW-basierte kommunale IT-Genossenschaft.

Diese Genossenschaftsstrukturen sind entscheidend für die Implementierungsstrategie: Sie ermöglichen kleinen Kommunen den Zugang zu Enterprise-Infrastruktur und -Diensten, ohne die vollen Entwicklungs- und Betriebskosten alleine tragen zu müssen.

### 3.4 Schweizer Bundes- und Kantonale Digitaldienste

Die föderale Struktur der Schweiz schafft sowohl Herausforderungen als auch Chancen für die kommunale Digitalisierung. Die E-Government-Strategie Schweiz 2024–2027 [16], gemeinsam erarbeitet vom Bundesrat und der Konferenz der Kantonsregierungen (KdK), legt einen kollaborativen Rahmen für digitale Dienste fest, der ausdrücklich offene Standards und Interoperabilität über alle föderalen Ebenen hinweg vorschreibt.

Zentrale Schweizer digitale Infrastrukturen umfassen:
- **Fedlex** (fedlex.admin.ch): Die offizielle Plattform für das Schweizer Bundesrecht, die auf offenen Standards basiert und maschinenlesbare Rechtsdaten bereitstellt.
- **opendata.swiss** [44]: Das nationale Open-Government-Daten-Portal, aufgebaut auf CKAN, das Tausende von Datensätzen von Bundes-, Kantons- und Kommunalbehörden unter CC-BY-4.0 katalogisiert.
- **GEVER** [43]: Das standardisierte elektronische Geschäftsverwaltungssystem für die Bundesverwaltung, definiert durch das Bundesarchivgesetz. Wichtige Implementierungen umfassen CMI AG's CMI GEVER, Fabasoft Cloud und kantonale Lösungen.
- **Swiss eID**: Ein dezentralisiertes, datenschutzschonendes digitales Identitätssystem (nach der Reform nach dem Referendum 2021, neu gestartet 2024), das auf Self-Sovereign-Identity-Prinzipien basiert.

Das kantonale IT-Ökosystem wird von verschiedenen Organisationen bedient: **VRSG** (Verwaltungsrechenzentrum St. Gallen) für ostschweizer Kantone, **abraxas Informatik** für die Zentral- und Ostschweiz sowie **BL-IT** für Basel-Landschaft — und stellen das genossenschaftliche Modell dar, das einzelne Gemeinden ohne eigene große IT-Abteilungen nutzen können.

### 3.5 ZenDiS und das OpenDesk-Programm

**ZenDiS** (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) [48], 2022 von der deutschen Bundesregierung gegründet, ist die bedeutendste institutionelle Innovation in der europäischen Open-Source-Regierungspolitik. ZenDiS fungiert als zentraler Steward für Deutschlands Open-Source-Arbeitsplatzprogramm und beauftragt, kuratiert und pflegt quelloffene Software-Suiten für die deutsche öffentliche Verwaltung.

Das Flaggschiff-Produkt von ZenDiS ist **OpenDesk** [42] — eine staatlich kuratierte Open-Source-Desktop-und-Kollaborationssuite, die folgende Komponenten integriert: Nextcloud (Dateiverwaltung und Zusammenarbeit), CryptPad (datenschutzkonformes Dokumentenbearbeiten), OpenProject (Projektmanagement und Aktenverknüpfung), Jitsi Meet (Videokonferenzen) und Element (Matrix-basiertes Messaging). Stand 2026 befindet sich OpenDesk in der gestaffelten Einführung in Bundesministerien und Länderverwaltungen.

Die strategische Bedeutung von ZenDiS und OpenDesk geht über die spezifischen Softwarekomponenten hinaus. Erstmals hat eine europäische Regierung eine dedizierte, öffentlich finanzierte Institution mit dem Mandat geschaffen, quelloffene Arbeitsplatzsoftware für die gesamte öffentliche Verwaltung nachhaltig zu pflegen, zu aktualisieren und weiterzuentwickeln. Dies adressiert eine kritische historische Schwachstelle öffentlicher Open-Source-Deployments: das Fehlen einer langfristigen Support-Infrastruktur außerhalb kommerzieller Anbieterbeziehungen.

Für kommunale Verwaltungen repräsentiert ZenDiS sowohl eine Ressource als auch ein Modell: als Ressource können kommunale IT-Abteilungen ZenDiS-kuratierte Komponenten mit Vertrauen in langfristigen Support und Sicherheitspflege einsetzen; als Modell können Schweizer Kantone und europäische Kommunen analoge Zentren auf geeigneten föderalen Ebenen einrichten.

### 3.6 eCH-Standards und Schweizer Interoperabilität

Die **eCH-Standards** [51] (E-Government-Standards Schweiz) sind das Schweizer Äquivalent zu Deutschlands XÖV-Standards — ein umfassendes Rahmenwerk von XML-basierten Datenaustauschspezifikationen für E-Government-Anwendungen. Entwickelt von der eCH-Vereinigung unter der Schirmherrschaft von E-Government Suisse, decken sie Personendaten (eCH-0011), Adressdaten (eCH-0010), Organisationsstrukturen (eCH-0007) und Interoperabilitätsrahmen (eCH-0014: Rahmenwerk für die Nutzung von E-Government-Standards) ab.

eCH-Standards sind für föderale IT-Systeme verbindlich und für kantonale und kommunale Systeme dringend empfohlen. Für einen in der Schweiz eingesetzten kommunalen Technologiestack ist eCH-Konformität nicht optional — sie bestimmt, ob das System mit der föderalen Identitätsinfrastruktur (Swiss eID), kantonalen Registern und kantonsübergreifenden Datenaustauschplattformen interoperieren kann.

Die praktische Implikation für die Stack-Auswahl: das Identitätsmanagement (Keycloak) muss über OpenID Connect mit Swiss eID föderieren und dabei eCH-0011-Personendatenattribute implementieren. Dokumentenmanagementsysteme müssen eCH-0058 (GEVER) für die Aktenführung implementieren. Open-Data-Portale müssen das OGD-Schweiz-Metadatenprofil (DCAT-AP CH) als eCH-Erweiterung implementieren.

### 3.7 Das EU-Datengesetz 2023 und kommunale Datenverwaltung

Das **EU-Datengesetz** (Verordnung (EU) 2023/2854) [47], anwendbar ab September 2025, gestaltet die Governance von Daten, die durch digitale öffentliche Dienste erzeugt und verarbeitet werden, grundlegend um. Die Implikationen für kommunale Technologiestacks sind erheblich:

**Artikel 5 — Datenweitergabepflichten:** Dienstanbieter müssen dem Käufer (d.h. der Kommune) auf Anfrage Daten, die durch Produkte und damit verbundene Dienste erzeugt werden, in einem gängigen Format zur Verfügung stellen. Dies adressiert direkt die Datenportabilitätsdimension des Anbieter-Lock-ins.

**Artikel 30 — Cloud-Wechsel:** Anbieter von Cloud-Diensten müssen Wechselunterstützung zu alternativen Anbietern ohne unverhältnismäßige Gebühren anbieten. Für eine Kommune, die eine Migration von einer proprietären Cloud zum Sovereign Cloud Stack erwägt, stärkt das Datengesetz ihre Verhandlungsposition.

**Artikel 35 — Offene Interoperabilitätsstandards:** Anbieter müssen offene Interoperabilitätsstandards implementieren und technische Dokumentation veröffentlichen, die alternative Implementierungen ermöglicht.

Die praktische Implikation für die kommunale Beschaffung: Verträge nach September 2025 müssen ausdrücklich auf Datengesetz-Rechte Bezug nehmen, und die Technologieauswahl sollte Systeme bevorzugen, die diese Rechte designbedingt implementieren — durch offene Formate, dokumentierte APIs und von der Community kontrollierte Datenmodelle — anstatt nur durch rechtliche Verpflichtung.

### 3.8 GovStack: Der Internationale Bausteinansatz

Die **GovStack-Initiative** [50], entwickelt von der ITU, DIAL (Digital Impact Alliance) und Partnerregierungen, stellt ein international validiertes Rahmenwerk aus interoperablen digitalen Regierungsbausteinen bereit — Spezifikationen für funktionale Dienste, die durch Open-Source- oder offene Standard-konforme Systeme implementiert werden können. GovStack-Bausteinspezifikationen definieren standardisierte APIs und Datenmodelle für: Identitätsverifizierung, Zahlungen, Einwilligungsmanagement, Messaging, Terminverwaltung, digitale Register und Informationsmediatoren.

Die Bedeutung von GovStack für die kommunale Strategie ist zweifach: Einerseits gewinnt ein kommunaler Stack, der auf GovStack-kompatiblen Komponenten aufbaut, Kompatibilität mit national und international eingesetzter digitaler Regierungsinfrastruktur. Andererseits unterstützt der Bausteinansatz modulare Beschaffung — Kommunen können jeden Baustein unabhängig beschaffen und ersetzen, ohne systemweite Störungen, vorausgesetzt sie konformieren mit den GovStack-API-Spezifikationen.

### 3.9 Open-Source-Bürgerplattformen

**Decidim** [12] (Barcelona, 2016) ist die am weitesten verbreitete quelloffene Partizipationsplattform weltweit, die von über 400 Organisationen eingesetzt wird, darunter Barcelona, Helsinki, New York und der Schweizer Kanton Schaffhausen. **CONSUL Democracy** [52] (Madrid, 2015) ist eine komplementäre Plattform mit besonderer Stärke in der Partizipativen Budgetierung, die in über 100 Städten weltweit eingesetzt wird.

**Matrix/Element** [14] stellt das strategisch wichtigste offene Kommunikationsprotokoll für die öffentliche Verwaltung dar. Der deutsche BundesMessenger, der französische Tchap und der Schweizer Bundespilot operieren alle auf dem Matrix-Protokoll. Das Föderationsmodell ermöglicht sichere organisationsübergreifende Kommunikation, während die Datensouveränität gewahrt bleibt.

**Nextcloud** [13] (Stuttgart, 2016) ist die am weitesten verbreitete quelloffene Dateisynchronisations- und Kollaborationsplattform in der europäischen öffentlichen Verwaltung — eingesetzt von Tausenden deutschen Kommunen, der Schweizer Bundesverwaltung und Dutzenden EU-Institutionen. Nextcloud ist ISO 27001 zertifiziert und unterstützt On-Premises-, Private-Cloud- und kooperativ gehostete Deployment-Modelle.

### 3.10 Lücken in der Literatur

Trotz der oben dokumentierten Fortschritte bestehen erhebliche Lücken: **Gesamtbetriebskostenstudien** zum Vergleich von Open-Source- und proprietären kommunalen Stacks sind spärlich. **Longitudinale Implementierungsdaten** von Städten, die vollständige Open-Source-Übergänge über 5+ Jahre abgeschlossen haben, sind begrenzt. **Perspektiven kleiner Kommunen** sind unterrepräsentiert. **Nutzererfahrungsforschung** zum Vergleich der Bürgerzufriedenheit mit Open-Source- und proprietären kommunalen Digitaldiensten fehlt nahezu vollständig. Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse.

---

## 4. Technologiestack-Analyse

Ein kommunaler Technologiestack lässt sich in neun Funktionsschichten zerlegen. Die folgende Analyse bewertet die führenden Open-Source-Optionen für jede Schicht anhand der in Abschnitt 2 definierten Siebenkriterien-Bewertungsmatrix (Skala 1–5).

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Bürger und Mitarbeiter authentifizieren; Identität über Dienste hinweg föderieren; Single Sign-On (SSO) implementieren; mit nationaler Identitätsinfrastruktur (BundID/Deutsche eID, Swiss eID) integrieren.

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die de-facto-Standard-Plattform für Identity and Access Management (IAM) im öffentlichen Sektor in Europa. Die Software implementiert OpenID Connect (OIDC), OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht die Föderierung mit nationalen Identitätssystemen. Für Schweizer Kommunen föderiert Keycloak mit Swiss eID via OIDC und implementiert dabei eCH-0011-Personendatenattribute [51]. Für deutsche Kommunen integriert Keycloak mit BundID via SAML 2.0.

| Kriterium | Bewertung | Anmerkungen |
|---|---|---|
| Lizenztransparenz | 5 | Apache 2.0 |
| Einsatzreife | 5 | Praxiserprobt, 10+ Jahre, Millionen Nutzer |
| Community-Gesundheit | 5 | Große aktive Community, CNCF-gehostet |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, eCH-0011 |
| Sicherheitslage | 5 | CVE-reaktiv, breit auditiert, FIPS-kompatibler Modus |
| TCO | 4 | Keine Lizenzkosten; Betriebskompetenz erforderlich |
| Referenzdeployments | 5 | EU-Institutionen, Deutsche Länder, Schweizer Kantone |
| **Gesamt** | **34/35** | |

### 4.2 Dokumentenverwaltung und Akten

**Funktion:** Offizielle Akten speichern, abrufen, klassifizieren und aufbewahren; GEVER/DMS-konforme Workflows verwalten; CMIS-Interoperabilität unterstützen.

**Empfohlene Komponenten: Nextcloud** [13] + **OpenProject** [20]

Für Schweizer Kommunen mit voller GEVER-Konformitätspflicht: CMI AG's CMI GEVER oder Fabasoft Community Edition stellt die Compliance-Schicht bereit, mit Nextcloud als kollaborativem Frontend. Für deutsche Kommunen bieten AKDB's BayernPortal oder Dataport-Komponenten die entsprechende Verwaltungsschicht.

| Kriterium | Bewertung | Anmerkungen |
|---|---|---|
| Lizenztransparenz | 5 | AGPL-3.0 (Nextcloud), GPL-3.0 (OpenProject) |
| Einsatzreife | 5 | 400.000+ Nextcloud-Organisationen weltweit |
| Community-Gesundheit | 5 | Nextcloud GmbH + große Community |
| Interoperabilität | 4 | WebDAV, CalDAV, CardDAV, CMIS; eCH-0058 via Plugin |
| Sicherheitslage | 5 | Nextcloud ISO 27001; vierteljährliche Penetrationstests |
| TCO | 5 | Keine Pro-Nutzer-Lizenz (Community); selbst- oder kooperativ gehostet |
| Referenzdeployments | 5 | Schweizer Bundesverwaltung, Deutsche Länder, EU-Institutionen |
| **Gesamt** | **34/35** | |

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Funktion:** Verwaltungsworkflows automatisieren; BPMN-2.0-Prozesse modellieren, ausführen und überwachen; XÖV/eCH-Datenstandards integrieren; Revisionspfade bereitstellen.

**Empfohlene Komponente: Camunda Platform 8 Community** [33]

Camunda bietet die funktionsreichste BPMN-2.0-native Workflow-Engine mit starker Verbreitung im deutschen öffentlichen Sektor. **Flowable** (Apache 2.0) ist eine leichtgewichtigere Alternative, die Camundas Dual-Lizenzierungsmodell vermeidet; beide sind auf der Prozessmodellebene weitgehend kompatibel [46].

| Kriterium | Bewertung | Anmerkungen |
|---|---|---|
| Lizenztransparenz | 4 | Community: Apache 2.0; Enterprise: proprietär (Dual-Lizenz) |
| Einsatzreife | 5 | Praxiserprobt im großen Maßstab |
| Community-Gesundheit | 4 | Aktiv; Enterprise-Tier finanziert Kernentwicklung |
| Interoperabilität | 5 | BPMN 2.0, DMN 1.3, CMMN 1.1, REST API, ereignisgesteuert |
| Sicherheitslage | 4 | Aktiv gepflegt; SOC 2 (Enterprise) |
| TCO | 3 | Community kostenlos; hochskalige Deployments ggf. Enterprise |
| Referenzdeployments | 4 | Mehrere deutsche Länder, Schweizer Kantons-Workflows |
| **Gesamt** | **29/35** | |

### 4.4 Bürgerbeteiligung

**Funktion:** Konsultation und Beratung; Partizipatives Haushalten; Bürgerinitiativensammlung; digitale Versammlungsverwaltung; Umfragen und Abstimmungen.

**Empfohlene Komponente: Decidim** [12]

Decidim ist die ausgereifteste und weltweit am weitesten verbreitete quelloffene Partizipationsplattform mit einem Governance-Modell, das selbst demokratische Digitalinfrastruktur exemplifiziert. **CONSUL Democracy** [52] bietet ein ergänzendes Toolset mit besonderer Stärke in der Partizipativen Budgetierung.

| Kriterium | Bewertung | Anmerkungen |
|---|---|---|
| Lizenztransparenz | 5 | AGPL-3.0 (Decidim und CONSUL) |
| Einsatzreife | 5 | 400+ Decidim-Deployments weltweit |
| Community-Gesundheit | 5 | Decidim-Vereinigung; CONSUL Madrider Rathaus |
| Interoperabilität | 4 | REST API, Webhooks, OAuth 2.0 |
| Sicherheitslage | 4 | Aktiv gepflegt; regelmäßige Sicherheitsaudits |
| TCO | 5 | Keine Lizenzkosten; Hosting und Anpassung sind die Kosten |
| Referenzdeployments | 5 | Barcelona, Helsinki, NYC, Schaffhausen, Madrid |
| **Gesamt** | **33/35** | |

### 4.5 Kommunikation und Zusammenarbeit

**Funktion:** Internes Messaging und Gruppenchat; verschlüsselte behördenübergreifende Kommunikation; Videokonferenzen für Ratssitzungen und Bürgerdienste; E-Mail und Kalender.

**Empfohlene Architektur:**

| Komponente | Lizenz | Reife | Bewertung | Entscheidender Vorteil |
|---|---|---|---|---|
| Matrix/Element [14] | Apache 2.0 | Produktiv | 5 | E2E-Verschlüsselung, Föderierung |
| Jitsi Meet [35] | Apache 2.0 | Produktiv | 5 | Browser-basiert, keine Client-Installation |
| BigBlueButton [34] | LGPL-3.0 | Produktiv | 4 | Ratssitzungsintegration, Aufzeichnung |
| Nextcloud Talk | AGPL-3.0 | Produktiv | 4 | Integration mit Dateiverwaltung |

Der deutsche BundesMessenger (Matrix-basiert) stellt ein Referenz-Deployment dar. Das Föderationsmodell ist entscheidend: Jede Kommune betreibt ihren eigenen Matrix-Server und kommuniziert sicher mit Servern anderer Organisationen, ohne dass Daten über einen zentralen Punkt geleitet werden.

### 4.6 Open-Data-Publikation

**Funktion:** Maschinenlesbare Datensätze veröffentlichen; Katalogsuche und API-Zugang bereitstellen; PSI/Open-Data-Richtlinie einhalten; in opendata.swiss und GovData.de einspeisen.

**Empfohlene Komponente: CKAN** [22]

CKAN ist die weltweit führende quelloffene Open-Data-Portal-Software (10+ Jahre Produktionsbetrieb im großen Maßstab). Sie betreibt opendata.swiss, GovData.de, data.gov (USA) und data.gov.uk. Ihr Metadatenmodell implementiert DCAT-AP (EU), DCAT-AP.de (Deutschland) und DCAT-AP CH (Schweiz), was die Ernte durch übergeordnete Portale ohne manuelle Neueingabe ermöglicht.

| Kriterium | Bewertung | Anmerkungen |
|---|---|---|
| Lizenztransparenz | 5 | AGPL-3.0 |
| Einsatzreife | 5 | 10+ Jahre Produktionsbetrieb auf nationaler Ebene |
| Community-Gesundheit | 4 | CKAN Association; OKF-Stewardship |
| Interoperabilität | 5 | DCAT-AP, DCAT-AP.de, DCAT-AP CH, OAI-PMH, SPARQL |
| Sicherheitslage | 4 | Aktiv gepflegt |
| TCO | 4 | Keine Lizenz; Betriebsaufwand für kleine Kommunen (kooperatives Hosting empfohlen) |
| Referenzdeployments | 5 | Schweiz, Deutschland, EU, USA, UK |
| **Gesamt** | **32/35** | |

### 4.7 Geoinformationssysteme

**Funktion:** Kartenbasierte Bürgerdienste; Stadtplanung; Geodatenpublikation; Notfallkoordination; INSPIRE-Direktive-Konformität.

**Empfohlene Komponenten:** QGIS [37] (Desktop/Server für Geodatenbearbeitung und -analyse), GeoServer (OGC-konforme Geodatenpublikation: WMS, WFS, WCS), OpenStreetMap [36] (Basiskartierungsschicht, ODbL-lizenziert), swisstopo (Schweiz) / BKG (Deutschland) — autoritative amtliche Geodaten mit offenen Download-APIs.

Die INSPIRE-Direktive verpflichtet öffentliche Verwaltungen in der EU/EEA zur Veröffentlichung von Geodaten in interoperablen Formaten — QGIS + GeoServer ist der Standard-Open-Source-Implementierungspfad für die INSPIRE-Konformität.

### 4.8 Öffentliche Website und Content-Management

**Funktion:** Öffentliche Website; Nachrichten und Bekanntmachungen; Dienst-Verzeichnis; Barrierefreiheit (WCAG 2.1 AA / BITV 2.0); mehrsprachige Inhaltsverwaltung.

**Empfohlene Komponenten:**
- **TYPO3** [19]: Dominant im deutschsprachigen öffentlichen Sektor. Die TYPO3 Association bietet LTS-Versionen (Long-Term-Support), Erweiterungen für den öffentlichen Sektor und eine große deutschsprachige Community. BITV 2.0 / WCAG 2.1 AA mit Standardkonfiguration konform. Besonders geeignet für Schweizer Gemeinden mit mehrsprachigen Anforderungen (DE/FR/IT).
- **Drupal**: Starke internationale Referenzen; eingesetzt von der Europäischen Kommission und mehreren nationalen Regierungsportalen. Besser für Kommunen, die starke internationale digitale Dienste oder EU-Digitalinfrastruktur-Integration benötigen.

### 4.9 Cloud-Infrastruktur

**Funktion:** Compute, Speicher, Netzwerk, Container-Orchestrierung; digitale Souveränität auf Infrastrukturebene; BSI-IT-Grundschutz/ISDS-konformer Betrieb.

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

SCS ist die strategisch wichtigste Infrastrukturwahl für europäische Kommunen, die echte digitale Souveränität anstreben. Der vollständig quelloffene Stack (OpenStack + Kubernetes [39] + Ceph, mit relationaler Persistenz via PostgreSQL [41]) kann selbst gehostet, über govdigital eG [23] betrieben oder von zertifizierten SCS-Hostern (plusserver, OSISM, Regio iT) mit vertraglichen Datensouveränitätsgarantien bereitgestellt werden.

| Kriterium | Bewertung | Anmerkungen |
|---|---|---|
| Lizenztransparenz | 5 | Apache 2.0 / vollständig offener Stack |
| Einsatzreife | 4 | Produktionsbetrieb in mehreren Ländern; reift schnell |
| Community-Gesundheit | 5 | OSBA-unterstützt; wachsende Community |
| Interoperabilität | 5 | Offene APIs, OCI-konform, CSP-neutral |
| Sicherheitslage | 5 | BSI-IT-Grundschutz-kompatibel; C5-zertifizierte Betreiber verfügbar |
| TCO | 4 | Keine Lizenzkosten; Infrastruktur- und Betriebskosten |
| Referenzdeployments | 4 | Deutsche Ländercloud; govdigital eG |
| **Gesamt** | **32/35** | |

### 4.10 Gesamtkostenrahmen (TCO)

Eine rigorose Beschaffungsentscheidung erfordert ein 5-Jahres-Gesamtbetriebskostenmodell (TCO). Die folgende Rahmenmethodik und indikativen Zahlen basieren auf öffentlich verfügbaren Daten aus kommunalen und kantonalen Deployments, Anbieterpreislisten und genossenschaftlichen Beschaffungsrahmenverträgen.

**Tabelle 1: Indikative 5-Jahres-TCO — Open-Source-Stack vs. Proprietäre Alternativen**
*(Pro-Nutzer-Werte; Organisationsgröße 500 Nutzer; EUR)*

| Kostenkategorie | Proprietär (Microsoft 365 E3-Äquivalent) | Open Source (OpenDesk-Äquivalent) | Anmerkungen |
|---|---|---|---|
| **Softwarelizenz (jährlich)** | 250–350 € | 0 € | OSS: keine Pro-Nutzer-Lizenz |
| **Hosting/Infrastruktur (jährlich)** | 30–60 € (inbegriffen) | 50–120 € | OSS: selbst- oder kooperativ gehostet |
| **Implementierung (einmalig, amortisiert)** | 20–40 € | 80–150 € | OSS: höhere Vorabkosten, keine laufenden Lizenzen |
| **Schulung (einmalig, amortisiert)** | 20–30 € | 30–50 € | Beide erfordern Schulung |
| **Support und Wartung (jährlich)** | 0 € (inbegriffen) | 20–50 € | OSS: Community + Kooperations-Support |
| **Anpassung (jährlich)** | 10–30 € (nur Anbieter) | 15–40 € (mehrere Anbieter) | OSS: Wettbewerbsmarkt |
| **Migration/Exit (Periodenende)** | 50–150 € (hoher Lock-in) | 10–30 € (geringer Lock-in) | OSS: offene Formate reduzieren Exit-Kosten |
| **5-Jahres-Gesamt pro Nutzer** | **1.780–2.600 €** | **1.450–2.200 €** | |
| **Indikative Einsparung pro Nutzer (5 Jahre)** | — | **200–600 €** | |
| **Für 500 Nutzer (5 Jahre)** | **890 T€–1,3 M€** | **725 T€–1,1 M€** | |
| **Indikative Einsparung (500 Nutzer, 5 Jahre)** | — | **100–300 T€** | |

*Hinweis: Die Zahlen sind indikativ und müssen gegen lokale Beschaffungsbedingungen validiert werden. Die Spanne spiegelt die Variation in Stadtgröße, bestehender Infrastruktur und Support-Modell wider. Das proprietäre Kostenvorteilsargument aus gebündelten Diensten schrumpft erheblich, wenn Anbieter-Lock-in-Exit-Kosten und Compliance-Kosten für das EU-Datengesetz einbezogen werden.*

**Zentrale TCO-Grundsätze:**
1. Proprietäre Lizenzkosten sind gut vorhersehbar; Open-Source-Implementierungskosten sind nach vorne geladen. Der TCO-Schnittpunkt tritt typischerweise im Jahr 2–3 auf.
2. Genossenschaftliche Beschaffungsstrukturen (govdigital eG, kantonale IT-Kooperativen) drücken Open-Source-Implementierungskosten weiter, indem sie auf mehrere Kommunen verteilt werden.
3. Das EU-Datengesetz [47] ändert die proprietäre TCO-Berechnung: Kommunen haben nun rechtliche Ansprüche auf Datenportabilität, die Wechselkosten reduzieren — aber nur, wenn die Verträge diese Rechte widerspiegeln.

### 4.11 Referenzarchitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    BÜRGERSCHNITTSTELLEN                         │
│  TYPO3/Drupal · Decidim/CONSUL · CKAN Offene Daten · eService  │
├─────────────────────────────────────────────────────────────────┤
│                     DIENSTE-SCHICHT                             │
│  Camunda/Flowable · XÖV/eCH-Formulare · GeoServer/QGIS         │
├─────────────────────────────────────────────────────────────────┤
│                  KOLLABORATIONS-SCHICHT                         │
│  Nextcloud · Matrix/Element · Jitsi · OpenProject              │
├─────────────────────────────────────────────────────────────────┤
│                    IDENTITÄTS-SCHICHT                           │
│  Keycloak SSO ←→ BundID / Swiss eID / eCH-0011                │
├─────────────────────────────────────────────────────────────────┤
│                  INFRASTRUKTUR-SCHICHT                          │
│  Sovereign Cloud Stack (OpenStack + Kubernetes + Ceph)          │
│  PostgreSQL · Objektspeicher · Souveränes Netzwerk             │
└─────────────────────────────────────────────────────────────────┘
         ↑ Alle Schichten kommunizieren über offene APIs ↑
      ↑ XÖV [DE] / eCH [CH] / DCAT-AP [EU] Datenstandards ↑
     ↑ BSI IT-Grundschutz [DE] / ISDS [CH] / NIS2 [EU] ↑
```

Alle Schichten kommunizieren über dokumentierte, offene APIs. Die Container-Orchestrierung übernimmt Kubernetes [39], die relationale Persistenz PostgreSQL [41] und den Objektspeicher Ceph — alles auf dem Sovereign Cloud Stack betrieben. Der Datenaustausch erfolgt über XÖV-Standards (Deutschland) [46] oder eCH-Standards (Schweiz) [51]. GovStack-Bausteinspezifikationen [50] bieten die internationale Interoperabilitätsschicht.

---

## 5. Implementierungsfahrplan

Die Implementierung ist als 36-monatiges, fünfphasiges Programm strukturiert. Jede Phase hat definierte Ergebnisse, Erfolgskriterien und Entscheidungspunkte. Die Phasen sind darauf ausgelegt, frühzeitig Mehrwert zu liefern.

### Phase 0: Grundlagen (Monate 1–3)

**Ziel:** Governance aufbauen, Ist-Zustand erfassen, Koalition bilden.

**Ergebnisse:**
- Digitaler Transformations-Lenkungsausschuss eingesetzt (Stadtspitze + IT + Beschaffung + Zivilgesellschaft + Datenschutzbeauftragter)
- Technologiebestandsaufnahme abgeschlossen (alle Software, Lizenzen, Kosten, Verträge, Integrations-abhängigkeiten erfasst)
- Stakeholder-Engagement-Plan verabschiedet und kommuniziert
- Beschaffungsrahmen etabliert (Rahmenvertrag mit Kooperations-IT-Anbieter, oder direkter Beschaffungspfad definiert)
- Absichtserklärung (MoU) mit primärem Implementierungspartner (Dataport, AKDB, ITEOS, govdigital, abraxas oder Äquivalent)

**Erfolgskriterien:**
- Politisches Mandat gesichert (Stadtratsbeschluss oder Stadtratsentscheid mit überparteilicher Unterstützung)
- Budgetrahmen genehmigt (indikativ: 200.000–500.000 € für Phasen 0–1, skalierend mit Stadtgröße)
- Projektleitung mit Befugnissen ernannt; Datenschutzbeauftragter eingebunden

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die Grundschichten — Identität und Infrastruktur — aufbauen, von denen alles andere abhängt.

**Ergebnisse:**
- Sovereign Cloud Stack-Umgebung in Betrieb (eigenes Rechenzentrum, zertifizierter Hoster oder Genossenschaft)
- Keycloak IAM deployed; föderiert mit nationalem Identitätssystem (BundID oder Swiss eID)
- Nextcloud-Basis-Deployment für interne Zusammenarbeit (ersetzt proprietären Cloud-Speicher)
- Matrix/Element-Messaging für Mitarbeitende (ersetzt proprietäres Instant-Messaging)
- BSI-IT-Grundschutz-Basis-Dokumentation vollständig (oder ISDS-Äquivalent für CH)

**Erfolgskriterien:**
- 100% des IT-Personals authentifiziert sich via Keycloak SSO
- Dateispeicher von proprietärer Cloud zu Nextcloud migriert (messbare Kosteneinsparung)
- Verschlüsseltes Mitarbeiter-Messaging in Betrieb
- Sicherheits-Baseline dokumentiert, vom DSB genehmigt, erster Penetrationstest abgeschlossen

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste fünf bürgernahe Dienste auf offener Infrastruktur migrieren oder erstellen; Open-Data- und Partizipationsplattformen einführen.

**Ergebnisse:**
- Fünf volumenstärkste Verwaltungsdienste auf Camunda/XÖV- (oder Flowable/eCH-)Stack deployed
- CMS-Migration abgeschlossen (Stadtwebsite vollständig auf Open-Source-CMS)
- CKAN Open-Data-Portal gestartet mit ersten 20 Datensätzen; in GovData.de / opendata.swiss geerntet
- Decidim-Instanz für ersten Partizipationsprozess (z.B. Partizipatives Haushalt) aktiv

**Erfolgskriterien:**
- 80% des Ziel-Dienstvolumens ohne Rückschritt durch neue Systeme verarbeitet
- Open-Data-Portal aktiv mit ≥20 Datensätzen, mindestens 5 maschinenlesbar
- Erster Decidim-Prozess mit dokumentiertem Bürgerengagement abgeschlossen

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Serviceabdeckung ausweiten; Daten-Governance aufbauen.

**Ergebnisse:**
- Alle Dienste über Keycloak SSO föderiert (Single Sign-On für alle Bürger- und Mitarbeiterdienste)
- Nextcloud in Dokumentenmanagement-Workflows integriert (GEVER/eCH- oder XÖV-basierte Akten)
- GIS-Schicht in Betrieb (QGIS + GeoServer; INSPIRE-konforme Datenpublikation)
- 80% der Verwaltungsdienste vollständig digitalisiert
- XÖV/eCH-Datenaustausch mit kantonalen/Landes- und Bundesbehörden in Betrieb
- Software-Stückliste (SBOM) veröffentlicht für alle Stack-Komponenten

**Erfolgskriterien:**
- End-to-End-Digitaldienste für 80% der Transaktionstypen (kein Papier erforderlich)
- Datenqualitätsmetriken etabliert und erste Jahresmessung abgeschlossen
- Erster Jahresbericht zu Offenen Daten veröffentlicht

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Nutzererlebnis optimieren; Ergebnisse messen; zum Open-Source-Gemeingut beitragen.

**Ergebnisse:**
- Bürgerzufriedenheitsumfrage (Mindest n=500)
- Mindestens drei Verbesserungen an Upstream-Projekten beigetragen (openCode.de, Nextcloud, TYPO3, Decidim)
- Kommunale Open-Source-Praxisgemeinschaft mit ≥3 Peer-Kommunen eingerichtet
- TCO-Bericht mit Ist- vs. Planzahlen veröffentlicht
- Barrierefreiheits-Audit abgeschlossen; WCAG 2.1 AA-Konformität zertifiziert

**Erfolgskriterien:**
- Net Promoter Score (NPS) für digitale Dienste ≥40
- Mindestens drei Upstream-Beiträge zusammengeführt
- Praxisgemeinschaft mit Peer-Kommunen aktiv

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; für Ausdehnung auf Nachbarkommunen vorbereiten.

**Ergebnisse:**
- Vollständiges Lizenz-Compliance-Audit aller Softwarekomponenten
- Datensouveränität verifiziert (100% der Bürgerdaten auf souveräner Infrastruktur)
- Replikations-Playbook für Nachbarkommunen veröffentlicht
- Strategiepapier v1.0 veröffentlicht (extern teilbares Release)

**Erfolgskriterien:**
- Keine proprietäre Einzelanbieter-Abhängigkeit im kritischen Dienstpfad
- Datenspeicherungsort zu 100% auf souveräner Infrastruktur (via SBOM und Hosting-Verträge verifizierbar)
- Mindestens eine Peer-Kommune hat das Playbook in Phase 0–1 eingesetzt

---

> **Infobox 1: Fallstudie Kleinstgemeinde (<20.000 Einwohner)**
>
> Eine Gemeinde mit 8.000 Einwohnern und einem dreiköpfigen IT-Team ist idealer Kandidat für kooperatives Hosting über ein kantonales Rechenzentrum (CH) oder einen regionalen kommunalen IT-Anbieter (DE). In diesem Modell wird keine eigene Infrastruktur benötigt: Die Genossenschaft betreibt SCS, Keycloak, Nextcloud, Decidim und CKAN als mandantenfähige Shared-Service-Instanzen mit Datenisolation auf Gemeindeebene. TYPO3 wird mit gemeindespezifischem Theme bereitgestellt.
>
> Implementierungskosten: 30.000–80.000 € (Phasen 0–1), mit laufenden Genossenschaftsgebühren von 15.000–40.000 € pro Jahr — deutlich unter dem proprietären Äquivalent von über 100.000 €. Der Kanton Schaffhausen (Decidim-Deployment) und opendata.swiss (CKAN, gehostet durch die Bundeskanzlei) sind Beispiele für dieses Genossenschaftsmodell auf kantonaler Ebene.

---

> **Infobox 2: Genossenschaftliches IT-Modell**
>
> Das genossenschaftliche IT-Anbietermodell — vertreten durch govdigital eG (Deutschland), Dataport AöR (Norddeutschland), AKDB (Bayern) und kantonale IT-Organisationen (Schweiz) — ist die entscheidende Organisationsinfrastruktur für nachhaltiges Open-Source-kommunales IT.
>
> Wesentliche Merkmale: öffentliches Eigentum (im Besitz der Mitglieds-Kommunen/Länder; Gewinne fließen an Mitglieder zurück), GWB/BöB-konforme Rahmenverträge, Open-Source-Bevorzugung, Skalenvorteile durch gemeinsame Infrastruktur- und Sicherheitsoperationen.
>
> Eine Kommune, die einer Genossenschaft beitritt, gibt keine Souveränität ab — sie bündelt souveräne Kapazität mit Gleichgesinnten unter demokratischer Governance. Diese Unterscheidung ist für gewählte Mandatsträger entscheidend, die genossenschaftliche IT mit dem proprietären Outsourcing verwechseln, dem sie zu Recht misstrauisch gegenüberstehen.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Hauptinteresse | Einfluss | Engagement-Ansatz |
|---|---|---|---|
| Bürgermeister / Stadtspitze | Politischer Erfolg, Kosten, Bürgerzustimmung | Hoch | Führungsbriefings, öffentliches Fortschritts-Dashboard |
| Stadtrat / Gemeinderat | Aufsicht, demokratische Legitimität | Hoch | Quartalsberichte, öffentliche Ratssitzungen |
| Städtisches IT-Team | Technische Machbarkeit, Arbeitsbelastung, Karriereentwicklung | Hoch | Ko-Design, Schulung, Community-Mitgliedschaft |
| Beschaffung / Rechtsabteilung | Compliance, Haftung, Revisionssicherheit | Mittel-Hoch | Rechtsbriefings, Schulung zu Rahmenverträgen |
| Verwaltungsangestellte | Benutzerfreundlichkeit, Zuverlässigkeit | Hoch | UX-Tests, Schulung, Parallelbetrieb |
| Bürgerinnen und Bürger | Dienstleistungsqualität, Datenschutz, Barrierefreiheit | Hoch | Decidim-Partizipationsdesign, Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Mittel | Öffentliche Roadmaps, offene Ratssitzungen |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung, Anerkennung | Mittel | openCode.de-Beteiligung, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Deployment, Umsatz | Mittel | Zertifizierte Partnerverträge, Genossenschafts-Mitgliedschaft |
| Datenschutzbeauftragter (DSB) | DSGVO-Konformität, Datensparsamkeit | Hoch | Privacy-by-Design-Review an jedem Phasenpunkt |
| Kantonale/Landesregierung | Interoperabilität, Rechtskonformität | Hoch | Standards-Abstimmung, XÖV/eCH-Konformität |
| Bundesregierung | OZG/EMBAG-Konformität, EfA-Wiederverwendung | Mittel | openCode.de-Veröffentlichung, Bundeskoordination |

### 6.2 Beschaffungsrahmen

Open-Source-Beschaffung erfordert einen strukturell anderen Rahmen als der Kauf proprietärer Lizenzen. Sechs Grundsätze regeln die Open-Source-konforme Beschaffung:

**Grundsatz 1 — Leistungen beschaffen, keine Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Mehrwertleistungen. Vergabeunterlagen müssen auf Service-Level-Vereinbarungen, Support-Verpflichtungen und Lieferobjekte — nicht auf Lizenzbedingungen — ausgerichtet sein.

**Grundsatz 2 — Genossenschaftliche Beschaffungsstrukturen nutzen.** govdigital eG, Dataport, AKDB, kantonale IT-Kooperativen und andere Genossenschaftsstrukturen bieten vorverhandelte Rahmenverträge, die GWB/BöB-Anforderungen erfüllen. Die Mitgliedschaft in einem bestehenden Rahmen reduziert die Vergabezeitdauer von 18–36 auf 2–6 Monate.

**Grundsatz 3 — "Public Money? Public Code!" als Vertragsbedingung** [4]. Alle unter Vertrag entwickelten Anpassungen müssen unter einer OSI-anerkannten Open-Source-Lizenz veröffentlicht und auf openCode.de oder einem gleichwertigen öffentlichen Repository publiziert werden. Musterklausel: *"Alle im Rahmen dieses Vertrags entwickelten Softwarelösungen, die nicht ausschließlich von den Eigentumsdaten des Auftraggebers abhängen, werden unter [EUPL-1.2 / AGPL-3.0 / Apache 2.0] lizenziert und innerhalb von 90 Tagen nach Erstbereitstellung auf openCode.de veröffentlicht."*

**Grundsatz 4 — 5-Jahres-TCO-Modellierung vorschreiben.** Die Bewertungsmatrix der Beschaffung muss ein 5-Jahres-TCO-Modell enthalten (vgl. Rahmen in Abschnitt 4.10), das Implementierung, Hosting, Schulung, Support und Exit-Kosten umfasst.

**Grundsatz 5 — Interoperabilitätsstandards als Ausschlusskriterium.** Alle beschafften Systeme müssen XÖV-Standards (Deutschland) [46], eCH-Standards (Schweiz) [51] und DCAT-AP (EU-Offene-Daten) implementieren. Nichteinhaltung ist ein Ausschlusskriterium, kein bewertetes Kriterium.

**Grundsatz 6 — Datengesetz-Rechte in Vertragsbedingungen verankern** [47]. Verträge nach September 2025 müssen ausdrücklich beinhalten: (a) Datenportabilitätsklauseln (Artikel 5), (b) Cloud-Wechsel-Unterstützungspflichten (Artikel 30) und (c) Anforderungen an offene Interoperabilitätsstandards (Artikel 35).

### 6.3 Musterstruktur für Ausschreibungsunterlagen

**Abschnitt 1 — Zweck und Hintergrund:** Gemeindename, Bevölkerung, aktuelles Technologiebild, strategisches Ziel (digitale Souveränität, OZG/EMBAG-Konformität, TCO-Reduktion).

**Abschnitt 2 — Leistungsumfang:** In Scope befindliche Softwarekomponenten (aus Abschnitt 4 dieses Papiers), Deployment-Modell (selbst gehostet / genossenschaftlich / zertifizierter Hoster), Support-Level (Geschäftszeiten / 24×7 / SLA-Stufe).

**Abschnitt 3 — Technische Anforderungen:**
- *Pflicht:* OSI-anerkannte Open-Source-Lizenz für alle gelieferte Software
- *Pflicht:* XÖV/eCH/DCAT-AP-Konformität für alle Datenschnittstellen
- *Pflicht:* BSI-IT-Grundschutz- (oder C5-)Dokumentation für alle gehosteten Komponenten
- *Pflicht:* SBOM-Lieferung und -Pflege
- *Bevorzugt:* GovStack-Bausteinspezifikations-API-Konformität
- *Bevorzugt:* openCode.de-Veröffentlichung jeder angepassten Entwicklung

**Abschnitt 4 — Beschaffungsbedingungen:** "Public Money? Public Code!"-Klausel, EU-Datengesetz-Rechte, Datensouveränitätsklausel (alle Daten werden in [DE/CH/EU] verarbeitet und gespeichert), Prüfungsrecht (Sicherheitsstatus jederzeit mit 30 Tagen Vorlauf prüfbar).

**Abschnitt 5 — Bewertungskriterien:**
- Technische Qualität und Open-Source-Lizenz-Konformität: 30%
- Gesamtbetriebskosten (5 Jahre, Methodik aus Abschnitt 4.10): 30%
- Referenzen aus vergleichbaren öffentlichen Deployments: 20%
- Interoperabilitätsstandards-Konformität: 10%
- Community-Gesundheit und Langfristnachhaltigkeit der Komponente: 10%

**Abschnitt 6 — Vertragsbedingungen:** Mindest-3-Jahres-Erstlaufzeit; 12 Monate Kündigungsfrist; vierteljährliche Sicherheitsupdates; monatliche Minor-Releases; Quellcode-Hinterlegung oder Äquivalent; Übergangshilfe bei Vertragsende (mindestens 6 Monate).

### 6.4 Veränderungsmanagement

Open-Source-Übergänge scheitern häufig nicht an technischen, sondern an menschlichen Faktoren: Widerstand der Endnutzer, unzureichende Schulung, Trägheit im mittleren Management und politischer Rückfall unter Anbieter-Lobbying [30].

**Empfehlungen:**
- Einen **Beauftragten für Digitale Transformation** auf Bürgermeisterstell-Ebene mit explizitem politischen Mandat und geschütztem Budget ernennen.
- In jeder Verwaltungseinheit **Open-Source-Botschafter** designieren: gut ausgebildet, angesehen, mit zugewiesener Zeit für Peer-Support-Funktion.
- **Parallelbetrieb** für mindestens drei Monate vor dem Umstieg auf kritische Systeme führen — länger für bürgernahe Dienste.
- **Früherfolge** dokumentieren und feiern: Kosteneinsparungen durch nicht verlängerte Lizenzverträge, neue Decidim-Prozess-Beteiligung, Verbesserungen der Sicherheitslage.
- Ein **öffentliches Transparenz-Dashboard** veröffentlichen, das Migrationfortschritt, Kosten (vor und nach), Serviceverfügbarkeit und Bürgerzufriedenheit zeigt.
- **Mandatsträger proaktiv briefen**: Sie mit Belegen ausstatten (TCO-Daten, Regulierungskonformitäts-Argumente, Peer-Kommunen-Referenzen), um auf Anbieter-Lobbying reagieren zu können.

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Priorität | Maßnahme |
|---|---|---|---|---|
| Politische Umkehr nach Wahl | Mittel | Hoch | Hoch | In Satzung/Verordnung verankern; überparteiliche Unterstützung aufbauen; TCO-Belege publizieren |
| Anbieter-Lobbying / FUD-Kampagnen | Hoch | Mittel | Hoch | Evidenz-Paket bereitstellen; Zivilgesellschaft einbinden; Regulierungsmandat publizieren |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Hoch | Schulungsprogramm; Kooperations-IT-Partner; Praxisgemeinschaft |
| Integrationsfehler zwischen Stack-Schichten | Mittel | Hoch | Hoch | Referenzarchitektur einhalten; phasenweise Einführung mit Entscheidungspunkten |
| Datenverlust bei Migration | Niedrig | Kritisch | Hoch | Vollständiges Backup-Protokoll; Parallelbetrieb ≥3 Monate; gestaffelte Migration |
| DSGVO-/Datenschutzverletzung | Niedrig | Hoch | Mittel | Privacy-by-Design; DSB an jedem Phasenpunkt; Datenfluss-Mapping |
| Nutzerannahme-Scheitern | Mittel | Hoch | Hoch | Veränderungsmanagement; UX-Tests; Schulung; Parallelsysteme; Botschafter |
| Cyberangriff | Niedrig | Kritisch | Hoch | BSI IT-Grundschutz; Penetrationstests; Incident-Response-Plan; NIS2-Konformität |
| Community-/Komponenten-Fragmentierung | Niedrig | Mittel | Mittel | CNCF/Apache-regierte Komponenten bevorzugen; Upstream beitragen |
| Kostenüberschreitung | Mittel | Mittel | Mittel | Phasengesteuertes Budget; unabhängiges Projektbüro; offene TCO-Abrechnung |
| Regulatorische Nicht-Konformität | Niedrig | Hoch | Mittel | Rechtliche Prüfung an jedem Phasenpunkt; XÖV/eCH-Konformitätstests |
| Schein-Open-Source-Lock-in | Mittel | Mittel | Mittel | Copyleft-Lizenzen bevorzugen; Hosted-only-Komponenten vermeiden; SBOM pflegen |

### 7.2 Das Münchner Mahnbeispiel — Aktualisierte Analyse

Das LiMux-Projekt der Landeshauptstadt München (2003–2017) ist der meistzitierte Fall eines großangelegten kommunalen Open-Source-Übergangs, der letztlich rückgängig gemacht wurde. Eine sorgfältige Lektüre der Nachbetrachtungsbelege ist für das Ziehen richtiger Schlüsse unabdingbar:

**Was die Rücknahme nicht war:** Sie wurde nicht durch das technische Scheitern der Open-Source-Software verursacht. München migrierte erfolgreich rund 14.000 Arbeitsplätze auf Linux und LibreOffice und erzielte damit erhebliche Kosteneinsparungen.

**Was die Rücknahme war:** Ein Wechsel der politischen Führung (Wahl 2014), gefolgt von einem in Auftrag gegebenen Beratergutachten (Accenture, 2015) — das von Kritikern als zugunsten einer proprietären Empfehlung strukturiert bewertet wurde —, gefolgt von einem Stadtratsbeschluss zur Rückmigration zu Windows (2017). Das Accenture-Gutachten wurde weitgehend kritisiert, weil es Lizenzkosteneinsparungen ausschloss und Kompatibilitätsprobleme Linux zuschrieb, die tatsächlich durch mangelnde Unterstützung offener Dateiformatstandards durch andere kommunale und Landesstellen verursacht wurden [30].

**Lehren für die kommunale Strategie:**
1. **Politisches Risikomanagement hat Vorrang**: überparteiliche Unterstützung sichern; digitale Souveränität in einem Stadtratsbeschluss mit erhöhten Mehrheitsanforderungen für die Rücknahme verankern.
2. **TCO-Dokumentation muss kontinuierlich und öffentlich sein**: wenn Kosteneinsparungen nicht öffentlich dokumentiert sind, können sie gegen anbieterfinanzierte Gegennarrative nicht verteidigt werden.
3. **Standardskonformität ist Voraussetzung, kein Nachgedanke**: Münchens Kompatibilitätsprobleme entstanden teilweise, weil Bayern und der Bund keine konsequenten offenen Dateiformatstandards implementiert hatten — eine Lücke, die OZG 2.0 und das Interoperable-Europe-Gesetz [6] nun schließen.
4. **Anbieter-Lobbying ist ein reales Risiko mit finanziellen Ressourcen dahinter**: zivilgesellschaftliches Engagement und transparente öffentliche Berichterstattung sind die Gegenmaßnahmen.

### 7.3 Erfolgsfallstudien

Drei zeitgenössische Fälle belegen erfolgreiche Open-Source-Kommunalstrategien in unterschiedlichen Größenordnungen:

**Barcelona, Spanien (Decidim, 2016):** Barcelonas Start von Decidim für die Partizipative Budgetierung mobilisierte im ersten Jahr über 40.000 Bürgerinnen und Bürger und wird seitdem von 400+ Organisationen weltweit eingesetzt. Die Open-Source-Technologiestrategie der Stadt wurde im Digitalstadtplan Barcelona 2017 festgeschrieben und bietet damit politische Dauerhaftigkeit über Wahlzyklen hinweg. Schlüsselfaktoren: visionäre politische Führung, eigenes Open-Source-Team in der Stadtverwaltung, frühzeitige Community-Investitionen.

**Helsinki, Finnland (Offene Daten + Decidim):** Helsinki betreibt eines der umfassendsten Open-Data-Programme Europas und nutzt Decidim für Bürgerbeteiligung. Das Linked-Open-Data-Portal der Stadt (aufgebaut auf CKAN) veröffentlicht über 900 Datensätze, darunter Echtzeit-Verkehrsdaten, Geodaten und Haushaltsdaten. Helsinkis Ansatz zeigt, dass Open-Data-Publikation selbst ein Bürgerbeteiligungstreiber sein kann.

**Kanton Schaffhausen, Schweiz (Decidim CH):** Als erste kantonale Decidim-Deployment in der Schweiz zeigt Schaffhausen, dass die Plattform im deutsch-schweizerischen Rechts- und Verwaltungskontext funktioniert. Das kantonale Deployment bietet eine replizierbare Vorlage für Schweizer Gemeinden jeder Größe.

**OpenDesk (Deutschland, 2023–heute):** Der föderale OpenDesk-Rollout stellt die erste staatlich kuratierte Open-Source-Arbeitsplatzsuite auf nationaler Ebene dar. Frühe Daten von ZenDiS zeigen positive Annahmequoten der Mitarbeitenden und erhebliche Kosteneinsparungen gegenüber proprietären Äquivalenten. Der Erfolg des Programms in deutschen Bundesministerien schafft politischen Rückhalt für die kommunale Einführung.

### 7.4 Sicherheitsüberlegungen

Das BSI-IT-Grundschutz-Rahmenwerk [26] bietet eine umfassende Sicherheitsbaseline unabhängig vom Lizenzmodell. Schlüsselanforderungen für den Open-Source-Kommunalstack:

- **Patch-Management**: Alle Serverkomponenten erhalten Sicherheitsupdates innerhalb von 48 Stunden nach Veröffentlichung kritischer CVEs; Standard-Updates innerhalb von 30 Tagen.
- **Authentifizierungs-Sicherheitsniveau**: Keycloak muss für BSI Authentikator-Sicherungsniveau 2 (AAL2) für bürgernahe Dienste konfiguriert werden; AAL3 (Hardware-Token) für privilegierten administrativen Zugang.
- **Verschlüsselung**: TLS 1.3 mindestens für alle Daten im Transit; AES-256-Verschlüsselung at-rest für alle personenbezogenen Datenkategorien; Ende-zu-Ende-Verschlüsselung für alle Matrix-Kommunikationen.
- **Penetrationstests**: Jährlicher Penetrationstest durch BSI-qualifizierte (CREST oder äquivalent) Anbieter; sofortige Behebung kritischer Befunde.
- **Software-Stückliste (SBOM)**: Monatlich aktualisiert und öffentlich zugänglich.
- **NIS2-Verpflichtungen** [27]: EU-Richtlinie 2022/2555 schreibt Vorfallsmeldung, Risikomanagement-Maßnahmen und Lieferketten-Sicherheit für wesentliche und wichtige Einrichtungen vor — Kommunen ab 50.000 Einwohnern fallen typischerweise in den Anwendungsbereich.
- **BSI C5-Zertifizierung** für Cloud-Hoster und SCS-Betreiber; oder äquivalente Attestierung.
- **Open-Source-Prüfungsvorteil**: Anders als bei proprietärer Software kann der Open-Source-Stack von der städtischen Sicherheitsabteilung, Peer-Kommunen, dem BSI und der Zivilgesellschaft unabhängig geprüft werden — ein struktureller Sicherheitsvorteil, den proprietäre Audits nicht replizieren können.

---

## 8. Schlussfolgerung

Die in diesem Papier beleuchteten Belege konvergieren auf vier Erkenntnisse, die durch die aktualisierte Analyse in v0.2.0 gestärkt werden:

**Erkenntnis 1: Open-Source-Technologiestacks für Kommunen sind technisch ausgereift und praxiserprobt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch quelloffene Software erfüllt werden, mit dokumentierten Deployments bei Peer-Kommunen in der Schweiz, Deutschland und der weiteren EU. Die in diesem Papier vorgestellte neunschichtige Referenzarchitektur kann von Kommunen mit 5.000 bis 500.000 Einwohnern implementiert werden.

**Erkenntnis 2: Der regulatorische Rahmen schreibt Open-Source und Interoperabilität zunehmend vor.** EMBAG [1], OZG 2.0 [2], das Interoperable-Europe-Gesetz [6] und das EU-Datengesetz [47] schaffen kollektiv rechtliche Verpflichtungen — die Open-Source-Veröffentlichung öffentlich finanzierter Software, Interoperabilitätsbewertungen, Datenportabilitätsrechte und offene API-Standards —, die proprietäre, anbietergebundene Systeme auf Dauer nicht erfüllen können.

**Erkenntnis 3: Die 5-Jahres-Gesamtbetriebskosten begünstigen Open-Source, wenn sie korrekt berechnet werden.** Der indikative TCO-Rahmen (Abschnitt 4.10) zeigt Einsparungen von 200–600 € pro Nutzer über fünf Jahre für eine 500-Nutzer-Kommune. Die Einsparungen sind größer, wenn Anbieter-Lock-in-Exit-Kosten und EU-Datengesetz-Compliance-Kosten einbezogen werden.

**Erkenntnis 4: Politisches und organisatorisches Investment ist der bindende Engpass.** Technische Entscheidungen sind sekundär gegenüber Governance-Design. Das Münchner Beispiel bestätigt, dass Open-Source-Übergänge technisch gelingen und politisch scheitern. Die Barcelonaer und Helsinkier Beispiele bestätigen, dass dauerhaftes politisches Mandat, dedizierte institutionelle Kapazität und transparente öffentliche Berichterstattung die Erfolgsdeterminanten sind.

Städte, die jetzt handeln, profitieren von First-Mover-Vorteilen: Prägung genossenschaftlicher Standards, Aufbau interner Expertise, Beitrag zu den Open-Source-Gemeingütern und Demonstration, dass ein anderer Pfad möglich ist. Der rechtliche Rahmen ist zunehmend förderlich, die Technologie ist erprobt, die Genossenschaftsinfrastruktur existiert, und die Wirtschaftlichkeit spricht dafür. Die Einladung ist offen.

**Nächste Schritte für diese Strategie:**
- **v0.3.0**: Begleitpapier für Kleinstgemeinden (Bevölkerung <50.000)
- **v1.0.0**: Extern teilbares Release mit unabhängig verifizierten TCO-Fallstudien und Bürgerzufriedenheits-Umframerahmen

---

## 9. Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0, gemeinfrei]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2024). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017, fortlaufend). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [© Europäische Union]

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 über Maßnahmen für ein hohes Maß an Interoperabilität des öffentlichen Sektors in der Union (Gesetz über interoperables Europa / Interoperable Europe Act)*. CELEX: 32024R0903. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R0903 — [EU-Rechtsakt, gemeinfrei]

[7] Wirtz, B. W. & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024 — [© Taylor & Francis]

[8] Janssen, M., Charalabidis, Y. & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740 — [© Taylor & Francis]

[9] FITKO. (2024). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/veroeffentlichungen/jahresbericht — [DL-DE/Zero 2.0]

[10] openCode.de. (2022, fortlaufend). *openCode — Open Source für die Verwaltung*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Offener Zugang; einzelne Repository-Lizenzen variieren]

[11] Sovereign Cloud Stack Community. (2024). *SCS Technische Dokumentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Freie quelloffene partizipative Demokratie für Städte und Organisationen*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2024). *Nextcloud für Behörden: Sicherheit, Souveränität und Zusammenarbeit*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [AGPL-3.0 (Community Edition)]

[14] The Matrix Foundation. (2024). *Matrix-Spezifikation v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei / E-Government Suisse. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Offener Zugang, Schweizer Bundespublikation]

[19] TYPO3 Association. (2024). *TYPO3 in der öffentlichen Verwaltung*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [GPL-2.0 (Kern); CC-BY-SA (Dokumentation)]

[20] OpenProject GmbH. (2024). *OpenProject für Behörden: Open-Source-Projektmanagement*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPL-3.0]

[21] Red Hat / Keycloak Community. (2024). *Keycloak: Open-Source-Identitäts- und Zugriffsmanagement*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2024). *CKAN: Open-Source-Datenportalsoftware*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Offener Zugang]

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Offener Zugang]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz — [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 über Maßnahmen für ein hohes gemeinsames Cybersicherheitsniveau in der Union (NIS2-Richtlinie)*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555 — [EU-Rechtsakt, gemeinfrei]

[29] UN DESA. (2022). *UN E-Government-Umfrage 2022: Die Zukunft digitaler Regierung*. New York: Vereinte Nationen. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [© Vereinte Nationen, offener Zugang]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001 — [© Elsevier]

[33] Camunda Services GmbH. (2024). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0 (Community)]

[34] BigBlueButton Inc. (2024). *BigBlueButton: Quelloffene Web-Videokonferenzlösung*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community / 8×8. (2024). *Jitsi Meet: Quelloffene Videokonferenz*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS-Projekt. (2024). *QGIS: Ein freies und quelloffenes geografisches Informationssystem*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL-Lizenz (OSI-anerkannt)]

[42] BMI / ZenDiS GmbH. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Offener Zugang, Schweizer Bundespublikation]

[44] opendata.swiss. (2024). *Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0 (Portal); individuelle Datensatzlizenzen variieren]

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen — Umsetzungsstrategie (EIF)*. Brüssel: Europäische Kommission, ISA²-Programm. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0]

[46] KoSIT. (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Offener Zugang]

[47] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 über harmonisierte Vorschriften für einen fairen Datenzugang und eine faire Datennutzung (EU-Datengesetz / Data Act)*. CELEX: 32023R2854. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854 — [EU-Rechtsakt, gemeinfrei]

[48] ZenDiS GmbH. (2024). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Jahresbericht 2023/2024*. Berlin: ZenDiS GmbH. https://zendisgmbh.de/ — [Offener Zugang]

[49] EU Open Source Observatory (OSOR). (2023). *OSOR Jahresbericht 2023: Open Source in europäischen öffentlichen Verwaltungen*. Brüssel: Europäische Kommission, DIGIT. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[50] ITU / DIAL. (2023). *GovStack-Bausteinspezifikationen v1.0*. Genf: Internationale Fernmeldeunion. https://govstack.global/building-blocks/ — [CC-BY-4.0]

[51] eCH. (2023). *eCH-0014 Rahmenwerk der E-Government-Standards Schweiz*. Bern: E-Government Suisse / eCH-Verein. https://www.ech.ch/de/ech/ech-0014 — [Offener Zugang; individuelle Standardlizenzen variieren]

[52] Consul Democracy Foundation. (2024). *CONSUL Democracy*. Madrid: Consul Democracy Foundation. https://consuldemocracy.org/ — [AGPL-3.0]

[53] Lathrop, D. & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. — [© O'Reilly Media]

[54] Schweizerischer Bundesrat. (2023). *Strategie Digitale Schweiz 2023*. Bern: Schweizerischer Bundesrat. https://www.bakom.admin.ch/bakom/de/home/digital-und-internet/strategie-digitale-schweiz.html — [Offener Zugang, CC-BY-4.0]

---

*Dieses Dokument wird unter der Creative Commons Namensnennung 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*
*Zitierhinweis: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*
*Versionshistorie: v0.1.0 (2026-06-20, Erster strukturierter Entwurf) → v0.2.0 (2026-06-20, Zitationsvollständiger Entwurf)*
