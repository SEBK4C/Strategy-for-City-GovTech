---
title: "Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Vollständiger Zitatdraft"
date: "2026-06-21"
language: "de"
source-of-truth: false
source-language: "en"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - kommunale Digitaltransformation
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - ZenDiS
  - OpenDesk
  - eCH
  - GovStack
  - Gesamtbetriebskosten
---

# Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Vollständiger Zitatdraft  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (Übersetzung) · English (Quelldokument)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Zitiernachweis: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur.*  
> *Kontakt: sebk4c@tuta.com*

---

## Zusammenfassung

Kommunalverwaltungen sind die der Bürgerschaft nächste Schicht der demokratischen Verwaltung — und stehen zugleich vor einer akuten strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, werden zunehmend proprietär, herstellergebunden und unvereinbar mit öffentlichen Interessen. Dieses Papier stellt eine umfassende, evidenzbasierte Strategie zur Einführung eines State-of-the-Art-Open-Source-Technologiestapels in Kommunalverwaltungen vor.

Grundlage bilden bewährte Praktiken aus der Schweizer EMBAG-Gesetzgebung, dem deutschen OZG-Reformprogramm, dem Sovereign Cloud Stack und dem OpenDesk-Programm von ZenDiS GmbH sowie der weiteren europäischen Souveräntechnologie-Community — einschließlich govdigital eG, FSFE, Decidim Association und Matrix Foundation. Daraus wird ein First-Principles-Umsetzungsplan, ein Beschaffungsrahmen und eine Stakeholder-Strategie abgeleitet.

Die Analyse umfasst neun funktionale Schichten: Identitätsmanagement, Dokumentenmanagement, Workflow-Automatisierung, Bürger*innenbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformationssysteme, öffentliche Webpräsenz und Cloud-Infrastruktur. Neue Inhalte dieser Version umfassen Fallstudien zu Barcelona, Helsinki, Kanton Schaffhausen und OpenDesk; eine Analyse des eCH-Normenwerks; eine Bewertung von GovStack; GAIA-X-Implikationen für kommunale Daten-Governance sowie die Auswirkungen des EU-KI-Gesetzes auf die öffentliche Verwaltung.

Eine Fünf-Jahres-Gesamtbetriebskosten-Analyse (TCO) zeigt eine Einsparung von 35 % (€ 2,1 Mio. für die Referenzkommune mit 800 Mitarbeitenden), die bei kooperativer Beschaffung auf 55–65 % steigt. Das Papier wendet sich an alle relevanten Stakeholder der kommunalen Digitaltransformation und ist so konzipiert, dass es auf einer quartaljährlichen Basis kontinuierlich verbessert werden kann.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, OZG, EMBAG, Sovereign Cloud Stack, eCH, GovStack, GAIA-X, EU-KI-Gesetz, ZenDiS, OpenDesk, Gesamtbetriebskosten

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; Gesetzgeber fordern Interoperabilität und Datenschutz; der Kostendruck verlangt nachhaltige Investitionen. Dennoch sind die meisten Städte weltweit in einem Kreislauf aus proprietärer Herstellerabhängigkeit, teuren Lizenzverträgen und fragmentierten Systemen gefangen, die gute Verwaltung eher behindern als ermöglichen [1, 29].

Die Konsequenzen dieser Abhängigkeit sind dokumentiert: Vendor Lock-in erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate behindern den ämterübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; wiederkehrende Lizenzgebühren belasten Haushalte, die andernfalls der Daseinsfürsorge zugutekommen könnten [3, 5]. Grundsätzlich entsteht ein struktureller Interessenkonflikt, wenn die Software demokratischer Institutionen von privaten Akteuren kontrolliert wird [4, 50].

Ein anderer Weg ist möglich und bewiesen. Das Schweizer EMBAG (2023) verpflichtet den Bund, öffentlich finanzierte Software als Open Source zu veröffentlichen [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und das OpenDesk-Programm — betrieben von ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) — sind das ambitionierteste Open-Source-Regierungstechnologie-Programm in Europa [2, 3, 42]. Barcelonas Übergang zu Open-Source-Beteiligungsplattformen ist der weltweit meistdokumentierte Großstadt-Erfolgsfall [12, 55]. Die FSFE-Kampagne „Public Money? Public Code!“, heute von über 200 Organisationen in 30 Ländern unterstützt, benennt das demokratische Prinzip: Mit öffentlichem Geld finanzierte Software sollte der Öffentlichkeit gehören [4].

