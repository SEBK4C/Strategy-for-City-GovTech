---
title: "Souverän von Grund auf: Eine zeitgemässe Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationskompletter Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
translation-of: "Doc/en/sovereign-by-design-v0.2.0.md"
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
  - Deutschland-Stack
  - E-Government
  - kommunale Technologie
  - NIS2
  - eCH-Standards
  - GovStack
---

# Souverän von Grund auf: Eine zeitgemässe Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autorin/Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur
**Korrespondenz:** sebk4c@tuta.com
**Version:** 0.2.0 — Zitationskompletter Entwurf
**Datum:** 2026-06-21
**Sprachen:** English (Quelldokument) · Deutsch (diese Übersetzung)
**SPDX-Lizenzkennung:** CC-BY-4.0

---

## Zusammenfassung

Kommunalverwaltungen bilden die dem Bürger nächste Ebene der demokratischen Verwaltung — und stehen dennoch vor einem akuten strukturellen Widerspruch: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, anbieterbindend und mit dem Gemeinwohlinteresse unvereinbar. Dieses Papier präsentiert eine umfassende, evidenzbasierte Strategie zur Einführung eines zeitgemässen, offenen und souveränen Technologiestapels in Kommunalverwaltungen.

Gestützt auf verifizierte Entwicklungen der Jahre 2024–2026 — darunter das Schweizer E-ID-Gesetz (Dezember 2024), den Deutschland-Stack mit verbindlichen Sovereign-Cloud-Stack-Standards (März 2026), das NIS2-Umsetzungsgesetz und das KRITIS-Dachgesetz (2025–2026) sowie den EU Interoperable Europe Act (2024) — werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie für Kommunen jeder Grösse abgeleitet.

Die Kostenanalyse stützt sich auf verifizierte Grossimplementierungen: die GendBuntu-Migration der Gendarmerie Nationale (103.164 Arbeitsplätze, 40 % TCO-Reduktion, ~2 Mio. Euro/Jahr Einsparungen), die LibreOffice-Migration des Landes Schleswig-Holstein (30.000 Arbeitsplätze, 15 Mio. Euro jährliche Einsparungen, weniger als ein Jahr Amortisationszeit) sowie die Signalen-Plattform (39 niederländische Kommunen, 7,9 Mio. Bürgerinnen und Bürger pro Jahr).

Das Papier kommt zum Schluss, dass Open-Source-Technologiestapel für Kommunen nicht nur technisch ausgereift sind, sondern gesamtkostengünstiger, demokratisch geboten und durch ein beschleunigendes Regulierungsumfeld zunehmend verpflichtend.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale digitale Transformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, Deutschland-Stack, E-Government, NIS2, eCH, GovStack

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Frage des Ob mehr — sie ist eine Frage des Wie und Wann. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienstleistungen; der Gesetzgeber verlangt Interoperabilität und Datenschutz; und der Kostendruck erfordert nachhaltige, wirtschaftliche Technologieinvestitionen. Dennoch befinden sich die meisten Kommunen nach wie vor in einem Kreislauf aus proprietärer Anbieterabhängigkeit, teuren Lizenzverträgen und fragmentierten Systemen, die gute Verwaltung behindern statt fördern [1, 29].

Die Folgen dieser Abhängigkeit sind gut dokumentiert: Vendor Lock-in erhöht die Wechselkosten und verschlechtert die Verhandlungsposition [4]; proprietäre Formate behindern behördenübergreifenden Datenaustausch und Transparenz [45]; Closed-Source-Infrastruktur verhindert unabhängige Sicherheitsaudits [26]; und wiederkehrende Lizenzgebühren binden Mittel, die anderweitig in die Daseinsvorsorge fliessen könnten [48].

Die Jahre 2024–2026 haben eine entscheidende Beschleunigung der europäischen Regulierungsreaktion gebracht. Das Schweizer E-ID-Gesetz vom Dezember 2024 [51] schafft eine staatliche digitale Identität (SWIYU) mit geplanter Integration in Kantons- und Gemeindeservices. Der EU Interoperable Europe Act (April 2024) begründet eine verbindliche Präferenz für Open-Source-Interoperabilitätslösungen in allen öffentlichen Verwaltungen [53]. Der IT-Planungsrat verpflichtete im März 2026 alle Verwaltungsebenen auf die Standards des Sovereign Cloud Stack (Deutschland-Stack) [49]. Das NIS2-Umsetzungsgesetz [60] und das KRITIS-Dachgesetz [61] — beide seit spätestens März 2026 in Kraft — begründen neue Cybersicherheitspflichten auch für Kommunen.

Gleichzeitig belegen grossmassstäbliche Implementierungen die technische und wirtschaftliche Reife des Ansatzes: OpenDesk (ZenDiS), seit September 2024 für alle deutschen Behörden verfügbar und auf 160.000 Lizenzen bis Ende 2025 ausgerichtet [58, 59]; GendBuntu der Gendarmerie Nationale (103.164 Arbeitsplätze, 40 % TCO-Reduktion) [47]; Schleswig-Holstein LibreOffice (15 Mio. Euro jährliche Einsparungen, unter einem Jahr Amortisation) [48]; und Signalen (39 niederländische Kommunen) [54].

Dieses Papier synthetisiert all diese Entwicklungen zu einer praxistauglichen, evidenzgestützten Strategie für Kommunalverwaltungen — adressiert an alle relevanten Akteure: Stadtverwaltungen, gewählte Mandatsträger, öffentliche IT-Fachkräfte, Beschaffungsstellen, Zivilgesellschaft, Open-Source-Gemeinschaften und souveräne Technologieanbieter.

### 1.1 Begriffsklärungen und Geltungsbereich

*Kommunalverwaltung* bezeichnet städtische und lokale Behörden, einschliesslich Gemeinden, Kommunen, Städte und äquivalente Strukturen in Schweizer Kantonen. Die Strategie ist für Kommunen von 5.000 bis über 500.000 Einwohner ausgelegt.

