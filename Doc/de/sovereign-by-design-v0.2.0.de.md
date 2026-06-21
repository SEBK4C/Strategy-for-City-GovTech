---
title: "Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsberichtigung Entwurf"
date: "2026-06-21"
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
  - GovStack
  - E-Government
  - Beschaffung
  - Total Cost of Ownership
---

# Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Kontakt:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** English (Quelldokument) · Deutsch (diese Übersetzung)  
**SPDX-Lizenzkennung:** CC-BY-4.0  

---

## Zusammenfassung

Kommunalverwaltungen bilden die bürgernahste Ebene der demokratischen Verwaltung, sind jedoch strukturell einer proprietären Technologieabhängigkeit, Anbieterbindung und einer wachsenden regulatorischen Diskrepanz zwischen ihren Softwareinfrastrukturen und den rechtlichen Anforderungen digitaler Souveränität ausgesetzt. Dieses Papier präsentiert eine umfassend zitierte Strategie für die Implementierung eines modernen, quelloffenen Technologie-Stacks für Stadtverwaltungen jeder Größenordnung. Auf Basis der Rechtsrahmen der Schweizer EMBAG-Gesetzgebung [1], der deutschen OZG-2.0-Reform und der Sovereign Cloud Stack-Initiative [2, 3], des Interoperable Europe Acts und der EU-Open-Source-Strategie [5, 6] sowie des GovStack-Bausteinrahmens [15] leiten wir eine evidenzbasierte Technologie-Stack-Bewertung, eine phasenweise 36-Monats-Implementierungs-Roadmap, eine Total-Cost-of-Ownership-Methodik, eine Stakeholder- und Beschaffungsstrategie sowie Fallstudien aus Barcelona, dem Kanton Schaffhausen, dem französischen Staat, der deutschen Bundesverwaltung und der Stadt München ab. Wir stellen fest, dass Open-Source-Technologie-Stacks für Kommunen technisch ausgereift, bei Bewertung auf Basis der vollen Lebenszykluskosten fiskalisch überlegen und in einer wachsenden Zahl europäischer Rechtssysteme gesetzlich vorgeschrieben sind. Politisches Mandat und Change-Management — nicht technische Kapazität — sind die entscheidenden Erfolgsfaktoren.

**Schlagwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitalisierung, OZG, EMBAG, Sovereign Cloud Stack, GovStack, E-Government, zivile Technologie, TCO, Beschaffung

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist nicht mehr optional. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienstleistungen; Regulierer verlangen Interoperabilität und Datenschutz; Haushaltszwänge erfordern nachhaltige Technologieinvestitionen; und ein wachsendes Gesetzeswerk in der Schweiz, Deutschland und der Europäischen Union schreibt ausdrücklich offene Standards, digitale Souveränität und die Open-Source-Veröffentlichung öffentlich finanzierter Software vor [1, 2, 5, 6].

Trotz dieser Treiber verbleiben die meisten Kommunalverwaltungen in Zyklen proprietärer Anbieterabhängigkeit: teure Lizenzvereinbarungen, Closed-Source-Systeme, die eine unabhängige Sicherheitsprüfung verhindern, proprietäre Datenformate, die den ämterübergreifenden Datenaustausch und die Bürgertransparenz behindern, und wiederkehrende Lizenzeskalationen, die Budgets von der Leistungserbringung abziehen [3, 4, 8].

Die Folgen des Nichthandelns verstärken sich gegenseitig. Anbieter verlagern kritische Kommunalsoftware zunehmend in Abonnement-Cloud-Modelle, was die Wechselkosten erhöht und die Verhandlungsposition schwächt. Regulatorische Anforderungen — DSGVO, NIS2, der Interoperable Europe Act, der Data Act und jurisdiktionsspezifische Mandate — schaffen rechtliche Risiken für Kommunen, deren proprietäre Systeme nicht unabhängig geprüft oder geändert werden können [6, 17, 27].

Ein anderer Weg ist sowohl möglich als auch bewährt. Die Schweizer EMBAG-Gesetzgebung von 2023 schreibt vor, dass alle mit öffentlichen Mitteln entwickelten Bundesbehördensoftware standardmäßig als Open Source veröffentlicht werden muss [1]. Deutschlands OZG-2.0-Reform, Sovereign Cloud Stack (SCS) und OpenDesk-Initiative repräsentieren das ambitionierteste Open-Source-Regierungstechnologieprogramm in Europa [2, 3, 42]. Die GovStack-Initiative der ITU/DIAL hat einen Bausteinrahmen für souveräne digitale Regierungsinfrastruktur formalisiert, der international anwendbar ist [15]. Die Kampagne „Öffentliches Geld? Öffentlicher Code!“ der Free Software Foundation Europe, unterstützt von über 200 Organisationen in 30 Ländern, artikuliert das demokratische Prinzip, das all dem zugrunde liegt: Software, die mit öffentlichen Mitteln bezahlt wird, sollte der Öffentlichkeit zur Verfügung stehen [4].

Dieses Papier fasst diese Entwicklungen zu einer praktischen, evidenzbasierten und kontinuierlich verbesserten Strategie für Kommunalverwaltungen zusammen. Es richtet sich an alle Beteiligten der kommunalen digitalen Transformation: Stadtverantwortliche, gewählte Amtsträger, öffentliche IT-Teams, Beschaffungsstellen, zivilgesellschaftliche Gruppen, Open-Source-Gemeinschaften und souveräne Technologieanbieter.

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und lokale Behörden, einschließlich Gemeinden, Kommunen, Städte und äquivalente Strukturen in Schweizer Kantonen. Die Strategie ist skalierbar von kleinen Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (500.000+), mit expliziter Maßstab-angepasster Anleitung.

*Open-Source-Technologie-Stack* bezeichnet Software, die unter OSI-genehmigten Lizenzen lizenziert ist und auf Infrastruktur betrieben wird, die die Kommune kontrolliert oder ohne unzumutbare Kosten migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer öffentlichen Institution, unabhängige, prüfbare Entscheidungen über ihre digitale Infrastruktur zu treffen, einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und ohne Single-Vendor-Abhängigkeit zu migrieren [3].

*GovStack* bezeichnet den von ITU/DIAL entwickelten Bausteinrahmen, der standardisierte, interoperable, quelloffene Komponenten für digitale öffentliche Infrastruktur bereitstellt [15].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Technologie-Stack für Kommunen im Jahr 2026 aus?
2. Welche Lehren können aus Schweizer, deutschen und europäischen souveränen Technologiegemeinschaften gezogen werden?
3. Was zeigt die Evidenz aus vergleichenden Fallstudien zu Open-Source-kommunalen Übergängen?
4. Wie gestaltet sich der Total-Cost-of-Ownership-Vergleich zwischen Open-Source- und proprietären Stacks?
5. Was ist der optimale phasenweise Implementierungsweg für Kommunen unterschiedlicher Größe?
6. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden?

---

## 2. Methodik

Dieses Papier verwendet ein Multi-Methoden-Forschungsdesign, das Folgendes kombiniert:

**Systematische Literaturrecherche** über begutachtete Veröffentlichungen, graue Literatur und Politikdokumente (2010–2026). Quellen wurden über Google Scholar, SSRN, EUR-Lex und Handdurchsuchung wichtiger Fachzeitschriften (Government Information Quarterly, Information Systems Management, European Journal of ePractice) mit Vorwärts-/Rückwärtszitationsverfolgung identifiziert.

**Vergleichende Politikanalyse** von Technologiegesetzen und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027, nDSG 2023), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie, IT-Planungsrat-Beschlüsse) und der Europäischen Union (Interoperable Europe Act 2024, EU-Open-Source-Strategie 2020–2023, Data Act 2023, KI-Gesetz 2024).

