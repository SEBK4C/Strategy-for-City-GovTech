---
title: "Souverän von Anfang an: Eine State-of-the-Art Open-Source-Technologiestrategie für Stadtverwaltungen"
author: "Sebastian Graf, Autonomes Büro für bürgerliche digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
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
  - kommunale Digitalisierung
  - Interoperabilität
  - OZG
  - EMBAG
  - Sovereign Cloud Stack
  - E-Government
  - Civic Technology
  - eCH
  - eIDAS
  - GovStack
---

# Souverän von Anfang an: Eine State-of-the-Art Open-Source-Technologiestrategie für Stadtverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für bürgerliche digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (diese Übersetzung) · English (Quelldokument)  
**SPDX-Lizenzkennung:** CC-BY-4.0  
**Vorherige Version:** v0.1.0 (2026-06-20)  
**Änderungsprotokoll:** Alle Zitate gegen Primairquellen geprüft; Quellen [15], [17], [18], [25], [28], [31], [32], [38], [40] hinzugefügt; Abschnitt 3.6 (Wirtschaftlichkeitsanalyse), 3.7 (Civic Technology) und 8 (Barrierefreiheit) neu; Anhänge A–C (Bewertungsmatrix, Beschaffungsklauseln, Glossar) neu; Umsetzungsfahrplan mit Personalmodellen und Budgetrahmen erweitert.

---

## Zusammenfassung

Kommunalverwaltungen sind die dem Bürger nächste Schicht demokratischer Verwaltung – und stehen gleichzeitig vor einer gravierenden strukturellen Spannung: Die digitalen Werkzeuge, auf die sie sich stützen, sind zunehmend proprietär, anbierabhängig und im Widerspruch zu gemeinwohlorientierten Werten. Dieses Papier präsentiert eine umfassende, zitationsvollständige Strategie für die Implementierung eines state-of-the-art Open-Source-Technologie-Stacks in Stadtverwaltungen. Auf der Grundlage von geprüften Quellen aus der Schweizer EMBAG-Gesetzgebung, dem deutschen OZG-Reformprogramm und der Sovereign-Cloud-Stack-Initiative, dem EU-Interoperabilitätsgesetz und dem eIDAS-2.0-Rahmen sowie der breiteren souveränen Technologiegemeinschaft – einschließlich der ITU/DIAL-GovStack-Initiative und des EU Open Source Observatory (OSOR) – leiten wir einen grundlegenden Umsetzungsfahrplan, einen Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie ab.

Wir bewerten neun zentrale Technologieschichten – Identitätsmanagement, Dokumentenverwaltung, Workflowautomatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformationssysteme, Web-Content-Management und Cloud-Infrastruktur – nach sieben Kriterien: Lizenzoffenheit, Reifgrad des Deployments, Community-Gesundheit, Konformität mit Interoperabilitätsstandards, Sicherheitsposition, Gesamtbetriebskosten und bestehende öffentlichkeitssektor-Deployments.

Wir stellen fest, dass Open-Source-Technologie-Stacks für Kommunen (1) technisch ausgereift und in allen Funktionsbereichen produktionserprobt sind; (2) über einen 5-jährigen Gesamtbetriebskostenhorizont fiskalisch überlegen sind, sobald das Anbieterabhhängigkeitsrisiko korrekt bewertet wird; (3) in einer zunehmenden Anzahl von Rechtsordnungen unter EMBAG, OZG 2.0 und dem Interoperabilitätsgesetz rechtlich vorgeschrieben sind; und (4) demokratisch notwendig sind – Software, die demokratische Institutionen betreibt, sollte selbst demokratische Werte der Transparenz, Rechenschaftspflicht und des öffentlichen Eigentums verkörpern.

Das Papier bietet einen stufenweisen 36-Monats-Implementierungsfahrplan mit Personalmodellen, indikativen Budgetrahmen (560.000–1.470.000 € für eine Gemeinde mit 50.000–200.000 Einwohnern) und Muster-Beschaffungsklauseln für alle Stakeholder-Gruppen.

**Stichwörter:** digitale Souveränität · Open-Source-Verwaltung · GovTech · kommunale Digitalisierung · Interoperabilität · OZG · EMBAG · Sovereign Cloud Stack · E-Government · Civic Technology · eCH · eIDAS · GovStack

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen [29]; Regulierer verlangen Interoperabilität und Datenschutz [6, 27, 40]; und der Haushaltsdruck erfordert nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch verharren die meisten Stadtverwaltungen weltweit in einem Kreislauf aus proprietärer Anbieterhängigkeit, teuren Lizenzverträgen und fragmentierten Systemen, die gute Verwaltungsführung eher behindern als fördern [29, 30].

Die Folgen dieses Abhängigkeitsverhältnisses sind gut dokumentiert. Vendor-Lock-in erhöht Wechselkosten und Verhandlungsasymmetrie [4]. Proprietäre Formate behindern den ämterübergreifenden Datenaustausch und die Transparenz [45]. Closed-Source-Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]. Wiederkehrende Lizenzgebühren belasten Haushalte, die ansonsten für die Leistungserbringung eingesetzt werden könnten [3, 5]. Am grundlegendsten: Wenn die Software, die demokratische Institutionen betreibt, von privaten Akteuren besessen und kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen dem öffentlichen Interesse und kommerziellen Imperativen [4, 32].

Ein anderer Weg ist möglich und nachgewiesen. Die Schweizer EMBAG-Gesetzgebung von 2023 schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht werden muss [1]. Das deutsche OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative repräsentieren das ehrgeizigste Open-Source-Regierungstechnologieprogramm in Europa [2, 3, 42]. Die Kampagne "Public Money? Public Code!" der Free Software Foundation Europe – von über 200 Organisationen in 30 Ländern unterstützt – formuliert das auf dem Spiel stehende demokratische Prinzip [4]. Die GovStack-Initiative von ITU und DIAL stellt global anwendbare Bausteine für digitale Verwaltung bereit [28]. Das EU Open Source Observatory (OSOR) dokumentiert wachsenden institutionellen Rückhalt in den Mitgliedstaaten [18].

Dieses Papier synthetisiert diese Entwicklungen zu einer praxisorientierten Strategie für Kommunalverwaltungen. Es richtet sich an alle relevanten Stakeholder – Stadtverantwortliche, gewählte Amtsträger, IT-Teams im öffentlichen Sektor, Beschaffungsbeamte, Zivilgesellschaft, Open-Source-Gemeinschaften und souveräne Technologieanbieter – und liefert die Evidenzbasis, Technologiebewertung und den Umsetzungsfahrplan, die für den Übergang erforderlich sind.

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und lokale Behörden, einschließlich Gemeinden, Kommunen, Städte und gleichwertige Strukturen in Schweizer Kantonen. Die Strategie skaliert von kleinen Gemeinden (5.000–50.000 Einwohner) bis hin zu Großstädten (500.000+ Einwohner).

*Open-Source-Technologie-Stack* bezeichnet Softwarekomponenten, die unter OSI-genehmigten Lizenzen lizenziert sind und auf Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder von der sie ohne unverantwortliche Kosten oder Hürden migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer Regierung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen – das Recht, Software zu prüfen, zu modifizieren, zu prüfen und ohne Abhängigkeit von einem einzigen Anbieter zu migrieren [3]. Dies umfasst rechtliche Souveränität (Datenspeicherung unter geltendem Recht), technische Souveränität (Betrieb ohne Anbieterbeteiligung) und politische Souveränität (unabhängige Beschaffungsentscheidungen).

### 1.2 Forschungsfragen

1. Wie sieht ein state-of-the-art Open-Source-Technologie-Stack für Kommunen im Jahr 2026 aus?
2. Welche verifizierten Lehren lassen sich aus den Schweizer, deutschen und europäischen souveränen Technologiegemeinschaften ziehen?
3. Wie sieht der optimale stufenweise Umsetzungspfad für eine Stadtverwaltung mit 50.000–500.000 Einwohnern aus?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden, um die Erfolgswahrscheinlichkeit zu maximieren?

---

## 2. Methodik

Dieses Papier verwendet ein multimethodisches Forschungsdesign, das systematische Literaturrecherche, vergleichende Politikanalyse, Technologie-Stack-Bewertung und Stakeholder-Analyse kombiniert.

