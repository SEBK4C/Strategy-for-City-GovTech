---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.1.0"
status: "Erster strukturierter Entwurf"
date: "2026-06-20"
language: "de"
source-of-truth: false
translation-source: "Doc/en/sovereign-by-design-v0.1.0.md"
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
  - Civic Technology
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur
**Korrespondenz:** sebk4c@tuta.com
**Version:** 0.1.0 — Erster strukturierter Entwurf
**Datum:** 2026-06-20
**Sprachen:** Englisch (Primärquelle) · Deutsch
**SPDX-License-Identifier:** CC-BY-4.0

---

## Zusammenfassung

Kommunalverwaltungen sind die dem Bürger nächste Ebene der demokratischen Verwaltung, stehen jedoch vor einem akuten strukturellen Spannungsfeld: Die digitalen Werkzeuge, auf die sie angewiesen sind, werden zunehmend proprietär, an Anbieter gebunden und an privatwirtschaftlichen Interessen ausgerichtet. Dieses Papier präsentiert eine umfassende Strategie zur Implementierung eines zukunftsweisenden, Open-Source-basierten Verwaltungstechnologie-Stacks in Kommunalverwaltungen. Auf Grundlage exemplarischer Praktiken aus der Schweizer Bundesverwaltung (EMBAG-Gesetzgebung), Deutschlands OZG-Reformprogramm und der Sovereign-Cloud-Stack-Initiative sowie der weiteren europäischen Gemeinschaft für souveräne Technologie leiten wir einen auf Grundprinzipien basierenden Implementierungsfahrplan, einen Stakeholder-Rahmen und eine Beschaffungsstrategie ab. Wir bewerten die zentralen Technologiekomponenten — Identitätsverwaltung, Dokumentenmanagement, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Publikation und Cloud-Infrastruktur — anhand der Kriterien digitale Souveränität, Interoperabilität, Gesamtbetriebskosten (Total Cost of Ownership) und bürgerliche Ausrichtung. Wir gelangen zu dem Schluss, dass Open-Source-Technologie-Stacks für Kommunalverwaltungen nicht nur technisch realisierbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Rechtssystemen gesetzlich vorgeschrieben sind. Das Papier bietet einen phasenweisen 36-Monats-Implementierungsfahrplan mit konkreten Beschaffungsempfehlungen für Stadtverwalter, gewählte Vertreter, IT-Teams und zivilgesellschaftliche Stakeholder.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, Civic Technology

---

## 1. Einleitung

Die digitale Transformation der kommunalen Verwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen; Regulatoren fordern Interoperabilität und Datenschutz; und der Kostendruck verlangt nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch befinden sich die meisten Kommunalverwaltungen weltweit in einem Kreislauf proprietärer Anbieterabhängigkeit, teurer Lizenzverträge und fragmentierter Systeme, die gute Verwaltungsführung eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut dokumentiert: Vendor-Lock-in erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate erschweren den behördenübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Quellcodes verhindern unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Budgets, die andernfalls für die Dienstleistungserbringung genutzt werden könnten [3, 5]. Am grundlegendsten entsteht ein struktureller Interessenkonflikt zwischen dem öffentlichen Interesse und privatwirtschaftlichen Interessen, wenn die Software demokratischer Institutionen von privaten Akteuren besessen und kontrolliert wird [4].

Ein anderer Weg ist möglich und erprobt. Die Schweizer EMBAG-Gesetzgebung aus dem Jahr 2023 (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundesbehördensoftware standardmäßig als Open Source veröffentlicht wird [1]. Deutschlands OZG-Reformprogramm, der Sovereign Cloud Stack und die OpenDesk-Initiative repräsentieren das ambitionierteste Open-Source-Regierungstechnologieprogramm in Europa [2, 3, 42]. Die Kampagne der Free Software Foundation Europe "Public Money? Public Code!", die mittlerweile von über 200 Organisationen in 30 Ländern unterstützt wird, formuliert das demokratische Prinzip auf dem Spiel: Software, die mit öffentlichen Geldern finanziert wird, sollte der Öffentlichkeit zur Verfügung stehen [4].

Dieses Papier fasst diese Entwicklungen zu einer praktischen Strategie für Kommunalverwaltungen zusammen. Es richtet sich an alle relevanten Stakeholder — Stadtverwalter, gewählte Vertreter, IT-Teams des öffentlichen Sektors, Beschaffungsämter, Zivilgesellschaftsgruppen, Open-Source-Gemeinschaften und souveräne Technologieanbieter — und stellt die Evidenzbasis, die Technologiebewertung und den Implementierungsfahrplan bereit, der für den Übergang benötigt wird.

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und lokale Regierungsbehörden, einschließlich Gemeinden, Kommunen, Städte und gleichwertige Strukturen in Schweizer Kantonen. Die Strategie ist so konzipiert, dass sie von kleinen Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (500.000+) skaliert werden kann, mit entsprechender Anpassung.

*Open-Source-Technologie-Stack* bezeichnet Softwarekomponenten, die unter OSI-genehmigten Lizenzen lizenziert sind und auf einer Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder ohne unverhältnismäßige Kosten oder Reibungsverluste migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer Regierung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen, einschließlich des Rechts, Software zu prüfen, zu ändern, zu auditieren und zu migrieren, ohne von einem einzigen Anbieter abhängig zu sein [3].

### 1.2 Forschungsfragen

1. Wie sieht ein zukunftsweisender Open-Source-Technologie-Stack für Kommunalverwaltungen im Jahr 2026 aus?
2. Welche Lehren lassen sich aus der Schweizer, deutschen und europäischen Gemeinschaft für souveräne Technologie ziehen?
3. Was ist der optimale phasenweise Implementierungsweg für eine Kommunalverwaltung mit 50.000–500.000 Einwohnern?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden, um die Erfolgswahrscheinlichkeit zu maximieren?

---

## 2. Methodik

Dieses Papier verwendet ein mehrere Methoden kombinierendes Forschungsdesign:

**Systematische Literaturrecherche** von Peer-Review-Publikationen, grauer Literatur und Politikdokumenten, die zwischen 2010 und 2026 veröffentlicht wurden und die Bereiche E-Government-Theorie, digitale Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunale Digitaltransformation abdecken.

**Vergleichende Politikanalyse** von Technologiegesetzgebung und -strategien aus der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, Deutsche Verwaltungscloud-Strategie) und der Europäischen Union (Interoperable Europe Act 2024, EU Open Source Strategy 2020–2023).

