---
title: "Souverän by Design: Eine zukunftsweisende Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf"
affiliation: "Autonomous Office of Civil Digital Infrastructure"
email: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
date: "2026-06-21"
SPDX-License-Identifier: CC-BY-4.0
lang: de
translation-of: "Doc/en/sovereign-by-design-v0.2.0.md"
keywords:
  - digitale Souveränität
  - Open-Source-Software
  - Kommunalverwaltung
  - E-Government
  - öffentliche Verwaltung
  - OZG
  - EMBAG
  - Sovereign Cloud
  - GovTech
  - Civic Technology
changelog:
  - version: "0.2.0"
    date: "2026-06-21"
    description: "Erstübersetzung ins Deutsche — Zitationsvollständige Version"
---

# Souverän by Design: Eine zukunftsweisende Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf
**Organisation:** Autonomous Office of Civil Digital Infrastructure
**Kontakt:** sebk4c@tuta.com
**Version:** 0.2.0 — Zitationsvollständiger Entwurf
**Datum:** 2026-06-21
**Lizenz:** CC-BY-4.0

## Kurzfassung

Kommunalverwaltungen in ganz Europa sehen sich einer beispiellosen Bündelung von Belastungen gegenüber: sich beschleunigende Verpflichtungen aus nationalen Digitalisierungsvorgaben wie dem deutschen Onlinezugangsgesetz 2.0 [2] und dem schweizerischen Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG) [1]; steigende Anforderungen an die Cybersicherheit nach der NIS2-Richtlinie [27]; wachsende Erwartungen der Bürgerinnen und Bürger an barrierefreie, reaktionsschnelle öffentliche Dienstleistungen; sowie eine strukturelle Abhängigkeit von einer kleinen Zahl proprietärer Softwareanbieter, deren Lizenzkosten einen zunehmenden Anteil knapper öffentlicher Haushalte beanspruchen. Das Konzept der digitalen Souveränität — die Fähigkeit öffentlicher Institutionen, ihre eigene digitale Infrastruktur zu steuern, zu prüfen, anzupassen und nachhaltig zu betreiben — hat sich von einer akademischen Abstraktion zu einem operativen politischen Gebot entwickelt.

Dieses Papier legt eine umfassende, evidenzbasierte Open-Source-Technologiestrategie für Kommunalverwaltungen mit Einwohnerzahlen zwischen 50.000 und 200.000 vor, mit primärem Bezug auf den deutschen und schweizerischen Regulierungskontext und sekundärer Anwendbarkeit in der gesamten Europäischen Union. Auf der Grundlage einer systematischen Literaturrecherche von 55 begutachteten und grauen Literaturquellen, einer vergleichenden Analyse kommunaler Implementierungen in Barcelona, München, Schleswig-Holstein und schweizerischen Kantonen sowie einer strukturierten Bewertung von elf Technologiedomänen argumentiert das Papier, dass ein kohärenter Open-Source-Stack — aufgebaut auf identifizierbaren, ausgereiften, von Communities getragenen Komponenten — die funktionalen Anforderungen proprietärer Alternativen erfüllen oder übertreffen kann, während er messbare Senkungen der langfristigen Gesamtbetriebskosten erzielt, Abhängigkeiten von Einzelanbietern beseitigt und digitale öffentliche Güter hervorbringt, die der breiteren bürgerschaftlichen Allmende zugutekommen.

Die Strategie ist um einen phasenweisen Umsetzungsfahrplan herum organisiert, der sechs Phasen von der organisatorischen Bereitschaft bis zur operativen Exzellenz abdeckt, mit indikativen Kostenspannen, die auf eine mittelgroße Kommune kalibriert sind. Ein Stakeholder- und Beschaffungsrahmen befasst sich mit der politischen Ökonomie des Technologieübergangs, einschließlich Veränderungsmanagement, rechtlicher Compliance und interkommunaler Kooperationsstrukturen. Ein Risikoregister und eine regulatorische Risikomatrix identifizieren die wichtigsten Fehlermodi, wobei der LiMux-Übergang Münchens als der kanonische Mahnfall dient. Drei Anhänge stellen operative Werkzeuge bereit: eine Beschaffungs-Checkliste mit 23 Fragen, eine Bewertungsmatrix zur Technologiebewertung mit sieben Kriterien und ein Selbstbewertungsinstrument zur kommunalen digitalen Souveränität mit 15 Fragen.

Das Papier kommt zu dem Schluss, dass digitale Souveränität keine utopische Wunschvorstellung, sondern ein erreichbares technisches und Governance-Ergebnis ist, sofern Kommunen den Übergang mit angemessener Vorbereitung, realistischen Kostenerwartungen und anhaltendem politischem Engagement angehen. Öffentliches Geld sollte öffentlichen Code hervorbringen [4].

**Schlagwörter:** digitale Souveränität, Open-Source-Government, GovTech, kommunale digitale Transformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Civic Technology

## 1. Einleitung

Die digitale Transformation der öffentlichen Verwaltung ist nicht länger optional. Bürgerinnen und Bürger in demokratischen Gesellschaften erwarten zunehmend, dass staatliche Dienstleistungen über digitale Kanäle verfügbar, zugänglich und vertrauenswürdig sind. Zugleich wurden die institutionellen Strukturen, über die Kommunen diese Dienstleistungen erbringen — veraltete Unternehmenssoftware-Stacks, proprietäre Cloud-Abhängigkeiten, bilaterale Anbieterverein­­barungen — weitgehend für eine andere Ära und ein anderes Bedrohungsumfeld konzipiert.

Der Digitale Kompass 2030 der Europäischen Union [51] setzt das ausdrückliche Ziel, dass bis 2030 alle wichtigen öffentlichen Dienstleistungen online verfügbar sein sollen und dass 100 Prozent der Bürgerinnen und Bürger Zugang zu elektronischen Identitätsdokumenten haben sollen. Der Interoperable Europe Act [6] verpflichtet öffentliche Stellen, die Interoperabilität digitaler Komponenten vor der Beschaffung zu bewerten. Das deutsche OZG 2.0 [2] schreibt eine föderierte Online-Diensterbringung auf Bundes-, Landes- und kommunaler Ebene vor. Das schweizerische EMBAG [1] verlangt, dass mit Bundesmitteln entwickelte Software als Open Source veröffentlicht wird, sofern keine spezifischen Ausnahmen greifen. Diese gesetzgeberischen Signale sind richtungsweisend konsistent: Die europäische öffentliche Verwaltung bewegt sich — zögerlich, aber unverkennbar — hin zu offener, interoperabler und rechenschaftspflichtiger digitaler Infrastruktur.

### 1.1 Der europäische Moment der digitalen Souveränität

Der Begriff „digitale Souveränität“ fand Eingang in den politischen Mainstream-Diskurs im Anschluss an eine Reihe von Störungen, die die Fragilität der Technologieabhängigkeiten des europäischen öffentlichen Sektors offenlegten: der SolarWinds-Lieferketten­angriff von 2020, wiederholte Ausfälle von Cloud-Anbietern mit Hauptsitz in den USA und rechtliche Unsicherheiten infolge der Ungültigerklärung des Privacy Shield und des darauf folgenden Schrems-II-Urteils zu transatlantischen Datenübermittlungen. Die Open-Source-Strategie 2020–2023 der Europäischen Kommission [5] benannte Open-Source-Software ausdrücklich als strategischen Wegbereiter der digitalen Souveränität. Das Open Source Observatory (OSOR) [28, 53] hat Hunderte replizierbarer staatlicher Open-Source-Implementierungen in den Mitgliedstaaten katalogisiert.

Für Kommunen im Besonderen ist die Souveränitätsfrage akut. Eine mittelgroße deutsche Stadt mit 80.000 Einwohnern kann pro Jahr 2–5 Millionen Euro für Softwarelizenzen, Wartungsverträge und Cloud-Abonnements bei einer Handvoll Anbieter ausgeben. Der marginale Verhandlungshebel dieser Kommune in einer einzelnen Verhandlung ist vernachlässigbar. Kollektives Handeln — durch gemeinsame Plattformen, kooperative Beschaffung und interkommunale Entwicklungskonsortien — ist die strukturelle Alternative. Institutionen wie govdigital eG [23], Dataport AöR [24] und ZenDiS GmbH [25] stellen aufkommende deutsche Modelle genau dieser Art dar.

### 1.2 Geltungsbereich und Definitionen

Für die Zwecke dieses Papiers:

**Kommunalverwaltung** bezeichnet die exekutiven und administrativen Funktionen einer Stadt oder Gemeinde (Gemeinde / Gemeinderat) mit einer Bevölkerung zwischen etwa 50.000 und 200.000, primär in Deutschland und der Schweiz, mit Verallgemeinerung auf vergleichbare EU-Jurisdiktionen.

**Digitale Souveränität** wird definiert als die Fähigkeit einer öffentlichen Institution, ihre eigene digitale Infrastruktur zu beherrschen: die Softwarekomponenten, die ihren Verwaltungsfunktionen zugrunde liegen, auszuwählen, einzusetzen, zu prüfen, zu modifizieren und bei Bedarf zu ersetzen, ohne strukturelle Abhängigkeit von einem einzelnen privaten Anbieter. Diese Definition synthetisiert akademische Behandlungen von Janowski [30], das OECD Digital Government Policy Framework [49] und die operative Rahmung der GovStack Initiative [31].

**Open-Source-Software (OSS)** bezeichnet Software, die unter einer von der Open Source Initiative anerkannten Lizenz lizenziert ist, wodurch der Quellcode zur Prüfung, Modifikation und Weiterverbreitung verfügbar wird. Das Papier folgt der Taxonomie des European Interoperability Framework (EIF) [45] bei der Unterscheidung zwischen Softwarefreiheit (Lizenz) und operativer Autonomie (Deployment und Hosting).

**Technologie-Stack** bezeichnet das geschichtete Ensemble von Softwarekomponenten — von der Infrastruktur über die Middleware bis zu den bürgernahen Anwendungen —, die zusammen die digitale Betriebsumgebung einer Kommune bilden.

### 1.3 Forschungsfragen

Dieses Papier behandelt vier primäre Forschungsfragen:

**RQ1:** Welche Open-Source-Technologiekomponenten sind hinreichend ausgereift, gut verwaltet und öffentlich im Einsatz, um im Planungshorizont 2024–2028 einen glaubwürdigen kommunalen digitalen Stack zu bilden?

**RQ2:** Wie hoch sind die vergleichenden Gesamtbetriebskosten von Open-Source- gegenüber proprietären Alternativen auf kommunaler Ebene unter Berücksichtigung von Lizenz-, Implementierungs-, Betriebs- und Übergangskosten?

**RQ3:** Welche Governance-, Beschaffungs- und Veränderungsmanagement-Strukturen maximieren die Wahrscheinlichkeit eines erfolgreichen Open-Source-Übergangs für eine mittelgroße Kommune?

**RQ4:** Welche regulatorischen Anforderungen — auf EU-, nationaler und kantonaler/Länderebene — muss eine kommunale Open-Source-Strategie erfüllen, und wie unterstützen oder erschweren Open-Source-Komponenten die Compliance?

## 2. Methodik

### 2.1 Systematische Literaturrecherche

Die Literaturrecherche wurde nach einem angepassten PRISMA-Rahmen durchgeführt. Suchanfragen, die die Begriffe „open source government“, „digital sovereignty municipality“, „e-government open source“, „OZG open source“, „EMBAG open source“, „municipal cloud“ und Kombinationen davon abdeckten, wurden gegen Google Scholar, BASE (Bielefeld Academic Search Engine) und das Joinup-/OSOR-Repository [28, 53] ausgeführt. Die Veröffentlichungsdaten wurden auf 2000–2026 beschränkt, mit Präferenz für Material nach 2015, mit Ausnahme grundlegender theoretischer Werke. Die Referenzliste von 55 Quellen wurde aus einem anfänglichen Abruf von etwa 280 Kandidatentiteln kuratiert.

