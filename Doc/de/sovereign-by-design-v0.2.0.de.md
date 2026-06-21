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

---

## Zusammenfassung

Kommunalverwaltungen in ganz Europa stehen vor einer beispiellosen Konvergenz von Anforderungen: beschleunigten Verpflichtungen aus nationalen Digitalisierungsmandaten wie dem deutschen Onlinezugangsgesetz 2.0 [2] und dem schweizerischen Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG) [1]; steigenden Anforderungen an die Cybersicherheit im Rahmen der NIS2-Richtlinie [27]; wachsenden Erwartungen der Bürgerinnen und Bürger an zugängliche und reaktionsfähige öffentliche Dienstleistungen; sowie einer strukturellen Abhängigkeit von einer kleinen Zahl proprietärer Softwareanbieter, deren Lizenzkosten einen wachsenden Anteil der knappen öffentlichen Haushalte beanspruchen. Das Konzept der digitalen Souveränität — die Fähigkeit öffentlicher Einrichtungen, ihre eigene digitale Infrastruktur zu kontrollieren, zu prüfen, anzupassen und nachhaltig zu betreiben — hat sich von einer akademischen Abstraktion zu einem operativen politischen Imperativ entwickelt.

Dieses Papier präsentiert eine umfassende, evidenzbasierte Open-Source-Technologiestrategie für Kommunalverwaltungen mit Einwohnerzahlen zwischen 50.000 und 200.000, mit primärem Bezug auf den deutschen und schweizerischen Rechtsrahmen und sekundärer Anwendbarkeit in der gesamten Europäischen Union. Gestützt auf eine systematische Literaturrecherche von 55 begutachteten und grauen Literaturquellen, eine vergleichende Analyse kommunaler Implementierungen in Barcelona, München, Schleswig-Holstein und Schweizer Kantonen sowie eine strukturierte Bewertung von elf Technologiebereichen argumentiert das Papier, dass ein kohärenter Open-Source-Stack — aufgebaut auf identifizierbaren, ausgereiften, von der Community unterstützten Komponenten — die funktionalen Anforderungen proprietärer Alternativen erfüllen oder übertreffen kann, während er messbare Reduzierungen der langfristigen Gesamtbetriebskosten erzielt, Abhängigkeiten von einzelnen Anbietern beseitigt und digitale öffentliche Güter schafft, die dem breiteren zivilgesellschaftlichen Gemeinwohl zugutekommen.

Die Strategie ist um einen phasenweisen Implementierungsfahrplan gegliedert, der sechs Phasen von der organisatorischen Bereitschaft bis zur operativen Exzellenz umfasst, mit indikativen Kostenbereichen, die auf eine mittelgroße Gemeinde kalibriert sind. Ein Stakeholder- und Beschaffungsrahmen befasst sich mit der politischen Ökonomie des Technologiewechsels, einschließlich Änderungsmanagement, Rechtssicherheit und interkommunaler Kooperationsstrukturen. Ein Risikoregister und eine regulatorische Risikoanalyse identifizieren die wichtigsten Versagensmuster, wobei Münchens LiMux-Wechsel als exemplarisches Warnbeispiel dient. Drei Anhänge stellen Arbeitsmittel bereit: eine Beschaffungscheckliste mit 23 Fragen, eine Technologiebewertungs-Bewertungsmatrix mit sieben Kriterien und ein Selbstbewertungsinstrument für kommunale digitale Souveränität mit 15 Fragen.

Das Papier kommt zu dem Schluss, dass digitale Souveränität kein utopisches Streben, sondern ein erreichbares technisches und verwaltungspolitisches Ergebnis ist, sofern Kommunen die Umstellung mit angemessener Vorbereitung, realistischen Kostenerwartungen und nachhaltigem politischem Engagement angehen. Öffentliches Geld sollte öffentlichen Code hervorbringen [4].

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale digitale Transformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Civic Technology

---

## 1. Einleitung

Die digitale Transformation der öffentlichen Verwaltung ist keine optionale Aufgabe mehr. Bürgerinnen und Bürger in demokratischen Gesellschaften erwarten zunehmend, dass Verwaltungsleistungen über digitale Kanäle verfügbar, zugänglich und vertrauenswürdig sind. Gleichzeitig wurden die institutionellen Strukturen, über die Kommunen diese Leistungen erbringen — veraltete Enterprise-Software-Stacks, proprietäre Cloud-Abhängigkeiten, bilaterale Anbieterverträge — weitgehend für eine andere Ära und ein anderes Bedrohungsumfeld konzipiert.

Der EU-Digitalkompas 2030 [51] setzt das explizite Ziel, dass alle wichtigen öffentlichen Dienstleistungen bis 2030 online verfügbar sein sollen und 100 Prozent der Bürgerinnen und Bürger Zugang zu elektronischen Ausweisdokumenten haben sollen. Der Interoperable Europe Act [6] verpflichtet Stellen des öffentlichen Sektors, die Interoperabilität digitaler Komponenten vor der Beschaffung zu bewerten. Das OZG 2.0 [2] Deutschlands schreibt eine föderierte Online-Leistungserbringung auf Bundes-, Landes- und kommunaler Ebene vor. Das schweizerische EMBAG [1] verlangt, dass mit Bundesmitteln entwickelte Software als Open Source veröffentlicht wird, sofern keine spezifischen Ausnahmen gelten. Diese gesetzgeberischen Signale sind richtungsweisend konsistent: Die europäische öffentliche Verwaltung bewegt sich — zögerlich, aber unverkennbar — auf eine offene, interoperable und rechenschaftspflichtige digitale Infrastruktur zu.

### 1.1 Der europäische Moment für digitale Souveränität

Der Begriff „digitale Souveränität" hielt nach einer Reihe von Störungen, die die Fragilität der europäischen Technologieabhängigkeiten im öffentlichen Sektor offenlegten, Einzug in den politischen Mainstream: der SolarWinds-Lieferkettenangriff 2020, wiederholte Ausfälle US-amerikanischer Cloud-Anbieter sowie rechtliche Unsicherheiten infolge der Ungültigkeitserklärung des Privacy Shield und des anschließenden Schrems-II-Urteils zu transatlantischen Datenübermittlungen. Die Open-Source-Strategie 2020–2023 der Europäischen Kommission [5] identifizierte Open-Source-Software ausdrücklich als strategischen Enabler digitaler Souveränität. Das Open Source Observatory (OSOR) [28, 53] hat Hunderte reproduzierbarer Open-Source-Implementierungen der Verwaltung in den Mitgliedstaaten katalogisiert.

Für Kommunen ist die Souveränitätsfrage besonders akut. Eine mittelgroße deutsche Stadt mit 80.000 Einwohnern kann jährlich 2 bis 5 Millionen Euro für Softwarelizenzen, Wartungsverträge und Cloud-Abonnements bei einer Handvoll Anbietern ausgeben. Die Verhandlungsmacht dieser Gemeinde in jeder einzelnen Verhandlung ist vernachlässigbar. Kollektives Handeln — durch gemeinsame Plattformen, kooperative Beschaffung und interkommunale Entwicklungskonsortien — ist die strukturelle Alternative. Institutionen wie govdigital eG [23], Dataport AöR [24] und ZenDiS GmbH [25] repräsentieren aufkommende deutsche Modelle genau dieser Art.

### 1.2 Anwendungsbereich und Begriffsbestimmungen

Im Sinne dieses Papiers bezeichnet:

**Kommunalverwaltung** die Exekutiv- und Verwaltungsfunktionen einer Stadt oder Gemeinde (Gemeinde / Gemeinderat) mit einer Einwohnerzahl zwischen etwa 50.000 und 200.000, vorrangig in Deutschland und der Schweiz, mit Verallgemeinerung auf vergleichbare EU-Rechtssysteme.

**Digitale Souveränität** ist definiert als die Fähigkeit einer öffentlichen Einrichtung, ihre eigene digitale Infrastruktur zu gestalten: die Softwarekomponenten, die ihre Verwaltungsfunktionen unterstützen, auszuwählen, einzusetzen, zu prüfen, zu modifizieren und gegebenenfalls zu ersetzen, ohne strukturelle Abhängigkeit von einem einzelnen privaten Anbieter. Diese Definition synthetisiert akademische Behandlungen von Janowski [30], dem OECD Digital Government Policy Framework [49] und dem operativen Rahmen der GovStack Initiative [31].

**Open-Source-Software (OSS)** bezeichnet Software, die unter einer von der Open Source Initiative anerkannten Lizenz steht und deren Quellcode zur Einsichtnahme, Modifikation und Weiterverbreitung zugänglich ist. Das Papier folgt der Taxonomie des European Interoperability Framework (EIF) [45] und unterscheidet zwischen Softwarefreiheit (Lizenz) und operativer Autonomie (Einsatz und Hosting).

**Technologie-Stack** bezeichnet das geschichtete Ensemble von Softwarekomponenten — von der Infrastruktur über Middleware bis hin zu bürgerorientierten Anwendungen —, die gemeinsam die digitale Betriebsumgebung einer Gemeinde bilden.

### 1.3 Forschungsfragen

Dieses Papier befasst sich mit vier primären Forschungsfragen:

**FF1:** Welche Open-Source-Technologiekomponenten sind im Planungshorizont 2024–2028 ausreichend ausgereift, gut verwaltet und öffentlich eingesetzt, um einen glaubwürdigen kommunalen digitalen Stack zu bilden?

**FF2:** Wie sehen die vergleichenden Gesamtbetriebskosten von Open-Source- gegenüber proprietären Alternativen auf kommunaler Ebene aus, unter Berücksichtigung von Lizenz-, Implementierungs-, Betriebs- und Transitionskosten?

**FF3:** Welche Governance-, Beschaffungs- und Änderungsmanagementstrukturen maximieren die Wahrscheinlichkeit einer erfolgreichen Open-Source-Umstellung für eine mittelgroße Gemeinde?

**FF4:** Welche regulatorischen Anforderungen — auf EU-, nationaler und kantonaler/Länderebene — muss eine kommunale Open-Source-Strategie erfüllen, und wie unterstützen oder erschweren Open-Source-Komponenten die Compliance?

---

## 2. Methodik

### 2.1 Systematische Literaturrecherche

Die Literaturrecherche wurde nach einem angepassten PRISMA-Rahmen durchgeführt. Suchanfragen zu den Begriffen „open source government", „digital sovereignty municipality", „e-government open source", „OZG open source", „EMBAG open source", „municipal cloud" und Kombinationen davon wurden in Google Scholar, BASE (Bielefelder Akademische Suchmaschine) und dem Joinup/OSOR-Repository [28, 53] ausgeführt. Veröffentlichungsdaten wurden auf 2000–2026 beschränkt, mit Bevorzugung von Material nach 2015, ausgenommen grundlegende theoretische Werke. Die Referenzliste mit 55 Quellen wurde aus einem ursprünglichen Abruf von rund 280 Kandidatentiteln kuratiert.

### 2.2 Vergleichende Politikanalyse

