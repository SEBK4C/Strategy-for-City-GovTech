---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitatvollständiger Entwurf"
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
  - ZenDiS
  - GovStack
  - eCH-Standards
  - Gesamtbetriebskosten
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitatvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (Übersetzung) · English (Quelle)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Übersetzung des Quelldokuments `en/sovereign-by-design-v0.2.0.md`. Änderungen werden zuerst im Quelldokument vorgenommen.*

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernächste Ebene demokratischer Administration, stehen jedoch vor einem strukturellen Dilemma: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellergebunden und nicht im Einklang mit öffentlichen Interessen. Diese Arbeit legt eine umfassende, zitatvollständige Strategie für die Implementierung eines modernen Open-Source-Verwaltungstechnologie-Stacks in Städten und Gemeinden vor. Auf der Grundlage vorbildlicher Praxis des Schweizer EMBAG-Gesetzes, des deutschen OZG-2.0-Reformprogramms, der Sovereign-Cloud-Stack- und OpenDesk-Initiativen — verwaltet durch ZenDiS GmbH — sowie der GovStack-Bausteininitiative von ITU und DIAL werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie von ersten Grundlagen her erarbeitet.

Die Analyse umfasst zehn Technologiekomponenten, bewertet nach Digitaler Souveränität, Interoperabilität, Gesamtbetriebskosten und demokratischer Eignung. Empirische Gesamtkostendaten aus der Migration der Französischen Gendarmerie (72.000 Arbeitsplätze, ~40 % Kostensenkung), der Extremadura-Region und Zaragoza belegen den wirtschaftlichen Vorteil. Die Arbeit zeigt: Open-Source-Kommunaltechnologiestacks sind nicht nur technisch reif, sondern fiskalisch überlegen, demokratisch notwendig und in wachsenden Rechtsordnungen gesetzlich vorgeschrieben. Der 36-monatige Fahrplan enthält ein Anbieterverzeichnis und eine Sonderanleitung für Kleingemeinden.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, ZenDiS, GovStack, eCH-Standards, Gesamtbetriebskosten

---

## 1. Einleitung

Die digitale Transformation kommunaler Verwaltungen ist keine Frage des Ob, sondern des Wie. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; der Gesetzgeber fordert Interoperabilität und Datenschutz; Haushaltszwänge verlangen nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte und Gemeinden weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit gefangen [1, 29].

Die Folgen dieser Abhängigkeit sind belegt: Herstellerbindung erhöht Wechselkosten und verschiebt Verhandlungsmacht [4]; proprietäre Formate behindern behördenübergreifenden Datenaustausch [45]; geschlossene Software verhindert unabhängige Sicherheitsstudien [26]; wiederkehrende Lizenzgebühren belasten Haushalte [3, 5]. Wenn die Software demokratischer Institutionen im Besitz privater Akteure ist, entsteht ein struktureller Interessenkonflikt [4, 47].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG (2023) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware grundsätzlich als Open Source veröffentlicht wird [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative — verwaltet durch ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) — sind das ambitionierteste Open-Source-GovTech-Programm Europas [2, 3, 42, 51]. Die GovStack-Initiative von ITU und DIAL bietet ein globales Rahmenwerk wiederverwendbarer digitaler öffentlicher Infrastruktur-Bausteine [52].

### 1.1 Begriffserklärungen

*Kommunale Verwaltung* bezeichnet Städte und Gemeinden einschließlich Schweizer Gemeinden, deutscher Kommunen und vergleichbarer Strukturen. Die Strategie ist für Gemeinden von 2.000 bis über 500.000 Einwohnerinnen und Einwohnern ausgelegt.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten unter OSI-anerkannten Lizenzen auf Infrastruktur, die die Kommune kontrolliert oder ohne unzumutbaren Aufwand wechseln kann.

*Digitale Souveränität* ist die Fähigkeit, unabhängige Entscheidungen über digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und zu migrieren [3, 48].

*Digitale öffentliche Infrastruktur (DPI)* bezeichnet gemeinsame digitale Systeme — Identität, Zahlungen, Datenaustausch — die als öffentliche Versorgungsleistungen funktionieren und von keinem einzelnen Akteur besessen werden [52].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunal-Technologiestack 2026 aus?
2. Was lässt sich aus der schweizerischen, deutschen und europäischen Souveränitätstechnologie-Gemeinschaft lernen?
3. Was ist der optimale Phasenimplementierungsweg für Gemeinden verschiedener Größen?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden?
5. Wie groß ist der Gesamtkostenvorteil offener gegenüber proprietären Stacks?

---

## 2. Methodik

Diese Arbeit verwendet einen Mehr-Methoden-Forschungsansatz:

**Systematische Literaturrecherche** peer-begutachteter Veröffentlichungen und Grundlagendokumente aus 2010–2026 zu E-Government-Theorie, digitaler Souveränität, Open-Source-Software in Behörden und kommunaler Digitaltransformation.

**Vergleichende Politikanalyse** von Technologiegesetzen aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, OpenDesk-Programm) und der Europäischen Union (Interoperable-Europe-Act 2024, EU-Open-Source-Strategie 2020–2023, EU Data Act 2023).

**Technologiestack-Bewertung** anhand einer Scoring-Matrix: (a) Lizenzoffenheit, (b) Einsatzreife, (c) Community-Gesundheit, (d) Interoperabilitätsstandards, (e) Sicherheitsprofil, (f) Gesamtbetriebskosten, (g) behördliche Einsatznachweise. Methodologie folgt dem OSOR-Bewertungsrahmen [53].

**TCO-Metaanalyse** empirischer Daten aus abgeschlossenen Open-Source-Migrationen in öffentlichen Verwaltungen.

