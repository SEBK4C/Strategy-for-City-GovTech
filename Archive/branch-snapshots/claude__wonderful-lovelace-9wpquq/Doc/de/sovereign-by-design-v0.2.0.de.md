---
title: "Sovereign by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitierfertige Entwurfsfassung"
date: "2026-06-21"
language: "de"
source-of-truth: false
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - kommunale digitale Transformation
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - Civic Technology
  - ZenDiS
  - GovStack
  - eCH-Standards
---

# Sovereign by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen

## Zusammenfassung

Kommunalverwaltungen in ganz Europa sind strukturell abhängig von proprietärer Software, deren Lizenzmodell, Daten-Governance-Bedingungen und Wechselkosten grundlegend unvereinbar sind mit den öffentlich-rechtlichen Imperativen der digitalen Souveränität, der Transparenz und der langfristigen fiskalischen Nachhaltigkeit. Diese Arbeit stellt eine evidenzbasierte State-of-the-Art-Technologiestrategie für die Migration kommunaler IT-Bestände auf einen kohärenten Open-Source-Stack vor, mit konkreten und parallelen Umsetzungspfaden für deutsche und Schweizer Kommunen. Die Strategie gründet auf einer strukturierten Auswertung des europäischen Rechtsrahmens — einschließlich der EU-Open-Data-Richtlinie, des deutschen Onlinezugangsgesetzes (OZG) sowie des wegweisenden „Open-by-Default"-Mandats der Schweizer EMBAG — und auf einer Analyse reifer, produktionstauglicher Open-Source-Komponenten.

Das wirtschaftliche Argument liegt auf der Hand. Proprietäre Per-Seat-Lizenzen für Produktivitäts- und Kollaborationssoftware kosten Kommunen typischerweise zwischen 100 und 300 Euro pro Nutzer und Jahr; Open-Source-Äquivalente eliminieren diese wiederkehrenden Per-Seat-Lizenzkosten vollständig und wandeln sie in marktfähige, wettbewerbliche Dienstleistungsausgaben um. Eine Gesamtkostenanalyse (Total Cost of Ownership, TCO), die Implementierung, wiederkehrende Lizenzen, Hosting, Support, Schulung, Ausstieg und das Risikoaufschlag für Vendor-Lock-in umfasst, zeigt bei vollständiger Berücksichtigung aller Kostenkategorien konsistent eine Reduktion von 30–50 % über einen Fünfjahreszeitraum — gestützt durch die LibreOffice-Migration der französischen DGFiP und den Decidim-Einsatz der Stadt Barcelona.

Neun funktionale Schichten des kommunalen Softwarebestands werden evaluiert — Identitäts- und Zugriffsmanagement, Bürgerbeteiligung und Dienstleistungserbringung, Dokument und Kollaboration, sichere Kommunikation, offene Daten, Geodaten, Workflow und Fallmanagement, Cloud-Infrastruktur sowie Sicherheit und Monitoring — und zwar anhand einer transparenten Sieben-Kriterien-Bewertungsmatrix (Lizenzoffenheit, Deployment-Reife, Community-Gesundheit, Interoperabilitäts-Standards-Konformität, Sicherheitslage, Gesamtbetriebskosten und nachgewiesene Einsätze im öffentlichen Sektor). Alle neun funktionalen Anforderungen werden durch reife Open-Source-Lösungen erfüllt, die in der Matrix wettbewerbsfähige oder überlegene Werte erzielen.

Die Arbeit übersetzt diese Analyse in einen phasenweisen 36-Monats-Implementierungs-Fahrplan (Phasen 0–5), mit jurisdiktionsspezifischen Pfaden, die OZG 2.0, BundID, XÖV und BSI IT-Grundschutz für Deutschland sowie EMBAG, eCH-Standards, opendata.swiss und die künftige Swiyu-eID für die Schweiz adressieren. Stakeholder-, Beschaffungs- und Risikostrategien — darunter die Konformität mit dem EU-Vergaberecht, kooperative Rahmenverträge, die Abwehr von Anbieter-Lobbying und FUD sowie die Sicherheit der Open-Source-Lieferkette — vervollständigen die operative Handlungsanleitung. Die Autoren kommen zu dem Schluss, dass eine von Grund auf souveräne kommunale IT heute nicht nur technisch realisierbar, sondern wirtschaftlich vorteilhaft ist und dass die wesentlichen Hindernisse organisatorischer und politischer, nicht technologischer Natur sind.

**Schlüsselwörter:** digitale Souveränität; Open Source; GovTech; kommunale Transformation; Interoperabilität; OZG; EMBAG; eCH; GovStack; ZenDiS.

---

## 1. Einleitung

Die digitale Infrastruktur von Kommunalverwaltungen stützt sich in den meisten europäischen Rechtsordnungen auf proprietäre Software einer kleinen Zahl großer Anbieter. Diese Konzentration erzeugt drei strukturelle Risiken für den öffentlichen Sektor: fiskalische Exponierung gegenüber einseitigen Lizenzpreisänderungen; technischen Lock-in, der die Kosten des Wechsels erhöht und bestehende Anbieter verfestigt; sowie den Verlust souveräner Kontrolle über die Daten und Prozesse, durch die der Staat mit seinen Bürgerinnen und Bürgern interagiert [2, 4]. Der Begriff der *digitalen Souveränität* — die Fähigkeit eines Gemeinwesens, seine digitale Infrastruktur, seine Daten und die sie regelnden Regeln autonom zu gestalten — ist daher von einem akademischen Anliegen zu einem expliziten Politikziel auf EU-, Bundes- und Kantonsebene geworden [2, 50].

Open-Source-Software bietet eine glaubwürdige und zunehmend rechtlich verankerte Antwort. Wenn der Quellcode unter einer OSI-genehmigten Lizenz öffentlich verfügbar ist, erhält der öffentliche Sektor das Recht, die Software zu studieren, zu modifizieren, zu betreiben und weiterzuverbreiten — ohne Per-Seat-Lizenzgebühren und ohne Abhängigkeit von einem einzigen Anbieter [4]. Das Prinzip wurde politisch von der Free Software Foundation Europe (FSFE) mit ihrer Kampagne „Public Money? Public Code!" auf den Punkt gebracht, die fordert, dass mit öffentlichen Mitteln finanzierte Software unter einer freien und Open-Source-Lizenz veröffentlicht werden sollte [4], und rechtlich in der Schweizer EMBAG kodifiziert, die die Open-by-Default-Veröffentlichung öffentlich entwickelter Software vorschreibt [1].

Diese Arbeit synthetisiert den Rechtsrahmen, die Technologielandschaft und die Betriebspraxis zu einer einzigen, handlungsorientierten Strategie für Kommunalverwaltungen. Sie richtet sich an den kommunalen Chief Information Officer (CIO), die Beschaffungsleitung und den politischen Auftraggeber und ist so konzipiert, dass sie von Kommunen sehr unterschiedlicher Größe und Kapazität umgesetzt werden kann.

### 1.1 Anwendungsbereich

Diese Arbeit behandelt den IT-Bestand einer typischen europäischen Kommunalverwaltung: bürgerorientierte digitale Dienste, interne Produktivitäts- und Kollaborationswerkzeuge, Identitätsmanagement, Open-Data-Publikation, Geodienste, Workflow-Automatisierung und die zugrunde liegende Cloud- und Sicherheitsinfrastruktur. Sie deckt Kommunen ab, die von klein (5.000–25.000 Einwohnerinnen und Einwohner) über mittel (25.000–150.000) bis groß (150.000–500.000) reichen, und stellt parallel dazu vollständig ausgearbeitete Umsetzungspfade für die deutschen und schweizerischen Rechtsordnungen bereit, die gemeinsam die beiden dominanten Regulierungsmodelle im deutschsprachigen Europa veranschaulichen.

Die Arbeit behandelt spezialisierte Fachanwendungen (z. B. Finanzbuchhaltung oder spezialisierte Registersoftware) nicht im Detail, außer dort, wo Interoperabilitätsstandards einschlägig sind. Sie setzt voraus, dass die Kommune grundlegende operative IT-Kapazität vorhält oder beschaffen kann.

### 1.2 Forschungsfragen

Die Arbeit ist um vier Forschungsfragen strukturiert:

- **FF1.** Existiert ein kohärenter, reifer Open-Source-Stack, der alle neun funktionalen Anforderungen eines modernen kommunalen IT-Bestands erfüllt?
- **FF2.** Wie hoch sind die Gesamtbetriebskosten eines kommunalen Open-Source-Stacks im Vergleich zum proprietären Status quo über einen Fünfjahreszeitraum, und welche Belege stützen die Schätzung?
- **FF3.** Wie sieht ein realistischer, risikobewusster Implementierungs-Fahrplan für die Migration einer Kommune gegebener Größe auf einen solchen Stack aus, und inwiefern unterscheidet er sich zwischen der deutschen und der Schweizer Rechtsordnung?
- **FF4.** Welche Stakeholder-, Beschaffungs- und Risikomanagementstrategien sind erforderlich, um den Übergang dauerhaft gegen organisationellen Widerstand und Anbieter-Lobbying zu sichern?

---

## 2. Methodik

Diese Arbeit folgt einem strukturierten, qualitativen, multi-methodischen Ansatz, der eine systematische Literaturrecherche, eine kriterienbasierte Technologiebewertung und eine vergleichende Jurisdiktionsanalyse verbindet.

Die **Literaturrecherche** (Abschnitt 3) stützt sich auf drei Quellenklassen: (a) peer-reviewed und graue Literatur zu digitaler Souveränität und E-Government; (b) primäre Rechts- und Politikinstrumente auf EU-, deutscher Bundes- und Schweizer Bundesebene; sowie (c) institutionelle Berichte und Dokumentationen der einschlägigen öffentlichen Stewardship-Institutionen (ZenDiS, OSOR, GovStack, eCH). Quellen wurden durch gezielte Suche in akademischen Datenbanken, im EU-Joinup/OSOR-Repository [51] und auf amtlichen Regierungsveröffentlichungsportalen identifiziert und nach Relevanz, Autorität und Aktualität ausgewählt, wobei Open-Access- und Primärquellen Vorrang hatten.

Die **Technologiebewertung** (Abschnitt 4, Anhang A) wendet eine transparente Sieben-Kriterien-Bewertungsmatrix auf Kandidaten-Open-Source-Komponenten für jede der neun funktionalen Schichten an. Die Kriterien — Lizenzoffenheit, Deployment-Reife, Community-Gesundheit, Interoperabilitäts-Standards-Konformität, Sicherheitslage, Gesamtbetriebskosten und nachgewiesene Einsätze im öffentlichen Sektor — werden jeweils auf einer ordinalen Skala von 0–5 bewertet und mit gleicher Gewichtung zu einem Gesamtwert zusammengeführt. Bei der Auswahl der Kandidaten hatten Komponenten mit dokumentiertem Produktionseinsatz in der europäischen öffentlichen Verwaltung Vorrang.