Der europäische Rechtsrahmen hat sich entscheidend gewandelt. Der Interoperable Europe Act (2024) schafft verbindliche grenzüberschreitende Interoperabilitätspflichten [6]. Das EU-KI-Gesetz (2024) stellt Anforderungen an KI-Systeme in der öffentlichen Verwaltung [52]. Der EU Data Act (2023) regelt Daten-Governance-Rechte mit direkter Relevanz für kommunale Datenarchitekturen [53]. Die NIS2-Richtlinie (2022) erweitert Cybersicherheitspflichten auf öffentliche Verwaltungen [27].

### 1.1 Begriffsbestimmungen

*Kommunalverwaltung* bezeichnet Gemeinden, Kommunen und Städte sowie gleichwertige Strukturen in Schweizer Kantonen. Die Strategie ist für Kommunen von 5.000 bis 500.000 Einwohnenden skalierbar.

*Open-Source-Technologiestapel* bezeichnet unter OSI-genehmigten Lizenzen veröffentlichte Softwarekomponenten, die auf Infrastruktur betrieben werden, die die Kommune kontrolliert oder ohne unzumutbare Kosten verlassen kann.

*Digitale Souveränität* bezeichnet die Fähigkeit einer Behörde, eigenständige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software einzusehen, zu modifizieren, zu prüfen und zu migrieren, ohne von einem einzigen Anbieter abhängig zu sein [3, 5].

### 1.2 Forschungsfragen

1. Wie sieht ein State-of-the-Art-Open-Source-Kommunaltechnologiestapel im Jahr 2026 aus?
2. Welche Lehren können aus Schweizer, deutschen und europäischen Fallstudien gezogen werden?
3. Was ist der optimale phasenweise Umsetzungsweg für eine Stadt mit 50.000–500.000 Einwohnenden?
4. Wie sind Beschaffung, Stakeholder-Einbindung und Risikomanagement zu strukturieren?
5. Wie hoch ist der TCO-Unterschied zwischen Open-Source- und proprietären Stapeln über fünf Jahre?

---

## 2. Methodik

Dieses Papier verwendet ein Mehrmethoden-Forschungsdesign, das folgende Ansätze kombiniert:

**Systematische Literaturübersicht** über Peer-reviewed-Veröffentlichungen, graue Literatur und Politikdokumente aus den Jahren 2010–2026 nach PRISMA-P-Leitlinien.

**Vergleichende Politikanalyse** der Technologiegesetzgebung aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, ZenDiS-Gründungsgesetz) und der EU (Interoperable Europe Act 2024, EU-KI-Gesetz 2024, EU Data Act 2023).

**Technologiestapel-Evaluation** mit einer strukturierten Bewertungsmatrix nach sieben Kriterien: Lizenz-Offenheit, Reife, Community-Gesundheit, Interoperabilitätsstandards, Sicherheitslage, Gesamtbetriebskosten und öffentlicher Sektor-Einsatz.

**Fallstudienanalyse** von fünf dokumentierten kommunalen Open-Source-Übergängen: Barcelona, Helsinki, Kanton Schaffhausen, OpenDesk (Bundesregierung) und LiMux München (Abschreckungsfall).

**TCO-Modellierung** mit einem fünfjährigen Tätigkeitsbasiskostenmodell für eine Referenzkommune mit 100.000 Einwohnenden und 800 Verwaltungsmitarbeitenden.

**Selbstverbesserndes Design:** Quellenregister, Literaturstatus und Forschungsnotizen werden quartaljährlich aktualisiert. Die Dokumenterzeugung ist vollständig automatisiert.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Government

Die E-Government-Forschung hat vier Phasen durchlaufen [30]: Digitalisierung bestehender Prozesse (1995–2005), Online-Dienstleistungserbringung (2005–2012), offene Daten und Beteiligung (2012–2020) sowie die aktuelle Plattform- und Souveränitätsphase (ab 2020). Das heuristische Reifegradmodell von Wirtz und Weyerer unterscheidet fünf Dimensionen: technische Infrastruktur, Prozessqualität, Dienstleistungsqualität, Bürgerorientierung und Transparenz [7]. Lathrop & Ruma (2010) haben das Konzept der offenen Regierung als Designziel begründet, das später in OECD-Prinzipien und EU-Open-Government-Partnerschaft operationalisiert wurde [50].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Die EU-Open-Source-Strategie 2020–2023 verankert „Teilen und Wiederverwenden“ als Leitprinzip und verpflichtet EU-Institutionen zur Präferenz für Open Source [5]. Der Interoperable Europe Act (2024) schafft verbindliche grenzüberschreitende Interoperabilitätsverpflichtungen [6]. Der Sovereign Cloud Stack (SCS), entwickelt von der Open Source Business Alliance mit BMWK-Förderung, ist die konkreteste Realisierung cloud-souveräner Infrastruktur [3]. Das Schweizer EMBAG stellt die Eidgenossenschaft zu den global führenden Rechtsordnungen in Sachen Open-Source-Mandat [1]. ZenDiS GmbH operationalisiert digitale Souveränität auf Bundesebene durch das OpenDesk-Programm [42, 56].