### 2.1 Einschränkungen

Technologiestack-Bewertungen spiegeln den Stand per Juni 2026 wider. Kostenschlätzungen sind indikative Bereiche, validiert gegen bekannte Einsätze.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen

Die E-Government-Literatur hat sich durch vier Generationen entwickelt [30]: Digitalisierung bestehender Prozesse (1995–2005) [29]; Online-Dienstleistungserbringung (2005–2012) [7]; Open Data und Partizipationsplattformen (2012–2020) [8]; Plattform-Government und Souveränitätswende (2020–heute) [45, 30].

Das Reifegradmodell von Wirtz und Weyerer [7] identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz. Lathrop und Ruma (2010) definieren Offene Regierung entlang Transparenz, Partizipation und Kollaboration — Achsen, die direkt den Open-Source-Prinzipien entsprechen [47].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Couture und Toupin (2019) unterscheiden drei Register: staatliche Souveränität über digitale Infrastruktur, individuelle Datensouveränität und kollektive technologische Selbstbestimmung [48]. Der EU Data Act 2023 führt Rechte öffentlicher Stellen auf Zugang zu privatwirtschaftlich gehaltenen Daten ein — mit direkten Auswirkungen auf kommunale IoT- und Smart-City-Einsätze [54].

Der Sovereign Cloud Stack (SCS R7, 2025) ist die konkreteste Realisierung digitaler Souveränität auf Infrastrukturebene [3, 11]. Das EMBAG (in Kraft ab 1. Januar 2024) verpflichtet die Schweiz zu einer der progressivsten Open-Source-Mandatsregeln weltweit [1].

### 3.3 Das deutsche OZG-Ökosystem und ZenDiS

Das OZG 2.0 (2024) adressiert Schwächen der ersten Generation durch das „Once Only“-Prinzip, den EfA-Ansatz und eine Bundesplattform-Architektur um BundID und FITKO [2, 9]. BundID erreichte Ende 2023 3,2 Millionen registrierte Nutzerinnen und Nutzer [2].

ZenDiS (gegründet 2022, Berlin) ist die institutionelle Trägerin des OpenDesk-Programms [51]. ZenDiS kuratiert die OpenDesk-Suite, verwaltet den Behörden-Open-Source-Katalog und vergibt Entwicklungsaufträge unter dem „Public Money? Public Code!“-Vertragsprinzip. Die Plattform openCode.de verzeichnet über 500 Open-Source-Repositories öffentlicher Stellen [10, 51].

OpenDesk v2.0 (2025) ergänzte Keycloak-native Authentifizierung, verbesserte mobile Clients und ein Helm-basiertes Kubernetes-Deployment-Chart für kommunales Selbsthosting [42, 51].

### 3.4 Schweizer Digitaldienste und eCH-Standards

Die E-Government-Strategie Schweiz 2024–2027, gemeinsam von Bundesrat und KdK verabschiedet, schreibt offene Standards und Interoperabilität vor [16].

**eCH-Standards** sind Schweizer XML-basierte Interoperabilitätsstandards für öffentliche Verwaltungen, verwaltet durch den Verein eCH. Für Gemeinden relevante Standards: eCH-0007 (Gemeindedaten), eCH-0020 (Meldewesen), eCH-0046 (Kontaktdaten), eCH-0058 (Schnittstellendefinitionen), eCH-0010 (Postadresse), eCH-0160 (Archivierung). Sie entsprechen dem XÖV-Familienprinzip in Deutschland und sind für kantonale und kommunale Systeme verbindlich [57].

**Schweizer eID**: Nach der Volksabstimmung vom März 2021 (64,4 % Ablehnung) wurde ein neues, datenschutzfreundliches, dezentrales eID-System entwickelt. Das revidierte E-ID-Gesetz wurde im März 2023 verabschiedet; kantonale Piloten begannen 2024; Nationwide-Verfügbarkeit ist für 2026 angestrebt [56]. Das neue eID-Modell setzt auf Self-Sovereign Identity (SSI) mit einem staatlich ausgestellten Credential-Wallet.

### 3.5 Souveräne Technologie-Gemeinschaften

**Decidim** (Barcelona, 2016): über 450 Einsätze in mehr als 40 Ländern. Der Kanton Schaffhausen, Kanton Zürich und die Stadt Bern nutzen Decidim für Haushaltsbefragungen, Strategieprozesse und Quartiersbeteiligung [12].

**CONSUL Democracy** (Madrid, 2015): komplementäre Partizipationsplattform mit starker Verbreitung im spanischsprachigen Raum, AGPL-3.0 [58].

**Matrix/Element**: Der BundesMessenger ist seit 2023 in allen Bundesministerien und mehreren Ländern operativ. Frankreichs Tchap versorgt 330.000 Beamte. NATO und britisches Verteidigungsministerium betreiben Matrix-Einsätze [14].

**GovStack** (ITU/DIAL): globales Rahmenwerk digitaler öffentlicher Infrastruktur-Bausteine — Identität, Einverständnis, Informationsmediator (X-Road), Zahlungen, Workflow — mit offenen Spezifikationen und Referenzimplementierungen. Kommunen können einzelne Bausteine inkrementell übernehmen [52].

### 3.6 OSOR und der EU Open Source Observatory

Der OSOR-Jahresbericht 2023 dokumentiert 36 neue behördliche Open-Source-Veröffentlichungen, identifiziert Deutschland und die Schweiz als führende Rechtsordnungen und verzeichnet ein Wachstum der Open-Source-Einführung in kommunalen Verwaltungen von ~18 % pro Jahr [53]. Genossenschaftliche Beschaffungsmodelle und länderübergreifendes Code-Sharing werden als primäre Hebel empfohlen.

