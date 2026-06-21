---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Übersetzung: Zitierungsvollständiger Entwurf"
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
  - GovStack
  - EU-Datengesetz
  - KI-Gesetz
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitierungsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (Übersetzung) · English (Quelldokument)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Vollständige Übersetzung des englischen Originals `en/sovereign-by-design-v0.2.0.md`.*  
> *Strukturelle Änderungen werden stets zuerst im Quelldokument vorgenommen.*

---

## Änderungsprotokoll

| Version | Datum | Zusammenfassung |
|---|---|---|
| 0.1.0 | 2026-06-20 | Erster strukturierter Entwurf |
| 0.2.0 | 2026-06-21 | Fallstudien (§5); Barrierefreiheitsschicht (§4.10); KI-Werkzeuge (§4.11); EU-Datengesetz und GovStack (§3.5–3.6); verifizierte Zitate [6][9][16][43]; neue Quellen [47]–[62]; Kleingemeinden-Fahrplan (§6.2); Vergaberecht und BöB (§7.3–7.4); DSGVO und KI-Akt (§8.4–8.5); Anhang A und B |

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernächste Ebene demokratischer Administration, stehen jedoch vor einem strukturellen Dilemma: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellergebunden und nicht im Einklang mit öffentlichen Interessen. Diese Arbeit legt eine umfassende Strategie für die Implementierung eines modernen, quelloffenen Verwaltungstechnologie-Stacks in Städten und Gemeinden vor. Auf der Grundlage vorbildlicher Praxis der Schweizer Bundesverwaltung (EMBAG-Gesetzgebung), des deutschen OZG-Reformprogramms, der Sovereign-Cloud-Stack-Initiative und der breiteren europäischen Souveränitätstechnologie-Gemeinschaft werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie erarbeitet. Elf Technologieschichten werden bewertet: Identitätsmanagement, Dokumentenmanagement, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformationssysteme, Content-Management, Cloud-Infrastruktur, Barrierefreiheit und KI/Automatisierungswerkzeuge. Fallstudien aus Barcelona, dem deutschen Bundes-OpenDesk-Programm, dem Kanton Schaffhausen, Schleswig-Holstein, Moers und dem mahnenden Münchener LiMux-Fall liefern empirische Grundlagen. Die Arbeit kommt zu dem Schluss, dass Open-Source-Technologiestacks für Kommunen nicht nur technisch realisierbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Rechtsordnungen gesetzlich vorgeschrieben sind.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, OZG, EMBAG, Sovereign Cloud Stack, E-Government, GovStack, EU-Datengesetz, KI-Gesetz

---

## 1. Einleitung

Die digitale Transformation kommunaler Verwaltungen ist keine Frage des Ob, sondern des Wie. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; der Gesetzgeber fordert Interoperabilität und Datenschutz; Haushaltszwänge verlangen nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte und Gemeinden weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit gefangen: teure Lizenzverträge, fragmentierte Systeme und proprietäre Formate, die gute Verwaltungsarbeit eher behindern als ermöglichen [1, 29].

Die Folgen sind gut belegt: Herstellerbindung erhöht Wechselkosten und verschiebt Verhandlungsmacht [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch [45]; geschlossene Software verhindert unabhängige Sicherheitsprüfungen [26]; wiederkehrende Lizenzgebühren belasten Haushalte, die besser für die Daseinsvorsorge eingesetzt werden könnten [3, 5]. Am grundlegendsten: Wenn die Software demokratischer Institutionen im Besitz privater Akteure ist, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Wohl und unternehmerischen Imperativen [4, 53].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG (2023) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware grundsätzlich als Open Source veröffentlicht wird [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative stellen das ambitionierteste Open-Source-GovTech-Programm Europas dar [2, 3, 42]. Der EU-Interoperabilitätsrechtsakt 2024 schafft verbindliche Verpflichtungen zur grenzüberschreitenden Interoperabilität [6]. Die Kampagne „Public Money? Public Code!“ der FSFE, von über 200 Organisationen in 30 Ländern unterstützt, benennt das demokratische Prinzip: Öffentlich finanzierte Software gehört der Öffentlichkeit [4].

### 1.1 Geltungsbereich und Begriffserklärungen

*Kommunale Verwaltung* bezeichnet Städte und Gemeinden einschließlich Schweizer Gemeinden, deutscher Kommunen und vergleichbarer Strukturen. Die Strategie ist für Gemeinden von 5.000 bis über 500.000 Einwohnerinnen und Einwohnern ausgelegt, mit spezifischen Wegen für jede Größenordnung.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten, die unter OSI-anerkannten Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Kommune kontrolliert oder ohne unzumutbaren Aufwand wechseln kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und zu migrieren, ohne Abhängigkeit von einem einzigen Anbieter [3].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunal-Technologiestack im Jahr 2026 aus?
2. Was lässt sich aus der schweizerischen, deutschen und europäischen Souveränitätstechnologie-Gemeinschaft lernen?
3. Was ist der optimale Phasenimplementierungsweg für kommunale Verwaltungen unterschiedlicher Größe?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden?

---

## 2. Methodik

Diese Arbeit verwendet einen Mehr-Methoden-Forschungsansatz:

**Systematische Literaturrecherche** peer-begutachteter Veröffentlichungen, grauer Literatur und Grundlagendokumente aus den Jahren 2010–2026.

**Vergleichende Politikanalyse** von Technologiegesetzen und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie) und der Europäischen Union (Interoperable-Europe-Act 2024, EU-Open-Source-Strategie 2020–2023, EU-Datengesetz 2023, EU-KI-Gesetz 2024).

**Technologiestack-Bewertung** anhand einer gewichteten Scoring-Matrix: (a) Lizenzoffenheit (15%), (b) Einsatzreife (20%), (c) Community-Gesundheit (15%), (d) Interoperabilitätsstandards-Konformität (15%), (e) Sicherheitsprofil (15%), (f) Gesamtbetriebskosten (10%), (g) bestehende Verwaltungsimplementierungen (10%). Bewertungen ordinal (1–5).

**Fallstudienanalyse** von sechs Implementierungen: Barcelona, Bundes-OpenDesk, Kanton Schaffhausen, Schleswig-Holstein, Moers und München LiMux [55, 56, 60].

**Stakeholder-Analyse** zur Kartierung der Interessen und Einbindungsbedarfe jeder Stakeholder-Gruppe.

Die Literaturrecherche ist als selbstverbesserndes System konzipiert: Quellenverzeichnis (`Mem/source-registry.md`) und Literaturrecherche-Status (`Mem/literature-review-state.md`) werden versioniert und vierteljährlich aktualisiert via `Scripts/update_literature_review.py`.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in Behörden behandeln; (b) behördliche Digitaltransformationsstrategie betreffen; (c) zum europäischen, schweizerischen oder deutschen Regulierungskontext gehören; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government hat sich durch vier Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse [29]. Die zweite Generation (2005–2012) betonte Online-Dienstleistungserbringung und Bürgerportale [7]. Die dritte Generation (2012–2020) brachte Open Data, partizipative Plattformen und Mobile-First-Service-Design [8]. Die vierte Generation (2020–heute) ist durch Plattform-Regierung, digitale Identitätsinfrastruktur, Datenräume und die Souveränitätswende geprägt [45].

Das Reifegradmodell von Wirtz und Weyerer identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Die KGSt wendet ein analoges Fünf-Stufen-Modell im deutschen kommunalen Kontext an und stellt fest, dass die meisten deutschen Kommunen auf den Stufen 2–3 verbleiben [61]. Open-Source-Stacks beschleunigen den Fortschritt in Richtung Stufen 4–5, indem sie Lizenzbarrieren für Anpassung und Integration beseitigen.

Lathrop und Ruma etablierten in *Open Government* (2010) den demokratischen Wertebär für offene Daten, offene Standards und Open-Source-Software als untrennbare Säulen transparenter, partizipativer und kollaborativer Verwaltung [53]. Dieses Rahmenwerk unterstützt die FSFE-Kampagne [4] und die EU-Open-Source-Strategie [5].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept digitaler Souveränität hat sich von einem akademischen Begriff zu einem politischen Imperativ entwickelt [3, 5]. Der EU-Interoperable-Europe-Act (Verordnung (EU) 2024/903) schafft verbindliche Verpflichtungen zur grenzüberschreitenden Interoperabilität und etabliert das Interoperable Europe Board [6].

Der Sovereign Cloud Stack (SCS) der OSBA, teilfinanziert durch das BMWK, ist die konkreteste Realisierung digitaler Souveränität in europäischer Cloud-Infrastruktur: vollständig quelloffene Cloud-Plattform (OpenStack + Kubernetes + Ceph), Stand 2026 in mehreren deutschen Länder-Cloud-Umgebungen [3, 23].

Das EMBAG (SR 172.019), in Kraft seit dem 1. Januar 2024, verpflichtet zur Open-Source-Veröffentlichung aller mit öffentlichen Mitteln entwickelten Bundessoftware [1]. Damit zählt die Schweiz weltweit zu den führenden Jurisdiktionen.

### 3.3 Das Deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalverwaltungen zur Online-Dienstleistungserbringung [2]. Die OZG-2.0-Reform adressiert Schwachstellen der ersten Generation durch das „Once Only“-Prinzip, den EfA-Ansatz (Einer für Alle) und BundID/FITKO [9, 10].

ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), 2022 als Bundesbetrieb gegründet, koordiniert die Open-Source-Entwicklung für die deutsche öffentliche Verwaltung einschließlich der OpenDesk-Suite [51]. Die Plattform openCode.de (2022) bietet ein zentrales Repository für Verwaltungs-Open-Source-Software [10].