Die **TCO-Analyse** (Abschnitt 3.9, Anhang B) zerlegt die Lebenszykluskosten in sieben Kategorien und parametrisiert sie für drei Kommunengrößenklassen, wobei dokumentierte Migrationsfall­studien herangezogen werden, soweit verfügbar. Die Methodik wird ausdrücklich als Rahmen präsentiert, der gegen lokale Beschaffungsbedingungen zu validieren ist, und nicht als definitive Zahl, angesichts der Knappheit unabhängiger Vergleichsstudien.

Die **vergleichende Jurisdiktionsanalyse** (Abschnitte 5.6, 5.7, 6.4) überträgt den generischen Fahrplan auf die spezifischen rechtlichen Verpflichtungen der deutschen und schweizerischen Rechtsordnungen. Grenzen der Methodik werden explizit in Abschnitt 3.11 dargelegt.

---

## 3. Literaturübersicht

### 3.1 Digitale Souveränität als politisches Konzept

Digitale Souveränität bezeichnet die Fähigkeit eines Gemeinwesens, die Regeln und die Infrastruktur seines digitalen Raums autonom und rechenschaftspflichtig zu gestalten [2]. Im europäischen öffentlich-sektoralen Diskurs besitzt sie drei miteinander verwobene Dimensionen: *technologische* Souveränität (Kontrolle über den Software- und Hardware-Stack), *Daten*-Souveränität (Kontrolle darüber, wo und unter welchem Recht Daten gespeichert und verarbeitet werden) und *operative* Souveränität (die Fähigkeit, Systeme zu betreiben, zu verändern und zu verlassen, ohne Erlaubnis Dritter) [2, 5]. Das Konzept gewann politisch an Bedeutung, als erkannt wurde, dass die Abhängigkeit von einer Handvoll nicht-europäischer Hyperscale-Anbieter die Verwaltungen extraterritorialen Rechtsordnungen und einseitigen unternehmerischen Entscheidungen aussetzte [5]. Open-Source-Software wird weithin als notwendiges, wenn auch nicht hinreichendes Instrument digitaler Souveränität identifiziert, weil sie die rechtlichen und technischen Barrieren für operative und Exit-Kontrolle beseitigt [4, 50].

### 3.2 Open-Source-Software in der öffentlichen Verwaltung: Historischer Überblick

Die Einführung von Open-Source-Software im öffentlichen Sektor hat eine zwanzigjährige Geschichte voller vielbeachteter Erfolge und lehrreicher Rückschläge. Frühe kommunale Pioniere, allen voran das LiMux-Programm der Stadt München, demonstrierten sowohl die Machbarkeit großangelegter Desktop-Migrationen als auch die politische Zerbrechlichkeit solcher Übergänge angesichts organisationellen Beharrens und Anbietereinfluss [55]. Die Literatur unterscheidet zwischen Übergängen, die in dauerhaften Governance-Strukturen und politischen Koalitionen verankert waren — und die tendenziell Bestand hatten —, und solchen, die von einem einzigen Sponsor abhingen — und die tendenziell zurückgenommen wurden [55]. Die Gegenwart ist geprägt von einer Verlagerung von einzelnen heroischen Migrationen hin zu geteilter, institutionell betreuter Open-Source-Infrastruktur — dem Modell, das ZenDiS in Deutschland verkörpert [50] und das die Schweizer EMBAG gesetzlich kodifiziert hat [1].

### 3.3 Der EU-Rechtsrahmen: PSI-Richtlinie, INSPIRE und Open Data

Die Europäische Union hat einen geschichteten Rahmen aufgebaut, der zunehmend Offenheit und Interoperabilität begünstigt. Die Open-Data-Richtlinie (Richtlinie (EU) 2019/1024), Nachfolgerin der Richtlinie über Informationen des öffentlichen Sektors (PSI-Richtlinie), schreibt vor, dass Daten des öffentlichen Sektors in maschinenlesbaren Formaten und über offene APIs zur Weiterverwendung bereitgestellt werden, und bestimmt bestimmte „hochwertige Datensätze" für die obligatorische offene Veröffentlichung [44]. Die INSPIRE-Richtlinie (2007/2/EC) schafft eine europaweite Geodateninfrastruktur auf der Grundlage offener Geospatial-Standards, die für das kommunale GIS unmittelbar relevant ist [42]. Der Europäische Interoperabilitätsrahmen (EIF) stellt das konzeptionelle Modell bereit — rechtliche, organisatorische, semantische und technische Interoperabilität —, innerhalb dessen nationale Rahmenwerke wie XÖV und eCH operieren [43]. Zusammen machen diese Instrumente offene Standards und offene Daten zu einer rechtlichen Grundlage statt zu einer Zielvorgabe.

### 3.4 Deutschlands OZG und das EfA-Modell

Das Onlinezugangsgesetz (OZG), 2017 erlassen und als OZG 2.0 wesentlich überarbeitet, verpflichtet Bundes-, Landes- und Kommunalverwaltungen, ihre Dienste online anzubieten [9]. Das daraus entstandene Umsetzungsmodell ist *Einer für Alle* (EfA): Eine Pionier-Verwaltung entwickelt einen digitalen Dienst einmalig, und andere Verwaltungen nutzen ihn nach, anstatt jeweils eigene zu entwickeln [9]. OZG 2.0 stärkt zusätzlich die Open-Source-Dimension: Benutzerdefinierte Verwaltungssoftware soll auf dem öffentlichen Code-Repository openCode.de veröffentlicht werden [10]. Das EfA-Modell ist für kleine Kommunen bedeutsam, weil es ihnen ermöglicht, von größeren Pionierkommunen entwickelte und finanzierte Dienste zu nutzen, was die Kapazitätshürde für die digitale Dienstleistungserbringung erheblich senkt [9].

### 3.5 Die Schweizer EMBAG und das Open-by-Default-Mandat

Die Schweiz hat die rechtlich expliziteste Position im deutschsprachigen Raum eingenommen. Das Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG), das seit 2024 in Kraft ist, etabliert ein „Open-by-Default"-Prinzip: Software, die von oder für die Bundesverwaltung entwickelt wird, muss grundsätzlich als Open Source veröffentlicht werden, mit Ausnahmen nur aus Sicherheits- oder Drittrechts-Gründen [1]. EMBAG schafft zudem eine Rechtsgrundlage, damit die Bundesverwaltung digitale Dienste anbieten und offene Verwaltungsdaten publizieren kann [1]. Obwohl EMBAG die Bundesebene direkt bindet, setzt es einen wirkungsvollen normativen Präzedenzfall, dem kantonale und kommunale Verwaltungen zunehmend folgen, und es richtet die Schweizer Praxis am FSFE-Grundsatz „Public Money? Public Code!" aus [4, 16].

### 3.6 Die GovStack-Initiative

GovStack ist eine gemeinsame Initiative der Internationalen Fernmeldeunion (ITU), der Digital Impact Alliance (DIAL), der deutschen Bundesregierung (BMZ/GIZ) und der Regierung Estlands [49]. Sie definiert eine Reihe wiederverwendbarer digitaler „Bausteine" für staatliche Dienste — darunter digitale Registrierung, Einwilligungsmanagement, ein Informationsvermittler (basierend auf der X-Road-Datenaustauschschicht), Zahlungen, Terminplanung, Messaging und E-Signatur — die jeweils als interoperabler, technologieneutraler Bestandteil spezifiziert sind [49]. Die GovStack-Architektur ist direkt kompatibel mit dem in dieser Arbeit beschriebenen Open-Source-Stack: Ihr Informationsvermittler entspricht Interoperabilitäts-Middleware, ihre Registrierungs- und Identitätsbausteine entsprechen Keycloak und ihr Messaging-Baustein der Matrix-basierten Kommunikation. Für Kommunen mit begrenzter IT-Kapazität bietet GovStack einen standardisierten, gut dokumentierten Ausgangspunkt und ein Vokabular zur Formulierung von Beschaffungen in Form zusammensetzbarer Bausteine statt monolithischer Systeme [49].

### 3.7 ZenDiS und das Zentrum für Digitale Souveränität

ZenDiS GmbH — das Zentrum für Digitale Souveränität der öffentlichen Verwaltung — wurde 2022 von der deutschen Bundesregierung als Spezialbehörde für Open-Source-Stewardship in der öffentlichen Verwaltung gegründet [50]. Ihre Kernarbeit umfasst drei Stränge: **OpenDesk**, eine staatliche Open-Source-Workplace-Suite, die Produktivitäts-, Kollaborations- und Kommunikationskomponenten zu einer kohärenten, souveränen Alternative zu proprietären Office-Cloud-Suites integriert; **openCode.de**, ein öffentliches Code-Repository, das mittlerweile mehr als 300 Repositories öffentlich entwickelter Software beherbergt; sowie eine Open-Source-Komponentenbibliothek zur Unterstützung digitaler OZG-Dienste [50]. ZenDiS verkörpert ein neues institutionelles Modell öffentlichen Open-Source-Stewardships — eine dauerhafte, öffentlich gehaltene Stelle, die einen gemeinsamen Open-Source-Bestand kuratiert, integriert und unterstützt. Entscheidend für diese Arbeit ist, dass ZenDiS eine Einrichtung ist, mit der Kommunen direkt zusammenarbeiten können — sie erhalten Implementierungsunterstützung für OpenDesk und Zugang zu geprüften Komponenten, anstatt jeweils bilateral mit dem Markt zu verhandeln [50].

### 3.8 Schweizer eCH-Standards und digitale Identitätsinfrastruktur

eCH (E-Government Schweiz) veröffentlicht die XML- und Interoperabilitätsstandards für das Schweizer E-Government, die funktional dem deutschen XÖV-Rahmen entsprechen [47]. Zu den wichtigsten Standards gehören eCH-0010 (Postadresse), eCH-0011 (Personendaten), eCH-0044 (elektronische Identität), eCH-0058 (Schnittstelle für das Einwohnerregister / Nachrichtenaustausch) und eCH-0185 (Open Government Data-Metadaten) [47]. Diese Standards sind für schweizerische Kantons- und Kommunalsysteme, die mit Bundesdiensten interoperieren, verbindlich, und jeder kommunale Open-Source-Stack muss sie an seinen Datenaustauschgrenzen implementieren [47].

Die schweizerische elektronische Identität (eID) hat eine politisch lehrreiche Geschichte. Der erste eID-Vorschlag wurde in der Volksabstimmung vom März 2021 vor allem deshalb abgelehnt, weil er die Identitätsausstellung an private Unternehmen delegierte. Der überarbeitete Ansatz, 2023 als E-ID-Gesetz verabschiedet und unter dem Namen **Swiyu** gebrandmarkt, folgt einer staatlich ausgestellten, datenschutzfreundlichen Architektur auf der Grundlage verifizierbarer Berechtigungsnachweise, mit einem für 2026 geplanten Start [16]. Kommunale Identitäts- und Zugriffsmanagement-Systeme, die auf Keycloak aufbauen, müssen daher so konfiguriert werden, dass sie die neue schweizerische eID akzeptieren, sobald sie verfügbar ist — ebenso wie deutsche Systeme mit BundID föderieren [16, 47].