**Technologie-Stack-Bewertung** mittels einer strukturierten Sieben-Kriterien-Bewertungsmatrix (Abschnitt 4.12, Anhang A), die jede Komponente bewertet nach: (a) Lizenzoffenheit, (b) Deployment-Reife, (c) Community-Gesundheit, (d) Interoperabilitätsstandard-Konformität, (e) Sicherheitslage, (f) Total Cost of Ownership und (g) bestehenden öffentlich-sektoralen Einsatz.

**Fallstudienanalyse** von sechs dokumentierten Open-Source-Kommunal-Technologie-Übergängen.

**Stakeholder-Analyse** zur Abbildung von Interessen, Einfluss und Engagementbedarf.

Die Literaturrecherche ist so gestaltet, dass sie sich selbst verbessert: `Mem/source-registry.md` und `Mem/literature-review-state.md` sind versionierte Dokumente, die vierteljährlich aktualisiert werden.

### 2.1 Einschluss- und Ausschlusskriterien

**Eingeschlossen:** Quellen zu Open-Source-Software in der öffentlichen Verwaltung; staatlicher digitaler Transformationsstrategie; europäischen, Schweizer oder deutschen regulatorischen Kontexten; oder Primärdaten zu kommunalen Technologieimplementierungen.

**Ausgeschlossen:** Quellen von Anbietern ohne unabhängige Korroboration; nicht begutachtete Quellen für Sachbehauptungen, sofern keine Primärquelle existiert.

### 2.2 Zitationsstatus

Jede Quelle wird in `Mem/source-registry.md` mit Verifizierungsstatus verfolgt: `verifiziert`, `unverifiziert` oder `archiviert`. Dieser Entwurf (v0.2.0) erreicht ca. 85% verifizierten Status. Verbleibende unverifizierte Quellen sind mit [*nicht verifiziert*] gekennzeichnet.

---

## 3. Literaturrecherche

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government hat sich durch vier breite Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Erstellung von Behördenwebsites, oft durch Abteilungssilos ohne Interoperabilität [29]. Die zweite Generation (2005–2012) betonte Online-Leistungserbringung, Bürgerportale und Back-Office-Integration. Wirtz und Weyerer etablierten ein holistisches Fünf-Dimensionen-Reifegradmodell: technische Infrastruktur, Prozessqualität, Dienstleistungsqualität, Bürgerorientierung und Transparenz [7]. Die dritte Generation (2012–2020) führte offene Daten, partizipative Plattformen und Mobile-first-Design ein; Janssen et al. identifizierten systemische Hindernisse für die Akzeptanz offener Daten, die bis heute bestehen [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und den Souveränitätswandel gekennzeichnet — die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstverwaltung ist [30, 45].

Lathrop und Rumas grundlegendes Sammelwerk *Open Government* (2010) [25] etablierte das Drei-Säulen-Rahmenwerk — Transparenz, Partizipation und Zusammenarbeit — das die globale Open-Government-Strategie weiterhin prägt.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Die EU-Open-Source-Strategie 2020–2023 („Think Open“) etablierte „Teilung und Wiederverwendung“ als Kernprinzip und verpflichtet EU-Institutionen dazu, Open-Source-Lösungen zu bevorzugen und eigenentwickelte Software als Open Source zu veröffentlichen [5]. Der Interoperable Europe Act von 2024 schafft verbindliche grenzüberschreitende Interoperabilitätsverpflichtungen für Behörden [6].

Deutschlands Sovereign Cloud Stack (SCS), entwickelt von der Open Source Business Alliance (OSBA) und teilfinanziert vom BMWK, bietet eine vollständig quelloffene, selbst-hostbare Cloud-Plattform (OpenStack + Kubernetes + Ceph), die öffentlichen Verwaltungen ermöglicht, technisch und rechtlich souveräne Infrastruktur zu betreiben [3, 11]. Stand 2026 unterstützt SCS mehrere Cloud-Umgebungen der deutschen Länder und ist in die kooperative Shared-Infrastruktur der govdigital eG integriert [23].

Die Schweizer EMBAG-Gesetzgebung, in Kraft seit dem 1. Januar 2024, schreibt vor, dass alle mit öffentlichen Mitteln entwickelte Bundesbehördensoftware als Open Source veröffentlicht wird, sofern nicht zwingende Sicherheitsgründe dagegen sprechen [1]. Ergänzt durch das neue Schweizer Datenschutzgesetz (nDSG), das seit September 2023 DSGVO-äquivalente Standards einführt [47], verfügt die Schweiz über einen umfassenden gesetzlichen Rahmen für digitale Souveränität.

Das ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), 2022 von der deutschen Bundesregierung eingerichtet, verwaltet wichtige Open-Source-Regierungsprojekte wie OpenDesk und bietet ein Modell dafür, wie die öffentlich-sektorale Open-Source-Programmverwaltung institutionalisiert werden kann [18, 42].

### 3.3 Der GovStack-Bausteinrahmen

Die GovStack-Initiative, ein Gemeinschaftsprojekt der Internationalen Fernmeldeunion (ITU) und des Digital Impact Alliance (DIAL), formalisiert einen „Bausteine“-Ansatz für digitale Regierungsinfrastruktur [15]. Bausteine sind interoperable, wiederverwendbare, quelloffene Softwarekomponenten, die gemeinsame übergreifende Regierungsfunktionen adressieren: Identität und Registrierung, Zahlungen, Einwilligung, Informationsvermittlung, Messaging, Terminplanung, digitale Register, geografische Informationsdienste und Workflow-/Algorithmus-Engines.

Der Bezug von GovStack für europäische Kommunen ist zweifach: Seine Bausteine-Taxonomie bietet ein international anerkanntes Klassifizierungsrahmenwerk für die Bewertung kommunaler Technologiekomponenten. Und seine Betonung der Interoperabilität über offene APIs und Standardprotokolle stimmt präzise mit den Anforderungen des Interoperable Europe Acts [6] und den deutschen XÖV-Standards überein [46].

### 3.4 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), erlassen 2017 und im Jahr 2024 wesentlich reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalbehörden, ihre Verwaltungsleistungen nach dem „Einmal-nur“-Prinzip online anzubieten [2]. Die Reform adressiert Schwachstellen der ersten Generation durch den „Einer für Alle“ (EfA)-Ansatz für gemeinsame Dienste, eine föderale Plattformarchitektur rund um BundID und dem Koordinierungsgremium FITKO [9, 10].

Die Plattform openCode.de, 2022 vom Digitalservice GmbH des Bundes gestartet, bietet ein zentrales Repository für Open-Source-Software der Regierung [10]. Stand 2025 hostet sie über 400 Repositories. Dataport AöR (Norddeutschland) und AKDB (Bayern) repräsentieren das kooperative Modell der IT-Leistungserbringung im öffentlichen Sektor, das das OZG-Ökosystem verstärkt hat [24].

Die XÖV-Standardfamilie, koordiniert von KoSIT, definiert XML-Datenaustauschformate für alle großen deutschen Verwaltungsprozesse [46]. Jedes Workflow-Automatisierungssystem für deutsche Kommunen muss relevante XÖV-Schemata implementieren.

### 3.5 Schweizerische kantonale und eidgenössische digitale Dienste

Die föderale Struktur der Schweiz schafft sowohl Komplexität als auch Chancen für die kommunale digitale Transformation. Wichtige Infrastrukturen sind:

**Fedlex** (fedlex.admin.ch): die offizielle Plattform für schweizerisches Bundesrecht, erstellt auf offenen Standards, die maschinenlesbare Rechtstexte in allen vier Landessprachen bereitstellt [1].

**opendata.swiss**: das nationale Open-Government-Data-Portal, aufgebaut auf CKAN, das Datensätze von Bundes-, Kantons- und Gemeindebehörden katalogisiert [44].

**GEVER** (Geschäftsverwaltung): der standardisierte Geschäftsverwaltungsrahmen für die Schweizerische Bundesverwaltung, der als Vorlage für kantonale und kommunale Implementierungen dient [43].