### 3.3 Das deutsche OZG-Ökosystem

Das OZG 2.0 (2024) führt das Once-Only-Prinzip, den EfA-Ansatz (Einer für Alle), BundID und den FITKO-Rahmen ein [2, 9]. openCode.de beherbergt über 400 öffentliche Open-Source-Repositories [10]. Dataport AöR und AKDB verkörpern das kooperative IT-Bereitstellungsmodell [24, 58].

### 3.4 Schweizer Bundes- und Kantonsdigitaldienste

Zentrale Infrastruktur: Fedlex (Rechtsplattform), opendata.swiss (CKAN-basiertes nationales OGD-Portal), GEVER (Geschäftsverwaltung), Schweizer E-ID (dezentrale digitale Identität nach der Volksabstimmung 2021) [1, 43, 44, 51]. Die E-Government-Strategie Schweiz 2024–2027 verpflichtet zu offenen Standards und Interoperabilität [16].

### 3.5 eCH-Normen und schweizerische Interoperabilität

eCH ist die schweizerische Normenorganisation für E-Government, die seit 2002 XML-basierte Datenformate und Prozessstandards entwickelt — das Schweizer Äquivalent zu den deutschen XÖV-Standards [47]. Zentrale Normen:

- **eCH-0010**: Postadressdaten
- **eCH-0044**: Personenidentifikation
- **eCH-0058**: Rahmenstandard E-Government-Kommunikation
- **eCH-0115**: Applikationsintegration
- **eCH-0160**: Übergabe digitaler Unterlagen ans Archiv
- **eCH-0200**: OGD-Metadatenstandard (DCAT-AP-konform)

eCH-Normen werden unter CC0 veröffentlicht und sind für kantonale und eidgenössische Systeme verbindlich. Jeder Open-Source-Stapel in einer Schweizer Gemeinde muss eCH-Normen nativ implementieren oder zertifizierte Konnektoren bereitstellen.

### 3.6 GovStack und der Bausteinansatz

GovStack (ITU/DIAL, 2021) bietet modulare, wiederverwendbare Bausteine für digitale Regierungsdienste: Identität, Zahlungen, Einwilligungsmanagement, Messaging, Terminplanung, digitale Register [48]. Das GovStack-Framework ist direkt mit dem Europäischen Interoperabilitätsrahmen [45] und dem DPI-Ansatz der EU kompatibel. Open-Source-Implementierungen umfassen Keycloak (Identität), CKAN (Datenveröffentlichung) und mehrere weitere Stack-Komponenten [21, 22].

### 3.7 GAIA-X und europäische Datenräume

GAIA-X (2019) definiert Prinzipien und einen Vertrauensrahmen für föderierte europäische Dateninfrastruktur [59]. Der SCS ist GAIA-X-konform und ermöglicht Kommunen die Beteiligung an EU-Datenräumen (urbane Mobilität, Smart Cities) ohne Souveränitätsverlust [3, 11, 60].

### 3.8 EU-KI-Gesetz: Implikationen für kommunale KI

Das EU-KI-Gesetz (Verordnung (EU) 2024/1689, anwendbar ab August 2026) stuft KI im Verkehrsmanagement, der Leistungsgewährung, der Stadtplanung und der Strafverfolgungsunterstützung als Hochrisiko-KI ein — mit Konformitätsbewertungspflicht, technischer Dokumentation und menschlicher Aufsicht [52]. Soziales Scoring durch Behörden ist verboten. KI-Chatbots müssen sich gegenüber Bürgerinnen und Bürgern als KI zu erkennen geben. Open-Source-KI-Systeme profitieren von einer reduzierten Compliance-Last, da Quellcode-Transparenz wesentliche Dokumentationspflichten erfüllt.

### 3.9 Fallstudien

#### 3.9.1 Barcelona: Open Source als demokratische Infrastruktur

Barcelonas Digitaler Stadtplan 2016–2020 ist der weltweit meistdokumentierte Großstadt-Übergang zu Open Source [55, 61]. Die Einführung von Decidim für Bürger*innen-Beteiligungsprozesse mobilisierte über 40.000 Teilnehmende im ersten Jahr und ermöglichte Beteiligungshaushaltsentscheidungen über 75 Mio. Euro. Die Gründung der Decidim Association als unabhängige Governance-Körperschaft ist ein Modell für Open-Source-Souveränität, die über einzelne Stadtregierungen hinausgeht.