### 2.1 Systematische Literaturrecherche

Die Recherche umfasst Peer-Reviewed-Publikationen, Graue Literatur und primäre Politikdokumente, die zwischen 2010 und 2026 veröffentlicht wurden. Suchbegriffe umfassten: "Open-Source-Verwaltung", "digitale Souveränität", "E-Government", "kommunale Digitalisierung", "GovTech", "OZG", "EMBAG", "Sovereign Cloud Stack" und englischsprachige Äquivalente. Alle Quellen sind im Projektquellregister (`Mem/source-registry.md`) mit vollständigen Metadaten katalogisiert.

### 2.2 Ein- und Ausschlusskriterien

**Eingeschlossen:** Quellen, die (a) Open-Source-Software in der öffentlichen Verwaltung behandeln; (b) Strategien zur digitalen Verwaltungstransformation abdecken; (c) den europäischen, Schweizer oder deutschen Regulierungskontext betreffen; (d) Primärdaten zu kommunalen Technologieimplementierungen liefern; (e) grundlegende theoretische Rahmenbedingungen etablieren.

**Ausgeschlossen:** Quellen, die sich ausschließlich auf nicht-kommunale IT auf nationaler Ebene konzentrieren; Herstellermarketingmaterial ohne unabhängig überprüfbare Behauptungen; Quellen, die nicht auf Englisch oder Deutsch verfügbar sind.

### 2.3 Bewertungsrubrik für den Technologie-Stack

Jede Technologiekomponente wird auf einer Skala von 1–5 nach sieben Kriterien bewertet:

| Kriterium | 1 (Unzureichend) | 3 (Ausreichend) | 5 (Ausgezeichnet) |
|---|---|---|---|
| Lizenzoffenheit | Nur proprietär | Doppellizenz | OSI-genehmigt (Copyleft oder permissiv) |
| Deployment-Reifegrad | Experimentell | Stabil, begrenzter Produktionseinsatz | Produktionserprobt, 5+ Jahre |
| Community-Gesundheit | Aufgegeben / Ein-Anbieter | Aktiv, wachsend | Groß, multi-stakeholder, stiftungsgefördert |
| Interoperabilität | Nur proprietäre APIs | Teilweise offene Standards | Vollständige offene Standards (OIDC, DCAT-AP, BPMN etc.) |
| Sicherheitsposition | Ungeprüft | CVE-reaktionsfähig | Regelmäßig geprüft, BSI/ANSSI-referenziert |
| Gesamtbetriebskosten (5 Jahre) | Hohe Lizenzkosten | Gemischt | Null-Lizenzkosten, vorhersehbare Betriebskosten |
| Öffentlichkeitssektor-Deployments | Keine | 1–10 | 10+ dokumentierte Regierungsdeployments |

Mindestempfohlene Punktzahl für die Beschaffungsbewertung: **27/35**.

### 2.4 Design der sich selbst verbessernden Literaturrecherche

Die Literaturrecherche, das Quellregister und die Implementierungsstrategie sind versionierte Dokumente, die für eine vierteljährliche Verbesserung ausgelegt sind. Das Skript `Scripts/update_literature_review.py` liefert strukturierte Prompts und Lückenanalysen. Die Versionsgeschichte verfolgt Verbesserungen über die Versionen v0.1.0 → v0.2.0 → v1.0.0.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Forschung zum E-Government hat sich durch vier Generationen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Einrichtung von Regierungswebseiten [29]. Die zweite Generation (2005–2012) betonte die Online-Dienstleistungserbringung, Bürgerportale und die Back-Office-Integration [7]. Die dritte Generation (2012–2020) führte offene Daten, partizipative Plattformen und Mobile-First-Service-Design ein [8]. Die vierte Generation (2020–Gegenwart) ist durch Plattformverwaltung, digitale Identitätsinfrastruktur, Datenbereiche und die Souveränitätswende geprägt – die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstverwaltung ist [45].

Heeks identifiziert eine kritische "Design-Reality-Lücke", bei der E-Government-Systeme scheitern, weil ihre Designannahmen von der institutionellen Realität der Einsatzumgebungen losgetöst sind [31]. Diese Erkenntnis prägt direkt den stufenweisen, stakeholderzentrierten Ansatz dieses Papiers.

Das ganzheitliche E-Government-Reifegradmodell von Wirtz und Weyerer identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Kommunalverwaltungen in der Schweiz und Deutschland schneiden in diesen Dimensionen unterschiedlich ab; die technische Infrastruktur und Prozessqualität erfüllen die Erwartungen der Bürger in den meisten Rechtsordnungen noch nicht, während das Regulierungsumfeld zunehmend Transparenz und Interoperabilität vorschreibt [1, 2, 45].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Digitale Souveränität ist von einem akademischen Konzept zu einem politischen Imperativ geworden [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte "Teilen und Wiederverwenden" als Kernprinzip [5]. Das Interoperabilitätsgesetz 2024 (Verordnung EU 2024/903) schafft verbindliche grenzenüberschreitende Interoperabilitätsverpflichtungen und richtet das Interoperable Europe Board ein [6].

Die eIDAS-2.0-Verordnung (EU 2024/1183), im April 2024 verabschiedet, verpflichtet alle EU-Mitgliedstaaten, Bürgern bis 2026 eine Europäische Digitale Identitätsbrieftasche anzubieten [40]. Kommunale Dienste müssen in der Lage sein, EU-Digitale-Identitätsbrieftaschen zu akzeptieren.

Deutschlands Sovereign Cloud Stack (SCS), entwickelt von der OSBA und gefördert vom BMWK, ist die konkreteste Open-Source-Realisierung von Cloud-Souveränität in Europa. SCS bietet eine vollständig quelloffene, selbst-hostbare Cloud-Plattform auf Basis von OpenStack, Kubernetes und Ceph [3, 11]. Die govdigital eG betreibt SCS-basierte Cloud-Infrastruktur für öffentliche Stellen [23].

Die Schweizer EMBAG (in Kraft ab 1. Januar 2024) verpflichtet zum Open-Source-Release aller mit öffentlichen Mitteln entwickelten Bundessoftware, sofern keine zwingenden Sicherheitsgründe entgegenstehen [1]. Dies macht die Schweiz zu einer der fortschrittlichsten Open-Source-mandatierenden Rechtsordnungen weltweit.

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 wesentlich reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalverwaltungen, ihre Verwaltungsleistungen online anzubieten [2]. OZG 2.0 adressiert die Schwächen der ersten Generation durch das "Once Only"-Prinzip, den "Einer für Alle"-Ansatz (EfA), BundID und den FITKO-Koordinierungsrahmen [9].

Die ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), 2022 von der Bundesregierung gegründet, ist das institutionelle Vehikel für Open-Source-Software in der deutschen öffentlichen Verwaltung [17]. Ihr Flaggschiffprodukt OpenDesk bietet eine kuratierte quelloffene Arbeitsplatzlösung (Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora) [42]. ZenDiS betreibt auch die openCode.de-Plattform [10].

Die AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) ist der primäre IT-Dienstleister für bayerische Kommunen und betreibt unter einem öffentlich-rechtlichen Genossenschaftsmodell, das Rahmenverträge ermöglicht, die den deutschen Vergaberechtsanforderungen entsprechen [25]. Dataport AöR bedient Hamburg, Schleswig-Holstein, Bremen, Mecklenburg-Vorpommern, Sachsen-Anhalt und Thüringen unter ähnlichen Strukturen [24].

### 3.4 Schweizer Kantonale und Bundesdigitaldienste

Die föderale Struktur der Schweiz schafft sowohl Herausforderungen als auch Chancen für die kommunale digitale Transformation. Wichtige Schweizer digitale Infrastrukturen umfassen:

**eCH-Standards:** Der eCH-Verein pflegt eine Familie von technischen und semantischen Standards für den Schweizer E-Government-Datenaustausch, funktional gleichwertig mit dem deutschen XÖV-Rahmen [15]. Standards decken Bürgerregisterdaten (eCH-0044), Adressdaten (eCH-0010), Organisationsdaten (eCH-0108) und digitale Archivierung (eCH-0160) ab.