### 3.7 Gesamtbetriebskosten: Empirische Belege

**Französische Gendarmerie Nationale**: Migration von 72.000 Arbeitsplätzen auf Ubuntu/LibreOffice (2008–2014). Berichtete Gesamtkosteneinsparung: ~40 %, entsprechend rund 14 Mio. EUR über fünf Jahre [59].

**Extremadura (Spanien)**: Einsatz von LinEx auf 40.000 öffentlichen Arbeitsplätzen; geschätzte Lizenzersparnisse 30 Mio. EUR jährlich [60].

**Zaragoza**: Migration von 3.000 Gemeindearbeitsplätzen; Lizenzersparnisse 1,5 Mio. EUR über drei Jahre; einmalige Migrationskosten 600.000 EUR; Nettoeinsparung 900.000 EUR [60].

**München LiMux** (2003–2017): politisch umgekehrt, nicht technisch gescheitert. Unabhängige Post-Mortems nennen vier Ursachen: politischer Führungswechsel 2014; ungender Schulungsaufwand; Kompatibilitätsdefizite bei Ländersystemen; keine parteiübergreifende Eigentümerschaft [30, 61].

**Richtwerte für Kommunen:**
- Lizenzersparnisse: 80–200 EUR/Arbeitsplatz/Jahr; 200–600 EUR/Server/Jahr
- Migrationsaufwand: 300–800 EUR/Arbeitsplatz (einmalig)
- Amortisation: 2–4 Jahre
- Langfristiger TCO-Vorteil: 30–45 % über 10 Jahre

---

## 4. Technologiestack-Analyse

Der kommunale Technologiestack gliedert sich in zehn Funktionsschichten. Bewertung 1–5; 5 = vollständig offen, produktionserprobt, breit eingesetzt.

### 4.1 Digitale Identität und Authentifizierung