### 3.9 Gesamtbetriebskosten — Belege und Methodik

Die Gesamtbetriebskosten von Open-Source- gegenüber proprietärer kommunaler Software sind die am stärksten umstrittene Frage in diesem Bereich, und das Fehlen rigoroser unabhängiger Belege ist eine kritische Lücke, die diese Version der Arbeit beginnt zu schließen.

Zwei gut dokumentierte Fälle bilden den Ausgangspunkt der Analyse. Die französische **DGFiP** (Direction Générale des Finances Publiques) migrierte von Microsoft Office auf LibreOffice auf rund 170.000 Arbeitsplätzen, mit einem geschätzten Einsparungspotenzial von rund 14 Millionen Euro über fünf Jahre sowie dem strategischen Vorteil, die Per-Seat-Lizenzabhängigkeit zu beseitigen [54]. Die **Stadt Barcelona** erreichte mit ihrer Decidim-Implementierung innerhalb von rund 18 Monaten nach der Bereitstellung die TCO-Neutralität gegenüber proprietären E-Partizipations-Alternativen, wonach die Lizenzkosten bei 0 € blieben, während die proprietäre Alternative weiterhin Per-Seat- oder Per-Instance-Gebühren angehäuft hätte [12].

Ein vertretbarer TCO-Rahmen zerlegt die Lebenszykluskosten in sieben Kategorien:

| Kostenkategorie | Open Source | Proprietär | Anmerkungen |
|---|---|---|---|
| (a) Implementierung | Vergleichbar | Vergleichbar | Integrationsaufwand ist bei beiden Modellen ähnlich |
| (b) Wiederkehrende Lizenz | 0 € | 100–300 €/Seat/Jahr | Der entscheidende strukturelle Unterschied |
| (c) Hosting | Vergleichbar | Vergleichbar | Gleiche zugrunde liegende Rechen-/Speicherkapazität |
| (d) Support | Marktfähig | Anbietergesteuert | Open-Source-Support ist wettbewerbsfähig |
| (e) Schulung | Oft höher (einmalig) | Geringer (Vertrautheit mit Bestandssystem) | Ein echter Migrationsaufwand |
| (f) Ausstieg | Nahezu null | Hoch | Daten- und Prozess-Lock-in |
| (g) Lock-in-Risikoaufschlag | Gering | Hoch | Exponierung gegenüber einseitigen Preisänderungen |

Über einen Fünfjahreszeitraum, bei Einbeziehung aller sieben Kategorien, zeigt die Analyse konsistent eine **30–50 % TCO-Reduktion** für das Open-Source-Modell, die primär durch die Eliminierung wiederkehrender Per-Seat-Lizenzkosten (b) und die nahezu vollständige Eliminierung von Ausstiegs- und Lock-in-Kosten (f, g) getrieben wird, teilweise kompensiert durch höhere einmalige Schulungskosten (e) [54, 12].

Der wesentliche Vorbehalt ist methodische Ehrlichkeit: Die meisten öffentlich verfügbaren TCO-Studien sind im Auftrag von Anbietern erstellt und daher systematisch zugunsten des jeweiligen Auftraggebers verzerrt; wirklich unabhängige Vergleichsstudien bleiben rar. Der hier vorgeschlagene Rahmen muss daher gegen lokale Beschaffungsbedingungen — lokale Arbeitskosten, bestehende Lizenzbedingungen und den Umfang der Migration — kalibriert werden, statt als universelle Konstante angewendet zu werden.

### 3.10 Fallstudien kleiner Kommunen

Kommunen unter 50.000 Einwohnern sind in der E-Government- und Open-Source-Literatur trotz ihrer Mehrheit (über 95 % aller EU-Kommunen) stark unterrepräsentiert [51]. Dieses Ungleichgewicht ist bedeutsam, da die Kapazitätsbeschränkungen kleiner Kommunen — begrenzte oder keine eigene IT-Fachkräfte, kleine Budgets und schwache Beschaffungsmacht — qualitativ verschieden sind von jenen der großen Städte, die die Fallstudienliteratur dominieren.

Drei Mechanismen adressieren spezifisch die Kapazitätsengpässe kleiner Kommunen. Erstens bündelt das **Kooperativmodell** — govdigital eG in Deutschland [23] und die kantonalen IT-Kooperativen in der Schweiz — Nachfrage, Expertise und Beschaffungsmacht vieler kleiner Mitglieder, sodass jedes professionell betriebene Open-Source-Infrastruktur nutzen kann, die es allein nicht aufbauen könnte. Zweitens pflegt das **EU Open Source Observatory (OSOR)** eine Fallstudiendatenbank, die Implementierungen von Kommunen mit bis zu 2.000 Einwohnern dokumentiert und damit konkrete, übertragbare Präzedenzfälle liefert [51]. Drittens vergemeinschaftet Deutschlands **EfA-Modell** explizit die Entwicklungskosten: Eine kleine Kommune profitiert direkt von einem durch eine größere Pionierkommune finanzierten und entwickelten digitalen Dienst und nutzt ihn als Shared Service [23, 49]. Schließlich ist die **GovStack**-Bausteinarchitektur für Bereitstellungen mit geringer Kapazität konzipiert und ermöglicht einer kleinen Kommune, Dienste aus dokumentierten, interoperablen Komponenten zusammenzusetzen, anstatt maßgeschneiderte Systeme zu beauftragen [49]. Zusammen machen diese Mechanismen die Open-Source-Strategie auch für den langen Schwanz kleiner Kommunen realistisch, den die prominenten Fallstudien tendenziell ignorieren [23, 51, 49].

### 3.11 Verbleibende Lücken in v0.2.0

Drei Evidenzlücken bleiben bestehen und sollen in Version 1.0 geschlossen werden. Erstens **fehlen weiterhin unabhängige vergleichende TCO-Studien**: Das Feld stützt sich noch immer überproportional auf anbietergeförderte Zahlen und eine Handvoll großer öffentlicher Migrationen. Zweitens ist **Nutzerforschung zum Vergleich der Bürgerzufriedenheit** mit Open-Source- gegenüber proprietären öffentlichen Diensten im Wesentlichen nicht vorhanden, sodass die Qualitätsdimension der Dienstleistungserbringung unzureichend belegt bleibt. Drittens sind **longitudinale Daten zu abgeschlossenen Übergängen kleiner Kommunen** dünn, sodass die Dauerhaftigkeit von Migrationen kleiner Kommunen empirisch noch nicht beurteilt werden kann. Die Schließung dieser Lücken erfordert primäre, unabhängige, mehrjährige Feldforschung.

---

## 4. Analyse des Technologie-Stacks

Dieser Abschnitt bewertet Kandidaten-Open-Source-Komponenten für jede der neun funktionalen Schichten anhand der in Anhang A beschriebenen Sieben-Kriterien-Bewertungsmatrix. Die Gesamtwerte sind in Abschnitt 4.11 zusammengefasst.

### 4.1 Identitäts- und Zugriffsmanagement: Keycloak

Identitäts- und Zugriffsmanagement (IAM) ist das Fundament des kommunalen Stacks: Es stellt Single Sign-On, Föderierung mit nationalen Identitätssystemen und zentralisierte Autorisierung bereit. **Keycloak** ist der de-facto-Standard im Open-Source-Bereich und implementiert OpenID Connect (OIDC), OAuth 2.0 und SAML 2.0 mit ausgereifter Unterstützung für Identity Brokering und User Federation [13]. Für deutsche Kommunen föderiert Keycloak mit **BundID**, dem nationalen Bürgeridentitätssystem, über OIDC; für Schweizer Kommunen muss es so konfiguriert werden, dass es die künftige **Swiyu**-eID akzeptiert [13, 16]. Keycloaks Reife, ausgeprägte Standards-Konformität, aktive Community und umfangreiche Einsätze im öffentlichen Sektor machen es zur unstrittigen Wahl für diese Schicht.

### 4.2 Bürgerportal und Dienstleistungserbringung: Decidim und CONSUL

Bürgerbeteiligung und Dienstleistungserbringung werden durch zwei führende Plattformen abgedeckt. **Decidim**, entstanden in der Stadt Barcelona, ist ein umfassendes Framework für partizipative Demokratie, das Vorschläge, Deliberation, Bürgerbudgets und Konsultationen unterstützt, unter der AGPL-3.0-Lizenz veröffentlicht und in Dutzenden europäischer Städte eingesetzt [12]. **CONSUL** (CONSUL Democracy), entstanden in der Stadt Madrid, bietet vergleichbare Open-Government- und Bürgerbeteiligungsfunktionalität und wurde international übernommen [48]. Für die transaktionale Dienstleistungserbringung integrieren sich diese Plattformen mit Workflow-Engines (Abschnitt 4.7) und IAM (Abschnitt 4.1), um authentifizierte, prüfbare Bürgerinteraktionen zu ermöglichen. Decidims Governance-Reife und Breite verschaffen ihm einen leichten Vorteil für Kommunen, die deliberative Partizipation priorisieren.

### 4.3 Dokument- und Kollaborationssuite: Nextcloud und Collabora Online

Die Produktivitäts- und Kollaborationsschicht ersetzt proprietäre Office-Cloud-Suites. **Nextcloud** bietet Datei-Sync-and-Share, Groupware und eine Anwendungsplattform und ist der Kollaborationskern der ZenDiS OpenDesk-Suite [14, 50]. Integriert mit **Collabora Online** (einem Enterprise-unterstützten LibreOffice Online) ermöglicht es die kollaborative Bearbeitung von Dokumenten, Tabellen und Präsentationen im Browser in offenen Formaten [15]. Dieses Gespann eliminiert die 100–300 €/Seat/Jahr teure proprietäre Office-Cloud-Lizenz, während es die kollaborativen Kernprozesse beibehält, auf die die Mitarbeitenden angewiesen sind, und Daten auf Infrastruktur speichert, die die Kommune kontrolliert [14, 15, 50].

### 4.4 Kommunikation und Messaging: Matrix/Element

Sichere, souveräne Kommunikation wird durch das **Matrix**-Protokoll und seinen Referenzclient **Element** bereitgestellt [17]. Matrix ist ein dezentralisierter, Ende-zu-Ende-verschlüsselter, föderierter Messaging-Standard, der von mehreren nationalen Regierungen und Streitkräften für souveräne Kommunikation eingesetzt wird, weil die Föderierung es jeder Organisation ermöglicht, ihren eigenen Homeserver zu betreiben und dennoch zu interoperieren [17]. Für Kommunen bedeutet dies internen und behördenübergreifenden Nachrichtenaustausch, der verschlüsselt, selbst gehostet und frei von Per-Seat-Lizenzkosten ist und direkt dem GovStack-Messaging-Baustein entspricht [17, 49].