### 3.4 Schweizer Behörden und föderale Digitaldienste

Schlüsselinfrastrukturen der Schweiz:

- **Fedlex** (fedlex.admin.ch): offizielle Plattform für Bundesrecht auf Basis offener Standards [1]
- **opendata.swiss**: nationales OGD-Portal auf CKAN-Basis [44]
- **GEVER**: standardisiertes Geschäftsverwaltungssystem als Vorlage für kantonale und kommunale Implementierungen [43]
- **Schweizer eID**: dezentrales, SSI-basiertes digitales Identitätssystem nach dem Referendum 2021
- **eCH-Standards**: Schweizer E-Government-Datenaustauschstandards (eCH-0046 digitale Zustellung, eCH-0099 Identitätsfederation, eCH-0115 OGD) — äquivalent zu Deutschlands XÖV-Familie [47]

Die E-Government-Strategie Schweiz 2024–2027, gemeinsam verabschiedet vom Bundesrat und der Konferenz der Kantonsregierungen, schreibt offene Standards und Interoperabilität vor [16].

### 3.5 Das sich wandelnde digitale Regulierungsumfeld der EU

Das europäische digitale Regulierungsumfeld hat sich in 2023–2024 erheblich erweitert und betrifft die kommunale Technologiebeschaffung direkt.

**EU-Datengesetz 2023** (Verordnung (EU) 2023/2854, in Kraft ab September 2025) regelt den Zugang zu und die Nutzung von Daten aus IoT-Geräten, einschließlich Smart-City-Sensoren und kommunaler Infrastruktur [50]. Open-Source-Datenplattformen (CKAN, Gaia-X-Datenräume) sind besser auf die Datengesetz-Pflichten abgestimmt als proprietäre Systeme.

**EU-Gesetz über Künstliche Intelligenz 2024** (Verordnung (EU) 2024/1689, in Kraft ab August 2024) führt einen risikobasierten Rahmen ein, der KI-Systeme in der öffentlichen Verwaltung direkt betrifft [57]. KI-Systeme für Bürgerentscheidungen (Leistungsbewilligung, Genehmigungsbearbeitung, Risikobewertung) fallen in die Kategorie „Hohes Risiko“ mit Anforderungen an Transparenz, Genauigkeit und menschliche Aufsicht.

**EU-Interoperabilitätsrechtsakt** (Verordnung (EU) 2024/903) verlangt verbindliche Interoperabilitätsprüfungen für gemeinsam genutzte digitale Dienste über Mitgliedstaatsgrenzen hinweg [6].

### 3.6 GovStack: Ein internationaler Building-Block-Rahmen

Die GovStack-Initiative, gemeinsam von der Internationalen Fernmeldeunion (ITU) und der Digital Impact Alliance (DIAL) entwickelt, definiert wiederverwendbare, quelloffene „Building Blocks“ für digitale Verwaltungsleistungen [49]. GovStacks 14 Bausteine — darunter Identität, Zahlungen, Workflow, Messaging, Zustimmung, Registrierung und Terminplanung — bieten einen international validierten Rahmen für die kommunale Dienstearchitektur.

Deutschland ist seit 2022 beitragender GovStack-Partner; das Bausteinmodell ist mit dem OZG-EfA-Ansatz vereinbar. Für Kommunen sollte die GovStack-Konformität neben XÖV/eCH-Interoperabilität als Ausschreibungsanforderung aufgenommen werden.

### 3.7 Open-Source-Gemeinschaften und souveräne Technologieplattformen

**Decidim** (Barcelona, 2016) wird von über 400 Organisationen in 40 Ländern eingesetzt [12]. Das Governance-Modell — eine Multi-Stakeholder-Vereinigung mit veröffentlichtem Sozialvertrag — ist selbst ein Modell für Open-Source-Souveränität.

**CONSUL Democracy** (Madrid, 2015) ist eine ergänzende Partizipationsplattform mit einfacherer Deployment-Architektur für kleinere Kommunen ohne dediziertes Plattformteam [48].

**Matrix/Element** bietet ein offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll. Der BundesMessenger der deutschen Bundesregierung und Frankreichs Tchap basieren auf Matrix [14, 60].

**Nextcloud** (Stuttgart, 2016) ist die meistgenutzte quelloffene Datei-Sync- und Kollaborationsplattform in europäischen Behörden [13].

**OpenDesk**, 2023 von der deutschen Bundesregierung eingeführt und von ZenDiS verwaltet: Nextcloud + CryptPad + OpenProject + Jitsi Meet + Element [42, 51].

### 3.8 Belege zu den Gesamtbetriebskosten

Verfügbare Belege umfassen:

- **Franzosische LibreOffice-Migration** (2018–2023): 100.000 Desktops migriert; geschätzte Einsparungen €20 Mio. über fünf Jahre bei ~€5 Mio. Implementierungskosten [52]
- **Schleswig-Holstein Desktop-Schätzung** (2024): Projektion €30 Mio. Lizenzeinsparungen über 10 Jahre bei 25.000 Computern [54]
- **Barcelona Decidim** (2016–2026): Null-Lizenzkosten-Plattform für Prozesse im Wert von €75 Mio. Bürgerbudget; Betriebskosten <€500 T/Jahr [56]
- **Münchener LiMux-Kontroverse**: Ein 2013 vorgelegter Stadtbericht behauptete, die Linux-Migration habe €23 Mio. mehr gekostet; unabhängige Analyse identifizierte methodische Fehler [55]

### 3.9 Forschungslücken

1. Unabhängige, vergleichende TCO-Studien auf Systemebene fehlen
2. Kleingemeinden-Fallstudien (<50.000 Einwohner) sind unterrepräsentiert
3. Bürgerzufriedenheitsforschung zu Open-Source-Diensten fehlt fast vollständig
4. EU-KI-Gesetz-Konformität für kommunale KI-Werkzeuge ist ein aufkommendes Thema
5. eCH- und GovStack-Integrations-Fallstudien aus Schweizer Kommunen liegen noch nicht vor

Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse.

---

## 4. Technologiestack-Analyse

Ein kommunaler Technologiestack lässt sich in elf Funktionsschichten unterteilen.

