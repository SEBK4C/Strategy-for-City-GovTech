---
title: "Von Anfang an souverän: Eine aktuelle Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
date: "2026-06-20"
language: "de"
source-of-truth: false
translation-of: "../en/sovereign-by-design-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
previous-version: "0.1.0"
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
  - Bürgertechnologie
---

# Von Anfang an souverän: Eine aktuelle Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Vorgängerversion:** [v0.1.0](sovereign-by-design-v0.1.0.de.md)  
**Datum:** 2026-06-20  
**Sprachen:** [English (Quelle)](../en/sovereign-by-design-v0.2.0.md) · Deutsch  
**SPDX-Lizenzkennung:** CC-BY-4.0  

---

## Zusammenfassung

Kommunalverwaltungen sind die bürgernächste Schicht der demokratischen Verwaltung und stehen dennoch vor einer akuten strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, werden zunehmend proprietär, anbietergekoppelt und stehen im Widerspruch zu gemeinwohlorientierten Werten. Wiederkehrende Softwarelizenzkosten belasten öffentliche Haushalte, die besser für Dienstleistungen eingesetzt werden könnten; Anbieterstärke schafft strukturelle Barrieren für Transparenz und demokratische Rechenschaftspflicht; quellgeschlossene Infrastruktur verhindert die unabhängigen Sicherheitsprüfungen, die für das öffentliche Vertrauen unentbehrlich sind.

Dieses Papier präsentiert eine umfassende, zitationsvollständige Strategie für die Implementierung eines modernen Open-Source-Technologiestapels in der Kommunalverwaltung. Auf Grundlage wegweisender Rechtsvorschriften — dem Schweizer EMBAG-Gesetz (2024), Deutschlands OZG-2.0-Reform, dem Interoperabilitätsgesetz der EU (2024) und dem EU-Datenverwaltungsgesetz (2022) — sowie exemplarischer Bereitstellungen aus Barcelona, Helsinki, der deutschen OpenDesk-Initiative und mehreren Schweizer Kantonen leiten wir einen grundlagenorientierten Implementierungsfahrplan für Kommunen zwischen 5.000 und 500.000 Einwohnern ab.

Wir bewerten vierzehn Technologiekomponenten über sieben Funktionsschichten nach den Kriterien digitale Souveränität, Interoperabilität, Sicherheitslage, Gesamtbetriebskosten (TCO) und bürgerschaftliche Ausrichtung. Wir legen einen stufenweisen 36-Monats-Implementierungsfahrplan mit phasengesteuerten Checklisten, einen an das deutsche und Schweizer Vergaberecht angepassten Beschaffungsrahmen, eine TCO-Methodik und einen KPI-Rahmen zur Erfolgsmessung vor.

Wir kommen zu dem Schluss, dass: (1) Open-Source-Technologiestapel technisch ausgereift und im Produktionsbetrieb erprobt sind; (2) das regulatorische Umfeld in der Schweiz, Deutschland und der EU zunehmend offene Standards und Open-Source-Standards vorschreibt; (3) der wirtschaftliche Fall systematisch zugunsten von Open-Source ausfällt, wenn Gesamtkosten einschließlich Anbieterhänfigkeitsrisiko korrekt modelliert werden; und (4) Erfolg ebenso sehr von politischem Mandat, Change-Management und Gemeinschaftseinbindung abhängt wie von der technischen Implementierung.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale digitale Transformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Bürgertechnologie, EU-Datengesetz, GovStack, Gesamtbetriebskosten

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen; Regulierungsbehörden fordern Interoperabilität und Datenschutz; Haushaltsdruck erfordert nachhaltige, kosteneffektive Technologieinvestitionen. Dennoch sind die meisten Städte in einem Kreislauf proprietärer Anbieterhängigkeit, teurer Lizenzverträge und fragmentierter Systeme gefangen [1, 29].

Die Folgen sind gut dokumentiert: Anbieterbindung erhöht Wechselkosten [4]; proprietäre Formate behindern agenturübergreifenden Datenaustausch [45]; quellgeschlossene Infrastruktur verhindert Sicherheitsprüfungen [26]; Lizenzgebühren belasten Haushalte, die sonst für Dienstleistungen eingesetzt werden könnten [3, 5].

Ein anderer Weg ist nachgewiesen:

- Die Schweizer **EMBAG**-Gesetzgebung verpflichtet zur Open-Source-Veröffentlichung öffentlich finanzierter Software [1].
- Die deutsche **OpenDesk**-Initiative belegt, dass eine vollständige Open-Source-Arbeitsplatzsuite im großen Maßstab einsetzbar ist [42].
- Der **Sovereign Cloud Stack** (SCS) bietet eine vollständig prüfbare, selbst hostbare Cloud-Infrastruktur [3].
- Die **"Public Money? Public Code!"**-Kampagne zählt über 200 Befürworterorganisationen in 30 Ländern [4].
- **Schleswig-Holstein** kündigte 2021 die Migration von 25.000 Arbeitsplätzen auf LibreOffice an — die größte derartige Migration in einem deutschen Bundesland [47].
- Das **Interoperabilitätsgesetz der EU** (2024) und das **Datenverwaltungsgesetz** (2022) schaffen verbindliche Verpflichtungen [6, 48].

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet Städte und lokale Behörden, einschließlich Gemeinden, Kommunen, Städte und entsprechende Strukturen in Schweizer Kantonen. Die Strategie skaliert von kleinen Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (500.000+).