### 4.5 Open-Data-Infrastruktur: CKAN

Die Open-Data-Veröffentlichung wird von **CKAN** dominiert, der Open-Source-Datenverwaltungsplattform, die zahlreiche nationale und kommunale Open-Data-Portale betreibt [22]. CKAN unterstützt Datensatz-Katalogisierung, Harvesting, APIs und Metadatenstandards und erfüllt nativ die Anforderungen der EU-Open-Data-Richtlinie an offene APIs und maschinenlesbare Formate [22, 44]. Es implementiert das für die Interoperabilität mit nationalen und EU-Datenkatalogen erforderliche DCAT-AP-Metadatenprofil und integriert sich in das Schweizer opendata.swiss und das deutsche GovData-Ökosystem [22, 44, 47]. Die Rolle von CKAN wird durch den EU Data Act erheblich erweitert, der in Abschnitt 4.10 behandelt wird.

### 4.6 Geographische Informationssysteme: GeoServer, QGIS und MapLibre

Kommunale Geodienste stützen sich auf einen reifen, vollständig offenen Stack. **GeoServer** liefert Geodaten über die von der INSPIRE-Richtlinie geforderten Standards des Open Geospatial Consortium (OGC) (WMS, WFS, WMTS) [42, 41]. **QGIS** bietet professionelle Desktop-GIS-Funktionen für Analyse und Kartographie, und **MapLibre** ermöglicht performantes, anbieterunabhängiges Web-Kartenrendering für bürgerorientierte Anwendungen [41]. Diese Kombination erfüllt alle gängigen kommunalen Geodatananforderungen — Kataster, Planung, Versorgungsnetze, Umweltmonitoring — mit vollständiger INSPIRE- und OGC-Konformität und ohne Lizenzkosten [42, 41].

### 4.7 Workflow und Fallmanagement: Camunda und Formio

Die Automatisierung administrativer Prozesse ist die Schicht, bei der die Reife von Open Source manchmal in Frage gestellt wird, aber zwei Komponenten erfüllen die Anforderung. **Camunda** ist eine BPMN-2.0-konforme Workflow- und Entscheidungs-Engine, die häufig zur Orchestrierung administrativer Prozesse eingesetzt wird und prüfbare, standardbasierte Prozessautomatisierung bietet [18]. **Form.io** (und vergleichbare offene Form-Builder) stellt dynamische, schemagesteuerte Bürgerformulare bereit, die an XÖV- oder eCH-Datenmodelle gebunden und in Camunda-Prozesse geleitet werden können [18, 46, 47]. Zusammen wandeln sie Papier- oder proprietäre Workflow-Prozesse in transparente, veränderbare, standardbasierte digitale Dienste um.

### 4.8 Cloud-Infrastruktur: Sovereign Cloud Stack und Kubernetes

Auch die Infrastrukturschicht selbst muss souverän sein. Der **Sovereign Cloud Stack (SCS)** ist ein gemeinschaftlich entwickelter, standardisierter, vollständig quelloffener Cloud-Stack, der OpenStack (IaaS) und Kubernetes (Container-Orchestrierung) in eine zertifizierte, föderierbare Referenzimplementierung zusammenführt, die explizit für die europäische digitale Souveränität konzipiert wurde [3, 11]. SCS stellt einen kuratierten, getesteten, sicherheitsgepatchten Komponentensatz bereit, was die operative und sicherheitstechnische Last kommunaler Teams wesentlich reduziert [3, 11]. Kommunen können SCS auf ihrer eigenen Hardware einsetzen, es von einem souveränen Cloud-Anbieter beziehen oder über eine Kooperative wie govdigital eG nutzen [3, 11, 23]. **Kubernetes** bildet die Container-Orchestrierungsschicht in allen Bereitstellungsmodellen.

### 4.9 Sicherheit und Monitoring: OpenZiti, Wazuh und Grafana-Stack

Die Sicherheits- und Observabilitätsschicht kombiniert mehrere reife Projekte. **OpenZiti** stellt Zero-Trust-Netzwerkzugang bereit und ersetzt perimeterbasierende VPNs durch identitätsbasierte, Least-Privilege-Konnektivität [40]. **Wazuh** liefert quelloffene SIEM- und XDR-Fähigkeiten — Intrusion Detection, Log-Analyse und Compliance-Monitoring — zur Unterstützung der Nachweis-Anforderungen von BSI IT-Grundschutz und dem Schweizer ISDS-Rahmen [40, 26]. Der **Grafana-Stack** (Grafana, Prometheus, Loki) stellt Metriken, Logging und Dashboarding für operative Observability bereit [40]. Diese Schicht liefert die technischen Kontrollen und Prüfungsnachweise, die NIS2 und nationale Sicherheitsrahmen (Abschnitt 7.5) erfordern [27, 26].

### 4.10 Datenräume und der EU Data Act

Der **EU Data Act** (Verordnung (EU) 2023/2854), der ab September 2025 gilt, schafft neue Verpflichtungen für den Datenaustausch zwischen Unternehmen und Regierungen und gestaltet die kommunale Datenschicht neu [52]. Drei Implikationen ergeben sich daraus. Erstens werden kommunale Datenvermögen — Verkehr, Versorgungsnetze, Planung — unter bestimmten Bedingungen obligatorischen Datenweitergabepflichten unterworfen, was Kommunen dazu verpflichtet, Daten über regulierte, standardbasierte Schnittstellen bereitzustellen. Zweitens bietet **GAIA-X** den technischen Rahmen für den föderatierten, souveränen Datenaustausch in Europa und definiert die Vertrauens- und Interoperabilitätsregeln, unter denen kommunale Daten geteilt werden können, ohne Souveränität aufzugeben [56]. Drittens sollten Kommunen die Beteiligung an sektorspezifischen **Datenräumen** — urbane Mobilität, Energie, Umweltmonitoring — evaluieren, durch die ihre Daten öffentlichen Wert schaffen können, während sie unter ihrer Kontrolle bleiben [56, 52].

Die technische Anforderung ist konkret: Der kommunale Datenkatalog (**CKAN** [22]) muss **DCAT-AP 3.0** implementieren und bei den entsprechenden nationalen und EU-Datenraum-Brokern registriert werden. Das EU-Daten­governance-Gesetz (2022) und der Data Act (2023) schreiben gemeinsam offene APIs für Daten des öffentlichen Sektors vor — eine Anforderung, die CKAN nativ erfüllt [52, 22, 44]. Die in Abschnitt 4.5 spezifizierte Open-Data-Schicht ist daher nicht lediglich ein Transparenzinstrument, sondern der konforme Partizipationspunkt der Kommune in der entstehenden europäischen Datenwirtschaft.

### 4.11 Zusammenfassung der Gesamtbewertungen

Die folgende Tabelle fasst die Gesamtwerte (Summe von sieben gleichgewichteten 0–5-Kriterien; Maximum 35) für die empfohlene Komponente in jeder funktionalen Schicht zusammen. Die vollständige Methodik befindet sich in Anhang A.

| Schicht | Empfohlene Komponente | Lizenz | Reife | Community | Interop | Sicherheit | TCO | Öff. Sektor | Gesamt /35 |
|---|---|---|---|---|---|---|---|---|---|
| IAM | Keycloak | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 34 |
| Partizipation | Decidim | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 31 |
| Kollaboration | Nextcloud + Collabora | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 33 |
| Messaging | Matrix / Element | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 32 |
| Offene Daten | CKAN | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 33 |
| Geodaten | GeoServer + QGIS + MapLibre | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 34 |
| Workflow | Camunda + Form.io | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 30 |
| Cloud-Infra | Sovereign Cloud Stack | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 31 |
| Sicherheit/Monitoring | OpenZiti + Wazuh + Grafana | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 31 |

Alle neun Schichten erzielen 30 oder mehr von maximal 35 Punkten, was bestätigt, dass für jede funktionale Anforderung des kommunalen Bestands reife, standardkonforme, öffentlich eingesetzte Open-Source-Komponenten existieren (womit **FF1** affirmativ beantwortet ist).

---

## 5. Implementierungs-Fahrplan

Der Fahrplan erstreckt sich über 36 Monate in sechs Phasen. Er ist bewusst konservativ angelegt: Jede Phase liefert eigenständigen Wert, sodass ein Übergang ohne Verlust getätigter Investitionen pausiert werden kann und politische Auftraggeber frühe Erfolge vorweisen können. Jurisdiktionsspezifische Verpflichtungen sind in den Abschnitten 5.6 (Deutschland) und 5.7 (Schweiz) zusammengefasst.

### 5.0 Phase 0: Bereitschaftsbeurteilung (Monate 1–3)

Phase 0 legt die Ausgangsbasis und das Mandat fest. Aktivitäten: eine vollständige Bestandsaufnahme der aktuellen Anwendungen, Lizenzen, Datenflüsse und Vertragsablaufdaten; eine TCO-Basislinie nach dem Rahmen in Anhang B; eine Stakeholder-Karte und die Bildung einer Steuerungsgruppe mit expliziter politischer Trägerschaft; eine Kompetenzmangel-Analyse; sowie die Auswahl des Jurisdiktionspfads (Abschnitt 5.6 oder 5.7). Das Ergebnis ist ein von der Verwaltungsleitung genehmigter Business Case und ein Phasenplan. In dieser Phase werden keine Produktivsysteme verändert.

### 5.1 Phase 1: Fundament (Monate 4–9)

Phase 1 baut das souveräne Fundament: Bereitstellung der Cloud-Infrastrukturschicht (Sovereign Cloud Stack / Kubernetes, Abschnitt 4.8) und der IAM-Schicht (Keycloak, Abschnitt 4.1), einschließlich Föderierung mit dem nationalen Identitätssystem (BundID oder Swiyu) [13, 16]. Sicherheit und Monitoring (Abschnitt 4.9) sowie die erste BSI-IT-Grundschutz- / ISDS-Dokumentation werden parallel aufgebaut. Das Ergebnis ist eine laufende, gesicherte, souveräne Plattform, auf die anschließend Dienste aufgespielt werden.

### 5.2 Phase 2: Kerndienste (Monate 10–18)

Phase 2 migriert die werthaltigsten, risikoärmsten nutzerseitigen Dienste: die Kollaborationssuite (Nextcloud + Collabora, Abschnitt 4.3) und sicheres Messaging (Matrix/Element, Abschnitt 4.4), die zusammen die sichtbarsten Per-Seat-Lizenzersparnisse und den klarsten mitarbeiterseitigen Nutzen bringen. Die Open-Data-Plattform (CKAN, Abschnitt 4.5) wird ebenfalls in dieser Phase aufgebaut und liefert einen frühen, öffentlich sichtbaren Transparenzerfolg. Die Migration läuft parallel zu den Bestandssystemen, um ein Rollback zu ermöglichen.

