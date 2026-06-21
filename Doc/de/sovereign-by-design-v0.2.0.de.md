---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf (Übersetzung)"
date: "2026-06-21"
language: "de"
translated-from: "en/sovereign-by-design-v0.2.0.md"
supersedes: "de/sovereign-by-design-v0.1.0.de.md"
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
  - Beschaffung
  - LibreOffice
  - KI-Gesetz
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur
**Korrespondenz:** sebk4c@tuta.com
**Version:** 0.2.0 — Zitationsvollständiger Entwurf (Übersetzung)
**Datum:** 2026-06-21
**Sprachen:** Deutsch (Übersetzung) · English (Quelle)
**Ersetzt:** v0.1.0 (2026-06-20)
**SPDX-License-Identifier:** CC-BY-4.0

> *Dieses Dokument ist eine vollständige Übersetzung des englischen Originals*
> *`en/sovereign-by-design-v0.2.0.md` (Quelldokument der Wahrheit).*
> *Strukturelle Änderungen werden zuerst im Quelldokument vorgenommen.*

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernächste Ebene demokratischer Administration, stehen jedoch vor einem strukturellen Dilemma: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellergebunden und nicht im Einklang mit öffentlichen Interessen. Diese Arbeit legt eine umfassende, zitationsvollständige Strategie für die Implementierung eines modernen, quelloffenen Verwaltungstechnologie-Stacks in Städten und Gemeinden vor. Auf der Grundlage vorbildlicher Praxis der Schweizer Bundesverwaltung (EMBAG-Gesetzgebung), des deutschen OZG-Reformprogramms und der Sovereign-Cloud-Stack-Initiative sowie der breiteren europäischen Souveränitätstechnologie-Gemeinschaft werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie von ersten Grundsätzen her erarbeitet. Zehn funktionale Technologieschichten — Identitätsmanagement, Dokumentenverwaltung, Büro-Produktivität, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformation, Cloud-Infrastruktur und KI — werden nach den Kriterien digitale Souveränität, Interoperabilität, Gesamtbetriebskosten und demokratische Eignung bewertet. Fünf detaillierte Implementierungsfallstudien (Barcelona, Gendarmerie Nationale, München, Jena und Kanton Zug) liefern die empirische Grundlage. Die Arbeit kommt zu dem Schluss, dass Open-Source-Technologiestacks nicht nur technisch realisierbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Jurisdiktionen gesetzlich vorgeschrieben sind. Die Version 0.2.0 integriert die vollständige Zitationsabdeckung für EU-Datengesetz, EU-KI-Gesetz, Cyberresilienzgesetz, eCH-Standards, Schweizer E-ID und ZenDiS.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Civic Technology, LibreOffice, KI-Gesetz, Beschaffung

---

## 1. Einleitung

Die digitale Transformation kommunaler Verwaltungen ist keine Frage des Ob, sondern des Wie. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; der Gesetzgeber fordert Interoperabilität und Datenschutz; Haushaltszwänge verlangen nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte und Gemeinden weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit gefangen: teure Lizenzverträge, fragmentierte Systeme und proprietäre Formate, die gute Verwaltungsarbeit eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut belegt: Herstellerbindung erhöht Wechselkosten und verschiebt Verhandlungsmacht zugunsten privater Anbieter [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Software verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Haushalte, die besser für die Daseinsvorsorge eingesetzt werden könnten [3, 5]. Am grundlegendsten: Wenn die Software demokratischer Institutionen im Besitz privater Akteure und durch diese kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Wohl und unternehmerischen Imperativen [4].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG (2023) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware grundsätzlich als Open Source veröffentlicht wird [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative stellen das ambitionierteste Open-Source-GovTech-Programm Europas dar [2, 3, 42]. Die Kampagne „Public Money? Public Code!" der FSFE, von über 200 Organisationen in 30 Ländern unterstützt, benennt das demokratische Prinzip [4]. Die Migration von rund 85.000 Arbeitsplätzen der Gendarmerie Nationale auf Ubuntu Linux und LibreOffice — mit ca. 40 Prozent Einsparungen bei den Arbeitsplatzkosten — belegt, dass groß angelegte Open-Source-Transitionen bei guter Steuerung gelingen [31].

Diese Arbeit fasst diese Entwicklungen zu einer Praxisstrategie für kommunale Verwaltungen zusammen. Sie richtet sich an alle relevanten Stakeholder — Stadtverwaltungen, Gemeinderäte, kommunale IT-Teams, Vergabestellen, Zivilgesellschaft, Open-Source-Gemeinschaften und Technologieanbieter — und liefert die Evidenzbasis, Technologiebewertung und den Implementierungsfahrplan für den Wandel.

### 1.1 Begriffserklärungen und Abgrenzungen

*Kommunale Verwaltung* bezeichnet Städte und Gemeinden einschließlich Schweizer Gemeinden, deutscher Kommunen (Gemeinden, Kreise, Städte) und vergleichbarer Strukturen. Die Strategie ist für Gemeinden von 5.000 bis über 500.000 Einwohnerinnen und Einwohnern ausgelegt.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten, die unter OSI-anerkannten Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Kommune kontrolliert oder ohne unzumutbaren Aufwand wechseln kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und zu migrieren, ohne Abhängigkeit von einem einzigen Anbieter [3].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunal-Technologiestack im Jahr 2026 aus?
2. Was lässt sich aus der schweizerischen, deutschen und europäischen Souveränitätstechnologie-Gemeinschaft lernen?
3. Was ist der optimale Phasenimplementierungsweg für eine Stadt mit 50.000–500.000 Einwohnerinnen und Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden, um die Erfolgschancen zu maximieren?

### 1.3 Warum Jetzt: Der regulatorische Moment 2026

Mitte 2026 stellt einen entscheidenden Wendepunkt dar. Mehrere sich überschneidende Regulierungsrahmen — jeder für sich bedeutsam — sind gleichzeitig in Kraft getreten und machen proprietäre, herstellergebundene kommunale IT rechtlich prekär und wirtschaftlich unattraktiv:

**Schweiz:** EMBAG trat am 1. Januar 2024 in Kraft und begründet eine Open-by-default-Pflicht für mit öffentlichen Mitteln entwickelte Software [1]. Die E-Government-Strategie Schweiz 2024–2027 überträgt diese Logik auf die Kantone und Gemeinden [16]. Das neue Schweizer E-ID-System, vom Parlament 2023 verabschiedet und ab 2025 schrittweise in Betrieb, bietet eine datenschutzfreundliche, staatliche digitale Identitätsinfrastruktur auf Basis verifizierbarer Nachweise [40].

**Deutschland:** OZG 2.0, verabschiedet 2024, verpflichtet alle Verwaltungsleistungen zur Online-Erbringung und schreibt Interoperabilität über BundID vor. FITKO koordiniert die Bundesumsetzung; ZenDiS GmbH verwaltet OpenDesk als Referenz-Open-Source-Arbeitsplatz [25]. Das „Once-Only"-Prinzip und der EfA-Ansatz (Einer für Alle) schaffen starke wirtschaftliche Anreize für kommunale Kooperationsbeschaffung.

**Europäische Union:** Der Interoperable Europe Act (VO (EU) 2024/903, in Kraft seit Mai 2024) begründet bindende Interoperabilitätspflichten für alle öffentlichen Verwaltungen in der EU [6]. Das EU-Datengesetz (VO (EU) 2023/2854, anwendbar ab September 2025) regelt den Datenzugang für IoT-Daten, die für Smart-City-Anwendungen relevant sind [28]. Das EU-KI-Gesetz (VO (EU) 2024/1689) stuft mehrere kommunale KI-Anwendungen als hochrisikobehaftet ein und verlangt Konformitätsbewertungen [49]. Das Cyberresilienzgesetz (VO (EU) 2024/2847) führt Sicherheits- und Update-Pflichten für Software ein [48]. Die NIS2-Richtlinie (2022/2555), deren Umsetzungsfrist Oktober 2024 war, schafft Cybersicherheitspflichten für die öffentliche Verwaltung [27].

Kommunen, die jetzt handeln, bauen Compliance-Kapital auf. Kommunen, die abwarten, häufen kumulierende Regulierungsschulden an.

---

## 2. Methodik

Diese Arbeit verwendet einen Mehr-Methoden-Forschungsansatz:

**Systematische Literaturrecherche** peer-begutachteter Veröffentlichungen, grauer Literatur und Grundlagendokumente aus den Jahren 2010–2026 zu E-Government-Theorie, digitaler Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunaler Digitaltransformation.

**Vergleichende Politikanalyse** von Technologiegesetzen und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, ZenDiS) und der Europäischen Union (Interoperable Europe Act 2024, EU-Open-Source-Strategie 2020–2023, EU-Datengesetz 2023, EU-KI-Gesetz 2024).

**Technologiestack-Bewertung** anhand einer Scoring-Matrix: (a) Lizenzoffenheit, (b) Einsatzreife, (c) Community-Gesundheit, (d) Interoperabilitätsstandards-Konformität, (e) Sicherheitsprofil, (f) Gesamtbetriebskosten (TCO), (g) bestehende Verwaltungsimplementierungen.

**Fallstudienanalyse** von fünf kommunalen oder behördlichen Open-Source-Transitionen, ausgewählt, um ein breites Spektrum an Städtegrößen, nationalen Kontexten und Ergebnissen — einschließlich einer Fehlschlagstudie zur ausgewogenen Analyse — abzudecken.

**Stakeholder-Analyse** zur Kartierung der Interessen, des Einflusses und der Einbindungsbedarfe jeder Stakeholder-Gruppe.

Die Literaturrecherche ist als selbstverbesserndes System konzipiert: Quellenverzeichnis (`Mem/source-registry.md`) und Literaturrecherche-Status (`Mem/literature-review-state.md`) werden versioniert und quartalsweise aktualisiert.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in Behörden behandeln; (b) behördliche Digitaltransformationsstrategie betreffen; (c) zum europäischen, schweizerischen oder deutschen Regulierungskontext gehören; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern. Quellen vor 2010 wurden aufgenommen, wenn sie grundlegende theoretische Rahmenbedingungen setzen (z.B. Lathrop & Ruma 2010 [32]).

### 2.2 Einschränkungen

Dieses Dokument ist ein zitationsvollständiger Entwurf (v0.2.0). Technologiestack-Bewertungen spiegeln den Stand öffentlich verfügbarer Informationen per Juni 2026 wider. Implementierungskostenschätzungen sind indikativ und müssen gegen lokale Beschaffungsbedingungen validiert werden.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die wissenschaftliche Literatur zum E-Government hat sich durch vier breite Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Erstellung von Verwaltungswebseiten [29]. Die zweite Generation (2005–2012) betonte Online-Dienstleistungserbringung, Bürgerportale und Back-Office-Integration [7]. Die dritte Generation (2012–2020) brachte Open Data, Partizipationsplattformen und Mobile-first-Design [8]. Die aktuelle vierte Generation (2020–heute) ist durch Platform Government, digitale Identitätsinfrastruktur, Datenräume und den Souveränitätswandel geprägt — die Erkenntnis, dass digitale Autonomie eine Voraussetzung demokratischer Selbstverwaltung ist [45].

Wirtz und Weyerers holistisches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Kommunale Verwaltungen in der Schweiz und Deutschland zeigen variable Ergebnisse über diese Dimensionen; technische Infrastruktur und Prozessqualität hinken den Bürgererwartungen in den meisten Jurisdiktionen hinterher, während der Regulierungsrahmen zunehmend Transparenz und Interoperabilität vorschreibt [1, 2, 45].

Lathrop und Rumas grundlegendes Sammelwerk *Open Government: Collaboration, Transparency, and Participation in Practice* (2010) formulierte die philosophischen und praktischen Argumente für offene Verwaltung, die die spätere Gesetzgebungswelle in Europa vorwegnahmen [32]. Ihr Argument — dass Offenheit und Interoperabilität Voraussetzungen demokratischer Rechenschaftspflicht sind, nicht bloß technische Präferenzen — bleibt das normative Fundament der Politikentwicklungen der 2020er Jahre.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept der digitalen Souveränität hat sich von einem akademischen Begriff zu einem politischen Imperativ im europäischen Kontext entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte „Teilen und Wiederverwenden" als Kernprinzip [5]. Der Interoperable Europe Act 2024 schafft bindende Interoperabilitätspflichten für alle öffentlichen Verwaltungen [6].

Deutschlands Sovereign Cloud Stack (SCS), entwickelt von der Open Source Business Alliance (OSBA) und durch das BMWK gefördert, ist die konkreteste Umsetzung digitaler Souveränität in der Cloud-Infrastruktur [3]. Die Schweizer Herangehensweise unterscheidet sich institutionell, konvergiert aber auf denselben Grundsätzen. EMBAG (in Kraft ab 1. Januar 2024) verpflichtet zur Open-Source-Veröffentlichung öffentlich finanzierter Bundessoftware [1]. Die GovStack-Initiative, gemeinsam von ITU und GIZ geführt, trägt einen internationalen Baustein-Rahmen für souveräne digitale Verwaltungsdienste bei [18].

### 3.3 Das deutsche OZG-Ökosystem und ZenDiS

Das Onlinezugangsgesetz (OZG), verabschiedet 2017 und wesentlich reformiert 2024 (OZG 2.0), verpflichtet alle deutschen Verwaltungen zur Online-Erbringung ihrer Leistungen [2]. OZG 2.0 adressiert Mängel der ersten Generation — fragmentierte Umsetzung, mangelnde Interoperabilität, inkonsistente Nutzererfahrung — durch das „Once-Only"-Prinzip, den EfA-Ansatz und eine föderale Plattformarchitektur rund um BundID und FITKO [9, 10].

ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) wurde 2022 von der Bundesregierung gegründet, um souveräne Open-Source-Software für den öffentlichen Sektor zu entwickeln und zu verwalten [25]. ZenDiS betreut OpenDesk — eine kuratierte Open-Source-Desktop- und Kollaborationssuite — und bietet Rahmenbedingungen für Bundes-, Landes- und zunehmend kommunale Behörden für den Zugang zu professionell verwalteter Open-Source-Arbeitsplatzsoftware. OpenDesk bündelt Nextcloud, Cryptpad, OpenProject, BigBlueButton, Element/Matrix und Collabora Online in einer einheitlichen, wartbaren Suite.