### 4.1 Digitale Identität und Authentifizierung

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die De-facto-Open-Source-Lösung für Identity and Access Management (IAM) in Behörden. Es implementiert OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht Federation mit nationalen Identitätssystemen (BundID in Deutschland, Schweizer eID).

| Kriterium | Bewertung | Anmerkung |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Einsatzreife | 5 | Produktion erprobt, 10+ Jahre |
| Community | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheit | 5 | CVE-reaktiv, geprüft |
| Gesamtkosten | 4 | Keine Lizenzkosten; Betriebskompetenz nötig |
| Behörden-Einsätze | 5 | EU-Institutionen, deutsche Länder, Schweizer Kantone |
| **Gewichteter Score** | **4,85** | |

### 4.2 Dokumentenmanagement und Aktenverwaltung

**Empfohlene Komponenten: Nextcloud** + **OpenProject** [13, 20]

Für Schweizer Kommunen mit GEVER-Anforderungen liefern CMI AG Community Edition und Fabasoft Community Edition die Compliance-Schicht; Nextcloud dient als kollaboratives Frontend. Im deutschen Kontext bieten AKDB und Dataport den äquivalenten Funktionsumfang.

| Kriterium | Bewertung | Anmerkung |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Einsatzreife | 5 | 400.000+ Organisationen (Nextcloud) |
| Community | 5 | Nextcloud GmbH + Community |
| Interoperabilität | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Sicherheit | 5 | ISO-27001-zertifiziertes Angebot |
| Gesamtkosten | 5 | Keine Lizenzkosten (Community) |
| Behörden-Einsätze | 5 | Schweizer Bund, deutsche Länder, EU-Institutionen |
| **Gewichteter Score** | **4,80** | |

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Empfohlene Komponente: Camunda Platform 8 Community** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe Verwaltungsprozesse und Integration von XÖV/eCH-Datenstandards [46, 47]. **Flowable** (Apache 2.0) ist eine leichtgewichtige Alternative.

### 4.4 Bürgerbeteiligung

**Primärempfehlung: Decidim** [12] · **Alternative: CONSUL Democracy** [48]

Decidim ist die ausgereifteste und am weitesten verbreitete quelloffene Partizipationsplattform weltweit. CONSUL Democracy bietet eine einfachere Architektur für kleinere Kommunen ohne dediziertes Plattformteam.

| Kriterium | Decidim | CONSUL |
|---|---|---|
| Lizenz | 5 (AGPL-3.0) | 5 (AGPL-3.0) |
| Einsatzreife | 5 | 4 |
| Community | 5 | 4 |
| Interoperabilität | 4 | 3 |
| Sicherheit | 4 | 4 |
| Kosten | 5 | 5 |
| Behörden-Einsätze | 5 | 4 |
| **Gewichteter Score** | **4,70** | **4,10** |

### 4.5 Kommunikation und Kollaboration

**Empfohlene Komponenten:**
- **Matrix/Element** für Messaging und sichere behördenübergreifende Kommunikation [14, 60]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Teamkommunikation

Der BundesMessenger (Matrix-basiert) ermöglicht kommunalen Mitarbeitenden, direkt mit Bundesbehördenmitarbeitenden auf derselben verschlüsselten, föderierten Infrastruktur zu kommunizieren [60].

### 4.6 Open-Data-Veröffentlichung

**Empfohlene Komponente: CKAN** [22]

CKAN betreibt opendata.swiss, data.gov und data.gov.uk. Das Plugin-System ermöglicht Integration mit DCAT-AP (EU), DCAT-AP.de (Deutschland) und dem OGD-Schweiz-Metadatenstandard.

**EU-Datengesetz-Konformität:** CKANs DCAT-AP-Konformität und offene API-Architektur sind gut auf die Datenzugangs-Pflichten für IoT- und Smart-City-Daten abgestimmt [50].

### 4.7 Geographische Informationssysteme

**Empfohlene Komponenten:**
- **QGIS** für räumliche Datenbearbeitung und Server-seitige Veröffentlichung [37]
- **GeoServer** für OGC-konforme WMS/WFS/WCS
- **OpenStreetMap** als kartographische Grundlage [36]

Swisstopo (Schweiz) und BKG (Deutschland) stellen offene, hochwertige Basiskartendaten bereit.

### 4.8 Öffentliche Website und Content-Management

**Empfohlene Komponenten:**
- **TYPO3** (deutschsprachige Welt): dominierend in Schweizer und deutschen Behörden; TYPO3-Association bietet LTS und BITV-2.0-konforme öffentliche Verwaltungserweiterungen [19]
- **Drupal**: starke internationale Referenzen; Europäische Kommission, finnische Regierung

### 4.9 Cloud-Infrastruktur und Hosting

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

SCS bietet eine vollständig quelloffene Cloud-Plattform (OpenStack + Kubernetes + Ceph), die selbst betrieben, über govdigital eG oder durch zertifizierte SCS-Betreiber (plusserver, OSISM, Gonicus) bereitgestellt werden kann.

### 4.10 Barrierefreiheit und Inklusion

*Neu in Version 0.2.0*

Barrierefreiheit ist eine gesetzliche Mindestanforderung, kein optionales Feature:

- **BITV 2.0** (Deutschland): Barrierefreie-Informationstechnik-Verordnung verlangt WCAG-2.1-AA-Konformität für öffentliche Stellen; die meisten deutschen Länder haben dies auf die kommunale Ebene ausgeweitet [58]
- **EN 301 549 v3.2.1** (EU): Europäischer IKT-Barrierefreiheitsstandard, referenziert durch die EU-Web-Accessibility-Richtlinie (2016/2102); für alle öffentlichen Stellen in der EU verbindlich [58]
- **Schweizer P028**: Standard für barrierefreie Regierungswebsites auf Basis von WCAG 2.1 AA

**Empfohlene quelloffene Werkzeuge:**
- **axe-core** (MPL-2.0): automatisierte Barrierefreiheitstestmaschine; integrierbar in CI/CD-Pipelines
- **Pa11y**: Kommandozeilen-Barrierefreiheitstests für automatisiertes Reporting
- **NVDA** (Open Source): für manuelle Screenreader-Tests
- **Leichte Sprache**: vereinfachte Versionen zentraler Bürgerkommunikation

Alle Ausschreibungen für bürgergerichtete Dienste müssen umfassen: WCAG-2.1-AA-Konformitätsbericht (ACR), automatisierte Barrierefreiheitstests in der CI/CD-Pipeline und jährliche Drittanbieter-Barrierefreiheitsprüfung als Dienstleistungsbedingung.

### 4.11 KI-Werkzeuge und Automatisierung

*Neu in Version 0.2.0*

KI-Werkzeuge bieten erhebliches Produktivitätspotenzial, müssen aber unter dem EU-KI-Gesetz sorgfältig gesteuert werden [57].

**Hohes Risiko** (Konformitätsbewertung nach Art. 9 EU-KI-Gesetz erforderlich):
- KI-gestützte Leistungsbewilligungsentscheidungen
- Risikobewertung für Inspektionspriorisierung
- Automatisierte Genehmigungsbearbeitung

**Begrenztes Risiko** (Transparenzpflichten nach Art. 50):
- KI-Chatbots für Bürgerinformationsdienste
- Dokumentenzusammenfassung für internen Gebrauch
- Besprechungsprotokollierung

**Minimales Risiko** (keine spezifischen Pflichten):
- Spam-Filterung; Code-Generierungsassistenz; Übersetzungsassistenz

**Quelloffene KI-Werkzeuge für den kommunalen Einsatz:**

| Werkzeug | Anwendungsfall | Lizenz | KI-Gesetz-Risiko |
|---|---|---|---|
| **Ollama + Mistral/Llama3** | Lokales LLM für Mitarbeitendenassistenz | MIT / Meta Llama 3 | Minimal–Begrenzt |
| **Open WebUI** | Web-Oberfläche für lokales LLM | MIT | Minimal |
| **Whisper** | Besprechungstranskription | MIT | Minimal |
| **LibreTranslate** | Dokumentenübersetzung | AGPLv3 | Minimal |
| **Apache Tika** | Dokumentenklassifizierung und Metadatenextraktion | Apache 2.0 | Minimal |
| **Tesseract OCR** | Digitalisierung gescannter Dokumente | Apache 2.0 | Minimal |