*Open-Source-Technologiestapel* bezeichnet Softwarekomponenten unter OSI-genehmigten Lizenzen, die auf Infrastruktur betrieben werden, über die die Gemeinde eigenständig verfügen kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, eigenständige und nachvollziehbare Entscheidungen über ihre digitale Infrastruktur zu treffen, einschliesslich des Rechts, Software zu prüfen, anzupassen, zu auditieren und ohne unverhältnismässige Abhängigkeit zu migrieren [3].

*Digitale Öffentliche Infrastruktur (DPI)* bezeichnet gemeinsam nutzbare, wiederverwendbare digitale Grundlagen — Identität, Zahlungsverkehr, Register, Nachrichtenwesen, Datenaustausch — die staatliche Dienste im Massstab ermöglichen [55].

### 1.2 Forschungsfragen

1. Wie sieht ein zeitgemässer Open-Source-Technologiestapel für Kommunen im Jahr 2026 aus?
2. Welche Schlüsse lassen sich aus den Erfahrungen des schweizerischen, deutschen und europäischen souveränen Technologieumfelds ziehen?
3. Welches ist der optimale Implementierungsweg für eine Stadt mit 50.000 bis 500.000 Einwohnern?
4. Wie sind Beschaffung, Stakeholder-Engagement und Risikomanagement zu gestalten?
5. Was verlangt das Regulierungsumfeld 2024–2026, und wie verändert es das Kalkül für Kommunen, die die Transformation verzögern?

---

## 2. Methodik

Das Papier verbindet folgende Forschungsansätze:

**Systematische Literaturübersicht** wissenschaftlicher Publikationen, Grauer Literatur und Politikdokumente 2010–2026 zu E-Government, digitaler Souveränität und kommunalem Open-Source-Einsatz. Die Literaturübersicht ist auf kontinuierliche Verbesserung ausgelegt (Quellenregister `Mem/source-registry.md`, Literaturstand `Mem/literature-review-state.md`).

**Vergleichende Politikanalyse** für die Schweiz (EMBAG 2023, E-ID-Gesetz 2024, E-Government-Strategie 2024–2027), Deutschland (OZG 2.0 2024, NIS2-Umsetzungsgesetz 2025, KRITIS-Dachgesetz 2026, Deutschland-Stack 2026) und die EU (Interoperable Europe Act 2024, NIS2-Richtlinie 2022).

**Technologiestapel-Bewertung** anhand einer strukturierten Bewertungsmatrix mit den Kriterien: (a) Lizenzoffenheit, (b) Deployment-Reife, (c) Community-Gesundheit, (d) Interoperabilitätsstandardkonformität, (e) Sicherheitsstatus, (f) Gesamtbetriebskosten (TCO) und (g) bestehende Behördeneinsätze.

**TCO-Evidenzsynthese** auf Basis verifizierter Daten aus GendBuntu (Frankreich), Schleswig-Holstein (Deutschland) und dem weiteren französischen Staatseinsatz.

### 2.1 Einschränkungen

Stand der Bewertungen: Juni 2026. Kostenschätzungen sind Richtwerte und müssen gegen lokale Beschaffungsbedingungen validiert werden. BundID-Statistiken beziehen sich auf August 2025. Der Deutschland-Stack wurde Anfang 2026 veröffentlicht; Ausführungsakte werden noch entwickelt.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government kennt vier Entwicklungsphasen [30]. Die aktuelle vierte Generation (ab 2020) ist durch Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und den Souveränitätsschwenk geprägt — die Erkenntnis, dass digitale Autonomie Voraussetzung demokratischer Selbstbestimmung ist [45].

Wirtz und Weyerers holistisches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Das GovStack-Rahmenwerk der ITU (v1.0, Juni 2023) ergänzt dies mit neun wiederverwendbaren Bausteinen für digitale öffentliche Infrastruktur: Identität, Zahlungsverkehr, Register, Nachrichtenwesen, Terminplanung, Einwilligungsverwaltung, digitale Signatur, Workflow und Datenerhebung [55].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Der IT-Planungsrat machte am 24. März 2026 die Standards des Sovereign Cloud Stack für alle Verwaltungsebenen verbindlich [49]. Der Deutschland-Stack schreibt zugleich ODF und PDF/UA als ausschliessliche Dokumentformate vor und schliesst proprietäre Alternativen explizit aus [49]. Die Sovereign Tech Agency (Deutschland) investierte rund 23,5 Mio. Euro in über 60 Open-Source-Infrastrukturprojekte [56]. Die Schweiz reagiert mit dem EMBAG (seit 1. Januar 2024 in Kraft), das die Open-Source-Veröffentlichung öffentlich finanzierter Software zum Regelfall erklärt [1].

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz 2.0 (2024) gibt Bürgerinnen und Bürgern ab 2029 einen Rechtsanspruch auf digitale Verwaltungsleistungen und bevorzugt ausdrücklich Open-Source-Lösungen [2, 62]. Ende 2023 waren erst 81 von 581 OZG-Leistungen online verfügbar [50]. BundID zählt im August 2025 rund 4,9 Mio. aktive Konten und rund 2 Mio. Logins pro Monat; es sind 43 digitale Verwaltungsleistungen angeschlossen [50].

**ZenDiS** (*Zentrum für Digitale Souveränität der öffentlichen Verwaltung*) — eine bundeseigene GmbH des Bundesinnenministeriums — übernahm im Januar 2024 die Verantwortung für OpenDesk [58, 59]. **OpenDesk** bündelt sechs Open-Source-Komponenten: Nextcloud, Cryptpad, OpenProject, Jitsi Meet, Element und Collabora Online. Seit Ende September 2024 steht die cloudbasierte Version allen Behörden zur Verfügung; Ziel sind 160.000 Lizenzen bis Ende 2025. Erste prominente Nutzung: Ministerpräsidentenkonferenz Leipzig, Oktober 2024 [59].

### 3.4 Schweizer Kantonal- und Bundesdigitalservices

Wichtige digitale Infrastruktur der Schweiz: **Fedlex** (Bundesrecht, offene Standards) [1]; **opendata.swiss** (nationales OGD-Portal, CKAN-basiert) [44]; **GEVER** (elektronische Geschäftsverwaltung) [43].