Politikdokumente aus Deutschland (OZG 2.0 [2], Digitalstrategie Deutschland [50], FIM [32], FITKO Jahresbericht [9], ZenDiS [25, 42]), der Schweiz (EMBAG [1], E-Government Strategie Schweiz 2024–2027 [16], BGEID [38], eCH-Standards [17], GEVER [43], opendata.swiss [44]) und der Europäischen Union (Interoperable Europe Act [6], EU Open Source Strategy [5], EIF [45], NIS2 [27], Digitalkompas 2030 [51]) wurden systematisch ausgewertet, um verbindliche Anforderungen, empfohlene Architekturen und Anreizstrukturen für die kommunale OSS-Einführung zu identifizieren.

### 2.3 Technologiebewertungsrahmen

Jeder Technologiebereich wurde anhand einer sieben Kriterien umfassenden Bewertungsmatrix bewertet (detailliert in Anhang B): Lizenzoffenheit, Einsatzreife, Community-Gesundheit, Interoperabilität, Sicherheit, Gesamtbetriebskosten und Einsätze im öffentlichen Sektor. Die Bewertungen wurden aus Anbieter- und Community-Dokumentation, OSOR-Fallstudien, BSI IT-Grundschutz-Kompatibilitätsbewertungen [26] und begutachteten Evaluierungen, soweit verfügbar, entnommen.

### 2.4 Stakeholderanalyse

Stakeholder-Kategorien wurden anhand des GovStack-Building-Blocks-Rahmens [31], des Wirtz-Weyerer E-Government-Reifegradmodells [7] und einer Analyse der deutschen Digitallotsen und der Schweizer E-Government Schweiz-Implementierungsstrukturen [16] identifiziert. Stakeholder-Interessen, Einflussniveaus und Einbindungsstrategien wurden mittels einer angepassten Macht-Interesse-Matrix abgebildet.

### 2.5 Einschluss-/Ausschlusskriterien

**Eingeschlossen:** Softwarekomponenten mit einer OSI-anerkannten Lizenz; aktive Upstream-Community (Commit-Aktivität innerhalb von 12 Monaten); dokumentierte Produktiveinsätze in der öffentlichen Verwaltung; Kompatibilität mit EU/DE/CH-Regulierungsanforderungen; ausreichende Dokumentation für einen unabhängigen Betrieb.

**Ausgeschlossen:** Komponenten unter einer Single-Vendor-Source-Available-Lizenz ohne OSI-Anerkennung; Komponenten ohne öffentliche Referenzimplementierungen; Komponenten mit zum Zeitpunkt der Erstellung ungelösten Sicherheitshinweisen mit CVSS ≥9,0.

### 2.6 Einschränkungen

Dieses Papier ist ein strategisches Politikdokument, keine kontrollierte empirische Studie. Kostenzahlen sind indikative Bereiche, die aus veröffentlichten Fallstudien und Beschaffungsdaten abgeleitet wurden, nicht aus primärer Feldforschung. Technologiebewertungen spiegeln den Stand der Upstream-Projekte Mitte 2026 wider und müssen regelmäßig überprüft werden. Der primäre Regulierungsrahmen des Papiers ist deutsch und schweizerisch; Gemeinden in anderen EU-Mitgliedstaaten sollten die Anwendbarkeit spezifischer Gesetzesverweise prüfen. Der Münchner LiMux-Fall wird als warnende Illustration behandelt, nicht als Falsifizierung der allgemeinen Open-Source-These.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen

Die akademische Erforschung des Electronic Government hat sich durch mehrere distinkte Phasen entwickelt. Lucke und Reinemanns Speyerer Definition [47] etablierte das grundlegende Vokabular für die deutschsprachige E-Government-Forschung: die Bereitstellung von Regierungsinformationen und -leistungen über elektronische Netze, strukturiert entlang der Achsen Government-to-Citizen (G2C), Government-to-Business (G2B) und Government-to-Government (G2G). Dunleavys Digital Era Governance [54] lieferte eine strukturelle Kritik an den IT-Outsourcing-Pathologien des New Public Management — Fragmentierung, Agentifizierung und Abhängigkeit von einzelnen Anbietern — und antizipierte viele der Souveränitätsbedenken, die die aktuelle Politik bewegen.

Janowski [30] formulierte ein vierstufiges Evolutionsmodell für digitale Verwaltung — Digitalisierung, Transformation, Einbindung und Kontextualisierung — das einen Entwicklungsrahmen für die Bewertung der kommunalen Bereitschaft liefert. Der OECD Digital Government Policy Framework [49] operationalisierte digitale Verwaltung als mehrdimensionales Konstrukt, das die Dimensionen Digital by Design, datengesteuerter öffentlicher Sektor, Verwaltung als Plattform, Open by Default, nutzerorientiert und proaktiv umfasst. Scholl [55] lieferte einen reflektierenden Überblick über die intellektuelle Entwicklung des Fachgebiets. Bertot, Jaeger und Grimes [48] stellten die empirische Verbindung zwischen IKT-Einsatz und Transparenzergebnissen her — eine zentrale Begründung für die Open-Data-Komponenten des in Abschnitt 4 beschriebenen Stacks.

### 3.2 Digitale Souveränität

Digitale Souveränität als politisches Konzept entbehrt einer einzigen kanonischen Definition. Dieses Papier übernimmt eine Zusammensetzungsdefinition, die das „Public Money? Public Code!"-Manifest der FSFE [4], die Open-Source-Strategie der Europäischen Kommission [5] und den GovStack-Building-Blocks-Rahmen [31] synthetisiert. Im Kern erfordert Souveränität: Prüfbarkeit (die Fähigkeit, Code einzusehen), Modifizierbarkeit (die Fähigkeit, Code an lokale Anforderungen anzupassen), Portabilität (die Fähigkeit, ohne prohibitive Wechselkosten von einem Anbieter oder Hosting-Anbieter zu migrieren) und Rechenschaftspflicht (klare Governance darüber, wer die Software und ihre Daten kontrolliert).

Der Interoperable Europe Act [6] operationalisiert eine Dimension der Souveränität durch eine obligatorische Interoperabilitätsbewertung, die von Stellen des öffentlichen Sektors verlangt, Interoperabilitätsbewertungen vor dem Einsatz neuer IKT-Lösungen durchzuführen und zu veröffentlichen. Das Prinzip „Public Money? Public Code!" [4] wurde von einer wachsenden Zahl europäischer kommunaler und regionaler Regierungen formell übernommen. Lathrop und Ruma [15] liefern die normative Grundlage, die offene Verwaltung — gekennzeichnet durch Transparenz, Zusammenarbeit und Partizipation — mit Open-Source-Infrastruktur als notwendige (wenn auch nicht hinreichende) Bedingung verknüpft.

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 erlassen und 2024 als OZG 2.0 [2] wesentlich überarbeitet, ist das gesetzliche Rückgrat der deutschen kommunalen Digitalisierung. OZG 2.0 führt das Prinzip „Once Only" ein — Bürgerinnen und Bürger sollen dieselben Daten nicht mehrfach bei verschiedenen Behörden einreichen müssen — und richtet einen Bundesmarktplatz für digitalisierte Verwaltungsleistungen ein, den Gemeinden nutzen können. FITKO (Föderale IT-Kooperation) koordiniert die technische Umsetzung über die Länder [9]. Das Programm Föderales Informationsmanagement (FIM) [32] stellt die semantischen Standards (FIM-Prozesse, FIM-Leistungen, FIM-Daten) bereit, die für die länderübergreifende Wiederverwendung von Leistungen erforderlich sind.

Die Plattform openCode.de [10], betrieben von der Digitalservice GmbH des Bundes, stellt ein öffentliches Code-Repository für OSS-Komponenten von Bund und Ländern bereit, die Gemeinden wiederverwenden können. govdigital eG [23] und Dataport AöR [24] bieten kooperative Hosting- und Managed-Service-Modelle an, die die Betriebslast für einzelne Gemeinden reduzieren. ZenDiS GmbH [25] — das Zentrum für Digitale Souveränität — koordiniert die OpenDesk-Bundesarbeitsplatzsuite [42] und berät öffentliche Stellen bei der souveränitätskompatiblen Beschaffung. Die AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) [18] betreut bayerische Gemeinden mit gemeinsamen IT-Diensten und hat begonnen, Open-Source-Komponenten in ihren Leistungskatalog zu integrieren. Die XÖV-Standards [46], entwickelt von KoSIT, stellen XML-basierte Datenaustauschformate für die verwaltungsübergreifende Kommunikation bereit und bilden die technische Interoperabilität, die OZG 2.0 erfordert.

### 3.4 Digitale Dienste der Schweizer Kantone und des Bundes

Die digitale Verwaltungslandschaft der Schweiz wird durch ihre föderale Struktur geprägt: der Bund, 26 Kantone und rund 2.200 Gemeinden üben jeweils erhebliche Verwaltungsautonomie aus. Das EMBAG [1] — Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben, in Kraft seit 1. Januar 2024 — ist eine wegweisende Bestimmung: Artikel 9 verlangt, dass Software, die von oder für Bundesbehörden entwickelt wurde, als Open Source veröffentlicht wird, sofern keine Ausnahmen aus Sicherheitsgründen, Rechten Dritter oder unverhältnismäßigem Aufwand gelten. Dieses Mandat „Open Source by Default" stellt eine der fortschrittlichsten OSS-Anforderungen in der europäischen öffentlichen Verwaltung dar.

Die E-Government Strategie Schweiz 2024–2027 [16] identifiziert Interoperabilität, digitale Identität und Datenwiederverwertung als die drei strategischen Säulen. Der Normungsverein eCH [17] veröffentlicht technische Standards für den E-Government-Datenaustausch, die den deutschen XÖV-Standards entsprechen, aber die schweizerischen Verfassungsbesonderheiten einschließlich der viersprachigen Verwaltung widerspiegeln. Das Bundesgesetz über den elektronischen Identitätsnachweis (BGEID) [38] schafft die rechtliche Grundlage für den schweizerischen elektronischen Identitätsnachweis (E-ID), der auf einem dezentralen, datenschutzwahrenden Wallet-Modell basiert. Der GEVER-Rahmen des Schweizerischen Bundesarchivs [43] regelt die elektronische Aktenführung in Bundesbehörden. opendata.swiss [44] ist das schweizerische nationale Open-Data-Portal und stellt einen föderativen Katalog maschinenlesbarer Regierungsdatensätze unter standardisierten Lizenzen bereit.

### 3.5 Open-Source-Communities und souveräne Technologie

Das Open-Source-Ökosystem für die öffentliche Verwaltung ist seit der ersten Welle staatlicher Linux-Implementierungen in den frühen 2000er Jahren erheblich gereift. Das OSOR [28, 53] katalogisiert über 700 OSS-Einsätze im öffentlichen Sektor in EU-Mitgliedstaaten. Die FSFE [4] setzt sich weiterhin für Open-Source-Beschaffungsmandate ein und hat formelle Unterstützung von mehreren europäischen Städten und Regionen erhalten. GovStack [31] stellt eine Building-Blocks-Spezifikation bereit, die generische Servicekomponenten der Verwaltung auf Open-Source-Referenzimplementierungen abbildet und die Wiederverwendung über Rechtssysteme hinweg erleichtert.