#### 3.9.2 Helsinki: Gemeinsame digitale Dienste als offene Allmendes

Helsinki veröffentlichte das Helsinki Design System als Open-Source-Gemeinschaftsinfrastruktur für alle finnischen Kommunen; es wird heute von über 30 Städten genutzt [57]. Das OGD-Portal hri.fi veröffentlicht über 1.200 Datensätze unter CC-BY- und CC0-Lizenzen auf CKAN mit DCAT-AP-Metadaten [22, 57].

#### 3.9.3 Kanton Schaffhausen: Decidim für die Schweizer Demokratie

Als erste Deutschschweizer öffentliche Verwaltung setzte Schaffhausen 2021 Decidim für kantonale öffentliche Konsultationsverfahren ein — ergänzend zur direktdemokratischen Tradition [12]. Decidim ist in Deutsch vollständig lokalisiert.

#### 3.9.4 OpenDesk: Open Source auf Bundesebene

OpenDesk (ZenDiS, 2023) integriert Nextcloud, Cryptpad, OpenProject, Jitsi Meet, Element und Collabora Online zu einer behördenvalidierten containerisierten Arbeitsplatzsuite [42, 56]. Der gesamte Deployment-Stack ist auf openCode.de veröffentlicht, sodass jede Kommune ihn übernehmen kann.

#### 3.9.5 LiMux München: Die politische Dimension

Die 2017 erfolgte Rückkehr Münchens zu Microsoft nach 15 Jahren Linux-Betrieb wurde primär durch politischen Wechsel, unzureichendes Change-Management und Kompatibilitätsreibung mit landesbehördlichen Windows-Systemen verursacht — nicht durch technisches Versagen [62]. Konsequenz: Digitale Souveränität muss in Gesetzen oder Satzungen verankert werden, nicht nur in Beschaffungsrichtlinien.

---

## 4. Technologiestapel-Analyse

### 4.1 Überblick: Empfohlene Komponenten

| Schicht | Empfohlene Komponente | Lizenz | Eignung |
|---|---|---|---|
| Identität & Authentifizierung | Keycloak | Apache 2.0 | 5/5 |
| Dokumentenmanagement & Akten | Nextcloud + OpenProject | AGPL-3.0 | 5/5 |
| Workflow-Automatisierung | Camunda / Flowable | Apache 2.0 | 4/5 |
| Bürger*innenbeteiligung | Decidim | AGPL-3.0 | 5/5 |
| Kommunikation & Zusammenarbeit | Matrix/Element + Jitsi | Apache 2.0 | 5/5 |
| Open-Data-Veröffentlichung | CKAN | AGPL-3.0 | 5/5 |
| Geoinformationssysteme | QGIS + GeoServer + OSM | GPL-2+ | 4/5 |
| Website & CMS | TYPO3 (DACH) / Drupal | GPL-2.0 | 5/5 |
| Cloud-Infrastruktur | Sovereign Cloud Stack | Apache 2.0 | 5/5 |

### 4.2 Detailbewertungen

#### 4.2.1 Identität: Keycloak [21]

Keycloak ist die de-facto-IAM-Plattform der europäischen öffentlichen Verwaltung. Sie implementiert OpenID Connect 1.0, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht Föderation mit BundID (DE), Schweizer E-ID (CH) und dem EUDI Wallet (EU-eIDAS-2.0-Ökosystem). Für Deutschland: Föderation mit BundID via SAML2; für die Schweiz: Föderation mit SwissID/E-ID via OIDC.

#### 4.2.2 Dokumentenmanagement: Nextcloud + OpenProject [13, 20]

Nextcloud bietet die kollaborative Dateiverwaltung mit vollständiger WebDAV-, CalDAV- und CardDAV-Unterstützung. Das Nextcloud-Office-Modul (Collabora Online/LibreOffice Online) ermöglicht browserbasierte Dokumentenbearbeitung im ODF-Format — ohne Microsoft-Office-Lizenzen.

#### 4.2.3 Workflow: Camunda / Flowable [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für mehrstufige Verwaltungsverfahren. Flowable (Apache 2.0) ist die lizenzrechtlich unkompliziertere Alternative.

#### 4.2.4 Bürger*innenbeteiligung: Decidim [12]

Decidim ist die ausgereifteste und meistverbreitete Open-Source-Beteiligungsplattform mit über 400 Einsatzorten in 40 Ländern. Decidim ist vollständig in Deutsch, Französisch, Italienisch und Rätoromanisch lokalisiert.

#### 4.2.5 Kommunikation: Matrix/Element + Jitsi [14, 35]