**Schweizer eID / SWIYU:** Das E-ID-Gesetz wurde am 20. Dezember 2024 mit 43:1 Stimmen im Ständerat verabschiedet [51]. Die offizielle elektronische Brieftasche heisst **SWIYU**. Die öffentliche Beta-Phase startete im ersten Quartal 2025; die Inbetriebnahme ist für **Anfang 2026** geplant [52]. Die Integration in Kantons- und Gemeindeservices (Adressänderungen, E-Voting, lokale Bewilligungen) folgt nach dem Bundeslaunch [52]. Die OIDC-Federation mit Keycloak ist technisch dokumentiert [51].

**eCH-Standards** bilden das schweizerische Äquivalent zu den deutschen XÖV-Standards. Relevante Normen für Gemeinden:
- **eCH-0007** (Datenstandard Gemeinden, V6.0): Austauschformat für Identifikation und Benennung von Schweizer Gemeinden [65].
- **eCH-0020** (Datenstandard Meldegründe, V4.1.0, genehmigt 16. Mai 2025): Zivilstandsregister-Datenaustausch [66].
- **eCH-0058** (Schnittstellenstandard Meldungsrahmen): technischer Nachrichtenrahmen für Systemkommunikation [66].

Die E-Government-Strategie Schweiz 2024–2027 verpflichtet alle Verwaltungsebenen auf offene Standards und Interoperabilität [16].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**OpenDesk** (ZenDiS, ab 2023) ist die Referenzarbeitsplatzlösung für die deutsche Bundesverwaltung [58, 59]. **Decidim** (Barcelona, ab 2016) ist die global führende Open-Source-Beteiligungsplattform [12]. **Matrix/Element** bildet die Grundlage für BundesMessenger (DE) und Tchap (FR) [14]. **Nextcloud** ist die am weitesten verbreitete Open-Source-Kollaborationsplattform in der europäischen öffentlichen Verwaltung [13].

**Signalen** (Amsterdam/Niederlande) ist kommunale Open-Source-Software für die Bearbeitung von Bürgerhinweisen aus dem öffentlichen Raum mit KI-gestützter Klassifikation. Sie wird von **39 niederländischen Kommunen** für **7,9 Mio. Einwohner pro Jahr** eingesetzt [54] — ein Musterbeispiel des EfA-Prinzips für kleine und mittlere Kommunen.

### 3.6 Gesamtbetriebskosten: Verifizierte Evidenzbasis

**Gendarmerie Nationale — GendBuntu (2008–heute):** Im Juni 2024 liefen 103.164 Arbeitsplätze (97 % des Fuhrparks) unter GendBuntu. Die Migration spart rund **2 Mio. Euro pro Jahr** an Softwarelizenzen und reduziert den TCO um geschätzte **40 %** gegenüber der proprietären Ausgangslage [47]. Ubuntu 24.04 LTS wurde im Dezember 2024 ausgerollt. Diese 16 Jahre dauernde, kontinuierlich dokumentierte Migration ist der weltweit robusteste TCO-Referenzfall für Linux in staatlichen Einrichtungen.

**Schleswig-Holstein — LibreOffice (2024–2026):** 30.000 Arbeitsplätze migrieren von Microsoft Office 365 zu LibreOffice. ODF ist seit dem **1. August 2024** offizielles Dokumentformat. Die Migration spart **15 Mio. Euro jährlich** (vorher rund 500 Euro/Person/Jahr für Office 365) bei einer Investition von **9 Mio. Euro** — Amortisation unter einem Jahr [48]. Dataport AöR stellt den First- und Second-Level-Support.

**Methodischer Hinweis:** Auf Basis dieser Belege liegt eine konservative Richtzahl für Open-Source-Einsparungen (nur Büro-Produktivitätssuite) bei **300–500 Euro pro Nutzerin bzw. Nutzer und Jahr** gegenüber äquivalenten proprietären Cloud-Suiten.

### 3.7 Kleine Kommunen: Fallstudien

**Signalen** (39 niederl. Kommunen) [54] und **eVaka** (finnische Kommunen, frühkindliche Betreuungsverwaltung) [63] belegen, dass der Entwicklungskosten-Sharing-Ansatz für kleine Kommunen hochgradig geeignet ist. **OpenForum Europe (2024)** kommt in einer Studie über europäische Kommunen zum Schluss: Kleine Kommunen erzielen die besten Ergebnisse, wenn sie an kooperativen Entwicklungskonsortien teilnehmen [63].

**Empfehlung für Kommunen unter 50.000 Einwohner:**
1. Anschluss an einen etablierten kooperativen IT-Dienstleister (govdigital eG, AKDB, Dataport, Schweizer Kantonsrechenzentrum).
2. Einführung von OpenDesk als Arbeitsplatzlösung (allen deutschen Behörden seit September 2024 via ZenDiS zugänglich).
3. Nutzung zertifizierter SCS-Cloud-Betreiber (plusserver, STACKIT, OSISM) für die Infrastruktur.
4. Beteiligung an gemeinsamer Applikationsentwicklung (EfA-Modell, Signalen-Modell).

### 3.8 Regulierungsrahmen 2024–2026

Kommunen mit 3–5-jährigen Beschaffungszyklen müssen die folgenden Regelungen berücksichtigen:

**Interoperable Europe Act (EU 2024/903):** In Kraft seit 11. April 2024; die meisten Bestimmungen gelten ab 12. Juli 2024; Interoperabilitätsfolgenabschätzungen sind ab dem 12. Januar 2025 verpflichtend [53]. Artikel 4 verpflichtet öffentliche Stellen zur Weitergabe von Interoperabilitätslösungen einschliesslich Quellcode. Öffentliche Stellen **sollen Open-Source-Lösungen bevorzugen**, wenn diese in Funktionalität, TCO, Nutzerfreundlichkeit und Sicherheit gleichwertig sind.