*Open-Source-Technologiestapel* bezeichnet Software unter OSI-genehmigten Lizenzen auf kontrollierbarer Infrastruktur.

*Digitale Souveränität* ist die Fähigkeit, unabhängige Entscheidungen über die digitale Infrastruktur zu treffen, einschließlich des Rechts auf Inspektion, Änderung, Prüfung und Migration ohne Einzelanbieter-Abhängigkeit [3].

*Gesamtbetriebskosten (TCO)* umfassen alle Lebenszykluskosten: Lizenzen, Implementierung, Hosting, Wartung, Schulung, Support und Ausstiegskosten einschließlich risikoadjustiertem Anbieterbindungswert.

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunaltechnologiestapel 2026 aus?
2. Welche Lehren sind aus der Schweizer, deutschen und europäischen Souveränitätsgemeinschaft zu ziehen?
3. Was ist der optimale stufenweise Umsetzungspfad für eine Stadt mit 50.000–500.000 Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden?
5. Welche quantitativen Metriken erfassen den Fortschritt in Richtung digitaler Souveränität am besten?

---

## 2. Methodik

**Systematische Literaturrecherche** peer-reviewter Veröffentlichungen und politischer Dokumente 2010–2026.

**Vergleichende Politikanalyse** der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027, E-ID-Gesetz 2023), Deutschlands (OZG 2017/2024, Schleswig-Holstein) und der EU (Interoperabilitätsgesetz 2024, Datenverwaltungsgesetz 2022).

**Technologiestapel-Bewertung** anhand einer Bewertungsmatrix (7 Kriterien, 1–5 Punkte, Maximum 35).

**Stakeholder-Analyse** nach dem Power-Interest-Grid.

**Fallstudienanalyse**: Barcelona, deutschen Bundesbehörden (OpenDesk), Schleswig-Holstein, Helsinki, Schweizer Bundesverwaltung.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die Literatur hat sich durch vier Phasen entwickelt [30]: Erste Generation (1995–2005) digitalisierte bestehende Prozesse [29]. Zweite Generation (2005–2012) betonte Online-Dienste [7]. Dritte Generation (2012–2020) führte Open Data und Partizipationsplattformen ein [8]. Vierte Generation (2020–heute) ist durch Plattform-Government, digitale Identitätsinfrastruktur und die Souveränitätswende geprägt [45].

Wirtz und Weyerys Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Dienstqualität, Bürgerorientierung und Transparenz [7]. Die GovStack-Initiative (ITU/DIAL) operationalisiert digitales Government durch modulare, interoperable „Bausteine“ [50].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Digitale Souveränität ist vom akademischen Konzept zum politischen Imperativ geworden [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte „Teilen und Wiederverwenden“ als Kernprinzip [5]. Das Interoperabilitätsgesetz 2024 schafft verbindliche Verpflichtungen [6].

Der Sovereign Cloud Stack (SCS), vom BMWK mitfinanziert, bietet eine vollständig offene Cloud-Plattform (OpenStack + Kubernetes + Ceph) [3, 11]. Das EMBAG-Gesetz der Schweiz, seit 1. Januar 2024 in Kraft, verpflichtet zur Open-Source-Veröffentlichung aller öffentlich finanzierten Bundessoftware [1].

### 3.3 Das deutsche OZG-Ökosystem

Das OZG (2017/2024) verpflichtet alle deutschen Verwaltungen, Dienste online anzubieten [2]. OZG 2.0 führt das „Once Only“-Prinzip, den EfA-Ansatz, BundID und FITKO-Koordination ein [9, 10].

**Schleswig-Holstein** (2021): Systematische Migration von 25.000 Arbeitsplätzen auf LibreOffice, Nextcloud und Thunderbird — ambitionierteste Open-Source-Verpflichtung auf Landesebene in Deutschland [47].

**ZenDiS GmbH** (gegr. 2022) koordiniert OpenDesk und das öffentliche Open-Source-Portfolio. Der Jahresbericht 2023 dokumentiert OpenDesk-Bereitstellung für 10.000+ Bundesbeamte [49].

openCode.de bietet ein zentrales Repository für staatliche Open-Source-Software [10].

### 3.4 Schweizer Kantonale und Bundesdigitaldienste

**eCH-Standards** definieren Datenformate und Schnittstellen für die Schweizer öffentliche Verwaltung auf allen Ebenen — das Schweizer Äquivalent zu XÖV [51]. Wichtige Standards: eCH-0010 (Adresse), eCH-0044 (Personen), eCH-0261 (Cloud für Government).

**Schweizer eID** (E-ID-Gesetz 2023): Nach der Volksabstimmung 2021 wurde ein neues Gesetz verabschiedet, das eine staatlich ausgestellte, datenschutzfreundliche digitale Identität etabliert [52].

**opendata.swiss** — CKAN-basiertes nationales Open-Data-Portal [44]. **GEVER** — standardisiertes Aktenverwaltungssystem [43].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016): 400+ Bereitstellungen in 40 Ländern; Barcelona, Helsinki, Kanton Schaffhausen, New York [12]. Barcelonas 2016er Beteiligungshaushalt engagierte 70.000+ Teilnehmende [54].

**CONSUL Democracy** (Madrid, 2015): Alternative mit Schwerpunkt auf direktdemokratischen Mechanismen [53].

**Matrix/Element**: Deutschen BundesMessenger und französischer Tchap basieren auf Matrix [14].