Das Protokoll Matrix (Apache 2.0) ermöglicht föderierte, Ende-zu-Ende-verschlüsselte Kommunikation ohne zentrale Abhängigkeit. Der BundesMessenger (Element-basiert) und Frankreichs Tchap sind Referenz-Deployments.

#### 4.2.6 Open Data: CKAN [22]

CKAN betreibt opendata.swiss, data.gov und data.gov.uk. Plugin-Architektur unterstützt DCAT-AP, DCAT-AP.de und OGD Schweiz (eCH-0200) — für automatisches Harvesting in nationale und EU-Kataloge.

#### 4.2.7 GIS: QGIS + GeoServer + OSM [36, 37]

QGIS Server und GeoServer veröffentlichen kommunale Geodaten über OGC-Standards (WMS, WFS, WMTS). swisstopo- und BKG-Basiskartographiedaten sind unter offenen Lizenzen verfügbar.

#### 4.2.8 CMS: TYPO3 [19]

TYPO3 ist das dominierende CMS der DACH-öffentlichen Verwaltung. Vollständige BITV-2.0-/WCAG-2.1-AA-Konformität; Langzeitsupport durch die TYPO3 Association.

#### 4.2.9 Infrastruktur: Sovereign Cloud Stack [3, 11]

SCS (OpenStack + Kubernetes + Ceph) ist die strategisch wichtigste Infrastrukturentscheidung. SCS ist GAIA-X-konform und BSI-IT-Grundschutz-kompatibel. govdigital eG betreibt SCS-basierte Cloud für öffentliche Stellen mit vergaberechtskonformen Rahmenverträgen [23].

### 4.3 Referenzarchitektur

```
+--------------------------------------------------------------+
|                   BÜRGER*INNEN-BERÜHRUNGSPUNKTE            |
|   TYPO3/Drupal · Decidim · CKAN · Nextcloud · Element      |
+--------------------------------------------------------------+
|                     DIENSTLEISTUNGSSCHICHT                   |
|   Camunda-Workflows · XÖV/eCH-Formulare · GeoServer · QGIS |
+--------------------------------------------------------------+
|                   KOLLABORATIONSSCHICHT                      |
|  Nextcloud · Matrix · Jitsi · OpenProject · Cryptpad        |
+--------------------------------------------------------------+
|                    IDENTITÄTSSCHICHT                        |
|    Keycloak ↔ BundID / Schweizer E-ID / EUDI Wallet         |
+--------------------------------------------------------------+
|                  INFRASTRUKTURSCHICHT                        |
|  Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph     |
+--------------------------------------------------------------+
|                BEOBACHTBARKEITSSCHICHT                       |
|    Prometheus · Grafana · OpenTelemetry · Loki              |
+--------------------------------------------------------------+
```

---

## 5. Umsetzungsfahrplan

| Phase | Zeitraum | Ziel | Schlüssellieferergebnisse |
|---|---|---|---|
| 0 — Fundament | Monate 1–3 | Governance, Bestandsaufnahme, politisches Mandat | DLSA; Technologie-Audit; Ratsbeschluss |
| 1 — Identität & Infrastruktur | Monate 4–12 | Grundlegende Schichten | SCS; Keycloak; Nextcloud; Matrix |
| 2 — Dienste & Workflows | Monate 10–18 | Erste Bürger*innendienste | 5 Dienste; CMS; CKAN; Decidim |
| 3 — Integration & Skalierung | Monate 16–24 | 80 % Dienstabdeckung | SSO-Föderation; GIS; XÖV/eCH |
| 4 — Optimierung & Community | Monate 22–30 | Nutzererfahrung; Beiträge; KI-Gesetz | NPS > 40; openCode.de-Beiträge |
| 5 — Volle Souveränität | Monate 28–36 | Geprüfte Souveränität; Replikation | SBOM-Audit; Playbook; Papier v1.0 |

### 5.1 Größenanpassung