**Technologie-Stack-Bewertung** unter Verwendung einer strukturierten Bewertungsmatrix, die jede Komponente nach folgenden Kriterien bewertet: (a) Offenheit der Lizenz, (b) Reife des Einsatzes, (c) Gesundheit der Gemeinschaft, (d) Einhaltung von Interoperabilitätsstandards, (e) Sicherheitslage, (f) Gesamtbetriebskosten und (g) bestehende Einsätze im öffentlichen Sektor.

**Stakeholder-Analyse** zur Erfassung der Interessen, des Einflusses und der Einbindungsbedarfe jeder Stakeholder-Gruppe im kommunalen Digitaltransformationsprozess.

Die Literaturrecherche ist selbstverbessernd konzipiert: Das Quellenregister (`Mem/source-registry.md`) und der Literaturrecherchestatus (`Mem/literature-review-state.md`) sind versionierte Dokumente, die in einem regelmäßigen Rhythmus aktualisiert werden. Das Skript `Scripts/update_literature_review.py` bietet strukturierte Anregungen zur vierteljährlichen Überprüfung und Verbesserung.

### 2.1 Einschlusskriterien

Quellen wurden berücksichtigt, wenn sie: (a) Open-Source-Software in der öffentlichen Verwaltung behandeln; (b) Strategien zur digitalen Transformation von Behörden abdecken; (c) den europäischen, Schweizer oder deutschen Rechtskontext betreffen; oder (d) Primärdaten zu kommunalen Technologieimplementierungen bereitstellen. Vor 2010 veröffentlichte Quellen wurden nur berücksichtigt, wenn sie grundlegende theoretische Rahmenbedingungen etablieren.

### 2.2 Einschränkungen

Dieses Papier ist ein erster strukturierter Entwurf (v0.1.0). Einige Zitate erfordern eine Überprüfung anhand primärer Quellen, was im Quellenregister vermerkt ist. Die Bewertungen des Technologie-Stacks spiegeln den Stand der öffentlich verfügbaren Informationen zum Stand Juni 2026 wider. Implementierungskostenschätzungen sind indikativ und müssen anhand lokaler Beschaffungsbedingungen validiert werden.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Government