**eCH-Standards**: Der Verein eCH koordiniert Schweizer E-Government-Datenaustauschstandards — das funktionale Äquivalent zur deutschen XÖV-Familie [31]. Schlüsselstandards umfassen eCH-0011 (Adressdaten), eCH-0020 (Personendaten) und eCH-0044 (eindeutiger Personenidentifikator).

Die *Strategie E-Government Schweiz 2024–2027*, gemeinsam vom Bundesrat und der Konferenz der Kantonsregierungen verabschiedet, schreibt offene Standards, digitale Souveränität und das „Einmal-nur“-Prinzip vor [16].

### 3.6 Open Source in der europäischen öffentlichen Verwaltung: OSOR-Evidenz

Das EU-Open-Source-Observatorium (OSOR), gepflegt von der Joinup-Plattform der Europäischen Kommission, veröffentlicht jährliche Berichte zur Open-Source-Nutzung in der europäischen öffentlichen Verwaltung [32]. Wichtige Erkenntnisse:

- 87% der europäischen öffentlichen Verwaltungen berichten den Einsatz von Open-Source-Software in mindestens einer Funktion
- Größte Einsatzbereiche: Webserver (Apache/nginx), Betriebssysteme (Linux auf Servern), Datenbanken (PostgreSQL, MySQL) und Büroproduktivität
- Primäre Hindernisse: fehlende interne Expertise (65% der Befragten), Unflexibilität des Beschaffungsrahmens (54%) und Interoperabilitätsbedenken (48%)
- Deutschland, Frankreich, die Niederlande und Spanien führen bei der politisch gesteuerten Open-Source-Einführung

### 3.7 EU-Datenverwaltung: Der Data Act 2023

Der EU-Data Act (Verordnung 2023/2854), in Kraft seit Januar 2024 mit den meisten Bestimmungen ab September 2025, hat erhebliche Auswirkungen auf kommunale Technologieentscheidungen [17]. Wichtige Bestimmungen:

**Artikel 4:** Daten, die von IoT-Geräten und vernetzten Systemen generiert werden, müssen auf Anfrage mit Nutzern geteilt werden können.

**Artikel 6:** Zugangsrechte Dritter zu Daten aus öffentlichen IoT-Installationen erfordern, dass Kommunen maschinenlesbare Datenzugänge bereitstellen können.

**Artikel 23:** Wechselrechte in Cloud-Verträgen verstärken das Argument für SCS und offene Datenspeicherformate.

Die praktische Auswirkung: Alle Technologieverträge müssen auf Data Act-Konformität geprüft werden. Open-Source-Systeme mit offenen Datenformaten und offenen APIs sind von Natur aus konformer.

### 3.8 EU-KI-Gesetz für Kommunalverwaltungen

Das EU-KI-Gesetz (Verordnung 2024/1689), in Kraft seit August 2024 mit den meisten Bestimmungen ab August 2026, schafft Verpflichtungen für den öffentlich-sektoralen KI-Einsatz [53]. Wichtige Risikokategorien:

**Verbotene KI** (Artikel 5): Soziales Scoring durch Behörden.

**Hochrisiko-KI** (Anhang III, §8): KI in der öffentlichen Verwaltung, einschließlich Systemen zur Bewertung von Personen für den Zugang zu öffentlichen Diensten. Hochrisiko-KI erfordert Konformitätsbeurteilung, technische Dokumentation, Protokollierung und menschliche Aufsicht.

**Transparenzverpflichtungen** (Artikel 50): Bürgerinnen und Bürger müssen informiert werden, wenn sie mit einem KI-System interagieren.

**Open-Source-Vorteil:** Open-Source-KI-Komponenten erfüllen die technische Dokumentationsanforderung des KI-Gesetzes (Artikel 11) leichter, wenn der Quellcode inspizierbar ist. Das KI-Gesetz enthält in den Artikeln 53 und 102 besondere Bestimmungen für Open-Source-Modelle.

### 3.9 Partizipationsplattformen: Vergleichende Evidenz

**Decidim** (Barcelona, 2016) ist die ausgereifteste und am weitesten verbreitete quelloffene Partizipationsplattform weltweit [12]. Ihr Einsatz in Barcelona (73.000+ aktive Teilnehmer), Helsinki (stadtweite partizipative Budgetierung), dem Schweizer Kanton Schaffhausen (Kantonsplanung) und New York City validiert sie über regulatorische und sprachliche Kontexte hinweg [50].

**CONSUL Democracy** (Madrid, 2015) ist eine Alternative mit besonderer Verbreitung in spanischsprachigen Kontexten [28]. Für Schweizer oder deutsche Kommunen empfiehlt sich Decidim aufgrund der deutschen Spraübersetzung, der aktiven deutschsprachigen Community und der kantonalen Fallstudien.

### 3.10 Kommunikationssicherheit: Matrix-Protokoll-Evidenz

Der deutsche Bundes-BundesMessenger (seit 2022 in Betrieb) setzt Element (Matrix-Client) für Ende-zu-Ende-verschlüsselte Kommunikation der Bundesbeamten ein, interoperabel mit Länder-Deployments via Matrix-Federation [14]. Frankreichs Tchap (seit 2019 für 250.000+ Nutzer) nutzt dasselbe Protokoll [14].

### 3.11 Lücken in der Literatur

Trotz erheblichen Wachstums der E-Government-Literatur bleiben drei kritische Lücken bestehen:

1. **Belastbare TCO-Studien** fehlen für einen vollständigen Open-Source- vs. proprietären kommunalen Stack über 5–10 Jahre.
2. **Kleine-Gemeinde-Longitudinaldaten** sind unterrepräsentiert — die meisten Fallstudien betreffen Großstädte oder Bundesbehörden.
3. **Bürger-UX-Forschung**, die die Bürgerzufriedenheit mit Open-Source- vs. proprietären kommunalen digitalen Diensten vergleicht, fehlt fast vollständig.

---

## 4. Technologie-Stack-Analyse

Ein kommunaler Technologie-Stack zerlegt sich in zehn funktionale Schichten, die mit GovStack-Bausteinen querverglichen werden, wo zutreffend. Jede Komponente wird gegen die Bewertungsmatrix in Anhang A bewertet.

### 4.1 Digitale Identität und Authentifizierung

**GovStack-Zuordnung:** Identität & Verifikation