Die openCode.de-Plattform, betrieben von Digitalservice GmbH des Bundes, bietet ein zentrales Repository für quelloffene Verwaltungssoftware mit über 400 Repositories (Stand 2026) [10]. Das EU Open Source Observatory (OSOR) belegt im Jahresbericht 2023, dass die Open-Source-Adoption im öffentlichen Sektor seit 2020 in allen Mitgliedstaaten kontinuierlich gewachsen ist, mit Deutschland, Frankreich und der Schweiz unter den Führenden [38]. Dataport AöR und AKDB repräsentieren das kooperative Modell kommunaler IT-Leistungserbringung [24, 50].

### 3.4 Schweizerische Kantonal- und Bundesdigitaldienste

Zu den wichtigsten digitalen Infrastrukturen der Schweiz zählen:

**Fedlex** (fedlex.admin.ch): die amtliche Plattform für Bundesrecht auf Basis offener Standards [1].

**opendata.swiss**: das nationale Open-Government-Data-Portal auf CKAN-Basis [44].

**GEVER**: das standardisierte Geschäftsverwaltungssystem der Bundesverwaltung als Vorbild für kantonale und kommunale Umsetzungen [43].

**Schweizer E-ID**: Nach der Ablehnung des ersten E-ID-Vorschlags in der Volksabstimmung vom März 2021 — bei der die Stimmbevölkerung die Beteiligung privater Anbieter an der digitalen Identitätsinfrastruktur ablehnte — entwickelte der Bundesrat ein neues Modell auf Basis von Self-Sovereign Identity (SSI). Das revidierte E-ID-Gesetz wurde Ende 2023 von der Bundesversammlung verabschiedet und das System ab 2025 schrittweise eingeführt [40]. Die neue E-ID ist staatlich ausgestellt, datenschutzfreundlich konzipiert und integriert sich über OpenID Connect und verifizierbare Nachweise mit Keycloak-basierten Identitätsverbünden.

**eCH-Standards**: Der Verein eCH (E-Government Standards) veröffentlicht die schweizerischen XML-Interoperabilitätsstandards, die das funktionale Äquivalent der deutschen XÖV-Familie sind [15]. Für Gemeinden besonders relevant: eCH-0007 (Gemeinderegister), eCH-0010 (Postadressregeln), eCH-0011 (Meldewesen), eCH-0020 (Ereignismeldung) und eCH-0058 (Schnittstellendefinition für E-Government-Anwendungen). Die Konformität mit eCH-Standards ist Voraussetzung für die Integration in kantonale Systeme.

### 3.5 Europäischer Regulierungsrahmen

Der EU-Gesetzgebungsoutput 2022–2024 hat einen umfassenden Rahmen für digitale Souveränität in der öffentlichen Verwaltung geschaffen:

**Interoperable Europe Act (VO (EU) 2024/903):** In Kraft seit Mai 2024, verpflichtet dieser Act alle öffentlichen Verwaltungen in der EU, interoperable digitale Komponenten und Datensätze standardmäßig zu teilen, wiederzuverwenden und zu veröffentlichen [6]. Er verpflichtet zu Interoperabilitätsbewertungen für alle neuen IT-Systeme.

**EU-Datengesetz (VO (EU) 2023/2854):** Anwendbar seit September 2025, regelt es den Datenzugang für von vernetzten Geräten erzeugte Daten [28]. Für Kommunen, die Smart-City-Infrastruktur betreiben — vernetzte Straßenbeleuchtung, Parksensoren, Luftqualitätsmessgeräte — begründet das Gesetz spezifische Zugriffsrechte für Nutzer und öffentliche Stellen auf IoT-erzeugte Daten.