**Nextcloud** (Stuttgart): Schweizer Bundesverwaltung (~40.000 Beamte), tausende Deutschen Kommunen [13].

**OpenDesk** (2023), verwaltet von ZenDiS GmbH: erste staatlich kuratierte Open-Source-Arbeitsplatzsuite im großen Maßstab [42, 49].

### 3.6 EU-Datenverwaltungsgesetz und Datengesetz

Das **Datenverwaltungsgesetz (DGA)** (Verordnung (EU) 2022/868) verpflichtet öffentliche Stellen, Daten zu nicht-exklusiven Bedingungen bereitzustellen [48].

Das **Datengesetz** (Verordnung (EU) 2023/2854) gewährt Regierungen Notfallzugang zu privatwirtschaftlichen Daten und stärkt Portabilitätsrechte [55].

### 3.7 GovStack und der Bausteinansatz

Die **GovStack**-Initiative (ITU/DIAL, 2021) bietet einen internationalen Rahmen für E-Government durch modulare Bausteine: Identität, Zahlungen, Registrierung, Messaging, Workflows [50]. Die Bausteinspezifikationen stimmen mit EU-Interoperabilitätsanforderungen überein.

### 3.8 Fallstudien

**Barcelona:** Digitaler Stadtplan 2016–2023 mit 70-%-Open-Source-Ausgabenziel. Decidim entwickelt und unter AGPL-3.0 veröffentlicht; 70.000+ Teilnehmende beim ersten Beteiligungshaushalt [54].

**Schleswig-Holstein:** Migration von 25.000 Arbeitsplätzen auf LibreOffice, Nextcloud, Thunderbird, stufenweise 2023–2026 [47].

**Helsinki:** 1.200+ offene Datensätze unter CC-BY-4.0 [56]; Decidim-Bereitstellung; Open-Source-First-Beschaffungspolitik.

**Schweizer Bundesverwaltung:** ~40.000 Bundesbeamte auf Nextcloud, integriert mit Schweizer eID und GEVER [13].

### 3.9 Lücken in der Literatur

1. **TCO-Vergleichsstudien** — meist anbieterbeeinflusst und methodologisch inkonsistent.
2. **Longitudinale Daten** abgeschlossener Open-Source-Transitionen sind begrenzt.
3. **Perspektiven kleiner Gemeinden** sind unterrepräsentiert.
4. **User-Experience-Forschung** zum Vergleich der Bürgerzufriedenheit fehlt fast vollständig.

---

## 4. Technologiestapel-Analyse

### 4.1 Digitale Identität und Authentifizierung

**Empfohlen: Keycloak** [21]

De-facto Open-Source-IAM für die öffentliche Verwaltung. Implementiert OIDC, OAuth 2.0, SAML 2.0, FIDO2/WebAuthn. Föderiert mit BundID und Schweizer eID.

| Kriterium | Punkte | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Bereitstellungsreife | 5 | 10+ Jahre Produktionseinsatz |
| Community-Gesundheit | 5 | CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheitslage | 5 | Breit geprüft |
| TCO | 4 | Keine Lizenzkosten; Betriebskompetenz erforderlich |
| Öffentl. Sektor Einsatz | 5 | EU-Institutionen, Bundesländer, Kantone |
| **Gesamt** | **34/35** | |

### 4.2 Dokumentenmanagement und Akten

**Empfohlen: Nextcloud** + **Alfresco Community** [13]

Alfresco Community Edition bietet ISO-15489-konformes Aktenmanagement. Für Schweizer GEVER-Konformität: CMI GEVER oder Fabasoft als Frontend über Nextcloud.

| Kriterium | Punkte | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 (Nextcloud); LGPL-3.0 (Alfresco) |
| Bereitstellungsreife | 5 | 400.000+ Organisationen |
| Community-Gesundheit | 5 | Nextcloud GmbH + Community |
| Interoperabilität | 4 | WebDAV, CalDAV, CMIS |
| Sicherheitslage | 5 | ISO 27001 |
| TCO | 5 | Keine Sitzlizenzkosten |
| Öffentl. Sektor Einsatz | 5 | Schweiz, Deutschland, EU |
| **Gesamt** | **34/35** | |

### 4.3 Workflow-Automatisierung und BPM

**Empfohlen: Camunda Platform 8 Community** oder **Flowable** [33]

Camunda: BPMN-2.0-native Workflow-Engine mit XÖV/eCH-Integration. Flowable (Apache 2.0): saubere OSI-konforme Alternative.

### 4.4 Bürgerbeteiligung

**Empfohlen: Decidim** [12] · **Alternative: CONSUL Democracy** [53]

400+ Bereitstellungen weltweit; Decidim Association bietet Governance und Social Contract.

### 4.5 Kommunikation und Zusammenarbeit

| Komponente | Lizenz | Punkte | Vorteil |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | 32/35 | E2E-Verschlüsselung, Föderation |
| Jitsi Meet | Apache 2.0 | 31/35 | Browserbasiert, selbst hostbar |
| BigBlueButton | LGPL-3.0 | 30/35 | Fokus auf Ratssitzungen |
| Nextcloud Talk | AGPL-3.0 | 31/35 | Integriert mit Dateiverwaltung |

### 4.6 Open-Data-Veröffentlichung

**Empfohlen: CKAN** [22] — betreibt opendata.swiss, data.gov, data.gov.uk.

### 4.7 Geografische Informationssysteme