**Kernprinzip:** Alle KI-Werkzeuge für bürgergerichtete Funktionen müssen menschliche Aufsicht gewährleisten, ihre KI-Natur offenlegen (EU-KI-Gesetz Art. 50) und gegen die eigenen Daten der Kommune prüfbar sein. Der lokale Betrieb quelloffener LLMs auf SCS-Infrastruktur gewährleistet Datensouveränität.

### 4.12 Referenzarchitektur

```
+--------------------------------------------------------------+
|                  BÜRGERSCHNITTSTELLEN                       |
|         TYPO3/Drupal · Decidim · CKAN · Nextcloud           |
|                 (WCAG 2.1 AA / BITV 2.0)                    |
+--------------------------------------------------------------+
|                   KI/AUTOMATISIERUNGS-SCHICHT                |
|     Ollama+LLM · Whisper · LibreTranslate · Apache Tika     |
+--------------------------------------------------------------+
|                      DIENSTE-SCHICHT                         |
|    Camunda Workflows · XÖV/eCH-Formulare · GeoServer · QGIS |
+--------------------------------------------------------------+
|                   KOLLABORATIONS-SCHICHT                     |
|    Nextcloud · Matrix/Element · Jitsi · OpenProject          |
+--------------------------------------------------------------+
|                     IDENTITÄTS-SCHICHT                       |
|          Keycloak ↔ BundID / Schweizer eID / GovStack        |
+--------------------------------------------------------------+
|                  INFRASTRUKTUR-SCHICHT                       |
|    Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph    |
+--------------------------------------------------------------+
```

---

## 5. Fallstudien

*Neuer Abschnitt in Version 0.2.0*

### 5.1 Barcelona: Decidim und die Open-Source-Digitalstadt

**Kontext:** Barcelona (Einwohnerzahl ~1,6 Mio.) führte 2016 die Decidim-Plattform unter dem Barcelonaer Digitalstadtplan 2016–2020 unter Technologiedirektorin Francesca Bria ein [56].

**Umsetzung:** Decidim wurde als Hauptplattform für den Bürgerhaushalt eingesetzt: Bürgerinnen und Bürger konnten Projekte für ~€75 Mio. Jahresbudget vorschlagen, diskutieren und abstimmen. Die Plattform wurde von Anfang an quelloffen entwickelt; 2021 wurde die Decidim Association als Commons-Governance gegründet.

**Ergebnisse:**
- 48.000+ registrierte Nutzende innerhalb von zwei Jahren
- 1.000+ Budgetvorschläge im ersten Zyklus
- Übernahme durch Katalonische Regionalregierung, Kanton Schaffhausen und 400+ Entitäten weltweit
- Betriebskosten <€500 T/Jahr [56]

**Kernlehren:** Open-Source-Veröffentlichung erzeugte globale Netzwerkeffekte. Politische Führung auf Exekutivebene war entscheidend. Start mit einem einzigen hochkarrätigen Anwendungsfall (Bürgerhaushalt) baut Schwung auf.

### 5.2 Bundes-OpenDesk: Quelloffener Arbeitsplatz in großskaliger Umsetzung

**Kontext:** Das OpenDesk-Programm der deutschen Bundesregierung, gestartet 2023 und von ZenDiS GmbH verwaltet, zielt auf eine vollständig quelloffene digitale Arbeitsumgebung für Bundesbedienstete [42, 51].

**Umsetzung:** OpenDesk integriert Nextcloud, CryptPad, OpenProject, Jitsi Meet, Element und Collabora Office zu einer einheitlich verwalteten Suite. Piloteinsatz begann 2023; breiterer Rollout für 2024–2026 geplant.

**Lehren für Kommunen:** ZenDiS’ Beschaffungsrahmen und Supportverträge können von Kommunen direkt übernommen werden und reduzieren den Vergabeaufwand erheblich. Die Komponenten-Architektur ermöglicht die Übernahme einzelner Komponenten ohne Verpflichtung zur Gesamtsuite.

### 5.3 Kanton Schaffhausen: Decidim für die kantonale Demokratie

**Kontext:** Der Kanton Schaffhausen (Einwohnerzahl ~85.000) gehörte zu den ersten Schweizer Kantonen, die Decidim für die kantonale Bürgerbeteiligung eingesetzt haben [12].

**Umsetzung:** Eingesetzt mit deutschsprachiger Anpassung und Integration in das kantonale Identitätsmanagement. Anwendungsfälle: Vernehmlassungen, räumliche Planungsbeteiligung, Online-Petitionen.

**Lehren:** Schweizer Föderalismus schafft ein natürliches Testfeld. Deutschsprachige Konfigurationen und Schweizer Anpassungen sind auf andere Kantone und deutsche Kommunen übertragbar.

### 5.4 Schleswig-Holstein: Linux-Desktop in Länder-Größenordnung

**Kontext:** Im Januar 2024 kündigte Schleswig-Holstein (Einwohnerzahl ~2,9 Mio., ~25.000 Landesbedienstete) den Übergang von Windows/Microsoft Office zu Linux und LibreOffice an; Prognose: €30 Mio. Einsparungen über 10 Jahre [54].

**Bedeutung:** Größter angekündigter Open-Source-Desktop-Übergang in der deutschen Landesverwaltung seit dem Münchener LiMux-Projekt. Im Gegensatz zu München wurden die Lehren aus der LiMux-Umkehr eingearbeitet: parteiübergreifendes politisches Mandat, Phasenrollout, dediziertes Changemanagement-Budget und Ausrichtung auf openCode.de und OZG 2.0.

**Lehren:** Politische Rahmung als Kosten- und Souveränitätsmaßnahme schuf parteiübergreifende Unterstützung. Einbettung in nationale Rahmenwerke reduziert das Umkehrrisiko.

### 5.5 Moers: Langfristiges Bekenntnis einer Kleinstadt

**Kontext:** Moers, Nordrhein-Westfalen (Einwohnerzahl ~103.000), betreibt Open-Source-Software auf kommunalen Computern seit 2001 — eine der ältesten laufenden Implementierungen in Deutschland [62].

**Kernlehren:**
- Der langfristige Kostenvorteil summiert sich: Nach dem anfänglichen Transitionsaufwand entfallen wiederkehrende Lizenz-Upgrade-Zyklen
- Kleinststädte können erfolgreich sein; Größe bestimmt nicht die Realisierbarkeit
- Über 24 Jahre erfolgreiche Integration mit Landes- und Bundessystemen widerlegt das Münchener Kompatibilitätsargument

### 5.6 München LiMux: Das mahnende Beispiel

**Kontext:** München begann 2003 mit der Migration von 15.000+ Computern auf Ubuntu Linux („LiMux“). 2017 beschloss ein neuer Stadtrat die Rückkehr zu Microsoft [30, 55].

**Vier Hauptursachen der Umkehrung:**
1. Kein parteiübergreifender politischer Schutz; neues Koalition mit engeren Microsoft-Verbindungen
2. Unzureichende Schulungsinvestitionen und dokumentierter Nutzerwiderstand
3. Einige Landessysteme setzten Windows-Umgebungen voraus; Workarounds schufen Reibungspunkte
4. Erfolgreiches Anbieter-Lobbying einschließlich Münchener Campus-Eröffnung und Förderangeboten

**Was funktionierte:** Die technische Migration selbst war 14 Jahre lang überwiegend erfolgreich. Das Scheitern war politisch und organisatorisch, nicht technisch.

**Kernlehren:** Technischer Erfolg ist notwendig, aber nicht hinreichend. Ein legislatives, parteiübergreifendes Mandat ist dauerhafter als ein Exekutivbeschluss. Anbieter-Lobbying ist vorhersehbar; Kommunikationsplanung und Zivilgesellschaftseinbindung sind die Gegenmaßnahmen.