**EU-KI-Gesetz (VO (EU) 2024/1689):** Die Verordnung klassifiziert KI-Systeme nach Risikoklassen [49]. Mehrere kommunal relevante Anwendungen fallen unter Anhang III (hochrisikobehaftete KI-Systeme), einschließlich KI in der Verwaltung für Leistungs- oder Dienstleistungsentscheidungen, die Bürgerinnen und Bürger betreffen. Hochrisiko-Anwendungen erfordern eine Grundrechte-Folgenabschätzung, Mechanismen zur menschlichen Aufsicht, vollständige Dokumentation und Registrierung in der EU-KI-Datenbank.

**Cyberresilienzgesetz (VO (EU) 2024/2847):** In Kraft seit Oktober 2024 mit dreijähriger Umsetzungsfrist, führt das CRA verbindliche Cybersicherheits- und Update-Pflichten für Produkte mit digitalen Elementen ein [48]. Für Kommunen gilt: Beschaffungs-Due-Diligence sollte nunmehr auch den CRA-Compliance-Status kommerzieller Softwareanbieter umfassen.

### 3.6 Open-Source-Gemeinschaften und Souveränitätstechnologie

**Decidim** (Barcelona, 2016) ist eine Partizipationsdemokratieplattform, die von über 400 Organisationen in 40 Ländern genutzt wird, darunter Barcelona, Helsinki, New York und der Kanton Schaffhausen [12]. Barcelonas Einsatz hat über 70.000 Proposals verarbeitet und zeigt: Partizipationsplattformen erfordern nachhaltiges politisches Mandat über die Erstimplementierung hinaus.

**CONSUL Democracy** (Madrid, 2015) ist eine AGPL-3.0-lizenzierte Alternative, die in spanischsprachigen Städten und einigen europäischen Kommunen stark verbreitet ist [17].

**Matrix/Element** bietet ein offenes, dezentrales, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll, das von europäischen Behörden zunehmend eingesetzt wird. Der deutsche BundesMessenger, das französische Tchap und das britische MoD nutzen Matrix [14].

**Nextcloud** (Stuttgart, 2016) ist die am weitesten verbreitete Open-Source-Datei-Sync-und-Kollaborationsplattform in der europäischen öffentlichen Verwaltung [13]. Nextcloud Hub 7 (2025) integriert KI-gestützte Dokumentenzusammenfassung mit lokal gehosteten Modellen.

**OpenDesk**, betreut von ZenDiS GmbH, ist eine kuratierte Open-Source-Suite aus Nextcloud, Cryptpad, OpenProject, BigBlueButton, Element und Collabora Online [42]. Version 2.x (2025) bietet eine einheitliche, wartbare Bereitstellungseinheit mit ZenDiS-Beschaffungsleitfaden für Kommunen.

### 3.7 Implementierungsfallstudien

#### 3.7.1 Barcelona: Decidim Partizipationsdemokratie (2016–heute)

Barcelonas Einsatz von Decidim, initiiert 2016 unter der Colau-Verwaltung, ist die am gründlichsten dokumentierte Open-Source-Civic-Tech-Implementierung auf Stadtebene. Über 70.000 registrierte Nutzer, mehr als 100.000 Proposals, stadtweite partizipative Haushaltsprozesse und strategische Planungskonsultationen. Drei Schlüssellehren: (a) Partizipationsplattformen erfordern nachhaltiges politisches Mandat und Ressourcen über die Erstbereitstellung hinaus; (b) die Open-Source-Governance der Plattform selbst — durch den Decidim-Verein — schützt vor politischer Rücknahme; (c) die AGPL-3.0-Lizenz ermöglicht die Nutzung durch 400+ Organisationen weltweit, ohne dass Barcelona die Kontrolle über eigene Daten oder Anpassungen verliert.

#### 3.7.2 Gendarmerie Nationale: Linux-Migration (2008–2014)

Die Migration von rund 85.000 Arbeitsplätzen der Gendarmerie Nationale von Windows auf Ubuntu Linux und von Microsoft Office auf OpenOffice/LibreOffice (2008–2014) ist die größte dokumentierte groß angelegte Open-Source-Desktop-Migration in der europäischen öffentlichen Verwaltung [31]. Geleitet von Oberstleutnant Xavier Guimard, verlief die Migration in strukturierten Wellen mit umfangreicher Mitarbeiterschulung. Ergebnisse: ca. 40 Prozent Reduktion der Arbeitsplatzkosten; deutlich reduzierte Herstellerabhängigkeit; verbesserte Update-Agilität. Die Linux-Umgebung der Gendarmerie ist weiterhin in Betrieb. Das französische Modell belegt: Open-Source-Desktop-Migration gelingt im großen Maßstab, wenn sie professionell gesteuert wird.

#### 3.7.3 München LiMux: Eine strukturelle Analyse (2003–2017)

Das LiMux-Projekt der Stadt München ist das meistzitierte Beispiel einer kommunalen Open-Source-Transition, die anschließend rückgängig gemacht wurde. Die technische Implementierung — Migration von rund 15.000 Arbeitsplätzen auf Ubuntu Linux und LibreOffice — war weitgehend erfolgreich. Post-Mortem-Analysen führen die Rücknahme 2017 primär auf folgende Ursachen zurück: (a) Führungswechsel 2014 mit engeren Beziehungen zu Microsoft; (b) aggressives Anbieter-Lobbying; (c) unzureichendes Management der Kompatibilität mit staatlichen Bayern-Systemen; (d) angestaute Nutzerunzufriedenheit durch unzureichende Trainingsfinanzierung [30]. Münchens Erfahrung invalidiert Open-Source-Transitionen nicht; sie bestätigt den Vorrang politischen Risikomanagements. Bezeichnend: München initiierte in den frühen 2020er Jahren erneut ein Open-Source-Evaluierungsprogramm.

#### 3.7.4 Jena: Kooperative OZG-Implementierung

Die Stadt Jena (ca. 113.000 Einwohner) zeigt, wie eine mittelgroße deutsche Kommune OZG-Dienste durch kooperative Beschaffung erfolgreich implementiert. Über das Thüringer IT-Kooperationsrahmen (TIT) werden OZG-konforme Dienste entwickelt und betrieben, die von allen 17 thüringischen Kreisen und der Landeshauptstadt geteilt werden. Das Modell demonstriert das EfA-Prinzip in der Praxis: Jena trägt zum geteilten Pool bei, erhält Zugang zu allen von anderen entwickelten Diensten und wahrt die Souveränität durch die öffentlich-rechtliche Governance von TIT. Die jährlichen Technologiekosten für Jena über TIT sind ca. 40 Prozent niedriger als vergleichbare Einzelbeschaffungen.

#### 3.7.5 Kanton Zug, Schweiz: Digitaler Vorreiter

Der Kanton Zug (ca. 130.000 Einwohner), bekannt als „Crypto Valley", ist auch im digitalen Verwaltungsbereich Vorreiter. Die Zuger Gemeindeverwaltung hat Self-Sovereign-Identity-Credentials für Bürgerdienste erprobt (ZugApp), Nextcloud für das kantonale Dokumentenmanagement eingesetzt und bewahrt Bürgerdaten auf kantonaler Infrastruktur. Zugs Ansatz belegt: Digitale Souveränität und Innovation sind komplementär, nicht konkurrierend.

### 3.8 Total-Cost-of-Ownership-Evidenz

Belastbare, unabhängige, komparative TCO-Studien für Open-Source- gegenüber proprietären kommunalen Stacks sind weiterhin rar. Die stärksten verfügbaren Evidenzpunkte:

**Gendarmerie Nationale (2008–2014):** Ca. 40 Prozent Reduktion der Arbeitsplatzkosten [31].

**Stadt Paris (2017):** Die Stadt Paris berichtete von Einsparungen von ca. 5 Millionen Euro im 5-Jahres-Zeitraum nach der Migration auf LibreOffice [51].

**Indikatives kommunales Stack-TCO-Modell (2026):**

| Komponente | Proprietär (jährlich/Nutzer) | Open Source gehostet (jährlich/Nutzer) | Open Source selbst gehostet (jährlich/Nutzer) |
|---|---|---|---|
| Produktivitätssuite | €200–300 | €80–150 | €30–60 |
| Dateispeicherung & Kollaboration | €120–200 | €60–100 | €20–50 |
| Videokonferenz | €100–180 | €40–80 | €15–40 |
| Identitätsmanagement | €50–100 | €20–40 | €10–25 |
| **Gesamt (indikativ)** | **€470–780** | **€200–370** | **€75–175** |

Für eine Stadt mit 50.000 Einwohnern und 500 IT-Nutzern beträgt die indikative 5-Jahres-Einsparung eines vollständig gehosteten Open-Source-Stacks gegenüber proprietären Alternativen ca. €675.000–€2.025.000. Implementierungskosten (€150.000–€500.000) werden innerhalb von 12–30 Monaten amortisiert.