- **QGIS** (GPL-2.0+) — räumliche Datenbearbeitung [37]
- **GeoServer** — OGC-konforme Datenpublikation
- **OpenStreetMap** (ODbL-1.0) — kartografische Basisschicht [36]

### 4.8 Öffentliche Website und CMS

- **TYPO3** — dominierend in Schweizer und deutschen Behörden [19]
- **Drupal** — genutzt von der Europäischen Kommission

### 4.9 Cloud-Infrastruktur

**Empfohlen: Sovereign Cloud Stack (SCS)** [3, 11]

Vollständig offene Cloud (OpenStack + Kubernetes + Ceph). Zertifizierte SCS-Hoster: plusserver, OSISM, REGIO iT. govdigital eG betreibt SCS-basierte gemeinsame Cloud [23].

### 4.10 Office-Produktivitätssuite

**Empfohlen: LibreOffice** + **Collabora Online** [47]

LibreOffice implementiert ODF (ISO/IEC 26300) als natives Format. Schleswig-Holsteins 25.000-Arbeitsplatz-Migration ist der Referenzeinsatz.

| Kriterium | Punkte | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | MPL-2.0 |
| Bereitstellungsreife | 5 | 200 Mio.+ Nutzer |
| Community-Gesundheit | 5 | The Document Foundation + Collabora |
| Interoperabilität | 5 | ODF nativ; OOXML kompatibel |
| Sicherheitslage | 4 | Aktiv gepflegt |
| TCO | 5 | Keine Lizenzkosten |
| Öffentl. Sektor Einsatz | 5 | Schleswig-Holstein, Barcelona, Schweiz |
| **Gesamt** | **34/35** | |

### 4.11 Web-Analyse

**Empfohlen: Matomo** — selbst gehostet, DSGVO-konform. Die DSK hat Google Analytics für deutsche Behörden ohne gültige Einwilligung als unzulässig eingestuft [57].

### 4.12 DevOps und internes Code-Hosting

**Empfohlen: Forgejo** + **Woodpecker CI** oder **GitLab Community Edition**

### 4.13 Kommunales ERP

Für Phase 1–3: Bestehendes ERP beibehalten; offene Schnittstellen (XÖV/eCH) implementieren. ERP-Migration als Phase-4+-Initiative planen.

### 4.14 Referenzarchitektur

```
+------------------------------------------------------------------+
|                      BÜRGER-TOUCHPOINTS                          |
|       TYPO3/Drupal · Decidim · CKAN · Nextcloud                |
+------------------------------------------------------------------+
|                        DIENSTE-SCHICHT                           |
|   Camunda-Workflows · XÖV/eCH-Formulare · GeoServer · QGIS    |
+------------------------------------------------------------------+
|                    KOLLABORATIONS-SCHICHT                        |
|  Nextcloud · Matrix/Element · Jitsi · OpenProject · E-Mail     |
+------------------------------------------------------------------+
|                    PRODUKTIVITÄTS-SCHICHT                       |
|          LibreOffice · Collabora Online · Matomo                |
+------------------------------------------------------------------+
|                       IDENTITÄTS-SCHICHT                        |
|              Keycloak ↔ BundID / Schweizer eID                   |
+------------------------------------------------------------------+
|                   DEVOPS & CODE-SCHICHT                          |
|            Forgejo · Woodpecker CI · GitLab CE                  |
+------------------------------------------------------------------+
|                    INFRASTRUKTUR-SCHICHT                         |
|  Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph         |
+------------------------------------------------------------------+
```

---

## 5. Implementierungsfahrplan

Drei Städtegrößen-Referenzkategorien:
- **Klein:** 5.000–50.000 Einwohner; IT-Personal 1–5
- **Mittel:** 50.000–250.000 Einwohner; IT-Personal 5–30
- **Groß:** 250.000–500.000 Einwohner; IT-Personal 30–100+

### Phase 0: Grundlage (Monate 1–3)

**Ziel:** Governance etablieren, aktuellen Zustand bewerten, Koalition aufbauen.

**Lieferergebnisse:**
- [ ] Lenkungsausschuss Digitale Transformation eingerichtet
- [ ] Technologieinventur abgeschlossen
- [ ] Kostenbasis etabliert
- [ ] Stakeholder-Engagementplan verabschiedet
- [ ] Vergaberechtliche Überprüfung abgeschlossen
- [ ] Absichtserklärung mit kooperativem IT-Anbieter
- [ ] Datenschutz-Folgenabschätzung (DSFA) beauftragt

**Budgetrichtwerte (Phase 0):**
| Größe | Indikatives Budget |
|---|---|
| Klein | 20.000–50.000 € |
| Mittel | 50.000–150.000 € |
| Groß | 150.000–400.000 € |

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Lieferergebnisse:**
- [ ] Sovereign Cloud Stack Umgebung operativ
- [ ] Keycloak bereitgestellt und mit nationalem Identitätssystem verbunden
- [ ] Nextcloud für interne Zusammenarbeit
- [ ] Matrix/Element Messaging für alle IT-Mitarbeitenden
- [ ] Matomo bereitgestellt; Google Analytics entfernt
- [ ] LibreOffice für 20 % der Mitarbeitenden
- [ ] BSI-IT-Grundschutz / ISDS-Basisdokumentation
- [ ] Forgejo oder GitLab CE für internes Code-Hosting