Die akademische Literatur zum E-Government hat sich durch vier breite Phasen entwickelt [30]. Die erste Generation des E-Government (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Erstellung von Behördenwebsites [29]. Die zweite Generation (2005–2012) betonte die Online-Dienstleistungserbringung, Bürgerportale und die Back-Office-Integration [7]. Die dritte Generation (2012–2020) führte Open Data, Partizipationsplattformen und Mobile-First-Servicegestaltung ein [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und die Souveränitätswende geprägt — die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstverwaltung ist [45].

Das ganzheitliche E-Government-Reifegradmodell von Wirtz und Weyerer identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Kommunalverwaltungen in der Schweiz und Deutschland schneiden in diesen Dimensionen unterschiedlich ab; technische Infrastruktur und Prozessqualität hinken in den meisten Rechtssystemen den Erwartungen der Bürger hinterher, während das regulatorische Umfeld Transparenz und Interoperabilität zunehmend vorschreibt [1, 2, 45].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept der digitalen Souveränität — die Fähigkeit öffentlicher Institutionen, unabhängige, überprüfbare Entscheidungen über ihre digitale Infrastruktur zu treffen — hat sich im europäischen Kontext von einem akademischen Konzept zu einem politischen Gebot entwickelt [3, 5]. Die EU Open Source Strategy 2020–2023 etablierte "Teilen und Wiederverwenden" als Kernprinzip und verpflichtet europäische Institutionen, bei der Technologiebeschaffung Open-Source-Lösungen zu bevorzugen [5]. Der Interoperable Europe Act 2024 schafft verbindliche Verpflichtungen für die grenzüberschreitende Interoperabilität in öffentlichen Verwaltungen [6].

Deutschlands Sovereign Cloud Stack (SCS), entwickelt von der Open Source Business Alliance (OSBA) und teilweise vom Bundesministerium für Wirtschaft und Klimaschutz (BMWK) finanziert, stellt die konkreteste Verwirklichung digitaler Souveränität in der Cloud-Infrastruktur dar. SCS bietet eine vollständig quelloffene, selbst hostbare Cloud-Plattform, die es öffentlichen Verwaltungen ermöglicht, technisch und rechtlich souveräne Infrastruktur zu betreiben [3]. Ab 2026 unterstützt SCS mehrere deutsche Länder-Cloud-Umgebungen und ist in die gemeinsame Infrastruktur der govdigital eG integriert [23].

Der Schweizer Ansatz unterscheidet sich institutionell, konvergiert aber auf dieselben Grundsätze. Das EMBAG-Gesetz, das am 1. Januar 2024 in Kraft trat, schreibt vor, dass alle mit öffentlichen Mitteln entwickelten Bundessoftware als Open Source veröffentlicht werden, sofern keine zwingenden Sicherheitsgründe dagegen sprechen [1]. Das Gesetz stellt die Schweiz zu den fortschrittlichsten Open-Source-mandatierenden Rechtsordnungen der Welt.

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 verabschiedet und 2024 grundlegend reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalverwaltungen, ihre Verwaltungsleistungen online anzubieten [2]. Die OZG-2.0-Reform behebt Schwächen der ersten Generation — darunter fragmentierte Umsetzung, schlechte Interoperabilität und inkonsistente Nutzererfahrung — durch das "Once Only"-Prinzip, den "Einer für Alle"-Ansatz (EfA) zur gemeinsamen Serviceentwicklung und eine föderale Plattformarchitektur mit BundID und FITKO im Zentrum [9, 10].

Die openCode.de-Plattform, 2022 gestartet, bietet ein zentrales Repository für behördliche Open-Source-Software, das Kommunen die Entdeckung, Wiederverwendung und Mitwirkung an gemeinsamen Lösungen ermöglicht [10]. Dataport AöR und AKDB repräsentieren das genossenschaftliche Modell der IT-Bereitstellung im öffentlichen Sektor, das das OZG-Ökosystem gestärkt hat [24].

### 3.4 Schweizer kantonale und föderale Digitaldienste

Die föderale Struktur der Schweiz schafft sowohl Herausforderungen als auch Chancen für die kommunale Digitaltransformation. Zu den wichtigsten digitalen Infrastrukturen der Schweiz gehören:

- **Fedlex** (fedlex.admin.ch): die offizielle Plattform für das Schweizer Bundesrecht, auf offenen Standards aufgebaut und maschinenlesbare Rechtsdaten bereitstellend [1].
- **opendata.swiss**: das nationale Portal für offene Behördendaten, auf CKAN aufgebaut und Tausende von Datensätzen aus Bundes-, Kantons- und Kommunalbehörden katalogisierend [44].
- **GEVER**: das standardisierte Geschäftsverwaltungssystem für die Bundesverwaltung, das als Vorlage für kantonale und kommunale Implementierungen dient [43].
- **Schweizer E-ID**: ein dezentrales, die Privatsphäre schützendes digitales Identitätssystem (nach der Reform von 2021, gestützt auf das E-ID-Gesetz) [51].

Die E-Government-Strategie Schweiz 2024–2027, gemeinsam verfasst vom Bundesrat und der Konferenz der Kantonsregierungen, legt einen kooperativen Rahmen für digitale Dienste fest, der ausdrücklich offene Standards und Interoperabilität vorschreibt [16].

Die eCH-Standardisierung (E-Government Standards Switzerland) stellt das schweizerische Äquivalent der deutschen XÖV-Familie dar: eine Sammlung von XML- und Schnittstellenstandards für den behördenübergreifenden Datenaustausch in der Schweiz [48].

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016) ist eine Partizipationsdemokratieplattform, die von über 400 Organisationen in 40 Ländern genutzt wird, darunter die Städte Barcelona, Helsinki und der Schweizer Kanton Schaffhausen [12]. Ihr Governance-Modell — eine Mehrparteienstakeholder-Vereinigung mit einem veröffentlichten Sozialvertrag — ist selbst ein Modell für Open-Source-Souveränität.

**CONSUL Democracy** (Madrid, 2015) ist ein weiteres ausgereiftes Open-Source-Partizipationssystem, das in mehr als 40 Ländern eingesetzt wird und sich besonders für Bürgervorschläge, partizipative Haushalte und kommunale Debatten eignet [47].

**Matrix/Element** bietet ein offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll, das von europäischen öffentlichen Verwaltungen zunehmend übernommen wird. Der deutsche föderale BundesMessenger und das französische Tchap betreiben beide auf Matrix [14].

**Nextcloud** (Stuttgart, 2016) ist die am weitesten verbreitete Open-Source-Dateisynchronisierungs- und Kollaborationsplattform in der europäischen öffentlichen Verwaltung, verwendet von Tausenden deutschen Gemeinden, der Schweizer Bundesverwaltung und Dutzenden EU-Institutionen [13].

**OpenDesk**, 2023 von der deutschen Bundesregierung gestartet und von der ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung) verwaltet, ist eine kuratierte Open-Source-Desktop- und Kollaborationssuite, die um Nextcloud, Cryptpad, OpenProject, Jitsi und Element herum aufgebaut ist. Es stellt die erste staatlich kuratierte Open-Source-Arbeitsplatzsuite in großem Maßstab dar [42, 49].

**GovStack** (ITU/DIAL-Initiative, 2021) definiert technologieneutrale "Building Blocks" für staatliche digitale Dienste — wiederverwendbare, interoperable Softwarekomponenten, die von jedem Land oder jeder Behörde eingesetzt werden können. GovStack ergänzt die europäischen Souveränitätsinitiativen durch einen globalen Referenzrahmen [53].

### 3.6 Lücken in der Literatur

1. **Gesamtbetriebskostenstudien**, die Open-Source- und proprietäre kommunale Stacks vergleichen, sind spärlich und methodisch inkonsistent. Die meisten verfügbaren Studien sind von Anbietern in Auftrag gegeben.
2. **Longitudinale Implementierungsdaten** aus Städten, die vollständige Open-Source-Übergänge abgeschlossen haben, sind begrenzt. Das LiMux-Projekt der Stadt München (2003–2017) wird häufig als mahnendes Beispiel zitiert; Post-Mortems führen das Scheitern primär auf politische, nicht technische Faktoren zurück [30].
3. **Perspektiven kleiner Gemeinden** sind unterrepräsentiert; die meisten Fallstudien konzentrieren sich auf Großstädte oder Bundesbehörden.
4. **Nutzerforschung zur Benutzererfahrung**, die die Bürgerzufriedenheit mit Open-Source- und proprietären kommunalen Digitaldiensten vergleicht, fehlt fast vollständig.

Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse und den Verbesserungsfahrplan.