Community-Governance ist ein wesentlicher Risikofaktor. Der GovStack-Rahmen [31] unterscheidet zwischen stiftungsverwalteten Projekten (z. B. Nextcloud unter dem dualen Modell Nextcloud GmbH + Community [13]), konsortiumsverwalteten Projekten (z. B. Sovereign Cloud Stack unter OSBA-Governance [3, 11]) und von Kommunen verwalteten Forks (mit höchstem Wartungsrisiko). Für souveränen Einsatz empfiehlt dieses Papier, stiftungs- und konsortiumsverwalteten Projekten mit nachgewiesener Akzeptanz im öffentlichen Sektor den Vorzug zu geben.

### 3.6 Gesamtbetriebskosten und wirtschaftliche Evidenz

Die Wirtschaftlichkeit kommunaler Software wird häufig sowohl in pro-proprietärer als auch in pro-Open-Source-Interessenvertretung falsch dargestellt. Eine ausgewogene TCO-Analyse muss umfassen: Lizenzgebühren, Implementierungs- und Integrationskosten, operativen Personalaufwand, Schulung, Supportverträge, Migrationskosten und die Opportunitätskosten der Lieferantenabhängigkeit.

**Proprietary Benchmark-Kosten.** Microsoft 365 Government-Lizenzierung (G3/G5-Tier) kostet typischerweise 150–400 Euro pro Nutzer und Jahr für zentrale Produktivitäts- und Kollaborationssuiten, ohne zusätzliche Module, Compliance-Add-ons, Azure-Hosting und Implementierungsdienstleistungen. Für eine Gemeinde mit 800 Mitarbeitern beläuft sich das jährliche Lizenzrisiko damit auf 120.000 bis 320.000 Euro allein für Produktivitätssoftware, vor Infrastruktur und Fachanwendungen.

**Open-Source-TCO-Evidenz.** Barcelonas digitales Transformationsprogramm (2016–2019), verankert in der Decidim-Plattform für partizipatorische Demokratie [12] und einer expliziten Richtlinie für ethische digitale Standards, soll der Stadt über vier Jahre 30 bis 40 Millionen Euro durch reduzierte proprietäre Lizenzierung und insgesellte Entwicklung eingespart haben. Schleswig-Holstein kündigte 2021 eine strukturierte Migration von 25.000 Landesarbeitsplätzen auf LibreOffice und Linux an, wobei die Landesregierung Lizenzkostenreduzierungen als primären Treiber nannte. Das OpenDesk-Projekt [42] baut die Bundesevidenz für deutschsprachige Open-Source-Produktivitätssuiten auf.

**München LiMux (Warnungsdaten).** Die Münchner LiMux-Migration (2003–2013) stellte etwa 15.000 Arbeitsplätze auf Linux und LibreOffice um und sparte nach Berichten 10 Millionen Euro an Lizenzkosten. Die anschließende Rückkehr (2017–2021, Rückkehr zu Windows/Microsoft 365) wird häufig als Beweis dafür angeführt, dass Open Source im großen Maßstab scheitert. Eine sorgfältige Lektüre der Münchner Post-Mortem-Literatur zeigt, dass die Rückkehr primär durch folgende Faktoren bedingt war: politischer Wechsel der Rathausführung, unzureichende Investitionen in Änderungsmanagement und Mitarbeiterschulung, Kompatibilitätsprobleme mit den Windows-abhängigen Arbeitsabläufen der Landesregierung und eine bewusste politische Entscheidung anstatt eines nachgewiesenen technischen Versagens.

**Schweizer Evidenz.** Schweizer Kantonsverwaltungen, die Open-Source-Komponenten über eCH-standardisierte Schnittstellen [17] und den GEVER-Rahmen [43] eingeführt haben, berichten, dass Interoperabilitätsstandardisierung — und nicht die Lizenzwahl an sich — der primäre TCO-Treiber ist. Gemeinden, die eCH-konforme Open-Source-Komponenten übernehmen, profitieren von gemeinsamen Datenmodellen, was die Integrationskosten reduziert. Der OSOR-Jahresbericht [28] und die Joinup-Plattform [53] stellen den derzeit umfassendsten Vergleichsdatensatz für europäische Regierungs-OSS-TCO bereit.

### 3.7 Bürgererfahrung und digitale Inklusion

Digitale Souveränität ist nicht nur ein institutionelles Anliegen. Bürgerinnen und Bürger interagieren mit kommunalen digitalen Diensten über ein breites Spektrum an technischem Können, sprachlichem Hintergrund und Zugang zu Geräten. Sowohl die OECD [49] als auch die UN E-Government Survey [29] dokumentieren anhaltende digitale Klüfte, die Open-Source-Strategien explizit adressieren müssen.

**Barrierefreiheit.** Die EU-Richtlinie über die Barrierefreiheit von Websites (2016/2102) und der Durchführungsbeschluss (EU) 2018/1524 verlangen, dass Websites und mobile Anwendungen des öffentlichen Sektors der WCAG 2.1 Level AA entsprechen. In Deutschland setzt die BITV 2.0 (Barrierefreie-Informationstechnik-Verordnung) diese Anforderung um. In der Schweiz gelten die P028-Bundeszugänglichkeitsrichtlinien. Gemeinden, die Open-Source-CMS, Bürgerportale und Partizipationsplattformen auswählen, müssen die WCAG-2.1-AA-Konformität überprüfen. TYPO3 [19] und Decidim [12] unterhalten aktive Barrierefreiheits-Arbeitsgruppen und veröffentlichen Konformitätserklärungen.

**Mehrsprachige Anforderungen.** Schweizer Gemeinden müssen möglicherweise Bürgerinnen und Bürger auf Deutsch, Französisch, Italienisch oder Rätoromanisch bedienen. Deutsche Gemeinden in Grenzregionen stellen zunehmend Dienste auf Türkisch, Arabisch und anderen Gemeinschaftssprachen bereit. Open-Source-CMS- und -Portalplattformen unterstützen mehrsprachige Inhalte generell durch etablierte Module, aber Gemeinden müssen für Übersetzungsabläufe und Content-Governance budgetieren.

**Vertrauen der Bürgerinnen und Bürger.** Die UN E-Government Survey [29] identifiziert das Vertrauen der Bürgerschaft als die bedeutendste nachfrageseitige Barriere für die E-Government-Nutzung. Vertrauen wird durch Transparenz (Open Source ermöglicht Prüfbarkeit), Datenschutz (DSGVO-Konformität, Datensparsamkeit) und Dienstleistungszuverlässigkeit aufgebaut. Sowohl die FSFE [4] als auch Janssen et al. [8] argumentieren, dass Open-Source-E-Government-Infrastruktur im Vergleich zu proprietären Black-Box-Systemen inhärente vertrauensbildende Eigenschaften besitzt.

**Inklusives Servicedesign.** Janssen, Charalabidis und Zuiderwijk [8] identifizieren Servicedesign — nicht die Technologiewahl — als den primären Bestimmungsfaktor für die Nutzung offener Daten und E-Government durch Bürgerinnen und Bürger. Open-Source-Plattformen sind eine notwendige, aber nicht hinreichende Bedingung für inklusive digitale Dienste. Gemeinden müssen neben der technischen Plattformimplementierung in UX-Forschung, verständliche Texte und unterstützende digitale Hilfeangebote investieren.

### 3.8 Lücken und Forschungsbedarf

Die Literatur zeigt mehrere bedeutende Lücken:

- Longitudinale TCO-Studien auf kommunaler Ebene, die Full-Stack-Open-Source- mit proprietären Implementierungen über Zeiträume von fünf Jahren und mehr vergleichen, fehlen weitgehend. Der Münchner Fall ist illustrativ, aber durch politische Variablen confundiert.
- Die regulatorische Interoperabilität zwischen dem deutschen OZG-Ökosystem und dem schweizerischen EMBAG/eCH-Rahmen wurde nicht systematisch kartiert; Grenzgemeinden stehen vor einer unstudiierten Compliance-Komplexität.
- KI-Governance in der öffentlichen Verwaltung ist ein aufkommendes Gebiet; souveräner KI-Einsatz auf kommunaler Ebene hat Stand Mitte 2026 keine etablierte Literaturbasis.
- Das Vertrauen der Bürgerschaft in Open-Source-E-Government wurde in europäischen kommunalen Kontexten empirisch nicht untersucht.

---

## 4. Technologie-Stack-Analyse

### 4.1 Digitale Identität — Keycloak

**Empfohlene Komponente:** Keycloak [21] | **Lizenz:** Apache 2.0 | **Bewertung: 4,70/5**

Keycloak stellt OpenID Connect (OIDC)-, OAuth-2.0- und SAML-2.0-Identitäts- und Zugriffsverwaltung für kommunale Anwendungen bereit. Es unterstützt Multi-Faktor-Authentifizierung, fein abgestimmte Autorisierung und Integration mit externen Identitätsanbietern, einschließlich Deutschlands BundID und der Schweizer E-ID [38]. Keycloaks Föderationsfähigkeiten ermöglichen es einer Gemeinde, einen einzigen autoritativen Identitätsspeicher zu pflegen und gleichzeitig die Authentifizierung an bürgerliche Identitätsanbieter in Übereinstimmung mit den Anforderungen von OZG 2.0 [2] und EMBAG [1] zu delegieren.

Einsatzreferenzen umfassen den gehosteten Keycloak-Dienst von Dataport für norddeutsche Gemeinden [24] und die Aufnahme von Keycloak als Identitätsschicht von OpenDesk durch ZenDiS [42]. Die BSI-IT-Grundschutz-[26]-Kompatibilität ist durch Standard-Härtungsverfahren erreichbar.

**Schlüsselintegration:** Keycloak sollte als zentraler Identitätsbroker konfiguriert werden, wobei bürgerorientierte Anwendungen OIDC-Token konsumieren und Mitarbeiteranwendungen SAML für Legacy-Kompatibilität verwenden.

### 4.2 Dokumentenmanagement — Nextcloud + OpenProject

**Empfohlene Komponenten:** Nextcloud [13] (AGPL-3.0, Bewertung 4,20) + OpenProject [20] (GPLv3, Bewertung 3,65)

Nextcloud bietet föderativen Dateispeicher, -freigabe und -zusammenarbeit mit unternehmenstauglichen Funktionen einschließlich Ende-zu-Ende-Verschlüsselung, Audit-Protokollierung und mobilen Clients. Nextcloud-for-Government-[13]-Einsätze umfassen mehrere deutsche Landesverwaltungen und Schweizer Kantonsbüros. OpenProject bietet Projektmanagement, Aufgabenverfolgung und Dokumentenabläufe.

**GEVER-Integration (CH):** Schweizer Gemeinden müssen diese Kombination an den GEVER-Rahmenanforderungen [43] für die Aktenführung messen. Für formale Akten, die der Aufbewahrungspflicht unterliegen, muss möglicherweise eine konforme Aktenführungsschicht (eCH-0039 [17]) über Nextcloud gelegt werden.

### 4.3 Workflow-Automatisierung — Camunda / Flowable