### 3.9 Lücken in der Literatur

1. **Longitudinale TCO-Studien** über vollständige 10-Jahres-Zyklen fehlen noch.
2. **Nutzerforschung zur Bürgerzufriedenheit** mit Open-Source- gegenüber proprietären kommunalen Digitaldiensten ist in der Fachliteratur nahezu absent.
3. **Kleingemeindeeperspektiven** (unter 10.000 Einwohner) sind unterrepräsentiert.
4. **KI-Governance im kommunalen Open-Source-Kontext** ist ein völlig neues Forschungsfeld; empirische Literatur zu kommunalen Open-Source-KI-Systemen unter dem EU-KI-Gesetz fehlt.

---

## 4. Technologiestack-Analyse

Der kommunale Technologiestack lässt sich in zehn funktionale Schichten aufteilen. Die folgende Analyse bewertet die führenden Open-Source-Optionen für jede Schicht nach den in Abschnitt 2 definierten Kriterien.

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Bürgerinnen, Bürger und Personal authentifizieren; Identitäten dienstübergreifend verbinden; Single Sign-On (SSO) realisieren; nationale Identitätssysteme anbinden.

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für die öffentliche Verwaltung in Europa. Es implementiert OpenID Connect, OAuth 2.0 und SAML 2.0 und ermöglicht den Verbund mit nationalen Identitätssystemen (BundID in Deutschland, Schweizer E-ID über OpenID Connect, eIDAS für grenzüberschreitende EU-Authentifizierung).

| Kriterium | Wertung (1–5) | Hinweise |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Einsatzreife | 5 | Produktionserprobt, 10+ Jahre |
| Community-Gesundheit | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Sicherheitsprofil | 5 | CVE-reaktionsfähig, regelmäßig auditiert |
| TCO | 4 | Keine Lizenzkosten; Betriebsexpertise erforderlich |
| Verwaltungseinsätze | 5 | Weitverbreitet in EU-Verwaltungen |

### 4.2 Dokumentenverwaltung und Akten

**Funktion:** Amtliche Unterlagen speichern, abrufen, klassifizieren und aufbewahren; GEVER-konforme (CH) oder E-Akte-konforme (DE) Workflows verwalten.

**Empfohlene Komponenten: Nextcloud** (kollaborative Dateiverwaltung) + **OpenProject** (Projektverknüpfung) [13, 20]

Für Schweizer Gemeinden mit voller GEVER-Compliance eignen sich kantonale Lösungen (CMI, Fabasoft Community) als Compliance-Schicht mit Nextcloud als kollaborativer Frontend. Für deutsche Kommunen bieten AKDB E-Akte und Dataport DMS äquivalente E-Akte-Konformität auf Open-Source-Grundlagen.

| Kriterium | Wertung (1–5) | Hinweise |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 (Nextcloud); GPLv3 (OpenProject) |
| Einsatzreife | 5 | 400.000+ Organisationen weltweit |
| Community-Gesundheit | 5 | Nextcloud GmbH + große Community |
| Interoperabilität | 4 | WebDAV, CalDAV, CardDAV, CMIS, eCH-0160 |
| Sicherheitsprofil | 5 | ISO-27001-zertifiziertes Angebot |
| TCO | 5 | Keine Lizenz pro Nutzer (Community Edition) |
| Verwaltungseinsätze | 5 | Schweizer Bundesverwaltung, deutsche Länder und Kommunen |

### 4.3 Büro-Produktivitätssuite

**Funktion:** Textverarbeitung, Tabellenkalkulation, Präsentationen; Erstellung und Bearbeitung von Dokumenten für Personal und Bürger; OpenDocument-Format (ODF) als Speicherformat.

**Empfohlene Komponenten: LibreOffice** (Desktop) + **Collabora Online** (Browser) [47]

LibreOffice, betreut von The Document Foundation unter LGPL-3.0, ist die führende Open-Source-Office-Suite in der europäischen öffentlichen Verwaltung. Bedeutende Einsätze: Gendarmerie Nationale (85.000+ Arbeitsplätze) [31], Stadt Paris [51], spanische Nationalverwaltung, Bundesverwaltungsamt [52] und zahlreiche deutsche Kommunen. Collabora Online CODE bietet eine browserbasierte Alternative, die nativ mit Nextcloud und OpenDesk integriert und kollaboratives Bearbeiten ohne Desktop-Installation ermöglicht.

| Kriterium | Wertung (1–5) | Hinweise |
|---|---|---|
| Lizenzoffenheit | 5 | LGPL-3.0 (LibreOffice); MPL-2.0 (Collabora) |
| Einsatzreife | 5 | 200 Mio.+ Nutzer weltweit; Verwaltungseinsatz seit 2010 |
| Community-Gesundheit | 5 | Document Foundation + Collabora als kommerzieller Träger |
| Interoperabilität | 4 | ODF ISO 26300; OOXML-Import/-Export; OASIS-Standards |
| Sicherheitsprofil | 4 | Regelmäßige CVE-Behebung; BSI-evaluiert |
| TCO | 5 | Keine Lizenzkosten pro Nutzer |
| Verwaltungseinsätze | 5 | Französische Verwaltung, Bund und Kommunen Deutschland, EU |

**Formatstrategie:** Alle amtlichen Unterlagen im OpenDocument-Format (ODF, ISO 26300) speichern. OOXML-Import/-Export für die Bürgerkommunikation aufrechterhalten. Neue Dokumente ODF-first anlegen (entspricht KGSt-Empfehlung).

### 4.4 Workflow-Automatisierung und Geschäftsprozessmanagement

**Funktion:** Verwaltungsworkflows automatisieren; BPMN-Prozesse modellieren, ausführen und überwachen; XÖV (DE) und eCH (CH) Datenstandards integrieren.

**Empfohlene Komponente: Camunda Platform 8 Community Edition** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe verwaltungsrechtliche Prozesse und XÖV/eCH-Datenstandards-Integration [46, 15]. **Flowable** (Apache 2.0) ist eine leichtgewichtige Alternative, wenn das duale Lizenzierungsmodell von Camunda Beschaffungsprobleme verursacht.

### 4.5 Bürgerbeteiligung

**Funktion:** Konsultation, partizipativer Haushalt, Initiativensammlung, Deliberationsplattformen.

**Empfohlene Komponente: Decidim** [12]

Decidim ist die ausgereifteste und am weitesten verbreitete Open-Source-Partizipationsplattform weltweit. **Alternative: CONSUL Democracy** [17] — AGPL-3.0, besonders stark in spanischsprachigen Städten und einigen europäischen Behörden; etwas einfachere Administration für kleine Kommunen.

### 4.6 Kommunikation und Kollaboration

**Funktion:** Interne Kommunikation, Videokonferenzen, E-Mail, Kalender; sichere behördenübergreifende Kommunikation.

**Empfohlene Komponenten:**
- **Matrix/Element** für Messaging und sichere Behördenkommunikation [14]
- **BigBlueButton** für Ratssitzungen und öffentliche Anhörungen [34]
- **Jitsi Meet** für informelle Videokonferenzen [35]
- **Nextcloud Talk** für integrierte Teamkommunikation

Der deutsche BundesMessenger (auf Matrix-Basis) und das französische Tchap bieten Referenzimplementierungen für kommunale Kontexte.

| Komponente | Lizenz | Reife | Kernvorteil |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Produktiv | E2E-Verschlüsselung, Föderation, Behördenendorsement |
| BigBlueButton | LGPL-3.0 | Produktiv | Rats-/Anhörungsfokus, Aufzeichnung |
| Jitsi Meet | Apache 2.0 | Produktiv | Browserbasiert, kein Account erforderlich |
| Nextcloud Talk | AGPL-3.0 | Produktiv | Integriert mit Dateiverwaltung und Kalender |

### 4.7 Open-Data-Veröffentlichung

**Funktion:** Maschinenlesbare Datensätze veröffentlichen; kommunale Daten katalogisieren; API-Zugang bereitstellen; EU-Open-Data-Richtlinie und DCAT-AP-Standards erfüllen.

**Empfohlene Komponente: CKAN** [22]

CKAN ist die weltweit führende Open-Source-Open-Data-Portal-Software. opendata.swiss, data.gov, data.gov.uk und Dutzende weitere Portale nutzen CKAN. Das Plugin-Ökosystem unterstützt DCAT-AP, DCAT-AP.de, OGD-Schweiz und Harvesting aus übergeordneten Nationalkatalogen.

### 4.8 Geographische Informationssysteme

**Funktion:** Kartenbasierte Bürgerdienste; Stadtplanung; räumliche Datenpublikation; OGC-konforme APIs.

**Empfohlene Komponenten:**
- **QGIS** (GPL-2.0+) für räumliche Datenbearbeitung und -analyse [37]
- **GeoServer** (LGPL-2.0) für OGC-konforme WMS/WFS-Publikation
- **OpenStreetMap** (ODbL-1.0) als Kartierungsgrundlage [36]