### 2.2 Vergleichende Politikanalyse

Politikdokumente aus Deutschland (OZG 2.0 [2], Digitalstrategie Deutschland [50], FIM [32], FITKO Jahresbericht [9], ZenDiS [25, 42]), der Schweiz (EMBAG [1], E-Government Strategie Schweiz 2024–2027 [16], BGEID [38], eCH-Standards [17], GEVER [43], opendata.swiss [44]) und der Europäischen Union (Interoperable Europe Act [6], EU Open Source Strategy [5], EIF [45], NIS2 [27], Digitaler Kompass 2030 [51]) wurden systematisch ausgewertet, um verbindliche Anforderungen, empfohlene Architekturen und Anreizstrukturen zu identifizieren, die für die kommunale OSS-Einführung relevant sind.

### 2.3 Rahmen zur Technologiebewertung

Jede Technologiedomäne wurde anhand einer Bewertungsmatrix mit sieben Kriterien (detailliert in Anhang B) bewertet: Lizenzoffenheit, Deployment-Reife, Community-Gesundheit, Interoperabilität, Sicherheit, Gesamtbetriebskosten und Einsatz im öffentlichen Sektor. Die Bewertungen wurden aus Anbieter- und Community-Dokumentation, OSOR-Fallstudien, BSI-IT-Grundschutz-Kompatibilitätsbewertungen [26] und, wo verfügbar, aus begutachteten Evaluationen abgeleitet.

### 2.4 Stakeholder-Analyse

Die Stakeholder-Kategorien wurden durch das GovStack-Building-Blocks-Framework [31], das E-Government-Reifegradmodell von Wirtz–Weyerer [7] und die Analyse der deutschen Digitallotsen sowie der schweizerischen E-Government-Schweiz-Umsetzungsstrukturen [16] identifiziert. Stakeholder-Interessen, Einflussniveaus und Engagement-Strategien wurden anhand einer modifizierten Macht-Interesse-Matrix abgebildet.

### 2.5 Einschluss-/Ausschlusskriterien

**Eingeschlossen:** Softwarekomponenten mit einer OSI-anerkannten Lizenz; aktive Upstream-Community (Commit-Aktivität innerhalb von 12 Monaten); dokumentierte Produktiv-Deployments in der öffentlichen Verwaltung; Kompatibilität mit EU-/DE-/CH-Regulierungsanforderungen; ausreichende Dokumentation für unabhängiges Deployment.

**Ausgeschlossen:** Komponenten unter einer Einzelanbieter-Source-Available-Lizenz ohne OSI-Anerkennung; Komponenten ohne Referenz-Deployments im öffentlichen Sektor; Komponenten mit ungelösten Sicherheitshinweisen mit Bewertung CVSS ≥9,0 zum Zeitpunkt der Abfassung.

### 2.6 Einschränkungen

Dieses Papier ist ein strategisches Policy-Dokument, keine kontrollierte empirische Studie. Die Kostenangaben sind indikative Spannen, die aus veröffentlichten Fallstudien und Beschaffungsdaten abgeleitet sind, nicht aus primärer Feldforschung. Die Technologiebewertungen spiegeln den Stand der Upstream-Projekte zur Jahresmitte 2026 wider und erfordern regelmäßige Überprüfung. Der primäre Regulierungsrahmen des Papiers ist deutsch und schweizerisch; Kommunen in anderen EU-Mitgliedstaaten sollten die Anwendbarkeit spezifischer gesetzgeberischer Verweise prüfen. Der Münchner LiMux-Fall wird als mahnende Illustration behandelt, nicht als Widerlegung der allgemeinen Open-Source-These.

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen

Die akademische Erforschung des Electronic Government hat sich über mehrere unterschiedliche Phasen entwickelt. Die Speyerer Definition von Lucke und Reinermann [47] begründete das grundlegende Vokabular für die deutschsprachige E-Government-Forschung: die Bereitstellung staatlicher Informationen und Dienstleistungen über elektronische Netze, strukturiert entlang der Achsen der Government-to-Citizen- (G2C), Government-to-Business- (G2B) und Government-to-Government- (G2G) Interaktionen. Dunleavy et al.’s Digital Era Governance [54] bot eine strukturelle Kritik der IT-Outsourcing-Pathologien des New Public Management — Fragmentierung, Agenturisierung und Einzelanbieter-Abhängigkeit — und nahm viele der Souveränitätsbedenken vorweg, die die aktuelle Politik beleben.

Janowski [30] formulierte ein vierstufiges Entwicklungsmodell des digitalen Staates — Digitalisierung, Transformation, Engagement und Kontextualisierung —, das einen entwicklungsbezogenen Rahmen zur Bewertung der kommunalen Bereitschaft bietet. Das OECD Digital Government Policy Framework [49] operationalisierte den digitalen Staat als ein mehrdimensionales Konstrukt, das Digital by Design, einen datengetriebenen öffentlichen Sektor, Government as a Platform, Open by Default, Nutzerorientierung und Proaktivität umfasst. Scholl [55] lieferte einen reflektierenden Überblick über die intellektuelle Entwicklung des Feldes. Bertot, Jaeger und Grimes [48] etablierten die empirische Verknüpfung zwischen IKT-Einsatz und Transparenzergebnissen — eine zentrale Rechtfertigung für die Open-Data-Komponenten des in Abschnitt 4 beschriebenen Stacks.

### 3.2 Digitale Souveränität

Digitaler Souveränität als politischem Konzept fehlt eine einzelne kanonische Definition. Dieses Papier übernimmt eine zusammengesetzte Definition, die das Manifest „Public Money? Public Code!“ der FSFE [4], die Open-Source-Strategie der Europäischen Kommission [5] und die GovStack-Building-Blocks-Rahmung [31] synthetisiert. Im Kern erfordert Souveränität: Auditierbarkeit (die Fähigkeit, Code zu prüfen), Modifizierbarkeit (die Fähigkeit, Code an lokale Anforderungen anzupassen), Portabilität (die Fähigkeit, von einem Anbieter oder Hosting-Dienstleister abzuwandern, ohne prohibitive Wechselkosten) und Rechenschaftspflicht (klare Governance darüber, wer die Software und ihre Daten kontrolliert).

Der Interoperable Europe Act [6] operationalisiert eine Dimension der Souveränität durch verbindliche Interoperabilitätsbewertung, indem er öffentliche Stellen verpflichtet, vor dem Einsatz neuer IKT-Lösungen Interoperabilitätsbewertungen durchzuführen und zu veröffentlichen. Das Prinzip „Public Money? Public Code!“ [4] wurde von einer wachsenden Zahl europäischer kommunaler und regionaler Regierungen formell übernommen. Lathrop und Ruma [15] liefern die normative Grundlage, die offenes Regierungshandeln — gekennzeichnet durch Transparenz, Zusammenarbeit und Partizipation — mit Open-Source-Infrastruktur als notwendige (wenn auch nicht hinreichende) Bedingung verknüpft.

### 3.3 Das deutsche OZG-Ökosystem

Deutschlands Onlinezugangsgesetz (OZG), 2017 erlassen und 2024 als OZG 2.0 [2] grundlegend überarbeitet, ist das gesetzgeberische Rückgrat der deutschen kommunalen Digitalisierung. OZG 2.0 führt das Prinzip „Once Only“ ein — Bürgerinnen und Bürger sollen dieselben Daten nicht mehrfach bei verschiedenen Behörden einreichen müssen — und etabliert einen bundesweiten Marktplatz digitalisierter Verwaltungsleistungen (Leistungen), die Kommunen abrufen können. FITKO (Föderale IT-Kooperation) koordiniert die technische Umsetzung über die Länder hinweg [9]. Das Programm Föderales Informationsmanagement (FIM) [32] stellt die semantischen Standards (FIM-Prozesse, FIM-Leistungen, FIM-Daten) bereit, die für die jurisdiktionsübergreifende Wiederverwendung von Leistungen erforderlich sind.

Die Plattform openCode.de [10], betrieben von der Digitalservice GmbH des Bundes, stellt ein öffentliches Code-Repository für Bundes- und Landes-OSS-Komponenten bereit, die Kommunen wiederverwenden können. govdigital eG [23] und Dataport AöR [24] bieten genossenschaftliche Hosting- und Managed-Service-Modelle, die die Betriebslast für einzelne Kommunen verringern. ZenDiS GmbH [25] — das Zentrum für Digitale Souveränität — koordiniert die Bundes-Arbeitsplatzsuite OpenDesk [42] und berät öffentliche Stellen zu souveränitätskompatibler Beschaffung. Die AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) [18] versorgt bayerische Kommunen mit gemeinsamen IT-Diensten und hat begonnen, Open-Source-Komponenten in ihren Leistungskatalog zu integrieren. Die XÖV-Standards [46], entwickelt von der KoSIT, stellen XML-basierte Datenaustauschformate für die interbehördliche Kommunikation bereit und untermauern die technische Interoperabilität, die OZG 2.0 verlangt.

### 3.4 Schweizerische kantonale und föderale digitale Dienste

Die digitale Verwaltungslandschaft der Schweiz wird durch ihre föderale Struktur geprägt: Der Bund, 26 Kantone und rund 2.200 Gemeinden üben jeweils erhebliche Verwaltungsautonomie aus. Das EMBAG [1] — Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben, in Kraft seit dem 1. Januar 2024 — ist eine wegweisende Bestimmung: Artikel 9 verlangt, dass von oder für Bundesbehörden entwickelte Software als Open Source veröffentlicht wird, sofern keine Ausnahmen wegen Sicherheit, Rechten Dritter oder unverhältnismäßigem Aufwand greifen. Dieses Mandat „Open Source by Default“ stellt eine der fortschrittlichsten OSS-Anforderungen in der europäischen öffentlichen Verwaltung dar.

Die E-Government Strategie Schweiz 2024–2027 [16] identifiziert Interoperabilität, digitale Identität und Datenwiederverwendung als die drei strategischen Säulen. Das Standardisierungsgremium eCH [17] veröffentlicht technische Standards für den E-Government-Datenaustausch, die den deutschen XÖV entsprechen, jedoch schweizerische verfassungsrechtliche Besonderheiten einschließlich der viersprachigen Verwaltung widerspiegeln. Das Bundesgesetz über den elektronischen Identitätsnachweis (BGEID) [38] schafft die rechtliche Grundlage für die schweizerische elektronische Identität (E-ID), basierend auf einem dezentralen, datenschutzwahrenden Wallet-Modell. Das GEVER-Framework des Schweizerischen Bundesarchivs [43] regelt die elektronische Schriftgutverwaltung in den Bundesbehörden. opendata.swiss [44] ist das schweizerische nationale Open-Data-Portal, das einen föderierten Katalog maschinenlesbarer staatlicher Datensätze unter standardisierten Lizenzen bereitstellt.

### 3.5 Open-Source-Communities und souveräne Technologie

Das Open-Source-Ökosystem für die öffentliche Verwaltung ist seit der ersten Welle staatlicher Linux-Deployments in den frühen 2000er-Jahren erheblich gereift. Das OSOR [28, 53] katalogisiert über 700 OSS-Deployments des öffentlichen Sektors in den EU-Mitgliedstaaten. Die FSFE [4] setzt sich weiterhin für Open-Source-Beschaffungsmandate ein und hat formelle Befragungen von mehreren europäischen Städten und Regionen erreicht. GovStack [31] stellt eine Building-Blocks-Spezifikation bereit, die generische staatliche Dienstkomponenten auf Open-Source-Referenzimplementierungen abbildet und so die Wiederverwendung über Jurisdiktionen hinweg erleichtert.