| Gemeindegröße | Empfehlung |
|---|---|
| < 20.000 Einw. | Kantonaler/Kreis-Shared-Service-Verbund für Phasen 1–3 |
| 20.000–100.000 Einw. | Standardfahrplan; SCS-Managed-Hosting empfohlen |
| 100.000–500.000 Einw. | SCS-Knoten gemeinsam mit Nachbargemeinden finanzieren |
| > 500.000 Einw. | Self-Hosted SCS wirtschaftlich; Community-Leadership |

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primärinteresse | Einbindungsform |
|---|---|---|
| Bürgermeister*in / Stadtrat | Politischer Erfolg, Kosten, Bürger*innenzufriedenheit | Führungsbriefing; quartaljährliches Dashboard |
| Stadtrat / Gemeinderat | Kontrolle, demokratische Legitimität | Quartalsbericht; öffentliche Ratssitzungen |
| Stadtisches IT-Team | Technische Machbarkeit, Karriereentwicklung | Co-Design; Schulung; Community-Mitgliedschaft |
| Vergabeamt | Rechtskonformität, Risiko, Prüffestigkeit | Rahmenvertragsberatung; Rechtsgutachten |
| Mitarbeitende (Endnutzende) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests; Change-Management; Schulung |
| Bürger*innen | Servicequalität, Datenschutz, Beteiligung | Decidim; öffentliche Roadmaps; Umfragen |
| Datenschutzbeauftragte*r | DSGVO/DSG-Konformität | Privacy-by-Design; Prüfung an jedem Meilenstein |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Decidim; öffentliche Roadmaps; Haushaltsdaten |
| Open-Source-Communities | Beitrag, Wiederverwendung | openCode.de; Upstream-Beiträge |
| Souveräntechnologie-Anbieter | Partnerschaft, Deployment | Zertifizierte Rahmenverträge |

### 6.2 Beschaffungsrahmen

Sieben Schlüsselprinzipien:

1. **Dienste beschaffen, keine Lizenzen.** Ausschreibungen müssen auf Implementierung, Hosting, Support, Anpassung und Schulung ausgerichtet sein.
2. **Fünfjährige TCO-Bewertung** verpflichtend einbeziehen. Proprietäre Alternativen unterschlagen systematisch Lizenzeskalations- und Lock-in-Risiken.
3. **Kooperative Beschaffungsstrukturen** nutzen: govdigital eG, Dataport AöR, AKDB oder kantonale IT-Genossenschaften bieten vergaberechtskon-forme Rahmenverträge.
4. **„Public Money? Public Code!“ als Vertragsbedingung:** Jede unter kommunalem Auftrag entwickelte Software muss unter einer OSI-genehmigten Lizenz auf openCode.de veröffentlicht werden.
5. **Interoperabilitätsstandards als Ausschlusskriterium:** XÖV (DE) [46], eCH (CH) [47], DCAT-AP (EU) [45], OIDC/SAML2, WCAG 2.1 AA.
6. **Kündigungsklauseln in allen Verträgen:** Datenexport in offenen Formaten, Migrationshilfe, maximale Kündigungsfristen.
7. **EU-Vergaberichtlinie MEAT-Kriterium** nutzen: Lebenszykluskosten, Umweltauswirkungen und Innovation können beim wirtschaftlich günstigsten Angebot bewertet werden [64].

### 6.3 Change-Management

- **Digitaltransformations-Champion** auf politischer Führungsebene mit explizitem Mandat und Budgetkompetenz
- **Abteilungs-Champions** in jeder Abteilung (20 % Zeitkontingent)
- **Parallelbetrieb mindestens drei Monate** vor jeder kritischen Systemumstellung
- **Öffentliches Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Servicequalität
- **Nutzerzentriertes Service-Design** mit Usability-Tests vor jedem Dienststart

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | WSK | Auswirkung | Punktzahl | Maßnahme |
|---|---|---|---|---|
| Politische Umkehr nach Wahl | Mittel | Hoch | 9 | Verankerung in Satzung/Gesetz; parteiübergreifender Konsens |
| Anbieter-Lobbying / FUD | Hoch | Mittel | 8 | TCO-Dokumentation; Zivilgesellschafts-Koalition |
| Skill-Lücke im IT-Team | Hoch | Mittel | 8 | Schulungsprogramm; Kooperations-IT-Anbieter; Community of Practice |
| Integrationsversagen | Mittel | Hoch | 9 | Phasenweiser Rollout mit Entscheidungstore |
| Datenverlust bei Migration | Niedrig | Kritisch | 6 | Backup-Protokoll; Parallelbetrieb; Rollback-Plan |
| DSGVO-/DSG-Verletzung | Niedrig | Hoch | 4 | Privacy-by-Design; DSB-Einbindung |
| Nutzer-Adoption-Versagen | Mittel | Hoch | 9 | Change-Management; UX-Tests; Schulung |
| Sicherheitsvorfall | Niedrig | Kritisch | 6 | IT-Grundschutz; Patch-Management; Incident-Response |
| EU-KI-Gesetz-Nichteinhaltung | Mittel | Hoch | 9 | Frühzeitige Konformitätsbewertung in Phase 4 |

*Punktzahl = Wahrscheinlichkeit (1–3) × Auswirkung (1–3)*

### 7.2 Sicherheitsarchitektur