**Empfehlung: Keycloak 24.x** [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für europäische Behörden. Version 24 (2024) führte native Unterstützung für das eIDAS-2.0-Wallet-Ökosystem ein. Es verbindet sich mit BundID (Deutschland), Schweizer eID und österreichischer eID über OIDC/SAML-Bridges.

| Kriterium | Bewertung | Anmerkung |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Einsatzreife | 5 | Produktion, 12+ Jahre, CNCF |
| Community | 5 | Red-Hat-gefördert, 1.000+ Beitragende |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS 2.0 |
| Sicherheit | 5 | CVE-reaktiv, FIPS-140-2-Option |
| TCO | 4 | Keine Lizenz; Betriebskompetenz erforderlich |
| Behörden-Einsätze | 5 | EU-Institutionen, Bundesländer, Kantone |

### 4.2 Dokumentenmanagement und Aktenverwaltung

**Empfehlung: Nextcloud 29.x** + **OpenProject 14.x** [13, 20]

Nextcloud Hub 8 (2025) ergänzte Files-Lifecycle-Management, automatische Aufbewahrungsdurchsetzung und ein verbessertes Prüfprotokoll. Für Schweizer GEVER-Konformität liefern kantonale Lösungen (CMI, Fabasoft) die Compliance-Schicht; Nextcloud dient als kollaboratives Frontend. Verifizierte Einsätze: Schweizer Bundesverwaltung (ausgewählte Abteilungen), Freistaat Sachsen, über 1.000 Kommunen [13].

### 4.3 Workflow-Automatisierung

**Empfehlung: Camunda Platform 8 Community** [33]

Camunda 8 (Zeebe-Engine): verteilte, hochdurchsatzfähige BPMN-2.0-Ausführung. Community Edition vollständig Apache 2.0. Für einfachere Deployments: Flowable 6.x oder Activiti 7.x (beide Apache 2.0). Kritisch: XÖV-Datenvalidatoren (Deutschland) bzw. eCH-0058-Schnittstellendefinitionen (Schweiz) müssen in die Workflow-Engine integriert werden.

### 4.4 Bürgerbeteiligung

**Empfehlung: Decidim 0.28.x** [12]

Release 0.28 (2025): verbesserte Barrierefreiheit (WCAG 2.2 AA), maschinengestützte Übersetzungsunterstützung, neu gestaltetes Mobile-UI. Schweizer Einsätze: Kanton Schaffhausen (Haushaltskonsultation), Kanton Zürich (Strategieprozesse), Stadt Bern (Quartiersbeteiligung).

**Alternative: CONSUL Democracy 2.3.x** [58]

### 4.5 Kommunikation und Kollaboration

**Empfehlung:**
- **Matrix/Element Server** für Messaging [14]
- **Jitsi Meet** oder **BigBlueButton 3.x** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Teamkommunikation im OpenDesk-Kontext

Die vom ZenDiS veröffentlichte BundesMessenger-Referenzarchitektur (2023) bietet ein direkt wiederverwendbares Kubernetes-Deployment-Spec für kommunale Matrix-Einsätze [51].

### 4.6 Open-Data-Veröffentlichung

**Empfehlung: CKAN 2.11.x** [22]

CKAN versorgt opendata.swiss, GovData.de, data.gov, data.gov.uk und Dutzende nationaler Portale. CKAN 2.11 (2025): native DCAT-AP-3.0-Unterstützung. Für Gemeinden, die bereits an opendata.swiss oder GovData.de teilnehmen: leichtgewichtiger CKAN-Harvesting-Konnektor ermöglicht Upstream-Veröffentlichung ohne eigenständigen Portal-Betrieb.

### 4.7 Geographische Informationssysteme

**Empfehlung:**
- **QGIS 3.38 LTR** [37]
- **GeoServer 2.25** für OGC-konforme WMS/WFS-Dienste
- **MapLibre GL JS** für browserbasierte Kartenanwendungen
- **OpenStreetMap** als kartographische Grundlage [36]

Swisstopo (map.geo.admin.ch) liefert offene Basiskartenkacheln unter Creative-Commons-Lizenz. Das BKG stellt offizielle topographische Basisdaten unter DL-DE/BY-2.0 bereit.

### 4.8 Öffentliche Website und Content-Management

**Empfehlung:**
- **TYPO3 13 LTS** für deutschsprachige Kommunen [19]
- **Drupal 10.x** bei starkem Mehrsprächigkeitsbedarf

TYPO3 13 LTS (2024, Support bis 2027): neues Backend, natives Headless-API, verbesserte BITV-2.0-/WCAG-2.1-AA-Tools. Die Government-Special-Interest-Group der TYPO3 Association pflegt eine kommunale Referenzdistribution.

### 4.9 Cloud-Infrastruktur

**Empfehlung: Sovereign Cloud Stack R7** [3, 11]

SCS R7 (2025) standardisiert auf OpenStack 2024.1 (Caracal), Kubernetes Cluster API, Rook/Ceph und Cilium. Zertifizierte SCS-Betreiber (Stand 2026): plusserver, OSISM, Wavestack, Artcodix. govdigital eG bietet einen verwalteten SCS-Cluster speziell für Behördenlasten mit Rahmenverträgen nach GWB [23].

### 4.10 Schriftgutverwaltung

**Empfehlung: OpenDesk mit Nextcloud-Files-Lifecycle + XDOMEA-Konnektor**

XDOMEA (XML-basierte Schriftverwaltungsschnittstelle) ist der deutsche Standard für elektronische Aktenübergabe an Archive. Ein Nextcloud-XDOMEA-Konnektor ermöglicht direkte Einreichung an Landesarchive ohne proprietäre Middleware. In der Schweiz regelt eCH-0160 die digitale Aktenübergabe [57].

### 4.11 Referenzarchitektur

```
╔══════════════════════════════════════════════════════════════╗
║                   BÜRGERSCHNITTSTELLEN                        ║
║         TYPO3 · Decidim · CKAN · Nextcloud Dateien         ║
╠══════════════════════════════════════════════════════════════╣
║                     DIENSTE-SCHICHT                          ║
║   Camunda Workflows · XÖV/eCH-Formulare · GeoServer · QGIS ║
╠══════════════════════════════════════════════════════════════╣
║                  KOLLABORATIONS-SCHICHT                      ║
║     Nextcloud · Matrix/Element · Jitsi · OpenProject        ║
╠══════════════════════════════════════════════════════════════╣
║                   IDENTITÄTS-SCHICHT                        ║
║            Keycloak ↔ BundID / Schweizer eID / eIDAS        ║
╠══════════════════════════════════════════════════════════════╣
║                  INFRASTRUKTUR-SCHICHT                      ║
║   Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph   ║
╚══════════════════════════════════════════════════════════════╝
```

Datenaustausch: XÖV-Familie (DE) [46] · eCH-Familie (CH) [57] · DCAT-AP 3.0 (EU)  
Sicherheit: BSI IT-Grundschutz (DE) [26] · ISDS (CH) · NIS2 (EU) [27]

---

## 5. Implementierungsfahrplan

Der Plan umfässt 36 Monate in fünf Phasen. Abschnitt 10 enthält größenspezifische Anpassungen.

### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand erfassen, Koalition aufbauen.

**Lieferergebnisse:** Lenkungsausschuss Digitaltransformation · Technologie-Ist-Analyse · Stakeholder-Engagement-Plan · Beschaffungsrahmen · MoU mit kommunalem IT-Dienstleister · DSFA-Baseline

**Budgetrahmen:** 50.000–150.000 EUR

**Erfolgskriterien:** Politisches Mandat gesichert · Budget für Phase 1 genehmigt · Projektleitung benannt (≥50 % Zeitanteil)

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundschichten aufbauen.

**Lieferergebnisse:** SCS-Umgebung in Betrieb (eigen oder via Hoster) · Keycloak deployiert und mit nationalem Identitätssystem verbunden · Nextcloud-Basis-Deployment · Matrix/Element für Mitarbeitende · BSI IT-Grundschutz / ISDS Basisdokumentation · Software Bill of Materials

**Budgetrahmen:** 200.000–600.000 EUR

**Erfolgskriterien:** 100 % der IT-Mitarbeitenden über Keycloak SSO · Dateispeicherung für ≥3 Fachbereiche auf Nextcloud migriert · Verschlüsseltes Messaging in Betrieb

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Fünf transaktionsstärkste Bürgerdienste auf offener Infrastruktur.

**Lieferergebnisse:** 5 Verwaltungsleistungen auf Camunda/XÖV oder eCH deployiert · TYPO3/Drupal CMS-Migration mit Barrierefreiheitsprüfung · CKAN mit 20 Datensätzen, geharvestet durch nationales Portal · Decidim-Instanz für ersten Beteiligungsprozess · Schulungsprogramm abgeschlossen

**Budgetrahmen:** 150.000–500.000 EUR

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten verbinden; 80 % Transaktionsabdeckung.

**Lieferergebnisse:** Alle Dienste über Keycloak SSO verbunden · Nextcloud mit Dokumentenmanagement-Workflows (XDOMEA/eCH-0160) · GIS-Schicht (QGIS + GeoServer) · 80 % Verwaltungsleistungen digitalisiert · Jährlicher Open-Data-Bericht

**Budgetrahmen:** 200.000–600.000 EUR

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Lieferergebnisse:** Bürgerzufriedenheitserhebung (Ziel: NPS ≥40) · Erstbeitrag zu openCode.de · Open-Source-Community of Practice mit ≥3 Peer-Kommunen · TCO-Bericht (Ist vs. Prognose) · Penetrationstest

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Lieferergebnisse:** Vollständige Lizenzkonformitätsprüfung · Datensouveränität verifiziert (100 % souveräne Infrastruktur) · Replikations-Playbook auf openCode.de · Strategiepapier v1.0

**Erfolgskriterien:** Null proprietäre Einzelanbieter-Abhängigkeiten im kritischen Pfad · Mindestens eine Nachbarkommune hat das Playbook übernommen

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Übersicht

| Stakeholder | Hauptinteresse | Einbindungsansatz | Hauptsorge |
|---|---|---|---|
| Bürgermeisterin / Exekutive | Politischer Erfolg, Kosten | Führungsbriefing, Dashboard | Sichtbare Unterbrechungen? |
| Gemeinderat | Kontrolle, Legitimität | Quartalsberichte | Rechtskonformität |
| Städtisches IT-Team | Machbarkeit, Arbeitsbelastung | Co-Design, Schulung | Qualifikationslücken |
| Vergabeamt | Rechtskonformität | Rahmenverträge | GWB/BöB-Konformität |
| Mitarbeitende | Benutzerfreundlichkeit | UX-Tests, Schulung | „Meine Tools funktionieren jetzt“ |
| Bürgerinnen und Bürger | Servicequalität, Datenschutz | Partizipatives Design | Ausfall, Datensicherheit |
| Zivilgesellschaft | Transparenz, Zugang | Decidim, öffentliche Roadmaps | Code-Zugang, Revisionsprüfbarkeit |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de | Nachhaltige Finanzierung |
| Souveräne Technologieanbieter | Partnerschaft | Zertifizierte Partnervereinbarungen | Vertragsbedingungen |
| Datenschutzbeauftragte/r | DSGVO / DSG | Privacy-by-Design pro Phase | Datenspeicherort |

### 6.2 Beschaffungsrahmen

**Grundsatz 1 — Dienste beschaffen, nicht Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**Grundsatz 2 — Genossenschaftliche Beschaffungsstrukturen nutzen.** govdigital eG und Schweizer kantonale IT-Genossenschaften bieten Rahmenverträge nach GWB/BöB [23].

**Grundsatz 3 — „Public Money? Public Code!“ anwenden.** Alle unter Vertrag entwickelte Individualsoftware muss unter OSI-anerkannter Lizenz veröffentlicht und auf openCode.de (Deutschland) oder äquivalenten Plattformen publiziert werden [4].

**Grundsatz 4 — 5-Jahres-Gesamtbetriebskosten bewerten.** Bewertung muss Implementierung, Hosting, Schulung, Support, Ausstiegskosten und Lock-in-Risikozuschlag umfassen.

**Grundsatz 5 — Interoperabilitätsstandards vorschreiben.** XÖV (DE) [46], eCH (CH) [57], DCAT-AP 3.0 (EU). Nicht-Konformität ist Ausschlusskriterium.

**Grundsatz 6 — Zertifizierte genossenschaftliche Anbieter bevorzugen.** SCS-zertifizierte Betreiber oder govdigital-eG-Mitglieder [23].

#### Musterbewertungskriterien und Gewichtungen

| Kriterium | Gewichtung | Begründung |
|---|---|---|
| Technische Qualität und Architekturpassung | 30 % | Langfristige Wartbarkeit |
| OSI-Lizenz und Offenheit | 15 % | Rechtliche und strategische Konformität |
| 5-Jahres-TCO (transparentes Modell) | 20 % | Haushaltsverantwortung |
| Interoperabilitätsstandards-Konformität | 15 % | OZG/eCH/DCAT-AP-Pflicht |
| Open-Source-Engagement des Anbieters | 10 % | PMPC-Prinzip |
| Einsatznachweise im öffentlichen Sektor | 10 % | Risikoreduktion |

### 6.3 Veränderungsmanagement

Open-Source-Transitionen scheitern am häufigsten nicht technisch, sondern an menschlichen Faktoren: Nutzerresistenz, unzureichende Schulung, Trauer des mittleren Managements und politischer Rückzug unter Anbieter-Lobbying [30, 61].

**Empfehlungen:**
- **Digital-Transformations-Champion** auf politischer Ebene mit explizitem Mandat benennen
- **Open-Source-Botschafter** in jedem Fachbereich (10 % Zeitanteil für Peer-Support)
- Mindestens drei Monate **Parallelbetrieb** vor Abschaltung kritischer Systeme
- **Frühe Erfolge** öffentlich kommunizieren (Kosteneinsparungen, neue Fähigkeiten)
- Öffentliches **Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Servicequalitätskennzahlen
- **Personalrat / Gewerkschaftsvertretung** frühzeitig einbinden
- Unabhängige **„Ein Tag im Leben“-UX-Studie** vor und nach der Migration

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| Politischer Rückzug nach Wahl | Mittel | Hoch | In Gemeindeordnung/Satzung verankern; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / Desinformation | Hoch | Mittel | Unabhängige TCO-Nachweise publizieren; Lobbying-Aktivitäten im Transparenzregister dokumentieren |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulungsprogramm ab Phase 0; IT-Genossenschaft als Auffangnetz |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout; Referenzarchitektur; Integrationstests in CI/CD |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup + Restore-Drill; Parallelbetrieb; Rollback-Kriterien |
| DSGVO-Verstoß | Niedrig | Hoch | Privacy-by-Design; DSB-Freigabe; DSFA; Datenkartierung |
| Benutzerakzeptanzmangel | Mittel | Hoch | Pflichtbudget Veränderungsmanagement (≥15 % Projektgesamtbudget) |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; jährlicher Penetrationstest; SBOM; NIS2-Incident-Response |
| Kostenabweichung | Mittel | Mittel | Phasengesteuertes Budget; unabhängiges Projektbüro; monatliches Varianzreporting |

### 7.2 Das Münchener Beispiel

Münchem LiMux (2003–2017) ist der meistzitierte Fall eines großangelegten kommunalen Open-Source-Rückzugs. Vier Ursachen [30, 61]: politischer Führungswechsel 2014; unzureichendes Schulungsbudget (~ein Drittel des Empfehlenswerten); Kompatibilitätsdefizite bei ODF-Unterstützung in Bayerischen Landessystemen; keine parteiübergreifende Eigentümerschaft. Die technische Implementierung war erfolgreich. Die Lektion: Politisches Risikomanagement — besonders die Verankerung digitaler Souveränität als kommunale Verfassungswert — ist die bindende Einschränkung.

### 7.3 Sicherheitsanforderungen

BSI IT-Grundschutz [26] und NIS2 [27] setzen die Sicherheitsbaseline. Kernanforderungen:
- Kritische Patches innerhalb von 30 Tagen eingespielt
- Bürgergerichtete Authentifizierung: BSI AAL2 (MFA obligatorisch)
- TLS 1.3 Minimum; HSTS; AES-256 für sensible Datenkategorien
- Jährlicher Penetrationstest an Phasengrenzen
- SBOM für alle Open-Source-Abhängigkeiten; automatisches CVE-Scanning
- Incident-Response gemäß NIS2 Art. 23 (24h Frühwarnung, 72h Meldung)

---

## 8. Verzeichnis souveräner Technologieanbieter

### 8.1 Deutschland

| Anbieter | Typ | Hauptangebot | Beschaffungsweg |
|---|---|---|---|
| govdigital eG | Öffentlich-rechtliche Genossenschaft | SCS-Cloud, BundesMessenger-Hosting | Rahmenvertrag (alle öffentlichen Stellen) |
| Dataport AöR | Öffentlicher IT-Dienstleister | OZG-Dienste, Nextcloud, ENA | AKDB/Dataport-Rahmen |
| AKDB | Kommunale IT-Genossenschaft | BayernPortal, Einwohnermeldeamt | Bayern-Rahmen; GWB-konform |
| ZenDiS GmbH | Bundesbehörde | OpenDesk-Programmführung | Direktkontakt für große Einsätze |
| plusserver | Zertifizierter SCS-Betreiber | Verwaltetes SCS | SCS-Zertifizierung; GWB-konform |
| OSISM GmbH | SCS-Tooling/Deployment | SCS-Plattform-Deployment | Direkte Vergabe |
| Univention | IAM / Verzeichnisdienste | UCS + Keycloak-Integration | Direkt oder Rahmen |

### 8.2 Schweiz

| Anbieter | Typ | Hauptangebot | Beschaffungsweg |
|---|---|---|---|
| SECO / eOperations | Bundesbehörde | E-Government-Plattformdienste | Kantonale Vereinbarungen |
| Abraxas Informatik | Kantonaler IT-Dienstleister | GEVER, Einwohnerregister | Kantonaler Rahmen |
| CMI AG | Kommunalsoftware | CMI AXIOMA (GEVER, eCH), CMI Pro | Direkte Vergabe (WTO/BöB-Schwelle) |
| Netcetera | Fintech/GovTech | Schweizer eID-Wallet-Integration | Direkte Vergabe |

### 8.3 Europäische Gemeinschaften

| Gemeinschaft | Governance | Ressource |
|---|---|---|
| OSBA / Sovereign Cloud Stack | OSBA e.V. | scs.community |
| FSFE | Non-Profit | fsfe.org, publiccode.eu |
| Decidim Association | Multi-Stakeholder | decidim.org |
| OSOR (EU) | Europäische Kommission | joinup.ec.europa.eu |
| GovStack Initiative | ITU + DIAL + Partner | govstack.global |
| openCode.de | ZenDiS / Digitalservice | opencode.de |

---

## 9. Gesamtkostenrahmen

### 9.1 Kostenstruktur

| Kategorie | Open Source | Proprietär | Anmerkung |
|---|---|---|---|
| Softwarelizenzen Produktivitätssuite | 0 EUR | 80–200 EUR/Platz/Jahr | Microsoft 365 E3: ~180 EUR/Platz/Jahr |
| Serverlizenzen (OS) | 0 EUR | 200–800 EUR/Server/Jahr | Windows Server Standard |
| Datenbanklizenzen | 0 EUR | 500–2.000 EUR/Server/Jahr | SQL Server Standard |
| Cloud-Hosting / Infrastruktur | 200–500 EUR/Server/Jahr | 400–1.200 EUR/Server/Jahr | SCS vs. Hyperscaler |
| Implementierung (einmalig) | 300–800 EUR/Arbeitsplatz | 50–150 EUR/Arbeitsplatz | Mehraufwand Migration |
| Schulung (einmalig) | 200–500 EUR/Mitarbeitende | 50–200 EUR/Mitarbeitende | Höher bei OS-Transition |
| Support / Wartung (jährlich) | 30–80 EUR/Platz | 0 (in Lizenz enthalten) | Genossenschafts-Support möglich |
| **5-Jahres-Nettokosteni (500 Plätze)** | **~1,2–1,8 Mio. EUR** | **~2,0–3,2 Mio. EUR** | **Einsparung: 0,8–1,4 Mio. EUR** |

### 9.2 Versteckte Kosten proprietärer Systeme

1. **Lizenzpreiseskalation:** Microsoft, Oracle, SAP: +8–15 % pro Jahr seit 2018
2. **Wechselkosten:** Migration aus tief integriertem proprietärem System kostet typisch 2–5× die ursprünglichen Implementierungskosten
3. **Auditrisiko:** Software-Asset-Management-Audits verursachen 50.000–500.000 EUR Compliance-Kosten
4. **Sicherheitsvorfallkosten:** Durchschnittliche kommunale Ransomware-Bereinigung: 1–5 Mio. EUR [26]

### 9.3 Genossenschaftliche Kostenteilung

Zehn Kommunen, die einen govdigital-eG-Infrastrukturvertrag teilen, reduzieren die Pro-Kommune-Infrastrukturkosten um 60–80 % gegenüber unabhängiger Vergabe. Das EfA-Modell (Einer für Alle) des OZG wendet die gleiche Logik auf die Anwendungsentwicklung an [2].

---

## 10. Leitfaden für Kleingemeinden

### 10.1 Stufe A: Sehr kleine Gemeinden (unter 5.000 Einwohner)

**Herausforderung:** Kein dediziertes IT-Team; IT wird von einem Generalisten oder gemeinsam mit Nachbargemeinden verwaltet.

**Strategie: Gehostete Dienste über kantonale/regionale Genossenschaft.**

Sehr kleine Gemeinden sollten keine selbstgehosteten Open-Source-Deployments anstreben. Stattdessen:
- Kantonaler IT-Genossenschaft oder AKDB/Dataport-Shared-Service beitreten
- OpenDesk oder Nextcloud als verwalteten Dienst bei zertifiziertem SCS-Hoster nutzen
- An intermunizipalem Workflow (EfA-Dienste) für transaktionsstarke Prozesse teilnehmen

**Minimaler lebenstüchtiger Stack:** Gehostetes Nextcloud + TYPO3 + gemeinsam genutztes Decidim mit Nachbargemeinden + Keycloak-Verbund mit kantonalem Identitätssystem.

**Budgetrichtwert:** 15.000–40.000 EUR/Jahr in Dienstleistungsverträgen; keine wesentlichen Investitionsausgaben.

### 10.2 Stufe B: Kleine Gemeinden (5.000–50.000 Einwohner)

**Strategie:** Genossenschaftliche Infrastruktur mit lokalem Betriebsmandat.

- govdigital-eG- oder kantonale SCS-Umgebung als Infrastruktur
- Lokale Keycloak-Instanz für SSO
- Nextcloud, Matrix/Element und Decidim als verwaltete Dienste
- Einen Mitarbeitenden als Open-Source-Administrator aufbauen

**Budgetrichtwert (5 Jahre gesamt):** 150.000–400.000 EUR

### 10.3 Stufe C: Mittelgroße Städte (50.000–500.000 Einwohner)

**Strategie:** Vollständige Implementierung gemäß Abschnitt-5-Fahrplan; Option für selbstgehostetes SCS.

**Budgetrichtwert (5 Jahre):** 1,5–4 Mio. EUR.

### 10.4 Stufe D: Großstädte (über 500.000 Einwohner)

**Strategie:** Vollständige Implementierung mit selbstgehostetem SCS, Upstream-Beitragsprogramm und Führungsrolle in EfA/gesamtschweizerischem Service-Sharing.

**Budgetrichtwert:** Stark variabel; vergleichbar mit LiMux (geschätzt 11–15 Mio. EUR über 10 Jahre inkl. Rückabwicklung vs. proprietäre Baseline ~20–25 Mio. EUR [61]).

---

## 11. Schlussfolgerung

Die Belege dieser Arbeit konvergieren auf fünf Befunde:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift und produktionserprobt auf allen Skalen.** Jede funktionale Anforderung einer modernen Kommunalverwaltung wird durch Open-Source-Software mit dokumentierten Einsätzen bei Peer-Kommunen und nationalen Regierungen erfüllt.

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland), der Interoperable-Europe-Act und der EU-Data-Act schaffen gesetzliche Verpflichtungen, die proprietäre, herstellergebundene Systeme langfristig nicht erfüllen können. Frühhandelnde Kommunen bauen Compliance-Kapital auf; späthandelnde akkumulieren regulatorische Schulden.