---

## 4. Technologie-Stack-Analyse

Ein kommunaler Technologie-Stack kann in neun funktionale Schichten unterteilt werden. Die folgende Analyse bewertet die führenden Open-Source-Optionen für jede Schicht anhand der in Abschnitt 2 definierten Bewertungskriterien.

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Bürger und Mitarbeiter authentifizieren; Identität über Dienste hinweg föderieren; Single Sign-On (SSO) implementieren.

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die de-facto Open-Source-Identitäts- und Zugriffsverwaltungsplattform (IAM) für die öffentliche Verwaltung. Es implementiert OpenID Connect, OAuth 2.0 und SAML 2.0, was eine Föderierung mit nationalen Identitätssystemen (BundID in Deutschland, E-ID in der Schweiz) ermöglicht. Es wird von zahlreichen europäischen Regierungen eingesetzt, darunter EU-Institutionen, deutsche Bundesländer und Schweizer Kantone.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Reife des Einsatzes | 5 | Produktionserprobt, 10+ Jahre |
| Gesundheit der Gemeinschaft | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheitslage | 5 | CVE-reaktionsschnell, weit geprüft |
| Gesamtbetriebskosten | 4 | Keine Lizenzkosten; Betriebsexpertise erforderlich |
| Einsätze im öffentlichen Sektor | 5 | Weit verbreitet in EU-Behörden |

### 4.2 Dokumentenmanagement und Aktenführung

**Funktion:** Offizielle Akten speichern, abrufen, klassifizieren und aufbewahren; GEVER-konforme Workflows verwalten.

**Empfohlene Komponenten: Nextcloud** (kollaboratives Dateimanagement) + **OpenProject** (Projekt- und Aktenverknüpfung) [13, 20]

Für Kommunen, die vollständige GEVER-Konformität (Schweiz) benötigen, bieten kantonale GEVER-Lösungen (CMI, Fabasoft Community) die Konformitätsschicht mit Nextcloud als kollaborativem Frontend. Für deutsche Kommunen bieten BayernPortal der AKDB und Dataport-Komponenten die gleichwertige Funktionalität.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 (Nextcloud) |
| Reife des Einsatzes | 5 | 400.000+ Organisationen |
| Gesundheit der Gemeinschaft | 5 | Nextcloud GmbH + Gemeinschaft |
| Interoperabilität | 4 | WebDAV, CalDAV, CardDAV, CMIS |
| Sicherheitslage | 5 | ISO 27001-zertifiziertes Angebot |
| Gesamtbetriebskosten | 5 | Keine Platzlizenz (Community) |
| Einsätze im öffentlichen Sektor | 5 | Schweizer Bund, deutsche Länder |

### 4.3 Workflow-Automatisierung und Geschäftsprozessmanagement

**Funktion:** Verwaltungs-Workflows automatisieren; BPMN-Prozesse modellieren, ausführen und überwachen.

**Empfohlene Komponente: Camunda Platform 8 Community** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe mehrstufige Verwaltungsprozesse und XÖV-Datenstandardintegration [46]. **Flowable** (Apache 2.0) ist eine schlanke Alternative, wenn das Dual-Lizenzmodell von Camunda Beschaffungskomplikationen verursacht.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 4 | Community: Apache 2.0; Enterprise: proprietär |
| Reife des Einsatzes | 5 | Produktionserprobt |
| Gesundheit der Gemeinschaft | 4 | Aktiv; Enterprise-Ebene finanziert Entwicklung |
| Interoperabilität | 5 | BPMN 2.0, REST API, eventgesteuert |
| Sicherheitslage | 4 | Aktiv gepflegt |
| Gesamtbetriebskosten | 3 | Community kostenlos; Skalierung ggf. Enterprise erforderlich |
| Einsätze im öffentlichen Sektor | 4 | Mehrere deutsche Bundesländer |

### 4.4 Bürgerbeteiligung

**Funktion:** Beratung, partizipatives Budgetieren, Initiativensammlung, Deliberationsplattformen.

**Empfohlene Komponente: Decidim** [12]

Decidim ist die ausgereifteste und am weitesten verbreitete Open-Source-Partizipationsplattform weltweit. Die Nutzung durch Barcelona, Helsinki, den Kanton Schaffhausen und die Stadt New York validiert sie in verschiedenen regulatorischen und sprachlichen Kontexten. Die Decidim Association bietet Governance, einen Sozialvertrag und eine globale Praxisgemeinschaft.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Reife des Einsatzes | 5 | 400+ Einsätze weltweit |
| Gesundheit der Gemeinschaft | 5 | Aktive Vereinigung und Gemeinschaft |
| Interoperabilität | 4 | REST API, Webhooks |
| Sicherheitslage | 4 | Aktiv gepflegt |
| Gesamtbetriebskosten | 5 | Keine Lizenzkosten |
| Einsätze im öffentlichen Sektor | 5 | Städte, Kantone, Bundesbehörden |

**Alternative:** CONSUL Democracy (Madrid), ebenfalls AGPL-3.0, stark in der spanischsprachigen Welt und einigen europäischen Städten [47].

### 4.5 Kommunikation und Zusammenarbeit

**Funktion:** Interne Nachrichten, Videokonferenzen, E-Mail, Kalender; sichere behördenübergreifende Kommunikation.

**Empfohlene Komponenten:**
- **Matrix/Element** für Nachrichten und behördenübergreifende sichere Kommunikation [14]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Nextcloud Talk** für integrierte Teamkommunikation

Der deutsche föderale BundesMessenger (auf Matrix aufgebaut) bietet eine Referenzimplementierung, die auf kommunale Kontexte anwendbar ist.