### 5.7 Fallübergreifende Erfolgsfaktoren

| Faktor | Belege |
|---|---|
| Führende politische Förderperson | Barcelona (Bürgermeisterin), Schleswig-Holstein (Minister), Moers (Kontinuität) |
| Parteiübergreifendes Mandat | Schleswig-Holstein; fehlte in München |
| Gemeinschaftseinbindung | Barcelona Decidim, Schaffhausen Partizipationsprozesse |
| Hochkarrätiger, risikoarmer erster Schritt | Barcelona (Bürgerhaushalt); alle Fälle (E-Mail vor Desktop) |
| Phasenweiser Rollout mit Entscheidungstore | Alle erfolgreichen Fälle |
| Upstream-Beitrag | Barcelona (Decidim Association), Deutschland (openCode.de) |
| Transparenz zu Kosten und Fortschritt | Barcelona, Schleswig-Holstein |

---

## 6. Implementierungsfahrplan

### 6.1 Standardweg (50.000–500.000 Einwohnende)

#### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand erfassen, Koalition aufbauen.

**Lieferergebnisse:**
- Lenkungsausschuss Digitaltransformation eingesetzt (Stadtführung + IT + Zivilgesellschaft)
- Technologie-Ist-Analyse abgeschlossen (Anbieterliste, Lizenzkosten, Integrations-Abhängigkeiten)
- Stakeholder-Engagement-Plan verabschiedet
- Memorandum of Understanding mit kommunalem IT-Dienstleister (Dataport, AKDB, govdigital eG o. Ä.)
- Basis-Barrierefreiheitsprüfung aller bestehenden digitalen Dienste

**Budgetrahmen:** €80.000–€200.000

**Erfolgskriterien:**
- Politisches Mandat gesichert (Gemeinderatsbeschluss, öffentlich angekündigt)
- Budget genehmigt
- Dedizierte Projektleitung benannt (mindestens 80% Stellenanteil)

#### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die Grundschichten aufbauen.

**Lieferergebnisse:**
- Sovereign Cloud Stack Umgebung in Betrieb (eigen oder zertifizierter SCS-Hoster)
- Keycloak eingesetzt und mit nationalem Identitätssystem verbunden
- Nextcloud Basis-Deployment für interne Kollaboration
- Matrix/Element Messaging für Mitarbeitende
- BSI IT-Grundschutz Basisdokumentation abgeschlossen
- Barrierefreiheits-Testpipeline etabliert (axe-core, Pa11y in CI/CD)

**Budgetrahmen:** €150.000–€400.000

**Erfolgskriterien:**
- 100% der IT-Mitarbeitenden authentifizieren sich über Keycloak SSO
- Dateispeicherung auf Nextcloud migriert
- Sicherheits-Baseline durch den kommunalen Datenschutzbeauftragten genehmigt

#### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die fünf transaktionstärksten Bürgerdienste auf offener Infrastruktur migrieren.

**Lieferergebnisse:**
- Fünf meistgenutzte Verwaltungsleistungen auf Camunda/XÖV-eCH-Stack
- TYPO3/Drupal-CMS-Migration mit WCAG-2.1-AA-Prüfung
- Open-Data-Portal (CKAN) mit ersten 20 Datensätzen
- Decidim-Instanz für ersten Bürgerbeteiligungsprozess
- Lokale KI-Werkzeuge für Mitarbeitendenassistenz (Ollama + Modell)

**Budgetrahmen:** €200.000–€600.000

**Erfolgskriterien:**
- 80% des Zieldienstvolumens ohne Regression verarbeitet
- WCAG-2.1-AA-Konformität auf der öffentlichen Website erreicht
- Open-Data-Portal live und auf opendata.swiss / GovData.de indexiert

#### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten verbinden; Serviceabdeckung auf 80% der Transaktionen erweitern.

**Lieferergebnisse:**
- Alle Dienste über Keycloak SSO verbunden
- Nextcloud mit Dokumentenmanagement-Workflows integriert
- GIS-Schicht in Betrieb (QGIS + GeoServer)
- 80% der Verwaltungsleistungen digitalisiert
- Behördenübergreifender Datenaustausch über XÖV/eCH operativ

**Budgetrahmen:** €250.000–€700.000

#### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Lieferergebnisse:**
- Bürgerzufriedenheitserhebung (Ziel: NPS > 40)
- Erstbeitrag zu openCode.de oder Upstream-Projekten
- Kommunale Open-Source-Community of Practice mit ≥3 Peer-Kommunen
- KI-Gesetz-Konformitätsprüfung für alle KI-gestützten Dienste

**Budgetrahmen:** €100.000–€300.000

#### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Lieferergebnisse:**
- Vollständige Lizenzkonformitätsprüfung und Software Bill of Materials
- Datensouveränität verifiziert (100% auf souveräner Infrastruktur)
- Playbook für Nachbarkommunen auf openCode.de veröffentlicht
- Strategiepapier auf v1.0 aktualisiert

**Budgetrahmen:** €80.000–€200.000

**Gesamtprogramminvestition:** €860.000–€2.400.000 über 36 Monate. Zum Vergleich: Jahreslizenzen Microsoft 365 für eine Stadt mit 1.000 Beschäftigten bei €300 pro Nutzerin und Jahr: €900.000 jährlich.

### 6.2 Kleingemeinden-Fahrplan (5.000–50.000 Einwohnende)

**Schritt 1 (Monat 1–2):** Beitritt zu govdigital eG oder kantonaler Genossenschaft. Verwaltetes SCS-Hosting über Rahmenvertrag.

**Schritt 2 (Monat 2–6):** Verwaltetes Nextcloud für Mitarbeitende. Proprietäres File-Sharing ersetzen.

**Schritt 3 (Monat 4–9):** Öffentliche Website auf TYPO3 oder Drupal migrieren (WCAG-2.1-AA-Vorlage). CKAN mit 10 Datensätzen starten.

**Schritt 4 (Monat 8–15):** Keycloak mit BundID/Schweizer eID verbinden. Drei Bürgerdienste auf offener Plattform.

**Schritt 5 (Monat 12–24):** Decidim für einen Beteiligungsprozess pro Jahr. Regionale Open-Source-Community of Practice beitreten.

**Realistisches Budget für eine Gemeinde von 20.000 Einwohnenden:** €60.000–€120.000 für das vollständige 24-Monats-Programm; €15.000–€30.000 jährlich danach. Jährliche Lizenzeinsparungen durch Beendigung von Microsoft-365- und proprietären Dokumentenmanagementverträgen: ca. €50.000–€100.000.

Siehe Anhang A für die detaillierte Checkliste.

---

## 7. Stakeholder- und Beschaffungsstrategie

### 7.1 Stakeholder-Übersicht

| Stakeholder | Hauptinteresse | Einbindungsansatz |
|---|---|---|
| Bürgermeisterin / Exekutive | Politischer Erfolg, Kosten, Bürgerakzeptanz | Führungsbriefing, Fortschritts-Dashboard |
| Gemeinderat | Kontrolle, demokratische Legitimität | Quartalsberichte, öffentliche Ratssitzungen |
| Städtisches IT-Team | Technische Machbarkeit, Arbeitsbelastung | Co-Design, Schulung, Community-Mitgliedschaft |
| Vergabeamt | Rechtliche Konformität, Risiko | Rahmenverträge, juristische Beratung |
| Verwaltungsmitarbeitende | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Veränderungsmanagement, Schulung |
| Bürgerinnen und Bürger | Servicequalität, Datenschutz | Partizipatives Design (Decidim), Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Decidim-Plattform, öffentliche Roadmaps |
| Datenschutzbeauftragte/r | DSGVO/nDSG-Konformität | Privacy-by-Design in jeder Phase |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Einsatz | SCS-zertifizierte Partnervereinbarungen |

### 7.2 Beschaffungsrahmen

Fünf Kernprinzipien:

**1. Dienste beschaffen, nicht Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**2. Genossenschaftliche Beschaffungsstrukturen nutzen.** govdigital eG und Schweizer kantonale IT-Genossenschaften bieten Rahmenverträge, die das öffentliche Vergaberecht erfüllen [23].

**3. Das „Public Money? Public Code!“-Prinzip anwenden.** Alle unter Vertrag entwickelte Individualsoftware muss unter einer OSI-anerkannten Lizenz veröffentlicht und auf openCode.de publiziert werden — als Vertragsbedingung [4].

**4. Gesamtbetriebskosten bewerten.** 5-Jahres-TCO-Modell einschließlich Implementierung, Hosting, Schulung, Support, Integration und Ausstiegskosten.

**5. Interoperabilitätsstandards fordern.** XÖV (Deutschland) [46], eCH (Schweiz) [47], DCAT-AP (EU Open Data), OGC-Standards (GIS) und EU-KI-Gesetz-Transparenzanforderungen für KI-Komponenten [57].

### 7.3 Vergaberechtliche Besonderheiten (Deutschland)

Deutsche öffentliche Beschaffung richtet sich nach GWB (Teil 4), VgV und UVgO. Schwellenwerte für IT-Dienstleistungen (2024):

| Schwellenwert | Verfahren |
|---|---|
| < €25.000 | Direktvergabe |
| €25.000–€221.000 | Verhandlungsverfahren (UVgO) |
| > €221.000 (EU-Schwelle) | Offenes Verfahren (EU-weiter Teilnahmewettbewerb) |

**Für Rahmenverträge:** Gemeinsame Beschaffung über govdigital eG, AKDB oder Dataport unter §108 GWB (In-House-Vergabe) ermöglicht Mitgliedskommunen den Direktbezug ohne Ausschreibungspflicht.

**Für Individualentwicklung:** Über EU-Schwelle ist ein Offenes Verfahren erforderlich. Die Open-Source-Veröffentlichungspflicht („Public Money? Public Code!“) sollte als technische Spezifikation (nicht als Zuschlagskriterium) aufgenommen werden.

### 7.4 Beschaffungsrechtliche Besonderheiten Schweiz (BöB / IVöB)

Schweizerische öffentliche Beschaffung richtet sich nach BöB (SR 172.056.1) auf Bundesebene und IVöB auf kantonaler/kommunaler Ebene. WTO-GPA-Schwellenwerte (2024): CHF 270.000 (Bund) bzw. CHF 430.000 (Kantone/Gemeinden).

**Schweizer Besonderheiten:**
- „Bestbieter-Prinzip“ muss angewendet werden; reine Preisvergabe ist bei komplexen IT-Dienstleistungen unzulässig
- Open-Source-Bevorzugung kann als technisches Spezifikationskriterium (z.B. „das System muss unter einer OSI-anerkannten Lizenz lizenziert sein“) formuliert werden, ohne das GPA-Diskriminierungsverbot zu verletzen
- Das EMBAG-Prinzip [1] bietet eine starke Politikgrundlage für Open-Source-Anforderungen in der kantonalen und kommunalen Beschaffung

### 7.5 Veränderungsmanagement

Open-Source-Transitionen scheitern häufig an menschlichen Faktoren: Nutzerresistenz, unzureichende Schulung, mittlere Management-Trägheit und politischer Rückzug unter Anbieter-Lobbying (bestätigt durch München LiMux [55]).

**Kernempfehlungen:**
- **Digital-Transformations-Champion** auf politischer Ebene mit mehrjährigem öffentlichem Bekenntnis benennen
- **Open-Source-Botschafter** in jeder Abteilung mit erweiterter Schulung einsetzen
- Mindestens drei Monate **Parallelbetrieb** vor Abschaltung kritischer Systeme
- **Frühe Erfolge** dokumentieren und öffentlich kommunizieren
- Öffentliches **Transparenz-Dashboard** mit Migrationsfortschritt, Kosteneinsparungen und Servicequalitätskennzahlen

---

## 8. Risikoanalyse

### 8.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| Politischer Rückzug nach Wahl | Mittel | Hoch | In Satzung verankern; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / Desinformationskampagnen | Hoch | Mittel | TCO-Belege; Zivilgesellschaft einbinden; FSFE-Kampagne |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulungsprogramm; IT-Genossenschaft; Community of Practice |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout; Referenzarchitektur; Integrationstests |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup; Parallelbetrieb; gestufte Migration |
| DSGVO-/nDSG-Verstoß | Niedrig | Hoch | Privacy-by-Design; DSFA; DSB-Freigabe |
| EU-KI-Gesetz-Nichteinhaltung | Mittel | Mittel | Risikoklassifizierung; Konformitätsbewertung für Hochrisiko-KI |
| Benutzerakzeptanzmangel | Mittel | Hoch | Veränderungsmanagement; UX-Tests; Schulung; Rückkopplungsschleifen |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests; SBOM; Incident-Response-Plan |
| Kostenabweichung | Mittel | Mittel | Phasengesteuertes Budget; unabhängiges Projektbüro |
| Bund/Land-Systemkompatibilität | Mittel | Mittel | Abhängigkeitsprüfung in Phase 0; Kompatibilitätsschicht |

### 8.2 Das Münchener Beispiel

Siehe Abschnitt 5.6. Angewendete Gegenmaßnahmen: parteiübergreifendes Mandat vor Commitment; Changemanagement-Budget gleichwertig mit technischem Budget; Kompatibilitätsprüfung in Phase 0; Zivilgesellschaftseinbindung als politischer Anker.

### 8.3 Sicherheitsanforderungen

Der BSI IT-Grundschutz liefert eine umfassende Sicherheits-Baseline [26]. Kernanforderungen:

- Regelmäßige Sicherheitsupdates mit dokumentiertem Patch-Management (maximale Reaktionszeit 72 Stunden für kritische Schwachstellen)
- Authentifizierung auf BSI AAL2 für bürgergerichtete Dienste
- Daten in Transit: TLS 1.3 Minimum; HSTS; automatisiertes Zertifikatsmanagement
- Ruhende Daten: verschlüsselt für alle personenbezogenen Datenkategorien
- Penetrationstests an jedem Phasentor durch BSI-qualifizierte Prufende
- Software Bill of Materials (SBOM) mit automatisierten CVE-Scans
- NIS2-konformer Incident-Response-Plan mit 72-Stunden-Meldepflicht [27]
- Jährliche externe Sicherheitsprüfung gemäß ISO 27001

### 8.4 Datenschutz und Privatsphäre

- **Datenschutz-Folgenabschätzungen (DSFA/DPIA)** sind für alle neuen bürgergerichteten Dienste und KI-Werkzeuge, die personenbezogene Daten verarbeiten, erforderlich (DSGVO Art. 35; Schweizer nDSG). Der Datenschutzbeauftragte muss vor dem Produktiveinsatz zustimmen.
- **Datenspeicherort:** Alle personenbezogenen Daten müssen auf SCS/souveräner Infrastruktur innerhalb des EU/EWR-Territoriums gespeichert werden (Schweiz gilt als adäquat unter der DSGVO).
- **Drittanbieter-Verarbeiter:** Alle Cloud-Anbieter müssen einen Auftragsverarbeitungsvertrag (AVV) gemäß DSGVO Art. 28 abschließen. SCS-zertifizierte Hoster bieten standardisierte AVVs.
- **Aufbewahrungsfristen:** Dokumentenmanagementsysteme müssen gesetzliche Aufbewahrungsfristen automatisch durchsetzen.
- **Recht auf Löschung:** Systeme müssen Löschanträge nach DSGVO Art. 17 innerhalb von 30 Tagen unterstützen.

### 8.5 EU-KI-Gesetz-Konformität

Für Kommunen, die KI-Werkzeuge einsetzen (Abschnitt 4.11):