**NIS2-Umsetzungsgesetz (Deutschland, in Kraft ab 6. Dezember 2025):** Ca. 30.000 Organisationen sind betroffen; Registrierungsfrist 6. März 2026; BSI ist Aufsichtsbehörde [60]. Direkte Pflichten: Risikomanagement, Meldepflichten, Lieferkettensicherheit, Managementhaftung.

**KRITIS-Dachgesetz (in Kraft ab 17. März 2026):** Ergänzt NIS2 um physische Resilienzpflichten und adressiert Kommunen und lokale Behörden direkt [61].

**Deutschland-Stack (IT-Planungsrat, 24. März 2026):** SCS-Standards verbindlich für alle Verwaltungsebenen; ODF und PDF/UA als einzige Dokumentformate; Umsetzungsziel 2028; 7-Schichten-Architektur [49].

**EMBAG (Schweiz, seit 1. Januar 2024):** Open-Source-Veröffentlichung öffentlich finanzierter Software als Regelfall [1].

**Schweizer E-ID-Gesetz (Dezember 2024):** Gesetzliche Grundlage für die staatliche eID (SWIYU), geplanter Einsatz ab Anfang 2026 [51, 52].

---

## 4. Technologiestapel-Analyse

Der kommunale Technologiestapel lässt sich in neun Funktionsebenen gliedern, die sich auf die GovStack-Bausteine [55] und den Deutschland-Stack [49] abbilden lassen.

### 4.1 Digitale Identität und Authentifizierung

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die faktische Standardlösung für Identitäts- und Zugangsverwaltung (IAM) in der öffentlichen Verwaltung. Es implementiert OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2 und ermöglicht Federation mit nationalen Identitätssystemen: BundID in Deutschland [50] und SWIYU/eID in der Schweiz [51, 52]. Der Deutschland-Stack schreibt eine Keycloak-kompatible OIDC-IAM-Schicht verbindlich vor [49].