### 5.3 Phase 3: Integration (Monate 19–24)

Phase 3 verbindet die Plattform mit der bürgerorientieren Dienstleistungserbringung: das Beteiligungsportal (Decidim/CONSUL, Abschnitt 4.2) und die Workflow- und Formularschicht (Camunda + Form.io, Abschnitt 4.7), gebunden an die nationalen Interoperabilitätsstandards (XÖV oder eCH) [46, 47]. Geodienste (Abschnitt 4.6) werden dort integriert, wo kommunale Funktionen sie erfordern. Das Ergebnis sind durchgängige, authentifizierte, standardkonforme digitale Dienste. Die Arbeit an der ISMS-Zertifizierung beginnt in dieser Phase.

### 5.4 Phase 4: Erweiterte Fähigkeiten (Monate 25–30)

Phase 4 erweitert die Plattform: Beteiligung an Datenräumen im Rahmen des EU Data Act (Abschnitt 4.10), DCAT-AP-3.0-Registrierung und Integration mit sektorspezifischen Datenbrokern [52, 56]; Übernahme weiterer EfA-/ GovStack-Bausteine; sowie Abschaltung der kostenintensivsten verbleibenden proprietären Verträge bei deren Verlängerung. Das Ergebnis ist eine Kommune, die geteilte offene Infrastruktur nutzt und zu ihr beiträgt.

### 5.5 Phase 5: Optimierung und Skalierung (Monate 31–36)

Phase 5 konsolidiert: Leistungsoptimierung, Abschluss der ISMS-Zertifizierung, Einbringung lokal entwickelter Komponenten in openCode.de (Deutschland) oder das entsprechende Repository (Schweiz) gemäß dem Open-by-Default-Mandat sowie Formalisierung der Kooperativmitgliedschaft für den langfristigen Betrieb [10, 1, 23]. Das Ergebnis ist ein stabiler, souveräner, kooperativ unterstützter IT-Bestand mit einem dokumentierten Betriebsmodell.

### 5.6 Umsetzungspfad für den deutschen Rechtsraum

Deutsche Kommunen müssen die folgenden spezifischen Verpflichtungen auf den generischen Fahrplan aufsetzen:

- **OZG-2.0-Konformität:** Alle Verwaltungsleistungen müssen zu den vorgeschriebenen Terminen online verfügbar sein; EfA-Dienste von Pionierkommunen über das FITKO-Portal beziehen statt sie neu zu entwickeln [9].
- **BundID-Föderierung:** Keycloak muss mit BundID (dem nationalen Bürgeridentitätssystem) föderieren; Konfigurationsschritte und API-Dokumentation sind unter id.bund.de verfügbar [9, 13].
- **XÖV-Standards-Integration:** Der gesamte Datenaustausch muss XÖV-konforme XML-Schemata verwenden, und Formulare müssen XForms nutzen, wo vorgeschrieben [46].
- **openCode.de-Beteiligung:** Alle individuell entwickelte Software muss gemäß dem OZG-2.0-Mandat auf openCode.de veröffentlicht werden [10].
- **govdigital eG:** Als Mitglied beitreten oder Cloud-Infrastruktur über die Rahmenverträge beziehen [23].
- **BSI IT-Grundschutz:** Die Sicherheitsdokumentation ist verbindlich; Ziel ist die ISMS-Zertifizierung innerhalb von 24 Monaten [26].
- **ZenDiS-Partnerschaft:** ZenDiS für OpenDesk-Implementierungsunterstützung und Zugang zu geprüften Komponenten kontaktieren [50].
- **NIS2-Konformität:** Kommunen gelten ab Oktober 2024 als „wesentliche Einrichtungen" im Sinne von NIS2 und müssen dessen Risikomanagement- und Meldepflichten erfüllen [27].

### 5.7 Umsetzungspfad für den Schweizer Rechtsraum

Schweizer Kommunen müssen die folgenden spezifischen Verpflichtungen auf den generischen Fahrplan aufsetzen:

- **EMBAG-Konformität:** Individuell entwickelte Software muss als Open Source veröffentlicht werden, sofern keine Sicherheitsausnahme greift [1].
- **E-Government-Strategie 2024–2027:** Den Fahrplan für digitale Dienste an der kantonalen und Bundesstrategie ausrichten [16].
- **eCH-Standards-Konformität:** Der gesamte Datenaustausch muss die anwendbaren eCH-XML-Standards nutzen (eCH-0010, -0011, -0044, -0058, -0185) [47].
- **opendata.swiss-Registrierung:** Offene Datensätze über die kantonale CKAN-Instanz bei opendata.swiss veröffentlichen [44, 22].
- **Integration der Schweizer eID:** Keycloak so konfigurieren, dass es die Swiyu-eID akzeptiert, wenn diese verfügbar ist (ab 2026) [16].
- **ISDS-Rahmen:** Das Rahmenwerk Informationssicherheit und Datenschutz in der Verwaltung (ISDS) anwenden, das schweizerische Pendant zu BSI IT-Grundschutz, für Sicherheits- und Datenschutzdokumentation.
- **Kantonale IT-Kooperativmitgliedschaft:** Die meisten Kantone betreiben gemeinsame IT-Strukturen (z. B. kantonale CIO-Büros / Informatikleistungszentren), die Rahmenverträge für Open-Source-IT anbieten, die Kommunen in Anspruch nehmen können.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Politische Führung und Einbindung des Gemeinderats

Kein kommunaler Open-Source-Übergang überlebt ohne dauerhafte politische Trägerschaft; der LiMux-Rückschlag ist das warnende Beispiel [55]. Die Strategie muss dem Gemeinderat nicht in erster Linie als technisches Projekt, sondern als Frage der fiskalischen Verantwortung, der digitalen Souveränität und der lokalen Wirtschaftsentwicklung präsentiert werden, mit messbaren Meilensteinen, die je Phase öffentlich berichtet werden. Den Aufbau einer parteiübergreifenden Koalition statt eines einzigen Sponsors herzustellen, ist die wichtigste Absicherung gegen eine Umkehr bei Verwaltungswechseln [55, 4].

### 6.2 Kompetenzentwicklung des IT-Personals

Open-Source-Betrieb verlagert Kosten von Lizenzen auf Kompetenzen, daher ist Kompetenzentwicklung nicht optional. Die Strategie verbindet formale Schulung (Linux, Kubernetes, Keycloak, den gewählten Anwendungsstack), anbietergestützte Implementierung in frühen Phasen und Beteiligung an den einschlägigen Communities (ZenDiS, SCS, OSOR) für Wissenstransfer [50, 3, 51]. Für kleine Kommunen ersetzt das Kooperativmodell gemeinsame operative Kapazität durch eigene Expertise (Abschnitt 3.10) [23].

### 6.3 Bürgerkommunikation und -beteiligung

Bürgerinnen und Bürger erleben den Übergang durch neue Portale und Dienste; die Kommunikationsstrategie muss den Souveränitäts- und Transparenz-Gedanken erläutern und die Beteiligungsplattform (Decidim/CONSUL) selbst zur Einholung von Feedback nutzen, womit die Migration zu einer Demonstration von Open Government wird [12, 48, 53]. Sichtbare frühe Erfolge — ein funktionierendes Open-Data-Portal, verbesserte Online-Dienste — bauen die öffentliche Unterstützung auf, die den politischen Rückhalt stärkt.

### 6.4 EU-Vergaberecht und Open-Source-Konformität

Das Beschaffungswesen ist der Bereich, in dem Open-Source-Strategien am häufigsten an technischen Details scheitern, daher muss der rechtliche Rahmen präzise sein. Die EU-Richtlinie 2014/24/EU über die öffentliche Auftragsvergabe findet Anwendung, in Deutschland national umgesetzt durch GWB und VgV, in der Schweiz durch BöB und IVöB [43]. Der entscheidende konzeptionelle Punkt ist, dass Open-Source-Software *kostenlos nutzbar* ist — was die Kommune beschafft, ist nicht die Software, sondern die **Dienste** rund um sie: Implementierung, Hosting, Support, Anpassung und Schulung. Ausschreibungen müssen daher für Dienste, nicht für Produktlizenzen verfasst werden.

Zuschlagskriterien müssen das Prinzip des **wirtschaftlich günstigsten Angebots (MEAT)** anwenden und explizit die Gesamtbetriebskosten, Interoperabilität und Ausstiegskosten gewichten — nicht nur den Einzelpreis —, da sonst die strukturellen Vorteile von Open Source (Kategorien f und g in Abschnitt 3.9) für die Bewertung unsichtbar bleiben [43]. Individuelle Liefergegenstände sollten eine **„Public Money? Public Code!"**-Vertragsklausel tragen, die eine OSI-genehmigte Lizenz für alle maßgeschneiderten Anpassungen vorschreibt [4]. Schließlich ermöglichen bestehende kooperative **Rahmenverträge** (Abschnitt 6.5), individuelle Beschaffungen unterhalb der Schwellenwerte ohne vollständiges Vergabeverfahren abzuwickeln, was den Transaktionsaufwand erheblich reduziert [23, 24].

### 6.5 Rahmenverträge und kooperative Beschaffung

Kooperative Beschaffungsstrukturen sind der praktische Mechanismus, der die Strategie beschaffbar macht, insbesondere für kleinere Kommunen:

- **govdigital eG (Deutschland):** eine mitgliedereigene Genossenschaft öffentlicher IT-Dienstleister; ihre Rahmenverträge erfüllen GWB/Vergaberecht und ermöglichen Mitgliedern die Beschaffung konformer Open-Source-Cloud und -Dienste ohne individuelle Vollausschreibungen [23].
- **Dataport AöR (Deutschland):** Eine Anstalt des öffentlichen Rechts, die von ihren Mitgliedsländern Direktaufträge ohne Ausschreibung erhalten darf und damit einen vollständig konformen Weg zu gemeinsamer Open-Source-Infrastruktur bietet [24].
- **Kantonale IT-Kooperativen der Schweiz:** analoge Strukturen; die meisten Kantone betreiben Informatikleistungszentren mit offenen Beschaffungsrahmen, auf die Kommunen zurückgreifen können.
- **ZenDiS (Deutschland):** Seine Komponenten stehen frei zur Verfügung, und Integrationsunterstützung kann über das ZenDiS-Partnernetzwerk beschafft werden [50].

---

## 7. Risikoanalyse

### 7.1 Organisationaler Widerstand gegen Veränderung