**Budgetrichtwerte (Phase 1):**
| Größe | Indikatives Budget |
|---|---|
| Klein | 40.000–100.000 € |
| Mittel | 100.000–300.000 € |
| Groß | 300.000–800.000 € |

### Phase 2: Dienste und Workflows (Monate 10–18)

**Lieferergebnisse:**
- [ ] TYPO3 oder Drupal CMS migriert
- [ ] Fünf höchstvolumige Verwaltungsleistungen auf Camunda/XÖV-Stapel
- [ ] CKAN Open-Data-Portal mit ersten 20 Datensätzen
- [ ] Decidim für ersten Partizipationsprozess
- [ ] GIS-Schicht operativ
- [ ] LibreOffice für 60 % der Mitarbeitenden
- [ ] Erster Open-Source-Beitrag auf openCode.de

**Budgetrichtwerte (Phase 2):**
| Größe | Indikatives Budget |
|---|---|
| Klein | 60.000–150.000 € |
| Mittel | 150.000–400.000 € |
| Groß | 400.000–1.000.000 € |

### Phase 3: Integration und Erweiterung (Monate 16–24)

- [ ] Alle Dienste via Keycloak SSO verbunden
- [ ] 80 % der Verwaltungsleistungen digitalisiert
- [ ] LibreOffice für 100 % der Mitarbeitenden; Microsoft-Verträge nicht erneuert
- [ ] Jährlicher TCO-Bericht als Open Data

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

- [ ] Bürgerzufriedenheitsumfrage (Ziel: NPS ≥ 40)
- [ ] ≥ 3 Verbesserungen upstream beigetragen
- [ ] Open-Source-Community of Practice mit ≥ 3 Partnerkommunen

### Phase 5: Souveränität und Skalierung (Monate 28–36)

- [ ] Vollständiges Lizenzkonformitäts-Audit
- [ ] Souveräne Datenresidenz durch externe Partei geprüft
- [ ] Null kritische Einzelanbieter-Abhängigkeiten
- [ ] Replikations-Playbook als Open-Source-Dokument veröffentlicht

### 5.1 KPI-Rahmen

| Dimension | KPI | Ziel (36 Monate) |
|---|---|---|
| Digitale Souveränität | % IT-Ausgaben für Open-Source | ≥ 70 % |
| Digitale Souveränität | Kritische Einzelanbieter-Abhängigkeiten | 0 |
| Dienstqualität | % Dienste online verfügbar | ≥ 90 % |
| Dienstqualität | Bürger-NPS | ≥ 40 |
| Kosten | Jährliche IT-Lizenzkosten pro Mitarbeitendem | Reduktion ≥ 40 % |
| Transparenz | Veröffentlichte offene Datensätze | ≥ 50 |
| Beteiligung | Via Decidim eingebundene Bürger pro Jahr | ≥ 5 % der Bevölkerung |
| Community | Veröffentlichte Open-Source-Beiträge | ≥ 5 pro Jahr |
| Sicherheit | Zeit bis Patchen kritischer CVEs | ≤ 48 Stunden |
| Barrierefreiheit | WCAG-2.1-AA-Konformität | 100 % bürgernahe Dienste |

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Macht | Interesse | Engagement |
|---|---|---|---|
| Bürgermeister/in | Hoch | Hoch | Sponsorenrolle; Fortschritts-Dashboard |
| Stadtrat | Hoch | Mittel | Quartalsberichte; Überwachungsausschuss |
| IT-Team | Mittel | Hoch | Co-Design; Schulung; Community |
| Beschaffungsstelle | Mittel | Mittel | Rechtliche Briefings; Rahmenverträge |
| Mitarbeitende | Niedrig–Mittel | Hoch | UX-Tests; Change-Management |
| Bürger:innen | Niedrig | Hoch | Partizipatives Design; Transparenz |
| Zivilgesellschaft | Niedrig | Hoch | Öffentliche Roadmaps; Decidim |
| Open-Source-Gemeinschaften | Niedrig | Hoch | openCode.de; Upstream-Beiträge |
| Souveräne Technologieanbieter | Mittel | Hoch | Zertifizierte Partnerverträge |
| Datenschutzbeauftragte/r | Mittel | Hoch | Privacy-by-Design; DSFA |
| Incumbent-Anbieter | Hoch | Hoch (opposed) | Datenportabilität; Vertragsklauseln |

### 6.2 Beschaffungsrahmen

**Grundsatz 1:** Dienste beschaffen, keine Lizenzen.

**Grundsatz 2:** Kooperative Beschaffungsstrukturen nutzen — govdigital eG (Deutschland), Schweizer kantonale IT-Genossenschaften [23].

**Grundsatz 3:** "Public Money? Public Code!" — alle Vertragsentwicklungen unter OSI-Lizenz auf openCode.de [4].

**Grundsatz 4:** 5-Jahres-TCO-Modell:

| Kostenkategorie | Proprietär | Open-Source |
|---|---|---|
| Softwarelizenzen | Jährlich wiederkehrend | 0 € (Community) |
| Implementierung | Einmalig | Einmalig |
| Hosting | Jährlich | Jährlich |
| Schulung | Einmalig + jährlich | Einmalig + jährlich |
| Support | Jährliches Abonnement | Community + kommerziell |
| Ausstieg / Migration | Hoch (Vendor Lock-in) | Niedrig (offene Formate) |

**Grundsatz 5:** XÖV [46] (Deutschland), eCH [51] (Schweiz), DCAT-AP (EU) als Pflichtstandards.