Swisstopo-Daten (seit 2021 frei verfügbar) und BKG-Geodaten (Deutschland) bieten hochqualitative staatliche Basiskartendaten, die mit QGIS und GeoServer kompatibel sind.

### 4.9 Öffentliche Website und Content-Management

**Funktion:** Bürger-Website; Nachrichten; Serviceverzeichnis; Barrierefreiheit (WCAG 2.1 AA / BITV 2.0); Mehrsprachigkeit.

**Empfohlene Komponenten:**
- **TYPO3** (GPL-2.0): dominantes CMS für Schweizer und deutsche Verwaltungen; TYPO3-Verein bietet LTS, öffentliche Verwaltungserweiterungen und Barrierefreiheitszertifizierung [19]
- **Drupal** (GPL-2.0): starke internationale Erfolgsbilanz; Europäische Kommission und französische Kommunen

### 4.10 Cloud-Infrastruktur und Hosting

**Funktion:** Compute, Speicherung, Netzwerk, Container-Orchestrierung; Datensouveränität auf Infrastrukturebene.

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

SCS ist die strategisch wichtigste Infrastrukturentscheidung für europäische Kommunen. Es bietet einen vollständig quelloffenen Cloud-Stack (OpenStack + Kubernetes + Ceph), der selbst gehostet oder über zertifizierte SCS-Hoster (plusserver, OSISM, govdigital eG) betrieben werden kann.

| Kriterium | Wertung (1–5) | Hinweise |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 / vollständig offen |
| Einsatzreife | 4 | Produktiv in mehreren deutschen Ländern |
| Community-Gesundheit | 5 | OSBA-getragen, wachsende internationale Adoption |
| Interoperabilität | 5 | Offene APIs, OCI-Container-Standard |
| Sicherheitsprofil | 5 | BSI-IT-Grundschutz-kompatibel; deutschen Datenstädte |
| TCO | 4 | Keine Lizenz; Infrastruktur- und Betriebskosten |
| Verwaltungseinsätze | 4 | Deutsche Länder, wachsende kommunale Nutzung |

### 4.11 KI und Automatisierung

**Funktion:** Intelligente Dokumentenverarbeitung; Bürgeranfragen-Routing; Genehmigungstriage; Wissensbasis-Suche; Workflow-Optimierung; automatisierte Übersetzung.

Schlüsselkomponenten in 2026:

**Ollama** (MIT): ein selbst gehosteter LLM-Inferenz-Laufzeitraum, der populäre offene Modelle (Llama 3, Mistral, Phi-3, Qwen) unterstützt. Ermöglicht Kommunen, LLM-basierte Dienste auf eigener Infrastruktur bereitzustellen und Bürgerdaten souverän zu halten.

**AnythingLLM** (MIT): dokumentenbewusstes LLM-Interface für RAG (Retrieval Augmented Generation) über kommunale Wissensdatenbanken.

**n8n** (Sustainable Use Licence, selbst hostbar): Open-Source-Workflow-Automatisierungswerkzeug mit nativer KI-Integration.

**OpenWebUI** (MIT): Browser-basiertes Interface für lokal gehostete LLMs.

**EU-KI-Gesetz-Konformitätsrahmen:**

| Anwendung | Risikoklasse | Anforderungen |
|---|---|---|
| Interne Dokumentenzusammenfassung | Minimal | Keine über allgemeine Transparenz hinaus |
| Bürger-FAQ-Chatbot | Begrenzt | Transparenzhinweis für Bürger |
| Genehmigungstriage-Priorisierung | Hoch | Grundrechte-Folgenabschätzung, menschliche Aufsicht, Registrierung |
| Automatisierte Leistungsanspruchsprüfung | Hoch | Vollständige KI-Gesetz-Konformitätsbewertung |
| Biometrische Identifikation bei Bürgerveranstaltungen | Verboten | Nicht zulässig |

**Operatives Grundprinzip:** Alle KI-Entscheidungen mit Bürgerwirkung müssen erklärbar, einer menschlichen Überprüfung zugänglich und in dem gemeindlichen KI-Register dokumentiert sein.

### 4.12 Referenzarchitektur

```
+---------------------------------------------------------------+
|                    BÜRGERKONTAKTPUNKTE                        |
|         TYPO3/Drupal . Decidim . CKAN . Nextcloud            |
+---------------------------------------------------------------+
|                       DIENSTSCHICHT                          |
|    Camunda Workflows . XÖV/eCH-Formulare . GeoServer . QGIS  |
+---------------------------------------------------------------+
|                    KOLLABORATIONSSCHICHT                     |
|    Nextcloud . Matrix/Element . BigBlueButton . OpenProject  |
+---------------------------------------------------------------+
|                    PRODUKTIVITÄTSSCHICHT                     |
|    LibreOffice (Desktop) . Collabora Online (Browser)        |
+---------------------------------------------------------------+
|                     IDENTITÄTSSCHICHT                        |
|       Keycloak <-> BundID / Schweizer E-ID / eIDAS           |
+---------------------------------------------------------------+
|                      KI / AUTOMATISIERUNG                    |
|       Ollama . AnythingLLM . n8n . OpenWebUI                 |
+---------------------------------------------------------------+
|                    INFRASTRUKTURSCHICHT                      |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph     |
+---------------------------------------------------------------+
```

Alle Schichten kommunizieren über offene APIs und offene Standards. Die Container-Orchestrierung erfolgt durch Kubernetes [39], die relationale Datenpersistenz durch PostgreSQL [41] — beide auf dem Sovereign Cloud Stack betrieben. Datenaustausch über XÖV-Standards (Deutschland) [46] oder eCH-Standards (Schweiz) [15]. Sicherheit gemäß BSI-IT-Grundschutz (Deutschland) [26] oder Schweizer ISDS-Rahmen.

---

## 5. Implementierungsfahrplan

Der Implementierungsfahrplan umfasst 36 Monate in fünf Phasen. Jede Phase hat definierte Ergebnisse, Erfolgskriterien und Entscheidungsgatter. Phasen überlappen sich bewusst, um Dynamik zu erhalten und „Big Bang"-Transitionen zu vermeiden.

### Phase 0: Fundament (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand aufnehmen, Koalition aufbauen.

**Ergebnisse:**
- Digitaler Transformationslenkungsausschuss eingesetzt (Stadtführung + IT + Zivilgesellschaft)
- Ist-Zustand-Technologieaudit abgeschlossen
- Stakeholder-Engagement-Plan verabschiedet
- Beschaffungsrahmen etabliert (siehe Abschnitt 6)
- Absichtserklärung mit kooperativem IT-Anbieter (Dataport, AKDB, TIT, govdigital, Schweizer Kantons-IT-Genossenschaft)

**Erfolgskriterien:**
- Politisches Mandat gesichert (Gemeinderatsbeschluss oder Exekutiventscheid)
- Budgetrahmen genehmigt (siehe Abschnitt 5.7)
- Projektleitung mit ausreichender Seniorität und Entscheidungsbefugnis bestimmt

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundlegende Schichten aufbauen, von denen alles andere abhängt.

**Ergebnisse:**
- Sovereign-Cloud-Stack-Umgebung in Betrieb (eigener oder verwalteter Hoster)
- Keycloak-Identitätsprovider bereitgestellt und mit nationalem Identitätssystem verbunden
- Nextcloud-Basisbereitstellung für interne Kollaboration
- LibreOffice auf allen Mitarbeiterarbeitsstationen (parallel zu bestehender Suite für 6 Monate)
- Matrix/Element-Messaging für IT und Führung
- BSI-IT-Grundschutz- oder Schweizer-ISDS-Basisdokumentation vollständig

**Erfolgskriterien:**
- 100% der IT-Mitarbeitenden können sich via Keycloak-SSO authentifizieren
- Dateispeicherung von proprietärer Cloud nach Nextcloud migriert
- Grundlegendes verschlüsseltes Messaging für Führungskräfte in Betrieb
- Sicherheitsbaseline dokumentiert und von Datenschutzbeauftragtem genehmigt
- LibreOffice bereitgestellt und Schulung für Pilotabteilung (>20 Personen) abgeschlossen

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste fünf bürgerorientierte Dienste auf offener Infrastruktur migrieren oder aufbauen.

**Ergebnisse:**
- Fünf mengenstärkste Verwaltungsleistungen auf Camunda/XÖV (DE) oder Camunda/eCH (CH) bereitgestellt
- TYPO3 oder Drupal CMS-Migration mit WCAG-2.1-AA-Zertifizierung abgeschlossen
- Open-Data-Portal (CKAN) mit ersten 20 Datensätzen gestartet
- Decidim-Instanz für ersten Partizipationsprozess bereitgestellt
- LibreOffice vollständig ausgerollt; proprietäre Suite außer Betrieb genommen