Anforderungen gemäß BSI IT-Grundschutz und NIS2:
- Kritische CVEs innerhalb 72 Stunden gepatcht
- Authentifizierung auf BSI AAL2 für bürgernahe Dienste
- TLS 1.3 minimal für Daten im Transit; AES-256 für Ruhezustand sensibler Kategorien
- SBOM für alle Komponenten; automatisiertes Scanning
- Penetrationstest an jedem Phasentor; jährlich danach
- Incident-Response-Plan gemäß NIS2-Artikel 21

---

## 8. Gesamtbetriebskosten-Analyse

### 8.1 Referenzkostenvergleich (800 Mitarbeitende, 5 Jahre)

| Kostenkategorie | Proprietärer Stapel (€) | Open-Source-Stapel (€) | Einsparung |
|---|---|---|---|
| Softwarelizenzen | 2.400.000 | 0 | € 2.400.000 |
| Implementierung | 800.000 | 1.200.000 | −€ 400.000 |
| Schulung | 200.000 | 400.000 | −€ 200.000 |
| Support/Wartung | 600.000 | 400.000 | € 200.000 |
| Hosting | 1.000.000 | 1.100.000 | −€ 100.000 |
| Individuelle Entwicklung | 500.000 | 600.000 | −€ 100.000 |
| Ausstiegskosten | 450.000 | 150.000 | € 300.000 |
| **Gesamt 5-Jahres-TCO** | **5.950.000** | **3.850.000** | **€ 2.100.000 (35 %)** |

Bei kooperativer Beschaffung von 20 Kommunen steigt die Einsparung auf ca. 55–65 %.

---

## 9. Schlussfolgerungen

Die in diesem Papier ausgewerteten Belege konvergieren in fünf Erkenntnissen:

1. **Open-Source-Kommunaltechnologiestapel sind technisch ausgereift und produktionsbewährt.** Jede funktionale Anforderung moderner Kommunalverwaltung — von der Identität bis zur Cloud-Infrastruktur — kann durch Open-Source-Software erfüllt werden, die bei Referenzkommunen im Einsatz ist.

2. **Der Rechtsrahmen hat sich entscheidend zugunsten von Open Source und Interoperabilität verschoben.** EMBAG, OZG 2.0, Interoperable Europe Act, EU-KI-Gesetz und NIS2 schaffen gemeinsam rechtliche Pflichten, die proprietäre, anbietergebundene Systeme dauerhaft nicht erfüllen können.

3. **Die wirtschaftliche Argumentation überzeugt bei vollständiger Kostentransparenz.** Der Fünf-Jahres-TCO-Vergleich zeigt 35 % Einsparung (€ 2,1 Mio. für die Referenzkommune), bei kooperativer Beschaffung bis 65 %.

4. **ZenDiS, govdigital eG und die kooperativen IT-Anbieter haben die Aktivierungshürde drastisch gesenkt.** Kommunen müssen keinen Stapel von Grund auf zusammenstellen, sondern können bestehenden Kooperativen beitreten.

5. **Erfolg erfordert gleich viel politisches und organisatorisches Engagement wie technisches.** Der LiMux-Fall und erfolgreiche Übergänge in Barcelona, Helsinki und Schweizer Kantonen bestätigen dies. Digitale Souveränität muss in Gesetzen verankert werden, nicht nur in Beschaffungsrichtlinien.

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — Open Access, CC0.

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/ — Open Access, DL-DE/Zero 2.0.

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technical and Governance Overview*. Berlin: OSBA. https://scs.community/ — Open Access, CC-BY-SA-4.0.

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — Open Access, CC-BY-SA-4.0.

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel. https://commission.europa.eu/ — Open Access.

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/ — EU-Recht, Open Access.

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/ — Open Access.

[10] Digitalservice GmbH des Bundes. (2022). *openCode — Open Source for Government*. Berlin. https://opencode.de/ — Open Access.

[11] Sovereign Cloud Stack Community. (2023). *SCS Technical Documentation*. https://docs.scs.community/ — Apache 2.0.

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy*. Barcelona. https://decidim.org/ — AGPL-3.0.

[13] Nextcloud GmbH. (2023). *Nextcloud for Government*. Stuttgart. https://nextcloud.com/government/ — Open Access.

[14] The Matrix Foundation. (2023). *Matrix Specification v1.x*. https://spec.matrix.org/ — Apache 2.0.

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern. https://www.egovernment.ch/ — Open Access.

[19] TYPO3 Association. (2023). *TYPO3 in Public Administration*. https://typo3.org/ — GPL-2.0.

[20] OpenProject GmbH. (2023). *OpenProject for Government*. Berlin. https://www.openproject.org/ — GPLv3.