**Grundsatz 6:** SCS-zertifizierte Anbieter oder govdigital-eG-Mitglieder bevorzugen [23].

### 6.3 Ausschreibungsvorlage (Mindestanforderungen)

```
1. LIZENZ: Alle Komponenten unter OSI-genehmigter Open-Source-Lizenz.

2. QUELLCODE: Entwicklungen innerhalb 30 Tagen nach Abnahme auf
   openCode.de unter OSI-Lizenz veröffentlicht.

3. DATENPORTABILITÄT: Alle Daten in dokumentierten, nicht-proprietären
   Formaten (ODF, CSV, JSON, XML, DCAT-AP) innerhalb 24 Stunden.

4. API: Dokumentierte REST- oder GraphQL-API. Keine proprietären
   Integrationsformate.

5. AUTHENTIFIZIERUNG: Keycloak/OIDC-Integration. Keine proprietären
   Identitätssilos.

6. SICHERHEIT: BSI-IT-Grundschutz (DE) / ISDS (CH).
   Penetrationstest-Bericht bei Abnahme erforderlich.

7. BARRIEREFREIHEIT: WCAG 2.1 AA (BITV 2.0 in Deutschland).

8. DATENRESIDENZ: Alle Daten in EU/EWR auf Infrastruktur, die nicht
   dem Nicht-EU-Datenzugriffsrecht unterliegt.

9. INTEROPERABILITÄT: XÖV (DE) / eCH (CH) für alle
   Datenaustauschschnittstellen.

10. AUSSTIEG: Dokumentierter Ausstiegsplan; vollständige Datenmigration
    innerhalb 90 Tagen ohne zusätzliche Kosten.
```

### 6.4 Change-Management-Rahmen

- **Executive-Sponsoring:** Bürgermeister/in oder Stadtdirektor/in als namentlicher Sponsor.
- **Digitale Transformations-Botschafter:innen:** Eine/r pro Abteilung.
- **Parallelbetrieb:** Mindestens 3 Monate für Produktivitätswerkzeuge; 6 Monate für bürgernahe Dienste.
- **Schulungsinvestitionen:** 4 Stunden pro Mitarbeitendem für LibreOffice; 8 Stunden für Nextcloud.
- **Transparenz:** Öffentliches Fortschritts-Dashboard ab Tag 1.

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|
| Politischer Rückschlag nach Wahl | Mittel | Hoch | In Satzung verankern; Parteiübergreifenden Konsens |
| Anbieter-Lobbying / FUD | Hoch | Mittel | TCO-Belege; Zivilgesellschaft einbinden |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulung; Kooperationsanbieter |
| Integrationsfehler | Mittel | Hoch | Stufenweiser Rollout; Referenzarchitektur |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollprotokoll-Backup; Parallelbetrieb |
| DSGVO-Verletzung | Niedrig | Hoch | Privacy-by-Design; DSFA |
| Scheiternde Nutzerakzeptanz | Mittel | Hoch | Change-Management; UX-Tests |
| Sicherheitsvorfall | Niedrig | Kritisch | IT-Grundschutz; Penetrationstests; SBOM |
| Kostenplanung | Mittel | Mittel | Phasengesteuertes Budget |

### 7.2 Das Münchener Warnbeispiel

Das LiMux-Projekt der Stadt München (2003–2017) wurde zurückgekehrt aufgrund von: (a) Wechsel der politischen Führung; (b) unzureichendem Change-Management; (c) Kompatibilitätsproblemen [30]. Die technische Umsetzung war erfolgreich — 14 Jahre Betrieb belegen das. Die Lehre: politisches Risikomanagement ist ebenso wichtig wie technische Planung.

### 7.3 DSGVO-Konformitätsanalyse

Alle empfohlenen Komponenten sind bei Selbsthosting standardmäßig DSGVO-konform. Hauptrisiken:

1. **Telemetrie in Software** — standardmäßig deaktivieren.
2. **Externe CDN-Abhängigkeiten** — alle Assets selbst hosten.
3. **Analytics** — Google Analytics durch DSK-Leitlinien unzulässig; Matomo verwenden [57].
4. **Auftragsverarbeitungsverträge** — nach DSGVO Art. 28 auch bei Dritthosting erforderlich.
5. **Revidiertes DSG (Schweiz)** — seit September 2023 in Kraft; selbst gehosteter Stapel standardmäßig konform.

### 7.4 Cybersicherheits-Reifegradmodell

| Kontrollbereich | Mindestanforderung |
|---|---|
| Authentifizierung | Keycloak mit MFA für alle Mitarbeitenden |
| Patch-Management | Kritische CVEs: ≤ 48 Std.; Hoch: ≤ 7 Tage |
| Netzwerk | TLS 1.3 überall |
| Daten in Ruhe | AES-256 für sensible Daten |
| Backup | 3-2-1-Regel; getestete Wiederherstellung |
| Vorfallreaktion | NIS2-konformer Plan; 24-Std.-Benachrichtigung |
| Penetrationstests | Jährlich; an jeder Phasensteuerung |
| SBOM | Für alle Open-Source-Abhängigkeiten |

### 7.5 Anbieter-Ausstiegsstrategie

1. Datenexport testen *vor* Bereitstellung.
2. 90-tägiges Datenexportfenster in proprietären Verträgen aushandeln.
3. Alle Konfigurationen dokumentieren.
4. 6 Monate Lesezugriff auf Legacy-Systeme nach Migration.