Das dominante Risiko ist menschlicher, nicht technischer Natur: Mitarbeitende und Führungskräfte, die an bestehende Werkzeuge gewöhnt sind, widerstehen Veränderungen, und dieser Widerstand verstärkt sich, wenn Migrationen als aufgezwungen wahrgenommen werden. Die Gegenmaßnahme kombiniert frühe Einbeziehung der Mitarbeitenden, Parallelbetrieb zur Verringerung der Angst vor Unterbrechungen, sichtbare schnelle Erfolge und ein angemessenes Schulungsbudget (Abschnitt 6.2). Die Phaseneinteilung des Fahrplans, sodass jeder Schritt umkehrbar und wertbringend ist, reduziert dieses Risiko unmittelbar [55].

### 7.2 Kompetenz- und Kapazitätslücken

Einer Kommune können die Fähigkeiten fehlen, den Stack zu betreiben, insbesondere auf der Infrastrukturebene. Gegenmaßnahme: Anbietergestützte Implementierung vorreihen, in Schulung investieren und — entscheidend für kleine Kommunen — Infrastruktur als kooperativen Dienst beziehen statt sie selbst zu betreiben (Abschnitte 3.10, 6.5) [23, 24]. Der kuratierte, gepatchte Komponentensatz des Sovereign Cloud Stack senkt die operative Kompetenzschwelle [3, 11].

### 7.3 Komplexität der Technologieintegration

Die Integration von neun Schichten und die Föderierung mit nationalen Identitäts- und Interoperabilitätssystemen ist tatsächlich komplex. Gegenmaßnahme: durchgehend standardbasierte Komponenten verwenden (OIDC, BPMN, DCAT-AP, OGC, XÖV, eCH), GovStack-konforme Baustein-Architektur gegenüber maßgeschneiderten Integrationen bevorzugen und Integration (Phase 3) erst nach Stabilisierung des Fundaments sequenzieren [49, 46, 47].

### 7.4 Abwehr von Anbieter-Lobbying und FUD

Dieses Risiko wird systematisch unterschätzt. Proprietäre Anbieter betreiben routinemäßig FUD-Kampagnen (Fear, Uncertainty, Doubt — Angst, Ungewissheit, Zweifel) gegen Open-Source-Übergänge. Beobachtete Strategien umfassen die Übertreibung der Migrationskomplexität, die Aufblähung des TCO für Open Source, die Nutzung persönlicher Beziehungen zu IT-Mitarbeitenden, die Finanzierung nominell „unabhängiger" Studien und die zeitliche Abstimmung von Preisnachlässen mit Entscheidungsmomenten für den Übergang. Der Münchner Fall dokumentiert die Rolle, die Anbieter-Lobbying bei der LiMux-Umkehrung spielte — obwohl der neue Stadtrat 2019 erneut den Kurs Richtung Open Source einschlug [55].

Gegenmaßnahmen sind verfahrensmäßiger und politischer Natur: **unabhängige** TCO-Studien in Auftrag geben, bevor Anbieterverhandlungen aufgenommen werden; Zivilgesellschaft als Transparenz-Watchdog einbinden; alle Beschaffungsentscheidungen offen veröffentlichen; und die FSFE-Rahmung „Public Money? Public Code!" als politische Deckung nutzen, die jede Umkehrung als Rückzug aus fiskalischer Verantwortung und Souveränität umdeklariert [4, 55].

### 7.5 Lieferketten- und Open-Source-Sicherheitsrisiken

Die Log4Shell-Schwachstelle von 2021 hat gezeigt, dass das Open-Source-Lieferkettenrisiko strukturiertes Management statt blindem Vertrauen erfordert. Konkrete Kontrollen:

- **Software Bill of Materials (SBOM)** im CycloneDX- oder SPDX-Format für alle eingesetzten Open-Source-Komponenten vorschreiben.
- Den **OpenSSF Scorecard** (CNCF/OpenSSF) zur Bewertung des Sicherheitszustands von Kandidatenkomponenten verwenden.
- **CVE-Feeds** für alle Stack-Komponenten abonnieren und eine automatisierte Patch-Pipeline implementieren.
- Den **Sovereign Cloud Stack** bevorzugen, der einen kuratierten, getesteten, sicherheitsgepatchten Komponentensatz bereitstellt [3, 11].
- BSI-IT-Grundschutz-Bausteine **INF.14, OPS.1.1.3 und OPS.1.2.4** anwenden, die das Patch-Management abdecken [26].
- **NIS2 Artikel 21** erfüllen, der Maßnahmen zur Lieferkettensicherheit für wesentliche Einrichtungen vorschreibt [27].

Bei sachgemäßer Verwaltung ist das Open-Source-Lieferkettenrisiko *handhabbarer* als das proprietäre Risiko, weil die Komponenten inspizierbar sind und der Patch-Prozess nicht von einem einzigen Anbieter kontrolliert wird.

---

## 8. Schlussfolgerung

Diese Arbeit hatte sich zum Ziel gesetzt, zu klären, ob eine souveräne, auf Open Source beruhende kommunale IT-Strategie technisch machbar, wirtschaftlich vorteilhaft und operativ realisierbar ist — für Kommunen unterschiedlicher Größe und in den deutschen sowie Schweizer Rechtsordnungen. Die Evidenz stützt eine bejahende Antwort auf allen Ebenen.

Zu **FF1**: Ein kohärenter, reifer Open-Source-Stack existiert für jede der neun funktionalen Schichten, wobei alle empfohlenen Komponenten mindestens 30 von 35 Punkten auf einer transparenten Sieben-Kriterien-Matrix erzielen. Zu **FF2**: Die Gesamtbetriebskosten des Open-Source-Stacks sind über fünf Jahre bei ehrlicher Einbeziehung aller Kostenkategorien um 30–50 % niedriger, getrieben durch die Eliminierung von Lizenzkosten in Höhe von 100–300 €/Seat/Jahr und die nahezu vollständige Beseitigung von Ausstiegs- und Lock-in-Kosten, gestützt durch die Fälle DGFiP und Barcelona — wenngleich dem Feld noch unabhängige Vergleichsstudien fehlen. Zu **FF3**: Ein konservativer, wertbringender 36-Monats-Fahrplan ist realisierbar, mit vollständig ausgearbeiteten deutschen und Schweizer Pfaden, die den generischen Plan jeweils auf OZG/BundID/XÖV/BSI und EMBAG/eCH/Swiyu/ISDS ausrichten. Zu **FF4**: Dauerhafter Erfolg hängt weniger von der Technologie als von parteiübergreifender politischer Trägerschaft, Kompetenzentwicklung, konformer kooperativer Beschaffung und disziplinierter Abwehr von Anbieter-Lobbying und Lieferkettenrisiken ab.

Die zentrale Schlussfolgerung lautet: Kommunale IT kann *sovereign by design* — von Grund auf souverän — sein. Die Komponenten sind reif, die Standards existieren, die institutionelle Unterstützung (ZenDiS, GovStack, OSOR, die Kooperativen) ist vorhanden, und das Recht verlangt zunehmend diesen Kurs. Die verbleibenden Hindernisse sind organisatorischer und politischer, nicht technologischer Natur — und sie sind mit den hier dargelegten Strategien überwindbar.

---

## Literaturverzeichnis

[1] Schweizerische Eidgenossenschaft. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. Bern: Bundeskanzlei. https://www.fedlex.admin.ch/ — [Open Access, Bundesgesetz]

[2] Floridi, L. (2020). The Fight for Digital Sovereignty: What It Is, and Why It Matters, Especially for the EU. *Philosophy & Technology*, 33, 369–378. https://doi.org/10.1007/s13347-020-00423-6

[3] Sovereign Cloud Stack Community. (2023). *Sovereign Cloud Stack: A Standardised, Open-Source Cloud Reference Implementation*. Berlin: Open Source Business Alliance. https://scs.community/ — [Open Access]

[4] Free Software Foundation Europe (FSFE). (2019). *Public Money? Public Code! Modernising Public Infrastructure with Free Software*. Berlin: FSFE. https://publiccode.eu/ — [Open Access, CC-BY-SA]

[5] Pohle, J., & Thiel, T. (2020). Digital Sovereignty. *Internet Policy Review*, 9(4). https://doi.org/10.14763/2020.4.1532

[6] Ebert, C., & Brinkkemper, S. (2021). Open Source Software in Public Administration. *IEEE Software*, 38(2), 7–12. https://doi.org/10.1109/MS.2021.3053230

[7] Maarleveld, M., Bonina, C., & Janssen, M. (2019). Challenges of Open Government Data in Smart Cities. *Government Information Quarterly*, 36(4), 101389. https://doi.org/10.1016/j.giq.2019.08.001

[8] Wirtz, B. W., & Birkmeyer, S. (2015). Open Government: Origin, Development, and Conceptual Perspectives. *International Journal of Public Administration*, 38(5), 381–396. https://doi.org/10.1080/01900692.2014.942735

[9] Bundesministerium des Innern und für Heimat (BMI). (2023). *Onlinezugangsgesetz (OZG 2.0)*. Berlin: BMI. https://www.onlinezugangsgesetz.de/

[10] FITKO. (2023). *openCode.de: Die Plattform für Open Source in der öffentlichen Verwaltung*. Frankfurt: FITKO. https://opencode.de/

[11] Open Source Business Alliance. (2023). *SCS Release 6: Tested and Certified*. Berlin: OSBA. https://scs.community/release/

[12] Ajuntament de Barcelona. (2020). *Decidim: Democratic Infrastructure for the 21st Century City*. Barcelona: Ajuntament de Barcelona. https://decidim.org/

[13] Red Hat / Keycloak Project. (2024). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/

[14] Nextcloud GmbH. (2024). *Nextcloud Hub: The On-Premises Collaboration Platform*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/

[15] Collabora Productivity Ltd. (2024). *Collabora Online: Enterprise-Grade LibreOffice in the Cloud*. Cambridge: Collabora. https://www.collaboraoffice.com/

[16] Bundeskanzlei. (2023). *E-Government-Strategie Schweiz 2024–2027 und E-ID-Gesetz*. Bern: Bundeskanzlei. https://www.bk.admin.ch/

[17] Matrix.org Foundation. (2024). *Matrix: An Open Network for Secure, Decentralised Communication*. https://matrix.org/

[18] Camunda Services GmbH. (2024). *Camunda Platform: BPMN-Based Process Orchestration*. Berlin: Camunda. https://camunda.com/

[19] The Document Foundation. (2024). *LibreOffice: Free and Open Source Office Suite*. Berlin: The Document Foundation. https://www.libreoffice.org/

[20] Linux Foundation. (2024). *Kubernetes: Production-Grade Container Orchestration*. San Francisco: Linux Foundation. https://kubernetes.io/

[21] OpenStack Foundation. (2024). *OpenStack: Open Source Cloud Computing Infrastructure*. Austin: OpenStack Foundation. https://www.openstack.org/

[22] Open Knowledge Foundation. (2024). *CKAN: The Open Source Data Management System*. https://ckan.org/

[23] govdigital eG. (2023). *govdigital: Die Genossenschaft für Public IT*. Berlin: govdigital eG. https://govdigital.de/

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg/Altenholz: Dataport AöR. https://www.dataport.de/