1. **Risikoklassifizierung** jedes KI-Werkzeugs vor dem Einsatz (Art. 9)
2. **Hochrisiko-System-Registrierung** in der EU-Datenbank (Art. 71) vor dem Einsatz
3. **Technische Dokumentation** gemäß Anhang IV für Hochrisiko-Systeme
4. **Menschliche Aufsichtsmechanismen** (Art. 14): Eine Person muss jede KI-gestützte Bürgerentscheidung übersteuern können
5. **Transparenz gegenüber Bürgerinnen und Bürgern** (Art. 50): KI-Chatbots müssen ihre KI-Natur offenlegen
6. **Vorfallsmeldung** schwerwiegender KI-Vorkommnisse an die nationale Aufsichtsbehörde

Quelloffene KI-Systeme sind grundsätzlich leichter konform zu gestalten als proprietäre Blackbox-Systeme, da technische Dokumentation und Modellprüfung von Natur aus möglich sind.

---

## 9. Schlussfolgerung

Die in dieser Arbeit ausgewerteten Belege — akademische Literatur, Politikanalyse, Technologiebewertung und sechs Fallstudien — konvergieren auf vier Befunde:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift, produktionserprobt und vollständig leistungsfähig.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Einsätzen erfüllt werden — von Kleinststädten (Moers, 24 Jahre) bis zu Großsstädten (Barcelona) und Bundesverwaltungen (Deutschland, Schweiz).

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor — verbindlich.** EMBAG (Schweiz), OZG 2.0 (Deutschland), der Interoperabilitätsrechtsakt, das EU-Datengesetz und das EU-KI-Gesetz schaffen gemeinsam ein rechtliches Umfeld, das proprietäre, herstellergebundene Systeme langfristig nicht erfüllen können.

**3. Die wirtschaftliche Begründung ist überzeugend, wenn die Gesamtkosten korrekt berechnet werden.** Schleswig-Holstein prognostiziert €30 Mio. Einsparungen über 10 Jahre. Barcelona betreibt eine Beteiligungsplattform für 48.000 Bürgerinnen und Bürger für unter €500 T/Jahr.

**4. Erfolg erfordert gleich viel politische und organisatorische Investition wie technische.** Das bindende Constraint ist nicht Codequalität — es ist die Fähigkeit, politischen Willen durch Wahlen, Haushaltszyklen und Anbieter-Druckkampagnen aufrechtzuerhalten.

Städte, die als Erste handeln, profitieren von Pioniervorteilen: Sie gestalten genossenschaftliche Standards, bauen Fachkompetenz auf und tragen zu den Open-Source-Gemeingutênteilen bei, die alle Kommunen teilen. Die rechtlichen Mandate, die fiskalische Argumentation, das demokratische Argument und die Fallstudienbelege zeigen alle in dieselbe Richtung. Die Einladung ist offen.

---

## Anhang A: Checkliste für Kleingemeinden

Für Gemeinden mit weniger als 50.000 Einwohnenden und begrenzten internen IT-Kapazitäten.

**Voraussetzungen:**
- [ ] Politisches Mandat von Bürgermeisterin und Gemeinderat (protokollierter Beschluss)
- [ ] Dedizierte Projektkoordination benannt
- [ ] Mitgliedschaft in govdigital eG oder kantonaler IT-Genossenschaft bestätigt
- [ ] Aktuelle IT-Kosten dokumentiert (alle Softwarelizenzen, Hosting, Supportverträge)

**Monate 1–3: Grundlegung**
- [ ] Verwaltetes SCS-Hosting über genossenschaftlichen Rahmenvertrag
- [ ] Alle Softwarelizenz-Ablaufdaten dokumentiert
- [ ] Basis-Barrierefreiheitsprüfung der öffentlichen Website
- [ ] Auftragsverarbeitungsverträge mit neuen Anbietern unterzeichnet

**Monate 2–6: Kollaboration**
- [ ] Verwaltetes Nextcloud für Mitarbeitende deployed
- [ ] Matrix/Element Messaging für Mitarbeitende (oder Nextcloud Talk)
- [ ] Alle Mitarbeitenden auf neuen Werkzeugen geschult (2 Halbtage pro Person)
- [ ] Abteilungsweise Open-Source-Botschafterinnen benannt

**Monate 4–9: Web und Open Data**
- [ ] Öffentliche Website auf TYPO3 oder Drupal (WCAG-2.1-AA-Vorlage) migriert
- [ ] Erste 10 Datensätze auf Open-Data-Portal veröffentlicht
- [ ] Anbindung an kantonalen / nationalen Open-Data-Katalog (opendata.swiss / GovData.de)

**Monate 8–18: Dienste und Identität**
- [ ] Keycloak mit BundID / Schweizer eID verbunden
- [ ] Drei meistgenutzte Bürgerdienste auf offene Plattform migriert
- [ ] Erster Decidim-Beteiligungsprozess gestartet

**Monate 18–24: Abschluss**
- [ ] Bürgerzufriedenheitserhebung durchgeführt
- [ ] TCO-Vergleich veröffentlicht (Schätzung vs. Ist)
- [ ] Regionale Open-Source-Community of Practice beigetreten
- [ ] Einen Datensatz oder eine Konfiguration auf openCode.de veröffentlicht

**Laufend:**
- [ ] Vierteljährliche Überprüfung des Quellenregisters (`Scripts/update_literature_review.py`)
- [ ] Jährliche Barrierefreiheitsprüfung
- [ ] Jährliche Sicherheitsupdate-Überprüfung (BSI IT-Grundschutz)

---

## Anhang B: Vergabetextbausteine

**B.1 Pflicht zur Open-Source-Veröffentlichung**