Community-Governance ist ein materieller Risikofaktor. Das GovStack-Framework [31] unterscheidet zwischen stiftungsgeführten Projekten (z. B. Nextcloud unter dem dualen Modell aus Nextcloud GmbH + Community [13]), konsortialgeführten Projekten (z. B. Sovereign Cloud Stack unter OSBA-Governance [3, 11]) und kommunal geführten Forks (mit dem höchsten Wartungsrisiko). Für souveränes Deployment empfiehlt dieses Papier eine Präferenz für stiftungsgeführte und konsortialgeführte Projekte mit nachgewiesener Akzeptanz im öffentlichen Sektor.

### 3.6 Gesamtbetriebskosten und ökonomische Evidenz

Die Ökonomie kommunaler Software wird sowohl in der proprietär-befürwortenden als auch in der open-source-befürwortenden Argumentation häufig falsch dargestellt. Eine ausgewogene TCO-Analyse muss umfassen: Lizenzgebühren, Implementierungs- und Integrationskosten, operatives Personal, Schulung, Supportverträge, Migrationskosten und die Opportunitätskosten des Lock-in.

**Proprietäre Benchmark-Kosten.** Die Lizenzierung von Microsoft 365 Government (G3/G5-Stufen) kostet typischerweise 150–400 Euro pro Nutzer und Jahr für Kern-Produktivitäts- und Kollaborationssuiten, ohne zusätzliche Module, Compliance-Add-ons, Azure-Hosting und Implementierungsdienste. Für eine Kommune mit 800 Beschäftigten beträgt die jährliche Lizenzexposition daher 120.000–320.000 Euro allein für Produktivitätssoftware, vor Infrastruktur und Fachverfahren.

**Open-Source-TCO-Evidenz.** Das Programm zur digitalen Transformation Barcelonas (2016–2019), verankert durch die Plattform für partizipative Demokratie Decidim [12] und eine ausdrückliche Politik für ethische digitale Standards, soll der Stadt über vier Jahre hinweg 30–40 Millionen Euro durch reduzierte proprietäre Lizenzierung und intern erbrachte Entwicklung eingespart haben. Schleswig-Holstein kündigte 2021 eine strukturierte Migration von 25.000 Landes-Arbeitsplätzen auf LibreOffice und Linux an, wobei die Landesregierung Lizenzkostensenkungen als primäre Triebfeder anführte. Das Projekt OpenDesk [42] baut die bundesweite Evidenzbasis für deutschsprachige Open-Source-Produktivitätssuiten auf.

**München LiMux (Mahndaten).** Die Münchner LiMux-Migration (2003–2013) konvertierte etwa 15.000 Arbeitsplätze auf Linux und LibreOffice und sparte Berichten zufolge 10 Millionen Euro an Lizenzkosten ein. Die anschließende Umkehr (2017–2021, Rückkehr zu Windows/Microsoft 365) wird häufig als Beleg dafür angeführt, dass Open Source im großen Maßstab scheitert. Eine sorgfältige Lektüre der Münchner Post-Mortem-Literatur zeigt, dass die Umkehr primär getrieben wurde durch: politischen Wechsel der kommunalen Führung, unzureichende Investitionen in Veränderungsmanagement und Mitarbeiterschulung, Kompatibilitätsprobleme mit Windows-abhängigen Arbeitsabläufen der Landesregierung und eine bewusste politische Entscheidung statt eines nachgewiesenen technischen Versagens.

**Schweizerische Evidenz.** Schweizerische kantonale Verwaltungen, die Open-Source-Komponenten über eCH-standardisierte Schnittstellen [17] und das GEVER-Framework [43] eingeführt haben, berichten, dass die Interoperabilitätsstandardisierung — statt der Lizenzwahl an sich — die primäre TCO-Triebfeder ist. Kommunen, die eCH-konforme Open-Source-Komponenten einführen, profitieren von gemeinsamen Datenmodellen, was die Integrationskosten senkt. Der OSOR Annual Report [28] und die Joinup-Plattform [53] stellen den derzeit umfassendsten vergleichenden Datensatz für die TCO europäischer staatlicher OSS bereit.

### 3.7 Bürgererfahrung und digitale Inklusion

Digitale Souveränität ist nicht nur ein institutionelles Anliegen. Bürgerinnen und Bürger interagieren mit kommunalen digitalen Diensten über ein breites Spektrum technischer Fähigkeiten, sprachlicher Hintergründe und Gerätezugänge hinweg. Sowohl die OECD [49] als auch die UN E-Government Survey [29] dokumentieren anhaltende digitale Klüfte, die Open-Source-Strategien ausdrücklich adressieren müssen.

**Barrierefreiheit.** Die EU-Richtlinie über den barrierefreien Zugang zu Websites (2016/2102) und der Durchführungsbeschluss (EU) 2018/1524 verlangen, dass Websites und mobile Anwendungen des öffentlichen Sektors WCAG 2.1 Level AA erfüllen. In Deutschland setzt die BITV 2.0 (Barrierefreie-Informationstechnik-Verordnung) diese Anforderung um. In der Schweiz gelten die föderalen Barrierefreiheitsrichtlinien P028. Kommunen, die Open-Source-CMS, Bürgerportale und Partizipationsplattformen auswählen, müssen die Konformität mit WCAG 2.1 AA prüfen. TYPO3 [19] und Decidim [12] unterhalten aktive Arbeitsgruppen zur Barrierefreiheit und veröffentlichen Konformitätserklärungen.

**Mehrsprachigkeitsanforderungen.** Schweizerische Kommunen müssen möglicherweise Bürgerinnen und Bürger auf Deutsch, Französisch, Italienisch oder Rätoromanisch bedienen. Deutsche Kommunen in Grenzregionen bieten zunehmend Dienste auf Türkisch, Arabisch und in anderen Gemeinschaftssprachen an. Open-Source-CMS- und Portalplattformen unterstützen mehrsprachige Inhalte im Allgemeinen über etablierte Module, doch müssen Kommunen Mittel für Übersetzungsabläufe und Content-Governance einplanen.

**Bürgervertrauen.** Die UN E-Government Survey [29] identifiziert das Bürgervertrauen als die bedeutendste nachfrageseitige Barriere für die E-Government-Akzeptanz. Vertrauen wird aufgebaut durch Transparenz (Open Source bietet Auditierbarkeit), Datenschutz (DSGVO-Konformität, Datenminimierung) und Dienstzuverlässigkeit. Sowohl die FSFE [4] als auch Janssen et al. [8] argumentieren, dass Open-Source-E-Government-Infrastruktur gegenüber Black-Box-proprietären Systemen intrinsische vertrauensbildende Eigenschaften besitzt.

**Inklusives Service-Design.** Janssen, Charalabidis und Zuiderwijk [8] identifizieren Service-Design — nicht die Technologiewahl — als die primäre Determinante der Akzeptanz von Open Data und E-Government durch Bürgerinnen und Bürger. Open-Source-Plattformen sind eine notwendige, aber nicht hinreichende Bedingung für inklusive digitale Dienste. Kommunen müssen neben dem technischen Plattform-Deployment in UX-Forschung, Inhalte in einfacher Sprache und assistierte digitale Unterstützungskanäle investieren.

### 3.8 Lücken und Agenda

Die Literatur offenbart mehrere bedeutende Lücken:

- Längsschnitt-TCO-Studien auf kommunaler Ebene, die Full-Stack-Open-Source- gegenüber proprietären Deployments über Zeithorizonte von fünf und mehr Jahren vergleichen, fehlen weitgehend. Der Münchner Fall ist illustrativ, aber durch politische Variablen verzerrt.
- Die regulatorische Interoperabilität zwischen dem deutschen OZG-Ökosystem und den schweizerischen EMBAG-/eCH-Rahmen wurde nicht systematisch kartiert; grenzüberschreitende Kommunen sehen sich einer unerforschten Compliance-Komplexität gegenüber.
- KI-Governance in der öffentlichen Verwaltung ist ein aufkommendes Feld; souveränes KI-Deployment auf kommunaler Ebene hat zur Jahresmitte 2026 keine etablierte Literaturbasis.
- Bürgervertrauen in Open-Source-E-Government im Besonderen wurde in europäischen kommunalen Kontexten nicht empirisch untersucht.

## 4. Analyse des Technologie-Stacks

Die folgenden Abschnitte bewerten elf Technologiedomänen anhand des in Anhang B beschriebenen Rahmens mit sieben Kriterien.

### 4.1 Digitale Identität — Keycloak

**Empfohlene Komponente:** Keycloak [21] | **Lizenz:** Apache 2.0 | **Score: 4.70/5**

Keycloak bietet Identitäts- und Zugriffsmanagement über OpenID Connect (OIDC), OAuth 2.0 und SAML 2.0 für kommunale Anwendungen. Es unterstützt Multi-Faktor-Authentifizierung, fein granulierte Autorisierung und die Integration mit externen Identitätsanbietern einschließlich der deutschen BundID und der schweizerischen E-ID [38]. Die Föderationsfähigkeiten von Keycloak erlauben es einer Kommune, einen einzigen autoritativen Identitätsspeicher zu unterhalten, während die Authentifizierung an Bürger-Identitätsanbieter delegiert wird, in Konformität mit den Anforderungen von OZG 2.0 [2] und EMBAG [1].

Deployment-Referenzen umfassen den gehosteten Keycloak-Dienst von Dataport für norddeutsche Kommunen [24] und die Aufnahme von Keycloak als Identitätsschicht von OpenDesk durch ZenDiS [42]. Die Kompatibilität mit BSI IT-Grundschutz [26] ist durch Standard-Härtungsverfahren erreichbar.

**Schlüsselintegration:** Keycloak sollte als zentraler Identitäts-Broker konfiguriert werden, wobei bürgernahe Anwendungen OIDC-Token konsumieren und Mitarbeiteranwendungen SAML für die Legacy-Kompatibilität verwenden.

### 4.2 Dokumentenmanagement — Nextcloud + OpenProject

**Empfohlene Komponenten:** Nextcloud [13] (AGPL-3.0, Score 4.20) + OpenProject [20] (GPLv3, Score 3.65)

Nextcloud bietet föderierte Dateispeicherung, -freigabe und -zusammenarbeit mit Funktionen auf Unternehmensniveau einschließlich Ende-zu-Ende-Verschlüsselung, Audit-Logging und mobilen Clients. Deployments von Nextcloud for Government [13] umfassen mehrere deutsche Landesverwaltungen und schweizerische kantonale Ämter. OpenProject bietet Projektmanagement, Aufgabenverfolgung und Dokumenten-Workflows.

**GEVER-Integration (CH):** Schweizerische Kommunen müssen diese Kombination gegen die Anforderungen des GEVER-Frameworks [43] für die Schriftgutverwaltung bewerten. Eine konforme Schriftgutverwaltungsschicht (eCH-0039 [17]) muss möglicherweise oberhalb von Nextcloud für formelle Aufzeichnungen liegen, die Aufbewahrungspflichten unterliegen.

### 4.3 Workflow-Automatisierung — Camunda / Flowable

**Empfohlene Komponenten:** Camunda Platform 8 Community [33] (Apache 2.0, Score 4.20) / Flowable (Apache 2.0)

BPMN-2.0-basierte Workflow-Engines sind wesentlich für die Digitalisierung von Verwaltungsprozessen unter OZG 2.0 [2] und FIM [32]. Die FIM-Prozessbibliothek stellt wiederverwendbare BPMN-Prozessvorlagen für mehr als 575 standardisierte Verwaltungsverfahren bereit und reduziert den Aufwand für die kundenspezifische Entwicklung erheblich. Beide Plattformen unterstützen die XÖV-Datenaustauschstandards [46] und sind mit FIM-Prozessmodellen kompatibel.

**Schlüsselintegration:** Workflow-Engines sollten mit Keycloak [21] für die Authentifizierung und mit Nextcloud [13] für Dokumentenanhänge integriert und auf Kubernetes [39] auf SCS-Infrastruktur [3] bereitgestellt werden.