**Empfohlene Komponenten:** Camunda Platform 8 Community [33] (Apache 2.0, Bewertung 4,20) / Flowable (Apache 2.0)

BPMN-2.0-basierte Workflow-Engines sind für die Digitalisierung von Verwaltungsverfahren im Rahmen von OZG 2.0 [2] und FIM [32] unerlässlich. Die FIM-Prozessbibliothek stellt wiederverwendbare BPMN-Prozessvorlagen für über 575 standardisierte Verwaltungsverfahren bereit, was den benutzerdefinierten Entwicklungsaufwand erheblich reduziert. Beide Plattformen unterstützen XÖV-Datenaustauschstandards [46] und sind mit FIM-Prozessmodellen kompatibel.

**Schlüsselintegration:** Workflow-Engines sollten mit Keycloak [21] zur Authentifizierung, Nextcloud [13] für Dokumentenanhänge integriert und auf Kubernetes [39] auf SCS-Infrastruktur [3] eingesetzt werden.

### 4.4 Bürgerbeteiligung — Decidim / CONSUL

**Empfohlene Komponenten:** Decidim [12] (AGPL-3.0, Bewertung 3,90) / CONSUL Democracy [40] (AGPL-3.0)

Digitale Partizipationsplattformen werden zunehmend im Rahmen kommunaler demokratischer Beteiligungspflichten vorgeschrieben oder erwartet. Decidim — in Barcelona entwickelt und von der Decidim Association [12] gepflegt — bietet partizipatives Budgetieren, Vorschläge, Versammlungen und deliberative Prozesse. CONSUL Democracy [40], entwickelt vom Ayuntamiento de Madrid, bietet vergleichbare Funktionen mit einer stärkeren Erfolgsbilanz in spanischsprachigen Rechtssystemen.

Decidim ist die empfohlene erste Wahl für deutsch- und französischsprachige Gemeinden aufgrund seiner aktiveren Internationalisierungscommunity, WCAG-2.1-AA-Auditgeschichte und Integration in europäische digitale Partizipationsnetzwerke. Die Plattform ist in über 400 Gemeinden weltweit im Einsatz, darunter Barcelona, Helsinki und mehrere Schweizer Gemeinden.

### 4.5 Kommunikation — Matrix / Jitsi / BigBlueButton

**Empfohlene Komponenten:** Matrix/Synapse [14] (Apache 2.0, Bewertung 4,35), Jitsi Meet [35] (Apache 2.0), BigBlueButton [34] (LGPL-3.0, Bewertung 3,90)

Das Matrix-Protokoll [14] stellt ein föderiertes, Ende-zu-Ende-verschlüsseltes Messaging-Netz für die Mitarbeiterkommunikation bereit. Element (der führende Matrix-Client) ist das Kommunikations-Backbone der französischen Regierungsplattform Tchap und des deutschen BundesMessengers. Jitsi Meet [35] stellt leichtgewichtige, browserbasierte Videokonferenzen bereit. BigBlueButton [34] bietet eine funktionsreichere Plattform, die für öffentliche Gemeinderatssitzungen und Bürgerkonsultationen geeignet ist.

### 4.6 Offene Daten — CKAN

**Empfohlene Komponente:** CKAN [22] | **Lizenz:** AGPL-3.0 | **Bewertung: 4,25/5**

CKAN ist die de facto Standard-Open-Data-Portalplattform für die europäische Verwaltung und liegt data.gov.uk, dem EU Open Data Portal, opendata.swiss [44] und GovData.de zugrunde. Für Gemeinden stellt CKAN einen standardskonformen Datenkatalog (DCAT-AP), Datensatzverwaltung, API-Zugang und Harvesting von anderen CKAN-Instanzen bereit. Gemeinden, die auf CKAN veröffentlichen, können über DCAT-AP-Harvesting mit kantonalen/Länder- und nationalen Portalen föderieren und damit Open-Data-Verpflichtungen unter OZG 2.0 [2] und der schweizerischen Open-Government-Data-Strategie [44] erfüllen.

### 4.7 GIS — QGIS / GeoServer / OpenStreetMap

**Empfohlene Komponenten:** QGIS [37] (GPL-2.0+, Bewertung 4,85), GeoServer, OpenStreetMap [36] (ODbL-1.0)

QGIS [37] bietet ein vollständiges Desktop-GIS für kommunale Mitarbeitende mit nativer Unterstützung für OGC-Standards (WMS, WFS, WCS). GeoServer stellt serverseitige räumliche Datenpublikation und OGC-Webdienste bereit. OpenStreetMap [36] stellt eine global gepflegte, lizenzgebührenfreie Basiskarte bereit. GeoServer sollte WMS/WFS-Dienste bereitstellen, die vom kommunalen Webportal für öffentliche Kartenanwendungen konsumiert werden. QGIS integriert sich mit PostgreSQL/PostGIS [41] zur Speicherung räumlicher Daten.

### 4.8 CMS — TYPO3 / Drupal

**Empfohlene Komponenten:** TYPO3 [19] (GPL-2.0, Bewertung 4,20) / Drupal

Die kommunale Website und das Bürgerportal erfordern ein CMS, das redaktionelle Zugänglichkeit mit technischer Sicherheit, Barrierefreiheitskonformität und langfristiger Wartbarkeit verbindet. TYPO3 [19] nimmt eine dominante Stellung in der deutschen und schweizerischen öffentlichen Verwaltung ein, mit außergewöhnlich hoher Penetration im öffentlichen Sektor in der DACH-Region. Die TYPO3 Association veröffentlicht spezifische Leitlinien für Einsätze in der öffentlichen Verwaltung, einschließlich BITV-2.0-/WCAG-2.1-AA-Konformitäts-Toolkits. Für die meisten deutschen und schweizerischen Gemeinden ist TYPO3 die pragmatische Empfehlung auf der Grundlage der bestehenden Dichte des Dienstleister-Ökosystems.

### 4.9 Cloud-Infrastruktur — Sovereign Cloud Stack

**Empfohlene Komponente:** Sovereign Cloud Stack (SCS) [3, 11] | **Lizenz:** Apache 2.0 | **Bewertung: 4,40/5**

Der Sovereign Cloud Stack [3] ist eine OSBA-koordinierte Open-Source-Cloud-Infrastrukturspezifikation, die auf OpenStack, Kubernetes [39] und Ceph aufbaut, mit zusätzlichen Schichten für Identität, Monitoring und Sicherheit, ausgerichtet auf BSI IT-Grundschutz [26] und BSI-Cloud-Mindeststandards [52].

SCS adressiert die grundlegende Frage der Infrastruktursouveränität: Eine Gemeinde oder ihr kooperativer Dienstleister kann SCS auf eigener oder gemieteter Hardware innerhalb der deutschen oder schweizerischen Jurisdiktion betreiben, wodurch Abhängigkeiten von US-amerikanischen Hyperscalern eliminiert und das Schrems-II-/transatlantische Datentransfer-Compliance-Problem gelöst werden. Mehrere SCS-zertifizierte Anbieter sind kommerziell verfügbar, und govdigital eG [23] entwickelt ein mandantenfähiges SCS-Angebot für den kommunalen Einsatz.

### 4.10 KI- und Datendienste

**Souveräne KI-Prinzipien für die öffentliche Verwaltung.** Der Einsatz von Künstlicher Intelligenz in der Kommunalverwaltung wirft spezifische Souveränitätsfragen auf. Die Abhängigkeit von proprietären Large-Language-Model-APIs (LLM) schafft Abhängigkeiten, die mit den DSGVO-Artikel-22-Verpflichtungen bezüglich automatisierter Entscheidungsfindung in Konflikt geraten können, Bürgerdaten der Verarbeitung durch Dritte unter nicht prüfbaren Bedingungen aussetzen und Anbieterabhängigkeit auf der Ebene der Inferenz statt der Software erzeugen können.

Dieses Papier übernimmt fünf souveräne KI-Prinzipien für die kommunale öffentliche Verwaltung:

1. **Datensparsamkeit und Pseudonymisierung:** Jede KI-Komponente, die Bürgerdaten verarbeitet, muss DSGVO-Datensparsamkeit und Pseudonymisierung anwenden. Eingaben an KI-Modelle sollten keine direkt identifizierenden Informationen enthalten, es sei denn, dies ist unbedingt erforderlich und ausdrücklich eingewilligt.
2. **Lokale Inferenz als Standard:** KI-Inferenz sollte auf Infrastruktur innerhalb der Kontrolle der Gemeinde oder ihres kooperativen Anbieters durchgeführt werden, nicht an externe APIs gesendet.
3. **Modelltransparenz:** Gemeinden sollten offene Gewichtsmodelle (Llama 3.x, Mistral, Falcon) mit veröffentlichten Modellkarten gegenüber proprietären geschlossenen Modellen bevorzugen.
4. **Mensch im Regelkreis:** Konsistent mit DSGVO Artikel 22 [27] dürfen Entscheidungen mit rechtlicher oder ähnlich bedeutsamer Wirkung auf Bürgerinnen und Bürger nicht ausschließlich durch automatisierte Verarbeitung getroffen werden. KI-Tools in kommunalen Kontexten sollten als Entscheidungsunterstützungswerkzeuge fungieren, nicht als autonome Entscheidungsträger.
5. **Anbieterdiversifizierung:** Wenn KI-Fähigkeiten extern beschafft werden, müssen Verträge Datenportabilität sicherstellen, Exklusivität vermeiden und die Migration zu alternativen Anbietern ermöglichen.

**Empfohlene Open-Source-KI-Komponenten:**

| Komponente | Lizenz | Funktion |
|---|---|---|
| LocalAI | MIT | OpenAI-kompatibler REST-API-Server; führt Open-Weight-LLMs lokal aus |
| Ollama | MIT | Laufzeitumgebung für lokale LLM-Implementierung; wachsende Modellbibliothek |
| OpenWebUI | MIT | Browserbasierte Chat-Oberfläche für LocalAI/Ollama-Backends |

**Kommunale KI-Anwendungsfälle:** Dokumentenzusammenfassung (Verarbeitung von Gemeinderatssitzungsprotokollen, Rechtstexten), FAQ-Chatbots für Bürgeranfragen (mit menschlichem Eskalationspfad), GIS-Analyseunterstützung, Übersetzungsunterstützung für mehrsprachige Serviceinhalte und internes Wissensmanagement.

**Data-Warehouse-Integration:** Kommunale KI-Dienste sollten mit einem PostgreSQL-[41]-basierten Data Warehouse oder einem CKAN-[22]-Datenkatalog integriert werden, um Retrieval-Augmented Generation (RAG) über kommunale Datensätze zu ermöglichen. Dieser Ansatz begrenzt KI-Ausgaben auf verifizierte kommunale Daten, reduziert das Halluzinationsrisiko und verbessert die Prüfbarkeit.