| Komponente | Lizenz | Reife | Hauptvorteil |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Produktion | E2E-Verschlüsselung, Föderierung |
| Jitsi Meet | Apache 2.0 | Produktion | Browserbasiert, selbst hostbar |
| BigBlueButton | LGPL-3.0 | Produktion | Fokus auf Ratssitzungen |
| Nextcloud Talk | AGPL-3.0 | Produktion | Integriert mit Dateiverwaltung |

### 4.6 Open-Data-Publikation

**Funktion:** Maschinenlesbare Datensätze veröffentlichen; Daten katalogisieren; API-Zugang bereitstellen; PSI-/Open-Data-Richtlinien einhalten.

**Empfohlene Komponente: CKAN** [22]

CKAN ist die weltweit führende Open-Source-Software für Open-Data-Portale. Sie betreibt opendata.swiss, data.gov, data.gov.uk und Dutzende nationaler und kommunaler Open-Data-Portale. Die Plugin-Architektur ermöglicht die Integration mit DCAT-AP-, DCAT-AP.de- und OGD-Schweiz-Metadatenstandards sowie die Ernte aus übergeordneten Katalogen.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | AGPL-3.0 |
| Reife des Einsatzes | 5 | 10+ Jahre Produktionseinsatz |
| Gesundheit der Gemeinschaft | 4 | CKAN Association; aktiv |
| Interoperabilität | 5 | DCAT-AP, OAI-PMH, SPARQL |
| Sicherheitslage | 4 | Aktiv gepflegt |
| Gesamtbetriebskosten | 4 | Keine Lizenzkosten; Betriebsaufwand |
| Einsätze im öffentlichen Sektor | 5 | Schweiz, Deutschland, EU |

### 4.7 Geografische Informationssysteme

**Funktion:** Kartenbasierte Bürgerdienste; Stadtplanung; Geodatenpublikation.

**Empfohlene Komponenten:**
- **QGIS** (Desktop/Server) für die Bearbeitung und Analyse räumlicher Daten [37]
- **GeoServer** (GeoTools) für die OGC-konforme Publikation räumlicher Daten
- **OpenStreetMap** als kartografische Basisschicht [36]

Die Schweizer swisstopo und Deutschlands BKG (Bundesamt für Kartographie und Geodäsie) stellen offene, hochwertige Behörden-Basiskartendaten zur Verfügung, die mit diesem Stack kompatibel sind.

### 4.8 Öffentliche Website und Content-Management

**Funktion:** Öffentliche Website; Neuigkeiten und Ankündigungen; Dienstleistungsverzeichnis.

**Empfohlene Komponenten:**
- **TYPO3** (deutschsprachige Welt): dominierend in der schweizerischen und deutschen öffentlichen Verwaltung; die TYPO3 Association bietet Langzeitsupport und Erweiterungen für den öffentlichen Sektor [19]
- **Drupal**: starke internationale Erfolgsbilanz; von der Europäischen Kommission verwendet

Beide Systeme unterstützen Barrierefreiheitsstandards (WCAG 2.1 AA / BITV 2.0), Mehrsprachigkeit und Integration mit Open-Data-Katalogen.

### 4.9 Cloud-Infrastruktur und Hosting

**Funktion:** Compute, Speicher, Netzwerk, Container-Orchestrierung; digitale Souveränität auf Infrastrukturebene.

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

SCS ist die strategisch wichtigste Infrastrukturwahl für europäische Kommunen. Er bietet einen vollständig quelloffenen Cloud-Stack (OpenStack + Kubernetes + Ceph), der selbst betrieben, von einer Genossenschaft (govdigital eG) betrieben oder von zertifizierten SCS-Cloud-Betreibern eingesetzt werden kann.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 / vollständig offen |
| Reife des Einsatzes | 4 | Produktionseinsatz in mehreren Ländern |
| Gesundheit der Gemeinschaft | 5 | OSBA-gestützt, wachsend |
| Interoperabilität | 5 | Offene APIs, OCI-konform |
| Sicherheitslage | 5 | BSI IT-Grundschutz-kompatibel |
| Gesamtbetriebskosten | 4 | Keine Lizenz; Infrastrukturkosten |
| Einsätze im öffentlichen Sektor | 4 | Deutsche Bundesländer, wachsend |

**Für Kommunen ohne eigene Cloud-Betriebskapazität:** zertifizierte SCS-Hoster (z.B. plusserver, OSISM) verwenden, die verwaltetes SCS mit vollständigen Datensouveränitätsgarantien anbieten.

### 4.10 Referenzarchitektur

```
+-------------------------------------------------------------+
|                  BUERGER-KONTAKTPUNKTE                     |
|        TYPO3/Drupal . Decidim . CKAN . Nextcloud           |
+-------------------------------------------------------------+
|                   DIENSTLEISTUNGSSCHICHT                   |
|   Camunda Workflows . XOeV-Formulare . GeoServer . QGIS   |
+-------------------------------------------------------------+
|                   KOLLABORATIONSSCHICHT                    |
|   Nextcloud . Matrix/Element . Jitsi . OpenProject         |
+-------------------------------------------------------------+
|                    IDENTITAETSSCHICHT                      |
|          Keycloak <-> BundID / Schweizer E-ID              |
+-------------------------------------------------------------+
|                  INFRASTRUKTURSCHICHT                      |
|  Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph    |
+-------------------------------------------------------------+
```

Alle Schichten kommunizieren über offene APIs. Die Container-Orchestrierung übernimmt Kubernetes [39]; die relationale Persistenz PostgreSQL [41], beide auf dem Sovereign Cloud Stack laufend. Der Datenaustausch erfolgt über XÖV-Standards (Deutschland) [46] oder eCH-Standards (Schweiz) [48]. Die Sicherheit wird durch BSI IT-Grundschutz (Deutschland) [26] oder das Schweizer ISDS-Framework geregelt.