### 4.4 Bürgerbeteiligung — Decidim / CONSUL

**Empfohlene Komponenten:** Decidim [12] (AGPL-3.0, Score 3.90) / CONSUL Democracy [40] (AGPL-3.0)

Digitale Beteiligungsplattformen werden zunehmend im Rahmen kommunaler demokratischer Beteiligungspflichten vorgeschrieben oder erwartet. Decidim — in Barcelona entwickelt und von der Decidim Association [12] gepflegt — bietet Bürgerhaushalte, Vorschläge, Versammlungen und deliberative Prozesse. CONSUL Democracy [40], entwickelt vom Ayuntamiento de Madrid, bietet vergleichbare Funktionen mit einer stärkeren Erfolgsbilanz in spanischsprachigen Jurisdiktionen.

Decidim ist die empfohlene primäre Wahl für deutsch- und französischsprachige Kommunen aufgrund seiner aktiveren Internationalisierungs-Community, seiner WCAG-2.1-AA-Audit-Historie und seiner Integration in europäische digitale Beteiligungsnetzwerke. Die Plattform ist in über 400 Kommunen weltweit im Einsatz, darunter Barcelona, Helsinki und mehrere schweizerische Gemeinden.

### 4.5 Kommunikation — Matrix / Jitsi / BigBlueButton

**Empfohlene Komponenten:** Matrix/Synapse [14] (Apache 2.0, Score 4.35), Jitsi Meet [35] (Apache 2.0), BigBlueButton [34] (LGPL-3.0, Score 3.90)

Das Matrix-Protokoll [14] bietet ein föderiertes, Ende-zu-Ende-verschlüsseltes Messaging-Gewebe für die Mitarbeiterkommunikation. Element (der Vorzeige-Matrix-Client) ist das Kommunikationsrückgrat der Tchap-Plattform der französischen Regierung und des deutschen BundesMessengers. Jitsi Meet [35] bietet leichtgewichtige, browserbasierte Videokonferenzen. BigBlueButton [34] bietet eine funktionsvollständigere Plattform, die für öffentliche Ratssitzungen und Bürgerkonsultationen geeignet ist.

### 4.6 Open Data — CKAN

**Empfohlene Komponente:** CKAN [22] | **Lizenz:** AGPL-3.0 | **Score: 4.25/5**

CKAN ist die De-facto-Standard-Open-Data-Portalplattform für die europäische Verwaltung und untermauert data.gov.uk, das EU Open Data Portal, opendata.swiss [44] und GovData.de. Für Kommunen bietet CKAN einen standardkonformen Datenkatalog (DCAT-AP), Datensatzverwaltung, API-Zugriff und Harvesting von anderen CKAN-Instanzen. Kommunen, die auf CKAN veröffentlichen, können sich über DCAT-AP-Harvesting mit kantonalen/Länder-Portalen und nationalen Portalen föderieren und so Open-Data-Verpflichtungen unter OZG 2.0 [2] und der schweizerischen Open-Government-Data-Strategie [44] erfüllen.

### 4.7 GIS — QGIS / GeoServer / OpenStreetMap

**Empfohlene Komponenten:** QGIS [37] (GPL-2.0+, Score 4.85), GeoServer, OpenStreetMap [36] (ODbL-1.0)

QGIS [37] bietet ein voll ausgestattetes Desktop-GIS für kommunale Mitarbeiter mit nativer Unterstützung für OGC-Standards (WMS, WFS, WCS). GeoServer bietet serverseitige Veröffentlichung räumlicher Daten und OGC-Webdienste. OpenStreetMap [36] bietet eine global gepflegte, lizenzgebührenfreie Basiskarte. GeoServer sollte WMS/WFS-Dienste bereitstellen, die vom kommunalen Webportal für öffentlichkeitsorientierte Kartenanwendungen konsumiert werden. QGIS integriert sich mit PostgreSQL/PostGIS [41] für die Speicherung räumlicher Daten.

### 4.8 CMS — TYPO3 / Drupal

**Empfohlene Komponenten:** TYPO3 [19] (GPL-2.0, Score 4.20) / Drupal

Die kommunale Website und das Bürgerportal erfordern ein CMS, das redaktionelle Zugänglichkeit mit technischer Sicherheit, Barrierefreiheitskonformität und langfristiger Wartbarkeit verbindet. TYPO3 [19] nimmt in der deutschen und schweizerischen öffentlichen Verwaltung eine dominierende Position ein, mit außerordentlich hoher Durchdringung des öffentlichen Sektors in der DACH-Region. Die TYPO3 Association veröffentlicht spezifische Leitfäden für Deployments in der öffentlichen Verwaltung einschließlich Toolkits zur Konformität mit BITV 2.0 / WCAG 2.1 AA. Für die meisten deutschen und schweizerischen Kommunen ist TYPO3 die pragmatische Empfehlung auf Basis der bestehenden Dichte des Dienstleister-Ökosystems.

### 4.9 Cloud-Infrastruktur — Sovereign Cloud Stack

**Empfohlene Komponente:** Sovereign Cloud Stack (SCS) [3, 11] | **Lizenz:** Apache 2.0 | **Score: 4.40/5**

Der Sovereign Cloud Stack [3] ist eine von der OSBA koordinierte Open-Source-Cloud-Infrastrukturspezifikation, aufgebaut auf OpenStack, Kubernetes [39] und Ceph, mit zusätzlichen Schichten für Identität, Monitoring und Sicherheit, die mit BSI IT-Grundschutz [26] und den BSI-Cloud-Mindeststandards [52] abgestimmt sind.

SCS adressiert die grundlegende Frage der Infrastruktursouveränität: Eine Kommune oder ihr genossenschaftlicher Dienstleister kann SCS auf eigener oder geleaster Hardware innerhalb der deutschen oder schweizerischen Jurisdiktion betreiben und so Abhängigkeiten von US-amerikanischen Hyperscalern beseitigen und das Compliance-Problem der Schrems-II- / transatlantischen Datenübermittlung lösen. Mehrere SCS-zertifizierte Anbieter sind kommerziell verfügbar, und govdigital eG [23] entwickelt ein mandantenfähiges SCS-Angebot für die kommunale Nutzung.

### 4.10 KI- und Datendienste

**Souveräne KI-Prinzipien für die öffentliche Verwaltung.** Der Einsatz künstlicher Intelligenz in der Kommunalverwaltung wirft eigene Souveränitätsbedenken auf. Die Abhängigkeit von proprietären Large-Language-Model-(LLM-)APIs schafft Abhängigkeiten, die mit den Verpflichtungen aus Artikel 22 DSGVO bezüglich automatisierter Entscheidungsfindung in Konflikt geraten können, Bürgerdaten der Verarbeitung durch Dritte zu Bedingungen aussetzen, die nicht geprüft werden können, und einen Vendor-Lock-in auf Inferenz- statt auf Softwareebene schaffen.

Dieses Papier übernimmt fünf souveräne KI-Prinzipien für die kommunale öffentliche Verwaltung:

1. **Datenminimierung und Pseudonymisierung:** Jede KI-Komponente, die Bürgerdaten verarbeitet, muss die DSGVO-Datenminimierung und -Pseudonymisierung anwenden. Eingaben in KI-Modelle sollten keine direkt identifizierenden Informationen enthalten, es sei denn, dies ist unbedingt erforderlich und ausdrücklich eingewilligt.
2. **Lokale Inferenz als Standard:** Die KI-Inferenz sollte auf Infrastruktur unter der Kontrolle der Kommune oder ihres genossenschaftlichen Dienstleisters durchgeführt und nicht an externe APIs gesendet werden.
3. **Modelltransparenz:** Kommunen sollten Modelle mit offenen Gewichten (Llama 3.x, Mistral, Falcon) mit veröffentlichten Model Cards gegenüber geschlossenen proprietären Modellen bevorzugen.
4. **Human in the Loop:** In Übereinstimmung mit Artikel 22 DSGVO [27] dürfen Entscheidungen mit rechtlichen oder ähnlich erheblichen Auswirkungen auf Bürgerinnen und Bürger nicht ausschließlich durch automatisierte Verarbeitung getroffen werden. KI-Werkzeuge im kommunalen Kontext sollten als Entscheidungsunterstützungswerkzeuge fungieren, nicht als autonome Entscheidungsträger.
5. **Anbieterdiversifizierung:** Wo KI-Fähigkeiten extern beschafft werden, müssen Verträge die Datenportabilität sicherstellen, Exklusivität vermeiden und die Migration zu alternativen Anbietern erlauben.

**Empfohlene Open-Source-KI-Komponenten:**

| Komponente | Lizenz | Funktion |
|---|---|---|
| LocalAI | MIT | OpenAI-kompatibler REST-API-Server; betreibt Modelle mit offenen Gewichten lokal |
| Ollama | MIT | Laufzeitumgebung für lokales LLM-Deployment; wachsende Modellbibliothek |
| OpenWebUI | MIT | Browserbasierte Chat-Oberfläche für LocalAI-/Ollama-Backends |

**Kommunale KI-Anwendungsfälle:** Dokumentenzusammenfassung (Verarbeitung von Ratsprotokollen, Rechtstexten), FAQ-Chatbots für Bürgeranfragen (mit Eskalationspfad zum Menschen), Unterstützung bei der GIS-Analyse, Übersetzungsunterstützung für mehrsprachige Dienstinhalte und internes Wissensmanagement.

**Data-Warehouse-Integration:** Kommunale KI-Dienste sollten mit einem PostgreSQL-[41]-basierten Data Warehouse oder einem CKAN-[22]-Datenkatalog integriert werden, um Retrieval-Augmented Generation (RAG) über kommunale Datensätze zu ermöglichen. Dieser Ansatz beschränkt KI-Ausgaben auf verifizierte kommunale Daten, verringert das Halluzinationsrisiko und verbessert die Auditierbarkeit.