---

## 8. Schlussfolgerung

Fünf Erkenntnisse:

**1. Technische Reife.** Jede Funktionsanforderung kann durch Open-Source-Software erfüllt werden.

**2. Regulatorisches Mandat.** EMBAG, OZG 2.0, Interoperabilitätsgesetz, Datenverwaltungsgesetz und Datengesetz schaffen ein Umfeld, in dem proprietäre Systeme Rechts- und Compliance-Schulden akkumulieren.

**3. Wirtschaftlicher Fall.** Open-Source eliminiert Sitzlizenzkosten (typisch 100–300 € pro Nutzendem und Jahr). 5-Jahres-TCO fällt systematisch zugunsten von Open-Source aus.

**4. Fallstudien belegen Erfolg.** Barcelona, Helsinki, Schweizer Kantone und Schleswig-Holstein zeigen: bei politischem Mandat + technischer Kompetenz + Stakeholder-Engagement gelingt der Wandel.

**5. Governance ist die bindende Einschränkung.** Die Technologie ist bereit. Die Frage ist Governance.

### 8.1 Empfehlungen nach Akteuren

**Stadtverwaltungen:** Technologieaudit beauftragen; govdigital eG beitreten; Digital-Transformations-Botschafter/in ernennen.

**Gewählte Vertreter:innen:** Open-Source-First-Resolution verabschieden; digitale Souveränität im Stadtentwicklungsplan verankern.

**IT-Teams:** Mit Keycloak und Nextcloud beginnen; SCS-Community und openCode.de beitreten.

**Beschaffungsstellen:** Ausschreibungsvorlagen mit Mindestanforderungen aus Abschnitt 6.3 aktualisieren.

**Zivilgesellschaft:** Für öffentliche Fortschritts-Dashboards eintreten; Decidim nutzen.

**Open-Source-Gemeinschaften:** Kommunale IT-Teams über openCode.de einbinden.

---

## 9. Glossar

| Begriff | Definition |
|---|---|
| **AGPL-3.0** | GNU Affero GPL v3 — Open-Source-Lizenz mit Quelloffenlegungspflicht bei Netzwerkeinsatz |
| **BöB** | Schweizer Bundesbeschaffungsgesetz |
| **BSI IT-Grundschutz** | Deutsches Cybersicherheits-Basisrahmenwerk, verbindliche Referenz |
| **BundID** | Deutsches Bundesbürgerkonto, „Once Only“-Authentifizierungsschicht |
| **BPMN 2.0** | Business Process Model and Notation — Workflow-Automatisierungsstandard |
| **CKAN** | Comprehensive Knowledge Archive Network — Open-Data-Portalsoftware |
| **DCAT-AP** | Datenkatalog-Vokabular-Anwendungsprofil — EU-Metadatenstandard |
| **DSFA** | Datenschutz-Folgenabschätzung |
| **eCH** | Schweizer E-Government-Standardisierungsorganisation |
| **EfA** | Einer für Alle — Deutsches Modell gemeinsamer Diensteentwicklung |
| **EMBAG** | Schweizer Gesetz zur Open-Source-Veröffentlichung öffentlich finanzierter Software |
| **FITKO** | Föderale IT-Kooperation — Koordinierungsgremium für OZG |
| **GEVER** | Geschäftsverwaltung — Schweizer Aktenmanagementstandard |
| **GovStack** | ITU/DIAL-Rahmenwerk für E-Government mit interoperablen Bausteinen |
| **GWB/VgV** | Deutsches Vergaberecht |
| **ISDS** | Informationssicherheit des Bundes (Schweiz) |
| **KoSIT** | Koordinierungsstelle für IT-Standards — XÖV-Standardisierungsgremium |
| **NIS2** | EU-Netz- und Informationssicherheitsrichtlinie (2022) |
| **ODF** | Open Document Format — ISO/IEC 26300 offener Office-Dokumentenstandard |
| **OIDC** | OpenID Connect — offenes Authentifizierungsprotokoll |
| **OZG** | Onlinezugangsgesetz — Deutsches Digitalisierungsgesetz |
| **SBOM** | Software Bill of Materials — Verzeichnis von Softwarekomponenten |
| **SCS** | Sovereign Cloud Stack — vollständig offene europäische Cloud-Infrastruktur |
| **TCO** | Total Cost of Ownership — Gesamtbetriebskosten |
| **WCAG 2.1** | Web Content Accessibility Guidelines — internationaler Barrierefreiheitsstandard |
| **XÖV** | XML in der öffentlichen Verwaltung — Deutsches XML-Datenaustauschstandards |
| **ZenDiS** | Zentrum für Digitale Souveränität der öffentlichen Verwaltung |

---

## 10. Literatur