**Erfolgskriterien:**
- 80% des Ziel-Transaktionsvolumens über neues System abgewickelt
- Keine Regression in Dienstverfügbarkeit gegenüber Ausgangszustand
- Erste Open-Data-Publikation live und durch nationalen Katalog geerntet

### Phase 3: Integration und Ausbau (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Dienstabdeckung auf 80% der Transaktionen ausbauen.

**Ergebnisse:**
- Alle Dienste über Keycloak-SSO verbunden
- Nextcloud mit Dokumentenmanagement- und GEVER/E-Akte-Workflows integriert
- GIS-Schicht in Betrieb (QGIS + GeoServer + Swisstopo/BKG-Basisdaten)
- 80% der Verwaltungsleistungen digitalisiert
- Behördenübergreifender Datenaustausch via XÖV/eCH in Betrieb
- Erste interne KI-Bereitstellung (Dokumentenzusammenfassung — minimales Risiko)

**Erfolgskriterien:**
- Papierlose Dienstleistungserbringung für 80% der Transaktionstypen
- Datenqualitätskennzahlen etabliert und öffentlich berichtet
- Erster jährlicher Open-Data-Bericht veröffentlicht
- KI-Nutzungsrichtlinie verabschiedet und veröffentlicht

### Phase 4: Optimierung und Community (Monate 22–30)

**Ziel:** Nutzererfahrung optimieren; Upstream-Beiträge leisten; Führungsposition etablieren.

**Ergebnisse:**
- Bürgerzufriedenheitsumfrage (Ziel: NPS > 40)
- Erste Beiträge an openCode.de / Upstream-Projekte
- Kommunale Open-Source-Community-of-Practice mit Partnerkommunen etabliert
- Performance-Benchmarks veröffentlicht
- EU-KI-Gesetz-Konformitätsregister für alle KI-Anwendungen eingerichtet

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; Replikation durch Nachbarkommunen vorbereiten.

**Ergebnisse:**
- Vollständiges Audit aller Softwarekomponenten auf Lizenzkonformität und CRA-Status
- Datensouveränität verifiziert (alle Daten auf SCS oder zertifiziertem SCS-Hoster)
- Replikations-Playbook für Nachbarkommunen auf openCode.de veröffentlicht
- Strategiepapier v1.0 veröffentlicht

**Erfolgskriterien:**
- Keine proprietären Einzelanbieter-Abhängigkeiten im kritischen Pfad
- Alle Daten auf souveräner EU-Infrastruktur
- Mindestens eine Nachbarkommune hat das Playbook übernommen

### 5.7 Budgetschätzungen nach Stadtgröße

Kostenbandbreiten sind indikativ und variieren je nach vorhandener Infrastruktur, Eigenkapazität und Genossenschaftsmitgliedschaft. Alle Angaben in EUR.

| Stadtkategorie | Einwohner | Phasen 0–1 | Phasen 2–5 | Jährlicher Betrieb (nach Migration) |
|---|---|---|---|---|
| Klein | 5.000–20.000 | €50.000–120.000 | €80.000–250.000 | €25.000–70.000 |
| Mittel | 20.000–100.000 | €120.000–350.000 | €250.000–800.000 | €70.000–250.000 |
| Groß | 100.000–500.000 | €350.000–1.200.000 | €800.000–3.000.000 | €250.000–900.000 |
| Metropole | 500.000+ | €1.200.000–5.000.000 | €3.000.000–15.000.000 | €900.000–4.000.000 |

**Hinweise:** (a) Kleine Kommunen sollten dringend einer Genossenschaft beitreten (Dataport, AKDB, TIT, govdigital, kantonale IT-Genossenschaft) — dies reduziert Phasen-0-1-Kosten um 40–70%. (b) Laufende Betriebskosten sinken gegenüber vergleichbaren proprietären Stacks über einen 5-Jahres-Horizont, sobald die Migrationskosten amortisiert sind. (c) Mitarbeiterschulungen sind die am häufigsten unterschätzte Budgetposition; mindestens 2 Schulungstage pro Mitarbeitendem pro wesentlichem neuen System einplanen.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Hauptinteresse | Einbindungsansatz |
|---|---|---|
| Bürgermeister / Verwaltungsspitze | Politischer Erfolg, Kosten, Bürgerzufriedenheit | Executive Briefing, Fortschrittsdashboard, TCO-Bericht |
| Gemeinderat | Aufsicht, demokratische Legitimität | Quartalsberichte, offene Ratssitzungen, jährliche Strategieüberprüfung |
| Kommunales IT-Team | Technische Machbarkeit, Arbeitsbelastung, Karriereentwicklung | Ko-Design, Schulung, Community-Mitgliedschaft, Konferenzbesuche |
| Vergabestelle | Rechtskonformität, Risiko, Wirtschaftlichkeit | Rahmenverträge, rechtliche Briefings, ZenDiS/BMI-Beschaffungsleitfaden |
| Mitarbeitende (Endnutzer) | Bedienbarkeit, Zuverlässigkeit, vertraute Werkzeuge | UX-Tests, Parallelbetrieb, Open-Source-Champions, Schulung |
| Bürgerinnen und Bürger | Dienstqualität, Datenschutz, Barrierefreiheit | Partizipatives Design via Decidim, Transparenzberichte, Barrierefreiheitstests |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Teilhabe, Datenrechte | Decidim-Plattform, öffentliche Roadmaps, Open-Data-Portal |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung, Nachhaltigkeit | openCode.de-Beteiligung, Upstream-Beiträge, gemeinsame Pflege |
| Souveräne Technologieanbieter | Partnerschaft, Bereitstellung, Referenzkunden | Zertifizierte Partnervereinbarungen, Ko-Entwicklung, Fallstudienpublikation |
| Datenschutzbeauftragter | DSGVO-Konformität, Privacy by Design | Privacy-by-Design-Review in jeder Phase, DSFA für alle bürgerseitig eingesetzten Systeme |
| Informationssicherheitsbeauftragter | NIS2/CRA-Konformität, IT-Grundschutz | Gemeinsame Erstellung der Sicherheitsbaseline, Penetrationstests-Abnahme |

### 6.2 Beschaffungsrahmen

Open-Source-Beschaffung erfordert einen anderen Rahmen als proprietäre Lizenzeinkäufe. Die Software ist kostenlos; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung. Grundprinzipien:

**1. Dienste beschaffen, keine Lizenzen.** Ausschreibungsunterlagen müssen auf Dienste (Implementierung, Hosting, Support, Updates) ausgerichtet sein, nicht auf Lizenzen.

**2. Das „Public Money? Public Code!"-Prinzip anwenden.** Alle vertraglich entwickelte Software muss unter einer OSI-anerkannten Open-Source-Lizenz veröffentlicht und auf openCode.de oder einem gleichwertigen öffentlichen Repository zugänglich gemacht werden [4]. EMBAG schafft dies als gesetzliche Anforderung auf Bundesebene; deutsche Kommunen sollten es als Beschaffungsrichtlinie übernehmen.

**3. Gesamtbetriebskosten bewerten.** Ausschreibungspunktbewertung muss ein 5-Jahres-TCO-Modell einschließen. Das indikative TCO-Modell in Abschnitt 3.8 bietet einen Rahmen.

**4. Interoperabilitätsstandards vorschreiben.** Alle beschafften Systeme müssen implementieren: XÖV (Deutschland) [46], eCH (Schweiz) [15], DCAT-AP (EU-Open-Data), OIDC/SAML2 (Identität), ODF (Dokumentenformat). Nicht-Konformität sollte ein Ausschlusskriterium sein.

**5. Zertifizierte kooperative Anbieter bevorzugen.** Für Infrastruktur und verwaltete Dienste SCS-zertifizierte Cloud-Betreiber oder Mitglieder von govdigital eG (Deutschland) oder Kantons-IT-Genossenschaften (Schweiz) bevorzugen [23].

**6. Ausstiegsplan in jeden Vertrag aufnehmen.** Jeder Managed-Service-Vertrag muss einen dokumentierten Migrationspfad enthalten: alle Daten in offenen Formaten, alle Konfigurationen exportierbar, mindestens 12 Monate Transitions-Support.

### 6.3 Schweizer Beschaffungsrecht (BöB)

Das Bundesgesetz über das öffentliche Beschaffungswesen (BöB, SR 172.056.1), grundlegend revidiert und seit 2021 in Kraft, regelt die Bundesbeschaffung. Für Open-Source-Kommunalbeschaffung relevante Bestimmungen:

- **Schwellenwert für wettbewerbliche Ausschreibung:** CHF 150.000 für Dienstleistungen (Bund). Kantonale Gemeinden folgen der Interkantonalen Vereinbarung über das öffentliche Beschaffungswesen (IVöB) und kantonalem Ausführungsrecht.
- **Dienstleistungsmodell:** Software-Lizenzen (kostenlos) unterliegen nicht dem Vergaberecht; zugehörige Dienste (Implementierung, Hosting, Support) oberhalb des Schwellenwerts schon. Das bedeutet: CKAN, Nextcloud, Keycloak und LibreOffice erfordern keinen Lizenz-Beschaffungsprozess — nur die Dienstleistungsverträge.
- **Open-Source-Präferenzklausel:** EMBAG Art. 9 begründet ein Open-by-default-Prinzip, das eine Bevorzugung von Open-Source-Lösungen in der Beschaffungsbewertung unterstützt. Kommunen können dies als Richtlinienkriterium übernehmen.
- **Rahmenverträge:** Die Bundesverwaltung veröffentlicht Rahmenverträge für IT-Dienste einschließlich Cloud-Hosting. Schweizer Kommunen können analoge kantonale Rahmenverträge aushandeln.

### 6.4 Deutsches Vergaberecht (GWB/UVgO)

Deutsches öffentliches Beschaffungswesen oberhalb der EU-Schwellenwerte unterliegt Teil 4 des GWB und der VgV. Unterhalb der Schwellenwerte gilt die UVgO. Relevante Bestimmungen:

- **Schwellenwert für wettbewerbliche Ausschreibung (2024):** €221.000 für Dienstleistungsaufträge (EU-Schwelle, VgV). Unterhalb: UVgO-Verfahren.
- **IT-spezifische Verträge:** EVB-IT (Ergänzende Vertragsbedingungen für IT) bieten Standardbedingungen für Verwaltungs-IT-Beschaffung. ZenDiS hat einen Open-Source-Beschaffungs-Leitfaden (2023) veröffentlicht, der mit EVB-IT kompatible Mustervertragsvorlagen enthält.
- **Dienstleistungsmodell:** Open-Source-Softwarelizenzen sind kostenlos und unterliegen nicht dem Vergaberecht. Die Beschaffung erfolgt ausschließlich für die Dienstleistungsebene.
- **Rahmenverträge:** govdigital eG bietet Rahmenverträge für SCS-basiertes Cloud-Hosting und OpenDesk an, die GWB-Teil-4-Anforderungen erfüllen. AKDB und Dataport AöR bieten ähnliche Strukturen für ihre Mitglieder. Kommunen, die diesen Genossenschaften beitreten, können im Rahmen bestehender Verträge beschaffen, ohne Einzelvergabeverfahren oberhalb der Schwellenwerte durchführen zu müssen.

### 6.5 Veränderungsmanagement

Open-Source-Transitionen scheitern häufig nicht an technischen, sondern an menschlichen Faktoren: Endnutzerwiderstand, unzureichende Schulung, mittleres Management Trägheit und politischer Rückzug unter Anbieter-Lobbying.

**Empfehlungen:**
- Einen **Digitalen Transformationschampion** auf politisch-senioraler Ebene mit explizitem, mehrjährigem Mandat und Budgethoheit bestimmen
- **Open-Source-Champions** in jeder Abteilung mit erweiterter Ausbildung und Peer-Support-Rolle einrichten
- Mindestens drei Monate **Parallelbetrieb** vor der Abschaltung kritischer Systeme
- **Frühe Erfolge** (Kosteneinsparungen, neue Fähigkeiten, Bürger-Feedback) dokumentieren und öffentlich kommunizieren
- Ein **öffentliches Transparenz-Dashboard** mit Migrationfortschritt, Kosten und Dienstqualitätskennzahlen betreiben
- **Personalräte und Gewerkschaften** frühzeitig einbinden: Rahmen als Kompetenzentwicklung und digitale Autonomie, nicht als Kostensenkung
- **Lobbying-Response-Plan** erstellen: Evidenzbasis für Open-Source-Entscheidungen vorab dokumentieren

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|
| Politischer Rückzug nach Wahl | Mittel | Hoch | In Satzung/Ordnung verankern; parteiübergreifenden Konsens aufbauen; Mitgliedschaft in Genossenschaften institutionalisieren |
| Anbieter-Lobbying / FUD-Kampagnen | Hoch | Mittel | TCO-Evidenz vorab dokumentieren; Zivilgesellschaft einbinden; Mandatsrationale öffentlich kommunizieren |
| Qualifikationslücken im IT-Team | Hoch | Mittel | Schulungsprogramm; kooperativer IT-Anbieter; Community of Practice; Gewinnung von Open-Source-Spezialisten |
| Integrationsfehler zwischen Stack-Schichten | Mittel | Hoch | Phasierter Rollout mit Entscheidungsgattern; Referenzarchitektur einhalten; Integrationstests an jedem Gatter |
| Datenverlust während Migration | Niedrig | Kritisch | Vollständiges Backup-Protokoll; Parallelbetrieb min. 3 Monate; gestufte Migration; unabhängige Backup-Verifikation |
| DSGVO / Datenschutzverletzung | Niedrig | Hoch | Privacy-by-Design in jeder Phase; DSB-Einbindung; DSFA für alle bürgerseitigen Systeme |
| Nutzerakzeptanzversagen | Mittel | Hoch | Veränderungsmanagement; UX-Tests; Schulung; Parallelsysteme; Abteilungs-Champions; Executive-Sponsorship |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI-IT-Grundschutz; Penetrationstests; Incident-Response-Plan; NIS2-Konformität; CRA-Bewusstsein |
| Community-Fragmentierung oder Projektaufgabe | Niedrig | Mittel | Nur Projekte mit kommerzieller Unterstützung oder großer Community einsetzen; Upstream beitragen; Community-Gesundheit überwachen |
| Kostenüberschreitung | Mittel | Mittel | Phasengesteuertes Budget; unabhängiges Projektbüro; offene TCO-Buchführung; Rücklage (20%) |
| KI-Gesetz-Nichtkonformität | Mittel | Hoch | KI-Gesetz-Konformitätsregister ab Phase 3; rechtliche Prüfung aller KI-Anwendungen |
| Interoperabilitätslücken mit Altsystemen | Mittel | Mittel | API-Mapping vor Migration; schrittweise Ablösung von Altsystemen; XÖV/eCH-Adapter |

### 7.2 Der Münchner Präzedenzfall

Das LiMux-Projekt der Stadt München ist in Abschnitt 3.7.3 detailliert analysiert. Zentrale Lektionen:

1. **Politische Institutionalisierung ist die Schlüsselrestriktion.** Digitale Souveränität als Prinzip in die digitale Strategie, Beschaffungsrichtlinie und idealerweise in eine kommunale Ordnung verankern.
2. **Interoperabilität mit staatlichen Systemen vorab verifizieren.** Münchens Kompatibilitätsprobleme mit bayerischen Staatssystemen waren vorhersehbar und vermeidbar.
3. **Schulungsfinanzierung ist unverzichtbar.** Mindestens 2 Schulungstage pro Mitarbeitendem pro wesentlichem Systemwechsel budgetieren.
4. **Anbieter-Lobbying einplanen.** Evidenzbasis für jede Open-Source-Entscheidung vorab dokumentieren. ZenDiS, FSFE und govdigital eG können Expertenunterstützung leisten.

### 7.3 Sicherheitsaspekte

Das BSI-IT-Grundschutz-Rahmenwerk bietet eine umfassende Sicherheitsbaseline, die unabhängig vom Lizenzmodell gilt [26]. Kernanforderungen:

- Sicherheitsupdates innerhalb von 14 Tagen nach Veröffentlichung; kritische Patches innerhalb von 72 Stunden
- Authentifizierung: BSI-Authenticator-Assurance-Level 2 (AAL2) für bürgerseitige Dienste, AAL3 für privilegierten Zugang
- Datenverschlüsselung: TLS 1.3 in Transit, AES-256 für sensible Kategorien in Ruhe
- Penetrationstests an jedem Phasengatter
- Incident-Response-Plan gemäß NIS2, jährlich getestet, mit CERT-Bund-Meldeverfahren integriert [27]
- Software-Stückliste (SBOM) im SPDX-Format für alle quelloffenen Komponenten, quartalsweise aktualisiert
- CRA-Konformität aller kommerziellen Anbieter prüfen [48]

### 7.4 KI-spezifische Risiken

**EU-KI-Gesetz-Nichtkonformität:** Das Einsetzen einer Hochrisiko-KI-Anwendung (Genehmigungstriage, Leistungsrouting) ohne Konformitätsbewertung, menschliche Aufsichtsmechanismen und EU-KI-Gesetz-Registrierung ist ein Regulierungsverstoß. Minderung: alle KI-Anwendungen vor Bereitstellung klassifizieren; anfangs nur minimale/begrenzte Risikoklassen einsetzen; Rechtsberatung für Hochrisikobewertungen einholen.

**Verzerrungen in automatisierten Bürgerentscheidungen:** LLM-basierte Dokumentenrouting- und Triagesysteme können systematische Verzerrungen gegenüber demografischen Gruppen aufweisen. Minderung: Open-Source-KI niemals als endgültiges Entscheidungssystem für einzelne Bürger ohne menschliche Überprüfung einsetzen; demografische Disparitäten in Ergebnissen quartalsweise überwachen.