| Kriterium | Punkte (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Deployment-Reife | 5 | Produktionserprobt, 10+ Jahre |
| Community-Gesundheit | 5 | Gross, aktiv, CNCF |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheitsstatus | 5 | CVE-responsiv, weit auditiert |
| TCO | 4 | Keine Lizenzkosten; Betriebsexpertise nötig |
| Behördeneinsätze | 5 | EU/DE/CH-Behörden weit verbreitet |

### 4.2 Dokumentenverwaltung und Aktenführung

**Empfohlene Komponenten: Nextcloud + Collabora Online + OpenProject** [13, 20, 42]

Der Deutschland-Stack schreibt ODF als Dokumentformat vor [49]; Nextcloud/Collabora unterstützen ODF nativ und sind Bestandteile von OpenDesk [42]. Für Schweizer Gemeinden mit GEVER-Pflicht: kantonale GEVER-Lösungen (CMI Axon, Fabasoft Community) als Compliance-Schicht, Nextcloud als kollaboratives Frontend [43].

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Empfohlene Komponente: Camunda Platform Community / Flowable** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit Unterstützung für XÖV (DE) [46] und eCH (CH) [65, 66]. Flowable (Apache 2.0) ist eine lizenzrechtlich unkompliziertere Alternative.

### 4.4 Bürgerbeteiligung

**Empfohlene Komponente: Decidim** [12]

Decidim ist die weltweit meistgenutzte Open-Source-Beteiligungsplattform. Eingesetzt in Barcelona, Helsinki, Kanton Schaffhausen und New York. AGPL-3.0. Die Decidim-Assoziation betreibt eine Multistakeholder-Governance mit veröffentlichtem Sozialvertrag.

### 4.5 Kommunikation und Zusammenarbeit

**Empfohlene Komponenten (kongruent mit OpenDesk):**
- **Matrix/Element** — verschlüsselte, föderierte Kommunikation [14]; Basis des BundesMessengers
- **Jitsi Meet** — selbst hostbare Videokonferenz [35]; OpenDesk-Komponente
- **Nextcloud Talk** — in Dateiverwaltung integrierte Teamkommunikation
- **Cryptpad** — verschlüsselte Echtzeit-Kollaboration [42]; OpenDesk-Komponente

### 4.6 Open-Data-Publikation

**Empfohlene Komponente: CKAN** [22]

CKAN betreibt opendata.swiss, data.gov und data.gov.uk. Unterstützt DCAT-AP, DCAT-AP.de und OGD-Schweiz-Metadatenstandards [44].

### 4.7 Geoinformationssysteme

**Empfohlene Komponenten:** QGIS [37] + GeoServer + OpenStreetMap [36]. Basiskartendaten: swisstopo (CH), BKG (DE).

### 4.8 Öffentlicher Webauftritt und CMS

**Empfohlene Komponenten:** TYPO3 [19] (dominant im deutschsprachigen öffentlichen Sektor; BITV 2.0/WCAG 2.1 AA) oder Drupal (EU-Institutionen). Beide unterstützen Mehrsprachigkeit, Barrierefreiheit und OIDC-Authentifizierung via Keycloak.

### 4.9 Cloud-Infrastruktur und Hosting

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** — seit März 2026 **verbindlich** für deutsche Kommunen [3, 11, 49, 64]

SCS (OpenStack + Kubernetes + Ceph) kann selbst gehostet, über govdigital eG oder durch zertifizierte SCS-Anbieter betrieben werden. Das Forum SCS-Standards wurde am 1. Januar 2025 von OSBA und 14 Mitgliedsunternehmen gegründet [64].

**SCS-zertifizierte/-ausgerichtete Betreiber:** plusserver (pluscloud open) [64], STACKIT (Schwarz Gruppe), OSISM [11], govdigital eG [23].

### 4.10 Referenzarchitektur

```
+----------------------------------------------------------------------+
|                       BÜRGERSCHNITTSTELLEN                           |
|         TYPO3/Drupal  ·  Decidim  ·  CKAN  ·  Nextcloud/Portal     |
+----------------------------------------------------------------------+
|                           SERVICESCHICHT                             |
|    Camunda/Flowable-Workflows  ·  XÖV/eCH-Formulare  ·  GeoServer  |
+----------------------------------------------------------------------+
|                      KOLLABORATIONSSCHICHT                           |
|    Nextcloud + Collabora  ·  Matrix/Element  ·  Jitsi  ·  Cryptpad  |
+----------------------------------------------------------------------+
|                         IDENTITÄTSSCHICHT                            |
|         Keycloak  ←→  BundID / Schweizer eID (SWIYU)               |
+----------------------------------------------------------------------+
|                       INFRASTRUKTURSCHICHT                           |
|   Sovereign Cloud Stack (SCS)  ·  Kubernetes  ·  PostgreSQL  ·  Ceph|
+----------------------------------------------------------------------+
```

Alle Schichten kommunizieren über offene APIs. Dokumentformate: ODF und PDF/UA (Deutschland-Stack) [49]. Datenaustauschnormen: XÖV (DE) [46] bzw. eCH (CH) [65, 66]. Sicherheitsrahmen: BSI IT-Grundschutz [26] konform mit NIS2/KRITIS [60, 61].

---

## 5. Implementierungsfahrplan

Fünf Phasen über 36 Monate. Für Kommunen unter 50.000 Einwohnern empfiehlt sich die Umsetzung mit Unterstützung eines kooperativen IT-Dienstleisters; für Städte über 200.000 Einwohner ist eigenes technisches Kapazitätsaufbau ab Phase 1 erforderlich.

### Phase 0: Fundament (Monate 1–3)

- Digitaler Transformationsausschuss (Stadtführung + IT + Zivilgesellschaft + DSB)
- Technologie-Bestandsaufnahme (Softwareinventar, Lizenzkosten, Verträge mit Ausstiegsklauseln)
- Stakeholder-Engagementplan
- Beschaffungsrahmen (s. Abschnitt 6.2)
- MoU mit kooperativem IT-Dienstleister (govdigital eG, AKDB, Dataport, kant. Rechenzentrum)
- NIS2/KRITIS-Gap-Analyse (deutsche Kommunen)
- DSGVO/nDSG-Datenmapping

**Erfolgsindikator:** Politisches Mandat gesichert (Stadtratsbeschluss); Budget genehmigt (ca. 150.000–400.000 Euro für kleine Städte, 400.000–1 Mio. Euro für Grossstädte).

### Phase 1: Identität und Infrastruktur (Monate 4–12)

- SCS-Cloudumgebung betriebsbereit
- Keycloak deployed und mit BundID (DE) bzw. SWIYU/eID (CH) föderiert
- Nextcloud + Collabora (OpenDesk) für interne Kollaboration
- Matrix/Element-Messaging mit E2E-Verschlüsselung
- BSI-IT-Grundschutz-Basis dokumentiert; NIS2-Umsetzungsplan genehmigt und beim BSI registriert

**Erfolgsindikator:** 100 % der IT-Mitarbeitenden authentifizieren sich via Keycloak SSO; Dateispeicherung auf Nextcloud; interne Dokumente in ODF.

### Phase 2: Services und Workflows (Monate 10–18)

- Fünf meistgenutzte Verwaltungsdienstleistungen auf Camunda/XÖV (DE) oder Camunda/eCH (CH)
- TYPO3/Drupal-CMS-Migration abgeschlossen
- CKAN-Open-Data-Portal mit ersten 20 DCAT-AP-konformen Datensätzen
- Decidim-Instanz für ersten Beteiligungsprozess
- SBOM für alle Open-Source-Abhängigkeiten gepflegt

### Phase 3: Integration und Ausbau (Monate 16–24)

- Alle Dienste via Keycloak SSO föderiert
- Nextcloud in GEVER/DOMEA-Workflows integriert
- GIS-Schicht (QGIS + GeoServer + swisstopo/BKG)
- 80 % der Verwaltungsleistungen digitalisiert
- Erster Upstream-Beitrag auf openCode.de

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

- Bürgerzufriedenheitsumfrage (Ziel: NPS > 40)
- Mindestens drei Upstream-Verbesserungen dokumentiert
- Kommunale Open-Source-Community mit ≥ 3 Partnerkommunen aktiv
- TCO-Bericht und Leistungskennzahlen öffentlich publiziert

### Phase 5: Souveränität und Skalierung (Monate 28–36)

- Vollständiger Lizenz-Compliance-Audit
- Datensouveränität zu 100 % auf SCS-zertifizierter EU-Infrastruktur verifiziert
- Replikations-Playbook für Nachbargemeinden publiziert
- Strategiepapier v1.0 publiziert und auf openCode.de eingereicht
- Deutschland-Stack/EMBAG-Konformitätsbericht publiziert

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Hauptinteresse | Engagementansatz |
|---|---|---|
| Bürgermeister / Exekutive | Politischer Erfolg, Kosten, Bürgerzustimmung | Executive Briefing, Fortschrittsdashboard, TCO-Evidenz |
| Gemeinderat | Aufsicht, demokratische Legitimität | Quartalsberichte, offene Sitzungen, Regulierungsinformation |
| Städtisches IT-Team | Machbarkeit, Arbeitsbelastung | Co-Design, Schulung, openCode.de-Community |
| Beschaffungsstelle | Rechtskonformität, Risiko | Rahmenverträge, GWB/BöB-Guidance |
| Sachbearbeiterinnen/-bearbeiter | Bedienbarkeit, Zuverlässigkeit | UX-Tests, Change-Management, Schulung |
| Bürgerinnen/Bürger | Servicequalität, Datenschutz | Partizipativdesign via Decidim, Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Decidim, öffentliche Roadmaps, offene TCO-Daten |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft | SCS-Partnerverträge, ZenDiS-Rahmen |
| Datenschutzbeauftragte | DSGVO/nDSG-Konformität | Privacy by Design an jedem Phasentor, DSFA für Identitätsschicht |
| IT-Sicherheitsbeauftragte | NIS2/KRITIS-Konformität | BSI-IT-Grundschutz, Notfallplanung |

### 6.2 Beschaffungsrahmen

**1. Dienste beschaffen, keine Lizenzen.** Open-Source-Software ist lizenzkostenfrei; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung [4].

**2. Kooperative Beschaffungsstrukturen nutzen.** govdigital eG und kantonale IT-Kooperativen bieten vergaberechtskonforme Rahmenverträge (GWB/BöB) [23]. ZenDiS stellt OpenDesk im Bundesrahmen ohne eigenes Vergabeverfahren bereit.

**3. „Öffentliches Geld – öffentlicher Code" vertraglich verankern.** Alle vertraglich erstellten Softwareanpassungen sind unter einer OSI-genehmigten Lizenz auf openCode.de zu veröffentlichen [4, 53].

**4. 5-Jahres-TCO berechnen.** Basierend auf der Schleswig-Holstein-Evidenz [48]: proprietäre Office-Suiten kosten rund 500 Euro/Nutzerin/Jahr allein an Lizenzen; Open-Source-Alternativen eliminieren diesen Posten.

**5. Interoperabilitätsnormen als Ausschlusskriterium:** XÖV [46] und ODF [49] (DE); eCH-0007, eCH-0020, eCH-0058 [65, 66] (CH); DCAT-AP [44] (EU).

**6. SCS-zertifizierte Infrastruktur bevorzugen.** Verbindlich für deutsche Kommunen gemäss Deutschland-Stack [49]; für Schweizer Kommunen empfohlen nach äquivalenten Souveränitätsmassstäben.

### 6.3 Change-Management

Open-Source-Transitionen scheitern selten an technischen, häufiger an menschlichen Faktoren: Nutzerwiderstände, unzureichende Schulung, politischer Rückschlag unter Lobbydruck.

**Empfehlungen:**
- **Digital-Transformations-Champion** auf politischer Führungsebene mit überparteilichem Mandat
- **Open-Source-Botschafterinnen/-Botschafter** in jeder Abteilung
- **Parallelbetrieb** mindestens drei Monate vor Umstellung kritischer Systeme
- **Frühzeitige Erfolge** dokumentieren und öffentlich kommunizieren
- **Öffentliches Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Servicequalität in Echtzeit

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Massnahme |
|---|---|---|---|
| Politische Kehrtwende nach Wahl | Mittel | Hoch | In Rechtsgrundlagen verankern; überparteilicher Konsens; TCO-Evidenz publizieren |
| Anbieter-Lobbying / FUD-Kampagnen | Hoch | Mittel | GendBuntu, Schleswig-Holstein, OpenDesk-Evidenz anführen; Zivilgesellschaft einbinden |
| Kompetenzlücke IT-Team | Hoch | Mittel | Schulungsprogramm; kooperativer IT-Dienstleister; openCode.de-Community |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweise Einführung mit Entscheidungstoren; Referenzarchitektur einhalten |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollsicherung; Parallelbetrieb; stufenweise Migration |
| DSGVO/nDSG-Verstoss | Niedrig | Hoch | Privacy by Design; DSB an jedem Phasentor; Datenmapping vor Migration |
| NIS2/KRITIS-Nichtkonformität | Mittel | Hoch | Gap-Analyse in Phase 0; BSI-IT-Grundschutz-Baseline; BSI-Registrierung |
| Nutzerakzeptanzproblem | Mittel | Hoch | Change-Management; UX-Tests; Schulung; Parallelbetrieb |
| Sicherheitsvorfall in Transition | Niedrig | Kritisch | BSI-IT-Grundschutz; Penetrationstests; Incident-Response-Plan |
| Community-Fragmentierung | Niedrig | Mittel | Upstream-Beiträge; openCode.de; govdigital eG |
| Kostenüberschreitung | Mittel | Mittel | Phasengebundenes Budget; offenes TCO-Reporting |

### 7.2 Der Fall München

Münchens LiMux-Projekt (2003–2017) gilt als Warnung. Rückblickende Analysen zeigen: Der Abbruch war primär politisch bedingt — Wechsel in der Stadtführung mit engeren Microsoft-Verbindungen, unzureichendes Change-Management und Inkompatibilitätsprobleme mit landesweiten Systemen —, nicht technisch motiviert [30]. Die technische Implementierung war weitgehend erfolgreich.

Der Kontrast mit der Gendarmerie Nationale (103.164 Arbeitsplätze, 16 Jahre ununterbrochener Betrieb und Upgrades) belegt: Die entscheidende Variable ist die institutionelle Beständigkeit, nicht die Software [47]. **Überparteiliche Verankerung und Change-Management sind der bindende Erfolgsfaktor.**

### 7.3 Sicherheitsanforderungen — NIS2 und BSI IT-Grundschutz

Das NIS2-Umsetzungsgesetz (in Kraft ab 6. Dezember 2025) und das KRITIS-Dachgesetz (in Kraft ab 17. März 2026) begründen neue direkte Pflichten für Kommunen [60, 61]. Kernanforderungen:

- **Patch-Management:** Dokumentierter Prozess für alle Serverkomponenten; Open-Source ermöglicht rasche, communitybetriebene Patch-Zyklen.
- **Authentifizierungsstärke:** BSI-AAL2 für bürgerseitige Dienste; Keycloak unterstützt AAL2 und AAL3 [21].
- **Verschlüsselung:** TLS 1.3 im Transit; Verschlüsselung ruhender personenbezogener Daten.
- **Penetrationstests:** An jedem Phasentor gemäss BSI IT-Grundschutz SYS.1 [26].
- **Software Bill of Materials (SBOM):** Für alle Open-Source-Abhängigkeiten; NIS2-Lieferkettensicherheitspflicht [60].
- **BSI-Registrierung:** Deadline 6. März 2026 [60].

### 7.4 Regulatorisches Compliance-Risiko

Der regulatorische Trend ist eindeutig: Interoperable Europe Act [53], Deutschland-Stack [49], OZG 2.0 [2], EMBAG [1], NIS2 [60] und KRITIS-Dachgesetz [61] bilden zusammen ein Konformitätsumfeld, in dem **proprietäre, anbieterbindende Systeme zunehmend nicht mehr haltbar** sind. Kommunen, die die Transformation verzögern, akkumulieren regulatorischen Schuldenstand und steigende Wechselkosten. Frühzeitige Umsteller gewinnen Compliance-Kapital und gestalten den kooperativen Standard aktiv mit.

---

## 8. Schlussfolgerungen

Die überprüfte Evidenz konvergiert auf fünf Befunde:

**1. Das regulatorische Mandat ist eindeutig und verbindlich.** Interoperable Europe Act (2024), Deutschland-Stack (2026), OZG 2.0 (2024), EMBAG (2024), NIS2-Umsetzungsgesetz (2025) und KRITIS-Dachgesetz (2026) bevorteilgen systematisch souveräne, interoperable kommunale Technologie. Kommunen, die jetzt handeln, bauen Compliance-Kapital auf; wer wartet, akkumuliert regulatorischen Schuldenstand.

**2. Das wirtschaftliche Argument ist durch Grossimplementierungen belegt.** GendBuntu (103.164 Arbeitsplätze, 40 % TCO-Reduktion, 16 Jahre) und Schleswig-Holstein (30.000 Arbeitsplätze, 15 Mio. Euro Jahreseinsparungen, unter einem Jahr Amortisation) liefern definitive Evidenz für die wirtschaftliche Überlegenheit offener Lösungen.

**3. Der Technologiestapel ist produktionsreif und kooperativ zugänglich.** OpenDesk (ZenDiS) steht allen deutschen Behörden seit September 2024 zur Verfügung. Die SCS-Standards sind für deutsche Kommunen verbindlich. Keycloak, Nextcloud, CKAN, Decidim und TYPO3 verweisen auf dokumentierte Behördeneinsätze in der Schweiz, Deutschland und der EU.

**4. Das Kooperationsmodell löst das Skalierungsproblem für kleine Kommunen.** Gemeinden unter 50.000 Einwohnern müssen keinen eigenen Stapel aufbauen. Über ZenDiS, govdigital eG und das EfA-Prinzip erhalten sie Zugang zu enterprise-fähiger, souveräner digitaler Infrastruktur zu marginalen Kosten.

**5. Politisches Engagement und Change-Management sind die bindenden Erfolgsfaktoren.** Nicht die Software, sondern die institutionelle Beständigkeit über Wahlzyklen hinweg entscheidet. Überparteiliche Mandate, öffentliche Transparenz-Dashboards und eingebettete Change-Botschafter sind die entscheidenden nicht-technischen Steuerungsgrössen.

Städte, die entschlossen handeln, profitieren von Kosteneinsparungen, Regulierungskonformität und einem Beitrag zum Open-Source-Commons, von dem alle Kommunen gemeinsam profitieren. Die strategische, wirtschaftliche und demokratische Grundlage für Handeln ist so stark wie nie zuvor.

---

## Literaturverzeichnis

Alle Quellenangaben sind vollständig im kanonischen Quellenregister (`Mem/source-registry.md`) mit Verifikationsstatus dokumentiert. Die Referenznummern [1]–[66] entsprechen den Einträgen im Quellenregister und im englischsprachigen Quelldokument (`Doc/en/sovereign-by-design-v0.2.0.md`).

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0; verifiziert]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0; verifiziert]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. https://scs.community/ — [CC-BY-SA-4.0; verifiziert]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* https://publiccode.eu/ — [CC-BY-SA-4.0; verifiziert]

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [verifiziert]