### 4.11 Referenzarchitektur

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 9 — CITIZEN & STAFF INTERFACES                               │
│  TYPO3/Drupal (portal)  │ Decidim/CONSUL (participation)           │
│  OpenWebUI (AI chat)    │ Mobile apps (TYPO3 REST)                 │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 8 — COLLABORATION & COMMUNICATION                            │
│  Nextcloud (files/docs) │ OpenProject (PM) │ Matrix/Element (chat) │
│  Jitsi Meet (video)     │ BigBlueButton (webinar/council)          │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 7 — PROCESS & WORKFLOW                                       │
│  Camunda / Flowable (BPMN 2.0)  │ FIM Prozessbibliothek            │
│  XÖV/eCH Connectors              │ XForms / form engine             │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 6 — AI & DATA SERVICES                                       │
│  LocalAI / Ollama (LLM inference)  │ OpenWebUI (interface)         │
│  CKAN (open data portal)           │ PostgreSQL/PostGIS (warehouse)│
│  RAG pipeline                      │ Anonymisation / pseudonymise  │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 5 — GEOSPATIAL                                               │
│  GeoServer (OGC WMS/WFS) │ QGIS (desktop/server) │ OSM (base map)│
│  PostGIS (spatial DB)    │ Public map portal                      │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 4 — IDENTITY & SECURITY                                      │
│  Keycloak (IAM / OIDC / SAML)  │ BundID federation (DE)           │
│  Swiss E-ID / BGEID (CH)        │ BSI IT-Grundschutz controls      │
│  NIS2-compliant SIEM / logging  │ Vulnerability scanning           │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 3 — INTEGRATION & API GATEWAY                                │
│  REST / GraphQL API gateway  │ XÖV / eCH adapters                  │
│  FIM connectors              │ Event bus (Kafka / NATS)            │
│  Audit logging               │ OpenAPI specifications               │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 2 — CONTAINER ORCHESTRATION                                  │
│  Kubernetes [39] │ Helm charts │ GitOps (Flux / ArgoCD)           │
│  Prometheus/Grafana (monitoring) │ Loki/OpenSearch (logging)      │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────▼───────────────────────────────────────┐
│  LAYER 1 — SOVEREIGN CLOUD INFRASTRUCTURE — SCS [3]               │
│  OpenStack (compute/network/storage) │ Ceph (block/object/file)   │
│  SCS-certified hoster OR on-premise  │ DE/CH/EU jurisdiction only  │
│  govdigital eG [23] / Dataport [24] / cantonal ICT provider        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Implementierungsfahrplan

### Phase 0 — Organisatorische Bereitschaft und Bestandsaufnahme
**Dauer:** 3–6 Monate | **Indikativer Kostenbereich: 50.000–200.000 Euro**

Durchführung der Selbstbewertung zur digitalen Souveränität (Anhang C); Kartierung des aktuellen Technologieportfolios und der Lizenzkosten; Festlegung eines politischen und exekutiven Mandats; Definition der Governance-Struktur; Identifikation von Kooperationspartnern.

**Liefergegenstände:** Bericht zur Basislinie digitaler Souveränität; Software-Asset-Inventar mit TCO-Basislinie; Gemeinderatsbeschluss; Partnerschaftsvereinbarungen mit kooperativen Dienstleistern.

**Erfolgskriterien:** Exekutiver Sponsor identifiziert und bestätigt; Software-Asset-Inventar vollständig; mindestens eine Kooperationspartnerschaft etabliert; Haushaltsrahmen für Phase 1 vom Gemeinderat genehmigt.

### Phase 1 — Infrastruktur- und Identitätsfundament
**Dauer:** 6–12 Monate | **Indikativer Kostenbereich: 150.000–500.000 Euro**

Einsatz SCS-basierter [3] Cloud-Infrastruktur; Implementierung von Keycloak [21] föderiert mit BundID/E-ID; Einrichtung des Kubernetes-Clusters [39] mit GitOps-Pipeline; Implementierung des NIS2-konformen Sicherheits-Baselines [27].

**Liefergegenstände:** SCS-Infrastruktur in Betrieb mit SLA-gestütztem kooperativem Support; Keycloak-Identitätsplattform in Produktion mit nationaler Identitätsföderierung; BSI-IT-Grundschutz-[26]-Basisdokumentation vollständig; NIS2-Vorfallreaktionsverfahren in Kraft.

**Erfolgskriterien:** Infrastrukturverfügbarkeit ≥99,5 % über einen 60-tägigen Beobachtungszeitraum; alle Mitarbeitenden können sich über Keycloak SSO authentifizieren; erste IT-Grundschutz-Lückenanalyse abgeschlossen und Abhilfemaßnahmenplan genehmigt.

### Phase 2 — Kollaborations- und Kommunikationsplattform
**Dauer:** 6–12 Monate | **Indikativer Kostenbereich: 200.000–600.000 Euro**

Einsatz von Nextcloud [13] und OpenProject [20]; Einsatz von Matrix/Element [14] für Mitarbeiter-Messaging; Einsatz von Jitsi [35] und BigBlueButton [34]; Durchführung des Mitarbeiterschulungsprogramms.

**Liefergegenstände:** Nextcloud mit abteilungsweisem Rollout-Plan; Matrix-Homeserver, föderiert mit Landesregierungsinstanzen, wo verfügbar; Videokonferenzen betriebsbereit und für Gemeinderatssitzungen getestet; Schulungsmaterialien und internes OSS-Champion-Netzwerk.

**Erfolgskriterien:** ≥80 % der Pilotabteilungsmitarbeitenden nutzen Nextcloud für primäres Dateimanagement; ≥60 % der internen Besprechungen über selbst gehostete Konferenzlösungen; Mitarbeiterzufriedenheitsumfragebewertung ≥3,5/5,0.

### Phase 3 — Workflow-Automatisierung und digitale Dienste
**Dauer:** 9–18 Monate | **Indikativer Kostenbereich: 150.000–400.000 Euro**

Einsatz der Camunda/Flowable-[33]-Workflow-Engine; Digitalisierung der 10 wichtigsten bürgerorientierten Prozesse mithilfe von FIM-Vorlagen [32]; Integration von OZG-2.0-Diensten [2]; Einsatz des CKAN-[22]-Open-Data-Portals; Start des TYPO3-[19]-Bürgerportals mit WCAG-2.1-AA-Konformität.

**Liefergegenstände:** Top-10-Bürgerprozesse digitalisiert und veröffentlicht; OZG-2.0-Dienste integriert und durch Landesbehörde bestätigt; CKAN-Portal live mit mindestens 20 Datensätzen, die an das nationale Portal föderiert sind; TYPO3-Portal mit veröffentlichter BITV-2.0-/WCAG-2.1-AA-Konformitätserklärung.

**Erfolgskriterien:** Top-10-Dienste Ende-zu-Ende online verfügbar ohne obligatorischen Papierschritt; CKAN-Portal durch govdata.de oder opendata.swiss geharvestet; WCAG-2.1-AA-Audit durch unabhängigen Dritten bestanden.

### Phase 4 — Erweiterte Dienste und Bürgerbeteiligung
**Dauer:** 6–12 Monate | **Indikativer Kostenbereich: 100.000–300.000 Euro**

Einsatz von Decidim [12] oder CONSUL [40] für Bürgerbeteiligung; Einsatz des GIS-Stacks (QGIS [37], GeoServer, OSM [36]); Start souveräner KI-Dienste (LocalAI/Ollama, OpenWebUI); Implementierung des PostgreSQL-[41]-Data-Warehouse mit RAG.

**Liefergegenstände:** Partizipationsplattform in Betrieb mit erstem Partizipationsprozess; GIS-Stack in Betrieb mit öffentlichem Kartenportal; KI-Assistent für Mitarbeitende zur Dokumentenzusammenfassung und FAQ-Erstellung; Data Warehouse in Betrieb; keine Bürgerdaten an externe KI-APIs gesendet.

**Erfolgskriterien:** ≥500 Bürgerteilnehmende im ersten partizipativen Budgetierungszyklus; GIS-Datensätze unter offener Lizenz auf CKAN veröffentlicht; KI-Assistent von ≥50 % der Verwaltungsmitarbeitenden übernommen.

### Phase 5 — Optimierung, Beitrag und Replikation
**Dauer:** Fortlaufend ab Monat 30+ | **Indikativer Jahresaufwand: 50.000–150.000 Euro/Jahr**

Optimierung der Betriebskosten; Beitrag zu Upstream-OSS-Communities; Veröffentlichung kommunaler Komponenten auf openCode.de [10]; Weitergabe von Erkenntnissen an Peer-Gemeinden; jährliche Überprüfung der Selbstbewertung.

**Liefergegenstände:** Dokumentierte Beiträge zu Upstream-OSS-Projekten; mindestens ein Modul/Template auf openCode.de veröffentlicht; interkommunale Wissensaustauschvereinbarung; jährlicher Bericht zur digitalen Souveränität an den Gemeinderat.

**Erfolgskriterien:** Netto-Lizenzkosteneinsparungen gegenüber dem Ausgangsniveau vor der Umstellung nachweisbar; mindestens ein OSS-Beitrag upstream akzeptiert; Peer-Gemeinde in kooperativer Beschaffung oder Wissensaustausch eingebunden.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Rolle | Primäres Interesse | Einfluss | Einbindungsstrategie |
|---|---|---|---|---|
| Gemeinderat | Politisches Mandat | Fiskalische Verantwortung, Bürgernutzen | Hoch | Fortschrittsberichte, TCO-Dashboards |
| Bürgermeister / Hauptverwaltungsbeamter | Exekutiver Sponsor | Strategische Vision, Risikomanagement | Hoch | Einzelgespräche, Meilensteinreviews |
| CIO / IT-Leitung | Technische Führung | Betriebszuverlässigkeit, Personalkapazität | Hoch | Gemeinsame Entwicklung des Fahrplans, technische Arbeitsgruppe |
| Verwaltungsmitarbeitende | Endnutzende | Benutzerfreundlichkeit, Schulung, Workflow-Kontinuität | Mittel–Hoch | Änderungsmanagement, Champion-Netzwerk |
| Bürgerinnen und Bürger | Leistungsempfängende | Dienstverfügbarkeit, Datenschutz | Mittel | Partizipationsplattformen, Transparenzberichte |
| Landes-/Kantonale IT-Behörde | Regulierungsaufsicht | OZG/EMBAG-Compliance, Interoperabilität | Hoch | Frühzeitige Abstimmung, gemeinsame Beschaffung |
| govdigital / Dataport [23, 24] | Kooperativer Dienstleister | Kommerzielle Beziehung, gemeinsame Dienste | Mittel | Rahmenvereinbarungen, SLA-Definition |
| OSS-Communities | Softwarelieferanten | Übernahme, Beitrag, Finanzierung | Niedrig | Community-Engagement, Upstream-Beiträge |
| Zivilgesellschaft / Digitalrechtsorganisationen | Interessenvertretung, Kontrolle | OSS-Prinzipien, Datenschutz | Niedrig–Mittel | Transparenzberichte, Public-Code-Versprechen |
| Lokale IKT-KMU | Implementierungspartner | Kommerzielle Möglichkeit | Mittel | Offene Beschaffung, UVgO-/VgV-Vergaben |

### 6.2 Beschaffungsrahmen