---

## 5. Implementierungsfahrplan

Die Implementierung ist als 36-monatiges, fünfphasiges Programm strukturiert. Jede Phase hat definierte Liefergegenstände, Erfolgskriterien und Entscheidungsgateways.

### Phase 0: Grundlage (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand bewerten, Koalition aufbauen.

**Liefergegenstände:**
- Lenkungsausschuss für die digitale Transformation etabliert (Stadtführung + IT + Zivilgesellschaft)
- Technologie-Ist-Analyse abgeschlossen
- Stakeholder-Einbindungsplan verabschiedet
- Beschaffungsrahmen etabliert (siehe Abschnitt 6)
- Absichtserklärung mit genossenschaftlichem IT-Anbieter (Dataport, AKDB, govdigital oder gleichwertig)

**Erfolgskriterien:**
- Politisches Mandat gesichert (Gemeinderatsbeschluss oder Exekutiventscheidung)
- Budgetrahmen genehmigt (indikativ: 200.000–500.000 EUR für Phase 0–1, je nach Stadtgröße)
- Projektleitung ernannt

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die Grundschichten aufbauen, auf denen alles andere aufbaut.

**Liefergegenstände:**
- Sovereign-Cloud-Stack-Umgebung in Betrieb (eigen oder gehostet)
- Keycloak-Identity-Provider eingerichtet und mit nationalem Identitätssystem föderiert
- Nextcloud-Basis für interne Zusammenarbeit eingerichtet
- Matrix/Element-Messaging für Mitarbeiter
- BSI-IT-Grundschutz-Basisdokumentation abgeschlossen

**Erfolgskriterien:**
- 100% der IT-Mitarbeiter können sich über Keycloak-SSO authentifizieren
- Dateispeicher von proprietärer Cloud auf Nextcloud migriert
- Grundlegende verschlüsselte Nachrichtenübermittlung in Betrieb
- Sicherheitsbasis dokumentiert und genehmigt

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die ersten fünf bürgerorientierten Dienste auf offener Infrastruktur migrieren oder aufbauen.

**Liefergegenstände:**
- Fünf Verwaltungsdienstleistungen mit dem höchsten Volumen auf Camunda/XÖV-Stack eingerichtet
- TYPO3- oder Drupal-CMS-Migration abgeschlossen
- Open-Data-Portal (CKAN) mit ersten 20 Datensätzen gestartet
- Decidim-Instanz für den ersten partizipativen Prozess eingerichtet

**Erfolgskriterien:**
- 80% des angestrebten Dienstleistungsvolumens über das neue System abgewickelt
- Keine Regression bei der Dienstverfügbarkeit gegenüber der Basis
- Erste Open-Data-Publikation live

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Dienstleistungsabdeckung auf 80% der Transaktionen ausweiten.

**Liefergegenstände:**
- Alle Dienste über Keycloak-SSO föderiert
- Nextcloud mit Dokumentenmanagement-Workflows integriert
- GIS-Schicht in Betrieb (QGIS + GeoServer)
- 80% der Verwaltungsdienste digitalisiert
- Behördenübergreifender Datenaustausch über XÖV/eCH in Betrieb

**Erfolgskriterien:**
- Ende-zu-Ende-Dienstleistungserbringung ohne Papier für 80% der Transaktionsarten
- Datenqualitätskennzahlen etabliert und verfolgt
- Erster jährlicher Open-Data-Bericht veröffentlicht

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

**Ziel:** Benutzererfahrung optimieren; Rückbeiträge an Open-Source-Gemeinschaften leisten; Ergebnisse veröffentlichen.

**Liefergegenstände:**
- Bürgerzufriedenheitsumfrage (Ziel: NPS > 40)
- Erster Beitrag zu openCode.de / Upstream-Projekten
- Kommunale Open-Source-Praxisgemeinschaft etabliert
- Leistungskennzahlen veröffentlicht

**Erfolgskriterien:**
- Mindestens drei Verbesserungen an Upstream-Projekte beigetragen
- Praxisgemeinschaft aktiv mit mindestens 3 eingebundenen Partnerkommunen
- Total-Cost-of-Ownership-Bericht veröffentlicht

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität erreichen; Erweiterung auf Nachbarkommunen vorbereiten.

**Liefergegenstände:**
- Vollständige Prüfung aller Softwarekomponenten auf Lizenzkonformität
- Souveräne Datenresidenz verifiziert
- Playbook für die Replikation durch Nachbarkommunen
- Strategiepapier v1.0 veröffentlicht

**Erfolgskriterien:**
- Null proprietäre Einzelanbieterabhängigkeiten im kritischen Pfad
- Datenresidenz zu 100% auf souveräner Infrastruktur
- Mindestens eine Partnerkommune hat das Playbook übernommen

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Einbindungsansatz |
|---|---|---|
| Bürgermeister/-in / Exekutive | Politischer Erfolg, Kosten, Bürgerzustimmung | Exekutivbriefing, Fortschrittsdashboard |
| Gemeinderat | Aufsicht, demokratische Legitimität | Vierteljährliche Berichte, offene Ratssitzungen |
| Städtisches IT-Team | Technische Machbarkeit, Arbeitsbelastung | Co-Design, Schulung, Community-Mitgliedschaft |
| Beschaffungsamt | Rechtskonformität, Risiko | Rahmenverträge, Rechtsbriefings |
| Beamte (Endnutzer) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Änderungsmanagement, Schulung |
| Bürger*innen | Servicequalität, Datenschutz | Partizipatives Design, Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Decidim-Plattform, öffentliche Fahrpläne |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de-Beteiligung, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Einsatz | Zertifizierte Partnerverträge |
| Datenschutzbeauftragte/r | DSGVO-Konformität | Privacy-by-Design-Überprüfung in jeder Phase |