[1] Schweizerischer Bundesrat. (2023). *EMBAG*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de  
[2] BMI. (2024). *OZG 2.0*. https://www.bmi.bund.de/  
[3] OSBA. (2023). *Sovereign Cloud Stack*. https://scs.community/  
[4] FSFE. (2017). *Public Money? Public Code!* https://publiccode.eu/  
[5] Europäische Kommission. (2020). *Open-Source-Strategie 2020–2023*. https://commission.europa.eu/  
[6] Europäisches Parlament und Rat. (2024). *Interoperabilitätsgesetz*. https://eur-lex.europa.eu/  
[7] Wirtz, B. W. & Weyerer, J. C. (2017). Public Management Review, 19(9). https://doi.org/10.1080/14719037.2017.1283024  
[8] Janssen et al. (2012). Information Systems Management, 29(4). https://doi.org/10.1080/10580530.2012.716740  
[9] FITKO. (2023). *Jahresbericht 2023*. https://www.fitko.de/  
[10] openCode.de. (2022). https://opencode.de/  
[11] SCS Community. (2023). https://docs.scs.community/  
[12] Decidim Association. (2021). https://decidim.org/  
[13] Nextcloud GmbH. (2023). https://nextcloud.com/government/  
[14] Matrix Foundation. (2023). https://spec.matrix.org/  
[16] E-Government Suisse. (2023). *E-Government-Strategie Schweiz 2024–2027*. https://www.egovernment.ch/  
[19] TYPO3 Association. (2023). https://typo3.org/  
[20] OpenProject GmbH. (2023). https://www.openproject.org/  
[21] Keycloak Community. (2023). https://www.keycloak.org/  
[22] CKAN Association. (2023). https://ckan.org/  
[23] govdigital eG. (2023). https://govdigital.de/  
[24] Dataport AöR. (2023). https://www.dataport.de/  
[26] BSI. (2023). *IT-Grundschutz-Kompendium*. https://www.bsi.bund.de/  
[27] Europäisches Parlament und Rat. (2022). *NIS2*. https://eur-lex.europa.eu/  
[29] UN DESA. (2022). *E-Government Survey 2022*. https://publicadministration.un.org/  
[30] Janowski, T. (2015). Government Information Quarterly, 32(3). https://doi.org/10.1016/j.giq.2015.07.001  
[33] Camunda. (2023). https://camunda.com/  
[34] BigBlueButton Inc. (2023). https://bigbluebutton.org/  
[35] Jitsi. (2023). https://jitsi.org/  
[36] OpenStreetMap Foundation. (2023). https://www.openstreetmap.org/  
[37] QGIS Project. (2023). https://www.qgis.org/  
[39] CNCF. (2023). *Kubernetes*. https://kubernetes.io/  
[41] PostgreSQL Global Development Group. (2023). https://www.postgresql.org/  
[42] BMI / ZenDiS GmbH. (2023). *OpenDesk*. https://opendesk.eu/  
[43] Schweizerisches Bundesarchiv. (2023). *GEVER*. https://www.bar.admin.ch/  
[44] opendata.swiss. (2023). https://opendata.swiss/  
[45] Europäische Kommission. (2017). *EIF*. https://joinup.ec.europa.eu/  
[46] KoSIT. (2023). *XÖV-Standards*. https://www.xoev.de/  
[47] Land Schleswig-Holstein. (2021). *Open-Source-Migration*. https://www.schleswig-holstein.de/  
[48] Europäisches Parlament und Rat. (2022). *Datenverwaltungsgesetz*. https://eur-lex.europa.eu/  
[49] ZenDiS GmbH. (2023). *Jahresbericht 2023*. https://zendis.de/  
[50] ITU / DIAL. (2022). *GovStack*. https://www.govstack.global/  
[51] eCH. (2023). *eCH-Standards*. https://www.ech.ch/  
[52] Schweizerischer Bundesrat. (2023). *E-ID-Gesetz*. https://www.fedlex.admin.ch/  
[53] Ayuntamiento de Madrid. (2017). *CONSUL Democracy*. https://consuldemocracy.org/  
[54] Ajuntament de Barcelona. (2017). *Barcelona Digital City*. https://ajuntament.barcelona.cat/digital/  
[55] Europäisches Parlament und Rat. (2023). *Datengesetz*. https://eur-lex.europa.eu/  
[56] City of Helsinki. (2023). *Helsinki Open Data*. https://hri.fi/  
[57] Datenschutzkonferenz (DSK). (2022). *Orientierungshilfe Telemedien*. https://www.datenschutzkonferenz-online.de/  

---

## Anhang A: Regulierungsreferenztabelle

| Verordnung | Jurisdiktion | Wichtigste Verpflichtung | In Kraft |
|---|---|---|---|
| EMBAG | Schweiz (Bund) | Open-Source-Veröffentlichung öffentlich finanzierter Software | 01.01.2024 |
| E-ID-Gesetz | Schweiz (Bund) | Staatlich ausgestellte digitale Identität | 2026 (erwartet) |
| OZG 2.0 | Deutschland (Bund) | Alle Verwaltungsleistungen online | 2024 |
| Interoperabilitätsgesetz | EU | Grenzüberschreitende Interoperabilität | 01.05.2024 |
| Datenverwaltungsgesetz | EU | Nichtexklusive Datenweitergabe aus öffentlichen Stellen | 24.09.2023 |
| Datengesetz | EU | Datenportabilität; Cloud-Wechselrechte | 12.09.2025 |
| NIS2-Richtlinie | EU | Cybersicherheitspflichten für wesentliche Dienste | 27.12.2022 |
| DSGVO | EU | Datenschutz | 25.05.2018 |
| rev. DSG / nFADP | Schweiz | DSGVO-angepasster Datenschutz | 01.09.2023 |
| BITV 2.0 | Deutschland | Web-Barrierefreiheit für Behörden | 2019 |

---

*Dieses Dokument wird unter CC-BY-4.0 veröffentlicht.*  
*Zitierung: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*  
*Veröffentlicht: https://github.com/SEBK4C/Strategy-for-City-GovTech*