Die kommunale OSS-Beschaffung muss durch EU-Vergaberegeln, deutsche VgV/UVgO- oder schweizerische BöB/VöB-Verfahren und die Interoperabilitätsbewertungspflicht des Interoperable Europe Act [6] navigieren. Sechs Grundsätze regeln den Rahmen:

1. **Funktionale Spezifikation, nicht Produktspezifikation.** Ausschreibungsunterlagen müssen die erforderlichen Funktionen angeben, nicht bestimmte Produkte, um offenen Wettbewerb zu gewährleisten und gleichzeitig OSS-Angebote zuzulassen.
2. **Bewertung der Gesamtbetriebskosten.** Vergabekriterien müssen mehrjährige TCO umfassen, die Lizenz-, Implementierungs-, Betriebs-, Schulungs-, Ausstiegs- und Migrationskosten abdecken.
3. **Offene Standards obligatorisch.** Alle beschafften Komponenten müssen XÖV [46] (DE), eCH [17] (CH), DCAT-AP (offene Daten), OGC (GIS), OIDC/SAML (Identität), BPMN 2.0 (Workflow) unterstützen.
4. **Quellcode-Hinterlegung oder offene Lizenz.** Bei maßgeschneiderter Entwicklung muss der Vertrag entweder die Open-Source-Veröffentlichung fordern (EMBAG Artikel 9 [1]) oder eine Quellcode-Hinterlegung vorsehen.
5. **Datenportabilität und Ausstiegsrechte.** Alle Verträge müssen eindeutige Datenportabilität einschließen: vollständiger, maschinenlesbarer Export aller kommunalen Daten in einem offenen Format innerhalb von 30 Tagen nach Vertragsbeendigung.
6. **Kooperative und Rahmenbeschaffung.** Gemeinden sollten Rahmenvereinbarungen priorisieren, die von govdigital [23], Dataport [24], BeschA oder kantonalen Beschaffungsstellen aufgestellt wurden.

### 6.3 Änderungsmanagement

Das Münchner LiMux-Post-Mortem zeigt, dass technische Qualität für eine erfolgreiche OSS-Umstellung nicht ausreichend ist. Änderungsmanagement ist der entscheidende Erfolgsfaktor: Ernennung interner OSS-Champions in jeder Abteilung; Investition in Schulungen proportional zur Mitarbeiterzahl (3–5 Tage pro Mitarbeiter für die Produktivitätssuiten-Umstellung); offene Kommunikation über die Umstellung; Einrichtung eines strukturierten Mitarbeiter-Feedbackmechanismus; Pilotierung vor Mandatierung.

### 6.4 Rechts- und Regulierungs-Compliance-Matrix

| Regulierung | Rechtsraum | Schlüsselanforderung | Auswirkung auf OSS-Stack | Compliance-Mechanismus |
|---|---|---|---|---|
| DSGVO / nDSG | EU / DE / CH | Rechtliche Grundlage, Datensparsamkeit, Auskunftsrechte | Alle bürgerorientierten Komponenten; KI-Dienste | Privacy-by-Design in Nextcloud/Keycloak; DSGVO-konformes Hosting; Datenschutzbeauftragter; Art.-22-Mensch-im-Regelkreis für KI |
| NIS2-Richtlinie [27] | EU (DE: KRITIS-Dachgesetz) | Vorfallmeldung (24h), Risikomanagement, Lieferkettensicherheit | SCS-Infrastruktur; alle kritischen Dienste | BSI IT-Grundschutz [26]; NIS2-kompatibles ISMS; Vorfallreaktionsplan |
| OZG 2.0 [2] | DE | Online-Leistungsverfügbarkeit; BundID; Once Only | Workflow [4.3]; Portal [4.8]; Identität [4.1] | Camunda-FIM-Integration; Keycloak-BundID-Föderierung; OZG-Marktplatz |
| EMBAG [1] | CH | Open Source by Default (Art. 9); Veröffentlichungspflicht | Alle maßgeschneiderte Entwicklung | OSS-Lizenz auf benutzerdefiniertem Code; Veröffentlichung auf kantonalem/föderalem Repository |
| Interoperable Europe Act [6] | EU | Interoperabilitätsbewertung vor Einsatz | Alle beschafften Komponenten | EIF-[45]-Bewertungscheckliste; Joinup-Veröffentlichung von Lösungen |
| BITV 2.0 / WCAG 2.1 AA | DE | AA-Konformität; Barrierefreiheitserklärung | Portal [4.8]; Partizipation [4.4]; alle Web-Apps | Drittanbieter-WCAG-Audit; TYPO3-Barrierefreiheits-Toolkit |
| BSI IT-Grundschutz [26] | DE | Basis-Sicherheitsmaßnahmen; Dokumentation | SCS [4.9]; Identität [4.1]; alle Infrastruktur | IT-Grundschutz-Implementierungsprojekt; jährliche Überprüfung |
| ISDS / P028 | CH | Sicherheitsbasis; Barrierefreiheit | Alle Bundes-/Kantonalsoftware | P028-Konformitätsbewertung; ISDS-Risikomanagement |
| eCH-Standards [17] | CH | Datenaustauschkonformität (eCH-0039, eCH-0058) | Workflow [4.3]; DMS [4.2]; offene Daten [4.6] | eCH-konforme Schnittstellen; eCH-Zertifizierung, wo verfügbar |

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| # | Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|---|
| R1 | Politische Umkehr — neue Gemeindeführung kehrt OSS-Mandat um | Mittel | Hoch | Gemeinderatsbeschluss; dokumentierter Bürgernutzen und TCO-Einsparungen |
| R2 | Mitarbeiterwiderstand — Endnutzende verweigern die Annahme neuer Tools | Mittel | Hoch | Änderungsmanagementprogramm; Champion-Netzwerk; schrittweises Rollout; Benutzerfreundlichkeitsinvestition |
| R3 | Integrationsversagen mit Legacy-Systemen der Länder/Kantone | Mittel | Mittel | XÖV/eCH-Standardkonformität; frühzeitige Integrationstests; Länder-Koordination |
| R4 | Ökosystemkollaps — wichtige OSS-Komponente verliert Community-Unterstützung | Niedrig | Hoch | Multi-Lieferanten-Supportverträge; Upstream-Beiträge; Fork-Bereitschaft |
| R5 | Sicherheitsvorfall — Verletzung der souveränen Infrastruktur | Niedrig | Sehr hoch | BSI IT-Grundschutz [26]; NIS2 ISMS [27]; Penetrationstests; SCS-Sicherheits-Baseline [3] |
| R6 | Kostenüberschreitung — Implementierungskosten übersteigen Schätzungen | Mittel | Mittel | Phasierte Finanzierung; 20%-Notfallreserve; kooperative Beschaffung |
| R7 | Compliance-Versagen — DSGVO/NIS2/OZG/EMBAG-Nichteinhaltung | Niedrig | Hoch | Rechts-Compliance-Matrix [Abschnitt 6.4]; Datenschutzbeauftragter ab Phase 0 |
| R8 | KI-Governance-Versagen — Bürgerdaten durch KI-Dienste exponiert | Mittel | Hoch | Nur lokale Inferenz; Datensparsamkeit; keine proprietären LLM-APIs für Bürgerdaten; DSGVO Art. 22 |
| R9 | Qualifikationslücke — unzureichende OSS-technische Kapazität intern | Hoch | Mittel | Schulungsinvestition; kooperatives Dienstleistungsmodell; schrittweise Internalisierung |
| R10 | Scope-Creep — Fahrplan dehnt sich über kommunale Kapazität hinaus aus | Mittel | Mittel | Phasen-Gate-Governance; Unterzeichnung durch exekutiven Sponsor; MVP-Disziplin |

### 7.2 Münchner Warnbeispiel

Das Münchner LiMux-Programm (2003–2013) ist die am umfassendsten dokumentierte großangelegte kommunale Open-Source-Umstellung in der europäischen Geschichte. Die Migration stellte erfolgreich etwa 14.800 Arbeitsplätze auf Ubuntu Linux und LibreOffice um und erzielte dokumentierte Lizenzeinsparungen von etwa 10 Millionen Euro. Die Rückkehr (initiiert durch die CSU/SPD-Koalitionsvereinbarung 2014, abgeschlossen etwa 2021) ist auf folgende Faktoren zurückzuführen: politischer Wechsel; eine 2016 von der neuen Verwaltung in Auftrag gegebene interne Bewertung; Lobbydruck seitens Microsoft; und Kompatibilitätsprobleme mit den Arbeitsabläufen der bayerischen Landesverwaltung.

**Lehren:** (1) Das politische Mandat muss in einem Gemeinderatsbeschluss institutionalisiert werden, nicht nur in einer Exekutiventscheidung. (2) Die Interoperabilität mit vertikalen Regierungssystemen ist existenziell. (3) Die Investition in das Änderungsmanagement muss proportional sein. (4) Wirtschaftliche Evidenz muss präventiv dokumentiert werden.

### 7.3 Sicherheitsüberlegungen

Die kommunale digitale Infrastruktur ist ein Ziel für Ransomware, Datendiebstahl und Angriffe staatlicher Akteure. BSI IT-Grundschutz [26] stellt die maßgebliche deutsche Baseline bereit. NIS2 [27] verlangt von Gemeinden, die als wesentliche oder wichtige Einrichtungen eingestuft sind, Risikomanagementmaßnahmen umzusetzen und erhebliche Vorfälle innerhalb von 24 Stunden zu melden. Schlüsselmaßnahmen: SCS-Infrastruktur [3] mit BSI-Cloud-Mindeststandards [52]; Keycloak [21] mit erzwungener MFA; Sicherheitsupdates innerhalb von 48 Stunden nach kritischem CVE; jährliche Penetrationstests; NIS2-konformer Vorfallreaktionsplan.

### 7.4 Regulatorische Risikoanalyse

| Regulatorische Entwicklung | Wahrscheinlichkeit (3 Jahre) | Kommunale Auswirkung | Reaktion |
|---|---|---|---|
| NIS2-Erweiterung auf kleinere Gemeinden | Mittel | Obligatorisches ISMS; Vorfallmeldekosten | ISMS in Phase 1 proaktiv implementieren |
| EU-KI-Akts-Tier-Reklassifizierung kommunaler KI-Anwendungsfälle | Mittel | Konformitätsbewertungsanforderungen | KI-Anwendungsfälle dokumentieren; Hochrisikokategorien vermeiden; Mensch-im-Regelkreis beibehalten |
| OZG-2.0-Interoperabilitätsmandat verschärft | Hoch | Schnellerer Implementierungszeitplan | Phase-3-OZG-Integration priorisieren; enger Kontakt mit Landes-IT-Behörde |
| DSGVO-Durchsetzung bezüglich Nicht-EU-Cloud-Hosting | Mittel | Herausforderung für Nicht-SCS-Implementierungen | Migration zu SCS [4.9] in Phase 1; Vermeidung von Nicht-EU-Hyperscalern |
| Schweizer BGEID-Rollout-Beschleunigung [38] | Hoch (CH) | Schnellere E-ID-Integration erforderlich | Keycloak-E-ID-Föderierung in Phase 1 integrieren |
| Interoperable Europe Act Compliance-Frist | Hoch | Interoperabilitätsbewertung erforderlich | EIF-[45]-Bewertung in alle Beschaffungen ab Phase 3+ einbeziehen |
| EMBAG-Artikel-9-Kantonsausdehnung (CH) | Mittel | OSS-Veröffentlichungspflichten | OSS-Veröffentlichungsklausel in alle Entwicklungsverträge aufnehmen |