### 6.2 Beschaffungsrahmen

Die Open-Source-Beschaffung erfordert einen anderen Rahmen als der proprietäre Lizenzkauf. Schlüsselprinzipien:

**1. Dienstleistungen beschaffen, keine Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung. Beschaffungsdokumente müssen um diese Dienstleistungen herum strukturiert werden.

**2. Genossenschaftliche Beschaffungsstrukturen nutzen.** Deutschlands govdigital eG und Schweizer kantonale IT-Genossenschaften bieten Rahmenverträge für kommunale Open-Source-IT an, die dem öffentlichen Vergaberecht entsprechen (GWB/Vergaberecht in Deutschland; BöB in der Schweiz) [23].

**3. Das "Public Money? Public Code!"-Prinzip anwenden.** Alle unter Vertrag entwickelten individuellen Softwarelösungen müssen unter einer OSI-genehmigten Open-Source-Lizenz veröffentlicht und auf openCode.de oder einem gleichwertigen öffentlichen Repository publiziert werden. Dies sollte eine Vertragsbedingung sein [4].

**4. Gesamtbetriebskosten bewerten.** Die Beschaffungsbewertung muss ein 5-Jahres-TCO-Modell umfassen, das Implementierung, Hosting, Schulung, Support und Ausstiegskosten abdeckt. Proprietäre Alternativen unterschätzen in der Regel langfristige Kosten, indem sie das Vendor-Lock-in-Risiko und die Lizenzeskalation weglassen.

**5. Interoperabilitätsstandards vorschreiben.** Alle beschafften Systeme müssen Folgendes implementieren: XÖV (Deutschland) [46], eCH (Schweiz) [48], DCAT-AP (EU Open Data). Nichteinhaltung sollte ein Ausschlusskriterium sein.

**6. Zertifizierte Genossenschaftsanbieter bevorzugen.** Für die Infrastruktur SCS-zertifizierte Cloud-Betreiber oder Mitglieder der govdigital eG bevorzugen, die an kollektive Datensouveränitätsvereinbarungen gebunden sind [23].

### 6.3 Änderungsmanagement

Open-Source-Übergänge scheitern häufig nicht an technischen, sondern an menschlichen Faktoren: Endnutzerwiderstand, unzureichende Schulung, Trägheit des mittleren Managements und politischer Rückschritt unter dem Druck von Anbieterlobbyismus.

**Empfehlungen:**
- Einen **Digital Transformation Champion** auf hochrangiger politischer Ebene mit ausdrücklichem Mandat ernennen
- **Open-Source-Champions** in jeder Abteilung mit fortgeschrittener Schulung und Peer-Support-Rolle etablieren
- Mindestens drei Monate lang **parallelen Betrieb** führen, bevor kritische Systeme umgestellt werden
- **Frühe Erfolge** (Kosteneinsparungen, neue Fähigkeiten, Bürgerfeedback) dokumentieren und feiern
- Ein **öffentliches Transparenz-Dashboard** veröffentlichen, das den Migrationsfortschritt, Kosten und Servicequalitätskennzahlen zeigt

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|
| Politische Kehrtwende nach Wahl | Mittel | Hoch | In Gesetz/Verordnung verankern; parteiübergreifenden Konsens aufbauen |
| Anbieterlobbyismus / FUD-Kampagnen | Hoch | Mittel | TCO-Belege dokumentieren; Zivilgesellschaft einbinden; Mandat veröffentlichen |
| Kompetenzlücke im IT-Team | Hoch | Mittel | Schulungsprogramm; genossenschaftlicher IT-Anbieter; Praxisgemeinschaft |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout mit Entscheidungsgateways; Referenzarchitektureadhärenz |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup-Protokoll; paralleler Betrieb; schrittweise Migration |
| DSGVO-/Datenschutzverletzung | Niedrig | Hoch | Privacy-by-Design; Einbindung des DSB; Datenmapping |
| Versagen der Nutzerakzeptanz | Mittel | Hoch | Änderungsmanagement; UX-Tests; Schulung; Parallelsysteme |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests; Vorfallsreaktionsplan |
| Gemeinschaftsfragmentierung | Niedrig | Mittel | Upstream beitragen; mit openCode.de ausrichten; govdigital eG beitreten |
| Kostenüberschreitung | Mittel | Mittel | Phasengebundenes Budget; unabhängiges Projektbüro; offene TCO-Abrechnung |

### 7.2 Der Münchener Warnfall

Das LiMux-Projekt der Stadt München (2003–2017) ist der am häufigsten zitierte Fall eines groß angelegten kommunalen Open-Source-Übergangs, der rückgängig gemacht wurde. Post-Mortem-Analysen identifizieren die Umkehrung als primär getrieben von: (a) einem Wechsel in der politischen Führung mit engeren Bindungen an Microsoft; (b) unzureichendem Änderungsmanagement und Benutzerschulung; (c) Kompatibilitätsproblemen mit Systemen auf Landesebene, die nicht aktualisiert worden waren, um offene Standards zu unterstützen [30]. Die technische Implementierung selbst war weitgehend erfolgreich.

Der Münchener Fall bestätigt, dass das politische Risikomanagement — parteiübergreifende Unterstützung aufzubauen und digitale Souveränität als konstitutionellen Wert zu verankern, nicht nur als Beschaffungspräferenz — genauso wichtig ist wie technische Planung.

### 7.3 Sicherheitsüberlegungen

Das IT-Grundschutz-Framework des BSI bietet eine umfassende Sicherheitsbasis, die unabhängig vom Lizenzmodell anwendbar ist [26]. Wesentliche Anforderungen:

- Alle Serverkomponenten müssen regelmäßige Sicherheitsupdates mit einem dokumentierten Patch-Management-Prozess erhalten
- Authentifizierung muss BSI-Authenticator-Assurance-Level-2 (AAL2) für bürgerorientierte Dienste erfüllen
- Daten während der Übertragung verschlüsselt (TLS 1.3 minimum); Daten im Ruhezustand für sensible Kategorien verschlüsselt
- Penetrationstests bei jedem Phasen-Gateway
- Vorfallsreaktionsplan in Übereinstimmung mit NIS2-Verpflichtungen [27]
- Software-Stückliste (SBOM) für alle Open-Source-Abhängigkeiten gepflegt

---

## 8. Schlussfolgerung

Die in diesem Papier untersuchten Belege konvergieren auf vier Befunde:

**1. Open-Source-Technologie-Stacks für Kommunalverwaltungen sind technisch ausgereift und produktionserprobt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software mit dokumentierten Einsätzen bei Peer-Kommunen erfüllt werden.

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland) und der Interoperable Europe Act (EU) schaffen rechtliche Verpflichtungen, die proprietäre, anbietergebundene Systeme nicht nachhaltig erfüllen können. Kommunen, die jetzt mit dem Übergang beginnen, bauen Compliance-Kapital auf; diejenigen, die zögern, häufen regulatorische Schulden an.

**3. Das wirtschaftliche Argument ist überzeugend, wenn Gesamtkosten korrekt berechnet werden.** Open-Source-Stacks eliminieren Platzlizenzkosten — oft 100–300 EUR pro Nutzer pro Jahr für Produktivitätssoftware allein — und reduzieren das Vendor-Lock-in-Risiko. Genossenschaftliche Beschaffungsmodelle verteilen Implementierungskosten auf viele Kommunen.

**4. Erfolg erfordert genauso viel politische und organisatorische Investition wie technische Investition.** Klares politisches Mandat, qualifiziertes Änderungsmanagement und nachhaltiges Stakeholder-Engagement sind die bindenden Einschränkungen. Der Münchener Fall und erfolgreiche Übergänge in Barcelona, Stuttgart und Schweizer Kantonen bestätigen dies gleichermaßen.

Kommunen, die sich zuerst bewegen, werden von First-Mover-Vorteilen profitieren: gemeinsame Standards gestalten, internes Know-how aufbauen und zum Open-Source-Commons beitragen, das alle Kommunen teilen. Die Einladung ist offen.

---

## Referenzen

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [Open Access, CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [Open Access, DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. Berlin: OSBA. https://scs.community/ — [Open Access, CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [Open Access, CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [Open Access]

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903 — [Open Access, EU-Gesetzgebung]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/ — [Open Access]

[10] openCode.de. (2022). *openCode — Open Source für den öffentlichen Sektor*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/ — [Open Access]

[11] Sovereign Cloud Stack Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/ — [Open Access, Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Freie Open-Source-Partizipationsdemokratie für Städte und Organisationen*. Barcelona: Decidim Association. https://decidim.org/ — [Open Access, AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud für die öffentliche Verwaltung: Sicherheit, Souveränität und Zusammenarbeit*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/ — [Open Access]

[14] The Matrix Foundation. (2023). *Matrix Specification*. https://spec.matrix.org/ — [Open Access, Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/ — [Open Access]

[19] TYPO3 Association. (2023). *TYPO3 in der öffentlichen Verwaltung*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association — [Open Access]

[20] OpenProject GmbH. (2023). *OpenProject für die öffentliche Verwaltung: Open-Source-Projektmanagement*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [Open Access, GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open-Source-Identitäts- und Zugriffsverwaltung*. https://www.keycloak.org/ — [Open Access, Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open-Source-Datenportalsoftware*. https://ckan.org/ — [Open Access, AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/ — [Open Access]

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/ — [Open Access]

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium*. Bonn: BSI. https://www.bsi.bund.de/ — [Open Access, CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2-Richtlinie*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555 — [Open Access]

[29] United Nations DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: United Nations. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022 — [Open Access]

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Open Access, Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open-Source-Webkonferenzen*. https://bigbluebutton.org/ — [Open Access, LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open-Source-Videokonferenzen*. https://jitsi.org/ — [Open Access, Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [Open Access, ODbL-1.0]

[37] QGIS Project. (2023). *QGIS: Ein freies und Open-Source-Geoinformationssystem*. https://www.qgis.org/ — [Open Access, GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — [Open Access, Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [Open Access, PostgreSQL-Lizenz]

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. https://opendesk.eu/ — [Open Access, AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/ — [Open Access]

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [Open Access, CC-BY-4.0]

[45] Europäische Kommission. (2017). *European Interoperability Framework — Implementation Strategy (EIF)*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [Open Access, CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/ — [Open Access]

[47] CONSUL Democracy. (2023). *CONSUL Democracy: Open Government and Citizen Participation Tool*. Madrid: Consul Project. https://consulproject.org/ — [Open Access, AGPL-3.0]

[48] eCH — E-Government Standards. (2023). *eCH-Standards: Interoperabilitätsstandards für E-Government in der Schweiz*. Bern: eCH. https://www.ech.ch/ — [Open Access]

[51] Bundeskanzlei / Bundesrätin. (2023). *E-ID — Elektronische Identität Schweiz*. Bern: Schweizerische Eidgenossenschaft. https://www.eid.admin.ch/ — [Open Access]

[53] GovStack Initiative. (2023). *GovStack: Digital Building Blocks for Sustainable Development*. Geneva: ITU / DIAL. https://www.govstack.global/ — [Open Access]

---

*Dieses Dokument wird unter der Creative-Commons-Lizenz Namensnennung 4.0 International (CC-BY-4.0) veröffentlicht.*
*Zitieren als: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*