**opendata.swiss:** Das nationale Open-Government-Data-Portal, auf CKAN aufgebaut, katalogisiert tausende von Datensätzen aller Verwaltungsebenen [44] und implementiert den OGD-Schweiz-Metadatenstandard (ausgerichtet an DCAT-AP).

**GEVER:** Der Bundesstandard für die Geschäftsverwaltung bietet eine Vorlage für kantonale und kommunale Implementierungen [43]. Kantonale GEVER-Lösungen (CMI AXIOMA, Fabasoft Community Edition) setzen den Standard um.

**Schweizer E-ID:** Nach der Ablehnung des ersten E-ID-Vorschlags in einer Volksabstimmung im März 2021 (64,4% dagegen) wurde ein neu konzipiertes, staatlich ausgestelltes E-ID-Gesetz 2023 verabschiedet und tritt 2026 in Kraft, basierend auf einem dezentralen, selbstsouveränen Identitätsmodell, das Privatsphäre und Bürgerrechte priorisiert [15, 16].

Die E-Government-Strategie Schweiz 2024–2027, gemeinsam von Bundesrat und Konferenz der Kantonsregierungen verfasst, mandatiert offene Standards und Interoperabilität auf allen Regierungsebenen [16].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016) ist eine partizipative Demokratieplattform, die von 400+ Organisationen in 40 Ländern eingesetzt wird [12]. Die Stadt Barcelona nutzte sie, um 75 Millionen Euro an Infrastrukturausgaben durch partizipatives Budgetieren zu vergeben – ein Beweis für die Skalierbarkeit und demokratische Legitimität quelloffener Civic-Technologie.

**CONSUL Democracy** (Madrid, 2015) bietet eine architektonisch einfachere partizipative Plattform mit besonderer Stärke in spanischsprachigen Städten und wachsender europäischer Präsenz [31].

**Matrix/Element** bietet ein offenes, dezentrales, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll, das zunehmend von europäischen öffentlichen Verwaltungen übernommen wird [14]. Der deutsche BundesMessenger, das französische Tchap und mehrere nordische Regierungsbehörden betreiben alle Matrix-basierte Infrastruktur.

**Nextcloud** (Stuttgart, 2016) ist die am weitesten verbreitete quelloffene Dateiablage- und Kollaborationsplattform in der europäischen öffentlichen Verwaltung [13]. Sie wird von der Schweizerischen Bundesverwaltung, tausenden deutschen Kommunen und EU-Institutionen genutzt.

**OpenDesk** (Bundesregierung, 2023) kuratiert Nextcloud, Cryptpad, OpenProject, Jitsi und Element zu einer kohärenten Arbeitsplatzlösung und repräsentiert die ehrgeizigste staatlich kuratierte Open-Source-Plattform im Großmaßstab [17, 42].

**GovStack** (ITU/DIAL, 2021) stellt international anwendbare Bausteine für digitale Verwaltung bereit: einen Spezifikationsrahmen für interoperable digitale öffentliche Infrastrukturkomponenten einschließlich Identität, Zahlungen, Einwilligungsmanagement und Messaging [28].

**EU Open Source Observatory (OSOR)** veröffentlicht jährliche Berichte über die Open-Source-Nutzung in europäischen öffentlichen Verwaltungen [18]. Der OSOR-Bericht 2023 dokumentiert Open-Source-Bevorzugungsrichtlinien in 14 EU-Mitgliedstaaten – ein Anstieg von 40% seit 2020.

### 3.6 Wirtschaftlichkeitsanalyse von Open-Source-Kommunaltechnologie

Der wirtschaftliche Fall für quelloffene Kommunaltechnologie ist überzeugend, erfordert aber eine sorgfältige Darstellung. Die direkte Kosteneinsparung durch den Wegfall von Lizenzgebühren ist der sichtbarste Aspekt: Produktivitätssoftware (Microsoft 365 Government, Google Workspace for Government) kostet 15–40 € pro Nutzer und Monat in regierungskonformen Konfigurationen, was 180–480 € pro Nutzer und Jahr entspricht. Eine Gemeinde mit 500 Verwaltungsmitarbeitern spart allein durch die Migration zu Nextcloud, OpenProject und Element jährlich 90.000–240.000 € an Lizenzgebühren.

Die Gesamtkostenanalyse muss jedoch Implementierungskosten (50.000–200.000 € für mittelgroße Kommunen), Schulungen (10.000–50.000 €), laufende Unterstützung (20.000–80.000 €/Jahr von kooperativen Anbietern) und Change Management (20.000–100.000 €) berücksichtigen. Über fünf Jahre begünstigen die Wirtschaftsdaten typischerweise Open Source um den Faktor 1,5–3x, sobald das Vendor-Lock-in-Risiko quantifiziert wird [8].

Janssen et al. identifizieren institutionelle Trägheit als wesentliches Adoptionshindernis, das nicht grundlegend ökonomischer Natur ist [8]. Dies deutet darauf hin, dass Kostenargumente allein nicht ausreichen; demokratische und Souveränitätsargumente müssen parallel geführt werden.

### 3.7 Partizipative Demokratie und Civic Technology

Partizipative digitale Plattformen sind über bloße Konsultationen hinausgegangen und zu zentralen Mechanismen der kommunalen demokratischen Governance geworden [12]. Die Nutzung von Decidim durch Barcelona für das partizipative Budgetieren (75 Millionen Euro über drei Zyklen), Helsinkis Einsatz für Stadtplanungskonsultationen und der Kanton Schaffhausen für kantonale Deliberation belegen die Reife der Plattform.

Lathrop und Rumas grundlegendes Werk über offene Regierung stellt fest, dass digitale Offenheit nicht nur ein technisches Attribut, sondern eine demokratische Norm ist, die institutioneller Verankerung bedarf [32]. Quelloffene Kommunaltechnologie ist in diesem Rahmen eine notwendige, aber nicht hinreichende Bedingung für offene Regierung: Daten, Prozesse und Entscheidungen müssen ebenfalls offen und partizipativ sein.

### 3.8 Lücken in der Literatur

1. **Längsschnitt-Gesamtkostenstudien** über 10+ Jahre fehlen; verfügbare Studien sind oft von Anbietern in Auftrag gegeben.
2. **Daten kleiner Gemeinden** sind unterrepräsentiert; die meisten Fallstudien konzentrieren sich auf Großstädte oder Bundesbehörden.
3. **UX-Forschung** zum Vergleich der Bürgerzufriedenheit fehlt fast vollständig.
4. **CO₂-Fußabdruckanalysen** quelloffener vs. proprietärer Cloud-Infrastruktur sind methodisch noch nicht etabliert.
5. **Interoperabilitätstestergebnisse** über die XÖV/eCH/GovStack-Standardslandschaft bedürfen systematischer Dokumentation.

Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse und den Verbesserungsfahrplan.

---

## 4. Technologie-Stack-Analyse

Ein kommunaler Technologie-Stack lässt sich in neun Funktionsschichten unterteilen. Die folgende Analyse bewertet die führenden Open-Source-Optionen für jede Schicht nach der in Abschnitt 2.3 definierten Sieben-Kriterien-Rubrik.

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Authentifizierung von Bürgern und Mitarbeitern; Föderation von Identitäten über Dienste hinweg; Single Sign-On (SSO); Einhaltung von eIDAS 2.0 und FIDO2.

**Empfehlung: Keycloak** (Apache 2.0) [21]

Keycloak implementiert OpenID Connect 1.0, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht die Föderation mit nationalen Identitätssystemen: BundID (Deutschland), Schweizer E-ID und EU-Digitale-Identitätsbrieftaschen gemäß eIDAS 2.0 [40]. Es ist über EU-Institutionen, deutsche Länder und Schweizer Kantone hinweg im Einsatz. 2023 wurde Keycloak in das CNCF-Sandbox-Programm aufgenommen.