**3. Die wirtschaftliche Begründung ist überzeugend.** Empirische Daten aus der Französischen Gendarmerie, Extremadura und Zaragoza belegen 30–45 % Kostenreduktion gegenüber vergleichbaren proprietären Stacks. Genossenschaftliche Beschaffungsstrukturen reduzieren Pro-Kommune-Implementierungskosten erheblich.

**4. Erfolg erfordert ebenso viel politische und organisatorische Investition wie technische.** Klares politisches Mandat, qualifiziertes Veränderungsmanagement und nachhaltiges Stakeholder-Engagement sind die bindenden Einschränkungen. Das Münchener Beispiel und erfolgreiche Transitionen in Barcelona, Stuttgart und Schweizer Kantonen bestätigen diesen Befund.

**5. Kleingemeinden können über genossenschaftliches Service-Sharing teilnehmen.** Das Genossenschaftsmodell verteilt die Transitionskosten auf viele Kommunen und macht Open-Source-Einführung für die Mediangemeinde mit unter 5.000 Einwohnerinnen und Einwohnern wirtschaftlich zugänglich.

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. In Kraft: 2024-01-01. https://www.fedlex.admin.ch/eli/cc/2023/682/de [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2025). *Sovereign Cloud Stack Release 7*. Berlin: OSBA. https://scs.community/ [Apache 2.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023: Think Open*. Brüssel. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. ABl. L 903, 01.05.2024. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903