> *„Alle im Rahmen dieses Vertrags entwickelte oder wesentlich veränderte Software sowie alle Konfigurationsvorlagen, Automatisierungsskripte und Datenschemata, die für die Auftraggebende erstellt werden, sind unter einer OSI-anerkannten Open-Source-Lizenz (https://opensource.org/licenses) spätestens 30 Tage nach dem ersten Produktiveinsatz zu veröffentlichen. Der Auftragnehmer veröffentlicht diese Materialien auf openCode.de oder einem gleichwertigen nationalen öffentlichen Repository. Der Quellcode ist mit einer README-Datei, einer Lizenzdatei und ausreichender Dokumentation zu veröffentlichen, damit eine fachkundige Drittpartei die Software unabhängig aufbauen, testen und betreiben kann.“*

**B.2 Datenportabilität und Ausstiegsrechte**

> *„Bei Beendigung oder Ablauf dieses Vertrags übermittelt der Auftragnehmer alle Daten in offenen, maschinenlesbaren Formaten (CSV, JSON, XML, SQL-Dump je nach Eignung) innerhalb von 30 Kalendertagen nach schriftlicher Anforderung, kostenfrei. Es dürfen keine technischen oder vertraglichen Maßnahmen ergriffen werden, die die Auftraggebende daran hindern, zu alternativen Diensten zu wechseln. Der Auftragnehmer stellt dokumentierte Migrationsverfahren und angemessene Migrationshilfe bereit.“*

**B.3 Interoperabilitätsanforderungen**

> *„Alle im Rahmen dieses Vertrags gelieferten Systeme müssen folgende offene Standards implementieren: XÖV-Standards für den relevanten Leistungsbereich (Deutschland) / eCH-Standards für den relevanten Leistungsbereich (Schweiz); DCAT-AP [aktuelle Version] für Datenkatalogfunktionalitäten; OpenID Connect 1.0 und OAuth 2.0 für Authentifizierung und Autorisierung; OGC WMS/WFS für Geodatendienste; REST- oder GraphQL-APIs mit vollständiger OpenAPI-Dokumentation für alle maschinenlesbaren Schnittstellen.“*

**B.4 KI-Transparenz und menschliche Aufsicht**

> *„Alle KI-Komponenten, die in den gelieferten Systemen enthalten sind oder hinzugefügt werden, müssen: (a) der Auftraggebenden vor dem Einsatz schriftlich mitgeteilt werden; (b) gemäß dem EU-KI-Gesetz (Verordnung (EU) 2024/1689) klassifiziert werden, mit dokumentierter Klassifizierungsentscheidung; (c) bei Hochrisiko-KI-Systemen alle Anforderungen von Titel III, Kapitel 3 erfüllen; (d) bei KI-Systemen, die Text oder Bilder für Endnutzende generieren, einen klaren Hinweis auf den KI-generierten Inhalt anzeigen (Art. 50 EU-KI-Gesetz).“*

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de [CC0; verifiziert 2026-06-21]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html [DL-DE/Zero 2.0; verifiziert 2026-06-21]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. https://scs.community/ [CC-BY-SA-4.0; verifiziert 2026-06-21]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* https://publiccode.eu/ [CC-BY-SA-4.0; verifiziert 2026-06-21]

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en [Offen; verifiziert 2026-06-21]

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable-Europe-Act*. CELEX 32024R0903. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R0903 [EU-Gesetzgebung; verifiziert 2026-06-21]

[7] Wirtz, B.W., & Weyerer, J.C. (2017). *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M. et al. (2012). *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. https://www.fitko.de/ueber-fitko/jahresbericht/ [DL-DE/Zero 2.0; verifiziert 2026-06-21]

[10] openCode.de. (2022). *openCode — Open Source für die Verwaltung*. https://opencode.de/ [Offen; verifiziert 2026-06-21]

[12] Decidim Association. (2021). *Decidim: Freie quelloffene Partizipationsdemokratie*. https://decidim.org/ [AGPL-3.0; verifiziert 2026-06-21]

[13] Nextcloud GmbH. (2023). *Nextcloud für Behörden*. https://nextcloud.com/government/ [Offen; verifiziert 2026-06-21]

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation v1.x*. https://spec.matrix.org/ [Apache 2.0; verifiziert 2026-06-21]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ [Offen; verifiziert 2026-06-21]

[19] TYPO3 Association. (2023). *TYPO3 in der öffentlichen Verwaltung*. https://typo3.org/project/association [Offen; verifiziert 2026-06-21]

[20] OpenProject GmbH. (2023). *OpenProject für Behörden*. https://www.openproject.org/ [GPLv3; verifiziert 2026-06-21]

[21] Red Hat / Keycloak Community. (2023). *Keycloak IAM*. https://www.keycloak.org/ [Apache 2.0; verifiziert 2026-06-21]

[22] CKAN Association. (2023). *CKAN: Open-Source-Datenportal-Software*. https://ckan.org/ [AGPL-3.0; verifiziert 2026-06-21]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/ [Offen; verifiziert 2026-06-21]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/ [Offen; verifiziert 2026-06-21]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html [CC-BY-ND 3.0 DE; verifiziert 2026-06-21]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2*. CELEX 32022L2555. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555 [EU-Gesetzgebung; verifiziert 2026-06-21]

[29] Vereinte Nationen (UNDESA). (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 [Offen; verifiziert 2026-06-21]

[30] Janowski, T. (2015). *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ [Apache 2.0; verifiziert 2026-06-21]

[34] BigBlueButton Inc. (2023). *BigBlueButton*. https://bigbluebutton.org/ [LGPL-3.0; verifiziert 2026-06-21]

[35] Jitsi Community. (2023). *Jitsi Meet*. https://jitsi.org/ [Apache 2.0; verifiziert 2026-06-21]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ [ODbL-1.0; verifiziert 2026-06-21]

[37] QGIS Project. (2023). *QGIS*. https://www.qgis.org/ [GPL-2.0+; verifiziert 2026-06-21]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ [Apache 2.0; verifiziert 2026-06-21]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ [PostgreSQL Lizenz; verifiziert 2026-06-21]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ [AGPL-3.0; verifiziert 2026-06-21]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html [Offen; verifiziert 2026-06-21]

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. https://opendata.swiss/ [CC-BY-4.0 Portal; verifiziert 2026-06-21]

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail [CC-BY-4.0; verifiziert 2026-06-21]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/ [Offen; verifiziert 2026-06-21]

[47] eCH Verein. (2023). *eCH-Standards für E-Government in der Schweiz*. https://www.ech.ch/ [Offen; verifiziert 2026-06-21]

[48] CONSUL Democracy Foundation. (2023). *CONSUL Democracy*. https://consuldemocracy.org/ [AGPL-3.0; verifiziert 2026-06-21]

[49] ITU / DIAL. (2023). *GovStack-Initiative: Building Blocks für digitale Verwaltungsleistungen*. https://www.govstack.global/ [Offen; verifiziert 2026-06-21]

[50] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 — EU-Datengesetz*. CELEX 32023R2854. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854 [EU-Gesetzgebung; verifiziert 2026-06-21]

[51] ZenDiS GmbH. (2023). *Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. https://zendis.de/ [Offen; verifiziert 2026-06-21]

[52] EU Open Source Observatory (OSOR) / Joinup. (2023). *Open Source im europäischen öffentlichen Sektor — Jahresbericht 2023*. https://joinup.ec.europa.eu/collection/open-source-observatory-osor [CC-BY-4.0; verifiziert 2026-06-21]

[53] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O’Reilly Media. ISBN 978-0-596-80435-0.

[54] Staatskanzlei Schleswig-Holstein. (2024). *Digitale Souveränität: Schleswig-Holstein setzt auf Open Source*. https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/StK/Schwerpunkte/OpenSource/openSource_node.html [Offen; verifiziert 2026-06-21]

[55] Koch, F. (2018). LiMux — ein Rück- und Ausblick. *Linux-Magazin*. https://www.linux-magazin.de/ausgaben/2018/01/limuex/ Siehe auch: Landeshauptstadt München. (2017). Stadtratsbeschluss S-02806-KVR-07573. [Öffentliches Protokoll]

[56] Ajuntament de Barcelona. (2020). *Barcelona Digital City Plan 2016–2020: Ergebnisse und nächste Schritte*. https://ajuntament.barcelona.cat/digital/en/digital-innovation/city-os-and-urban-data/digital-city-plan-2016-2020 [CC-BY-4.0; verifiziert 2026-06-21]

[57] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 — KI-Gesetz*. CELEX 32024R1689. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689 [EU-Gesetzgebung; verifiziert 2026-06-21]

[58] ETSI. (2021). *EN 301 549 v3.2.1: Barrierefreiheitsanforderungen für IKT-Produkte und -Dienstleistungen*. https://www.etsi.org/deliver/etsi_en/301500_302000/301549/03.02.01_60/en_301549v030201p.pdf [Offen]. Siehe auch: Bundesministerium des Innern. (2011, geändert 2019). *Barrierefreie-Informationstechnik-Verordnung (BITV 2.0)*. https://www.gesetze-im-internet.de/bitv_2_0/ [CC0; verifiziert 2026-06-21]

[59] Gaia-X AISBL. (2024). *Gaia-X Jahresbericht 2024*. https://gaia-x.eu/ [Offen; verifiziert 2026-06-21]

[60] Bundesministerium des Innern und für Heimat (BMI). (2023). *BundesMessenger: Sichere Kommunikation für die Bundesverwaltung*. https://messenger.bund.de/ [Offen; verifiziert 2026-06-21]

[61] KGSt. (2022). *Digitale Transformation in Kommunen: Reifegradmodell und Handlungsempfehlungen*. Köln: KGSt. https://www.kgst.de/ [KGSt-Mitgliedspublikation]

[62] Stadtverwaltung Moers. (2023). *Open Source in der Stadtverwaltung Moers*. https://www.moers.de/de/rathaus/open-source/ [Offen; verifiziert 2026-06-21]

---

*Veröffentlicht unter CC-BY-4.0. Namensnennung: Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur (sebk4c@tuta.com)*  
*Version 0.2.0 — Zitierungsvollständiger Entwurf — 2026-06-21*  
*Quelldokument: Englisch · Diese Übersetzung: Deutsch*  
*Repository: https://github.com/SEBK4C/Strategy-for-City-GovTech*