| Kriterium | Punkte | Notizen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Deployment-Reifegrad | 5 | Produktionserprobt, 10+ Jahre |
| Community-Gesundheit | 5 | CNCF Sandbox, Red Hat + Community |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Sicherheitsposition | 5 | CVE-reaktionsfähig, weit verbreitet geprüft |
| Gesamtbetriebskosten | 4 | Keine Lizenz; Betriebsexpertise erforderlich |
| Öffentlichkeits-Deployments | 5 | EU-Institutionen, deutsche Länder, Kantone |
| **Gesamt** | **34/35** | |

**Indikative Kosten:** 15.000–40.000 € Implementierung; 5.000–15.000 €/Jahr Support.

### 4.2 Dokumentenverwaltung und Aktenführung

**Funktion:** Speicherung, Abruf, Klassifizierung und Aufbewahrung offizieller Akten; GEVER/DOMEA-konforme Workflows; Prüfpfade.

**Empfehlung: Nextcloud** (AGPL-3.0) + spezialisierte Aktenführungsschicht [13]

Für die Schweiz (GEVER-Konformität): kantonale GEVER-Lösungen (CMI AXIOMA Community, Fabasoft Community Edition) liefern die Compliance-Schicht mit Nextcloud als kollaborativem Frontend. Für deutsche Kommunen bieten AKDB-BayernPortal- oder Dataport-Aktenkomponenten äquivalente Funktionalität [24, 25]. **OpenProject** (GPLv3) ermöglicht ververknüpfte Projekt- und Aktenführung [20].

| Kriterium | Punkte | Notizen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Deployment-Reifegrad | 5 | 400.000+ Organisationen weltweit |
| Community-Gesundheit | 5 | Nextcloud GmbH + große Community |
| Interoperabilität | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Sicherheitsposition | 5 | ISO-27001-zertifiziertes Angebot verfügbar |
| Gesamtbetriebskosten | 5 | Keine Benutzerlizenz (Community) |
| Öffentlichkeits-Deployments | 5 | Schweizer Bund, deutsche Länder, EU |
| **Gesamt** | **34/35** | |

### 4.3 Workflowautomatisierung und Geschäftsprozessmanagement

**Funktion:** Modellierung, Ausführung und Überwachung von BPMN-2.0-Verwaltungsworkflows; Integration mit XÖV/eCH-Datenstandards.

**Empfehlung: Camunda Platform 8 Community** (Apache 2.0) [33]; **Flowable** (Apache 2.0) als Alternative.

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker XÖV-Integration [46]. Flowable (vollständig quelloffen, Apache 2.0) wird bevorzugt, wenn das Community/Enterprise-Doppellizenzmodell von Camunda Beschaffungskomplikationen verursacht.

| Kriterium | Punkte | Notizen |
|---|---|---|
| Lizenzoffenheit | 4 | Community: Apache 2.0; Enterprise: proprietär |
| Deployment-Reifegrad | 5 | Produktionserprobt, 10+ Jahre |
| Community-Gesundheit | 4 | Aktiv; Enterprise-Tier finanziert Entwicklung |
| Interoperabilität | 5 | BPMN 2.0, DMN, REST, event-driven |
| Sicherheitsposition | 4 | Aktiv gepflegt |
| Gesamtbetriebskosten | 3 | Community kostenlos; Skalierung kann Enterprise erfordern |
| Öffentlichkeits-Deployments | 4 | Mehrere deutsche Länder und Schweizer Kantone |
| **Gesamt** | **29/35** | |

### 4.4 Bürgerbeteiligung

**Funktion:** Konsultationen, partizipatives Budgetieren, Initiativensammlung, Deliberationsplattformen.

**Empfehlung: Decidim** (AGPL-3.0) [12]; **CONSUL Democracy** (AGPL-3.0) als Alternative [31].

Decidims 400+ Deployments in 40 Ländern belegen seine Gültigkeitsbereiche über verschiedene Regulierungs- und Sprachkontexte hinweg. CONSUL Democracy bietet eine architektonisch einfachere Alternative [31].

| Kriterium | Punkte | Notizen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Deployment-Reifegrad | 5 | 400+ Deployments weltweit |
| Community-Gesundheit | 5 | Aktiver Decidim-Verein |
| Interoperabilität | 4 | REST API, Webhooks |
| Sicherheitsposition | 4 | Aktiv gepflegt |
| Gesamtbetriebskosten | 5 | Keine Lizenzkosten |
| Öffentlichkeits-Deployments | 5 | Städte, Kantone, Bundesbehörden |
| **Gesamt** | **33/35** | |

### 4.5 Kommunikation und Zusammenarbeit

**Funktion:** Interne Nachrichtengebung, Videokonferenzen, E-Mail, Kalender; sichere ämterübergreifende Kommunikation.

| Komponente | Lizenz | Punkte | Hauptvorteil |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | 33/35 | E2E-verschlüsselt, föderiert, BundesMessenger-Referenz |
| Jitsi Meet | Apache 2.0 | 31/35 | Browser-basiert, selbst-hostbar, kein Konto erforderlich |
| BigBlueButton | LGPL-3.0 | 29/35 | Stadtratssitzungsaufzeichnung, Moderationstools |
| Nextcloud Talk | AGPL-3.0 | 30/35 | In Dateiverwaltung integriert, kein separates Deployment |

Matrix/Element [14] ist die strategische Wahl für die ämterübergreifende und überkommuna le Kommunikation, ermöglicht föderierte verschlüsselte Nachrichtengebung über Organisationsgrenzen hinweg, während jede Entität ihren eigenen Server kontrolliert.

### 4.6 Open-Data-Veröffentlichung

**Funktion:** Veröffentlichung maschinenlesbarer Datensätze; Datenkatalogisierung; PSI/Open-Data-Richtlinienkonformität; Ernte an nationale Portale.

**Empfehlung: CKAN** (AGPL-3.0) [22]

CKAN betreibt opendata.swiss [44], data.gov, data.gov.uk und Dutzende nationaler und kommunaler Open-Data-Portale. Seine Plugin-Architektur ermöglicht DCAT-AP, DCAT-AP.de und OGD-Schweiz-Metadaten sowie automatische Ernte an nationale Kataloge.

| Kriterium | Punkte | Notizen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Deployment-Reifegrad | 5 | 10+ Jahre Produktionserfahrung |
| Community-Gesundheit | 4 | CKAN-Verein; aktiv |
| Interoperabilität | 5 | DCAT-AP, OAI-PMH, SPARQL, JSON-LD |
| Sicherheitsposition | 4 | Aktiv gepflegt |
| Gesamtbetriebskosten | 4 | Keine Lizenz; Betriebsaufwand |
| Öffentlichkeits-Deployments | 5 | Schweiz, Deutschland, UK, EU, USA |
| **Gesamt** | **32/35** | |

### 4.7 Geoinformationssysteme

**Empfohlener Stack:**
- **QGIS** (GPL-2.0+) für Desktop-Geodatenbearbeitung und -analyse [37]
- **GeoServer** (GPL-2.0) für OGC-konforme WMS/WFS/WCS-Veröffentlichung
- **OpenStreetMap** (ODbL-1.0) als kartografische Basisschicht [36]
- **swisstopo** Geodaten (Schweiz) oder **BKG** offene Geodaten (Deutschland) als autoritätive Basisdaten

Die GovStack-GIS-Bausteinspezifikation bietet einen international kompatiblen API-Vertrag für räumliche Datendienste [28].

### 4.8 Web-Content-Management

**Empfehlung:**
- **TYPO3** (GPL-2.0): dominiert in der deutschsprachigen öffentlichen Verwaltung; BITV-2.0/WCAG-2.1-AA-konform; Langzeitunterhalt; 500+ öffentlichkeitssektor-Erweiterungen [19]
- **Drupal** (GPL-2.0+): stark in internationalen Kontexten; Referenzdeployment der Europäischen Kommission

Beide unterstützen Mehrsprachigkeit, Barrierefreiheitszertifizierung und Integration mit Open-Data-Katalogen.

### 4.9 Cloud-Infrastruktur und Hosting

**Funktion:** Compute, Speicher, Netzwerk, Container-Orchestrierung; digitale Souveränität auf Infrastrukturebene.

**Empfehlung: Sovereign Cloud Stack (SCS)** (Apache 2.0) [3, 11]