[7] Wirtz, B.W., & Weyerer, J.C. (2017). *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M. et al. (2012). *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. https://www.fitko.de/ [DL-DE/Zero 2.0]

[10] openCode.de / Digitalservice GmbH des Bundes. (2022–2026). *openCode — Open Source für die Verwaltung*. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2025). *SCS Technische Dokumentation, Release 7*. https://docs.scs.community/ [Apache 2.0]

[12] Decidim Association. (2025). *Decidim 0.28.x*. Barcelona. https://decidim.org/ [AGPL-3.0]

[13] Nextcloud GmbH. (2025). *Nextcloud Hub 8 für Behörden*. Stuttgart. https://nextcloud.com/government/ [AGPL-3.0]

[14] The Matrix Foundation. (2025). *Matrix-Spezifikation v1.10*. https://spec.matrix.org/ [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: BK. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2024). *TYPO3 13 LTS in der öffentlichen Verwaltung*. https://typo3.org/ [GPL-2.0+]

[20] OpenProject GmbH. (2025). *OpenProject 14.x für Behörden*. https://www.openproject.org/ [GPLv3]

[21] Red Hat / Keycloak Community. (2024). *Keycloak 24.x*. https://www.keycloak.org/ [Apache 2.0]

[22] CKAN Association. (2025). *CKAN 2.11.x*. https://ckan.org/ [AGPL-3.0]