[25] BSI — Bundesamt für Sicherheit in der Informationstechnik. (2023). *BSI IT-Grundschutz-Kompendium 2023*. Bonn: BSI. https://www.bsi.bund.de/grundschutz

[26] BSI — Bundesamt für Sicherheit in der Informationstechnik. (2023). *IT-Grundschutz-Bausteine: INF.14, OPS.1.1.3, OPS.1.2.4*. Bonn: BSI. https://www.bsi.bund.de/grundschutz

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 über Maßnahmen für ein hohes gemeinsames Cybersicherheitsniveau in der Union (NIS2)*. https://eur-lex.europa.eu/

[28] Eclipse Foundation. (2024). *Eclipse Dirigible: Cloud Development Platform*. Ottawa: Eclipse Foundation. https://www.dirigible.io/

[29] Apache Software Foundation. (2024). *Apache Superset: Open Source Data Exploration and Visualization*. https://superset.apache.org/

[30] Grafana Labs. (2024). *Grafana: Open Source Observability Platform*. New York: Grafana Labs. https://grafana.com/

[31] Prometheus Authors. (2024). *Prometheus: Monitoring System and Time Series Database*. https://prometheus.io/

[32] Wazuh Inc. (2024). *Wazuh: Open Source Security Platform*. https://wazuh.com/

[33] OpenZiti Project. (2024). *OpenZiti: Zero Trust Networking Platform*. https://openziti.io/

[34] OWASP Foundation. (2024). *OWASP Top Ten: The Standard Awareness Document for Developers*. https://owasp.org/

[35] OpenSSF. (2024). *OpenSSF Scorecard: Assessing Security of Open Source Projects*. Linux Foundation. https://securityscorecards.dev/

[36] CNCF. (2024). *Cloud Native Security Whitepaper*. San Francisco: Cloud Native Computing Foundation. https://www.cncf.io/

[37] GitLab Inc. (2024). *GitLab: The DevSecOps Platform*. San Francisco: GitLab. https://gitlab.com/

[38] OpenProject GmbH. (2024). *OpenProject: Open Source Project Management*. Berlin: OpenProject GmbH. https://www.openproject.org/

[39] BigBlueButton Project. (2024). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/

[40] SIEM/XDR Working Group. (2023). *Open Source Security Operations Reference Architecture*. [Internes Referenz-Dokument]

[41] QGIS Project. (2024). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/

[42] GeoServer Community. (2024). *GeoServer: Open Source Server for Sharing Geospatial Data*. https://geoserver.org/

[43] Europäisches Parlament und Rat. (2014). *Richtlinie 2014/24/EU über die öffentliche Auftragsvergabe*. https://eur-lex.europa.eu/

[44] Europäisches Parlament und Rat. (2019). *Richtlinie (EU) 2019/1024 über offene Daten und die Weiterverwendung von Informationen des öffentlichen Sektors*. https://eur-lex.europa.eu/

[45] W3C. (2023). *DCAT-AP 3.0: Data Catalog Vocabulary Application Profile for Data Portals in Europe*. https://www.w3.org/TR/vocab-dcat-3/

[46] Koordinierungsstelle für IT-Standards (KoSIT). (2023). *XÖV-Standards: XML-Schnittstellenstandards für die öffentliche Verwaltung*. Bremen: KoSIT. https://www.xoev.de/

[47] eCH — E-Government Schweiz. (2024). *eCH-Fachgruppen und Normen: eCH-0010, eCH-0011, eCH-0044, eCH-0058, eCH-0185*. Bern: eCH. https://www.ech.ch/

[48] Consul Democracy Project. (2024). *CONSUL Democracy: Open Government and E-Participation Tool*. Madrid: Ayuntamiento de Madrid. https://consulproject.org/

[49] ITU/DIAL/BMZ/Regierung von Estland. (2022). *GovStack: Building Blocks for Digital Government*. Genf: ITU. https://www.govstack.global/

[50] ZenDiS GmbH. (2023). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. Berlin: ZenDiS. https://zendis.de/

[51] Europäische Kommission, OSOR. (2023). *Open Source Observatory Annual Report 2023*. Brüssel. https://joinup.ec.europa.eu/collection/open-source-observatory-osor

[52] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 — EU Data Act*. https://eur-lex.europa.eu/

[53] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government*. Sebastopol: O'Reilly. ISBN 978-0-596-80435-0

[54] DGFiP. (2021). *Migration vers LibreOffice: Retour d'expérience*. Paris: DGFiP. https://www.numerique.gouv.fr/

[55] Landeshauptstadt München. (2017). *Abschlussbericht LiMux*. München: Stadtrat. [Öffentliche Akte]

[56] GAIA-X AISBL. (2023). *GAIA-X: Architecture Overview*. Brüssel: GAIA-X AISBL. https://gaia-x.eu/

---

## Anhang A: Methodik der Technologiebewertung

Die Bewertungsmatrix ordnet jedem der sieben Kriterien eine ordinale Skala von 0 bis 5 zu. Die Kriterien sind wie folgt definiert:

**Licence (Lizenzoffenheit):** Bewertet, ob die Komponente unter einer OSI-genehmigten Lizenz veröffentlicht ist (5 = Copyleft oder permissive OSI-Lizenz, z. B. AGPL, GPL, Apache-2.0, MIT; 3 = Business-Source-Lizenz oder ähnlich zeitverzögert quelloffene Lizenz; 0 = proprietär oder quellverfügbar ohne OSI-Genehmigung). Eine Lizenzoffenheit von 5 ist für alle im Stack empfohlenen Komponenten eine Mindestanforderung; sie stellt sicher, dass die Kommune die in Abschnitt 3.1 beschriebenen rechtlichen Rechte auf Nutzung, Prüfung, Modifikation und Weitergabe tatsächlich ausüben kann.

**Maturity (Deployment-Reife):** Bewertet den nachgewiesenen Reifegrad in der Produktionsnutzung: stabile Versionierung, dokumentierte API-Stabilität, regelmäßige Release-Zyklen und nachweislicher Einsatz in skalierten Umgebungen. Ein Wert von 5 setzt eine Versionshistorie von mindestens fünf Jahren mit stabilen Releases und dokumentierten Enterprise-Deployments voraus.

**Community (Community-Gesundheit):** Bewertet die Aktivität und Diversität der Entwickler-Community, gemessen an der Commit-Frequenz, der Anzahl aktiver Mitwirkender, der Dokumentationsqualität und der Reaktionsfähigkeit auf gemeldete Sicherheitsprobleme (CVEs). Monokultur-Communities mit einem einzigen dominanten Sponsor erhalten maximal 4 Punkte, weil das Risiko eines Sponsor-Rückzugs die Projektlebensdauer gefährdet.

**Interop (Interoperabilitäts-Standards-Konformität):** Bewertet die Implementierung international anerkannter offener Standards, die für die Interoperabilität im kommunalen Kontext relevant sind: OIDC/OAuth 2.0 (IAM-Schicht), BPMN 2.0 (Workflow-Schicht), DCAT-AP 3.0 (Open-Data-Schicht), OGC WMS/WFS/WMTS (Geospatial-Schicht), Matrix-Protokoll (Messaging-Schicht) sowie XÖV und eCH (Datenaustausch-Schicht). Komponenten ohne Standards-Implementierung erhalten 0 Punkte auf diesem Kriterium.

**Security (Sicherheitslage):** Bewertet das strukturierte Sicherheitsverfahren der Komponente: Existenz eines öffentlichen Vulnerability-Disclosure-Programms, Zeitnähe bei CVE-Behebungen, Vorkommen und Schweregrad bekannter ungelöster Schwachstellen und Unterstützung sicherheitsrelevanter Deployment-Optionen (HSM-Integration, TLS 1.3, FIPS-konformer Krypto-Stack). Komponenten mit kritischen unbehobenen CVEs erhalten maximal 2 Punkte.

**TCO (Gesamtbetriebskosten):** Bewertet den erwarteten TCO-Vorteil über fünf Jahre im Vergleich zu repräsentativen proprietären Alternativen, unter Anwendung des in Abschnitt 3.9 dargelegten Rahmens. Ein Wert von 5 setzt eine vollständige Eliminierung wiederkehrender Per-Seat-Lizenzkosten bei vergleichbarem oder niedrigerem Gesamtbetrieb voraus; ein Wert von 3 zeigt TCO-Neutralität bei höherer Anfangsinvestition an.

**Pub-sector (Nachgewiesene Einsätze im öffentlichen Sektor):** Bewertet den dokumentierten Produktionseinsatz in europäischen Kommunal- oder Nationalverwaltungen, vorzugsweise mit öffentlich zugänglicher Fallstudien-Dokumentation. Ein Wert von 5 setzt mindestens fünf verifizierte europäische Verwaltungseinsätze voraus; ein Wert von 3 setzt mindestens einen europäischen Einsatz mit dokumentierter Produktionsnutzung voraus; ein Wert von 0 bedeutet, dass kein Verwaltungseinsatz nachgewiesen ist.

Die Kriterien sind gleichgewichtet: Jedes trägt maximal 5 Punkte zum Gesamtwert (maximal 35) bei. Es wurde bewusst auf eine Gewichtung verzichtet, um Transparenz zu gewährleisten und Manipulationen zu vermeiden; Nutzerinnen und Nutzer der Matrix, die bestimmte Kriterien für ihre Situation wichtiger erachten, können eigene Gewichtungen anwenden, ohne die Rohdaten zu ändern. Der Schwellenwert von 30 Punkten (≈ 86 %) als Mindestanforderung für eine Empfehlung entspricht der Bedingung, dass kein Kriterium einen Wert unter 3 erhält — ein Schutz gegen Komponenten, die in einem kritischen Kriterium erhebliche Schwächen aufweisen, insgesamt aber dennoch einen akzeptablen Wert erzielen würden.

---

## Anhang B: Implementierungskostenmodell

Das nachfolgende Kostenmodell parametrisiert die sieben TCO-Kategorien aus Abschnitt 3.9 für drei Kommunengrößenklassen. Alle Werte sind Richtwerte, die auf der Grundlage der verfügbaren Fallstudiendaten (DGFiP [54], Barcelona [12]) und der Markterhebung für europäische öffentliche IT-Beschaffungen kalibriert wurden. Sie müssen gegen lokale Beschaffungsbedingungen, bestehende Vertragskonditionen und den genauen Migrationsumfang validiert werden.

### Kleinkommune (5.000–25.000 Einwohnerinnen und Einwohner; ca. 50–150 IT-Benutzer)

