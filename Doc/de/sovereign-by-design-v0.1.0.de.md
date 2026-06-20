---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.1.0"
status: "Übersetzung: Erster Strukturierter Entwurf"
date: "2026-06-20"
language: "de"
translated-from: "en/sovereign-by-design-v0.1.0.md"
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
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur
**Korrespondenz:** sebk4c@tuta.com
**Version:** 0.1.0 — Übersetzung: Erster Strukturierter Entwurf
**Datum:** 2026-06-20
**Sprachen:** Deutsch (Übersetzung) · English (Quelle)
**SPDX-License-Identifier:** CC-BY-4.0

> *Dieses Dokument ist eine vollständige Übersetzung des englischen Originals*
> *`en/sovereign-by-design-v0.1.0.md` (Quelldokument der Wahrheit).*
> *Strukturelle Änderungen werden zuerst im Quelldokument vorgenommen.*

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernächste Ebene demokratischer Administration, stehen jedoch vor einem strukturellen Dilemma: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellergebunden und nicht im Einklang mit öffentlichen Interessen. Diese Arbeit legt eine umfassende Strategie für die Implementierung eines modernen, quelloffenen Verwaltungstechnologie-Stacks in Städten und Gemeinden vor. Auf der Grundlage vorbildlicher Praxis der Schweizer Bundesverwaltung (EMBAG-Gesetzgebung), des deutschen OZG-Reformprogramms und der Sovereign-Cloud-Stack-Initiative sowie der breiteren europäischen Souveränitätstechnologie-Gemeinschaft werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie von ersten Grundsätzen her erarbeitet.

Die Analyse umfasst die zentralen Technologiekomponenten — Identitätsmanagement, Dokumentenmanagement, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung und Cloud-Infrastruktur — bewertet nach den Kriterien digitale Souveränität, Interoperabilität, Gesamtbetriebskosten und demokratische Eignung. Die Arbeit kommt zu dem Schluss, dass Open-Source-Technologiestacks für Kommunen nicht nur technisch realisierbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Jurisdiktionen gesetzlich vorgeschrieben sind. Der Fahrplan umfasst 36 Monate mit konkreter Beschaffungsanleitung für Stadtverantwortliche, gewählte Mandatsträger, IT-Teams, Zivilgesellschaft und Technologieanbieter.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Civic Technology

---

## 1. Einleitung

Die digitale Transformation kommunaler Verwaltungen ist keine Frage des Ob, sondern des Wie. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; der Gesetzgeber fordert Interoperabilität und Datenschutz; Haushaltszwänge verlangen nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte und Gemeinden weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit gefangen: teure Lizenzverträge, fragmentierte Systeme und proprietäre Formate, die gute Verwaltungsarbeit eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut belegt: Herstellerbindung erhöht Wechselkosten und verschiebt Verhandlungsmacht zugunsten privater Anbieter [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Software verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Haushalte, die besser für die Daseinsvorsorge eingesetzt werden könnten [3, 5]. Am grundlegendsten: Wenn die Software demokratischer Institutionen im Besitz privater Akteure und durch diese kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Wohl und unternehmerischen Imperativen [4].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben, 2023) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware grundsätzlich als Open Source veröffentlicht wird [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative stellen das ambitionierteste Open-Source-GovTech-Programm Europas dar [2, 3, 42]. Die Kampagne „Public Money? Public Code!“ der Free Software Foundation Europe, mittlerweile von über 200 Organisationen in 30 Ländern unterstützt, benennt das demokratische Prinzip: Software, die mit öffentlichen Mitteln bezahlt wurde, soll der Öffentlichkeit zur Verfügung stehen [4].

### 1.1 Begriffserklärungen und Abgrenzungen

*Kommunale Verwaltung* bezeichnet Städte und Gemeinden einschließlich Schweizer Gemeinden, deutscher Kommunen und vergleichbarer Strukturen. Die Strategie ist für Gemeinden von 5.000 bis über 500.000 Einwohnerinnen und Einwohnern ausgelegt.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten, die unter OSI-anerkannten Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Kommune kontrolliert oder ohne unzumutbaren Aufwand wechseln kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und zu migrieren, ohne Abhängigkeit von einem einzigen Anbieter [3].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunal-Technologiestack im Jahr 2026 aus?
2. Was lässt sich aus der schweizerischen, deutschen und europäischen Souveränitätstechnologie-Gemeinschaft lernen?
3. Was ist der optimale Phasenimplementierungsweg für eine Stadt mit 50.000–500.000 Einwohnerinnen und Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden, um die Erfolgschancen zu maximieren?

---

## 2. Methodik

Diese Arbeit verwendet einen Mehr-Methoden-Forschungsansatz:

**Systematische Literaturrecherche** peer-begutachteter Veröffentlichungen, grauer Literatur und Grundlagendokumente aus den Jahren 2010–2026 zu E-Government-Theorie, digitaler Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunaler Digitaltransformation.

**Vergleichende Politikanalyse** von Technologiegesetzen und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie) und der Europäischen Union (Interoperable-Europe-Act 2024, EU-Open-Source-Strategie 2020–2023).