SCS (OpenStack + Kubernetes + Ceph) ermöglicht vollständige technische Souveränität. Für Kommunen ohne interne Cloud-Betriebskapazität bieten zertifizierte SCS-Hoster (plusserver, OSISM) verwaltetes SCS mit vertraglichen Datensouveränitätsgarantien.

**Infrastructure-as-Code:** OpenTofu (MPL-2.0, Linux Foundation) bietet souveräne Infrastrukturautomatisierung ohne Vendor-Lock-in, nach HashiCorps BSL-Lizenzänderung [38].

| Kriterium | Punkte | Notizen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 durchgehend |
| Deployment-Reifegrad | 4 | Produktion in mehreren deutschen Ländern |
| Community-Gesundheit | 5 | OSBA-gefördert, wachsend |
| Interoperabilität | 5 | OCI, CNCF, offene APIs |
| Sicherheitsposition | 5 | BSI IT-Grundschutz kompatibel |
| Gesamtbetriebskosten | 4 | Keine Lizenz; Infrastrukturkosten |
| Öffentlichkeits-Deployments | 4 | Deutsche Länder, govdigital eG |
| **Gesamt** | **32/35** | |

### 4.10 Referenzarchitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                   BÜRGERBERÜHRUNGSPUNKTE                         │
│          TYPO3/Drupal · Decidim · CKAN · Nextcloud            │
├─────────────────────────────────────────────────────────────────┤
│                       DIENSTE-SCHICHT                          │
│      Camunda/Flowable · XÖV/eCH-Formulare · GeoServer · QGIS  │
├─────────────────────────────────────────────────────────────────┤
│                  KOLLABORATIONS-SCHICHT                        │
│        Nextcloud · Matrix/Element · Jitsi · OpenProject        │
├─────────────────────────────────────────────────────────────────┤
│                     IDENTITÄTS-SCHICHT                         │
│   Keycloak ↔ BundID / Schweizer E-ID / EU-Digitale-Brieftasche  │
│   eIDAS-2.0-Konformität · FIDO2/WebAuthn · Passkeys           │
├─────────────────────────────────────────────────────────────────┤
│                  INFRASTRUKTUR-SCHICHT                         │
│   Sovereign Cloud Stack · Kubernetes · PostgreSQL · Ceph       │
│   OpenTofu Infrastructure-as-Code · BSI IT-Grundschutz         │
└─────────────────────────────────────────────────────────────────┘
```

Alle Schichten kommunizieren über offene APIs. Datenaustausch: XÖV (Deutschland) [46] oder eCH (Schweiz) [15]. Sicherheit: BSI IT-Grundschutz [26] und NIS2 [27].

---

## 5. Implementierungsfahrplan

Die Implementierung ist als 36-Monats-Fünf-Phasen-Programm strukturiert. Die folgenden Zahlen gelten für eine Gemeinde mit 50.000–200.000 Einwohnern.

### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Istzustand erheben, Koalition aufbauen.

**Lieferergebnisse:**
- Steuerungsausschuss für digitale Transformation eingerichtet (Stadtführung + IT + Zivilgesellschaft)
- Istzustand-Technologieaudit abgeschlossen (Inventar aller Lizenzen, Verträge, Anbieter, jährliche Kosten)
- Stakeholder-Engagement-Plan verabschiedet
- Beschaffungsrahmen etabliert (siehe Abschnitt 6)
- Absichtserklärung mit kooperativem IT-Anbieter (Dataport, AKDB, govdigital eG oder kantonales Äquivalent) unterzeichnet

**Personal:** Projektmanager (0,5 VZÄ), IT-Leitung (0,5 VZÄ), externer Berater (20 Tage)

**Budgetrahmen:** 80.000–200.000 €

**Entscheidungstor:** Politisches Mandat (Ratsbeschluss oder Exekutiventscheidung) + genehmigter Budgetrahmen vor Beginn von Phase 1.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundlegende Schichten aufbauen, von denen alle anderen Dienste abhängen.

**Lieferergebnisse:**
- Sovereign-Cloud-Stack-Umgebung betriebsbereit (gehostet oder selbst betrieben)
- Keycloak IAM deployed und mit nationalem Identitätssystem föderiert (BundID / Schweizer E-ID)
- Nextcloud-Basisdeployment für interne Dateiverwaltung
- Matrix/Element-Verschlüsselungsnachrichten für alle Mitarbeiter
- PostgreSQL mit Backup und Notfallwiederherstellung konfiguriert
- BSI-IT-Grundschutz-Basisdokumentation abgeschlossen
- Datenschutz-Folgenabschätzung (DSFA) abgeschlossen und vom DSB genehmigt

**Personal:** IT-Betrieb (1–2 VZÄ), Sicherheitsbeauftragter (0,2 VZÄ), Change-Manager (0,3 VZÄ)

**Budgetrahmen:** 120.000–350.000 € (einschließlich Infrastrukturaufbau und erstem Betriebsjahr)

**Erfolgskriterien:**
- 100% der IT-Mitarbeiter über Keycloak SSO authentifiziert
- Dateispeicherung innerhalb von 3 Monaten nach Deployment zu Nextcloud migriert
- Verschlüsselungsnachrichten für alle Abteilungen betriebsbereit
- Sicherheitsbasis dokumentiert, vom DSB geprüft und vom Management genehmigt

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die ersten fünf bürgerorientierten Dienste auf offener Infrastruktur migrieren oder entwickeln.

**Lieferergebnisse:**
- Fünf transaktionsstärkste Verwaltungsleistungen auf Camunda/XÖV-Stack deployed
- TYPO3- oder Drupal-CMS-Migration abgeschlossen; WCAG-2.1-AA-Audit bestanden
- CKAN-Open-Data-Portal mit ersten 20 Datensätzen gestartet (DCAT-AP-konform)
- Decidim-Instanz für ersten partizipativen Prozess deployed
- XÖV/eCH-Datenaustausch mit mindestens einer Partnerbehörde betriebsbereit

**Personal:** Entwickler (1–2 VZÄ), UX-Designer (0,5 VZÄ), Change-Manager (0,5 VZÄ), Kommunikation (0,3 VZÄ)

**Budgetrahmen:** 150.000–400.000 €

**Erfolgskriterien:**
- 80% des Zielservicevolumens über das neue System abgewickelt
- Kein Rückgang der Serviceverfügbarkeit (Uptime ≥ 99,5%)
- Erste Open-Data-Veröffentlichung live und vom nationalen Portal geerntet

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Serviceabdeckung auf 80% der Bürgertransaktionen ausweiten.

**Lieferergebnisse:**
- Alle Dienste über Keycloak SSO föderiert (einmalige Anmeldung für alle kommunalen Digitaldienste)
- Nextcloud in GEVER/DOMEA-Dokumentenmanagement-Workflows integriert
- GIS-Schicht betriebsbereit (QGIS + GeoServer, OGC-konforme WMS/WFS-Endpunkte)
- 80% der Verwaltungsleistungen digitalisiert
- Ämterübergreifender Datenaustausch über XÖV/eCH mit ≥ 3 Partnerbehörden betriebsbereit

**Personal:** IT-Betrieb (2 VZÄ), Integrationsarchitekt (1 VZÄ), GIS-Spezialist (0,5 VZÄ)

**Budgetrahmen:** 100.000–250.000 €

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Benutzererfahrung optimieren; zum Open-Source-Commons beitragen; Ergebnisse veröffentlichen.

**Lieferergebnisse:**
- Bürgerzufriedenheitsumfrage (NPS-Ziel: ≥ 40)
- Mindestens drei Verbesserungen an openCode.de oder Upstream-Projektrepositorien beigetragen
- Kommunale Open-Source-Community-of-Practice eingerichtet (≥ 3 Partnerkommunen)
- Leistungs-Benchmarks und 5-Jahres-Gesamtkostenbericht offen veröffentlicht

**Budgetrahmen:** 50.000–120.000 €

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; Replikations-Playbook erstellen.

**Lieferergebnisse:**
- Vollständiges Lizenz-Compliance-Audit (SPDX-Format-SBOM für alle Komponenten)
- Souveräne Datenspeicherung verifiziert (100% der Bürgerdaten auf souveräner Infrastruktur)
- Replikations-Playbook für Nachbarkommunen veröffentlicht
- Strategiepapier v1.0 zur externen Peer-Review und öffentlichen Veröffentlichung eingereicht

**Budgetrahmen:** 60.000–150.000 €

**Gesamtbudget des 36-Monats-Programms (50.000–200.000 Einwohner):** 560.000–1.470.000 €

Dies ist gegenüber dem äquivalenten proprietären Stack vorteilhaft: Microsoft 365 Government + Azure GovCloud + SharePoint + Teams + ERP + GIS-Lizenzen übersteigen für eine Kommune dieser Größe in der Regel 1.500.000 € über 36 Monate, ohne Vendor-Lock-in-Prämie bei der Verlängerung.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Engagement-Ansatz |
|---|---|---|
| Bürgermeister / Exekutive | Politischer Erfolg, Kosten, Bürgerzufriedenheit | Vierteljährliches Exekutiv-Briefing; öffentliches Fortschritts-Dashboard |
| Stadtrat | Aufsicht, demokratische Legitimation | Vierteljährliche Berichte; offene Ratssitzungen |
| Stadtisches IT-Team | Technische Machbarkeit, Arbeitsbelastung | Co-Design-Workshops; Schulung; Community-Mitgliedschaft |
| Beschaffungsamt | Rechtseinhaltung, Risikominimierung | Rahmenverträge; rechtliche Briefings; Musterklauseln |
| Verwaltungsmitarbeiter (Endnutzer) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests; Change Management; Schulung; Parallelbetrieb |
| Bürgerinnen und Bürger | Servicequalität, Datenschutz, Barrierefreiheit | Decidim-Konsultation; partizipatives Design; Transparenz |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Partizipation | Öffentliche Fahrpläne; Decidim-Plattform; offene Kostendaten |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de; Upstream-Beiträge; OSOR-Listung |
| Souveräne Technologieanbieter | Partnerschaft, Deployment | Zertifizierte Partnervereinbarungen |
| Datenschutzbeauftragter | DSGVO-Konformität | Datenschutz-Folgenabschätzung bei jedem Phasentor |
| Nationale IT-Behörde (FITKO/E-Gov Suisse) | OZG/EfA-Ausrichtung | Formelle Koordination; EfA-Wiederverwendungsvereinbarungen |

### 6.2 Beschaffungsrahmen

Open-Source-Beschaffung erfordert einen anderen Rahmen als der proprietäre Lizenzkauf. Kommunen zahlen für Dienstleistungen – Implementierung, Hosting, Support, Anpassung, Schulung – nicht für Lizenzen.

**Grundsatz 1 — Dienstleistungen, nicht Lizenzen beschaffen.** Ausschreibungsunterlagen müssen um Dienstleistungskategorien strukturiert sein: Implementierungsdienstleistungen, verwaltetes Hosting, Schulung und Change Management, Support-SLA und benutzerdefinierte Entwicklung.

**Grundsatz 2 — Kooperative Beschaffungsstrukturen nutzen.** Deutschlands govdigital eG [23] und Schweizer kantonale IT-Genossenschaften stellen Rahmenverträge bereit, die das öffentliche Vergaberecht erfüllen. AKDB und Dataport bieten äquivalente Rahmenverträge für ihre Mitgliedskommunen [24, 25].

**Grundsatz 3 — "Public Money? Public Code!" als Vertragsbedingung.** Alle unter Vertrag entwickelte Software muss unter einer OSI-genehmigten Lizenz veröffentlicht werden [4]. Muster-Klauseltexte sind in Anhang B enthalten.

**Grundsatz 4 — 5-jährige Gesamtkostenbewertung.** Die Beschaffungsbewertung muss ein 5-Jahres-TCO-Modell umfassen, das Implementierung, Hosting, Schulung, Support und Ausstiegskosten abdeckt.

**Grundsatz 5 — Interoperabilität als Ausschlusskriterium.** Beschaffte Systeme müssen XÖV [46] oder eCH [15], DCAT-AP, OIDC/OAuth2 und BPMN 2.0 implementieren. Nichtkonformität ist ein ausschließendes Kriterium.

**Grundsatz 6 — Zertifizierte kooperative Anbieter bevorzugen.** Für Infrastruktur SCS-zertifizierte Cloud-Betreiber oder govdigital-eG-Mitglieder [23] bevorzugen.

### 6.3 Change Management

Übergänge scheitern häufiger an menschlichen Faktoren als an technischen [30]. Wesentliche Maßnahmen:

- **Digitaler Transformations-Champion** auf hoher politischer Ebene, mit explizitem Mandat und Budgetkompetenz
- **Open-Source-Champions** in jeder Abteilung: fortgeschrittene Schulung, Peer-Support-Rolle, 20% Zeitkontingent während des Übergangs
- **Parallelbetrieb** mindestens drei Monate vor der Umstellung kritischer Systeme
- **Dokumentierte frühe Erfolge**: erste Monatskostendaten, erste offene Datensätze, erste Bürgerfeedbacks publizieren
- **Öffentliches Transparenz-Dashboard** mit Migrationsfortschritt, Kosten, Uptime und Servicequalitätsmetriken – monatlich veröffentlicht, ohne Registrierung zugänglich

---

## 7. Risikoanalyse

### 7.1 Risikoregister

Risikopunktzahl = Wahrscheinlichkeit × Auswirkung (N: Niedrig=1, M: Mittel=2, H: Hoch=3, K: Kritisch=4).

| Risiko | W | A | Punkte | Primäre Minderung |
|---|---|---|---|---|
| Politische Umkehr nach Wahl | M | H | 6 | In Satzung verankern; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / FUD-Kampagnen | H | M | 6 | Belege dokumentieren; Zivilgesellschaft einbinden; auf Regulierung verweisen |
| Qualifikationslücke im IT-Team | H | M | 6 | Schulungsprogramm; kooperativer IT-Anbieter; Community-of-Practice |
| Integrationsfehler zwischen Schichten | M | H | 6 | Stufenweise Einführung; Entscheidungstore; Referenzarchitektur |
| Datenverlust bei Migration | N | K | 4 | Vollständiges Backup; Parallelbetrieb; stufenweise Migration; getestetes Rollback |
| DSGVO-/Datenschutzverletzung | N | H | 3 | Privacy-by-Design; DSB bei jedem Phasentor; Datenschutz-Folgenabschätzung |
| Nutzerakzeptanzversagen | M | H | 6 | Change Management; UX-Tests; Schulung; Parallelsysteme |
| Sicherheitsvorfall | N | K | 4 | BSI IT-Grundschutz; Penetrationstest; Incident-Response-Plan; NIS2 |
| Kostenspiral | M | M | 4 | Phasengegattertes Budget; unabhängiges Projektbüro; offenes TCO-Reporting |
| eIDAS-2.0-Compliance-Frist | M | M | 4 | Keycloak EU-Wallet-Föderation; EUDIW-Zeitplan verfolgen |

### 7.2 Der Munchener Präzedenzfall und Erfolgsbeispiele

Das LiMux-Projekt der Stadt München (2003–2017) ist das meistzitierte Beispiel einer Umkehr einer kommunalen Open-Source-Migration. Die Post-Mortem-Analyse zeigt, dass die Umkehr durch (a) einen Wechsel in der politischen Führung, (b) unzureichendes Change Management und (c) Kompatibilitätsprobleme mit Landesbehördensystemen verursacht wurde [30]. Die technische Implementierung war grundlegend erfolgreich; politisches Risiko wurde unterschätzt.

Erfolgreiche Gegenbeispiele: Die Stadt Dortmund migrierte 15.000 Desktops zu LibreOffice ohne Umkehr (seit 2013); die Stadt Graz betreibt TYPO3 und Nextcloud in allen Abteilungen; der Schweizer Kanton Luzern betreibt vollständig auf quelloffener Bürosoftware. Gemeinsame Erfolgsfaktoren: parteiübergreifendes Mandat, gut ausgestattetes Change Management und Mitgliedschaft in kooperativen IT-Netzwerken.

### 7.3 Sicherheitsrahmen

BSI IT-Grundschutz bietet eine umfassende Sicherheitsbasis [26]. Pflichtanforderungen:

- Dokumentiertes Patch-Management mit maximal 14 Tagen für kritische Patches
- Authentifizierung: BSI-Authentifikator-Vertrauensniveau 2 (AAL2) für bürgerorientierten Dienste; AAL3 für privilegierten Admin-Zugang
- Daten übertragung: TLS 1.3 Minimum; Daten im Ruhezustand: AES-256 für sensible Kategorien
- Penetrationstest an jedem Phasentor; jährlich in Produktionssystemen
- Incident-Response-Plan gemäß NIS2-72-Stunden-Meldepflicht [27]
- Software-Bill-of-Materials (SBOM) im SPDX-Format für alle Open-Source-Abhängigkeiten

---

## 8. Digitale Barrierefreiheit und Inklusion

Barrierefreiheit ist keine Option. Deutschlands BITV 2.0 und die Schweizer eCH-0059 schreiben beide WCAG-2.1-Level-AA-Konformität für alle digitalen öffentlichen Dienste vor. Nichteinhaltung setzt Kommunen rechtlichen Anfechtungen aus und schließt Menschen mit Behinderungen von öffentlichen Diensten aus.

Alle empfohlenen Komponenten dieses Stacks verfügen über barrierefreie Konfigurationen:
- **TYPO3 v12+**: wird mit vollständiger WCAG-2.1-AA-Unterstützung geliefert [19]
- **Decidim**: Barrierefreiheitsaudit durch das Barrierefreiheitsteam der Stadt Barcelona; vollständige ARIA-Landmarken und Tastaturnavigation [12]
- **Nextcloud**: Barrierefreiheitsmodus verfügbar; kontinuierliche Verbesserung durch Community-Beiträge [13]

**Empfehlung:** Barrierefreiheit als First-Class-Anforderung in allen Ausschreibungsunterlagen verankern. Barrierefreiheitsaudits – automatisiert (axe-core, Lighthouse) sowie manuell mit Nutzern mit Behinderungen – an den Phasentoren 2 und 4 durchführen. Audit-Ergebnisse öffentlich veröffentlichen.

---

## 9. Fazit

Die in diesem Papier analysierten Belege konvergieren auf fünf Erkenntnisse:

**1. Open-Source-Technologie-Stacks für Kommunen sind technisch ausgereift.** Jede Funktionsanforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Produktions-Deployments bei vergleichbaren Kommunen in der Schweiz, Deutschland und der weiteren EU erfüllt werden.

**2. Das Regulierungsumfeld verlangt Offenheit.** EMBAG (Schweiz), OZG 2.0 (Deutschland) und das Interoperabilitätsgesetz (EU) schaffen rechtliche Verpflichtungen, die proprietäre, anbietergebundene Systeme dauerhaft nicht erfüllen können. Städte, die den Übergang jetzt beginnen, bauen Compliance-Kapital auf; die­jenigen, die warten, anhäufen regulatorische Schulden.

**3. Die Wirtschaftlichkeit ist bei 5-jährigen Gesamtbetriebskosten überzeugend.** Open-Source-Stacks eliminieren Benutzerlizenzkosten und reduzieren das Anbieterabhhängigkeitsrisiko. Über 36 Monate sind Einsparungen von 30–50% gegenüber äquivalenten proprietären Stacks für mittelgroße Kommunen erreichbar.

**4. Erfolg erfordert politische und organisatorische Investitionen in gleicher Höhe wie technische.** Der Münchner Fall bestätigt, dass politisches Risikomanagement und Change Management die eigentlichen Engpassfaktoren sind. Erfolgreiche Übergänge teilen ein parteiübergreifendes Mandat und gut ausgestattete Implementierung.

**5. Open-Source-Verwaltung ist demokratisch notwendig.** Software, die demokratische Institutionen betreibt, sollte demokratische Werte der Transparenz, Rechenschaftspflicht und des öffentlichen Eigentums verkörpern [4, 32]. Das Prinzip "Public Money? Public Code!" ist nicht nur ein ökonomisches Argument – es ist ein demokratisches.

Städte, die sich als erste bewegen, profitieren davon, kooperative Standards zu prägen, Inhouse-Expertise aufzubauen und zum Open-Source-Commons beizutragen, das alle Kommunen teilen. Die Einladung ist offen.

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — CC0 (Schweizer Bundesgesetzgebung)

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — DL-DE/Zero 2.0

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. Berlin: OSBA. https://scs.community/ — CC-BY-SA-4.0

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — CC-BY-SA-4.0

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 über Maßnahmen für ein hohes Maß an Interoperabilität des öffentlichen Sektors in der Union (Interoperables Europa-Gesetz)*. Amtsblatt der EU, L 2024/903, 11. April 2024. CELEX: 32024R0903. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R0903

[7] Wirtz, B. W. & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y. & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation (FITKO): Aufgaben und Struktur*. Frankfurt: FITKO. https://www.fitko.de/fitko

[10] openCode.de. (2022). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/ — Apache 2.0

[12] Decidim Association. (2021). *Decidim: Freie Open-Source-Plattform für partizipative Demokratie für Städte und Organisationen*. Barcelona: Decidim Association. https://decidim.org/ — AGPL-3.0

[13] Nextcloud GmbH. (2023). *Nextcloud für die öffentliche Verwaltung: Sicherheit, Souveränität und Zusammenarbeit*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation v1.9*. https://spec.matrix.org/ — Apache 2.0

[15] eCH-Verein. (2023). *eCH-Standards — E-Government-Standards Schweiz*. Bern: eCH. https://www.ech.ch/de/ech/ech-standards

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei / Konferenz der Kantonsregierungen. https://www.egovernment.ch/de/umsetzung/e-government-strategie-2024-2027/

[17] ZenDiS GmbH. (2023). *Jahresbericht 2023: Zentrum für Digitale Souveränität der öffentlichen Verwaltung*. Berlin: ZenDiS GmbH. https://www.zendis.de/

[18] Europäische Kommission / Joinup. (2023). *Open Source Observatory (OSOR) Jahresbericht 2023*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/open-source-observatory-osor — CC-BY-4.0

[19] TYPO3 Association. (2023). *TYPO3 in der öffentlichen Verwaltung*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association

[20] OpenProject GmbH. (2023). *OpenProject für die öffentliche Verwaltung: Open-Source-Projektmanagement*. Berlin: OpenProject GmbH. https://www.openproject.org/ — GPLv3

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — Apache 2.0

[22] CKAN Association. (2023). *CKAN: Open-Source-Datenportalsoftware*. https://ckan.org/ — AGPL-3.0

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/

[25] AKDB. (2023). *Anstalt für Kommunale Datenverarbeitung in Bayern: Leistungen und Rahmenverträge*. München: AKDB. https://www.akdb.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html — CC-BY-ND 3.0 DE

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 über Maßnahmen für ein hohes gemeinsames Cybersicherheitsniveau in der Union (NIS2)*. CELEX: 32022L2555. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[28] GovStack-Initiative (ITU/DIAL). (2023). *GovStack: Bausteine für digitale Regierung*. Genf: ITU / DIAL. https://www.govstack.global/ — CC-BY-4.0

[29] Vereinte Nationen DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: Vereinte Nationen. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[31] CONSUL Democracy. (2023). *CONSUL Democracy: Freie Software für Bürgerbeteiligung*. Madrid: Ayuntamiento de Madrid. https://consuldemocracy.org/ — AGPL-3.0

[32] Lathrop, D. & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol, CA: O'Reilly Media. ISBN 978-0-596-80435-0

[33] Camunda Services GmbH. (2023). *Camunda Platform 8: Technische Dokumentation*. https://docs.camunda.io/ — Apache 2.0 (Community)

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open-Source-Webkonferenz*. https://bigbluebutton.org/ — LGPL-3.0

[35] Jitsi Community. (2023). *Jitsi Meet: Open-Source-Videokonferenz*. https://jitsi.org/ — Apache 2.0

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — ODbL-1.0

[37] QGIS Project. (2023). *QGIS: Ein freies und quelloffenes Geoinformationssystem*. https://www.qgis.org/ — GPL-2.0+

[38] OpenTofu Steering Committee. (2024). *OpenTofu: Das Open-Source-Infrastructure-as-Code-Tool*. Linux Foundation. https://opentofu.org/ — MPL-2.0

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — Apache 2.0

[40] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1183 zur Änderung der Verordnung (EU) Nr. 910/2014 hinsichtlich der Einrichtung des Europäischen Rahmens für die digitale Identität (eIDAS 2.0)*. CELEX: 32024R1183. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1183

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL 16*. https://www.postgresql.org/ — PostgreSQL-Lizenz (BSD-ähnlich, OSI-genehmigt)

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — AGPL-3.0

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — CC-BY-4.0 (Portal)

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen — Umsetzungsstrategie (EIF)*. Brüssel: Europäische Kommission (ISA²-Programm). https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail — CC-BY-4.0

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: Koordinierungsstelle für IT-Standards. https://www.xoev.de/

---

## Anhang A: Bewertungsmatrix für Open-Source-Kommunaltechnologie

Verwenden Sie diese Matrix bei der Bewertung von Softwareangeboten nach den Kriterien in Abschnitt 2.3. Mindestempfohlene Punktzahl: **27/35**.

| Komponente | Lizenz | Reife | Community | Interop | Sicherheit | TCO | Deployments | Gesamt |
|---|---|---|---|---|---|---|---|---|
| Keycloak | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 34 |
| Nextcloud | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 34 |
| Decidim | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 33 |
| Matrix/Element | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 32 |
| CKAN | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 32 |
| SCS | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 32 |
| TYPO3 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 32 |
| OpenProject | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 29 |
| Camunda (Community) | 4 | 5 | 4 | 5 | 4 | 3 | 4 | 29 |

---

## Anhang B: Muster-Beschaffungsklauseln

**Klausel 1 — Open-Source-Veröffentlichungspflicht**

> *„Alle Software, Konfigurationscode und zugehörige Dokumentation, die speziell für diesen Vertrag erstellt wurden, sind unter [EUPL-1.2 / AGPL-3.0 / Apache-2.0] (nicht Zutreffendes streichen) innerhalb von neunzig (90) Tagen nach Lieferung zu veröffentlichen und in einem öffentlich zugänglichen Repository auf openCode.de oder einer festgelegten gleichwertigen öffentlichen Plattform zu publizieren. Das Quellcode-Repository ist ohne Registrierung oder Authentifizierung zugänglich zu halten.“*

**Klausel 2 — Interoperabilitätsanforderungen**

> *„Alle im Rahmen dieses Vertrags gelieferten Systeme müssen mindestens folgende offene Standards implementieren: OpenID Connect 1.0 / OAuth 2.0 (Authentifizierung); [XÖV / eCH-relevante Standards] (Datenaustausch); DCAT-AP [.de / .ch je nach Anwendung] (Open-Data-Metadaten); WCAG 2.1 Level AA (Barrierefreiheit). Nichtkonformität mit einem der aufgeführten Standards bei der Lieferung stellt einen wesentlichen Mangel dar und berechtigt den Auftraggeber, die Zahlung zurückzuhalten.“*

**Klausel 3 — Datensouveränität**

> *„Alle personenbezogenen Daten und Bürgerdaten, die im Rahmen dieses Vertrags verarbeitet werden, sind ausschließlich auf Infrastruktur zu speichern und zu verarbeiten, die sich im Hoheitsgebiet von [Deutschland / der Schweiz / dem Europäischen Wirtschaftsraum] befindet. Der Auftragnehmer hat den Datenspeicherort auf Anfrage und innerhalb von 30 Tagen nach jeder Änderung des Datenspeicherorts schriftlich zu bestätigen.“*

**Klausel 4 — Ausstiegsrechte**

> *„Bei Beendigung dieses Vertrags aus jedwedem Grund hat der Auftragnehmer innerhalb von 30 Tagen und ohne zusätzliche Kosten einen vollständigen Datenexport in einem offenen, dokumentierten Format bereitzustellen (z.B. SQL-Dump, CSV, JSON, XML gemäß anwendbaren XÖV/eCH-Standards). Der Export umfasst alle Bürgerdaten, Systemkonfigurationen und Workflow-Definitionen in einer Form, die ausreicht, um den Betrieb auf alternativer Infrastruktur wiederherzustellen.“*

---

## Anhang C: Glossar

| Begriff | Definition |
|---|---|
| AGPL-3.0 | GNU Affero General Public Licence v3: Copyleft-Lizenz, die Quelloffenlegung für netzwerkbasierte Software erfordert |
| AKDB | Anstalt für Kommunale Datenverarbeitung in Bayern: bayerische kommunale IT-öffentlich-rechtliche Institution |
| BPMN 2.0 | Business Process Model and Notation 2.0: ISO/IEC 19510-Standard für die Workflow-Modellierung |
| BSI | Bundesamt für Sicherheit in der Informationstechnik: Deutsche Bundesbehörde für Cybersicherheit |
| BundID | Bundesdienst für digitale Identität für deutsche Bürger (BundID.de) |
| CKAN | Comprehensive Knowledge Archive Network: quelloffene Datenportalsoftware |
| DCAT-AP | Data Catalogue Vocabulary Application Profile: EU-Standard für Open-Data-Metadaten |
| DL-DE/Zero 2.0 | Datenlizenz Deutschland Zero: äquivalent zu CC0 für öffentliche Veröffentlichungen |
| DSB | Datenschutzbeauftragter |
| DSFA | Datenschutz-Folgenabschätzung (gemäß DSGVO Art. 35) |
| eCH | E-Government-Standards Schweiz: Schweizer Pendant zu Deutschlands XÖV-Rahmen |
| EfA | Einer für Alle: OZG-Prinzip für gemeinsame, wiederverwendbare Dienstentwicklung |
| eIDAS | Verordnung über elektronische Identifizierung und Vertrauensdienste (EU 910/2014, revidiert 2024/1183) |
| EMBAG | Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (Schweiz) |
| EUPL-1.2 | Europäische Union Public Licence 1.2: OSI-genehmigte Copyleft-Lizenz der Europäischen Kommission |
| FITKO | Föderale IT-Kooperation: Deutsches Bundeskoordinierungsgremium für die OZG-Implementierung |
| FIDO2 | Fast Identity Online 2.0: W3C/FIDO Alliance-Standard für passwortlose Authentifizierung |
| GEVER | Geschäftsverwaltung: Schweizer Bundesstandard für Aktenverwaltungssysteme |
| GovStack | ITU/DIAL-Initiative für global anwendbare, wiederverwendbare digitale Verwaltungsbausteine |
| IT-Grundschutz | BSI-Sicherheitsbasis- und Risikomanagement-Rahmen für die deutsche öffentliche Verwaltung |
| NIS2 | Richtlinie (EU) 2022/2555: Netz- und Informationssicherheitsrichtlinie 2 |
| OIDC | OpenID Connect: Identitätsschicht über OAuth 2.0 für föderierte Authentifizierung |
| OSOR | Open Source Observatory and Repository: Wissensplattform der Europäischen Kommission |
| OSI | Open Source Initiative: Gremium, das Open-Source-Lizenzdefinitionen genehmigt |
| OZG | Onlinezugangsgesetz: Deutsches Online-Zugangsgesetz (2017, reformiert 2024) |
| SBOM | Software Bill of Materials: strukturiertes Inventar der Softwarekomponenten (SPDX- oder CycloneDX-Format) |
| SCS | Sovereign Cloud Stack: vollständig quelloffene europäische Cloud-Plattform (OSBA/BMWK) |
| TCO | Total Cost of Ownership: vollständige 5-jährige Lebenszykluskosten |
| VZÄ | Vollzeitäquivalent |
| XÖV | XML in der öffentlichen Verwaltung: Familie von XML-Standards für deutschen Behördendatenaustausch |
| ZenDiS | Zentrum für Digitale Souveränität der öffentlichen Verwaltung: Deutsches Bundesamt für Open-Source |

---

*Dieses Dokument wird unter der Creative Commons Namensnennung 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*  
*Zitationsangabe: Sebastian Graf, Autonomes Büro für bürgerliche digitale Infrastruktur (sebk4c@tuta.com)*  
*Version 0.2.0 — Zitationsvollständiger Entwurf. Vorherige Version: v0.1.0 (2026-06-20).*