[6] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2-Richtlinie*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 — [verifiziert]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). E-Government-Reifegradmodell. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024 — [verifiziert]

[8] Janssen, M. et al. (2012). Open Data Adoption Barriers. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740 — [verifiziert]

[9] FITKO. (2023). *Jahresbericht 2023*. https://www.fitko.de/ — [verifiziert]

[10] openCode.de / ZenDiS. (2024). *openCode — Open Source for Government*. https://opencode.de/ — [verifiziert]

[11] Sovereign Cloud Stack Community. (2025). *SCS Technical Documentation*. https://docs.scs.community/ — [verifiziert]

[12] Decidim Association. (2021). *Decidim: Participatory Democracy Platform*. https://decidim.org/ — [AGPL-3.0; verifiziert]

[13] Nextcloud GmbH. (2024). *Nextcloud für Behörden*. https://nextcloud.com/government/ — [AGPL-3.0; verifiziert]

[14] The Matrix Foundation. (2024). *Matrix Specification*. https://spec.matrix.org/ — [Apache 2.0; verifiziert]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [verifiziert]

[19] TYPO3 Association. (2024). *TYPO3 in Public Administration*. https://typo3.org/project/association — [GPL-2.0; verifiziert]

[20] OpenProject GmbH. (2024). *OpenProject for Government*. https://www.openproject.org/ — [GPLv3; verifiziert]