**Technologiestack-Bewertung** anhand einer Scoring-Matrix: (a) Lizenzoffenheit, (b) Einsatzreife, (c) Community-Gesundheit, (d) Interoperabilitätsstandards-Konformität, (e) Sicherheitsprofil, (f) Gesamtbetriebskosten, (g) bestehende Verwaltungsimplementierungen.

**Stakeholder-Analyse** zur Kartierung der Interessen, des Einflusses und der Einbindungsbedarfe jeder Stakeholder-Gruppe.

Die Literaturrecherche ist als selbstverbesserndes System konzipiert: Quellenverzeichnis (`Mem/source-registry.md`) und Literaturrecherche-Status (`Mem/literature-review-state.md`) werden versioniert und regelmäßig aktualisiert. Das Skript `Scripts/update_literature_review.py` liefert strukturierte Aufforderungen für die vierteljährliche Aktualisierung.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in Behörden behandeln; (b) behördliche Digitaltransformationsstrategie betreffen; (c) zum europäischen, schweizerischen oder deutschen Regulierungskontext gehören; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern.

### 2.2 Einschränkungen

Dieses Dokument ist ein erster strukturierter Entwurf (v0.1.0). Einige Zitate bedürfen der Verifizierung gegen Primärquellen (im Quellenverzeichnis vermerkt). Technologiestack-Bewertungen spiegeln den Stand öffentlich verfügbarer Informationen per Juni 2026 wider. Implementierungskostenschätzungen sind indikativ.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government hat sich durch vier Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Schaffung von Regierungswebsites [29]. Die zweite Generation (2005–2012) betonte die Online-Dienstleistungserbringung, Bürgerportale und Back-Office-Integration [7]. Die dritte Generation (2012–2020) brachte Open Data, partizipative Plattformen und Mobile-First-Service-Design [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattform-Regierung, digitale Identitätsinfrastruktur, Datenräume und die Souveränitätswende geprägt — die Erkenntnis, dass digitale Autonomie eine Voraussetzung demokratischer Selbstregierung ist [45].

Das Reifegradmodell von Wirtz und Weyerer identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Kommunen in Deutschland und der Schweiz zeigen heterogene Leistungen über diese Dimensionen; technische Infrastruktur und Prozessqualität hinken den Bürgererwartungen in den meisten Jurisdiktionen nach, während das regulatorische Umfeld zunehmend Transparenz und Interoperabilität vorschreibt [1, 2, 45].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept digitaler Souveränität hat sich von einem akademischen Begriff zu einem politischen Imperativ im europäischen Kontext entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte „Teilung und Wiederverwendung“ als Kernprinzip [5]. Der Interoperable-Europe-Act 2024 schafft bindende Verpflichtungen zur grenzüberschreitenden Interoperabilität [6].

Der Sovereign Cloud Stack (SCS) der Open Source Business Alliance (OSBA), teilfinanziert durch das BMWK, stellt die konkreteste Realisierung digitaler Souveränität in der Cloud-Infrastruktur dar [3]. Stand 2026 bildet SCS die Grundlage für mehrere deutsche Länder-Cloud-Umgebungen und ist in govdigital eGs gemeinsame Infrastruktur integriert [23].

Das EMBAG, in Kraft seit dem 1. Januar 2024, verlangt, dass alle mit öffentlichen Mitteln entwickelte Bundessoftware als Open Source veröffentlicht wird, sofern keine zwingenden Sicherheitsgründe dagegen sprechen [1]. Damit gehört die Schweiz zu den führenden Jurisdiktionen weltweit.

### 3.3 Das Deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalverwaltungen, ihre Verwaltungsleistungen online anzubieten [2]. Die OZG-2.0-Reform adressiert Schwächen der ersten Generation durch das „Once Only“-Prinzip, den EfA-Ansatz (Einer für Alle) und eine Bundesplattform-Architektur um BundID und FITKO [9, 10].

Die Plattform openCode.de (2022) bietet ein zentrales Repository für behördliche Open-Source-Software [10]. Dataport AöR und AKDB repräsentieren das genossenschaftliche Modell kommunaler IT-Erbringung [24].

### 3.4 Schweizer Behörden und föderale Digitaldienste

Schweizer Schlüsselinfrastrukturen umfassen:

- **Fedlex** (fedlex.admin.ch): offizielle Plattform für Bundesrecht auf Basis offener Standards [1]
- **opendata.swiss**: nationales Open-Government-Data-Portal auf CKAN-Basis [44]
- **GEVER**: standardisiertes Geschäftsverwaltungssystem der Bundesverwaltung als Vorlage für kantonale und kommunale Implementierungen [43]
- **Schweizer eID**: dezentrales, datenschutzfreundliches digitales Identitätssystem

Die E-Government-Strategie Schweiz 2024–2027, gemeinsam verabschiedet vom Bundesrat und der Konferenz der Kantonsregierungen, schreibt offene Standards und Interoperabilität vor [16].

### 3.5 Souveräne Technologie-Gemeinschaften

**Decidim** (Barcelona, 2016) ist eine Partizipationsdemokratie-Plattform, die von über 400 Organisationen in 40 Ländern eingesetzt wird, darunter Barcelona, Helsinki und der Kanton Schaffhausen [12].

**Matrix/Element** bietet ein offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll. Der BundesMessenger der deutschen Bundesregierung und Frankreichs Tchap basieren auf Matrix [14].

**Nextcloud** (Stuttgart, 2016) ist die meistgenutzte quelloffene Datei-Sync- und Kollaborationsplattform in europäischen Behörden [13].

**OpenDesk**, 2023 von der deutschen Bundesregierung eingeführt und von ZenDiS verwaltet, ist eine kuratierte Open-Source-Desktop-Suite: Nextcloud + Cryptpad + OpenProject + Jitsi + Element [42].

### 3.6 Forschungslücken

1. **Gesamtkostenvergleichsstudien** zwischen Open-Source- und proprietären Kommunal-Stacks sind spärlich und methodisch inkonsistent.
2. **Längsschnittdaten** aus Städten mit abgeschlossenen Open-Source-Transitionen sind begrenzt. Münchens LiMux-Projekt (2003–2017) gilt als warnendes Beispiel; Post-Mortems identifizieren primär politische, nicht technische Ursachen [30].
3. **Kleingemeinden-Perspektiven** sind unterrepräsentiert.
4. **Nutzerzufriedenheitsforschung** zu Open-Source-Bürgerdienstportalen fehlt fast vollständig.

Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse.

---

## 4. Technologiestack-Analyse

Ein kommunaler Technologiestack lässt sich in neun Funktionsschichten unterteilen.

### 4.1 Digitale Identität und Authentifizierung

**Empfohlene Komponente: Keycloak** [21]

Keycloak ist die De-facto-Open-Source-Lösung für Identity and Access Management (IAM) in Behörden. Es implementiert OpenID Connect, OAuth 2.0 und SAML 2.0 und ermöglicht Verbund mit nationalen Identitätssystemen (BundID in Deutschland, eID in der Schweiz).

| Kriterium | Bewertung (1–5) | Anmerkung |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Einsatzreife | 5 | Produktion erprobt, 10+ Jahre |
| Community | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheit | 5 | CVE-reaktiv, geprüft |
| Gesamtkosten | 4 | Keine Lizenzkosten; Betriebskompetenz nötig |
| Behörden-Einsätze | 5 | Weit verbreitet in EU-Behörden |

**Integrationshinweis:** Keycloak muss mit dem nationalen eID/BundID-System verbunden werden, um doppelte Identitätssilos zu vermeiden.

### 4.2 Dokumentenmanagement und Aktenverwaltung

**Empfohlene Komponenten: Nextcloud** + **OpenProject** [13, 20]

Für Schweizer Kommunen mit GEVER-Anforderungen liefern kantonale Lösungen (CMI, Fabasoft Community) die Compliance-Schicht; Nextcloud dient als kollaboratives Frontend. Im deutschen Kontext decken AKDB- und Dataport-Komponenten den äquivalenten Bedarf ab.

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Empfohlene Komponente: Camunda Platform 8 Community** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe mehrstufige Verwaltungsprozesse und XÖV-Datenstandards-Integration [46]. **Flowable** (Apache 2.0) ist eine leichtgewichtige Alternative.

### 4.4 Bürgerbeteiligung

**Empfohlene Komponente: Decidim** [12]

Decidim ist die ausgereifteste und am weitesten verbreitete Open-Source-Beteiligungsplattform weltweit. Der Kanton Schaffhausen, Barcelona, Helsinki und New York City validieren sie über regulatorische und sprachliche Kontexte hinweg.

**Alternative:** CONSUL Democracy (Madrid), AGPL-3.0.

### 4.5 Kommunikation und Kollaboration

**Empfohlene Komponenten:**
- **Matrix/Element** für Messaging und sichere behördenübergreifende Kommunikation [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Teamkommunikation

Der BundesMessenger bietet einen Referenzeinsatz und Beschaffungsrahmen für kommunale Kontexte.

### 4.6 Open-Data-Veröffentlichung

**Empfohlene Komponente: CKAN** [22]

CKAN ist die weltweit führende Open-Source-Software für Open-Data-Portale: opendata.swiss, data.gov, data.gov.uk. Das Plugin-System ermöglicht Integration mit DCAT-AP, DCAT-AP.de und dem OGD-Schweiz-Metadatenstandard.

### 4.7 Geographische Informationssysteme

**Empfohlene Komponenten:**
- **QGIS** (Desktop/Server) für räumliche Datenbearbeitung [37]
- **GeoServer** für OGC-konforme räumliche Datenpublikation
- **OpenStreetMap** als kartographische Grundlage [36]

Swisstopo (Schweiz) und BKG (Deutschland) stellen offene, hochwertige behördliche Kartendaten bereit.

### 4.8 Öffentliche Website und Content-Management

**Empfohlene Komponenten:**
- **TYPO3** (deutschsprachige Welt): dominierend in schweizer und deutschen Behörden; die TYPO3-Association bietet Langzeit-Support [19]
- **Drupal**: starke internationale Referenzen; Europäische Kommission

Beide Systeme unterstützen Barrierefreiheitsstandards (WCAG 2.1 AA / BITV 2.0) und Mehrsprachigkeit.

### 4.9 Cloud-Infrastruktur und Hosting

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

SCS ist die strategisch wichtigste Infrastrukturentscheidung für europäische Kommunen: vollständig quelloffene Cloud-Plattform (OpenStack + Kubernetes + Ceph), selbst betrieben, durch govdigital eG oder durch zertifizierte SCS-Cloud-Betreiber bereitgestellt.

**Für Kommunen ohne In-house-Cloud-Betriebskapazität:** zertifizierte SCS-Hoster (z. B. plusserver, OSISM) bieten verwaltetes SCS mit vollständigen Datensouveränitätsgarantien.

### 4.10 Referenzarchitektur

```
+-------------------------------------------------------------+
|                   BÜRGERSCHNITTSTELLEN                      |
|         TYPO3/Drupal . Decidim . CKAN . Nextcloud          |
+-------------------------------------------------------------+
|                     DIENSTE-SCHICHT                        |
|     Camunda Workflows . XÖV-Formulare . GeoServer . QGIS   |
+-------------------------------------------------------------+
|                  KOLLABORATIONS-SCHICHT                    |
|     Nextcloud . Matrix/Element . Jitsi . OpenProject       |
+-------------------------------------------------------------+
|                   IDENTITÄTS-SCHICHT                       |
|            Keycloak <-> BundID / Schweizer eID             |
+-------------------------------------------------------------+
|                  INFRASTRUKTUR-SCHICHT                     |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph   |
+-------------------------------------------------------------+
```

Alle Schichten kommunizieren über offene APIs. Datenaustausch erfolgt über XÖV-Standards (Deutschland) [46] oder eCH-Standards (Schweiz). Sicherheit richtet sich nach BSI IT-Grundschutz [26] oder dem Schweizer ISDS-Framework.

---

## 5. Implementierungsfahrplan

Der Plan umfasst 36 Monate in fünf Phasen, jeweils mit definierten Lieferergebnissen, Erfolgskriterien und Entscheidungstoren.

### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand erfassen, Koalition aufbauen.

**Lieferergebnisse:**
- Lenkungsausschuss Digitaltransformation eingesetzt (Stadtführung + IT + Zivilgesellschaft)
- Technologie-Ist-Analyse abgeschlossen
- Stakeholder-Engagement-Plan verabschiedet
- Beschaffungsrahmen etabliert (s. Abschnitt 6)
- Memorandum of Understanding mit kommunalem IT-Dienstleister (Dataport, AKDB, govdigital o. Ä.)

**Erfolgskriterien:**
- Politisches Mandat gesichert (Gemeinderatsbeschluss oder Exekutiventscheid)
- Budgetrahmen genehmigt (indikativ: 200.000–500.000 € für Phase 0–1, je nach Stadtgröße)
- Projektleitung benannt

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die Grundschichten aufbauen, von denen alles andere abhängt.

**Lieferergebnisse:**
- Sovereign Cloud Stack Umgebung in Betrieb (eigen oder gehostet)
- Keycloak Identity Provider deployiert und mit nationalem Identitätssystem verbunden
- Nextcloud Basis-Deployment für interne Kollaboration
- Matrix/Element Messaging für Mitarbeitende
- BSI IT-Grundschutz Basisdokumentation abgeschlossen

**Erfolgskriterien:**
- 100 % der IT-Mitarbeitenden authentifizieren sich über Keycloak SSO
- Dateispeicherung von proprietärer Cloud auf Nextcloud migriert
- Grundlegendes verschlüsseltes Messaging in Betrieb

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die fünf transaktionsstärksten Bürgerdienste auf offener Infrastruktur migrieren oder aufbauen.

**Lieferergebnisse:**
- Fünf meistgenutzte Verwaltungsleistungen auf Camunda/XÖV-Stack deployiert
- TYPO3/Drupal CMS-Migration abgeschlossen
- Open-Data-Portal (CKAN) mit ersten 20 Datensätzen
- Decidim-Instanz für ersten Bürgerbeteiligungsprozess

**Erfolgskriterien:**
- 80 % des Zieldienstvolumens über neues System verarbeitet
- Keine Regression in der Dienstverfügbarkeit gegenüber Baseline
- Erste Open-Data-Veröffentlichung live

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten verbinden; Serviceabdeckung auf 80 % der Transaktionen erweitern.

**Lieferergebnisse:**
- Alle Dienste über Keycloak SSO verbunden
- Nextcloud mit Dokumentenmanagement-Workflows integriert
- GIS-Schicht in Betrieb (QGIS + GeoServer)
- 80 % der Verwaltungsleistungen digitalisiert
- Behördenübergreifender Datenaustausch über XÖV/eCH operativ

**Erfolgskriterien:**
- Ende-zu-Ende-Diensterbringung ohne Papier für 80 % der Transaktionsarten
- Erster jährlicher Open-Data-Bericht veröffentlicht

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Nutzererlebnis verbessern; zu Open-Source-Gemeinschaften beitragen; Ergebnisse veröffentlichen.

**Lieferergebnisse:**
- Nutzerzufriedenheitserhebung (Ziel: NPS > 40)
- Erstbeitrag zu openCode.de / Upstream-Projekten
- Kommunale Open-Source-Community of Practice gegründet
- Leistungsbenchmarks veröffentlicht

**Erfolgskriterien:**
- Mindestens drei Verbesserungen upstream beigesteuert
- Community of Practice aktiv mit ≥ 3 Peer-Kommunen
- Gesamtbetriebskostenbericht veröffentlicht

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Volle digitale Souveränität erreichen; Replikation durch Nachbarkommunen vorbereiten.

**Lieferergebnisse:**
- Vollständige Lizenzkonformitätsprüfung aller Softwarekomponenten
- Datensouveränität verifiziert (100 % auf souveräner Infrastruktur)
- Playbook für Nachbarkommunen publiziert
- Strategiepapier v1.0 veröffentlicht

**Erfolgskriterien:**
- Null proprietäre Einzelanbieter-Abhängigkeiten im kritischen Pfad
- Mindestens eine Nachbarkommune hat das Playbook übernommen

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
| Datenschutzbeauftragte/r | DSGVO-Konformität | Privacy-by-Design-Prüfung in jeder Phase |

### 6.2 Beschaffungsrahmen

Open-Source-Beschaffung erfordert einen anderen Rahmen als proprietärer Lizenzkauf. Grundprinzipien:

**1. Dienste beschaffen, nicht Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**2. Genossenschaftliche Beschaffungsstrukturen nutzen.** govdigital eG und Schweizer kantonale IT-Genossenschaften bieten Rahmenverträge, die das öffentliche Vergaberecht (GWB/Vergaberecht; BöB Schweiz) erfüllen [23].

**3. Das „Public Money? Public Code!“-Prinzip anwenden.** Alle unter Vertrag entwickelte Individualsoftware muss unter einer OSI-anerkannten Lizenz veröffentlicht und auf openCode.de publiziert werden — als Vertragsbedingung [4].

**4. Gesamtbetriebskosten bewerten.** Beschaffungsbewertungen müssen ein 5-Jahres-TCO-Modell umfassen: Implementierung, Hosting, Schulung, Support und Ausstiegskosten.

**5. Interoperabilitätsstandards fordern.** Alle beschafften Systeme müssen XÖV (Deutschland), eCH (Schweiz) und DCAT-AP (EU Open Data) implementieren [46].

**6. Zertifizierte genossenschaftliche Anbieter bevorzugen.** Für Infrastruktur: SCS-zertifizierte Cloud-Betreiber oder Mitglieder von govdigital eG [23].

### 6.3 Veränderungsmanagement

Open-Source-Transitionen scheitern häufig nicht an technischen, sondern an menschlichen Faktoren: Nutzerresistenz, unzureichende Schulung, mittlere Management-Trägheit und politischer Rückzug unter Anbieter-Lobbying.

**Empfehlungen:**
- **Digital-Transformations-Champion** auf politischer Ebene mit explizitem Mandat benennen
- **Open-Source-Botschafter** in jeder Abteilung mit erweiterter Schulung
- Mindestens drei Monate **Parallelbetrieb** vor Abschaltung kritischer Systeme
- **Frühe Erfolge** dokumentieren und kommunizieren (Kosteneinsparungen, neue Fähigkeiten)
- Öffentliches **Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Servicequalitätskennzahlen

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| Politischer Rückzug nach Wahl | Mittel | Hoch | In Satzung/Gesetz verankern; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / Desinformationskampagnen | Hoch | Mittel | TCO-Belege dokumentieren; Zivilgesellschaft einbinden |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulungsprogramm; IT-Genossenschaft; Community of Practice |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout; Referenzarchitektur-Einhaltung |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup-Protokoll; Parallelbetrieb; gestufte Migration |
| DSGVO-Verstoß | Niedrig | Hoch | Privacy-by-Design; DSB-Einbindung; Datenkartierung |
| Benutzerakzeptanzmangel | Mittel | Hoch | Veränderungsmanagement; UX-Tests; Schulung |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests; Incident-Response-Plan |
| Kostenabweichung | Mittel | Mittel | Phasengesteuertes Budget; unabhängiges Projektbüro |

### 7.2 Das Münchener Beispiel

Das Münchener LiMux-Projekt (2003–2017) ist der meistzitierte Fall einer großangelegten kommunalen Open-Source-Transition, die rückgängig gemacht wurde. Ein unabhängiges Post-Mortem ergab, dass die Umkehrung primär durch politischen Führungswechsel, unzureichendes Veränderungsmanagement und Kompatibilitätsprobleme mit Landessystemen verursacht wurde — nicht durch technische Mängel [30]. Der politische Risikorahmen ist mindestens so wichtig wie die technische Planung.

### 7.3 Sicherheitsanforderungen

Der BSI IT-Grundschutz liefert eine umfassende Sicherheitsbaseline, unabhängig vom Lizenzmodell [26]. Kernanforderungen:

- Alle Serverkomponenten erhalten regelmäßige Sicherheitsupdates mit dokumentiertem Patch-Management-Prozess
- Authentifizierung erfüllt BSI Authenticator Assurance Level 2 (AAL2) für bürgergerichtete Dienste
- Daten in Transit verschlüsselt (TLS 1.3 Minimum); ruhende Daten verschlüsselt für sensitive Kategorien
- Penetrationstests an jedem Phasentor
- Incident-Response-Plan gemäß NIS2-Verpflichtungen [27]
- Software Bill of Materials (SBOM) für alle Open-Source-Abhängigkeiten

---

## 8. Schlussfolgerung

Die in dieser Arbeit ausgewerteten Belege konvergieren auf vier Befunde:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift und produktionserprobt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Einsätzen in Peer-Kommunen erfüllt werden.

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland) und der Interoperable-Europe-Act (EU) schaffen gesetzliche Verpflichtungen, die proprietäre, herstellergebundene Systeme langfristig nicht erfüllen können. Frühzeitig handelnde Kommunen bauen Compliance-Kapital auf; spät handelnde akkumulieren regulatorische Schulden.

**3. Die wirtschaftliche Begründung ist überzeugend, wenn die Gesamtkosten korrekt berechnet werden.** Open-Source-Stacks eliminieren Pro-Kopf-Lizenzkosten — oft 100–300 € pro Nutzerin und Jahr allein für Produktivitätssoftware — und reduzieren das Herstellerbindungsrisiko. Genossenschaftliche Beschaffungsmodelle verteilen Implementierungskosten auf viele Kommunen.

**4. Erfolg erfordert ebenso viel politische und organisatorische Investition wie technische.** Klares politisches Mandat, qualifiziertes Veränderungsmanagement und nachhaltiges Stakeholder-Engagement sind die bindenden Faktoren.

Städte, die als Erste handeln, profitieren von Pioniervorteilen: Sie gestalten kooperative Standards, bauen Fachkompetenz auf und tragen zu den Open-Source-Gemeingütern bei, die alle Kommunen teilen. Die Einladung ist offen.

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023*. Brüssel. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Interoperable Europe Act — Verordnung (EU) 2024/903*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903

[7] Wirtz, B.W., & Weyerer, J.C. (2017). *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M. et al. (2012). *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. https://www.fitko.de/

[10] openCode.de. (2022). *openCode — Open Source für die Verwaltung*. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/

[12] Decidim Association. (2021). *Decidim: Freie quelloffene Partizipationsdemokratie*. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud für Behörden*. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2023). *TYPO3 in der öffentlichen Verwaltung*. https://typo3.org/

[20] OpenProject GmbH. (2023). *OpenProject für Behörden*. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak IAM*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open-Source-Datenportal-Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. https://govdigital.de/

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium*. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *NIS2-Richtlinie — Richtlinie (EU) 2022/2555*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[29] Vereinte Nationen (UNDESA). (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS Project. (2023). *QGIS*. https://www.qgis.org/ — [GPL-2.0+]

[39] CNCF. (2023). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. https://opendata.swiss/ — [CC-BY-4.0]

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. https://www.xoev.de/

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Licence (CC-BY-4.0) veröffentlicht.*
*Namensnennung: Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur (sebk4c@tuta.com)*