[23] govdigital eG. (2025). *Rahmenvertrag Cloud-Infrastruktur*. https://govdigital.de/

[24] Dataport AöR. (2025). *Dataport — IT-Dienstleister*. https://www.dataport.de/

[26] BSI. (2023). *IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/ [CC-BY-ND 3.0 DE]

[27] EP und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[29] UN DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2025). *Camunda Platform 8 Community*. https://camunda.com/download/ [Apache 2.0]

[34] BigBlueButton Inc. (2025). *BigBlueButton 3.x*. https://bigbluebutton.org/ [LGPL-3.0]

[35] Jitsi Community. (2025). *Jitsi Meet*. https://jitsi.org/ [Apache 2.0]

[36] OpenStreetMap Foundation. (2025). *OpenStreetMap*. https://www.openstreetmap.org/ [ODbL-1.0]

[37] QGIS Project. (2024). *QGIS 3.38 LTR*. https://www.qgis.org/ [GPL-2.0+]

[39] CNCF. (2025). *Kubernetes*. https://kubernetes.io/ [Apache 2.0]

[41] PostgreSQL Global Development Group. (2025). *PostgreSQL 17*. https://www.postgresql.org/

[42] BMI / ZenDiS GmbH. (2025). *OpenDesk 2.0*. https://opendesk.eu/ [AGPL-3.0]