[21] Keycloak Community (CNCF). (2024). *Keycloak: Open Source IAM*. https://www.keycloak.org/ — [Apache 2.0; verifiziert]

[22] CKAN Association. (2024). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0; verifiziert]

[23] govdigital eG. (2024). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/ — [verifiziert]

[24] Dataport AöR. (2024). *IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/ — [verifiziert]

[26] BSI. (2023). *IT-Grundschutz-Kompendium Edition 2023*. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE; verifiziert]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [verifiziert]

[30] Janowski, T. (2015). Digital government evolution. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001 — [verifiziert]

[33] Camunda Services GmbH. (2024). *Camunda Platform Community Edition*. https://camunda.com/download/ — [Apache 2.0; verifiziert]

[35] Jitsi Community. (2024). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0; verifiziert]

[36] OpenStreetMap Foundation. (2024). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0; verifiziert]

[37] QGIS Project. (2024). *QGIS: A Free and Open Source GIS*. https://www.qgis.org/ — [GPL-2.0+; verifiziert]

[39] CNCF. (2024). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0; verifiziert]

[41] PostgreSQL Global Development Group. (2024). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL Licence; verifiziert]

[42] ZenDiS GmbH / BMI. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0; verifiziert]

[43] Schweizerisches Bundesarchiv (BAR). (2024). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html — [verifiziert]