---

## 8. Schlussfolgerung

Der Fall für Open-Source-digitale Souveränität in der Kommunalverwaltung hat sich im vergangenen Jahrzehnt entschieden von Interessenvertretung zu Evidenz verlagert. Gesetzliche Rahmenbedingungen in Deutschland (OZG 2.0 [2]), der Schweiz (EMBAG [1]) und der Europäischen Union (Interoperable Europe Act [6], EU Open Source Strategy [5]) schaffen nun strukturelle Anreize — und in einigen Fällen Verpflichtungen — für öffentliche Verwaltungen, offener, interoperabler und prüfbarer Software den Vorzug zu geben. Die Technologiekomponenten für einen vollständigen kommunalen digitalen Stack sind ausgereift, gut verwaltet und auf vergleichbarer Ebene in ganz Europa im Einsatz.

Digitale Souveränität ist kein Endzustand, sondern eine kontinuierliche Praxis. Die Gemeinde, die diesen Stack 2027 einsetzt, wird ihre Technologieentscheidungen 2032 erneuern müssen. Der Vorteil des Open-Source-Ansatzes besteht genau darin, dass diese Erneuerung möglich ist: Komponenten können ersetzt, aufgerüstet oder geforkt werden ohne Anbietererlaubnis oder vertragliche Strafe. Die digitale Infrastruktur der Öffentlichkeit sollte so prüfbar, anpassungsfähig und demokratisch sein wie die Institutionen, denen sie dient. Öffentliches Geld sollte öffentlichen Code hervorbringen [4].

---

## Literaturverzeichnis