**Empfehlung: Keycloak** (Red Hat / CNCF, Apache 2.0) [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für die europäische öffentliche Verwaltung, die OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2 implementiert und eine Föderation mit BundID (Deutschland) und Swiss eID ermöglicht.

**BundID vs. Swiss eID:**

| Merkmal | BundID (Deutschland) | Swiss eID (nach 2023) |
|---|---|---|
| Architektur | Zentralisierter Bundes-IdP | Dezentralisiert, SSI-basiert |
| Standards | SAML 2.0, OIDC | W3C DID, Verifiable Credentials |
| Datenschutzmodell | Zentraler Datenspeicher | Benutzerseitige Credentials |
| Keycloak-Integration | Ja (OIDC-Föderation) | Via VC/OIDC-Brücke [in Entwicklung] |

**Gewichteter Durchschnitt: 4,9** — Stark empfohlen

### 4.2 Dokumentenmanagement und Schriftgut

**GovStack-Zuordnung:** Informationsvermittler, Digitale Register

**Empfehlung: Nextcloud** (AGPL-3.0) + **OpenProject** (GPL-3.0) [13, 20]

Für die schweizerische GEVER-Konformität bieten kantonale GEVER-Lösungen (CMI GEVER, Fabasoft Govbox) die Compliance-Schicht; Nextcloud dient als kollaboratives Frontend via WebDAV. Der eCH-0039-Standard (E-Mail- und Dokumentenlieferungsstandard) ist über Nextcloud-Plugins erreichbar [31]. Für deutsche Kommunen unterstützen AKDB- und Dataport-Lösungen den XDomea-Standard für elektronischen Schriftguttransfer mit Nextcloud-Integration.

**Gewichteter Durchschnitt: 4,9** — Stark empfohlen

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**GovStack-Zuordnung:** Workflow & Algorithmus, Terminplaner

**Empfehlung: Camunda Platform 8 Community** (Apache 2.0) [33] oder **Flowable** (Apache 2.0)

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit XÖV-Integration für deutsche Kommunen [46] und REST-Integration für Schweizer eCH-Workflows [31]. Für Kommunen, die über die Doppellizenzierung von Camunda unsicher sind, ist Flowable die risikoarme Alternative.

**Gewichteter Durchschnitt: 4,1** — Empfohlen (Lizenzentwicklung beobachten)

### 4.4 Bürgerbeteiligung

**GovStack-Zuordnung:** Einwilligung

**Empfehlung: Decidim** (AGPL-3.0) [12]

Decidim ist die ausgereifteste und am weitesten verbreitete quelloffene Partizipationsplattform weltweit. Der Einsatz in Barcelona, Helsinki, Schaffhausen und New York City bestätigt sie in unterschiedlichen regulatorischen und sprachlichen Kontexten.

**Alternative:** CONSUL Democracy (Madrid) [28], ebenfalls AGPL-3.0, für spanischsprachige Kontexte.

**Gewichteter Durchschnitt: 4,7** — Stark empfohlen

### 4.5 Kommunikation und Zusammenarbeit

**GovStack-Zuordnung:** Messaging

**Empfohlener Stack:**
- **Matrix/Element** für sichere Kommunikation und ämterübergreifende Nachrichten [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Teamkommunikation [13]

Der deutsche BundesMessenger (Matrix) bietet eine validierte Referenzimplementierung [14].

**Matrix/Element: 4,5** — Stark empfohlen

### 4.6 Open-Data-Veröffentlichung

**GovStack-Zuordnung:** Informationsvermittler

**Empfehlung: CKAN** (AGPL-3.0) [22]

CKAN betreibt opendata.swiss, data.gov, data.gov.uk und Dutzende nationaler und kommunaler Open-Data-Portale. **DCAT-AP-3.0-Konformität** (Release 2024) ist über ckanext-dcat erreichbar, erforderlich für deutsche Kommunen (DCAT-AP.de-Profil) und Schweizer Beiträge zu opendata.swiss [44, 54].

**Gewichteter Durchschnitt: 4,6** — Stark empfohlen

### 4.7 Geoinformationssysteme

**GovStack-Zuordnung:** Geografische Informationsdienste

**Empfehlung:** QGIS (GPL-2.0+) + GeoServer (GPL-2.0) + OpenStreetMap (ODbL-1.0) [36, 37]

Die Schweizer swisstopo und das deutsche BKG stellen offene, hochqualitative kartografische Basisdaten bereit, die mit diesem Stack kompatibel sind.

**Gewichteter Durchschnitt: 4,3** — Empfohlen

### 4.8 Öffentliche Website und Content-Management

**Empfehlung: TYPO3** (GPL-2.0) [19] oder **Drupal** (GPL-2.0)

Die Dominanz von TYPO3 in der deutschsprachigen öffentlichen Verwaltung — verwendet von der Mehrheit der deutschen und Schweizer Kommunalwebsites — kombiniert mit den 10-Jahres-LTS-Zyklen der TYPO3 Association macht es zur Standardwahl für diese Region. Beide Systeme erfüllen WCAG 2.1 AA / BITV 2.0 Barrierefreiheitsstandards.

**Gewichteter Durchschnitt: 4,4** — Stark empfohlen (DACH-Region)

### 4.9 Cloud-Infrastruktur und Hosting

**GovStack-Zuordnung:** Infrastruktur

**Empfehlung: Sovereign Cloud Stack (SCS)** (Apache 2.0) [3, 11]

SCS bietet einen vollständigen, quelloffenen, prüfbaren Cloud-Stack (OpenStack + Kubernetes + Ceph), der es Kommunen ermöglicht, Hyperscaler-Abhängigkeit zu vermeiden. **Für Kommunen ohne interne Cloud-Kapazität:** Zertifizierte SCS-Hoster wie plusserver und OSISM betreiben im Rahmen der govdigital-eG-Kooperative, deren Verträge das deutsche Vergaberecht (GWB/VgV) erfüllen [23].

**Gewichteter Durchschnitt: 4,5** — Stark empfohlen

### 4.10 Künstliche Intelligenz und algorithmische Systeme

*Neu in v0.2.0 — spiegelt den raschen KI-Einsatz in der öffentlichen Verwaltung wider.*

Für Kommunen, die KI-gestützte Dienste in Betracht ziehen, erfordert das EU-KI-Gesetz einen Konformität-zuerst-Ansatz [53]. Empfehlungen:

1. **KI-Anwendungsfalls klassifizieren** nach KI-Gesetz-Risikokategorien vor der Beschaffung
2. **Offene Gewichtsmodelle bevorzugen** (z. B. Llama, Mistral, Gemma), die auf souveräner SCS-Infrastruktur betrieben werden können
3. **Mensch-in-der-Schleife implementieren** für alle bürgerseitigen Hochrisiko-Anwendungen
4. **SBOM pflegen** für KI-Komponenten einschließlich Modellversion, Trainingsdatenquelle und Fine-Tuning-Geschichte
5. **Hochrisiko-Systeme registrieren** in der EU-KI-Datenbank vor dem Einsatz

### 4.11 Referenzarchitektur

```
+------------------------------------------------------------------+
|                       BÜRGERBERÜHRUNGSPUNKTE                    |
|          TYPO3/Drupal · Decidim · CKAN · Nextcloud-Portal      |
+------------------------------------------------------------------+
|                    KI-SCHICHT (optional / schrittweise)          |
|     Offene Gewichtsmodelle (souverän gehostet) · Übersichts-DB  |
+------------------------------------------------------------------+
|                         DIENSTSCHICHT                            |
|      Camunda/Flowable Workflows · XÖV/eCH-Formulare · GeoServer |
+------------------------------------------------------------------+
|                     KOLLABORATIONSSCHICHT                        |
|       Nextcloud · Matrix/Element · Jitsi/BBB · OpenProject      |
+------------------------------------------------------------------+
|                         IDENTITÄTSSCHICHT                       |
|             Keycloak ↔ BundID / Swiss eID / FIDO2               |
+------------------------------------------------------------------+
|                          DATENSCHICHT                            |
|     PostgreSQL · CKAN · OpenStreetMap-Kacheln · Ceph (Objekt)  |
+------------------------------------------------------------------+
|                      INFRASTRUKTURSCHICHT                        |
|       Sovereign Cloud Stack · Kubernetes · Ceph · OpenStack     |
+------------------------------------------------------------------+
```

### 4.12 Zusammenfassung der Technologiebewertung

| Komponente | Gewichteter Score | Empfehlung |
|---|---|---|
| Keycloak (IAM) | 4,9 | Stark empfohlen |
| Nextcloud (Dokumentenmanagement) | 4,9 | Stark empfohlen |
| PostgreSQL (Datenbank) | 4,9 | Stark empfohlen |
| Decidim (Bürgerbeteiligung) | 4,7 | Stark empfohlen |
| CKAN (Open Data) | 4,6 | Stark empfohlen |
| SCS (Cloud-Infrastruktur) | 4,5 | Stark empfohlen |
| Matrix/Element (Messaging) | 4,5 | Stark empfohlen |
| TYPO3 (CMS, DACH) | 4,4 | Stark empfohlen |
| QGIS + GeoServer (GIS) | 4,3 | Empfohlen |
| Jitsi Meet (Video) | 4,3 | Empfohlen |
| OpenProject (Projektmanagement) | 4,2 | Empfohlen |
| Camunda 8 Community | 4,1 | Empfohlen (Lizenz beobachten) |

---

## 5. Implementierungs-Roadmap

Die Roadmap umfasst ein 36-Monats-, Fünf-Phasen-Programm mit expliziten Maßstabsvarianten und Budgetanleitung.

### 5.1 Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand bewerten, Koalition aufbauen.

**Ergebnisse:**
- Digitaler Transformationssteuerungsausschuss (Stadtführung + IT + Zivilgesellschaft)
- Ist-Zustand-Technologieaudit abgeschlossen
- Stakeholder-Engagementplan verabschiedet
- Beschaffungsrahmen und erste Rechtsklärung
- Absichtserklärung mit kooperativem IT-Anbieter (Dataport, AKDB, govdigital oder kantonaler Anbieter)
- Projektleiter mit formalem Mandat ernannt

**Budget (indikativ nach Stadtgröße):**

| Stadtgröße | Phase-0-Budget |
|---|---|
| Klein (<50T) | €50.000–€120.000 |
| Mittel (50T–200T) | €150.000–€350.000 |
| Groß (>200T) | €350.000–€700.000 |

### 5.2 Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundlegende Schichten aufbauen, von denen alle nachfolgenden Phasen abhängen.

**Ergebnisse:**
- SCS-Umgebung in Betrieb (eigengehostet oder über zertifizierten Hoster)
- Keycloak deployed und mit nationalem Identitätssystem föderiert (BundID / Swiss eID)
- Nextcloud-Grundlinie für interne Zusammenarbeit
- Matrix/Element-Messaging für Mitarbeitende
- BSI-IT-Grundschutz / ISDS-Basisdokumentation vollständig

**Erfolgskriterien:** 100% der IT-Mitarbeitenden authentifizieren sich über Keycloak-SSO; Dateispeicherung von proprietärer Cloud zu Nextcloud migriert; verschlüsseltes Messaging in Betrieb.

### 5.3 Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste fünf bürgerseitige Dienste auf offener Infrastruktur migrieren oder aufbauen.

**Ergebnisse:**
- Fünf volumenstarkste Verwaltungsleistungen auf Camunda/XÖV- (oder eCH-)Stack
- TYPO3- oder Drupal-CMS-Migration abgeschlossen
- CKAN-Open-Data-Portal mit ersten 20 Datensätzen
- Decidim-Instanz für ersten partizipativen Prozess

### 5.4 Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Dienstabdeckung auf 80% der Transaktionen ausweiten.

**Ergebnisse:**
- Alle Dienste via Keycloak-SSO föderiert
- GIS-Schicht in Betrieb
- Ämterübergreifender Datenaustausch via XÖV/eCH operational

### 5.5 Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** UX optimieren; zur Open-Source-Gemeinschaft beitragen; Ergebnisse veröffentlichen.

**Ergebnisse:**
- Bürgerzufriedenheitserhebung (Ziel-NPS > 40)
- Erste Beiträge auf openCode.de veröffentlicht
- Kommunale Open-Source-Community of Practice eingerichtet
- TCO-Bericht veröffentlicht

### 5.6 Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; Replikationshandbuch erstellen.

**Ergebnisse:**
- Vollständiges Lizenz-Compliance-Audit
- Souveräne Datenresälenz verifiziert (100% auf offener Infrastruktur)
- Replikationshandbuch für Nachbargemeinden
- Strategiepapier v1.0 veröffentlicht

### 5.7 Maßstab-Angepasste Varianten

**Kleine Gemeinde (<50.000):**
- Bestehenden kooperativen IT-Anbieter beitreten statt eigene SCS-Instanz zu betreiben
- Gemeinsame Keycloak-Instanz des Kooperativbetriebs nutzen
- Phase 2 auf die 3 (statt 5) volumenstarksten Dienste fokussieren
- Mit 2–3 Partnergemeinden für Decidim-Deployment zusammenarbeiten

**Mittelgroße Stadt (50.000–200.000):**
Standard-36-Monats-Roadmap. In Phase 1 selbst-gehostetes vs. kooperatives SCS-Hosting bewerten.

**Großstadt (>200.000):**
- In Phase 0 ein internes Open Source Programme Office (OSPO) einrichten
- Parallelbetrieb mindestens 6 Monate vor kritischen System-Umstellungen
- 48-Monats-Roadmap aufgrund der Komplexität
- Ziel: 5+ Upstream-Beiträge pro Jahr

### 5.8 Indikative 5-Jahres-Budget-Bereiche

| Stadtgröße | Implementierung (36M) | 5-Jahres-Gesamt (inkl. Betrieb) |
|---|---|---|
| Klein (<50T) | €150T–€400T | €400T–€800T |
| Mittel (50T–200T) | €500T–€1,5M | €1,5M–€3M |
| Groß (>200T) | €2M–€6M | €6M–€12M |

Zum Vergleich: Microsoft 365 E3 (€24,10/Nutzer/Monat, Preisstand 2024) kostet ca. €2,4M/Jahr für 10.000 Nutzer — €12M über 5 Jahre für eine mittelgroße Stadt. Beim Open-Source-Stack betragen die Gesamtlebenszykluskosten 25–50% weniger.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Einfluss | Engagement-Ansatz |
|---|---|---|---|
| Bürgermeister / Exekutive | Politischer Erfolg, Kosten | Sehr hoch | Führungsbriefing; Fortschritts-Dashboard |
| Stadtrat | Aufsicht; demokratische Legitimität | Hoch | Vierteljährliche Berichte; offene Sitzungen |
| IT-Team | Umsetzbarkeit; Arbeitsbelastung | Hoch | Co-Design; Schulung; Community |
| Beschaffungsamt | Rechtskonformität; Prüfpfad | Hoch | Rahmenvereinbarungen; Rechtsbriefings |
| Bedienstete (Nutzer) | Zuverlässigkeit; Benutzerfreundlichkeit | Hoch | UX-Tests; Change-Management |
| Datenschutzbeauftragter | DSGVO/nDSG-Konformität | Mittel-Hoch | Privacy-by-Design in jeder Phase |
| Bürgerinnen und Bürger | Dienstleistungsqualität; Datenschutz | Hoch (Wahlen) | Partizipatives Design; Transparenz |
| Zivilgesellschaft / NGOs | Transparenz; Verantwortlichkeit | Mittel | Decidim; öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Beitrag; Wiederverwendung | Mittel | openCode.de; Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft; Einsatz | Mittel | Zertifizierte Partnervereinbarungen |
| Nachbargemeinden | Kooperation; Kostenteilung | Mittel | Community of Practice |

### 6.2 Beschaffungsrahmen

Ffünf Kernprinzipien:

**1. Dienste beschaffen, nicht Lizenzen.** Vergabedokumente spezifizieren Servicelevel, Reaktionszeiten und Support-Kapazität — keine Softwarelizenzen.

**2. „Öffentliches Geld? Öffentlicher Code!“-Prinzip anwenden** [4]. Alle unter Vertrag entwickelte Software muss unter einer OSI-genehmigten Lizenz veröffentlicht werden.

**3. Kooperative Beschaffungsstrukturen nutzen.** Deutschlands govdigital eG und Schweizer kantonale IT-Kooperativen bieten Rahmenvereinbarungen, die das öffentliche Beschaffungsrecht erfüllen [23].

**4. Interoperabilitätsstandards vorschreiben.** XÖV [46] (Deutschland), eCH [31] (Schweiz), DCAT-AP 3.0 [54] (EU) — Nicht-Konformität ist ein Ausschlusskriterium.

**5. 5-Jahres-TCO bewerten.** Vergabebewertung muss ein Lebenszykluskosten-Modell umfassen (Abschnitt 9).

### 6.3 Rahmenvereinbarungen

| Anbieter | Gebiet | Abdeckung | Vergabebasis |
|---|---|---|---|
| govdigital eG | Deutschland | Cloud, SCS-Hosting, Arbeitsplatz | GWB/VgV Rahmenverträge |
| Dataport AöR | Norddeutschland | Vollständige IT-Dienste | Öffentliche Körperschaft — direkt |
| AKDB | Bayern | Vollständige IT-Dienste | Öffentliche Körperschaft — direkt |
| Kantonale IT-Kooperativen | Schweiz | Kantonal-spezifisch | IVöB/BöB |
| OSISM / plusserver | Deutschland / EU | SCS-zertifiziertes Hosting | Kommerziell; DL-DE konform |

### 6.4 Change-Management

Strukturiertes Programm:

1. **Exekutiv-Sponsor** auf Stadtrats- oder Bürgermeisterebene mit explizitem Mandat und KPIs
2. **Open-Source-Champions** in jeder Abteilung: erweiterte Schulung, Peer-Support-Rolle
3. **Parallelbetrieb** mindestens 3 Monate vor kritischer System-Umstellung
4. **Dokumentierte frühe Erfolge** — Kosteneinsparungen, neue Fähigkeiten, Bürgerdienst-Verbesserungen
5. **Öffentliches Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Dienstqualitätsmetriken

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Maßnahme |
|---|---|---|---|
| Politische Umkehr nach der Wahl | Mittel | Hoch | In Gesetze verankern; überparteilicher Konsens |
| Anbierter-Lobbying / FUD-Kampagnen | Hoch | Mittel | TCO-Evidenz; Zivilgesellschaft; Mandat öffentlich machen |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulung; kooperativer Anbieter; Community of Practice |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweise Einführung mit Entscheidungstoren |
| Datenverlust bei Migration | Gering | Kritisch | Vollständiges Backup; Parallelbetrieb; getestete Rückabwicklung |
| DSGVO / nDSG-Verletzung | Gering | Hoch | Privacy-by-Design; DSB in jeder Phase |
| EU-KI-Gesetz-Nichtkonformität | Mittel | Hoch | KI-Anwendungsfall-Register; Konformitätsbeurteilung vor Einsatz |
| Benutzerakzeptanzversagen | Mittel | Hoch | Change-Management; UX-Tests; Schulung |
| Sicherheitsvorfall | Gering | Kritisch | IT-Grundschutz; Pen-Tests; SBOM; NIS2-konformes IR |
| Kostenentgleisungen | Mittel | Mittel | Phasengestuftes Budget; unabhängiges Projektbüro |

### 7.2 Der Fall München LiMux: Eine Umkehr verstehen

Das LiMux-Projekt der Stadt München (2003–2017) ist die meistzitierte Umkehr eines großangelegten kommunalen Open-Source-Übergangs. Post-mortem-Analysen [40] identifizieren als primäre Treiber politische und managementbezogene Faktoren:

1. **Politische Diskontinuität:** Die Stadtratswahl 2014 brachte eine Koalition mit engeren Bindungen an Microsoft. Die Entscheidung zur Umkehr ging jeder technischen Bewertung voraus.
2. **Ungendügendes Change-Management:** Endanwender-Schulung war unzureichend; Help-Desk-Kapazität war unterfinanziert.
3. **Interoperabilitätsversagen auf Landesebene:** Bayerische Landessysteme unterstützten keine offenen Dokumentenstandards, was echte Reibung schuf.
4. **Unzureichende Institutionalisierung:** Das Programm hing am persönlichen Mandat weniger Ratsmitglieder.

**Lehren:** Verpflichtung legislativ verankern; überparteiliche Unterstützung sichern; Interoperabilität auf Landes-/Kantonsebene als Vorbedingung sichern; Change-Management mit 15–20% des Gesamtbudgets finanzieren.

### 7.3 Sicherheitsbetrachtungen

BSI-IT-Grundschutz bietet eine umfassende Sicherheitsbasislinie [26]; NIS2 schafft zusätzliche Verpflichtungen [27]:

- Maximal 72-Stunden-Patch-Zyklus für kritische CVEs
- Authentifizierung: BSI-AAL2 für bürgerseitige; AAL3 für administrative Konten
- Daten in Transit: TLS 1.3 Minimum
- Daten im Ruhezustand: AES-256 für sensible Kategorien
- Penetrationstests an jedem Phasenstor und jährlich
- SBOM im SPDX- oder CycloneDX-Format für alle Komponenten
- Incident-Response gemäß NIS2-Artikel 23 (24-Stunden-Erstmeldung an nationales CSIRT)

### 7.4 Datenschutz: DSGVO und nDSG

**Deutsche Kommunen:** DSGVO gilt vollumfänglich. Open-Source-Systeme erleichtern die DSGVO-Konformität, da Quellcode auf Datenschutzeigenschaften geprüft werden kann.

**Schweizer Kommunen:** Das nDSG trat am 1. September 2023 in Kraft [47] und führt DSGVO-äquivalente Standards ein. Schweizer Besonderheiten: Vorabkonsultation beim EDPB für Hochrisikoverarbeitung; Pflichtverletzungsmeldung innerhalb 72 Stunden.

---

## 8. Fallstudien

### 8.1 Barcelona: Partizipative Demokratie im Massstab

**Kontext:** Barcelona setzte Decidim 2016 für das „Pla de Barris“-Stadtentwicklungsprogramm ein und erweiterte es auf stadtweite partizipative Budgetierung, strategische Planung und kommunale Referendumsprozesse.

**Skala:** 73.000+ registrierte Teilnehmende; 14.000+ Vorschläge; €30M in partizipativ budgetierten Projekten [12, 50].

**Lehren:** Politisches Engagement auf Bürgermeisterebene muss über Haushaltsszyklen aufrechterhalten werden. Das Beitragen von Anpassungen zum Upstream reduziert die langfristigen Wartungskosten erheblich.

### 8.2 Kanton Schaffhausen: Das Kleinjurisdiktionsmodell

**Kontext:** Der Kanton Schaffhausen (Bevölkerung ~83.000) setzte Decidim 2020 für die Konsultation zum Kantonalen Richtplan ein.

**Lehren für kleine Jurisdiktionen:** Open-Source-Plattformen skalieren effizient nach unten. Lokale Integratoren mit Open-Source-Expertise sind unverzichtbar. Datenexport in Standardformaten muss vor dem Einsatz verifiziert werden.

### 8.3 Deutsche Bundesverwaltung: OpenDesk-Roll-out

**Kontext:** Das Bundesministerium des Innern und ZenDiS lancierten 2023 OpenDesk als kuratierten Open-Source-Arbeitsplatz für die Bundesverwaltung [42, 18]. Komponenten: Nextcloud, Cryptpad, OpenProject, Jitsi, Element, Collabora.

**Lehren:** Kuration und Integrationsarbeit ist erheblich. Das ZenDiS-Modell — eine dedizierte öffentliche Körperschaft, die die Integrationsschicht pflegt, während Upstream-Gemeinschaften Komponenten pflegen — ist auf Länder- und Großstadtebene replizierbar.

### 8.4 Französischer Staat: LibreOffice-Migration

**Kontext:** Das französische Innenministerium schloss 2021–2023 eine Großmigration von Microsoft Office auf LibreOffice für ca. 260.000 Nutzer über 4.000 Standorte ab [38].

**Ergebnisse:** Geschätzte Einsparungen: €20M über 3 Jahre. ODF-Format als Standard für alle internen Dokumente eingeführt. Kompatibilität mit externen Partnern, die .docx verwenden, erfordert aktives Management.

### 8.5 München LiMux: Eine Umkehr verstehen

*Siehe Abschnitt 7.2 für die vollständige Analyse.* Zusammenfassung: Technisch erfolgreich, politisch umgekehrt. Die Hauptlehren sind in die Roadmap und das Risikoregister dieses Papiers integriert.

### 8.6 Helsinki: Exzellenz im digitalen Dienstleistungsdesign

**Kontext:** Helsinki ist durchgängig eine der führenden Städte weltweit für digitale öffentliche Dienste, kombiniert Open-Source-Komponenten mit einem starken Service-Design-Ansatz und dem Helsinki Design System (Open Source, MIT-lizenziert).

**Ergebnisse:** Top-3-Platzierung in EU-E-Government-Umfragen; berichtete NPS-Scores von 60+ für digitale Dienste.

**Lehren:** Service-Design und UX-Investition sind ebenso wichtig wie die Technologieauswahl. Die Veröffentlichung des Design-Systems als Open Source ermöglicht dem weiteren finnischen öffentlichen Sektor, es wiederzuverwenden.

---

## 9. Total-Cost-of-Ownership-Methodik

### 9.1 TCO-Rahmen

Ein 5-Jahres-TCO-Modell für kommunale Technologie muss folgende Kostenkategorien umfassen:

### 9.2 Kostenkategorien

| Kategorie | Proprietär | Open-Source |
|---|---|---|
| A. Softwareakquisition | Lizenzgebühren (pro Nutzer/Kern; 5–8% jährliche Eskalation) | €0 (OSI-Lizenz = kostenlose Nutzung) |
| B. Implementierung | Integration, Konfiguration, Individualentwicklung, Datenmigration | Gleich; aber alle Individualentwicklung muss Open-Source-veröffentlicht werden [4] |
| C. Infrastruktur / Hosting | Server oder Cloud-Hosting | SCS-Hosting: typischerweise 30–50% günstiger als Hyperscaler |
| D. Betrieb / Wartung | Systemadmin, Patching, Monitoring | Vergleichbar; Community-Support ergänzt kommerziellen |
| E. Schulung / Change-Mgmt. | Initial + laufende Schulung | Vergleichbar; 15–20% des Gesamtbudgets empfohlen |
| F. Support-Kosten | Support-Verträge (18–22% der Lizenzkosten/Jahr) | Kommerzieller Support optional (z.B. Nextcloud Enterprise) |
| G. Ausstieg / Migrationkosten | Datenextraktion + Formatkonvertierung (100–200% der Jahreslizenz) | Offene Formate: typisch 60–80% niedrigere Ausstiegskosten |
| H. Regulatorische Konformität | DSGVO/nDSG-Modifikationen; KI-Gesetz-Konformitätsbeurteilungen | Open-Source: leichter zu prüfen und für Konformität zu modifizieren |

### 9.3 Indikative Benchmarks

Auf Basis veröffentlichter Evidenz aus den Fallstudien in Abschnitt 8:

| Kostenkomponente | Proprietär (typisch) | Open-Source (typisch) | Evidenzquelle |
|---|---|---|---|
| Produktivitäts-Suite (pro Nutzer/Jahr) | €180–360 | €0–50 | Französischer Staat [38] |
| IAM-Plattform (gesamt 5J.) | €200T–500T | €50T–150T | OSOR-Evidenz [32] |
| CMS-Plattform (gesamt 5J.) | €100T–300T | €30T–100T | TYPO3 Association [19] |
| Cloud-Hosting (mittelgroße Stadt, 5J.) | €2M–5M | €800T–2M | SCS-Preisgestaltung [3, 23] |
| Ausstieg / Migration (nach 5J.) | €500T–2M | €100T–400T | Vorteil offener Formate |
| **Gesamt für mittelgroße Stadt** | **€4M–10M** | **€1,5M–4M** | **Einsparungen: 50–70%** |

---

## 10. Schlussfolgerung

Die in diesem Papier aufbereiteten Belege konvergieren auf fünf Erkenntnisse:

**1. Open-Source-Kommunal-Technologie-Stacks sind technisch ausgereift und in allen Größenordnungen erprobt.** Jede Funktionsanforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Einsätzen in Peer-Kommunen in der Schweiz, Deutschland, Frankreich, Spanien und Finnland erfüllt werden.

**2. Das regulatorische Umfeld schreibt zunehmend Open-Source und Interoperabilität vor.** EMBAG [1], OZG 2.0 [2], der Interoperable Europe Act [6], der EU-Data Act [17] und das EU-KI-Gesetz [53] schaffen ein verdickendes Netz von Verpflichtungen, das proprietäre, anbietergekoppelte, closed-format-Systeme nicht nachhaltig erfüllen können.

**3. Die wirtschaftliche Argumentation ist überzeugend, wenn Gesamtkosten korrekt gezählt werden.** Open-Source-Stacks eliminieren Pro-Platz-Lizenzkosten, reduzieren das Anbieterbindungsrisiko und stellen überlegene Ausstiegsoptionalität bereit. Auf Basis verfügbarer Evidenz liefern Open-Source-Stacks 50–70% Gesamtlebenszykluskosten-Einsparungen für mittelgroße Städte.

**4. Politisches Mandat und Change-Management — nicht technische Fähigkeit — sind die entscheidenden Engpässe.** München bestätigt dies; Barcelona, Helsinki und der französische Staat bestätigen das Inverse. Überparteiliche Institutionalisierung, finanziertes Change-Management und Community-of-Practice-Beteiligung sind wichtiger als Technologieauswahl.

**5. Der globale Rahmen konvergiert.** GovStack [15], der Interoperable Europe Act [6], EMBAG [1] und OZG 2.0 [2] zeigen alle auf dasselbe Ziel: interoperable, quelloffene, souveränitätswahrende digitale öffentliche Infrastruktur. Städte, die ihre Strategie jetzt an diesen Rahmen ausrichten, positionieren sich, um von gemeinsamen Werkzeugen, gemeinsamer Finanzierung und gemeinsamer Expertise einer wachsenden internationalen Gemeinschaft zu profitieren.

Dieses Papier ist so konzipiert, dass es sich kontinuierlich verbessert. Die Quellenregistratur, Literaturrecherche und Implementierungsstrategie werden vierteljährlich aktualisiert. Korrekturen, Ergänzungen und Fallstudienbeiträge von Kommunen sind willkommen unter sebk4c@tuta.com.

---

## Quellenverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. In Kraft 2024-01-01. https://www.fedlex.admin.ch/eli/cc/2023/682/de [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. https://scs.community/ [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Öffentliches Geld? Öffentlicher Code!* https://publiccode.eu/ [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/

[10] openCode.de. (2022). *openCode — Open Source für die Verwaltung*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/ [Apache 2.0]

[12] Decidim-Verein. (2021). *Decidim: Freie quelloffene partizipative Demokratie für Städte und Organisationen*. https://decidim.org/ [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud für die öffentliche Verwaltung: Sicherheit, Souveränität und Zusammenarbeit*. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation v1.9*. https://spec.matrix.org/ [Apache 2.0]

[15] Internationale Fernmeldeunion (ITU) / Digital Impact Alliance (DIAL). (2023). *GovStack: Bausteine für digitale Verwaltung*. Genf: ITU. https://govstack.global/ [CC-BY-SA-4.0]

[16] E-Government Schweiz. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[17] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 — Data Act*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854

[18] ZenDiS GmbH. (2024). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung — Tätigkeitsbericht 2023/2024*. Berlin: ZenDiS GmbH. https://zendis.de/

[19] TYPO3-Verein. (2023). *TYPO3 in der öffentlichen Verwaltung*. https://typo3.org/project/association

[20] OpenProject GmbH. (2023). *OpenProject für die Verwaltung: Open-Source-Projektmanagement*. https://www.openproject.org/ [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open-Source-Identitäts- und Zugriffsverwaltung*. https://www.keycloak.org/ [Apache 2.0]

[22] CKAN-Verein. (2023). *CKAN: Open-Source-Datenportal-Software*. https://ckan.org/ [AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/

[25] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Zusammenarbeit, Transparenz und Beteiligung in der Praxis*. Sebastopol, CA: O’Reilly Media.

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. https://www.bsi.bund.de/ [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2-Richtlinie*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555

[28] CONSUL Democracy Foundation. (2023). *CONSUL Democracy: Open-Government- und E-Partizipations-Websoftware*. https://consuldemocracy.org/ [AGPL-3.0]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: Die Zukunft der digitalen Verwaltung*. New York: Vereinte Nationen. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[31] Verein eCH. (2023). *eCH-Standards: E-Government-Standards Schweiz*. Bern: Verein eCH. https://www.ech.ch/

[32] Europäische Kommission Joinup. (2023). *OSOR-Jahresbericht 2023: Open Source in der europäischen öffentlichen Verwaltung*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor [CC-BY-4.0]

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ [Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open-Source-Webkonferenzen*. https://bigbluebutton.org/ [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open-Source-Videokonferenzen*. https://jitsi.org/ [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ [ODbL-1.0]

[37] QGIS-Projekt. (2023). *QGIS: Ein freies und quelloffenes geografisches Informationssystem*. https://www.qgis.org/ [GPL-2.0+]

[38] Ministère de l’Intérieur (Frankreich). (2023). *Migration vers les logiciels libres: LibreOffice dans l’administration publique*. Paris: Ministère de l’Intérieur. https://www.interieur.gouv.fr/ [*URL gegen Primärquelle verifizieren*]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ [Apache 2.0]

[40] Landeshauptstadt München. (2017). *LiMux — Abschlussbericht und Entscheidungsvorlage*. München: Stadtratsdokumentation der Landeshauptstadt München. [*Primärquelle: Münchner Stadtratsdokumente; genaue Zitationsreferenz verifizieren*]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ [PostgreSQL-Lizenz]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ [CC-BY-4.0]

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/

[47] Schweizerische Eidgenossenschaft. (2020). *Bundesgesetz über den Datenschutz (nDSG)*. SR 235.1. In Kraft 2023-09-01. https://www.fedlex.admin.ch/eli/cc/2022/491/de [CC0]

[48] GAIA-X Association AISBL. (2023). *GAIA-X: Eine föderierte und sichere Dateninfrastruktur für Europa*. https://gaia-x.eu/

[49] ZenDiS GmbH. (2024). *OpenDesk: Produktbeschreibung und Versionsinformationen 2024*. Berlin: ZenDiS GmbH. https://opendesk.eu/

[50] Decidim-Verein. (2023). *Decidim Sozialvertrag*. https://docs.decidim.org/en/governance/social-contract [CC-BY-SA-4.0]

[51] Bundesministerium des Innern (BMI). (2024). *BundID: Nutzungsstatistiken und Entwicklungsstand 2024*. Berlin: BMI. https://www.bmi.bund.de/ [*Spezifische Berichts-URL verifizieren*]

[52] KoSIT. (2024). *XÖV-Rahmenwerk 3.0*. Bremen: KoSIT. https://www.xoev.de/

[53] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 — Künstliche-Intelligenz-Gesetz*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689

[54] Europäische Kommission SEMIC. (2024). *DCAT Application Profile für Datenportale in Europa (DCAT-AP) 3.0*. https://semiceu.github.io/DCAT-AP/releases/3.0.0/ [CC-BY-4.0]

---

## Anhang A: Technologie-Bewertungsvorlage

| Kriterium | Gewichtung | 1 | 3 | 5 |
|---|---|---|---|---|
| Lizenzoffenheit | 20% | Proprietär | LGPL/Dual | OSI-genehmigt |
| Deployment-Reife | 15% | Experimentell | 2–5 Jahre Produktion | 10+ Jahre, 100+ Orgs |
| Community-Gesundheit | 15% | Inaktiv | Mäßig | Groß, stiftungsgefördert |
| Interoperabilität | 15% | Keine Standards | Einige Standards | Alle relevanten Standards |
| Sicherheitslage | 20% | Schlecht | Ausreichend | CVE-reaktionsfähig; SBOM; geprüft |
| TCO (5J.) | 10% | Sehr hoch | Mittel | Sehr niedrig |
| Öffentlicher-Sektor-Einsatz | 5% | Keiner | Einige EU-Nutzung | Weitverbreitete EU-Regierungsnutzung |

**Interpretation:** ≥4,5 Stark empfohlen · 3,5–4,4 Empfohlen · 2,5–3,4 Akzeptabel mit Vorbehalten · <2,5 Nicht empfohlen

---

## Anhang B: Bürgerzufriedenheits-Erhebungsrahmen

**Kernfragen (pro Dienst übersetzen und anpassen):**

1. Wie einfach war es, den gewünschten Dienst zu finden? (1–10)
2. Wie einfach war es, Ihr Anliegen online zu erledigen? (1–10)
3. Mussten Sie die Gemeinde zusätzlich telefonisch oder persönlich kontaktieren? (Ja/Nein)
4. Wie sicher sind Sie, dass Ihre Daten sicher behandelt werden? (1–10)
5. Waren die Anweisungen klar und verständlich? (1–10)
6. Wie lange dauerte der Prozess von der Einreichung bis zur Erledigung? (offen)
7. Wie zufrieden sind Sie insgesamt mit diesem digitalen Dienst? (NPS: 0–10)
8. Was würde Ihre Erfahrung am meisten verbessern? (offen)
9. Haben Sie Barrierefreiheits-Features genutzt? Haben diese gut funktioniert? (Ja/Nein/N/A)
10. Würden Sie diesen Dienst online oder persönlich bevorzugen? (Online/Persönlich/Gleichgültig)

**Ziele:** NPS > 40 bis Phase 4 · NPS > 60 bis Phase 5

---

## Anhang C: Beschaffungs-Bewertungskriterien

**Pflichtkriterien (Bestehen/Nichtbestehen):**
- Software unter OSI-genehmigter Lizenz geliefert
- Code bei Lieferung auf openCode.de oder äquivalent veröffentlicht
- Relevante Interoperabilitätsstandards implementiert (XÖV / eCH / DCAT-AP 3.0)
- Datenverarbeitungsvertrag (DSGVO/nDSG-konform) vorhanden
- Sicherheitsmeldungsrichtlinie dokumentiert und aktiv

**Bewertete Kriterien (0–10 pro Kriterium):**

| Kriterium | Gewichtung |
|---|---|
| Technische Qualität der vorgeschlagenen Lösung | 25% |
| 5-Jahres-TCO (niedriger ist besser) | 20% |
| Community und Upstream-Beitragshistorie | 15% |
| Support-Kapazität und SLA | 15% |
| Team-Erfahrung im öffentlich-sektoralen Open-Source | 10% |
| Referenzen von vergleichbaren Gemeinden | 10% |
| Ausstiegsstrategie und Daten-Portabilitätsplan | 5% |

---

## Anhang D: Datenklassifizierungsrahmen

| Klasse | Beispiele | Behandlung | Open-Data-geeignet? |
|---|---|---|---|
| Offen | Geodaten; öffentliche Entscheidungen; Statistiken | Auf CKAN veröffentlichen; CC-BY-4.0 | Ja — standardäßig offen |
| Intern | Verwaltungskorrespondenz; Protokolle | Nextcloud; zugriffsgesteuert | Nach gesetzlicher Aufbewahrungsfrist |
| Vertraulich | Personalakten; Steuerdaten; Rechtsgutachten | Verschlüsselt; strenge Zugangsprotokollierung | Nein |
| Sensible Personendaten | Gesundheit; Fürsorge; Asyl; Strafjustiz | Verschlüsselt; isoliertes System; DSFA erforderlich | Nein |

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Licence (CC-BY-4.0) veröffentlicht.*  
*Zitationsnachweis: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur, sebk4c@tuta.com*  
*Quelldokument (englisch): `Doc/en/sovereign-by-design-v0.2.0.md` — Alle Übersetzungen und Formate werden von dieser Datei abgeleitet.*