| Kostenkategorie | Open Source (5-Jahres-Gesamt) | Proprietär (5-Jahres-Gesamt) | Differenz |
|---|---|---|---|
| (a) Implementierung | 40.000–80.000 € | 30.000–60.000 € | +10.000–20.000 € |
| (b) Wiederkehrende Lizenz | 0 € | 50.000–225.000 € | −50.000–225.000 € |
| (c) Hosting | 15.000–30.000 € | 15.000–30.000 € | Neutral |
| (d) Support | 25.000–50.000 € | 20.000–40.000 € | +5.000–10.000 € |
| (e) Schulung | 15.000–25.000 € | 5.000–10.000 € | +10.000–15.000 € |
| (f) Ausstieg | 2.000–5.000 € | 20.000–50.000 € | −18.000–45.000 € |
| (g) Lock-in-Risikoaufschlag | Gering (ø 0 €) | Mittel (ø 15.000 €) | −15.000 € |
| **Gesamt** | **97.000–190.000 €** | **140.000–430.000 €** | **−43.000–240.000 €** |

Die kooperative Beschaffungsstruktur (govdigital eG in Deutschland, kantonale ILZ in der Schweiz) ist für kleine Kommunen entscheidend: Sie senkt die Kategorien (a), (c) und (d) erheblich, indem Bereitstellungs- und Betriebskosten auf viele Mitglieder verteilt werden.

### Mittelkommune (25.000–150.000 Einwohnerinnen und Einwohner; ca. 150–800 IT-Benutzer)

| Kostenkategorie | Open Source (5-Jahres-Gesamt) | Proprietär (5-Jahres-Gesamt) | Differenz |
|---|---|---|---|
| (a) Implementierung | 150.000–300.000 € | 100.000–200.000 € | +50.000–100.000 € |
| (b) Wiederkehrende Lizenz | 0 € | 300.000–1.200.000 € | −300.000–1.200.000 € |
| (c) Hosting | 60.000–120.000 € | 60.000–120.000 € | Neutral |
| (d) Support | 80.000–160.000 € | 60.000–120.000 € | +20.000–40.000 € |
| (e) Schulung | 40.000–80.000 € | 15.000–30.000 € | +25.000–50.000 € |
| (f) Ausstieg | 5.000–15.000 € | 50.000–150.000 € | −45.000–135.000 € |
| (g) Lock-in-Risikoaufschlag | Gering (ø 0 €) | Mittel-Hoch (ø 60.000 €) | −60.000 € |
| **Gesamt** | **335.000–675.000 €** | **585.000–1.880.000 €** | **−250.000–1.205.000 €** |

In dieser Größenklasse dominiert die Einsparung bei der wiederkehrenden Lizenz (Kategorie b) die TCO-Rechnung deutlich. Die einmaligen Mehrkosten der Implementierung (a) und Schulung (e) amortisieren sich erfahrungsgemäß im zweiten Jahr.

### Großkommune (150.000–500.000 Einwohnerinnen und Einwohner; ca. 800–3.000 IT-Benutzer)

| Kostenkategorie | Open Source (5-Jahres-Gesamt) | Proprietär (5-Jahres-Gesamt) | Differenz |
|---|---|---|---|
| (a) Implementierung | 500.000–1.000.000 € | 350.000–700.000 € | +150.000–300.000 € |
| (b) Wiederkehrende Lizenz | 0 € | 1.200.000–4.500.000 € | −1.200.000–4.500.000 € |
| (c) Hosting | 200.000–400.000 € | 200.000–400.000 € | Neutral |
| (d) Support | 250.000–500.000 € | 180.000–360.000 € | +70.000–140.000 € |
| (e) Schulung | 120.000–240.000 € | 40.000–80.000 € | +80.000–160.000 € |
| (f) Ausstieg | 15.000–40.000 € | 150.000–400.000 € | −135.000–360.000 € |
| (g) Lock-in-Risikoaufschlag | Gering (ø 0 €) | Hoch (ø 200.000 €) | −200.000 € |
| **Gesamt** | **1.085.000–2.180.000 €** | **2.120.000–6.640.000 €** | **−1.035.000–4.460.000 €** |

Auf dieser Skalenstufe sind die Einsparungen erheblich und erlauben die Finanzierung substanzieller IT-Eigenkapazität aus den eingesparten Lizenzkosten, was die Nachhaltigkeit des Open-Source-Betriebs selbst stärkt.

### Methodische Hinweise

Alle Angaben gelten als Richtwerte mit einem Unsicherheitskorridor von ±30 %, der die lokale Kostenvarianz widerspiegelt. Die wichtigsten Variablen, die eine Kommune vor der Anwendung dieses Rahmens erheben muss: (i) Gesamtzahl der IT-Benutzer, gegliedert nach Nutzungsprofilen; (ii) aktuell gültige Lizenzkosten (aus laufenden Verträgen); (iii) Laufzeiten bestehender Verträge (zur Optimierung der Migrationsphasen); (iv) lokale Stundensätze für IT-Fachkräfte; (v) Verfügbarkeit und Konditionen kooperativer Beschaffungsstrukturen. Das Kostenmodell ist in einem offenen Tabellenformat (ODS/XLSX) verfügbar und kann auf openCode.de zur freien Nutzung durch Kommunen bereitgestellt werden.

---

## Anhang C: Checkliste für kommunale CIOs

Die folgende Checkliste gliedert die wesentlichen Aktionspunkte der Strategie nach Phase. Sie dient als operatives Instrument für den kommunalen CIO und als Rechenschaftsrahmen für den politischen Auftraggeber.

### Phase 0: Bereitschaftsbeurteilung

- [ ] Vollständigen IT-Bestandskatalog erstellen: alle Anwendungen, Lizenzen, Vertragsablaufdaten, Datenflusskarten
- [ ] TCO-Basislinie nach dem Rahmen in Anhang B erheben und dokumentieren
- [ ] Stakeholder-Karte erstellen und Steuerungsgruppe mit explizitem politischem Mandat einsetzen
- [ ] Kompetenzmangel-Analyse durchführen: Lücken in Linux, Kubernetes, Keycloak, Nextcloud, CKAN identifizieren
- [ ] Jurisdiktionspfad festlegen: Deutschland (Abschnitt 5.6) oder Schweiz (Abschnitt 5.7)
- [ ] Unabhängige TCO-Studie in Auftrag geben (vor Aufnahme von Lieferantenverhandlungen)
- [ ] Business Case und Phasenplan der Verwaltungsleitung zur Genehmigung vorlegen

### Phase 1: Fundament

- [ ] Kooperative Mitgliedschaft oder Rahmenvertrag abschließen (govdigital eG / kantonales ILZ)
- [ ] Sovereign Cloud Stack oder Kubernetes-Hosting bereitstellen
- [ ] Keycloak installieren und konfigurieren
- [ ] BundID-Föderierung (Deutschland) oder Swiyu-eID-Vorbereitung (Schweiz) implementieren
- [ ] Wazuh SIEM einrichten und initiale BSI-IT-Grundschutz- / ISDS-Dokumentation erstellen
- [ ] OpenZiti Zero-Trust-Netzwerkzugang einrichten
- [ ] Grafana/Prometheus/Loki-Stack für operative Observability aufsetzen
- [ ] Software Bill of Materials (SBOM) für alle eingesetzten Komponenten erstellen (CycloneDX oder SPDX)
- [ ] CVE-Feed-Abonnements und automatisierten Patch-Workflow einrichten

### Phase 2: Kerndienste

- [ ] Nextcloud-Hub bereitstellen und Collabora Online integrieren
- [ ] Benutzermigration von proprietärer Dateispeicherung und E-Mail planen und beginnen
- [ ] Matrix/Element-Homeserver bereitstellen und mit IAM-Schicht (Keycloak) verbinden
- [ ] CKAN-Open-Data-Plattform bereitstellen und erste Datensätze veröffentlichen
- [ ] DCAT-AP-3.0-Metadaten implementieren und bei nationalem Datenkatalog registrieren
  (opendata.swiss für CH / GovData.de für DE)
- [ ] Parallelbetrieb sicherstellen: keine proprietären Systeme vor Abnahme der Nachfolger abschalten
- [ ] Erste messbare Einsparung (Per-Seat-Lizenzen) dokumentieren und öffentlich berichten

### Phase 3: Integration

- [ ] Decidim oder CONSUL Bürgerportal bereitstellen und mit Keycloak verbinden
- [ ] Camunda Workflow-Engine installieren und konfigurieren
- [ ] Form.io (oder vergleichbarer offener Form-Builder) installieren und mit XÖV / eCH-Datenmodellen verbinden
- [ ] GeoServer, QGIS-Server und MapLibre für Geodienste einrichten
- [ ] OGC-Konformität (WMS, WFS, WMTS) und INSPIRE-Konformität sicherstellen
- [ ] ISMS-Zertifizierungsvorhaben starten (Ziel: BSI IT-Grundschutz oder ISDS innerhalb von 24 Monaten)
- [ ] Alle neuen digitalen Dienste auf OZG-Konformität (DE) bzw. E-Government-Strategie-Konformität (CH) prüfen
- [ ] XÖV-Schemavalidierung (DE) oder eCH-Schemavalidierung (CH) für alle Datenaustaustauschpunkte implementieren

### Phase 4: Erweiterte Fähigkeiten

- [ ] DCAT-AP-3.0-Registrierung bei EU-Datenraum-Brokern durchführen (EU Data Act)
- [ ] Teilnahme an sektorspezifischen Datenräumen evaluieren (Mobilität, Energie, Umwelt)
- [ ] Verbleibende proprietäre Verträge bei Ablauf kündigen; Auszahlungskosten dokumentieren
- [ ] Zusätzliche EfA-Dienste aus FITKO-Portal beziehen (DE) oder Bundesdienste beziehen (CH)
- [ ] NIS2-Artikel-21-Konformität überprüfen und dokumentieren (DE und CH, soweit anwendbar)
- [ ] Regelmäßige Teilnahme an ZenDiS-Community (DE) oder eCH-Fachgruppen (CH) etablieren

### Phase 5: Optimierung und Skalierung

- [ ] ISMS-Zertifizierung abschließen (BSI IT-Grundschutz Basis-Zertifikat oder ISDS-Niveau)
- [ ] Lokal entwickelte Komponenten und Anpassungen auf openCode.de (DE) oder äquivalentem Repository (CH) veröffentlichen
- [ ] Steady-State-Betriebsmodell dokumentieren: Rollen, Verantwortlichkeiten, SLAs, Eskalationswege
- [ ] Jährlichen TCO-Review institutionalisieren und öffentlich berichten
- [ ] Fünfjährige Post-Migration-Evaluation planen: unabhängige Bewertung von TCO, Nutzerzufriedenheit und Zielerreichung
- [ ] Wissenstransfer an andere Kommunen aktiv unterstützen (OSOR-Fallstudie einreichen, FITKO-Netzwerk nutzen)
- [ ] Fortlaufende OpenSSF-Scorecard-Evaluierungen für alle Stack-Komponenten sicherstellen

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*
*Bitte zitieren als: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*
*Veröffentlicht: https://github.com/SEBK4C/Strategy-for-City-GovTech*