**„Shadow AI" — unautoriserter Einsatz externer KI-Dienste:** Mitarbeitende, die kommerzielle Cloud-KI für die Verarbeitung von Bürgerdaten oder amtlichen Dokumenten nutzen, verursachen DSGVO-Verstöße und Sicherheitsrisiken. Minderung: souveräne selbst gehostete Alternative (OpenWebUI + Ollama) als Teil der KI-Schicht bereitstellen; klare KI-Nutzungsrichtlinie vor Phase 3 verabschieden und alle Mitarbeitenden schulen.

**Anbieterabhängigkeit bei KI-Funktionen:** Open-Source-Anwendungen (Nextcloud, TYPO3) bieten zunehmend KI-Funktionen, die standardmäßig externe APIs aufrufen. Diese Funktionen sorgfältig bewerten; Bereitstellungen mit lokal gehosteten Modellen oder Modellersatzmöglichkeiten bevorzugen.

---

## 8. Schlussfolgerung

Die in dieser Arbeit betrachtete Evidenz konvergiert in fünf Befunden:

**1. Open-Source-Kommunal-Technologiestacks sind technisch ausgereift, produktionserprobt und umfassend unterstützt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung — Identität, Dokumente, Büro-Produktivität, Workflows, Partizipation, Kommunikation, Open Data, GIS, Cloud-Infrastruktur und KI — kann durch Open-Source-Software mit dokumentierten, operativen Einsätzen in Partnerkommunen in ganz Europa gedeckt werden.

**2. Der Regulierungsrahmen in der Schweiz, Deutschland und der EU schreibt Open Source und Interoperabilität zunehmend vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland) und Interoperable Europe Act (EU) schaffen rechtliche Verpflichtungen, denen proprietäre, herstellergebundene Systeme dauerhaft nicht standhalten können. EU-Datengesetz, EU-KI-Gesetz und Cyberresilienzgesetz fügen weitere Compliance-Dimensionen hinzu, die mit transparenten, auditierbaren Open-Source-Systemen besser handhabbar sind.

**3. Das wirtschaftliche Argument ist auf einer 5-Jahres-TCO-Basis überzeugend.** Open-Source-Stacks eliminieren Nutzerlizenzgebühren — bei vergleichbaren proprietären Alternativen auf €470–780 pro Nutzer und Jahr geschätzt — und reduzieren das Risiko der Anbieterabhängigkeit. Kooperative Beschaffungsmodelle verteilen Implementierungskosten. Indikative Amortisationszeiten: 12–30 Monate je nach Stadtgröße.

**4. Die fünf Fallstudien belegen, dass Erfolg in allen Größenordnungen erreichbar ist.** Barcelona (große Stadt, Partizipationsplattform), Gendarmerie Nationale (85.000 Arbeitsplätze, Produktivitätssuite), Jena (mittlere Stadt, OZG-Kooperation), Kanton Zug (Vorreiterkanton, Identität und Dateien) und der Münchner Gegenfall (politisches Risikomanagement) definieren gemeinsam das Spektrum des Gelingenden und Scheiternden.

**5. Politische Nachhaltigkeit und Veränderungsmanagement sind die bindenden Restriktionen — nicht die Technologie.** Klares politisches Mandat, parteiübergreifende Institutionalisierung, echtes Schulungsinvestment und kommunizierte Früherfolge sind ebenso wichtig wie technische Planung. Der Münchner Fall bestätigt dies; Barcelona, Jena und Zug bestätigen das Umgekehrte.

Kommunen, die jetzt handeln, gewinnen First-Mover-Vorteile: gemeinsame Standards prägen, eigenes Know-how aufbauen, Beschaffungskomplexität mit zunehmend reifenden Rahmenwerken reduzieren und zu den Open-Source-Commons beitragen, die alle Kommunen teilen. Das Zeitfenster der regulatorischen Opportunität ist offen. Die Werkzeuge sind bereit. Die Beschaffungsrahmen existieren. Die einzig verbleibende Frage ist der politische Wille.

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0, schweizerische Bundesgesetzgebung]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0) — Novelle des Onlinezugangsgesetzes*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2024). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — [Apache 2.0 / CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [EU-Publikation, Open Access]

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R0903 — [EU-Recht, public domain]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2024). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/publikationen/jahresberichte — [DL-DE/Zero 2.0]

[10] openCode.de. (2022–2026). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open Access]

[11] Sovereign Cloud Stack Community. (2024). *SCS Technical Documentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy for Cities and Organizations*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2024). *Nextcloud for Government: Security, Sovereignty, and Collaboration*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [AGPL-3.0]

[14] The Matrix Foundation. (2024). *Matrix Specification v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[15] eCH (E-Government Standards Association). (2024). *eCH-Standards für E-Government-Anwendungen*. Bern: eCH. https://www.ech.ch/ — [Open Access]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open Access, schweizerische Bundesveröffentlichung]

[17] CONSUL Democracy. (2024). *CONSUL: Open Source Democracy for Cities and Organizations*. Madrid: Ayuntamiento de Madrid. https://consuldemocracy.org/ — [AGPL-3.0]

[18] GovStack Initiative. (2024). *GovStack: Building Blocks for Digital Government*. Genf / Berlin: ITU / Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ). https://www.govstack.global/ — [CC-BY-SA-4.0]

[19] TYPO3 Association. (2024). *TYPO3 in Public Administration*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [GPL-2.0]

[20] OpenProject GmbH. (2024). *OpenProject: Open Source Project Management for Government*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community (CNCF). (2024). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2024). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open Access]

[24] Dataport AöR. (2024). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open Access]

[25] ZenDiS GmbH. (2024). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Jahresbericht 2023*. Berlin: ZenDiS GmbH. https://zendis.de/ — [Open Access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html — [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 über Maßnahmen für ein hohes gemeinsames Cybersicherheitsniveau (NIS2)*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555 — [EU-Recht, public domain]

[28] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 — EU-Datengesetz*. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854 — [EU-Recht, public domain]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [UN Open Access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[31] Guimard, X. (2013). *Migration to Ubuntu Linux in the Gendarmerie Nationale: A Cost-Benefit Analysis*. Paris: Direction Générale de la Gendarmerie Nationale (DGGN). Zitiert in: FSFE Fallstudien. https://fsfe.org/activities/os/localgov.en.html — [Open Access]

[32] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0.

[33] Camunda Services GmbH. (2024). *Camunda Platform 8 Community Edition*. Berlin: Camunda. https://camunda.com/download/ — [Apache 2.0 Community; proprietär Enterprise]

[34] BigBlueButton Inc. (2024). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community / 8x8 Inc. (2024). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS: A Free and Open Source Geographic Information System*. https://www.qgis.org/ — [GPL-2.0+]

[38] Europäische Kommission / OSOR. (2023). *Open Source Observatory (OSOR) Annual Report 2023: Open Source in European Public Administration*. Brüssel: Europäische Kommission, Joinup. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — [CC-BY-4.0]

[39] Cloud Native Computing Foundation (CNCF). (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[40] Schweizerische Bundeskanzlei. (2023). *Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (E-ID-Gesetz)*. SR 161.5. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2024/291/de — [CC0, schweizerische Bundesgesetzgebung]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence, OSI-anerkannt]

[42] ZenDiS GmbH / BMI. (2024). *OpenDesk 2.x: Der digitale Arbeitsplatz der öffentlichen Verwaltung*. Berlin: ZenDiS GmbH. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [Open Access]

[44] opendata.swiss. (2024). *Open Government Data Switzerland*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0 Portal]

[45] Europäische Kommission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — [CC-BY-4.0]

[46] KoSIT (Koordinierungsstelle für IT-Standards). (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open Access]

[47] The Document Foundation. (2024). *LibreOffice*. Berlin: The Document Foundation. https://www.libreoffice.org/ — [LGPL-3.0 / MPL-2.0]

[48] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/2847 — Cyberresilienzgesetz (CRA)*. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R2847 — [EU-Recht, public domain]

[49] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 — Gesetz über Künstliche Intelligenz (KI-Gesetz)*. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689 — [EU-Recht, public domain]

[50] AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern). (2024). *AKDB: IT-Dienstleister für Kommunen in Bayern*. München: AKDB. https://www.akdb.de/ — [Open Access]

[51] Ville de Paris / DSTI. (2017). *Migration LibreOffice: Bilan 2012–2017*. Paris: Ville de Paris. Zitiert in: OSOR Fallstudien. https://joinup.ec.europa.eu/ — [Open Access]

[52] Bundesverwaltungsamt (BVA). (2023). *LibreOffice-Einsatz in der Bundesverwaltung*. Köln: BVA. https://www.bva.bund.de/ — [Open Access]

---

*Dieses Dokument wird unter der Creative-Commons-Lizenz Namensnennung 4.0 International (CC-BY-4.0) veröffentlicht.*
*Quellenangabe: Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur (sebk4c@tuta.com)*
*Version 0.2.0 — Zitationsvollständiger Entwurf — 2026-06-21*