[1] Schweizerische Bundeskanzlei (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*, SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://fedlex.admin.ch/eli/cc/2023/682/de. Lizenz: CC0.

[2] Bundesministerium des Innern und für Heimat (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de. Lizenz: DL-DE/Zero 2.0.

[3] Open Source Business Alliance (OSBA) (2023). *Sovereign Cloud Stack (SCS)*. Berlin: OSBA. https://scs.community. Lizenz: Apache 2.0 / CC-BY-SA-4.0.

[4] Free Software Foundation Europe (FSFE) (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu. Lizenz: CC-BY-SA-4.0.

[5] Europäische Kommission (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu. Lizenz: CC-BY.

[6] Europäisches Parlament und Rat (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*, ABl. L 903/2024, 22. März 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903. Lizenz: EU-Gesetzgebung (gemeinfrei).

[7] Wirtz, B.W. & Weyerer, J.C. (2017). Holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024.

[8] Janssen, M., Charalabidis, Y. & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740.

[9] FITKO (2024). *FITKO Jahresbericht 2023*. Frankfurt: FITKO. https://fitko.de. Lizenz: DL-DE/Zero 2.0.

[10] Digitalservice GmbH des Bundes (2023). *openCode.de*. Berlin: Digitalservice. https://opencode.de.

[11] SCS Community / OSBA (2024). *Sovereign Cloud Stack Technical Documentation*. Berlin: OSBA. https://docs.scs.community. Lizenz: Apache 2.0.

[12] Decidim Association (2021). *Decidim: Free Open-Source Participatory Democracy*. Barcelona: Decidim Association. https://decidim.org. Lizenz: AGPL-3.0.

[13] Nextcloud GmbH (2023). *Nextcloud for Government*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/. Lizenz: AGPL-3.0.

[14] The Matrix Foundation (2023). *Matrix Specification v1.9*. London: Matrix Foundation. https://spec.matrix.org. Lizenz: Apache 2.0.

[15] Lathrop, D. & Ruma, L. (Hrsg.) (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O'Reilly Media. ISBN 978-0-596-80435-0.

[16] E-Government Suisse (2023). *Strategie E-Government Schweiz 2024–2027*. Verabschiedet am 22. November 2023. Bern: Schweizerische Eidgenossenschaft. https://egovernment.ch. Lizenz: offener Zugang.

[17] eCH-Verein (2023). *eCH-Standards für E-Government Schweiz*. Zürich: eCH. https://ech.ch. Lizenz: CC-BY-4.0.

[18] AKDB (2023). *IT-Services für Kommunen in Bayern*. München: AKDB. https://akdb.de.

[19] TYPO3 Association (2023). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org. Lizenz: GPL-2.0.

[20] OpenProject GmbH (2023). *OpenProject for Government*. Berlin: OpenProject GmbH. https://openproject.org. Lizenz: GPLv3.

[21] Keycloak Community / Red Hat (2023). *Keycloak: Open Source Identity and Access Management*. https://keycloak.org. Lizenz: Apache 2.0.

[22] CKAN Association (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org. Lizenz: AGPL-3.0.

[23] govdigital eG (2023). *Genossenschaft für digitale Verwaltung*. Berlin: govdigital. https://govdigital.de.

[24] Dataport AöR (2023). *IT-Dienstleister für die öffentliche Verwaltung*. Altenholz: Dataport. https://dataport.de.

[25] ZenDiS GmbH (2024). *Zentrum für Digitale Souveränität — Jahresbericht 2023*. Berlin: ZenDiS. https://zendis.de.

[26] BSI (2023). *IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://bsi.bund.de. Lizenz: CC-BY-ND 3.0 DE.

[27] Europäisches Parlament und Rat (2022). *Richtlinie (EU) 2022/2555 — NIS2-Richtlinie*, ABl. L 333/80, 27. Dezember 2022. https://eur-lex.europa.eu. Lizenz: EU-Gesetzgebung (gemeinfrei).

[28] Europäische Kommission / Joinup (2023). *OSOR Annual Review 2023*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor. Lizenz: CC-BY-4.0.

[29] UN DESA (2022). *UN E-Government Survey 2022*. New York: Vereinte Nationen. https://publicadministration.un.org. Lizenz: UN Open Access.

[30] Janowski, T. (2015). Digital government evolution. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001.

[31] GovStack Initiative / ITU & DIAL (2023). *GovStack Building Blocks Specification v1.0*. Genf: ITU. https://govstack.global. Lizenz: CC-BY-SA-4.0.

[32] Bundesverwaltungsamt / BMI (2023). *Föderales Informationsmanagement (FIM)*. Köln: BVA. https://bva.bund.de. Lizenz: DL-DE/Zero 2.0.

[33] Camunda Services GmbH (2023). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com. Lizenz: Apache 2.0.

[34] BigBlueButton Inc. (2023). *Open Source Web Conferencing*. Ottawa: BigBlueButton. https://bigbluebutton.org. Lizenz: LGPL-3.0.

[35] Jitsi Community (2023). *Jitsi Meet*. San Francisco: 8x8 / Jitsi Community. https://jitsi.org. Lizenz: Apache 2.0.

[36] OpenStreetMap Foundation (2023). *OpenStreetMap*. London: OSMF. https://openstreetmap.org. Lizenz: ODbL-1.0.

[37] QGIS Project (2023). *QGIS: A Free and Open Source Geographic Information System*. https://qgis.org. Lizenz: GPL-2.0+.

[38] Bundesamt für Justiz / Eidgenössische Kanzlei (2023). *Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (BGEID)*, SR 161.5. Bern: Schweizerische Eidgenossenschaft. https://fedlex.admin.ch. Lizenz: CC0.

[39] Cloud Native Computing Foundation (CNCF) (2023). *Kubernetes*. San Francisco: Linux Foundation. https://kubernetes.io. Lizenz: Apache 2.0.

[40] Consul Project / Ayuntamiento de Madrid (2023). *CONSUL Democracy*. Madrid: Ayuntamiento de Madrid. https://consulproject.org. Lizenz: AGPL-3.0.

[41] PostgreSQL Global Development Group (2023). *PostgreSQL*. https://postgresql.org. Lizenz: PostgreSQL Licence.

[42] ZenDiS GmbH / BMI (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. Berlin: ZenDiS. https://opendesk.eu. Lizenz: AGPL-3.0.

[43] Schweizerisches Bundesarchiv (BAR) (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://bar.admin.ch/bar/de/home/digitale-archivierung/gever.html. Lizenz: offener Zugang.

[44] opendata.swiss (2023). *Open Government Data Switzerland*. Bern: Schweizerisches Bundesarchiv / BFS. https://opendata.swiss. Lizenz: CC-BY-4.0 (Portal).

[45] Europäische Kommission, ISA²-Programm (2017). *European Interoperability Framework (EIF)*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu. Lizenz: CC-BY-4.0.

[46] KoSIT (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://xoev.de.

[47] Lucke, J. & Reinermann, H. (2000). *Speyerer Definition von Electronic Government*. Speyer: Forschungsinstitut für öffentliche Verwaltung. https://foev.dhv-speyer.de. Lizenz: offener Zugang.

[48] Bertot, J.C., Jaeger, P.T. & Grimes, J.M. (2010). Using ICTs to create a culture of transparency. *Government Information Quarterly*, 27(3), 264–271. https://doi.org/10.1016/j.giq.2010.04.003.

[49] OECD (2020). *The OECD Digital Government Policy Framework*. OECD Public Governance Policy Papers Nr. 02. Paris: OECD. https://doi.org/10.1787/f64fed2a-en.

[50] Bundesregierung Deutschland (2022). *Digitalstrategie Deutschland*. Berlin: Bundesregierung. https://digitalstrategie-deutschland.de. Lizenz: DL-DE/Zero 2.0.

[51] Europäische Kommission (2021). *2030 Digital Compass*, COM(2021) 118 final. Brüssel: Europäische Kommission. Lizenz: CC-BY.

[52] BSI (2022). *Mindeststandard des BSI zur Nutzung externer Cloud-Dienste*, Version 1.1. Bonn: BSI. https://bsi.bund.de. Lizenz: CC-BY-ND 3.0 DE.

[53] Joinup / Europäische Kommission (2023). *Open Source Observatory and Repository (OSOR)*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor. Lizenz: CC-BY-4.0.

[54] Dunleavy, P., Margetts, H., Bastow, S. & Tinkler, J. (2006). *Digital Era Governance*. Oxford: Oxford University Press. ISBN 978-0-19-929414-8.

[55] Scholl, H.J. (2017). Electronic government: A study domain past its zenith? *Information Polity*, 22(4), 313–329. https://doi.org/10.3233/IP-170417.

---

## Anhang A — Beschaffungscheckliste (23 Fragen)

| # | Frage | Ja | Teilweise | Nein |
|---|---|---|---|---|
| 1 | Ist die ausgeschriebene Komponente unter einer OSI-anerkannten Open-Source-Lizenz verfügbar? | | | |
| 2 | Ist der Quellcode öffentlich in einem zugänglichen Repository (z. B. GitHub, GitLab, openCode.de) verfügbar? | | | |
| 3 | Gibt es eine aktive Upstream-Community mit Commit-Aktivität innerhalb der letzten 12 Monate? | | | |
| 4 | Sind mindestens drei dokumentierte Produktiveinsätze in vergleichbaren Kommunalverwaltungen vorhanden? | | | |
| 5 | Unterstützt die Komponente die relevanten offenen Standards (XÖV, eCH, DCAT-AP, OGC, OIDC/SAML, BPMN 2.0)? | | | |
| 6 | Ist die Komponente mit BSI IT-Grundschutz kompatibel (oder kann sie es durch Härtung werden)? | | | |
| 7 | Erfüllt die Komponente WCAG 2.1 Level AA für alle bürgerorientierten Oberflächen? | | | |
| 8 | Sind gewerbliche Support-Verträge mit mindestens zwei unabhängigen Anbietern verfügbar? | | | |
| 9 | Werden Sicherheits-CVEs innerhalb definierter Fristen öffentlich veröffentlicht und gepatcht? | | | |
| 10 | Enthält der Vertrag eine vollständige, maschinenlesbare Datenexportklausel innerhalb von 30 Tagen? | | | |
| 11 | Enthält der Vertrag keine Exklusivitäts- oder Wechselgebührenklauseln? | | | |
| 12 | Ist maßgeschneiderte Entwicklung unter einer OSS-Lizenz veröffentlichungspflichtig (EMBAG Art. 9 oder gleichwertig)? | | | |
| 13 | Wurde eine mehrjährige TCO-Analyse durchgeführt, die Lizenz-, Betriebs-, Schulungs- und Migrationskosten umfasst? | | | |
| 14 | Wurde eine EIF-Interoperabilitätsbewertung (gemäß Interoperable Europe Act) abgeschlossen und dokumentiert? | | | |
| 15 | Ist die Komponente mit dem nationalen digitalen Identitätssystem kompatibel (BundID / Schweizer E-ID)? | | | |
| 16 | Kann die Komponente innerhalb der DE/CH/EU-Jurisdiktion auf SCS-zertifizierter Infrastruktur oder gleichwertiger gehostet werden? | | | |
| 17 | Ist die Datenschutz-Folgenabschätzung (DSFA) gemäß DSGVO Art. 35 dokumentiert, wo erforderlich? | | | |
| 18 | Unterstützt die Komponente mandantenfähige oder föderierte Architekturen für interkommunale Nutzung? | | | |
| 19 | Ist das Governance-Modell der Community (Stiftung, Konsortium oder Single-Vendor) dokumentiert und akzeptabel? | | | |
| 20 | Gibt es einen definierten Migrationspfad weg von der Komponente, wenn zukünftige Ablösung erforderlich ist? | | | |
| 21 | Ist die Komponente in relevanten OSOR-Fallstudien oder Joinup-Lösungskatalogen verzeichnet? | | | |
| 22 | Ist das Schulungs- und Dokumentationsökosystem ausreichend für den kommunalen Eigenbetrieb? | | | |
| 23 | Ist die Komponente auf der Negativliste des BMI oder anderen restriktiven Beschaffungslisten aufgeführt (ausschließen wenn ja)? | | | |

---

## Anhang B — Technologiebewertungs-Bewertungsmethodik

### B.1 Bewertungskriterien

Jede Technologiekomponente wird anhand von sieben Kriterien auf einer Skala von 1 (unzureichend) bis 5 (hervorragend) bewertet. Das gewichtete Gesamtergebnis ergibt sich aus den nachfolgend aufgeführten Gewichtungen.

| Kriterium | Gewichtung | Beschreibung |
|---|---|---|
| Lizenzoffenheit | 15 % | OSI-anerkannte Lizenz; keine proprietären Einschränkungen; Copyleft-Verträglichkeit |
| Einsatzreife | 20 % | Produktivitätsnachweise in vergleichbaren Umgebungen; Versionsstabilität; Upgrade-Pfade |
| Community-Gesundheit | 15 % | Commit-Aktivität; Anzahl der Mitwirkenden; Governance-Modell; Reaktionsfähigkeit |
| Interoperabilität | 20 % | Unterstützung offener Standards; API-Verfügbarkeit; Datenaustauschfähigkeit |
| Sicherheit | 15 % | CVE-Verwaltungsprozess; BSI-Kompatibilität; Verschlüsselungsstandards; Audit-Protokollierung |
| Gesamtbetriebskosten | 10 % | Lizenzkosten; Implementierungsaufwand; laufende Betriebskosten; Schulungsbedarf |
| Einsätze im öffentlichen Sektor | 5 % | Dokumentierte Referenzen in europäischen Gemeindeverwaltungen |

### B.2 Komponentenbewertungen

| Komponente | Lizenz | Lizenzoff. | Einsatzreife | Comm.-Gesd. | Interop. | Sicherheit | TCO | Öff.-Sektor | Gesamt |
|---|---|---|---|---|---|---|---|---|---|
| Keycloak | Apache 2.0 | 5,0 | 4,5 | 4,5 | 5,0 | 4,5 | 4,5 | 5,0 | **4,70** |
| SCS | Apache 2.0 | 5,0 | 4,0 | 4,0 | 4,5 | 4,5 | 4,0 | 4,5 | **4,40** |
| Matrix/Synapse | Apache 2.0 | 5,0 | 4,0 | 4,5 | 5,0 | 4,5 | 3,5 | 4,0 | **4,35** |
| CKAN | AGPL-3.0 | 4,5 | 4,5 | 4,0 | 5,0 | 4,0 | 4,5 | 5,0 | **4,25** |
| Nextcloud | AGPL-3.0 | 4,5 | 4,5 | 4,0 | 4,0 | 4,0 | 4,5 | 4,5 | **4,20** |
| TYPO3 | GPL-2.0 | 4,5 | 4,5 | 4,0 | 4,0 | 4,0 | 4,0 | 5,0 | **4,20** |
| Camunda (Community) | Apache 2.0 | 4,5 | 4,5 | 3,5 | 4,5 | 4,0 | 4,0 | 4,0 | **4,20** |
| QGIS | GPL-2.0+ | 5,0 | 5,0 | 4,5 | 5,0 | 4,5 | 5,0 | 5,0 | **4,85** |
| Decidim | AGPL-3.0 | 4,5 | 4,0 | 4,0 | 3,5 | 3,5 | 4,0 | 4,5 | **3,90** |
| BigBlueButton | LGPL-3.0 | 4,0 | 4,0 | 3,5 | 4,0 | 4,0 | 4,0 | 3,5 | **3,90** |
| OpenProject | GPLv3 | 4,5 | 4,0 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | **3,65** |

### B.3 Bewertungshinweise

- Bewertungen basieren auf dem Stand der Upstream-Projekte Mitte 2026.
- Gewichtungen spiegeln kommunale Prioritäten wider: Interoperabilität und Einsatzreife werden am stärksten gewichtet.
- QGIS erhält die höchste Gesamtbewertung (4,85) aufgrund seiner außergewöhnlichen Reife, des aktiven Communities und der breiten Unterstützung offener Standards.
- Keycloak erhält die zweithöchste Bewertung (4,70) aufgrund der kritischen Bedeutung seiner Identitätsfunktion und der starken Community.
- OpenProject erhält die niedrigste Bewertung (3,65) aufgrund begrenzter öffentlicher Sektor-Referenzen im Vergleich zu Alternativlösungen; es bleibt jedoch empfehlenswert in Kombination mit Nextcloud.

---

## Anhang C — Kommunale Selbstbewertung zur digitalen Souveränität

### Anweisungen

Beantworten Sie jede Frage mit einem der folgenden Werte:
- **3** = Vollständig erfüllt / vorhanden
- **2** = Teilweise erfüllt / in Entwicklung
- **1** = Minimal vorhanden / geplant
- **0** = Nicht vorhanden / nicht geplant

Summieren Sie alle Punkte. Maximale Punktzahl: 45.

**Auswertung:**
- 36–45: Hohe digitale Souveränität — fortgeschrittene Commune, Peer-Sharing empfohlen
- 27–35: Mittlere digitale Souveränität — solide Grundlage, gezielte Verbesserungen erforderlich
- 18–26: Niedrige digitale Souveränität — strukturelle Defizite, strategische Priorisierung erforderlich
- 0–17: Kritische digitale Abhängigkeit — dringende strategische Intervention empfohlen

### Bewertungsfragen

| # | Bereich | Frage | Punkte (0–3) |
|---|---|---|---|
| 1 | Governance | Verfügt die Gemeinde über eine schriftliche digitale Souveränitäts- oder OSS-Strategie, die vom Gemeinderat verabschiedet wurde? | |
| 2 | Governance | Gibt es einen benannten CIO oder IT-Verantwortlichen mit explizitem Mandat für Souveränitätsfragen? | |
| 3 | Infrastruktur | Wird die primäre IT-Infrastruktur auf Servern innerhalb der DE/CH/EU-Jurisdiktion betrieben? | |
| 4 | Infrastruktur | Sind die Hosting-Anbieter nach SCS oder vergleichbaren souveränen Standards zertifiziert oder betreibt die Gemeinde eigene Infrastruktur? | |
| 5 | Software | Welcher Anteil der eingesetzten Software ist unter OSI-anerkannten Lizenzen lizenziert? (0=<25 %, 1=25–49 %, 2=50–74 %, 3=≥75 %) | |
| 6 | Software | Werden proprietäre Software-Abhängigkeiten aktiv reduziert durch einen dokumentierten Migrationsplan? | |
| 7 | Identität | Ist die digitale Identitätsverwaltung auf einer selbst betriebenen oder kooperativ betriebenen IAM-Plattform realisiert? | |
| 8 | Identität | Ist die Gemeinde mit dem nationalen Identitätssystem (BundID / Schweizer E-ID) föderiert oder plant die Föderierung? | |
| 9 | Daten | Verfügt die Gemeinde über ein dokumentiertes Dateninventar aller personenbezogenen Daten und deren Speicherorte? | |
| 10 | Daten | Betreibt die Gemeinde ein öffentliches Open-Data-Portal (z. B. CKAN) mit mindestens 20 Datensätzen? | |
| 11 | Sicherheit | Ist ein IT-Grundschutz-konformes oder gleichwertiges ISMS implementiert und dokumentiert? | |
| 12 | Sicherheit | Gibt es einen NIS2-konformen Vorfallreaktionsplan mit definierten 24h-Meldeprozeduren? | |
| 13 | Beschaffung | Enthalten alle IT-Verträge Datenportabilitäts- und Ausstiegsklauseln (vollständiger Export in offenem Format innerhalb von 30 Tagen)? | |
| 14 | Interoperabilität | Unterstützen alle bürgerorientierten Dienste die relevanten offenen Standards (XÖV, eCH, OIDC, DCAT-AP)? | |
| 15 | Partizipation | Betreibt die Gemeinde eine digitale Bürgerbeteiligungsplattform (z. B. Decidim, CONSUL) für partizipative Prozesse? | |

**Gesamtpunktzahl: ___ / 45**

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Licence (CC-BY-4.0) veröffentlicht.*
*Quellenangabe: Sebastian Graf, Autonomous Office of Civil Digital Infrastructure (sebk4c@tuta.com)*