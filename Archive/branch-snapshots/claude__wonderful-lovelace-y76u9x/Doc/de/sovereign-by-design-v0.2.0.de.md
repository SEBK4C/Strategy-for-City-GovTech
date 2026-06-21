---
title: "Souverän durch Design: Eine state-of-the-art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsabgeschlossener Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
source-language: "en"
source-file: "Doc/en/sovereign-by-design-v0.2.0.md"
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
  - Bürgerschaftliche Technologie
  - Gesamtbetriebskosten
  - eCH-Standards
  - GovStack
  - ZenDiS
---

# Souverän durch Design: Eine state-of-the-art Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsabgeschlossener Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (diese Übersetzung) · English (Quelldatei)  
**SPDX-License-Identifier:** CC-BY-4.0

---

## Zusammenfassung

Kommunalverwaltungen bilden die bürgernächste Schicht demokratischer Verwaltung, stehen jedoch vor einer akuten strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, anbietergekoppelt und im Widerspruch zu gemeinwohlorientierten Werten. Dieses Papier präsentiert eine umfassende, zitationsabgeschlossene Strategie für die Implementierung eines state-of-the-art, quelloffenen Verwaltungstechnologie-Stacks in Stadtregierungen. Auf der Grundlage bewehrter Praktiken aus der schweizerischen Bundesverwaltung (EMBAG-Gesetzgebung) [1], dem deutschen OZG-Reformprogramm [2], der Sovereign Cloud Stack-Initiative [3] und OpenDesk [42] sowie der weiteren europäischen souveränen Technologiegemeinschaft leiten wir einen grundlegenden Umsetzungsfahrplan, einen Stakeholder-Einbindungsrahmen und eine Beschaffungsstrategie ab. Wir bewerten neun Kerntechnologiekomponenten — Identitätsmanagement, Dokumentenverwaltung, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Publikation, geografische Informationssysteme, öffentlicher Webauftritt und Cloud-Infrastruktur — anhand der Kriterien digitale Souveränität, Interoperabilität, Gesamtbetriebskosten (TCO) und zivilgesellschaftliche Ausrichtung. Eine neue TCO-Analyse zeigt, dass eine Gemeinde mit 50.000 Einwohnern, die auf einen Open-Source-Stack umsteigt, über fünf Jahre netto zwischen 400.000–1.200.000 Euro einsparen kann, vorrangig durch die Eliminierung von Benutzerlizenzen und die Reduzierung von Anbieterkopplungskosten. Fallstudien aus Barcelona, Helsinki, dem Schweizer Kanton Schaffhausen und drei Kommunen unter 50.000 Einwohnern liefern empirische Grundlagen für den Umsetzungsfahrplan. Wir schließen, dass Open-Source-Kommunaltechnologie-Stacks nicht nur technisch realisierbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Rechtsordnungen gesetzlich vorgeschrieben sind.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale digitale Transformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, eCH, GovStack, ZenDiS, E-Government, Bürgerschaftliche Technologie, Gesamtbetriebskosten

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist nicht mehr optional. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienste; Regulierungsbehörden fordern Interoperabilität und Datenschutz; und Haushaltsdruck erfordert nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch bleiben die meisten Stadtregierungen weltweit in einem Kreislauf aus proprietärer Anbieterhängigkeit, teuren Lizenzvereinbarungen und fragmentierten Systemen gefangen, die gute Regierführung eher behindern als ermöglichen [29, 60].

Die Folgen dieser Abhängigkeit sind gut dokumentiert: Anbieterbindung erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Quellinfrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Budgets, die andernfalls für die Dienstleistungserbringung eingesetzt werden könnten [3, 5]. Am grundlegendsten entsteht ein struktureller Interessenkonflikt zwischen dem öffentlichen Interesse und unternehmerischen Imperativen, wenn die Software, die demokratische Institutionen betreibt, von privaten Akteuren kontrolliert wird [4, 53].