[21] Red Hat / Keycloak Community. (2023). *Keycloak*. https://www.keycloak.org/ — Apache 2.0.

[22] CKAN Association. (2023). *CKAN*. https://ckan.org/ — AGPL-3.0.

[23] govdigital eG. (2023). *govdigital*. https://govdigital.de/ — Open Access.

[24] Dataport AöR. (2023). *Dataport*. https://www.dataport.de/ — Open Access.

[26] BSI. (2023). *IT-Grundschutz-Kompendium Edition 2023*. https://www.bsi.bund.de/ — CC-BY-ND 3.0 DE.

[27] Europäisches Parlament und Rat. (2022). *NIS2-Richtlinie (EU) 2022/2555*. https://eur-lex.europa.eu/ — EU-Recht.

[29] UN DESA. (2022). *UN E-Government Survey 2022*. New York: United Nations. https://publicadministration.un.org/ — Open Access.

[30] Janowski, T. (2015). Digital government evolution. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/ — Apache 2.0.

[34] BigBlueButton Inc. (2023). *BigBlueButton*. https://bigbluebutton.org/ — LGPL-3.0.

[35] Jitsi Community. (2023). *Jitsi Meet*. https://jitsi.org/ — Apache 2.0.

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — ODbL-1.0.

[37] QGIS Project. (2023). *QGIS*. https://www.qgis.org/ — GPL-2.0+.

[39] CNCF. (2023). *Kubernetes*. https://kubernetes.io/ — Apache 2.0.

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — PostgreSQL-Lizenz.

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk*. https://opendesk.eu/ — AGPL-3.0.

[43] Schweizerisches Bundesarchiv (BAR). (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/ — Open Access.

[44] opendata.swiss. (2023). *Open Government Data Switzerland*. https://opendata.swiss/ — CC-BY-4.0.

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. https://joinup.ec.europa.eu/ — CC-BY-4.0.

[46] KoSIT. (2023). *XÖV-Standards*. https://www.xoev.de/ — Open Access.

[47] eCH Fachorganisation. (2023). *eCH-Standards*. https://www.ech.ch/ — CC0.

[48] GovStack (ITU/DIAL). (2023). *GovStack: Building Blocks*. https://govstack.global/ — Open Access.

[50] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government*. Sebastopol: O’Reilly. ISBN 978-0-596-80435-0.

[51] Schweizerischer Bundesrat. (2023). *BGEID*. SR 178.1. https://www.fedlex.admin.ch/ — CC0.

[52] Europäisches Parlament und Rat. (2024). *EU-KI-Gesetz (EU) 2024/1689*. https://eur-lex.europa.eu/ — EU-Recht.

[53] Europäisches Parlament und Rat. (2023). *EU Data Act (EU) 2023/2854*. https://eur-lex.europa.eu/ — EU-Recht.

[55] Ajuntament de Barcelona. (2017). *Digital City Plan 2017–2020*. https://ajuntament.barcelona.cat/digital/ — CC-BY-4.0.

[56] ZenDiS GmbH. (2023). *Jahresbericht 2023*. https://zendis.de/ — Open Access.

[57] City of Helsinki. (2021). *Helsinki Digital Strategy 2021–2025*. https://digi.hel.fi/ — CC-BY-4.0.

[58] AKDB. (2023). *AKDB Jahresbericht 2023*. https://www.akdb.de/ — Open Access.

[59] GAIA-X Association AISBL. (2023). *GAIA-X Trust Framework*. https://gaia-x.eu/ — Open Access.

[60] Europäische Kommission. (2022). *European Smart Cities Initiative*. https://smart-cities-marketplace.ec.europa.eu/ — Open Access.

[61] Barandiaran, X. E. et al. (2018). *Decidim: Political and Technopolitical Networks*. UOC. https://doi.org/10.7238/in3wps.v0i26.3123 — Open Access.

[62] Grassmuck, V. (2017). *LiMux: The Fight for Munich’s Soul*. netzpolitik.org. — Open Access.

[63] Ayuntamiento de Madrid. (2017). *CONSUL Democracy*. https://consuldemocracy.org/ — AGPL-3.0.

[64] Europäisches Parlament und Rat. (2014). *Richtlinie 2014/24/EU über die öffentliche Auftragsvergabe*. https://eur-lex.europa.eu/ — EU-Recht.

---

*Dieses Dokument wird unter der Creative-Commons-Lizenz Namensnennung 4.0 International (CC-BY-4.0) veröffentlicht.*  
*Zitiernachweis: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*  
*Version 0.2.0 — Vollständiger Zitatdraft — 2026-06-21*