[44] opendata.swiss. (2024). *Open Government Data Switzerland*. https://opendata.swiss/ — [CC-BY-4.0; verifiziert]

[45] Europäische Kommission. (2017). *European Interoperability Framework (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0; verifiziert]

[46] KoSIT. (2024). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/ — [verifiziert]

[47] OSOR / Wikipedia. (2024). *GendBuntu — Gendarmerie Nationale Ubuntu-Migration*. https://en.wikipedia.org/wiki/GendBuntu — [verifiziert: 103.164 Arbeitsplätze Juni 2024, 40 % TCO-Reduktion, ~2 Mio. Euro/Jahr Einsparungen]

[48] Document Foundation Blog / The Register. (2025). *Schleswig-Holstein LibreOffice-Migration*. https://blog.documentfoundation.org/blog/2025/03/13/updates-on-schleswig-holstein-moving-to-libreoffice/ — [verifiziert: 30.000 Arbeitsplätze, 15 Mio. Euro Jahreseinsparungen, 9 Mio. Euro Investition, <1 Jahr Amortisation]

[49] IT-Planungsrat / Heise. (2026). *Deutschland-Stack: SCS-Standards verbindlich*. https://www.heise.de/en/news/Deutschland-Stack-IT-Planning-Council-makes-open-source-cloud-standards-binding-11222752.html — [verifiziert: verbindlich ab 24. März 2026; ODF + PDF/UA Pflichtformate; alle Verwaltungsebenen]

[50] Biometric Update / Smart Country Convention. (2025). *BundID: 4,9 Mio. Konten, 2 Mio. Logins/Monat*. https://www.biometricupdate.com/202508/germanys-bundid-gets-2-million-logins-per-month — [verifiziert: August 2025]

[51] Schweizerischer Bundesrat. (2024). *E-ID-Gesetz: Bundesratsentscheid zur technischen Umsetzung*. https://www.admin.ch/gov/en/start/documentation/media-releases/media-releases-federal-council.msg-id-102922.html — [CC0; verifiziert: Gesetz vom 20. Dezember 2024]

[52] The Human Colossus Foundation / Adnovum. (2024–2025). *Schweizer E-ID: Start Anfang 2026; SWIYU-Brieftasche*. https://humancolossus.foundation/blog/n3gsylv3aor40vhkpjjdr7yzv8zllm-xyngw-p5mpg-2stzm-a3kmw — [verifiziert]

[53] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/eli/reg/2024/903/oj/eng — [verifiziert: in Kraft 11. April 2024; Open-Source-Präferenz verbindlich; Interoperabilitätsfolgenabschätzungen ab 12. Januar 2025]

[54] OSOR / Interoperable Europe Portal. (2024). *Open Source für Kommunaldienste: Fallstudie Signalen*. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/open-source-municipal-services-case-study-signalen — [verifiziert: 39 niederl. Kommunen, 7,9 Mio. Einwohner/Jahr]

[55] GovStack / ITU / GIZ. (2023). *GovStack Specification v1.0*. https://govstack.global/ — [CC-BY-4.0; verifiziert: v1.0 Juni 2023; 9 Bausteine; kommunal anwendbar]

[56] Sovereign Tech Agency. (2025). *Stärkung offener digitaler Infrastruktur*. https://www.sovereign.tech/ — [verifiziert: ~23,5 Mio. Euro in 60+ Projekten; ~17 Mio. Euro Jahresbudget]

[57] OSOR / Interoperable Europe Portal. (2024–2025). *OSOR Handbook und Berichte*. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor — [verifiziert]

[58] ZenDiS GmbH. (2024). *openDesk: About; ZenDiS — Co-creating Digital Sovereignty*. https://www.opendesk.eu/en/about — [verifiziert: ZenDiS bundeseigene GmbH; Übernahme openDesk Januar 2024]

[59] Wikipedia / AllThingsOpen. (2024–2025). *OpenDesk (Wikipedia)*. https://en.wikipedia.org/wiki/OpenDesk — [verifiziert: Ziel 160.000 Lizenzen Ende 2025; Komponenten bestätigt]

[60] Jones Day / Greenberg Traurig. (2025–2026). *NIS2-Umsetzungsgesetz Deutschland*. https://www.jonesday.com/en/insights/2025/10/germany-implements-new-kritis-umbrella-law-and-nis2-directive — [verifiziert: in Kraft 6. Dezember 2025; ~30.000 betroffene Organisationen]

[61] Jones Day / openkritis.de. (2026). *KRITIS-Dachgesetz in Kraft ab 17. März 2026*. https://www.openkritis.de/eu/eu-nis-2-germany.html — [verifiziert]

[62] OSOR / Interoperable Europe Portal. (2024). *OZG 2.0 bevorzugt Open Source*. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/germanys-ozg-20-favors-open-source-solutions — [verifiziert]

[63] OpenForum Europe. (2024). *Open Source in europäischen Kommunalverwaltungen*. https://openforumeurope.org/publications/open-source-software-adoption-and-reuse-in-european-local-governments/ — [verifiziert]

[64] OSBA / Sovereign Cloud Stack. (2025). *Forum SCS-Standards gegründet*. https://sovereigncloudstack.org/announcements/osba-forum-scs-standards/ — [verifiziert: gegründet 1. Januar 2025; 14 Mitgliedsunternehmen]

[65] eCH-Verein. (2024). *eCH-0007 Datenstandard Gemeinden V6.0*. https://www.ech.ch/de/ech/ech-0007/6.0 — [verifiziert]

[66] eCH-Verein. (2025). *eCH-0020 V4.1.0 / eCH-0058 Schnittstellenstandard*. https://ech.ch/de/node/455110 — [verifiziert: eCH-0020 V4.1.0 genehmigt 16. Mai 2025]

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Licence (CC-BY-4.0) veröffentlicht.*
*Angabe als: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*
*Version 0.2.0 — Zitationskompletter Entwurf. Alle zitierten Quellen tragen den Status „verifiziert" im Quellenregister.*