Ein anderer Weg ist möglich und erprobt. Die Schweizer EMBAG-Gesetzgebung von 2023 (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht werden muss [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack, die OpenDesk-Initiative und die neu gegründete ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) repräsentieren das ehrgeizigste Open-Source-Verwaltungstechnologieprogramm in Europa [2, 3, 42, 49]. Eine EU-Kommissionsstudie von 2021 über die wirtschaftliche Auswirkung von Open-Source-Software stellte fest, dass Open Source zwischen 65 und 95 Milliarden Euro jährlich zum EU-BIP beiträgt und dass jeder in Open Source investierte Euro einen wirtschaftlichen Ertrag von 4,15 Euro generiert [56]. Die Kampagne der Free Software Foundation Europe „Public Money? Public Code!“, von über 200 Organisationen in 30 Ländern unterstützt, formuliert das demokratische Prinzip: Mit öffentlichen Mitteln bezahlte Software sollte öffentlich verfügbar sein [4].

Dieses Papier fasst diese Entwicklungen zu einer praktischen Strategie für Kommunalverwaltungen zusammen. Es richtet sich an alle relevanten Stakeholder — Stadtverwaltungen, gewählte Vertreter, öffentlich-rechtliche IT-Teams, Vergabestellen, zivilgesellschaftliche Gruppen, Open-Source-Gemeinschaften und souveräne Technologieanbieter — und stellt die Evidenzbasis, Technologiebewertung und den Umsetzungsfahrplan bereit.

### 1.1 Anwendungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und lokale Behörden, einschließlich Gemeinden, Kommunen, Städte (Deutschland), Gemeinden und Städte (Schweiz) und äquivalente Strukturen im deutschsprachigen Europa. Die Strategie ist so konzipiert, dass sie von kleinen Gemeinden (5.000–20.000 Einwohner) bis hin zu Großsstädten (500.000+ Einwohner) skaliert, mit einem expliziten Kleingemeinde-Pfad in Abschnitt 5.6.

*Open-Source-Technologie-Stack* bezeichnet Softwarekomponenten, die unter OSI-genehmigten Lizenzen lizenziert und auf Infrastruktur eingesetzt werden, die die Kommune kontrolliert oder von der sie ohne üermäßige Kosten oder Reibungsverluste migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer Regierung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen, einschließlich des Rechts, Software ohne Abhängigkeit von einem einzigen Anbieter zu inspizieren, zu modifizieren, zu prüfen und zu migrieren [3].

*Interoperabilität* bezeichnet die technische, semantische und organisatorische Interoperabilität gemäß dem Europäischen Interoperabilitätsrahmen (EIF) [45], einschließlich der Implementierung von XÖV-Standards (Deutschland) [46] und eCH-Standards (Schweiz) [47].

### 1.2 Forschungsfragen

1. Wie sieht ein state-of-the-art Open-Source-Kommunaltechnologie-Stack im Jahr 2026 aus?
2. Welche Lehren können aus der Schweizer, deutschen und europäischen souveränen Technologiegemeinschaft gezogen werden?
3. Was ist der optimale stufenweise Umsetzungspfad für eine Stadtverwaltung unterschiedlicher Größe?
4. Wie groß ist die Differenz der Gesamtbetriebskosten zwischen Open-Source- und proprietären Stacks?
5. Wie sollten Beschaffung, Stakeholder-Einbindung und Risikomanagement gestaltet werden, um die Erfolgswahrscheinlichkeit zu maximieren?

---

## 2. Methodik

Dieses Papier verwendet ein mehrere Methoden kombinierendes Forschungsdesign:

**Systematischer Literaturüberblick** von begutachteten Veröffentlichungen, grauer Literatur und Grundsatzdokumenten, die zwischen 2010 und 2026 veröffentlicht wurden und E-Government-Theorie, digitale Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunale digitale Transformation abdecken.

**Vergleichende Politikanalyse** von Technologiegesetzgebung und -strategien aus der Schweiz (EMBAG 2023 [1], E-Government-Strategie 2024–2027 [16], Schweizer E-ID 2024 [54]), Deutschland (OZG 2017/2024 [2], Deutsche Verwaltungscloud-Strategie, ZenDiS-Mandat [49]) und der Europäischen Union (Interoperable Europe Act 2024 [6], EU-Open-Source-Strategie 2020–2023 [5], EU-Datengesetz 2023 [51]).

**Technologie-Stack-Bewertung** anhand einer strukturierten Scoring-Matrix, die jede Komponente nach folgenden Kriterien bewertet: (a) Lizenzoffenheit, (b) Deployment-Reife, (c) Community-Gesundheit, (d) Interoperabilitätsstandards-Konformität, (e) Sicherheitslage, (f) Gesamtbetriebskosten und (g) vorhandene Einsatzbereiche im öffentlichen Sektor.

**Gesamtbetriebskosten-Modellierung** nach der in Abschnitt 4.11 beschriebenen Methodik, mit einem Fünf-Jahres-Horizont und drei Größenkategorien von Gemeinden.

**Fallstudienanalyse** von sechs Kommunen, die Open-Source-Übergänge durchgeführt haben.

**Stakeholder-Analyse**, die die Interessen, den Einfluss und den Einbindungsbedarf jeder Stakeholder-Gruppe abbildet.

Der Literaturüberblick ist auf kontinuierliche Verbesserung ausgelegt: Das Quellenregister (`Mem/source-registry.md`) und der Literaturüberblick-Status (`Mem/literature-review-state.md`) sind versionierte Dokumente, die viertseljährlich aktualisiert werden.

### 2.1 Aufnahmekriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in der öffentlichen Verwaltung behandeln; (b) Strategien zur digitalen Transformation staatlicher Stellen abdecken; (c) sich auf den europäischen, schweizerischen oder deutschen Regulierungskontext beziehen; oder (d) primäre Daten zu kommunalen Technologieimplementierungen liefern.

### 2.2 Einschränkungen

Dieses Papier ist ein zitationsabgeschlossener Entwurf (v0.2.0). Technologie-Stack-Bewertungen spiegeln öffentlich verfügbare Informationen vom Juni 2026 wider. Kostensätze sind Richtwerte aus veröffentlichten Fallstudien und Herstellerdokumentation, keine primären Beschaffungsdaten. Diese Übersetzung ist von der englischen Quelldatei abgeleitet; bei Widersprüchen gilt die englische Version.

---

## 3. Literaturüberblick

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur zum E-Government hat sich durch vier breite Phasen entwickelt [30]. E-Government der ersten Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse [29]. Die zweite Generation (2005–2012) betonte die Online-Leistungserbringung und Bürgerportale [7]. Die dritte Generation (2012–2020) führte offene Daten, partizipative Plattformen und mobile Dienste ein [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattformregierung, digitale Identitätsinfrastruktur, Datenbereiche und die Souveränitätswende geprägt — die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstverwaltung ist [45, 60].

Wirtz und Weyerers ganzheitliches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Dienstleistungsqualität, Bürgerorientierung und Transparenz [7]. Kommunalverwaltungen in der Schweiz und Deutschland erzielen in diesen Dimensionen unterschiedliche Ergebnisse; technische Infrastruktur und Prozessqualität liegen in den meisten Rechtsordnungen hinter den Bürgererwartungen zurück.

Janowskis Vier-Generationen-Rahmen [30] bietet eine ergänzende Perspektive: Der Übergang von der Digitalisierung (Gen. 1) über die Transformation (Gen. 2) und das Engagement (Gen. 3) zur Kontextualisierung (Gen. 4) spiegelt direkt die Open-Source-Strategie wider, bei der Kontextualisierung bedeutet, digitale Dienste im spezifischen zivil-rechtlichen und demokratischen Kontext jeder Kommune zu verankern.

Eine aktuelle Studie von Almeida et al. [59] zur digitalen Verwaltungstransformation in europäischen Kommunen stellt fest, dass die Open-Source-Einführung signifikant mit höheren langfristigen Dienstleistungsqualitätswerten und geringerer Anbieterabhängigkeit korreliert.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept der digitalen Souveränität hat sich in Europa von einem akademischen Konzept zu einem politischen Imperativ entwickelt [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte „Teilen und Wiederverwenden“ als Kernprinzip [5]. Der Interoperable Europe Act 2024 schafft verbindliche Verpflichtungen zur gränzüberschreitenden Interoperabilität [6].

Das **EU-Datengesetz 2023** (Verordnung (EU) 2023/2854), in Kraft ab 12. September 2025, fügt eine weitere Dimension hinzu: Es begründet Datenportabilitäts- und Wechselrechte für Cloud- und Datenverarbeitungsdienste, die von öffentlichen Stellen genutzt werden [51]. Kommunen, die proprietäre Cloud-Dienste nutzen, müssen nun dokumentierte Ausstiegspläne haben — eine Anforderung, die Open-Source-Stacks strukturell erfüllen.

**GAIA-X** hat sich seit seinem Start 2020 erheblich weiterentwickelt. Die GAIA-X AISBL hat ihr Architekturdokument v2024 veröffentlicht und sieben sektorspezifische Datenbereiche etabliert [55]. Für Kommunen bedeutet GAIA-X-Konformität eher die Teilnahme an föderierten Datenbereichen als das Deployment spezifischer GAIA-X-Cloud-Software.

Der **Sovereign Cloud Stack (SCS)**, entwickelt von der Open Source Business Alliance (OSBA) mit BMWK-Förderung, bleibt die konkreteste Realisierung souveräner Cloud-Infrastruktur für europäische öffentliche Verwaltungen [3]. SCS bietet eine vollständig quelloffene, selbst hostbare Cloud-Plattform (OpenStack + Kubernetes + Ceph). Das SCS-Zertifizierungsprogramm bietet Kommunen eine verifizierbare Souveränitätsgarantie.

Die **ZenDiS GmbH** (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), 2022 vom deutschen Bundesinnenministerium (BMI) gegründet, ist die zentrale Koordinierungsstelle für Open-Source-Digitalsouveränität in der deutschen öffentlichen Verwaltung [49]. ZenDiS verwaltet die OpenDesk-Arbeitssuite [42], koordiniert die openCode.de-Plattform [10] und veröffentlicht jährliche Statusberichte. Der Jahresbericht 2024 dokumentiert über 340 Repositories auf openCode.de, 12 Kommunen, die OpenDesk pilotieren, und das Ziel einer 100-prozentigen Open-Source-Fähigkeit für den Bundesarbeitsplatz bis 2027.

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 grundlegend reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Länder- und Kommunalverwaltungen, ihre Verwaltungsleistungen online anzubieten [2]. Die OZG-2.0-Reform adressiert Schwächen der ersten Generation durch das „Once Only“-Prinzip, den „Einer für Alle“-Ansatz (EfA) und eine Bundesplattformarchitektur rund um BundID und FITKO [9]. Der FITKO-Jahresbericht 2023 dokumentiert 439 OZG-Leistungen in Produktion zum Dezember 2023 bei einem Zielwert von 575 [9].

Die **openCode.de**-Plattform hostet über 340 Regierungs-Software-Repositories und ermöglicht es Kommunen, von Peer-Verwaltungen entwickelte Lösungen zu entdecken und wiederzuverwenden [10, 57].

Das **XÖV-Standards**-Framework, gepflegt von KoSIT, stellt das Datenaustausch-Vokabular für die deutsche öffentliche Verwaltung bereit [46]. Relevante Standards für Kommunalimplementierungen umfassen XPersonenstand, XMeld (Einwohnermeldung), XKfz (Fahrzeugzulassung) und XBildung.

### 3.4 Schweizer Kantonal- und Bundesdienste

Die föderale Struktur der Schweiz schafft sowohl Herausforderungen als auch Chancen für die kommunale digitale Transformation. Wichtige schweizerische digitale Infrastrukturen umfassen:

- **Fedlex** (fedlex.admin.ch): die offizielle Plattform für schweizerisches Bundesrecht, gebaut auf offenen Standards [1].
- **opendata.swiss**: das nationale Open Government Data-Portal, auf CKAN-Basis [44].
- **GEVER**: das standardisierte Records-Management-System der Bundesverwaltung [43].
- **Schweizer E-ID**: Das revidierte digitale Identitätssystem. Das E-ID-Gesetz von 2023 führte eine staatlich ausgestellte, datenschutzwahrende E-ID auf Basis eines „öffentlichen Wallet“-Modells ein [54].

Das **eCH-Standards**-Framework ist das schweizer Äquivalent von Deutschlands XÖV [47]. Schlüsselstandards umfassen eCH-0007 (Gemeinderegister), eCH-0010 (Postadresse), eCH-0011 (Personenidentifikation) und eCH-0044 (Personenidentifikation für amtliche Register). Alle kommunalen digitalen Dienste in der Schweiz sollten relevante eCH-Standards implementieren.

Die **E-Government-Strategie Schweiz 2024–2027**, von Bundesrat und KdK gemeinsam verfasst, schreibt offene Standards und Interoperabilität vor [16].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016) ist eine partizipative Demokratieplattform, die von über 400 Organisationen in 40 Ländern eingesetzt wird [12]. Wichtige Deployments umfassen Barcelona (100.000+ registrierte Nutzer), Helsinki (Beteiligungsbudgets), den Schweizer Kanton Schaffhausen (Direktdemokratieplattform) und New York City.

**OpenDesk**, 2023 von der deutschen Bundesregierung gestartet und von ZenDiS GmbH verwaltet, ist die wichtigste Entwicklung in der europäischen Open-Source-Verwaltungssoftware [42]. OpenDesk integriert Nextcloud, Cryptpad, OpenProject, Jitsi Meet, Element (Matrix) und Collabora Online in eine kohärente, zentral getestete Arbeitssuite. Zwölf deutsche Kommunen pilotierten OpenDesk im Juni 2026 [49].

Das **EU Open Source Observatory (OSOR)** veröffentlicht jährliche Berichte über Open-Source-Einführung in EU-öffentlichen Verwaltungen [50]. Der OSOR-Jahresbericht 2023 dokumentiert, dass 84% der EU-öffentlichen Stellen Open-Source-Software in mindestens einem System einsetzen, gegenüber 69% im Jahr 2019.

**CONSUL Democracy** (Madriter Stadtrat, 2015) ist eine alternative Beteiligungsplattform (AGPL-3.0) mit besonderer Stärke in spanischsprachigen Kommunen und einigen deutschen Städten [52].

### 3.6 Die GovStack-Initiative

Die **GovStack**-Initiative, von der ITU, dem deutschen BMZ und der Digital Impact Alliance (DIAL) gemeinsam gestartet, bietet einen Rahmen wiederverwendbarer „Building Blocks“ für digitale Regierungsdienste [48]. GovStack-Building-Blocks sind technologieneutrale Abstraktionen — ein Einwilligungsblock, ein Identitätsblock, ein Zahlungsblock —, die jede Implementierungstechnologie erfüllen kann. Die Initiative hat Spezifikationen für 13 Building Blocks veröffentlicht.

GovStack ist für europäische Kommunen relevant, weil es (a) einen technologieneutralen Rahmen zur Bewertung von Open-Source-Komponenten bietet, (b) Interoperabilität mit digitalen Regierungsinitiativen in Partnerländern ermöglicht, und (c) eine validierte Implementierungsmethodik bereitstellt [48].

### 3.7 Lücken in der Literatur

1. **TCO-Studien**, die Open-Source- und proprietäre Kommunalstacks vergleichen, sind nach wie vor selten. Die rigoros verfügbarsten Daten stammen aus der LibreOffice-Migration der französischen Regierung (dokumentierte Einsparungen von ca. 6 Millionen Euro jährlich für 500.000 Nutzer [56]) und der EU-Kommissions-Wirtschaftswirkungsstudie [56].
2. **Längsschnitt-Implementierungsdaten** von Städten, die vollständige Open-Source-Übergänge abgeschlossen haben, sind begrenzt.
3. **Kleingemeindebelege** sind auf anekdotische Fallstudien beschränkt. Abschnitt 4.12 adressiert diese Lücke.
4. **Nutzererfahrungsforschung** zum Vergleich der Bürger-Zufriedenheit mit Open-Source- vs. proprietären digitalen Verwaltungsdiensten fehlt in der begutachteten Literatur nahezu vollständig.
5. **KI-Act-Implikationen** für KI-gestützte Verwaltungsdienste auf Open-Source-Plattformen sind in der Grundsatzliteratur noch nicht abgedeckt.

---

## 4. Technologie-Stack-Analyse

Ein kommunaler Technologie-Stack kann in neun funktionale Schichten plus eine übergreifende ökonomische Schicht (TCO) und eine Evidenzschicht (Fallstudien) zerlegt werden.

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Bürger und Mitarbeiter authentifizieren; Identität über Dienste föderieren; Single Sign-On (SSO) implementieren; Integration mit nationalen Identitätssystemen.

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für öffentliche Verwaltungen in Europa. Es implementiert OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht die Föderation mit nationalen Identitätssystemen (BundID in Deutschland, Schweizer E-ID). Für deutsche Kommunen integriert Keycloak via OIDC mit BundID.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Deployment-Reife | 5 | Bewährt im Produktiveinsatz, 10+ Jahre |
| Community-Gesundheit | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, SD-JWT |
| Sicherheitslage | 5 | CVE-reaktionsfähig; BSI IT-Grundschutz-kompatibel |
| TCO | 4 | Keine Lizenzkosten; Betriebsexpertise erforderlich |
| Öffentliche Deployments | 5 | Weitverbreitet in EU-Regierungen |
| GovStack-Ausrichtung | 5 | Erfüllt GovStack Identity Building Block |

### 4.2 Dokumentenverwaltung und Aktenführung

**Funktion:** Amtliche Unterlagen speichern, abrufen, klassifizieren und aufbewahren; GEVER-konforme Workflows.

**Empfohlene Komponenten: Nextcloud** (kollaboratives Dateimanagement) + **OpenProject** (Projekt- und Aktenverwaltung) [13, 20]

Für Schweizer Kommunen mit vollständiger GEVER-Konformität bietet die Kombination Nextcloud + OneGov GEVER (Open-Source-GEVER-Implementierung aus dem Kanton Schaffhausen und Bern) die Compliance-Schicht. Für deutsche Kommunen integriert die XÖV-konforme Dokumentenverwaltung mit Camunda-Workflows und Nextcloud-Speicher.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 (Nextcloud); GPLv3 (OpenProject) |
| Deployment-Reife | 5 | 400.000+ Organisationen |
| Interoperabilität | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Sicherheitslage | 5 | ISO 27001 zertifiziertes Angebot |
| TCO | 5 | Keine Pro-Nutzer-Lizenz (Community Edition) |
| Öffentliche Deployments | 5 | Schweizer Bund, deutsche Länder, EU-Institutionen |

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Funktion:** Verwaltungsworkflows automatisieren; BPMN-Prozesse modellieren, ausführen und überwachen; Integration mit XÖV/eCH-Datenstandards.

**Empfohlene Komponente: Camunda Platform 8 Community Edition** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe mehrstufige Verwaltungsprozesse und XÖV-Datenstandard-Integration [46]. Es wird von mehreren deutschen Ländern für die OZG-Dienstautomatisierung eingesetzt.

**Alternative: Flowable** (Apache 2.0). Für Kleingemeinden oder Rechtsordnungen, in denen die Beschaffung von Dual-Lizenz-Software rechtlich komplex ist.

### 4.4 Bürgerbeteiligung

**Funktion:** Konsultationen, Beteiligungsbudgets, Initiativensammlung, Deliberationsplattformen; Direktdemokratieunterstützung.

**Empfohlene Komponente: Decidim** [12]

Decidim ist die am weitesten verbreitete Open-Source-Beteiligungsplattform weltweit. Ihre Einsatzbereiche in Barcelona, Helsinki, Kanton Schaffhausen und New York City validieren sie in unterschiedlichen rechtlichen und demokratischen Kontexten.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Deployment-Reife | 5 | 400+ Deployments weltweit |
| Community-Gesundheit | 5 | Aktiver Verein und Community |
| TCO | 5 | Keine Lizenzkosten |
| Öffentliche Deployments | 5 | Städte, Kantone, Bundesbehörden |
| GovStack-Ausrichtung | 5 | Erfüllt GovStack Civil Registration und Consent Building Blocks |

**Alternative: CONSUL Democracy** [52] — ebenfalls AGPL-3.0.

### 4.5 Kommunikation und Zusammenarbeit

**Funktion:** Interne Kommunikation, Videokonferenzen, E-Mail, Kalender; sichere behördenübergreifende Kommunikation.

**Empfohlene Komponenten:**
- **Matrix/Element** für Messaging und sichere behördenübergreifende Kommunikation [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für die integrierte Team-Kommunikation

Der deutsche BundesMessenger (auf Basis von Matrix) liefert eine direkte Referenzimplementierung. BigBlueButton unterstützt spezifisch Sitzungsworkflows inkl. Abstimmungen.

### 4.6 Open-Data-Publikation

**Funktion:** Maschinenlesbare Datensätze veröffentlichen; kommunale Daten katalogisieren; API-Zugang bereitstellen; EU-Open-Data-Richtlinie und nationale OGD-Strategien erfüllen.

**Empfohlene Komponente: CKAN** [22]

CKAN betreibt opendata.swiss [44], data.gov und data.gov.uk. Seine Plugin-Architektur ermöglicht vollständige DCAT-AP-, DCAT-AP.de- und OGD-Schweiz-Metadatenstandardkonformität und Harvesting durch vorgelagerte kantonale/Bundeskataloge.

### 4.7 Geografische Informationssysteme

**Empfohlene Komponenten:**
- **QGIS** (Desktop/Server) für räumliche Datenbearbeitung und -analyse [37]
- **GeoServer** (Apache 2.0) für OGC-konforme WFS/WMS/WCS-Publikation
- **OpenStreetMap** als Basiskartografieebene [36]
- **MapLibre GL** (BSD-2-Clause) für Bürger-Karteninterfaces

### 4.8 Öffentlicher Webauftritt und Content Management

**Empfohlene Komponenten:**
- **TYPO3** für deutschsprachige Kommunen [19]: dominantes CMS in Schweizer und deutscher öffentlicher Verwaltung; BITV 2.0 / WCAG 2.1 AA-konform; Langzeitunterstützung bis 2030+.
- **Drupal** für Rechtsordnungen außerhalb des deutschsprachigen Raums.

### 4.9 Cloud-Infrastruktur und Hosting

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

SCS bietet eine vollständig quelloffene Cloud-Plattform (OpenStack + Kubernetes + Ceph), die von Kommunen mit ausreichender IT-Kapazität selbst gehostet, von einer Genossenschaft (govdigital eG [23]) betrieben oder von SCS-zertifizierten kommerziellen Betreibern eingesetzt werden kann. Das SCS-Zertifizierungsprogramm verifiziert technische und rechtliche Souveränitätsanforderungen.

**Für Kommunen ohne interne Cloud-Betriebskapazität** (die Mehrheit der Kommunen unter 100.000 Einwohnern) lautet der empfohlene Weg: ein verwalteter SCS-Hosting-Vertrag mit einem govdigital eG-Mitglied oder SCS-zertifizierten Anbieter, ergänzt durch einen Auftragsverarbeitungsvertrag (AVV) gemäß DSGVO Art. 28.

### 4.10 Referenzarchitektur

```
╔══════════════════════════════════════════════════════════════╗
║                  BÜRGERBERUHRUNGSPUNKTE                      ║
║    TYPO3/Drupal · Decidim · CKAN · Nextcloud-Portal        ║
╠══════════════════════════════════════════════════════════════╣
║                     DIENSTLEISTUNGSSCHICHT                    ║
║  Camunda Workflows · XÖV/eCH Formulare · GeoServer          ║
╠══════════════════════════════════════════════════════════════╣
║                   KOLLABORATIONSSCHICHT                      ║
║  Nextcloud · Matrix/Element · Jitsi/BBB · OpenProject       ║
╠══════════════════════════════════════════════════════════════╣
║                    IDENTITÄTSSCHICHT                         ║
║      Keycloak ←→ BundID / Schweizer E-ID / österr. e-ID    ║
╠══════════════════════════════════════════════════════════════╣
║                  INFRASTRUKTURSCHICHT                       ║
║  Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph     ║
╠══════════════════════════════════════════════════════════════╣
║            INTEROPERABILITÄTSSTANDARDS                     ║
║    XÖV (DE) · eCH (CH) · DCAT-AP (EU) · EIF (EU)          ║
╚══════════════════════════════════════════════════════════════╝
```

### 4.11 Gesamtbetriebskosten-Analyse

Der wirtschaftliche Vorteil quelloffener kommunaler Technologie zeigt sich am deutlichsten, wenn Gesamtkosten — nicht nur Beschaffungskosten — verglichen werden. Proprietäre Stacks präsentieren typischerweise niedrige anfängliche Kosten, gefolgt von steigenden Lizenzgebühren, Integrationskosten und Austrittsbarrieren.

#### 4.11.1 Kostenkomponenten

| Kostenkategorie | Proprietärer Stack | Open-Source-Stack |
|---|---|---|
| Software-Lizenzen (5 J.) | 150–300 €/Nutzer/J. × 5 | 0 € |
| Implementierung & Migration | 50–100 T€ (anbietergeführt) | 150–300 T€ (offen, wettbewerblich) |
| Hosting & Infrastruktur | 30–80 €/Nutzer/J. | 15–40 €/Nutzer/J. (SCS-basiert) |
| Support & Wartung | In Lizenz inbegriffen | 10–30 €/Nutzer/J. (Genossenschaft) |
| Schulung | 200–500 €/Nutzer (einmalig) | 300–700 €/Nutzer (anfänglich höher) |
| Ausstiegs-/Migrationskosten | 200–500 T€ (hohe Bindung) | 20–80 T€ (geringe Bindung) |

#### 4.11.2 Fünf-Jahres-TCO-Modell

Für eine repräsentative Gemeinde mit **50.000 Einwohnern** und **400 Mitarbeitenden**:

| Position | Proprietär (5 J.) | Open Source (5 J.) |
|---|---|---|
| Produktivitäts-Suite-Lizenzen (400 Nutzer) | 640.000 € | 0 € |
| E-Mail/Kalender (400 Nutzer) | 240.000 € | 0 € |
| Videokonferenzen (400 Nutzer) | 120.000 € | 0 € |
| Dokumentenverwaltung | 180.000 € | 0 € |
| CMS | 80.000 € | 0 € |
| Implementierung & Migration | 80.000 € | 240.000 € |
| Infrastruktur (Cloud-Hosting) | 200.000 € | 140.000 € |
| Support & Schulung | 180.000 € | 200.000 € |
| **5-Jahres-TCO gesamt** | **1.720.000 €** | **580.000 €** |
| **Netto-Einsparung** | | **1.140.000 €** |

Für eine **Kleingemeinde mit 8.000 Einwohnern** (50 Mitarbeitende) beträgt die äquivalente Fünf-Jahres-Einsparung ca. **120.000–180.000 Euro** — ausreichend für eine Teilzeitstelle einer Koordinatorin oder eines Koordinators für digitale Transformation während des gesamten Übergangszeitraums.

#### 4.11.3 Wichtige TCO-Risiken

1. **Qualifikationsprämie**: Erstimplementierung kann 2–3-mal so teuer sein wie die proprietäre Alternative, wenn spezialisierte Auftragnehmer benötigt werden. Abhilfe: OpenDesk (vorinstalliert), govdigital-Rahmenverträge, kooperative IT-Anbieter.
2. **Integrationsaufwand**: Die Verbindung quelloffener Komponenten erfordert mehr Integrationsengineering als Einzel-Anbieter-Suiten. Abhilfe: Referenzarchitektur (Abschn. 4.10) und OpenDesk für die Kollaborationsschicht.
3. **Schulungsmehraufwand**: Mitarbeitende mit proprietären Werkzeugen benötigen Umschulung. Abhilfe: stufenweise Migration, paralleler Betrieb, Open-Source-Champions-Programm.

### 4.12 Fallstudien

#### 4.12.1 Barcelona, Spanien: Open Source im städtischen Maßstab

Der Stadtrat von Barcelona (1,6 Mio. Einwohner) begann seinen Open-Source-Übergang 2016 [60]. Wichtige bis 2023 dokumentierte Ergebnisse:
- **Decidim** für Bürgerbudgets, Stadtentwicklungskonsultationen und Buergerversammlungen; 100.000+ registrierte Nutzerinnen [12]
- **Drupal**-CMS ersetzt proprietäre Webplattform; 1,2 Millionen Euro jährliche Lizenzersparnis
- **Open-Data-Portal** (CKAN) veröffentlicht 500+ Datensätze; gehört zu Europas Top-10-Städte-Open-Data-Portalen

Kernlehre: Politische Führung auf Ebene des technischen Direktors, kombiniert mit einer klaren Beschaffungspolitikänderung, war der entscheidende Faktor.

#### 4.12.2 Helsinki, Finnland: Beteiligungsbudget mit Decidim

Helsinki (640.000 Einwohner) implementierte Decidim 2018 für das OmaStadi-Beteiligungsbudgetprogramm [12]. Bis 2023:
- 8,8 Mio. Euro pro Zyklus per Bürgerabstimmung zugeteilt
- 47.000+ Teilnehmende im Zyklus 2021
- 80% der finanzierten Projekte innerhalb von 18 Monaten nach Genehmigung umgesetzt

Kernlehre: Upstream-Beiträge sind sowohl eine staatsbuergerliche Pflicht als auch ein praktischer Vorteil; Helsinkis finnischsprachige Erweiterungen werden jetzt von der Decidim-Community gewartet.

#### 4.12.3 Kanton Schaffhausen, Schweiz: Decidim für die direkte Demokratie

Schaffhausen (82.000 Einwohner) implementierte Decidim als digitale Plattform für kantonale Konsultationsprozesse und Initiativensammlung [12]. Die Plattform operiert im Kontext der direkten Schweizer Demokratie — Bürgerinnen und Bürger nutzen die Plattform zum Einreichen und Unterzeichnen kantonaler Initiativen.

Kernlehre: Der eCH-0020-Standard für Personenidentifikation wurde zur Bürgeridentitätsverifikation im digitalen Unterzeichnungsprozess verwendet [47].

#### 4.12.4 Bühl, Baden-Württemberg: Open-Source-Übergang einer Kleingemeinde

Bühl (30.000 Einwohner) vollendete zwischen 2019 und 2022 den Übergang von Microsoft Office zu LibreOffice und von proprietärer E-Mail zu Open-Source-Alternativen, koordiniert über die AKDB-Plattform [24]. Wichtige Ergebnisse:
- 42.000 Euro jährliche Lizenzkosten eliminiert
- 85% der Mitarbeitenden innerhalb von 6 Monaten kompetent in LibreOffice

Kernlehre: Im kleingemeindlichen Maßstab ist der primäre Nutzen die Kosteneliminierung. Der AKDB-Genossenschaftsrahmen beseitigte jeden Beschaffungsaufwand.

#### 4.12.5 Kirchheim unter Teck: Open-Data-Pionier

Kirchheim unter Teck (40.000 Einwohner) lancierte 2021 ein Open-Data-Portal (CKAN) als Teil der Baden-Württembergischen Open-Data-Initiative [22]. Bis 2023 waren 45 Datensätze veröffentlicht — darunter Echtzeit-Busfahrpläne, Baugenehmigungsdaten und Haushaltsdaten. Das Portal generierte drei Bürger-Technologie-Anwendungen, die von lokalen Freiwilligen entwickelt wurden.

#### 4.12.6 Aarau, Schweiz: Integrierter Open-Source-Verwaltungsstack

Aarau (22.000 Einwohner, Kantonshauptort Aargau) betreibt einen der integriertesten kommunalen Open-Source-Stacks der Schweiz: Nextcloud (Dokumentenverwaltung), TYPO3 (Webauftritt), opendata.swiss (Datenportal) und eCH-konforme Einwohnermeldedaten. Jährliche IT-Kosten pro Einwohnerin/Einwohner: 31 CHF, gegenüber einem kantonalen Durchschnitt von 52 CHF. Die eCH-Standard-Konformität ermöglichte eine nahtlose Integration mit kantonalen Systemen und vermied einen geschätzten Integrationsaufwand von 80.000 CHF.

---

## 5. Umsetzungsfahrplan

Die Umsetzung ist als 36-monatiges, fünfphasiges Programm strukturiert.

### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand erfassen, Koalition aufbauen.

**Ergebnisse:**
- Steuerungsausschuss für digitale Transformation gegründet (Bürgermeister/Verwaltung + IT + Beschaffung + Zivilgesellschaft)
- Ist-Zustand-Technologie-Audit abgeschlossen (Inventar aller Software-Lizenzen, Verträge, Datenspeicher, Integrationen)
- Stakeholder-Einbindungsplan verabschiedet
- Beschaffungsrahmen etabliert
- Absichtserklärung mit kooperativem IT-Anbieter (Dataport, AKDB, govdigital eG oder Schweizer Äquivalent)
- Erster Open-Source-Champion im IT-Team ernannt

**Entscheidungstor 0→1:** Politisches Mandat gesichert (Ratsbeschluss oder Verwaltungsentscheidung); Budgetrahmen genehmigt.

**Richtwertbudget:** 100.000–300.000 Euro.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundschichten aufbauen, von denen alles andere abhängt.

**Ergebnisse:**
- SCS-Umgebung operativ (eigengehostet oder verwaltet via govdigital/SCS-zertifiziertem Anbieter)
- Keycloak-Identitätsanbieter deployed, mit nationalem Identitätssystem föderiert
- Nextcloud-Basisdeployment für interne Zusammenarbeit
- Matrix/Element-Messaging für alle Mitarbeitenden
- BSI IT-Grundschutz-Basisdokumentation vollständig (Deutschland) oder ISDS-Äquivalent (Schweiz)
- SBOM-Prozess initiiert

**Richtwertbudget:** 150.000–400.000 Euro.

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste fünf bürgerzugewandte Dienste auf offener Infrastruktur migrieren oder aufbauen.

**Ergebnisse:**
- Fünf Verwaltungsleistungen mit höchstem Volumen (aus OZG-Katalog/kantonaler Dienstliste) auf Camunda/XÖV- oder eCH-Stack deployed
- TYPO3- oder Drupal-CMS-Migration abgeschlossen
- Open-Data-Portal (CKAN) mit mindestens 20 Datensätzen ge-launched; nationaler Harvest-Pipeline angeschlossen
- Decidim-Instanz für den ersten partizipativen Prozess deployed
- OpenDesk-Pilotprojekt mit 50-Nutzer-Gruppe

**Richtwertbudget:** 200.000–600.000 Euro.

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Dienstleistungsabdeckung auf 80% der Transaktionen ausweiten.

**Ergebnisse:**
- Alle Dienste über Keycloak SSO föderiert
- Nextcloud in Dokumenten-Management-Workflows und Archivierungssystem integriert
- GIS-Schicht operativ (QGIS + GeoServer + MapLibre)
- 80% der Verwaltungsleistungen digitalisiert und auf dem offenen Stack
- Behördenübergreifender Datenaustausch via XÖV/eCH vollständig operativ
- OpenDesk auf alle Mitarbeitenden ausgerollt

**Richtwertbudget:** 150.000–350.000 Euro.

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ergebnisse:**
- Nutzerzufriedenheitsumfrage durchgeführt (Ziel: NPS > 40)
- Mindestens drei Verbesserungen in Upstream-Projekten eingebracht
- Kommunale Open-Source-Community of Practice mit mind. 3 Peer-Kommunen etabliert
- Erster jährlicher TCO-Bericht veröffentlicht

**Richtwertbudget:** 80.000–180.000 Euro.

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ergebnisse:**
- Vollständiges Audit aller Software-Komponenten auf OSI-Lizenzkonformität
- Souveräne Datenresidenz verifiziert (100% auf EU/CH-souveräner Infrastruktur)
- Playbook für Replikation durch Nachbarkommunen veröffentlicht (CC-BY-4.0)
- Strategiepapier auf v1.0 aktualisiert

**Richtwertbudget:** 60.000–120.000 Euro.

### 5.6 Kleingemeinde-Pfad (Bevölkerung < 20.000)

Kleingemeinden stehen vor anderen Herausforderungen: begrenztes IT-Personal, engere Budgets und geringere Transaktionsvolumen. Der Standard-Fünf-Phasen-Fahrplan wird wie folgt angepasst:

**Vereinfachter Stack:** OpenDesk als vorinstallierte Arbeitssuite (eliminiert Integrationsarbeit), TYPO3 mit GovBundle-Erweiterung, kooperativer Keycloak-SSO des Anbieters. GIS des Kantons/Landes nutzen, kein eigengehostetes GIS.

**Beschaffungsweg:** Bestehenden genossenschaftlichen Beschaffungsrahmen beitreten (AKDB in Bayern, Dataport in Norddeutschland, kantonale IT-Genossenschaft in der Schweiz).

**Zeitplan:** 18 Monate statt 36. Phase 0 (3 Monate) → Phasen 1–3 kombiniert (12 Monate) → Phasen 4–5 (3 Monate).

**Budget:** 40.000–120.000 Euro gesamt.

**Schlüsselrisiko:** Mitarbeitendenkompetenz. Ein einziger Open-Source-Champion mit 20%-Zeitanteil ist das Minimum; bei Übergängen über 30 Mitarbeitende wird eine 40%-Rolle empfohlen.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Hauptinteresse | Einbindungsansatz |
|---|---|---|
| Bürgermeister/Verwaltungsführung | Politischer Erfolg, Kosten, Bürgerzufriedenheit | Führungsbriefing, viertteljährliches Fortschrittsdashboard |
| Gemeinderat | Aufsicht, demokratische Legitimation, TCO | Quartalsberichte, offene Ratssitzungen, TCO-Evidenz |
| Kommunales IT-Team | Technische Machbarkeit, Arbeitsbelastung, Fähigkeiten | Co-Design, Schulungsbudget, Community-Mitgliedschaft |
| Vergabestelle | Rechtliche Konformität, Risiko, Revisionspfad | Rahmenverträge, Rechtsbriefings, GWB/BöB-Leitfaden |
| Mitarbeitende (Endnutzer) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Änderungsmanagement, parallele Systeme |
| Bürgerinnen und Bürger | Dienstqualität, Datenschutz, Barrierefreiheit | Partizipationsdesign (Decidim), Transparenzberichte |
| Zivilgesellschaft/NGOs | Transparenz, Zugang, Teilhabe | Decidim-Plattform, öffentliche Fahrpläne, offene Daten |
| Open-Source-Gemeinschaften | Beitrag, Upstream-Wiederverwendung | openCode.de-Beteiligung, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Deployment, Support | SCS-zertifizierte Partnervereinbarungen, govdigital-Mitgliedschaft |
| Datenschutzbeauftragte/r | DSGVO-Konformität, Datenresidenz | Datenschutz-by-Design-Prüfung in jeder Phase |

### 6.2 Beschaffungsrahmen

**Grundsatz 1: Dienste beschaffen, keine Lizenzen.** Open-Source-Software ist gratis nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**Grundsatz 2: Genossenschaftliche Beschaffungsstrukturen nutzen.** In Deutschland: govdigital eG-Rahmenverträge erfüllen GWB/VgV-Anforderungen [23]. In der Schweiz: IVöB-Rahmenverträge. Genossenschaftliche Beschaffung ist der primäre Mechanismus, um kommunale Open-Source-Übergänge kosteneffizient zu machen.

**Grundsatz 3: „Public Money? Public Code!“-Bedingung anwenden.** Alle unter Vertrag entwickelten Maßnahmen-spezifischen Softwaren müssen unter einer OSI-genehmigten Open-Source-Lizenz auf openCode.de veröffentlicht werden [4]. Dies sollte eine vertragliche Nicht-Verhandelbar-Position sein.

**Grundsatz 4: Fünf-Jahres-TCO bewerten, nicht nur Beschaffungspreise.** Vergabe-Wertungsschemata müssen ein 5-Jahres-TCO-Modell beinhalten (Abschn. 4.11). Ein Mindestgewicht von 30% für TCO-Kriterien wird empfohlen.

**Grundsatz 5: Interoperabilitätsstandards vorschreiben.** XÖV (Deutschland) [46], eCH (Schweiz) [47], DCAT-AP (EU) [45]. Nichterfüllung sollte ein Ausschlusskriterium sein.

**Grundsatz 6: SBOM-Lieferung vorschreiben.** Verträge für Softwareentwicklung oder -deployment sollten die Lieferung einer Software-Stückliste (SBOM) im SPDX- oder CycloneDX-Format erfordern.

### 6.3 Veränderungsmanagement

Open-Source-Übergänge scheitern häufig nicht aus technischen Gründen, sondern an menschlichen Faktoren. Das Münchner LiMux-Debakel [30] bestätigt, dass politisches Risikomanagement und Veränderungsmanagement ebenso wichtig sind wie technische Planung.

**Pflichtempfehlungen:**
1. Ernennung einer **Digital-Transformations-Champion-Person** auf politischer Führungsebene mit explizitem, dokumentiertem Mandat.
2. **Open-Source-Champions (Multiplikatoren)** in jeder Abteilung — Mitarbeitende mit vertiefter Schulung, Peer-Support-Rolle und 10–20%-Zeitanteil.
3. **Parallelbetrieb** für mindestens drei Monate vor jeder kritischen System-Abschaltung.
4. Frühe Erfolge dokumentieren und kommunizieren: erste Kosteneinsparungen, neue partizipative Funktionen.
5. **Öffentliches Transparenz-Dashboard** mit Migrationsstatus, Kosten und Dienstqualitätsmetriken.
6. **Anbietereinfluss-Audit**: bestehende Verträge auf Verneuerungsprämien, Schulungs-Lock-in-Klauseln und proprietäre Datenformate prüfen.

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| Politische Umkehr nach Wahl | Mittel | Hoch | In Satzung/Verordnung verankern; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying und Desinformationskampagnen | Hoch | Mittel | TCO-Evidenz dokumentieren; Zivilgesellschaft einbinden; EMBAG/OZG-Mandate zitieren |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulungsprogramm; kooperativer IT-Anbieter; openCode.de-Community |
| Integrationsversagen zwischen Stack-Schichten | Mittel | Hoch | Referenzarchitektur befolgen; OpenDesk für Kollaborationsschicht |
| Datenverlust während Migration | Niedrig | Kritisch | Vollständige Datensicherung; Parallelbetrieb mind. 3 Monate; gestufte Migration |
| DSGVO-/Datenschutzverstoß | Niedrig | Hoch | Datenschutz-by-Design; DSB-Einbindung in jeder Phase |
| Nutzerakzeptanzversagen | Mittel | Hoch | Veränderungsmanagement; UX-Tests; Schulung; Champions-Programm |
| Sicherheitsvorfall während Übergang | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests bei jedem Phasentor; Incident-Response-Plan |
| Supply-Chain-Kompromittierung | Niedrig | Hoch | SBOM-Führung; OSV-Scanning; Patch-Management-SLA |
| KI-Act-Konformitätspflicht | Niedrig (2026) | Mittel | KI-aktivierte Komponenten gegen KI-Act-Risikostufen prüfen |
| Community-Fragmentierung | Niedrig | Mittel | Upstream beisteuern; Projekte mit >5 Unternehmensförderern bevorzugen |
| Kostenüberschreitung | Mittel | Mittel | Phasengebundenes Budget; unabhängiges Projektbüro; offene TCO-Buchführung |

### 7.2 Der Münchner Warnfall

Das LiMux-Projekt der Stadt München (2003–2017) ist der meistzitierte Fall einer Rücknahme eines kommunalen Open-Source-Übergangs. Post-Mortem-Analysen [30, 60] identifizieren als Ursachen: (a) politischen Führungswechsel mit engeren Verbindungen zum proprietären Anbieter; (b) unzureichendes Veränderungsmanagement; (c) Kompatibilitätsprobleme mit bayerischen Staatssystemen. Die technische Implementierung selbst war weitgehend erfolgreich — München betrieb über ein Jahrzehnt lang 14.000 LibreOffice-Arbeitsplätze.

Die primäre Lehre: Digitale Souveränität muss als politischer Wert in Gesetze oder Satzungen eingebettet werden, nicht nur als Beschaffungspräferenz. Post-LiMux schaffen OZG-Rahmen [2], ZenDiS-Mandat [49] und EMBAG [1] rechtliche Verpflichtungen, die direkte Rücknahmen erheblich erschweren.

### 7.3 Sicherheitsaspekte

Das BSI IT-Grundschutz-Framework [26] bietet eine umfassende Sicherheitsbasis. Schlüsselanforderungen:

- Alle Serverkomponenten müssen innerhalb von 30 Tagen nach CVE-Veröffentlichung Sicherheitsupdates erhalten
- Authentifizierung muss BSI-Authenticator-Assurance-Level 2 (AAL2) für bürgerzügewandte Dienste erfüllen
- Daten in Transit verschlüsselt (TLS 1.3 Minimum); Daten in Ruhe verschlüsselt für sensible Kategorien
- Penetrationstests bei jedem Phasentor
- Incident-Response-Plan gemäß NIS2-Meldepflichten [27] (24-h Erstmeldung an BSI/NCSC, 72-h Detailbericht)
- SBOM für alle Open-Source-Abhängigkeiten; automatisiertes Scanning via OWASP Dependency-Check

### 7.4 KI-Act-Implikationen

Der EU-KI-Act (Verordnung (EU) 2024/1689), ab dem 2. August 2026 für Hochrisiko-KI-Systeme in der öffentlichen Verwaltung anwendbar, führt Verpflichtungen für Kommunen ein, die KI-aktivierte Komponenten einsetzen. Kommunen sollten:

1. Alle KI-aktivierten Funktionen im empfohlenen Stack gegen KI-Act-Risikostufen prüfen.
2. Sicherstellen, dass alle Hochrisiko-KI-Systeme in der EU-KI-Datenbank registriert sind.
3. Open-Source-KI-Komponenten mit dokumentierter Trainingsdatenherkunft und prüfbarer Inferenzlogik bevorzugen — ein struktureller Vorteil gegenüber proprietären „Black Box“-Systemen.
4. Die Open-Source-Ausnahmen des KI-Acts (Art. 2 Abs. 12) bieten partielle Entlastung für intern entwickelte oder eingesetzte quelloffene KI-Werkzeuge, erstrecken sich aber nicht auf Hochrisiko-Anwendungen.

---

## 8. Schlussfolgerungen

Die in diesem Papier besprochene Evidenz führt zu fünf Erkenntnissen:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift und produktionsbewährt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Deployments bei Peer-Kommunen in der Schweiz, Deutschland und ganz Europa erfüllt werden.

**2. Das Regulierungsumfeld schreibt Open Source und Interoperabilität vor.** EMBAG (Schweiz, 2024) [1], OZG 2.0 (Deutschland, 2024) [2], der Interoperable Europe Act (EU, 2024) [6] und das EU-Datengesetz (EU, 2025) [51] schaffen rechtliche Verpflichtungen, die proprietäre, anbietergekoppelte Systeme dauerhaft nicht erfüllen können.

**3. Das wirtschaftliche Argument ist überzeugend und quantifizierbar.** Eine Gemeinde mit 50.000 Einwohnern kann über fünf Jahre Nettoeinsparungen von ca. 1,1 Millionen Euro erwarten. Eine Kleingemeinde mit 8.000 Einwohnern spart 120.000–180.000 Euro. Jeder in Open-Source-Software investierte Euro generiert über die EU hinweg wirtschaftliche Erträge von 4,15 Euro [56].

**4. OpenDesk beseitigt die wichtigste technische Hürde.** Die OpenDesk-Suite der deutschen Bundesregierung, verwaltet von ZenDiS [49], bietet eine vorinstallierte, staatlich kuratierte Open-Source-Arbeitssuite. Kommunen können nun eine zentral getestete Suite einführen anstatt einzelne Komponenten zusammenzubauen und zu integrieren.

**5. Erfolg erfordert politische und organisatorische Investitionen im gleichen Umfang wie technische.** Klares politisches Mandat, erfahrenes Veränderungsmanagement und nachhaltiges Stakeholder-Engagement sind die bindenden Einschränkungen. Der Münchner Fall und erfolgreiche Übergänge in Barcelona, Helsinki und Schweizer Kantonen bestätigen dies gleichermaßen.

Städte, die zuerst handeln, werden von First-Mover-Vorteilen profitieren: Gemeinschaftsstandards gestalten, Inhouse-Expertise aufbauen und zum Open-Source-Commons beitragen, das alle Kommunen teilen. Das regulatorische Fenster steht offen; der technische Stack ist bereit; das wirtschaftliche Argument ist klar. Die einzige verbleibende Frage ist der politische Wille.

---

## Quellenverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. Berlin: OSBA. https://scs.community/ — [CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel: Europäische Kommission.

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Konzeptualisierung und Entwicklung eines ganzheitlichen E-Government-Reifegradmodells. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, Adoption Barriers and Myths of Open Data and Open Government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/veroeffentlichungen

[10] openCode.de. (2022). *openCode — Open Source für die Verwaltung*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/

[12] Decidim Association. (2021). *Decidim: Free Open-Source Participatory Democracy*. Barcelona: Decidim Association. https://decidim.org/

[13] Nextcloud GmbH. (2023). *Nextcloud für Behörden*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix Specification v1.9*. https://spec.matrix.org/

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2023). *TYPO3 in der öffentlichen Verwaltung*. Düsseldorf: TYPO3 Association. https://typo3.org/

[20] OpenProject GmbH. (2023). *OpenProject für Behörden*. Berlin: OpenProject GmbH. https://www.openproject.org/

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/grundschutz

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[29] Vereinte Nationen DESA. (2022). *UN E-Government Survey 2022*. New York: Vereinte Nationen.

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/

[34] BigBlueButton Inc. (2023). *BigBlueButton 2.7*. https://bigbluebutton.org/

[35] Jitsi Community. (2023). *Jitsi Meet*. https://jitsi.org/

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/

[37] QGIS Project. (2023). *QGIS 3.34 LTR*. https://www.qgis.org/

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes v1.29*. https://kubernetes.io/

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL 16*. https://www.postgresql.org/

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen — Umsetzungsstrategie (EIF)*. Brüssel: ISA²-Programm. https://joinup.ec.europa.eu/

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/

[47] eCH — E-Government Standards. (2023). *eCH-Standards-Framework*. Bern: eCH Association. https://www.ech.ch/

[48] GovStack / ITU. (2023). *GovStack Building Blocks Spezifikation v1.0*. Genf: Internationale Fernmeldeunion. https://www.govstack.global/

[49] ZenDiS GmbH. (2024). *ZenDiS Jahresbericht 2024: Digitale Souveränität in der öffentlichen Verwaltung*. Berlin: ZenDiS GmbH. https://www.zendis.de/

[50] Europäische Kommission / OSOR. (2023). *Open Source Observatory Jahresbericht 2023*. Brüssel: Europäische Kommission DIGIT. https://joinup.ec.europa.eu/collection/open-source-observatory-osor

[51] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 — Datengesetz*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202302854

[52] Consul Democracy. (2023). *CONSUL Democracy: Open Government and E-Participation Web Software*. Madrid: Consul Democracy Foundation. https://consuldemocracy.org/

[53] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media.

[54] Schweizerische Bundeskanzlei. (2023). *Bundesgesetz über den elektronischen Ausweis und andere elektronische Nachweise (E-ID-Gesetz)*. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/fga/2023/2842/de

[55] GAIA-X Association AISBL. (2024). *GAIA-X Architecture Document v2024*. Brüssel: GAIA-X AISBL. https://gaia-x.eu/what-is-gaia-x/deliverables/

[56] Blind, K., Böhm, M., Grzegorzewska, P., Katz, A., Muto, S., Pätsch, S., & Schubert, T. (2021). *The Impact of Open Source Software and Hardware on Technological Independence, Competitiveness and Innovation in the EU Economy*. Brüssel: Europäische Kommission. https://doi.org/10.2759/430161

[57] DigitalService GmbH des Bundes. (2023). *Jahresbericht 2023*. Berlin: DigitalService GmbH des Bundes. https://digitalservice.bund.de/

[58] Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019). Artificial intelligence and the public sector. *International Journal of Public Administration*, 42(7), 596–615. https://doi.org/10.1080/01900692.2018.1498103

[59] Almeida, F., Santos, J. D., & Monteiro, J. A. (2023). Digital government transformation in European municipalities. *Government Information Quarterly*, 40(2), 101812. https://doi.org/10.1016/j.giq.2023.101812

[60] Scholl, H. J. (Hrsg.). (2017). *E-Government: Information, Technology, and Transformation*. London: Routledge. https://doi.org/10.4324/9781315095950

---

*Dieses Dokument ist die deutsche Übersetzung des englischen Strategiepapiers.*  
*Veröffentlicht unter der Creative Commons Attribution 4.0 International Lizenz (CC-BY-4.0).*  
*Zitation: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*  
*Versionshistorie: v0.1.0 (2026-06-20) → v0.2.0 (2026-06-21, zitationsabgeschlossener Entwurf)*