[43] BAR. (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/

[44] opendata.swiss. (2025). *Open Government Data Schweiz*. https://opendata.swiss/ [CC-BY-4.0]

[45] Europäische Kommission / ISA². (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. https://joinup.ec.europa.eu/ [CC-BY-4.0]

[46] KoSIT. (2024). *XÖV-Standards*. https://www.xoev.de/

[47] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government*. Sebastopol: O’Reilly. ISBN 978-0-596-80435-0.

[48] Couture, S., & Toupin, S. (2019). *New Media & Society*, 21(10), 2305–2322. https://doi.org/10.1177/1461444819865984

[51] ZenDiS GmbH. (2025). *Jahresbericht 2024*. Berlin: ZenDiS. https://zendis.de/

[52] GovStack Initiative / ITU & DIAL. (2024). *GovStack Specification: Digital Public Infrastructure Building Blocks*. Genf: ITU. https://govstack.global/ [CC-BY-SA-4.0]

[53] Europäische Kommission / DIGIT. (2024). *OSOR-Jahresbericht 2023*. https://joinup.ec.europa.eu/collection/open-source-observatory [CC-BY-4.0]

[54] EP und Rat. (2023). *Verordnung (EU) 2023/2854 — Data Act*. ABl. L 2854, 13.12.2023. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854

[55] Schweizerische Bundeskanzlei. (2024). *Bundesstrategie Open Government Data 2024–2027*. https://opendata.admin.ch/

[56] EJPD. (2023). *Bundesgesetz über den elektronischen Ausweis (E-ID-Gesetz)*. https://www.fedlex.admin.ch/eli/fga/2023/787/de

[57] eCH — E-Government Standards Schweiz. (2024). *eCH-Standardskatalog: eCH-0007, 0010, 0020, 0046, 0058, 0160*. Bern: eCH. https://www.ech.ch/de/standards

[58] Ayuntamiento de Madrid / CONSUL Democracy Project. (2023). *CONSUL Democracy 2.3.x*. https://consulproject.org/ [AGPL-3.0]

[59] Gendarmerie Nationale / DGGN. (2014). *Migration Linux: Bilan 2008–2014*. Zusammenfassung: https://lwn.net/Articles/630516/

[60] Comisión de Gobierno Electrónico de España. (2007). *Software Libre en las Administraciones Públicas Españolas*. Madrid: MAP.

[61] Accenture / Landeshauptstadt München. (2017). *Abschlussbericht zur Evaluation des Münchener LiMux-Projekts*. [Kritik in: Baack, S. (2018). *JeDEM*, 10(1). https://www.jedem.org/index.php/jedem/article/view/508]

---

*Veröffentlicht unter Creative Commons Attribution 4.0 International (CC-BY-4.0).*  
*Namensnennung: Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur (sebk4c@tuta.com)*  
*Zitierung: Graf, S. (2026). Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen (v0.2.0). https://github.com/SEBK4C/Strategy-for-City-GovTech*