### 4.11 Referenzarchitektur

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 9 — CITIZEN & STAFF INTERFACES                               │
│  TYPO3/Drupal (portal)  │ Decidim/CONSUL (participation)           │
│  OpenWebUI (AI chat)    │ Mobile apps (TYPO3 REST)                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 8 — COLLABORATION & COMMUNICATION                            │
│  Nextcloud (files/docs) │ OpenProject (PM) │ Matrix/Element (chat) │
│  Jitsi Meet (video)     │ BigBlueButton (webinar/council)          │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 7 — PROCESS & WORKFLOW                                       │
│  Camunda / Flowable (BPMN 2.0)  │ FIM Prozessbibliothek            │
│  XÖV/eCH Connectors              │ XForms / form engine             │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 6 — AI & DATA SERVICES                                       │
│  LocalAI / Ollama (LLM inference)  │ OpenWebUI (interface)         │
│  CKAN (open data portal)           │ PostgreSQL/PostGIS (warehouse)│
│  RAG pipeline                      │ Anonymisation / pseudonymise  │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 5 — GEOSPATIAL                                               │
│  GeoServer (OGC WMS/WFS) │ QGIS (desktop/server) │ OSM (base map)│
│  PostGIS (spatial DB)    │ Public map portal                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 4 — IDENTITY & SECURITY                                      │
│  Keycloak (IAM / OIDC / SAML)  │ BundID federation (DE)           │
│  Swiss E-ID / BGEID (CH)        │ BSI IT-Grundschutz controls      │
│  NIS2-compliant SIEM / logging  │ Vulnerability scanning           │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 3 — INTEGRATION & API GATEWAY                                │
│  REST / GraphQL API gateway  │ XÖV / eCH adapters                  │
│  FIM connectors              │ Event bus (Kafka / NATS)            │
│  Audit logging               │ OpenAPI specifications               │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 2 — CONTAINER ORCHESTRATION                                  │
│  Kubernetes [39] │ Helm charts │ GitOps (Flux / ArgoCD)           │
│  Prometheus/Grafana (monitoring) │ Loki/OpenSearch (logging)      │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  LAYER 1 — SOVEREIGN CLOUD INFRASTRUCTURE — SCS [3]               │
│  OpenStack (compute/network/storage) │ Ceph (block/object/file)   │
│  SCS-certified hoster OR on-premise  │ DE/CH/EU jurisdiction only  │
│  govdigital eG [23] / Dataport [24] / cantonal ICT provider        │
└────────────────────────────────────────────────────────────┘
```

Alle Schichten kommunizieren über offene APIs, die in OpenAPI-Spezifikationen dokumentiert sind. Die Container-Orchestrierung über den gesamten Stack wird von Kubernetes [39] übernommen, die relationale Persistenz von PostgreSQL [41] und die Objektspeicherung von Ceph auf SCS [3]. Der Datenaustausch verwendet XÖV-Standards (Deutschland) [46] oder eCH-Standards (Schweiz) [17]. Die Sicherheit wird durch BSI IT-Grundschutz [26] (DE) oder das schweizerische ISDS-Framework geregelt.

## 5. Umsetzungsfahrplan

Der folgende phasenweise Fahrplan ist für eine Kommune mit 50.000–200.000 Einwohnern und 200–1.000 Verwaltungsmitarbeitern konzipiert. Die Kostenspannen sind indikativ und sollten durch eine kommunenspezifische Machbarkeitsstudie präzisiert werden. Alle Angaben sind in EUR und stellen die Gesamtinvestition einschließlich externer Dienste, Hardware (wo zutreffend) und interner Personalzeit zu Marktpreisen dar. Kommunen, die an kooperativer Beschaffung teilnehmen (govdigital [23], Dataport [24], kantonale IKT), sollten Kosten am unteren Ende jeder Spanne erwarten.

### Phase 0 — Organisatorische Bereitschaft und Basisbewertung

**Dauer:** 3–6 Monate | **Indikative Kostenspanne: 50.000–200.000 €**

**Ziele:** Durchführung der Selbstbewertung zur digitalen Souveränität (Anhang C); Kartierung des aktuellen Technologieportfolios und der Lizenzkosten; Etablierung des politischen und exekutiven Mandats; Definition der Governance-Struktur; Identifizierung kooperativer Partner.

**Ergebnisse:**
- Basisbericht zur digitalen Souveränität
- Software-Asset-Inventar mit TCO-Basislinie
- Beschluss des Gemeinderats
- Partnerschaftsvereinbarungen mit genossenschaftlichen Dienstleistern

**Erfolgskriterien:**
- Exekutiver Sponsor identifiziert und verpflichtet
- Software-Asset-Inventar vollständig
- Mindestens eine genossenschaftliche Partnerschaft etabliert
- Budgetrahmen für Phase 1 vom Rat genehmigt

### Phase 1 — Infrastruktur- und Identitätsfundament

**Dauer:** 6–12 Monate | **Indikative Kostenspanne: 150.000–500.000 €**

**Ziele:** Bereitstellung der SCS-basierten [3] Cloud-Infrastruktur; Implementierung von Keycloak [21] föderiert mit BundID/E-ID; Etablierung eines Kubernetes-Clusters [39] mit GitOps-Pipeline; Implementierung einer NIS2-konformen Sicherheitsbasislinie [27].

**Ergebnisse:**
- SCS-Infrastruktur betriebsbereit mit SLA-gestütztem genossenschaftlichem Support
- Keycloak-Identitätsplattform produktiv mit nationaler Identitätsföderation
- BSI-IT-Grundschutz-[26]-Basisdokumentation vollständig
- NIS2-Incident-Response-Verfahren etabliert

**Erfolgskriterien:**
- Infrastruktur-Verfügbarkeit ≥99,5 % über einen Beobachtungszeitraum von 60 Tagen
- Alle Mitarbeiter können sich über Keycloak-SSO authentifizieren
- Erste IT-Grundschutz-Lückenanalyse abgeschlossen und Behebungsplan genehmigt

### Phase 2 — Kollaborations- und Kommunikationsplattform

**Dauer:** 6–12 Monate | **Indikative Kostenspanne: 200.000–600.000 €**

**Ziele:** Bereitstellung von Nextcloud [13] und OpenProject [20]; Bereitstellung von Matrix/Element [14] für das Mitarbeiter-Messaging; Bereitstellung von Jitsi [35] und BigBlueButton [34]; Durchführung eines Mitarbeiterschulungsprogramms.

**Ergebnisse:**
- Nextcloud mit Rollout-Plan auf Abteilungsebene
- Matrix-Homeserver föderiert mit Landesregierungsinstanzen, wo verfügbar
- Videokonferenzen betriebsbereit und für Ratssitzungen getestet
- Schulungsmaterialien und internes Netzwerk von OSS-Champions

**Erfolgskriterien:**
- ≥80 % der Mitarbeiter der Pilotabteilung nutzen Nextcloud für das primäre Dateimanagement
- ≥60 % der internen Besprechungen über selbst gehostete Konferenzdienste
- Mitarbeiterzufriedenheitsumfrage mit Wert ≥3,5/5,0

### Phase 3 — Workflow-Automatisierung und digitale Dienste

**Dauer:** 9–18 Monate | **Indikative Kostenspanne: 150.000–400.000 €**

**Ziele:** Bereitstellung der Camunda-/Flowable-[33]-Workflow-Engine; Digitalisierung der zehn wichtigsten bürgernahen Prozesse mithilfe von FIM-Vorlagen [32]; Integration von OZG-2.0-Diensten [2]; Bereitstellung des CKAN-[22]-Open-Data-Portals; Start des TYPO3-[19]-Bürgerportals mit WCAG-2.1-AA-Konformität.

**Ergebnisse:**
- Die zehn wichtigsten Bürgerprozesse digitalisiert und veröffentlicht
- OZG-2.0-Dienste integriert und von der Landesbehörde bestätigt
- CKAN-Portal live mit mindestens 20 zum nationalen Portal föderierten Datensätzen
- TYPO3-Portal mit veröffentlichter Konformitätserklärung zu BITV 2.0 / WCAG 2.1 AA

**Erfolgskriterien:**
- Die zehn wichtigsten Dienste durchgängig online verfügbar ohne obligatorischen Papierschritt
- CKAN-Portal von govdata.de oder opendata.swiss geharvestet
- WCAG-2.1-AA-Audit von unabhängiger dritter Partei bestanden

### Phase 4 — Erweiterte Dienste und Bürgerbeteiligung

**Dauer:** 6–12 Monate | **Indikative Kostenspanne: 100.000–300.000 €**

**Ziele:** Bereitstellung von Decidim [12] oder CONSUL [40] für die Bürgerbeteiligung; Bereitstellung des GIS-Stacks (QGIS [37], GeoServer, OSM [36]); Start souveräner KI-Dienste (LocalAI/Ollama, OpenWebUI); Implementierung eines PostgreSQL-[41]-Data-Warehouse mit RAG.

**Ergebnisse:**
- Beteiligungsplattform betriebsbereit mit erstem partizipativem Prozess
- GIS-Stack betriebsbereit mit öffentlichem Kartenportal
- KI-Assistent für Mitarbeiter zur Dokumentenzusammenfassung und FAQ-Erstellung
- Data Warehouse betriebsbereit; keine Bürgerdaten an externe KI-APIs gesendet

**Erfolgskriterien:**
- ≥500 Bürgerteilnehmer im ersten Bürgerhaushalts-Zyklus
- GIS-Datensätze unter offener Lizenz auf CKAN veröffentlicht
- KI-Assistent von ≥50 % der Verwaltungsmitarbeiter angenommen

### Phase 5 — Optimierung, Beitrag und Replikation

**Dauer:** Laufend ab Monat 30+ | **Indikative jährliche Kosten: 50.000–150.000 €/Jahr**

**Ziele:** Optimierung der Betriebskosten; Beitrag zu Upstream-OSS-Communities; Veröffentlichung kommunaler Komponenten auf openCode.de [10]; Weitergabe von Erkenntnissen an Partnerkommunen; jährliche Überprüfung der Selbstbewertung.

**Ergebnisse:**
- Dokumentierte Beiträge zu Upstream-OSS-Projekten
- Mindestens ein Modul/eine Vorlage auf openCode.de veröffentlicht
- Interkommunale Wissensaustauschvereinbarung
- Jährlicher Bericht zur digitalen Souveränität an den Gemeinderat

**Erfolgskriterien:**
- Netto-Lizenzkosteneinsparungen nachweisbar gegenüber der Basislinie vor dem Übergang
- Mindestens ein OSS-Beitrag upstream akzeptiert
- Partnerkommune in kooperative Beschaffung oder Wissensaustausch eingebunden

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Rolle | Primäres Interesse | Einfluss | Engagement-Strategie |
|---|---|---|---|---|
| Gemeinderat | Politisches Mandat | Haushaltsverantwortung, Bürgernutzen | Hoch | Fortschrittsberichte, TCO-Dashboards |
| Bürgermeister/in / Verwaltungsspitze | Exekutiver Sponsor | Strategische Vision, Risikomanagement | Hoch | Einzelbriefings, Meilenstein-Reviews |
| CIO / IT-Leitung | Technische Leitung | Betriebszuverlässigkeit, Personalkapazität | Hoch | Co-Design des Fahrplans, technische Arbeitsgruppe |
| Verwaltungsmitarbeiter | Endnutzer | Bedienbarkeit, Schulung, Workflow-Kontinuität | Mittel–Hoch | Veränderungsmanagement, Champion-Netzwerk |
| Bürgerinnen und Bürger | Leistungsempfänger | Dienstverfügbarkeit, Datenschutz | Mittel | Beteiligungsplattformen, Transparenzberichterstattung |
| Landes-/kantonale IT-Behörde | Regulatorische Aufsicht | OZG/EMBAG-Compliance, Interoperabilität | Hoch | Frühzeitige Abstimmung, gemeinsame Beschaffung |
| govdigital / Dataport [23, 24] | Genossenschaftlicher Dienstleister | Geschäftsbeziehung, gemeinsame Dienste | Mittel | Rahmenvereinbarungen, SLA-Definition |
| OSS-Communities | Software-Lieferanten | Akzeptanz, Beitrag, Finanzierung | Niedrig | Community-Engagement, Upstream-Beiträge |
| Zivilgesellschaft / Digital-Rights-Organisationen | Interessenvertretung, Kontrolle | OSS-Prinzipien, Datenschutz | Niedrig–Mittel | Transparenzberichterstattung, Public-Code-Selbstverpflichtung |
| Lokale IKT-KMU | Implementierungspartner | Geschäftliche Chance | Mittel | Offene Beschaffung, UVgO-/VgV-Ausschreibungen |

### 6.2 Beschaffungsrahmen

Die kommunale OSS-Beschaffung muss die EU-Vergaberegeln, die deutschen VgV-/UVgO- oder schweizerischen BöB-/VöB-Verfahren und die Interoperabilitätsbewertungspflicht des Interoperable Europe Act [6] navigieren. Sechs Prinzipien regeln den Rahmen:

1. **Funktionsspezifikation, nicht Produktspezifikation.** Ausschreibungsunterlagen müssen erforderliche Funktionen spezifizieren (z. B. „föderiertes Identitätsmanagement konform zu OIDC 1.0 und SAML 2.0“) statt benannter Produkte, um offenen Wettbewerb zu gewährleisten und zugleich OSS-Angebote zuzulassen. Dies ist eine rechtliche Anforderung nach EU-Vergaberecht.

2. **Bewertung der Gesamtbetriebskosten.** Die Zuschlagskriterien müssen mehrjährige TCO umfassen, die Lizenz-, Implementierungs-, Betriebs-, Schulungs-, Ausstiegs- und Migrationskosten abdecken. Null Lizenzkosten für OSS bedeuten nicht null Gesamtkosten; proprietäre Alternativen untertreiben typischerweise die nachgelagerten Lock-in-Kosten.

3. **Offene Standards verpflichtend.** Alle beschafften Komponenten müssen XÖV [46] (DE), eCH [17] (CH), DCAT-AP (Open Data), OGC (GIS), OIDC/SAML (Identität), BPMN 2.0 (Workflow) unterstützen. Nichtkonformität sollte ein Ausschlusskriterium sein.

4. **Quellcode-Hinterlegung oder offene Lizenz.** Für jede maßgeschneiderte Entwicklung muss der Vertrag entweder die Open-Source-Veröffentlichung verlangen (EMBAG Artikel 9 [1] für schweizerische Kommunen; Best Practice für deutsche Kommunen) oder eine Quellcode-Hinterlegung etablieren, die der Kommune den Zugang sichert.

5. **Datenportabilität und Ausstiegsrechte.** Alle Verträge müssen unzweideutige Datenportabilität enthalten: Der Lieferant muss innerhalb von 30 Tagen nach Vertragsbeendigung einen vollständigen, maschinenlesbaren Export aller kommunalen Daten in einem offenen Format ohne zusätzliche Kosten bereitstellen.

6. **Genossenschaftliche und Rahmenbeschaffung.** Kommunen sollten Rahmenvereinbarungen priorisieren, die von govdigital [23], Dataport [24], BeschA oder kantonalen Beschaffungsstellen etabliert wurden, um den Verwaltungsaufwand zu verringern und von kollektiver Verhandlungsmacht zu profitieren.

### 6.3 Veränderungsmanagement

Die Münchner LiMux-Post-Mortem [Abschnitt 7.2] zeigt, dass technische Qualität für einen erfolgreichen OSS-Übergang nicht ausreicht. Veränderungsmanagement ist der kritische Erfolgsfaktor:

- **Interne OSS-Champions ernennen** in jeder Abteilung, geschult und ermächtigt, kollegiale Unterstützung zu leisten.
- **In Schulungen proportional zur Mitarbeiterzahl investieren.** Eine Faustregel von 3–5 Schulungstagen pro Mitarbeiter für einen Übergang der Produktivitätssuite steht im Einklang mit Best Practices der Unternehmenssoftware-Implementierung.
- **Offen über den Übergang kommunizieren.** Gemeinderatsbeschlüsse, Mitarbeiter-Newsletter und Ankündigungen auf der öffentlichen Website sollten die Begründung der digitalen Souveränität in einfacher Sprache erläutern.
- **Eine Rückkopplungsschleife etablieren.** Ein strukturierter Mitarbeiter-Feedback-Mechanismus (vierteljahrweise Umfrage, sichtbarer Issue-Tracker) erlaubt es, Probleme zu erkennen, bevor sie zu politischen Belastungen werden.
- **Pilotbetrieb vor Mandat.** Jede Plattform sollte in einer freiwilligen Abteilung pilotiert werden, bevor ein verpflichtender Rollout erfolgt. Pilotabteilungen sollten nach Begeisterung statt nach Dringlichkeit ausgewählt werden.

### 6.4 Rechts- und Compliance-Matrix

| Regelung | Jurisdiktion | Schlüsselanforderung | Auswirkung auf OSS-Stack | Compliance-Mechanismus |
|---|---|---|---|---|
| GDPR / DSGVO | EU / DE / CH (nDSG) | Rechtsgrundlage, Datenminimierung, Auskunftsrechte | Alle bürgernahen Komponenten; KI-Dienste | Privacy-by-Design in Nextcloud/Keycloak; DSGVO-konformes Hosting; DSB-Bestellung; Art. 22 Human-in-Loop für KI |
| NIS2-Richtlinie [27] | EU (DE: KRITIS-Dachgesetz) | Vorfallmeldung (24 h), Risikomanagement, Lieferkettensicherheit | SCS-Infrastruktur; alle kritischen Dienste | BSI IT-Grundschutz [26]; NIS2-kompatibles ISMS; Incident-Response-Playbook |
| OZG 2.0 [2] | DE | Online-Dienstverfügbarkeit; BundID; Once Only | Workflow [4.3]; Portal [4.8]; Identität [4.1] | Camunda-FIM-Integration; Keycloak-BundID-Föderation; OZG-Marktplatz |
| EMBAG [1] | CH | Open Source by Default (Art. 9); Veröffentlichungspflicht | Alle maßgeschneiderte Entwicklung | OSS-Lizenz auf eigenem Code; Veröffentlichung im kantonalen/föderalen Repository |
| Interoperable Europe Act [6] | EU | Interoperabilitätsbewertung vor Einsatz | Alle beschafften Komponenten | EIF-[45]-Bewertungs-Checkliste; Joinup-Veröffentlichung der Lösungen |
| BITV 2.0 / WCAG 2.1 AA | DE | AA-Konformität; Barrierefreiheitserklärung | Portal [4.8]; Beteiligung [4.4]; alle Web-Apps | WCAG-Audit durch Dritte; TYPO3-Barrierefreiheits-Toolkit |
| BSI IT-Grundschutz [26] | DE | Basissicherheitsmaßnahmen; Dokumentation | SCS [4.9]; Identität [4.1]; gesamte Infrastruktur | IT-Grundschutz-Implementierungsprojekt; jährliche Überprüfung |
| ISDS / P028 | CH | Sicherheitsbasislinie; Barrierefreiheit | Gesamte föderale/kantonale SW | P028-Konformitätsbewertung; ISDS-Risikomanagement |
| eCH-Standards [17] | CH | Datenaustausch-Compliance (eCH-0039, eCH-0058) | Workflow [4.3]; DMS [4.2]; Open Data [4.6] | eCH-konforme Schnittstellen; eCH-Zertifizierung, wo verfügbar |

## 7. Risikoanalyse

### 7.1 Risikoregister

| # | Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|---|
| R1 | Politische Umkehr — neue kommunale Führung kehrt OSS-Mandat um | Mittel | Hoch | Gemeinderatsbeschluss; dokumentierter Bürgernutzen und TCO-Einsparungen |
| R2 | Mitarbeiterwiderstand — Endnutzer verweigern Annahme neuer Werkzeuge | Mittel | Hoch | Veränderungsmanagement-Programm; Champion-Netzwerk; phasenweiser Rollout; Investition in Bedienbarkeit |
| R3 | Integrationsversagen mit Länder-/kantonalen Legacy-Systemen | Mittel | Mittel | XÖV-/eCH-Standardkonformität; frühzeitige Integrationstests; Länderkoordination |
| R4 | Ökosystem-Kollaps — Schlüssel-OSS-Komponente verliert Community-Support | Niedrig | Hoch | Multi-Lieferanten-Supportverträge; Upstream-Beitrag; Fork-Bereitschaft |
| R5 | Sicherheitsvorfall — Kompromittierung der souveränen Infrastruktur | Niedrig | Sehr hoch | BSI IT-Grundschutz [26]; NIS2-ISMS [27]; Penetrationstests; SCS-Sicherheitsbasislinie [3] |
| R6 | Kostenüberschreitung — Implementierungskosten übersteigen Schätzungen | Mittel | Mittel | Phasenweise Finanzierung; 20 % Kontingenzreserve; kooperative Beschaffung |
| R7 | Compliance-Versagen — DSGVO/NIS2/OZG/EMBAG-Nichtkonformität | Niedrig | Hoch | Rechts-Compliance-Matrix [Abschnitt 6.4]; DSB-Einbindung ab Phase 0 |
| R8 | KI-Governance-Versagen — Bürgerdaten durch KI-Dienste offengelegt | Mittel | Hoch | Nur lokale Inferenz; Datenminimierung; keine proprietären LLM-APIs für Bürgerdaten; DSGVO Art. 22 |
| R9 | Kompetenzlücke — unzureichende OSS-technische Kapazität intern | Hoch | Mittel | Investition in Schulung; genossenschaftliches Dienstmodell; schrittweise Internalisierung |
| R10 | Scope Creep — Fahrplan wächst über kommunale Kapazität hinaus | Mittel | Mittel | Phase-Gate-Governance; Freigabe durch exekutiven Sponsor; MVP-Disziplin |

### 7.2 Münchner Mahnfall

Das Münchner LiMux-Programm (2003–2013) ist der am ausführlichsten dokumentierte großflächige kommunale Open-Source-Übergang in der europäischen Geschichte, und seine Umkehr ist das am häufigsten angeführte Argument gegen die kommunale OSS-Einführung. Eine rigorose Lektüre der Evidenz [30, siehe auch Abschnitt 3.6] liefert eine differenziertere Lehre.

Die LiMux-Migration konvertierte erfolgreich etwa 14.800 Arbeitsplätze auf Ubuntu Linux und LibreOffice und erzielte dokumentierte Lizenzeinsparungen von etwa 10 Millionen Euro. Das Programm war technisch funktionsfähig: Die Mehrheit der migrierten Arbeitsplätze betrieb den Open-Source-Stack ohne berichteten Produktivitätsverlust, der über den vergleichbarer Windows-Migrationen hinausging.

Die Umkehr (eingeleitet durch die Koalitionsvereinbarung von CSU/SPD 2014, abgeschlossen etwa 2021) ist zurückzuführen auf: die Wahl eines neuen Bürgermeisters mit einer anderen Technologieorientierung; eine 2016 von der neuen Verwaltung in Auftrag gegebene interne Bewertung, die den Koordinationsaufwand von LiMux kritisierte; Lobbydruck von Microsoft (das anschließend seinen deutschen Hauptsitz nach München verlegte); und Kompatibilitätsherausforderungen mit den Windows-abhängigen Arbeitsabläufen der bayerischen Landesregierung.

**Lehren:**
1. Das politische Mandat muss in einem Ratsbeschluss institutionalisiert werden, nicht nur in einer Exekutiventscheidung.
2. Interoperabilität mit vertikalen Regierungssystemen ist existenziell; XÖV-/eCH-Konformität auf Länderebene ist eine Voraussetzung.
3. Investitionen in Veränderungsmanagement müssen verhältnismäßig sein; Unterschiede in der Benutzeroberfläche sind durch Schulung behebbar und nicht OSS inhärent.
4. Ökonomische Evidenz muss präemptiv dokumentiert werden, um politische Anfechtung zu überstehen.

### 7.3 Sicherheitsüberlegungen

Kommunale digitale Infrastruktur ist ein Ziel für Ransomware, Datendiebstahl und Einflussnahme durch Nationalstaaten. BSI IT-Grundschutz [26] stellt die maßgebliche deutsche Basislinie bereit. NIS2 [27] verlangt von Kommunen, die als wesentliche oder wichtige Einrichtungen klassifiziert sind, Risikomanagementmaßnahmen zu implementieren und erhebliche Vorfälle innerhalb von 24 Stunden zu melden.

Open-Source-Software bietet intrinsische Sicherheitsvorteile (öffentliche Code-Überprüfung, schnelle Community-Patch-Zyklen) neben Herausforderungen (kleineren Kommunen kann es an Personal fehlen, um CVE-Hinweise zu überwachen). Das genossenschaftliche Dienstmodell (govdigital [23], Dataport [24]) adressiert dies durch Zentralisierung des Sicherheitsbetriebs für mehrere kommunale Kunden.

**Wesentliche Sicherheitsmaßnahmen:**
- SCS-Infrastruktur [3] betrieben mit den BSI-Cloud-Mindeststandards [52] als Basislinie
- Keycloak [21] erzwingt MFA für alle Mitarbeiter und privilegierten Zugriff
- Sicherheitsupdates innerhalb von 48 Stunden nach Veröffentlichung kritischer CVE (CVSS ≧ 7.0)
- Jährliche Penetrationstests durch einen BSI-qualifizierten Auditor
- NIS2-konformer Incident-Response-Plan vor dem Go-Live von Phase 1 etabliert

### 7.4 Regulatorische Risikomatrix

| Regulatorische Entwicklung | Wahrscheinlichkeit (3 Jahre) | Kommunale Auswirkung | Reaktion |
|---|---|---|---|
| NIS2-Ausweitung auf kleinere Kommunen | Mittel | Verpflichtendes ISMS; Kosten der Vorfallmeldung | ISMS in Phase 1 proaktiv implementieren |
| Neueinstufung kommunaler KI-Anwendungsfälle nach EU AI Act | Mittel | Anforderungen an Konformitätsbewertung | KI-Anwendungsfälle dokumentieren; Hochrisikokategorien vermeiden; Human-in-Loop beibehalten |
| Verschärfung des OZG-2.0-Interoperabilitätsmandats | Hoch | Schnellerer Umsetzungszeitplan | Phase-3-OZG-Integration priorisieren; enger Kontakt zur Länder-IT-Behörde |
| DSGVO-Durchsetzung bei Nicht-EU-Cloud-Hosting | Mittel | Herausforderung für Nicht-SCS-Deployments | Migration zu SCS [4.9] in Phase 1; Nicht-EU-Hyperscaler vermeiden |
| Beschleunigung des schweizerischen BGEID-Rollouts [38] | Hoch (CH) | Schnellere E-ID-Integration erforderlich | Keycloak-E-ID-Föderation in Phase 1 integrieren |
| Compliance-Frist des Interoperable Europe Act | Hoch | Interoperabilitätsbewertung erforderlich | EIF-[45]-Bewertung in alle Beschaffungen ab Phase 3 aufnehmen |
| Kantonale Ausweitung von EMBAG Artikel 9 (CH) | Mittel | OSS-Veröffentlichungspflichten | OSS-Veröffentlichungsklausel in alle Entwicklungsverträge aufnehmen |

## 8. Schlussfolgerung

Die Argumentation für open-source-basierte digitale Souveränität in der Kommunalverwaltung hat sich im vergangenen Jahrzehnt entschieden von der Interessenvertretung zur Evidenz verlagert. Gesetzgeberische Rahmen in Deutschland (OZG 2.0 [2]), der Schweiz (EMBAG [1]) und der Europäischen Union (Interoperable Europe Act [6], EU Open Source Strategy [5]) schaffen nun strukturelle Anreize — und in einigen Fällen Verpflichtungen — für öffentliche Verwaltungen, offene, interoperable und auditierbare Software zu bevorzugen. Die Technologiekomponenten, um einen vollständigen kommunalen digitalen Stack bereitzustellen, sind ausgereift, gut verwaltet und in vergleichbarem Maßstab in ganz Europa produktiv im Einsatz.

Dieses Papier hat über elf Technologiedomänen und einen sechsphasigen Umsetzungsfahrplan hinweg argumentiert, dass eine Kommune mit 50.000–200.000 Einwohnern einen vollständig souveränen Open-Source-Digital-Stack bereitstellen kann, der die funktionalen Anforderungen proprietärer Alternativen erfüllt oder übertrifft. Die kritischen Erfolgsfaktoren sind nicht technischer, sondern organisatorischer Natur: politisches Mandat mit institutioneller Beständigkeit; Investition in Veränderungsmanagement und Schulung proportional zur Mitarbeiterzahl; Beschaffungsrahmen, die Lock-in bestrafen statt den niedrigsten Anfangspreis zu belohnen; und kooperative Strukturen, die es Kommunen erlauben, die Betriebslast komplexer Infrastruktur zu teilen.

Die Münchner LiMux-Erfahrung ist eine mahnende Illustration, keine Widerlegung. Ihre Lehren — das Mandat institutionalisieren, in Interoperabilität investieren, die Ökonomie dokumentieren — sind vollständig in den hier vorgestellten Fahrplan und Governance-Rahmen integriert. Die Fälle Barcelona, Schleswig-Holstein und der schweizerischen Kantone zeigen, dass die These tragfähig ist, wenn diese Bedingungen erfüllt sind.

Digitale Souveränität ist kein Endzustand, sondern eine kontinuierliche Praxis. Die Kommune, die diesen Stack 2027 bereitstellt, wird ihre Technologieentscheidungen 2032 erneuern müssen. Der Vorteil des Open-Source-Ansatzes ist gerade, dass diese Erneuerung möglich ist: Komponenten können ohne Anbietererlaubnis oder vertragliche Strafe ersetzt, aktualisiert oder geforkt werden. Die digitale Infrastruktur der Öffentlichkeit sollte ebenso auditierbar, anpassbar und demokratisch sein wie die Institutionen, denen sie dient. Öffentliches Geld sollte öffentlichen Code hervorbringen [4].

## Literaturverzeichnis

[1] Swiss Federal Chancellery (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*, SR 172.019. Bern: Swiss Confederation. https://fedlex.admin.ch/eli/cc/2023/682/de. Licence: CC0.

[2] Bundesministerium des Innern und für Heimat (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de. Licence: DL-DE/Zero 2.0.

[3] Open Source Business Alliance (OSBA) (2023). *Sovereign Cloud Stack (SCS)*. Berlin: OSBA. https://scs.community. Licence: Apache 2.0 / CC-BY-SA-4.0.

[4] Free Software Foundation Europe (FSFE) (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu. Licence: CC-BY-SA-4.0.

[5] European Commission (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brussels: European Commission. https://commission.europa.eu. Licence: CC-BY.

[6] European Parliament and Council (2024). *Regulation (EU) 2024/903 — Interoperable Europe Act*, OJ L 903/2024, 22 March 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903. Licence: EU legislation (public domain).

[7] Wirtz, B.W. & Weyerer, J.C. (2017). Holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024.

[8] Janssen, M., Charalabidis, Y. & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740.

[9] FITKO (2024). *FITKO Jahresbericht 2023*. Frankfurt: FITKO. https://fitko.de. Licence: DL-DE/Zero 2.0.

[10] Digitalservice GmbH des Bundes (2023). *openCode.de*. Berlin: Digitalservice. https://opencode.de.

[11] SCS Community / OSBA (2024). *Sovereign Cloud Stack Technical Documentation*. Berlin: OSBA. https://docs.scs.community. Licence: Apache 2.0.

[12] Decidim Association (2021). *Decidim: Free Open-Source Participatory Democracy*. Barcelona: Decidim Association. https://decidim.org. Licence: AGPL-3.0.

[13] Nextcloud GmbH (2023). *Nextcloud for Government*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/. Licence: AGPL-3.0.

[14] The Matrix Foundation (2023). *Matrix Specification v1.9*. London: Matrix Foundation. https://spec.matrix.org. Licence: Apache 2.0.

[15] Lathrop, D. & Ruma, L. (Eds.) (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O'Reilly Media. ISBN 978-0-596-80435-0.

[16] E-Government Suisse (2023). *Strategie E-Government Schweiz 2024–2027*. Adopted 22 November 2023. Bern: Swiss Confederation. https://egovernment.ch. Licence: open access.

[17] eCH Association (2023). *eCH-Standards für E-Government Schweiz*. Zürich: eCH. https://ech.ch. Licence: CC-BY-4.0.

[18] AKDB (2023). *IT-Services für Kommunen in Bayern*. Munich: AKDB. https://akdb.de.

[19] TYPO3 Association (2023). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org. Licence: GPL-2.0.

[20] OpenProject GmbH (2023). *OpenProject for Government*. Berlin: OpenProject GmbH. https://openproject.org. Licence: GPLv3.

[21] Keycloak Community / Red Hat (2023). *Keycloak: Open Source Identity and Access Management*. https://keycloak.org. Licence: Apache 2.0.

[22] CKAN Association (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org. Licence: AGPL-3.0.

[23] govdigital eG (2023). *Genossenschaft für digitale Verwaltung*. Berlin: govdigital. https://govdigital.de.

[24] Dataport AöR (2023). *IT-Dienstleister für die öffentliche Verwaltung*. Altenholz: Dataport. https://dataport.de.

[25] ZenDiS GmbH (2024). *Zentrum für Digitale Souveränität — Jahresbericht 2023*. Berlin: ZenDiS. https://zendis.de.

[26] BSI (2023). *IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://bsi.bund.de. Licence: CC-BY-ND 3.0 DE.

[27] European Parliament and Council (2022). *Directive (EU) 2022/2555 — NIS2 Directive*, OJ L 333/80, 27 December 2022. https://eur-lex.europa.eu. Licence: EU legislation (public domain).

[28] European Commission / Joinup (2023). *OSOR Annual Review 2023*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor. Licence: CC-BY-4.0.

[29] UN DESA (2022). *UN E-Government Survey 2022*. New York: United Nations. https://publicadministration.un.org. Licence: UN open access.

[30] Janowski, T. (2015). Digital government evolution. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001.

[31] GovStack Initiative / ITU & DIAL (2023). *GovStack Building Blocks Specification v1.0*. Geneva: ITU. https://govstack.global. Licence: CC-BY-SA-4.0.

[32] Bundesverwaltungsamt / BMI (2023). *Föderales Informationsmanagement (FIM)*. Cologne: BVA. https://bva.bund.de. Licence: DL-DE/Zero 2.0.

[33] Camunda Services GmbH (2023). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com. Licence: Apache 2.0.

[34] BigBlueButton Inc. (2023). *Open Source Web Conferencing*. Ottawa: BigBlueButton. https://bigbluebutton.org. Licence: LGPL-3.0.

[35] Jitsi Community (2023). *Jitsi Meet*. San Francisco: 8x8 / Jitsi Community. https://jitsi.org. Licence: Apache 2.0.

[36] OpenStreetMap Foundation (2023). *OpenStreetMap*. London: OSMF. https://openstreetmap.org. Licence: ODbL-1.0.

[37] QGIS Project (2023). *QGIS: A Free and Open Source Geographic Information System*. https://qgis.org. Licence: GPL-2.0+.

[38] Bundesamt für Justiz / Eidgenössische Kanzlei (2023). *Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (BGEID)*, SR 161.5. Bern: Swiss Confederation. https://fedlex.admin.ch. Licence: CC0.

[39] Cloud Native Computing Foundation (CNCF) (2023). *Kubernetes*. San Francisco: Linux Foundation. https://kubernetes.io. Licence: Apache 2.0.

[40] Consul Project / Ayuntamiento de Madrid (2023). *CONSUL Democracy*. Madrid: Ayuntamiento de Madrid. https://consulproject.org. Licence: AGPL-3.0.

[41] PostgreSQL Global Development Group (2023). *PostgreSQL*. https://postgresql.org. Licence: PostgreSQL Licence.

[42] ZenDiS GmbH / BMI (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. Berlin: ZenDiS. https://opendesk.eu. Licence: AGPL-3.0.

[43] Schweizerisches Bundesarchiv (BAR) (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://bar.admin.ch/bar/de/home/digitale-archivierung/gever.html. Licence: open access.

[44] opendata.swiss (2023). *Open Government Data Switzerland*. Bern: Swiss Federal Archives / BFS. https://opendata.swiss. Licence: CC-BY-4.0 (portal).

[45] European Commission, ISA² Programme (2017). *European Interoperability Framework (EIF)*. Brussels: European Commission. https://joinup.ec.europa.eu. Licence: CC-BY-4.0.

[46] KoSIT (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://xoev.de.

[47] Lucke, J. & Reinermann, H. (2000). *Speyerer Definition von Electronic Government*. Speyer: Forschungsinstitut für öffentliche Verwaltung. https://foev.dhv-speyer.de. Licence: open access.

[48] Bertot, J.C., Jaeger, P.T. & Grimes, J.M. (2010). Using ICTs to create a culture of transparency. *Government Information Quarterly*, 27(3), 264–271. https://doi.org/10.1016/j.giq.2010.04.003.

[49] OECD (2020). *The OECD Digital Government Policy Framework*. OECD Public Governance Policy Papers No. 02. Paris: OECD. https://doi.org/10.1787/f64fed2a-en.

[50] Bundesregierung Deutschland (2022). *Digitalstrategie Deutschland*. Berlin: Bundesregierung. https://digitalstrategie-deutschland.de. Licence: DL-DE/Zero 2.0.

[51] European Commission (2021). *2030 Digital Compass*, COM(2021) 118 final. Brussels: European Commission. Licence: CC-BY.

[52] BSI (2022). *Mindeststandard des BSI zur Nutzung externer Cloud-Dienste*, Version 1.1. Bonn: BSI. https://bsi.bund.de. Licence: CC-BY-ND 3.0 DE.

[53] Joinup / European Commission (2023). *Open Source Observatory and Repository (OSOR)*. Brussels: European Commission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor. Licence: CC-BY-4.0.

[54] Dunleavy, P., Margetts, H., Bastow, S. & Tinkler, J. (2006). *Digital Era Governance*. Oxford: Oxford University Press. ISBN 978-0-19-929414-8.

[55] Scholl, H.J. (2017). Electronic government: A study domain past its zenith? *Information Polity*, 22(4), 313–329. https://doi.org/10.3233/IP-170417.

## Anhang A — Beschaffungs-Checkliste (23 Fragen)

Füllen Sie diese Checkliste aus, bevor Sie eine Ausschreibung für digitale Komponenten veröffentlichen, die von dieser Strategie abgedeckt werden. Mit „Nein“ oder „Teilweise“ beantwortete Fragen erfordern eine dokumentierte Begründung.

| # | Frage | Ja | Teilweise | Nein |
|---|---|---|---|---|
| 1 | Ist die Komponente unter einer OSI-anerkannten Open-Source-Lizenz lizenziert? | | | |
| 2 | Ist der Quellcode öffentlich in einem versionskontrollierten Repository verfügbar? | | | |
| 3 | Wurde die Komponente von einer unabhängigen Stelle auf GDPR/DSGVO-Konformität geprüft? | | | |
| 4 | Erfüllt die Komponente WCAG 2.1 Level AA (oder verlangt die Ausschreibung dies)? | | | |
| 5 | Unterstützt die Komponente OIDC 1.0 oder SAML 2.0 für die Integration mit Keycloak? | | | |
| 6 | Ist die Komponente auf Kubernetes/SCS ohne anbieterspezifische Cloud-Abhängigkeiten bereitstellbar? | | | |
| 7 | Enthält der Vertrag einen bedingungslosen Datenexport in einem offenen Format innerhalb von 30 Tagen nach Beendigung? | | | |
| 8 | Verbietet der Vertrag die Nutzung kommunaler Daten zum Training von KI-Modellen oder für Sekundärzwecke? | | | |
| 9 | Spezifiziert die Ausschreibung funktionale Anforderungen (keine Produktnamen) und gewährleistet so offenen Wettbewerb? | | | |
| 10 | Hat das Bewertungskriterium mehrjährige TCO (Lizenz + Implementierung + Betrieb + Ausstieg) einbezogen? | | | |
| 11 | Sind verpflichtende offene Standards spezifiziert (XÖV/DE, eCH/CH, DCAT-AP, BPMN 2.0, OGC)? | | | |
| 12 | Wurde eine Interoperabilitätsbewertung gemäß dem Interoperable Europe Act [6] durchgeführt? | | | |
| 13 | Enthält der Vertrag eine Quellcode-Hinterlegung oder OSS-Veröffentlichungspflicht für maßgeschneiderte Entwicklung? | | | |
| 14 | Ist die Upstream-OSS-Community aktiv (Commits innerhalb von 12 Monaten; reaktionsschneller Issue-Tracker)? | | | |
| 15 | Gibt es dokumentierte Produktiv-Deployments im öffentlichen Sektor in vergleichbarem Maßstab? | | | |
| 16 | Verfügt die Komponente über eine veröffentlichte Sicherheitsrichtlinie und einen CVE-Reaktionsprozess mit SLA? | | | |
| 17 | Ist die Komponente mit BSI IT-Grundschutz [26] oder den ISDS-(CH-)Härtungsrichtlinien kompatibel? | | | |
| 18 | Hat der Lieferant die Fähigkeit nachgewiesen, Support in der/den erforderlichen kommunalen Sprache(n) zu leisten? | | | |
| 19 | Ist genossenschaftliche oder Rahmenbeschaffung (govdigital, Dataport, kantonale Stelle) verfügbar und genutzt? | | | |
| 20 | Hat der DSB die DSFA für diese Komponente geprüft? | | | |
| 21 | Unterstützt die Komponente den NIS2-[27]-Vorfallmeldungs-Workflow (Logging, Alerting, 24 h)? | | | |
| 22 | Wurde die kommunale Datenschutzaufsichtsbehörde, wo erforderlich, benachrichtigt? | | | |
| 23 | Ist ein Übergangsplan für die Migration weg von dieser Komponente bei Einstellung dokumentiert? | | | |

## Anhang B — Methodik der Technologiebewertung

### Sieben Kriterien und Gewichtungen

| Kriterium | Gewichtung | Bewertungen 1–5 (kurze Beschreibung) |
|---|---|---|
| C1 Lizenzoffenheit | 20 % | 1=proprietär; 3=OSI-Copyleft; 5=OSI-permissiv oder bestätigt gov-kompatibles Copyleft |
| C2 Deployment-Reife | 15 % | 1=Alpha; 3=stabil, begrenzte Upgrade-Dokumentation; 5=LTS, Zero-Downtime-Upgrades dokumentiert |
| C3 Community-Gesundheit | 15 % | 1=Einzelanbieter, stagnierend; 3=Multi-Contributor, monatliche Releases; 5=stiftungsgeführt, wöchentliche Aktivität |
| C4 Interoperabilität | 15 % | 1=nur proprietäre APIs; 3=1–2 verpflichtende Standards; 5=alle anwendbaren Standards nativ unterstützt |
| C5 Sicherheit | 15 % | 1=keine Sicherheitsrichtlinie; 3=Patches innerhalb von 30 d; 5=dediziertes Sicherheitsteam, Patches innerhalb von 7 d bei kritischen |
| C6 TCO | 10 % | 1=hohe Lizenz + Lock-in; 3=null Lizenz, moderate Implementierung; 5=null Lizenz, geringe Implementierung, Commodity-Betrieb |
| C7 Einsatz im öffentlichen Sektor | 10 % | 1=keine; 3=1–5 dokumentiert; 5=>20 dokumentiert, OSOR-Fallstudie verfügbar |

**Gewichteter Gesamtscore** = (C1×0,20) + (C2×0,15) + (C3×0,15) + (C4×0,15) + (C5×0,15) + (C6×0,10) + (C7×0,10)

Komponenten, die bei einem einzelnen Kriterium unter 3,0 oder im Gesamtscore unter 3,5 liegen, werden ohne dokumentierte mildernde Faktoren nicht empfohlen.

### Referenzwerte

| Komponente | C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Score** |
|---|---|---|---|---|---|---|---|---|
| Keycloak [21] | 5 | 5 | 4 | 5 | 4 | 5 | 5 | **4.70** |
| Nextcloud [13] | 3 | 5 | 4 | 4 | 4 | 5 | 5 | **4.20** |
| OpenProject [20] | 3 | 4 | 3 | 4 | 3 | 5 | 4 | **3.65** |
| Camunda CE [33] | 5 | 4 | 3 | 5 | 4 | 5 | 4 | **4.20** |
| Decidim [12] | 3 | 4 | 4 | 4 | 3 | 5 | 5 | **3.90** |
| Matrix/Synapse [14] | 5 | 4 | 4 | 5 | 4 | 5 | 4 | **4.35** |
| BigBlueButton [34] | 4 | 4 | 3 | 4 | 3 | 5 | 5 | **3.90** |
| CKAN [22] | 3 | 5 | 4 | 5 | 4 | 5 | 5 | **4.25** |
| QGIS [37] | 5 | 5 | 5 | 5 | 4 | 5 | 5 | **4.85** |
| TYPO3 [19] | 3 | 5 | 4 | 4 | 4 | 5 | 5 | **4.20** |
| SCS [3] | 5 | 4 | 4 | 5 | 5 | 4 | 3 | **4.40** |

## Anhang C — Selbstbewertung zur kommunalen digitalen Souveränität

Dieses Instrument bietet eine strukturierte Selbstbewertung für Kommunen, die ihre aktuelle Haltung zur digitalen Souveränität bewerten. In Phase 0 ausfüllen und ab Phase 5 jährlich wiederholen. Gemeinsam ausgefüllt von CIO, Rechts-/Compliance-Beauftragtem und einem Mitglied der kommunalen Führung.

**Bewertung:** Ja = 2 Pkt., Teilweise = 1 Pkt., Nein = 0 Pkt. Maximum: 30 Punkte.

**Interpretation:** 25–30: Starke Souveränität; 18–24: In Entwicklung; 10–17: Aufkommend — Übergangsprogramm empfohlen; 0–9: Kritische Abhängigkeit — sofortiges Handeln erforderlich.

| # | Frage | Ja (2) | Teilweise (1) | Nein (0) |
|---|---|---|---|---|
| 1 | Verfügt die Kommune über eine dokumentierte, vom Gemeinderat genehmigte Richtlinie zur digitalen Souveränität? | | | |
| 2 | Pflegt die Kommune ein vollständiges Software-Asset-Inventar einschließlich SaaS-Abonnements und Cloud-Verträgen? | | | |
| 3 | Kann die Kommune ihre Primärdaten innerhalb von 90 Tagen ohne prohibitive Kosten aus jedem Einzelanbieter migrieren? | | | |
| 4 | Verwendet die Kommune offene, standardisierte Datenformate (XÖV/eCH, DCAT-AP, OGC, OIDC) für alle primären Datenaustausche? | | | |
| 5 | Wird die primäre Infrastruktur der Kommune innerhalb der EU-/EWR-Jurisdiktion gehostet, die dem EU-Datenschutzrecht unterliegt? | | | |
| 6 | Erfüllt das kommunale Portal WCAG 2.1 Level AA mit einer veröffentlichten Barrierefreiheitserklärung? | | | |
| 7 | Verfügt die Kommune über einen DSB und aktuelle DSFA für alle wichtigen digitalen Dienste? | | | |
| 8 | Hat die Kommune BSI-IT-Grundschutz-(DE-) oder ISDS-(CH-)Basiskontrollen implementiert? | | | |
| 9 | Ist die Kommune NIS2-konform oder bereitet sich aktiv darauf vor? | | | |
| 10 | Verwendet die Kommune mindestens eine Open-Source-Komponente in ihrem aktuellen operativen Stack? | | | |
| 11 | Nimmt die Kommune an mindestens einer kooperativen IT-Struktur teil? | | | |
| 12 | Veröffentlicht die Kommune mindestens fünf offene Verwaltungsdatensätze auf einem DCAT-AP-konformen Portal? | | | |
| 13 | Bietet die Kommune mindestens fünf Bürgerprozesse vollständig online an (durchgängig digital)? | | | |
| 14 | Verfügt die Kommune über eine schriftliche Richtlinie, die externe KI-APIs für die Verarbeitung personenbezogener Bürgerdaten verbietet? | | | |
| 15 | Hat die Kommune in den letzten 12 Monaten mindestens einen Beitrag zu einem Upstream-Open-Source-Projekt geleistet? | | | |

**Gesamtscore:** _____ / 30 | **Datum:** _______________ | **Ausgefüllt von:** _______________

**Identifizierte prioritäre Lücken (Bewertung 0):** ______________________________

**Nächste geplante Überprüfung:** _______________

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Licence (CC-BY-4.0) veröffentlicht.*
*Zitieren als: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*
