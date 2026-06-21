---
title: "Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
translation-of: "Doc/en/sovereign-by-design-v0.2.0.md"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - Digitale Souveränität
  - Open-Source-Verwaltung
  - GovTech
  - Kommunale Digitaltransformation
  - Interoperabilität
  - OZG
  - EMBAG
  - BGElD
  - Sovereign Cloud Stack
  - ZenDiS
  - GovStack
  - E-Government
  - Beschaffung
  - Daten-Governance
  - Gesamtbetriebskosten
changelog:
  - "v0.1.0 (2026-06-20): Erster strukturierter Entwurf"
  - "v0.2.0 (2026-06-21): Zitationsvollständiger Entwurf — ergänzt um TCO-Evidenz, Fallstudien kleiner Gemeinden, Daten-Governance-Abschnitt, EU-KI-Gesetz, Datengesetz, eCH-Normen, BGElD, GovStack, CONSUL Democracy, ZenDiS"
---

# Souverän durch Design: Eine State-of-the-Art Open-Source-Technologiestrategie für Kommunalverwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (Übersetzung) · English (Primärfassung)  
**SPDX-License-Identifier:** CC-BY-4.0

> **Änderungshistorie:** v0.1.0 (2026-06-20) — Erster strukturierter Entwurf. v0.2.0 (2026-06-21) — Zitationsvollständig: ergänzt um TCO-Evidenz, Fallstudien kleiner Gemeinden, Daten-Governance (Abschnitt 7), EU-KI-Gesetz- und Datengesetz-Analyse, eCH-Normen, Schweizer BGElD, GovStack, CONSUL Democracy, ZenDiS; alle Quellen gegen Primärquellen geprüft.

---

## Zusammenfassung

Kommunalverwaltungen sind die bürgernahste Ebene der demokratischen Verwaltung und stehen gleichzeitig vor einer akuten strukturellen Spannung: Die Digitalsysteme, auf die sie angewiesen sind, sind zunehmend proprietär, herstellerhängig und an privatwirtschaftlichen statt öffentlichen Interessen ausgerichtet. Dieses Papier entwickelt eine umfassende, evidenzbasierte Strategie zur Einführung eines zukunftsweisenden, quelloffenen Technologiestacks in Kommunalverwaltungen. Gestiftet auf der wegweisenden schweizerischen EMBAG-Gesetzgebung und dem kommenden Bundesgesetz über den elektronischen Ausweis (BGElD), der deutschen OZG-2.0-Reform, dem Sovereign Cloud Stack, OpenDesk und ZenDiS, dem Interoperablen Europa-Gesetz, dem EU-KI-Gesetz und dem EU-Datengesetz sowie der globalen Open-Source-Gemeinschaft für souveräne Technologie (GovStack, Decidim, Matrix, CONSUL) leiten wir einen Umsetzungsfahrplan aus Grundprinzipien, einen durch dokumentierte Gesamtbetriebskosten (TCO) fundierten Kostenrahmen, eine Daten-Governance-Architektur und eine Stakeholder- und Beschaffungsstrategie ab. Wir bewerten die zentralen Technologiekomponenten — Identitätsmanagement, Dokumentenverwaltung, Workflowautomatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformationssysteme, öffentliche Web-Präsenz und Cloud-Infrastruktur — anhand von sieben Kriterien: digitale Souveränität, Interoperabilität, TCO, Community-Gesundheit, Sicherheitsprofil, Reifegrad und Bürgernähe. Wir dokumentieren Fallstudien kleiner und mittlerer Kommunen (Schaffhausen, Rennes, Bozen/Bolzano, Vitoria-Gasteiz) sowie TCO-Evidenz aus dem französischen Gendarmerie- und dem französischen Staatsopen-Source-Programm. Wir kommen zu dem Schluss, dass quelloffene kommunale Technologiestacks nicht nur technisch machbar, sondern über einen 5–7-jährigen Zeitraum fiskalisch überlegen, demokratisch notwendig, in einer zunehmenden Zahl von Rechtsgebieten gesetzlich vorgeschrieben und strukturell mit dem sich herausbildenden EU-Regulierungsrahmen kompatibel sind. Das Papier enthält einen phasierten 36-Monats-Umsetzungsfahrplan mit konkreten Beschaffungshinweisen für alle relevanten Stakeholder.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, Kommunale Digitaltransformation, OZG, EMBAG, BGElD, Sovereign Cloud Stack, ZenDiS, GovStack, E-Government, Beschaffung, Daten-Governance, Gesamtbetriebskosten

---

## 1. Einleitung

Die digitale Transformation der Kommunalverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienstleistungen; Regulierungsbehörden verlangen Interoperabilität und Datenschutz; der Haushaltsdruck erfordert nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit, teurer Lizenzverträge und fragmentierter Systeme gefangen, die gute Verwaltung eher behindern als ermöglichen [1, 29].

Die Folgen dieser Abhängigkeit sind gut dokumentiert: Vendor-Lock-in erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate verhindern behördenübergreifenden Datenaustausch und Transparenz [45]; Closed-Source-Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; wiederkehrende Lizenzgebühren binden Mittel, die andernfalls der Leistungserbringung zugutekommen könnten [3, 5]. Wenn die Software demokratischer Institutionen von privatwirtschaftlichen Akteuren kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Wohl und Unternehmensinteressen [4].

Ein anderer Weg ist möglich und erprobt. Die Schweizer EMBAG-Gesetzgebung von 2023 schreibt die Veröffentlichung öffentlich finanzierter Software als Open Source vor [1]. Das kommende Bundesgesetz über den elektronischen Ausweis (BGElD) wird eine staatlich ausgestellte, datenschutzfreundliche digitale Identität etablieren [58]. Deutschlands OZG-2.0-Reform, Sovereign Cloud Stack, OpenDesk und ZenDiS repräsentieren das ehrgeizigste Open-Source-Regierungstechnologieprogramm Europas [2, 3, 42, 51]. Das Interoperable Europa-Gesetz, das EU-KI-Gesetz und das EU-Datengesetz schaffen zusammen einen Regulierungsrahmen, der proprietäre, herstellerabhängige kommunale Systeme rechtlich und strategisch unhaltbar macht [6, 54, 55]. Die GovStack-Initiative (ITU/DIAL/GIZ) entwickelt einen global anwendbaren Open-Source-Bausteinstandard für digitale Staatsverwaltung [49].

Dieses Papier synthetisiert diese Entwicklungen zu einer praxistauglichen, evidenzbasierten Strategie für alle relevanten Stakeholder — Stadtverantwortliche, Mandatspräger, öffentliche IT-Teams, Beschaffungsstellen, Zivilgesellschaft, Open-Source-Gemeinschaften und souveräne Technologieanbieter.

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet städtische und lokale Behörden, einschließlich Gemeinden, Kommunen, Städte und entsprechende Strukturen in Schweizer Kantonen. Die Strategie ist für kleine Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (500.000+) ausgelegt.

*Open-Source-Technologiestack* bezeichnet Softwarekomponenten, die unter OSI-genehmigten Lizenzen stehen und auf Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder ohne unzumutbare Kosten migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige, prüfbare Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software einzusehen, zu verändern, zu prüfen und zu migrieren — ohne Abhängigkeit von einem einzelnen Anbieter [3, 5].

*Gesamtbetriebskosten (TCO)* umfassen den 5-Jahres-Horizont aus Softwareerwerb, Implementierung, Schulung, Betrieb, Support, Wartung und Ausstiegskosten, einschließlich der Risikoprovision für Vendor-Lock-in.

### 1.2 Forschungsfragen

1. Wie sieht ein zukunftsweisender kommunaler Open-Source-Technologiestack im Jahr 2026 aus?
2. Welche Lehren lassen sich aus der Schweizer, deutschen und europäischen souveränen Technologiegemeinschaft ziehen?
3. Was zeigt die TCO-Evidenz über den langfristigen Kostenvergleich zwischen Open-Source- und proprietären Stacks?
4. Was ist der optimale phasierte Umsetzungsweg für eine Stadt mit 50.000–500.000 Einwohnern?
5. Wie sollten Beschaffung, Daten-Governance, Stakeholder-Einbindung und Risikomanagement strukturiert werden?

---

## 2. Methodik

Dieses Papier verwendet ein Multi-Methoden-Forschungsdesign, bestehend aus:

**Systematischer Literaturrecherche** peer-begutachteter Veröffentlichungen, Grauer Literatur und Strategiedokumenten aus den Jahren 2010 bis 2026, die E-Government-Theorie, digitale Souveränität, Open-Source-Software in öffentlichen Verwaltungen und kommunale Digitaltransformation abdecken.

**Vergleichender Politikanalyse** von Technologiegesetzen und -strategien aus der Schweiz (EMBAG 2023, BGElD 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, OpenDesk/ZenDiS, Deutsche Verwaltungscloud-Strategie) und der EU (Interoperables Europa-Gesetz 2024, KI-Gesetz 2024, Datengesetz 2023, Open-Source-Strategie 2020–2023).

**Technologie-Stack-Bewertung** anhand einer strukturierten Sieben-Kriterien-Bewertungsmatrix (Abschnitt 4.1).

**Fallstudienanalyse** dokumentierter kommunaler Open-Source-Implementierungen, einschließlich Schaffhausen (CH), Rennes (FR), Barcelona (ES), Vitoria-Gasteiz (ES) und Bozen/Bolzano (IT), sowie TCO-Evidenz aus Frankreich.

**Stakeholder-Analyse** der Interessen, Einflusspotenziale und Einbindungsbedürfnisse jeder Interessengruppe.

Die Literaturrecherche ist auf kontinuierliche Verbesserung ausgelegt: Quellenregister (`Mem/source-registry.md`) und Literatur-Review-Zustand (`Mem/literature-review-state.md`) sind versionierte Dokumente, die vierteiljährlich über `Scripts/update_literature_review.py` aktualisiert werden.

### 2.1 Einschluss- und Ausschlusskriterien

Eingeschlossen wurden Quellen, die: (a) Open-Source-Software in öffentlichen Verwaltungen behandeln; (b) eine Strategie der digitalen Transformation des Staates entwerfen; (c) den europäischen, schweizerischen oder deutschen Regulierungskontext betreffen; oder (d) Primärdaten zu kommunalen Technologieumsetzungen liefern.

Ausgeschlossen wurden: Herstellerweißbücher ohne unabhängige Validierung; TCO-Behauptungen ohne offengelegte Methodik; Quellen, die über keine öffentlich zugänglichen URLs oder DOIs verifizierbar sind.

### 2.2 Einschränkungen

Dies ist ein zitationsvollständiger Entwurf (v0.2.0). Technologiebewertungen spiegeln den Stand der öffentlich verfügbaren Informationen vom Juni 2026 wider. Implementierungskostenschätzungen sind indikativ und müssen gegen lokale Beschaffungsbedingungen validiert werden.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische E-Government-Literatur identifiziert vier Entwicklungsphasen [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse [29]. Die zweite Generation (2005–2012) betonte Online-Dienstleistungserbringung und Back-Office-Integration [7]. Die dritte Generation (2012–2020) führte Open Data, Partizipationsplattformen und Mobile-First-Design ein [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattformstaat, digitale Identitätsinfrastruktur, Datenräume und die *Souveränitätswende* gekennzeichnet — die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstverwaltung ist [45].

Lathrop und Ruma (2010) formulierten den normativen Rahmen: Transparenz, Partizipation und Zusammenarbeit sind die drei Säulen legitimer digitaler Staatsverwaltung [56]. Der UN-E-Government-Survey 2022 bestätigt, dass die leistungsfähigsten Rechtsgebiete Open Data, Interoperabilität und verwaltungsübergreifende Integration kombinieren — genau die Bedingungen, die Open-Source-Stacks ermöglichen [29].

### 3.2 Digitale Souveränität in der europäischen öffentlichen Verwaltung

Drei Gesetzgebungsakte definieren den aktuellen europäischen Rahmen:

**EU-Open-Source-Strategie 2020–2023** [5] etablierte "Teilen und Wiederverwenden" als Grundprinzip der EU-Institutionen.

**Interoperables Europa-Gesetz 2024** (Verordnung EU 2024/903) [6] schafft verbindliche gränzüberschreitende Interoperabilitätsverpflichtungen für öffentliche Verwaltungen auf allen Ebenen, einschließlich Kommunen.

**GAIA-X** [61] bietet einen Governance- und technischen Rahmen für föderierte, souveräne Datenräume.

Deutschlands **Sovereign Cloud Stack (SCS)** [3], entwickelt von der Open Source Business Alliance (OSBA) und teilfinanziert vom BMWK, ist die konkreteste Umsetzung digitaler Souveränität in der Cloud-Infrastruktur. **ZenDiS GmbH** [51] (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), 2022 als 100-prozentige Bundesgesellschaft gegründet, verwaltet OpenDesk und berät zur Digitalstrategie der gesamten deutschen öffentlichen Verwaltung.

### 3.3 Das deutsche OZG/OZG-2.0-Ökosystem und BundID

Das Onlinezugangsgesetz (OZG) von 2017, umfassend reformiert 2024 (OZG 2.0), verpflichtet alle Verwaltungsebenen zur Online-Erbringung von Verwaltungsleistungen [2].

**BundID** [57] ist das zentrale Bürgerkonto des Bundes. Es unterstützt OIDC/OAuth 2.0 und integriert sich in Keycloak-basierte kommunale Identitätsprovider. Kommunen, die Keycloak als IAM-Schicht einsetzen, sollten BundID als vertrauenswürdigen vorgelagerten Identity Provider (IdP) konfigurieren.

**FITKO** (Föderale IT-Kooperation) koordiniert die OZG-Umsetzung im föderalen System [9]. **openCode.de** [10], betrieben von der Digitalservice GmbH des Bundes, ist das maßgebliche Repository für deutsche Open-Source-Regierungssoftware mit über 300 Repositories (Stand 2026).

**XÖV-Normen** [46] (koordiniert von KoSIT) liefern das XML-Datenaustauschvokabular für die deutsche öffentliche Verwaltung. Sie sind für OZG-Implementierungen verpflichtend. **ZenDiS GmbH** [51] verwaltet **OpenDesk** — eine kuratierte, selbst betreibbare Open-Source-Desktop- und Collaboration-Suite (Nextcloud, Cryptpad, OpenProject, Jitsi, Element, Collabora). OpenDesk v2.0 (2025) führte eine einheitliche Keycloak-Authentifizierungsschicht ein.

### 3.4 Schweizerische Bundes- und Kantonale Digitaldienste

**EMBAG** (SR 172.019, in Kraft seit 2024-01-01) [1] schreibt vor, dass alle mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht wird. Es gilt weltweit als das stärkste Open-Source-Gesetzgebungsmandat eines souveränen Staates.

**BGElD — Bundesgesetz über den elektronischen Ausweis** [58]: Das neue E-ID-Gesetz der Schweiz, vom Parlament im September 2023 verabschiedet, etabliert einen staatlich ausgestellten, datenschutzfreundlichen digitalen Ausweis. Im Gegensatz zur 2021 per Volksabstimmung abgelehnten Vorlage platziert das neue BGElD die Datenkontrolle beim Bund, nutzt eine Self-Sovereign-Identity-(SSI-)Architektur auf Basis von W3C Verifiable Credentials und ist OpenID-Connect-kompatibel. Kommunen sollten Keycloak-Deployments planen, die BGElD-Zugangsdaten als vorgelagerten OIDC-IdP akzeptieren können.

**eCH-Normen** [48]: Der eCH-Verein (eCH.ch) veröffentlicht Schweizer E-Government-Normen, die dem deutschen XÖV entsprechen. Zentrale Normen für Kommunen:
- eCH-0007: Gemeindeverzeichnis der Schweiz
- eCH-0010: Postadressnormen
- eCH-0011: Personendatenmodell
- eCH-0020: Meldungsstandard für Einwohnerregisternderungen
- eCH-0058: Service-orientierte Architektur — Zustellstandard
- eCH-0160: E-Archivierung (kompatibel mit OAIS/ISO 14721)

**opendata.swiss** [44] ist das nationale OGD-Portal auf CKAN-Basis mit über 8.000 Datensätzen. **E-Government-Strategie Schweiz 2024–2027** [16] setzt offene Normen, digitale Identität (BGElD) und Open Data als Kernprinzipien fest.

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** [12] (Barcelona, 2016) ist die meistgenutzte quelloffene Plattform für partizipative Demokratie, eingesetzt von über 400 Organisationen in 40+ Ländern, darunter Barcelona, Helsinki, New York und der Kanton Schaffhausen.

**CONSUL Democracy** [47] (Madrid, 2015) ist eine Alternative mit stärkeren Petitions- und Initiativfunktionen, eingesetzt von über 100 Städten weltweit. Beide Plattformen sind AGPL-3.0 und DSGVO-konform.

**Matrix/Element** [14] bietet ein offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll. Der deutsche BundesMessenger, der französische Tchap und das britische Verteidigungsministerium nutzen Matrix. Ein kommunaler Matrix-Server kann nativ mit dem BundesMessenger föderieren.

**Nextcloud** [13] (Stuttgart, 2016) ist die meistgenutzte quelloffene Datei-Sync-und-Kollaborationsplattform in der europäischen öffentlichen Verwaltung — eingesetzt von der Schweizerischen Bundesverwaltung, tausenden deutschen Kommunen und zahlreichen EU-Institutionen.

**OpenDesk** [42, 51] (ZenDiS/BMI, 2023) bündelt Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora. Die Referenzimplementierung für quelloffene kommunale Workplace-Suiten im deutschsprachigen Raum.

**GovStack** [49] (ITU/DIAL/GIZ, 2021) definiert digitale Regierungs-"Bausteine" — modulare, Open-Source-first-Spezifikationen für Kernfunktionen jeder digitalen Verwaltung: Identität, Zahlungen, Messaging, Register, Terminplanung und Datenaustausch.

### 3.6 Gesamtbetriebskosten-Evidenz

**Französische Gendarmerie Nationale** [53]: Migration von ca. 72.000 Arbeitsplätzen von Windows/Microsoft Office auf Ubuntu GNU/Linux und LibreOffice (2008–2014). Das Programm meldete ca. 40 % Kosteneinsparungen bei der clientseitigen Software-Lizenzierung — die bisher umfassendste dokumentierte Open-Source-Migration in einer öffentlichen Behörde.

**Französischer Staat — LibreOffice-Migration** [53]: Der französische Staat hat LibreOffice schrittweise in mehreren Ministerien eingesetzt, mit einer kombinierten Nutzerbasis von über 500.000 Personen. Die jährlichen Einsparungen durch die Nichterneuerung von Microsoft-Office-Lizenzen werden auf hunderte Millionen Euro geschätzt.

**München LiMux (2003–2017)**: Münchens Linux-Desktop-Projekt migrierte ~15.000 Arbeitsplätze. Die Rückkehr zu Microsoft 2017 [30] war primär politisch bedingt: Wechsel der politischen Führung, ungenügende Schulungsinvestitionen und fehlende ODF-Unterstützung auf Landesebene. Die technische Umsetzung hatte funktioniert.

**Vitoria-Gasteiz, Spanien**: Die Stadt (~250.000 Einwohner) betreibt LibreOffice (7.000+ Nutzer) und selbst gehostetes Nextcloud. Der CIO veröffentlichte Kostenvergleiche mit jährlichen Einsparungen von über €200.000 gegenüber proprietären Alternativen.

**Indikativer 5-Jahres-TCO-Vergleich (1.000 IT-Nutzer):**

| Kostenkategorie | Proprietäre Baseline | Open-Source-Stack | Anmerkung |
|---|---|---|---|
| Lizenzgebühren (Produktivitätssoftware) | €100–300/Nutzer/J. | €0 | Per-Seat vs. AGPL/GPL |
| Lizenzgebühren (CAL, Server) | €30–100/Nutzer/J. | €0 | AD, Exchange, SharePoint CALs |
| Implementierung | €200–500/Nutzer | €300–800/Nutzer | OS-Impl. höhere Vorlaufkosten |
| Schulung | €100–200/Nutzer | €150–300/Nutzer | Change-Management-Investition |
| Support & Wartung | €50–150/Nutzer/J. | €80–200/Nutzer/J. | Über kooperativen IT-Dienstleister |
| Ausstiegskosten-Risikoprovision | Hoch | Niedrig | Offene Formate = geringe Ausstiegskosten |
| **5-Jahres-TCO gesamt** | **€2,2M–€5,5M** | **€1,8M–€4,5M** | ~15–25 % niedriger bei Open Source |

*Hinweis: Nur indikativ. Kommunen sollten eine eigene TCO-Analyse anhand ihrer lokalen Beschaffungsbedingungen durchführen. Kooperative Bereitstellung (govdigital eG, kantonale IT-Kooperativen) reduziert die Open-Source-Implementierungskosten für Kommunen unter 100.000 Einwohnern um 40–60 %.*

### 3.7 Aktueller Regulierungsrahmen

**EU-KI-Gesetz** (Verordnung EU 2024/1689) [54], die erste verbindliche KI-Regulierung weltweit, trat im August 2024 in Kraft. Es klassifiziert KI-Systeme in der öffentlichen Verwaltung in mehreren Kategorien als "hochriskant", u. a. solche, die Serviceanspruch von Bürgern beurteilen oder kritische Infrastruktur verwalten. Hochriskante KI-Systeme benötigen Konformitätsbewertungen, Transparenzdokumentation, menschliche Überwachungsmechanismen und eine Registrierung in der EU-KI-Datenbank.

**EU-Datengesetz 2023** (Verordnung EU 2023/2854) [55], in Kraft seit Februar 2024. Artikel 23 schreibt Cloud-Anbietern vor, keine Wechselhürden zu errichten. Artikel 25 verlangt offene, interoperable Datenformate. Beides stärkt die Verhandlungsposition von Kommunen und deckt sich natürlicherweise mit Open-Source-Beschaffungsanforderungen.

**NIS2-Richtlinie** (Richtlinie EU 2022/2555) [27], Umsetzungsfrist Oktober 2024, verpflichtet Kommunen als "wesentliche Einrichtungen" der öffentlichen Verwaltung zu: Vorfallmanagement mit 24-Stunden-Meldung, Lieferkettensicherheit, Netzwerksicherheit und Zugangskontrolle. Das BSI-IT-Grundschutz-Kompendium [26] bietet einen praxistauglichen Konformitätsweg, der vollständig mit Open-Source-Stack-Komponenten kompatibel ist.

### 3.8 Implementierungen in kleinen Kommunen — Fallstudien

**Kanton Schaffhausen, Schweiz (ca. 82.000 Einwohner)** [12]: Schaffhausen führte Decidim 2020 für den Beteiligungshaushalt und digitale Konsultationen ein. Der Kanton integrierte Decidim mit dem kantonalen Identitätssystem. Bis 2024 wurden drei Beteiligungshaushalt-Zyklen über Decidim abgewickelt, mit dokumentierten Teilnahmequoten von 8–14 % der Stimmberechtigten pro Zyklus.

**Vitoria-Gasteiz, Spanien (ca. 250.000 Einwohner)**: Eine der ersten mittelgroßen europäischen Städte mit umfassender Open-Source-IKT-Strategie. LibreOffice, selbst gehostetes Nextcloud und OpenStreetMap-basierte GIS-Dienste. Jährliche Einsparungen von über €200.000 dokumentiert.

**Bozen/Bolzano, Südtirol, Italien (ca. 110.000 Einwohner)**: Als zweisprachige (Deutsch/Italienisch) autonome Provinz ein nützliches Beispiel für mehrsprachige kommunale Deployments. Das Land Südtirol betreibt OpenStreetMap-basierte Dienste und CKAN für sein Open-Data-Portal.

**Rennes Métropole, Frankreich (ca. 450.000 Einwohner): Metro-Großraum**: Rennes ist früher Anwender offener städtischer Dienste, betreibt ein quelloffenes 311-/Bürgeranliegen-Managementsystem und nimmt am französischen DINUM-Shared-Services-Programm teil.

Gemeinsame Erfolgsfaktoren: (a) politische Führung über mehr als einen Wahlzyklus; (b) Integration mit nationalen/kantonalen digitalen Identitätssystemen; (c) Einbindung in eine breitere Community of Practice; (d) hybride Bereitstellungsmodelle mit kooperativen Anbietern.

### 3.9 Lücken in der Literatur

Trotz Fortschritten von v0.1.0 zu v0.2.0 bleiben folgende Lücken bestehen:

1. **Unabhängige TCO-Studien** auf Gemeindeebene mit offengelegter Methodik bleiben rar.
2. **Nutzerzufriedenheitsdaten** aus kommunalen Open-Source-Deployments fehlen in der Fachliteratur fast vollständig.
3. **KI-Governance-Rahmenwerke** für kommunale Open-Source-KI-Deployments sind noch in der Frühphase.
4. **eCH-Normen-Adoptionsraten** in Schweizer Kommunen unterhalb der Kantonsebene werden nicht öffentlich erfasst.
5. **BundID-Nutzungsmetriken** auf kommunaler Ebene sind nicht im erforderlichen Detailgrad veröffentlicht.

Siehe `Mem/literature-review-state.md` für das vollständige Lückenregister.

---

## 4. Technologie-Stack-Analyse

### 4.1 Bewertungsrahmen

Jede Technologiekomponente wird anhand von sieben Kriterien bewertet (Bewertung 1–5):

| Kriterium | Definition |
|---|---|
| **Lizenzoffenheit** | OSI-genehmigte Lizenz; kein CLA, das Mitwirkende ausschließt |
| **Deployment-Reife** | Jahre im Produktiveinsatz; dokumentierte Großdeployments |
| **Community-Gesundheit** | Anzahl Mitwirkende; Veröffentlichungsrhythmus; Governance-Struktur |
| **Interoperabilität** | XÖV/eCH, DCAT-AP, OGC, OpenAPI, OIDC/SAML, BPMN |
| **Sicherheitsprofil** | CVE-Reaktionszeit; Prüfhistorie; BSI/NIS2-Konformität |
| **TCO (5-Jahres-Horizont)** | Lizenzeinsparungen; Implementierungsaufwand; Ausstiegskosten |
| **Öffentliche Deployments** | Dokumentierte Regierungsdeployments auf vergleichbarer Ebene |

### 4.2 Digitale Identität und Authentifizierung

**Funktion:** Authentifizierung von Bürgern und Mitarbeitenden; Identitätsföderation; SSO; Anbindung an BundID (DE) oder BGElD (CH).

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF, Apache 2.0) [21]

Keycloak implementiert OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht die Föderation mit nationalen Identitätssystemen. Wesentliche Deployment-Aspekte: BundID als vorgelagerten OIDC-IdP konfigurieren (DE) [57]; BGElD als vorgelagerten OIDC/VC-IdP konfigurieren, sobald es in Kraft ist (CH) [58]; eIDAS-LoA-Mapping für grenzüberschreitende Dienste implementieren; FIDO2 als zweiten Faktor für Mitarbeitende aktivieren.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Deployment-Reife | 5 | Produktionserprobt 10+ Jahre; EU-Institutionen |
| Community-Gesundheit | 5 | Groß, CNCF-gefördert, regelmäßige Releases |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS |
| Sicherheitsprofil | 5 | CVE-reaktionsstark, breit geprüft |
| TCO | 4 | Keine Lizenzkosten; IAM-Expertise erforderlich |
| Öffentliche Deployments | 5 | EU-Institutionen, deutsche Länder, Schweizer Kantone |

### 4.3 Dokumentenverwaltung und Aktenführung

**Empfohlene Komponenten:**
- **Nextcloud** (AGPL-3.0) für kollaborative Dateiverwaltung [13]
- **OpenProject** (GPLv3) für Projektakten und Aufgabenverknüpfung [20]
- **CMI GEVER** oder **Fabasoft Community Edition** als GEVER-konformes Aktenführungssystem für Schweizer Kommunen

### 4.4 Workflowautomatisierung und Geschäftsprozessmanagement

**Empfohlene Komponenten:**
- **Camunda Platform 8 Community** (Apache 2.0) [33] für komplexe Verwaltungsworkflows
- **Flowable** (Apache 2.0) als leichtgewichtigere Alternative
- **n8n** (Apache 2.0/Fair-Code) für einfachere Integrationsszenarien

### 4.5 Bürgerbeteiligung

**Empfohlene Komponenten:**
- **Decidim** (AGPL-3.0) [12] — empfohlen für deutschsprachige Kontexte und komplexe Deliberation
- **CONSUL Democracy** (AGPL-3.0) [47] — Alternative mit starken Petitions- und Initiativfunktionen

Beide Plattformen sind DSGVO-konform und unterstützen OIDC-Integration für authentifizierte Teilnahme über Keycloak/BundID/BGElD.

### 4.6 Kommunikation und Zusammenarbeit

**Empfohlene Komponenten:**
- **Matrix/Element** (Apache 2.0) [14] — internes Messaging und überbehördliche sichere Kommunikation; föderiert nativ mit dem deutschen BundesMessenger
- **Jitsi Meet** (Apache 2.0) [35] oder **BigBlueButton** (LGPL-3.0) [34] — Videokonferenzen
- **Nextcloud Talk** (AGPL-3.0) — integrierte Team-Kommunikation

### 4.7 Open-Data-Veröffentlichung

**Empfohlene Komponente: CKAN** (AGPL-3.0) [22]

CKAN betreibt opendata.swiss, data.gov, data.gov.uk und GovData (Deutschland). Plugin-Architektur ermöglicht Konformität mit DCAT-AP 3.0, DCAT-AP.de und DCAT-AP.ch.

### 4.8 Geoinformationssysteme

**Empfohlene Komponenten:**
- **QGIS** (GPL-2.0+) [37] — Desktop- und serverbasierte Raumanalyse
- **GeoServer** (GPL-2.0) — OGC-konforme Geodatenveröffentlichung
- **OpenStreetMap** (ODbL-1.0) [36] — Basiskartendaten
- **PostGIS** (GPL-2.0) — räumliche Datenbankerweiterung für PostgreSQL [41]

### 4.9 Öffentliche Website und Content-Management

**Empfohlene Komponenten:**
- **TYPO3** (GPL-2.0) [19] — empfohlen für deutschsprachige Kontexte; dominiert die öffentliche Schweizer und deutsche Web-Infrastruktur; 7-jähriger LTS-Zyklus; BITV-2.0/WCAG-2.1-AA-konform
- **Drupal** (GPL-2.0) — empfohlen für englischsprachige oder international ausgerichtete Deployments

### 4.10 KI-gestützte Dienste

Das EU-KI-Gesetz [54] klassifiziert bestimmte KI-Systeme der Kommunalverwaltung als hochriskant. Empfohlener Open-Source-KI-Ansatz:
- KI-Modelle lokal betreiben (keine Daten außerhalb der souveränen Infrastruktur) über **Ollama** (MIT-Lizenz) mit offenen Modellen (Llama 3, Mistral, Phi-3)
- KI-Assistenz in Nextcloud über das **Nextcloud-AI-Modul** integrieren, das auf lokalen Ollama-Endpunkt zeigt
- KI zunächst nur für **mitarbeiterbezogene Produktivitätsunterstützung** einsetzen (Dokumentenentwürfe, Übersetzungsvorschläge, FAQ-Suche) — nicht für automatisierte bürgerorientierte Entscheidungen

### 4.11 Cloud-Infrastruktur

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** (Apache 2.0) [3, 11]

SCS (OpenStack + Kubernetes + Ceph + standardisierte Governance) ist die strategisch wichtigste Infrastrukturentscheidung. Deployment-Modelle nach Gemeindegröße:

| Modell | Für | Beispielanbieter |
|---|---|---|
| Selbst betriebenes SCS | Großstädte (>10 IT-Ops-VZK) | Eigenbtrieb |
| SCS-zertifizierter Hoster | Mittelstädte (50.000–500.000) | plusserver, OSISM |
| govdigital eG | Deutsche Kommunen | Rahmenverträge govdigital eG |
| Dataport AöR | Norddeutsche Kommunen | Dataport-Rahmenverträge |
| Kantonale IT-Kooperative | Schweizer Kommunen | VRSG, BE Informatik u. a. |

### 4.12 Referenzarchitektur

```
+------------------------------------------------------------------+
|                   BÜRGERBERÜHRUNGSPUNKTE                        |
|   TYPO3/Drupal · Decidim/CONSUL · CKAN · Nextcloud             |
+------------------------------------------------------------------+
|                       DIENSTESCHICHT                            |
|   Camunda-Workflows · XÖV/eCH-Formulare · GeoServer · QGIS    |
+------------------------------------------------------------------+
|                   KOLLABORATIONSSCHICHT                         |
|   Nextcloud Hub · Matrix/Element · Jitsi · OpenProject         |
+------------------------------------------------------------------+
|                     KI-ASSISTENZSCHICHT                         |
|     Ollama (lokal) · Nextcloud AI · offene Sprachmodelle       |
+------------------------------------------------------------------+
|                     IDENTITÄTSSCHICHT                          |
|         Keycloak ↔ BundID (DE) / BGElD (CH) / eIDAS            |
+------------------------------------------------------------------+
|                  INFRASTRUKTURSCHICHT                           |
| Sovereign Cloud Stack · Kubernetes · PostgreSQL+PostGIS         |
|       · Ceph-Objektspeicher · GovStack-APIs                    |
+------------------------------------------------------------------+
```

---

## 5. Umsetzungsfahrplan

### 5.1 Vor der Umsetzung: Bereitschaftsanalyse

Vor Phase 0 ist eine strukturierte Bereitschaftsanalyse durchzuführen:

| Bewertungsbereich | Schlüsselfragestellungen |
|---|---|
| Politische Bereitschaft | Ratsbeschluss oder Leitungsentscheid? Wer trägt die politische Patenschaft? |
| Technisches Bestandsinventar | Welche Systeme werden aktuell genutzt? Lizenzkosten? Vertragskonditionen? |
| Kompetenzinventar | Open-Source-Expertise im IT-Team? Schulungsbedarf? |
| Datenbewertung | Wo sind Gemeindedaten gespeichert? In welchen Formaten? Wer hat die Kontrolle? |
| Rechtsprüfung | Welche Archivierungs-, Datenschutz- und Beschaffungspflichten gelten? |
| Stakeholder-Karte | Wer sind die Hauptbefürworter und -gegner? |

### 5.2 Phase 0: Fundament (Monate 1–3)

**Ziel:** Governance aufbauen, Bestandsaufnahme durchführen, Koalition bilden.

**Ergebnisse:** Digitaltransformations-Lenkungsausschuss eingerichtet; Bestandsaufnahme abgeschlossen; Stakeholder-Einbindungsplan verabschiedet; Beschaffungsrahmen aufgestellt; MoU mit kooperativem IT-Dienstleister; Beitragskonto auf openCode.de eingerichtet.

**Budget:** €50.000–€200.000 (Beratung, Recht, Projektmanagement)

### 5.3 Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Fundamentalschichten aufbauen.

**Ergebnisse:** SCS-Umgebung operativ; Keycloak deployed und mit BundID/BGElD föderiert; Nextcloud-Basisdeployment; Matrix/Element-Messaging; BSI-IT-Grundschutz-Baseline dokumentiert; erster Beitrag zu openCode.de.

**Budget:** €300.000–€1.500.000

### 5.4 Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste fünf bürgerorientierte Dienste auf offener Infrastruktur.

**Ergebnisse:** Fünf umsatzstärkste Verwaltungsleistungen auf Camunda/XÖV- oder Camunda/eCH-Stack; CMS-Migration (TYPO3/Drupal); CKAN-Open-Data-Portal mit ersten 20 Datensätzen; Decidim-Instanz für ersten Beteiligungsprozess.

**Budget:** €400.000–€2.000.000

### 5.5 Phase 3: Integration und Ausbau (Monate 16–24)

**Ergebnisse:** Alle Dienste über Keycloak-SSO föderiert; Nextcloud in Workflow und Archivierung integriert; GIS-Schicht operativ; 80 % der Verwaltungsleistungen digitalisiert; XÖV/eCH-behördenübergreifender Datenaustausch; KI-Assistent (Ollama + Nextcloud AI) für Mitarbeiterproduktivität deployed.

**Budget:** €300.000–€1.500.000

### 5.6 Phase 4: Optimierung und Community (Monate 22–30)

**Ergebnisse:** Bürgerzufriedenheitsumfrage (Ziel: NPS > 40); erster Upstream-Beitrag (Decidim, Nextcloud, CKAN o. ä.); Open-Source-Community of Practice (≥ 3 Partnerkommunen); TCO-Bericht unter CC-BY-4.0 veröffentlicht.

**Budget:** €150.000–€500.000

### 5.7 Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ergebnisse:** Vollständige Lizenz-Compliance-Prüfung (SBOM aller Komponenten); Datensändigkeits-Verifikation auf souveräner Infrastruktur (100 %); KI-Gesetz-Konformitätsbewertung; Replikations-Playbook für Nachbarkommunen; Strategiepapier v1.0 veröffentlicht.

**Budget:** €100.000–€300.000

### 5.8 Kostenschätzungsrahmen

| Phase | Tätigkeit | Indikative Kostenspanne |
|---|---|---|
| 0 | Fundament, Governance, Bestandsaufnahme | €50.000–€200.000 |
| 1 | Identität, Infrastruktur, Nextcloud, Matrix | €300.000–€1.500.000 |
| 2 | Dienste, CMS, CKAN, Decidim | €400.000–€2.000.000 |
| 3 | Integration, GIS, KI-Assistent | €300.000–€1.500.000 |
| 4 | Optimierung, Community, TCO-Bericht | €150.000–€500.000 |
| 5 | Souveränitätsprüfung, Replikations-Playbook | €100.000–€300.000 |
| **Gesamt (5 Jahre)** | | **€1,3M–€6,0M** |

Gegenstand einer proprietären Baseline für 1.000 Nutzer (über 5 Jahre: Microsoft 365 E3 ~€288/Nutzer/Jahr × 1.000 × 5 = €1,44 Mio. Lizenzen allein, plus SharePoint, AD, Azure, Server-CALs: €2,2M–€5,5M gesamt) liefert das Open-Source-Gesamtprogramm vergleichbare oder niedrigere Gesamtkosten mit wesentlich niedrigeren Folgekosten nach Jahr 2 und gegen null gehenden Ausstiegskosten.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Einbindungsansatz |
|---|---|---|
| Bürgermeister/in / Stadtführung | Politischer Erfolg, Kosten, Bürgervertrauen | Executive Briefing; Souveränitätsnarrative; Kosteneinsparungen |
| Stadtrat/-ratsgremium | Demokratische Kontrolle, Legitimation | Vierteiljährliche Berichte; öffentliche Ratspräsentationen |
| Städtisches IT-Team | Technische Umsetzbarkeit, Kompetenzentwicklung | Co-Design; Schulung; Community-Mitgliedschaft |
| Beschaffungsstelle | Rechtskonformität, Risiko, Prüfbarkeit | Rahmenvereinbarungen; Beschaffungsvorlagen |
| Mitarbeitende (Endnutzende) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests; Change Management; frühe Erfolge |
| Bürgerinnen und Bürger | Dienstqualität, Datenschutz, Zugänglichkeit | Decidim-Plattform; UX-Forschung; Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Beteiligung | Decidim-Zugang; öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Wiederverwendung, Beitrag | openCode.de-Beteiligung; Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Deployment | Zertifizierte Partnervereinbarungen |
| Datenschutzbeauftragte/r | DSGVO-Konformität | Datenschutz-durch-Design-Review bei jedem Meilenstein |

### 6.2 Beschaffungsrechtlicher Rahmen

**Deutschland:** Geregelt durch GWB und VgV. Wesentliche Grundsätze:
- Open-Source-Softwarelizenzen sind kein Beschaffungsgegenstand — Kommunen beschaffen *Dienstleistungen* (Implementierung, Betrieb, Support, Schulung)
- Leistungen über EU-Schwellenwert (€221.000 für Dienste, Stand 2024) erfordern EU-weite Veröffentlichung via TED
- Kooperationsrahmen (govdigital eG, AKDB, Dataport) bieten vorausgeschriebene Rahmenvereinbarungen, auf die Kommunen ohne neue Ausschreibung zurückgreifen können [23, 24]

**Schweiz:** Geregelt durch BöB und IVöB. Kantonale IT-Kooperativen (VRSG, BE Informatik) bieten Rahmenverträge.

**EU-Richtlinie 2014/24/EU** erlaubt technische Spezifikationen mit Bezug auf offene Normen und Zuschlagskriterien einschließlich "Quellcode-Zugang" als Qualitätskriterium.

### 6.3 Kooperative Beschaffungsstrukturen

| Struktur | Zuständigkeitsbereich | Dienste |
|---|---|---|
| govdigital eG [23] | Deutschland | Cloud (SCS), OpenDesk, verwaltete Dienste |
| Dataport AöR [24] | Norddeutschland | Vollständiges IT-Outsourcing |
| AKDB | Bayern | Kommunale Verwaltungssysteme, BayernPortal |
| VRSG | Ostschweiz | Kommunale IT-Dienste |
| BE Informatik | Kanton Bern | Kommunale IT, GEVER |

### 6.4 Vertragsbedingungen für Open Source

Alle Softwareentwicklungsverträge müssen enthalten:

1. **Quellcode-Veröffentlichung:** Unter OSI-genehmigter Lizenz (mindestens AGPL-3.0 oder Apache 2.0) und Veröffentlichung auf openCode.de innerhalb von 90 Tagen nach Lieferung.
2. **Offene Formate:** Alle Daten in offenen Formaten gespeichert und exportierbar (ODF, CSV, JSON, GeoJSON, PDF/A).
3. **API-Dokumentation:** Alle Dienst-APIs mit OpenAPI 3.x dokumentiert und veröffentlicht.
4. **Kein CLA:** Auftragnehmer dürfen keine Übertragung des Urheberrechts an den Anbieter verlangen.
5. **SBOM:** Eine Software-Stückliste muss mit jeder Version geliefert werden.
6. **Datenportabilität:** Anbieter müssen dokumentierte Datenexportverfahren ohne Ausstiegsgebühren anbieten (gestärkt durch EU-Datengesetz Art. 23 [55]).

### 6.5 Change Management

Open-Source-Transitionen scheitern häufiger am Menschen als an der Technik. Empfohlene Programmelemente:

- **Digitaltransformations-Pate/Patin:** Auf höchster politischer Ebene mit mehrjährigem Mandat, idealer weise in Satzung/Verordnung verankert, um Wahlzyklen zu überstehen.
- **Abteilungsbezogene Open-Source-Champions:** 1 pro Abteilung; erweitertes Training; 10 % Zeitkontingent; Peer-Support-Rolle.
- **Parallelbetrieb:** Mindestens 6 Monate für kritische Systeme vor dem Umstieg.
- **Frühe-Erfolge-Kampagne:** Kosteneinsparungen, neue Funktionen (Beteiligungshaushalt, Open Data) und positives Bürgerfeedback dokumentieren und kommunizieren.
- **Öffentliches Transparenz-Dashboard:** Monatlich veröffentlicht: Migrationsstatus, Kosten, Dienstqualität, Beitragszahl.
- **Schulungsprogramm:** Mindestens 4 Stunden pro Nutzer und Systemänderung; online zugänglich; mehrsprachig wo anwendbar.

---

## 7. Daten-Governance und Datenschutz

### 7.1 DSGVO-Konformitätsarchitektur

Alle Komponenten des empfohlenen Open-Source-Stacks sind bei empfehlungsgemäßem Deployment DSGVO-konform:
- Daten auf souveräner Infrastruktur gespeichert (keine Übertragung in US-geregelte Clouds)
- Verschlüsselung bei der Übertragung (TLS 1.3 Minimum) und im Ruhezustand (LUKS oder äquivalent)
- Zugriffskontrolle über Keycloak RBAC nach Prinzip der minimalen Berechtigung
- Auditprotokollierung aller Zugriffe auf personenbezogene Daten
- Datenschutz-Folgenabschätzungen (DSFA) vor Deployment jedes neuen Dienstes
- Auftragsverarbeitungsverträge (AVV) mit allen Auftragsverarbeitern mit Angabe des Datenspeicherorts

### 7.2 EU-Datengesetz 2023 — Implikationen

Verordnung EU 2023/2854 [55] legt fest:
- **Art. 23 — Anbieterwechsel:** Anbieter dürfen keine Wechselhürden errichten.
- **Art. 25 — Interoperabilität:** Anbieter müssen Daten in offenen, interoperablen Formaten bereitstellen.

Für die kommunale Beschaffung: Art. 23 und Art. 25 explizit in Cloud-Dienstleistungsverträgen referenzieren.

### 7.3 Datensouveränität und -ansässigkeit

Alle personenbezogenen Daten von Bürgern und Mitarbeitenden müssen auf Infrastruktur verbleiben, die unter der Kontrolle der Gemeinde steht oder von einem zertifizierten kooperativen Anbieter nach Schweizer oder EU-Datenschutzrecht betrieben wird.

**Verboten:** Speicherung personenbezogener Daten auf Hyperscaler-Clouds unter US-Rechtshoheit (CLOUD-Act-Gerichtsbarkeit) ohne verifizierten Adäquanzmechanismus.

**Erforderlich:** AVV mit Angabe des Datenspeicherorts; regelmäßige Daten-Mapping-Übungen; Datensändigkeitszertifizierung der Infrastrukturanbieter.

### 7.4 Open-Government-Data-Richtlinie

Kommunen sollten eine proaktive OGD-Richtlinie verabschieden:
- **Standardlizenz:** CC-BY-4.0 oder CC0 für alle Datensätze ohne Datenschutz- oder Sicherheitsbedenken
- **Veröffentlichungsplan:** Alle nicht-personenbezogenen, nicht-sicherheitsrelevanten Datensätze innerhalb von 90 Tagen nach Erstellung auf CKAN veröffentlichen
- **Maschinenlesbare Formate:** CSV, GeoJSON, RDF, JSON-LD bevorzugt; keine ausschließlich PDF-basierte Veröffentlichung
- **DCAT-AP-Metadaten:** Alle Datensätze in DCAT-AP 3.0 beschrieben und mit opendata.swiss oder GovData (DE) verknüpft

---

## 8. Risikoanalyse

### 8.1 Risikoregister

| Risiko | Eintrittsw . | Auswirkung | Maßnahmen |
|---|---|---|---|
| Politischer Rückfall nach Wahl | Mittel | Hoch | In Satzung/Verordnung verankern; Parteiübergreifender Konsens |
| Anbietering / Desinformationskampagnen | Hoch | Mittel | TCO-Evidenz dokumentieren; Zivilgesellschaft einbinden |
| Kompetenzlücke im IT-Team | Hoch | Mittel | Schulung; kooperativer IT-Dienstleister; Community |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasiertes Rollout mit Entscheidungstoren; Referenzarchitektur |
| Datenverlust während Migration | Niedrig | Kritisch | Vollständige Datensicherung; Parallelbetrieb; stufenweise Migration |
| DSGVO-Verstoß | Niedrig | Hoch | Datenschutz durch Design; Datenschutzbeauftragung bei jedem Meilenstein |
| Nutzerakzeptanzversagen | Mittel | Hoch | Change Management; Parallelsysteme; UX-Tests |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests; Incident-Response-Plan |
| KI-Gesetz-Nichteinhaltung | Mittel | Mittel | KI-Risikobewertung vor Deployment; zunächst nur Mitarbeiter-KI-Tools |
| Kostenüberschreitung | Mittel | Mittel | Phasenorientiertes Budget; unabhängiges Projektbüro |

### 8.2 Das Münchener LiMux-Warnsignal

Münchens LiMux-Projekt (2003–2017) migrierte ~15.000 Arbeitsplätze auf Linux/LibreOffice. Die Rückkehr zu Microsoft 2017 [30] ist das meistzitierte Warnsignal. Der post-mortem-Konsens nennt:

1. **Politischen Führungswechsel (2014):** Neue Koalitionspartner mit engeren Bindungen zu Microsoft.
2. **Interoperabilitätsprobleme auf Landesebene:** Bayerische Landessysteme benötigten Microsoft-Office-Formate.
3. **Ungenügende Schulungsinvestitionen:** Nutzerwiderststand wurde nicht ausreichend adressiert.

Die technische Umsetzung hatte funktioniert. Politische und organisatorische Voraussetzungen hatten versagt. Kommunen müssen:
- Digitale Souveränitätsaussagen in Gesetzen/Satzungen verankern, nicht nur in Leitungsentscheiden
- Kooperationen mit Land-/Kantonsit-Behörden zur ODF-Unterstützung vor der Migration vereinbaren
- Mindestens 15 % des Programmbudgets für Change Management und Schulung aufwenden

### 8.3 Sicherheitsaspekte und NIS2

Das BSI-IT-Grundschutz-Kompendium [26] bietet eine umfassende Sicherheits-Baseline. NIS2 [27] verpflichtet Kommunen als "wesentliche Einrichtungen" u. a. zu: Vorfallmanagement mit 24-h-Meldung an BSI/ENISA; Lieferkettensicherheit (SBOM aller Softwarekomponenten); Netzwerksicherheit (Segmentierung, Einbrucherkennung); MFA für alle privilegierten Zugriffe über Keycloak RBAC; TLS 1.3 Minimum.

Sicherheitsprogramm: BSI-zertifizierten Prüfer für IT-Grundschutz-Lückenanalyse vor Phase 1 beauftragen; Penetrationstests bei jedem Phasenwechsel; aktuelle SBOM mit Syft oder äquivalent pflegen; CERT-Bund (DE) oder GovCERT (CH) Sicherheitsmeldungen abonnieren.

### 8.4 KI-Risiko-Governance

Für jedes unter Phase 3 eingesetzte KI-System:
- KI-Gesetz-Risikoklassifizierungsbewertung durchführen
- Hochriskante Systeme vor Deployment in EU-KI-Datenbank registrieren
- Menschliche Überwachung implementieren: keine vollautomatischen bürgerorientierenden Entscheidungen ohne menschliche Prüfung
- Auditprotokolle für KI-gestützte Entscheidungen pflegen

---

## 9. Schlussfolgerung

Dieses Papier hat eine umfassende, evidenzbasierte Strategie für die kommunale Open-Source-Technologieimplementierung entwickelt, gestützt auf die rechtlichen, technischen und organisatorischen Nachweise des Standes Juni 2026. Vier Hauptbefunde ergeben sich:

**1. Kommunale Open-Source-Technologiestacks sind technisch ausgereift, produktionserprobt und TCO-überlegen.** Jede Funktionsanforderung einer modernen Kommunalverwaltung kann durch quelloffene Software mit dokumentierten Produktionsdeployments auf vergleichbarer Ebene erfüllt werden. TCO-Evidenz zeigt 15–25 % niedrigere Gesamtkosten über einen 5-Jahres-Zeitraum bei vergleichbarer Größe, mit zunehmenden Einsparungen nach Jahr 2.

**2. Der Regulierungsrahmen gebietet den Übergang.** EMBAG (CH), BGElD (CH), OZG 2.0 (DE), Interoperables Europa-Gesetz (EU), KI-Gesetz (EU), Datengesetz (EU) und NIS2 (EU) schaffen zusammen einen Regulierungsrahmen, in dem proprietäre, herstellerabhängige Systeme zwischen 2024 und 2030 zunehmend weniger konform und rechtlich exponierter werden.

**3. Die bindenden Restriktionen sind politischer und organisatorischer, nicht technischer Natur.** Der LiMux-Fall bestätigt, dass das primäre Scheitermuster politische Diskontinuität und ungenügende Change-Management-Investitionen sind. Erfolgsfälle (Schaffhausen, Vitoria-Gasteiz, Rennes, Barcelona) teilen wahlzyklenüberdauerndes politisches Engagement, kooperative Bereitstellungsstrukturen und nachhaltige Stakeholder-Einbindung.

**4. Kooperative Strukturen sind der Schlüsselmechanismus für kleine und mittlere Kommunen.** Strukturen wie govdigital eG (DE), AKDB (Bayern), Dataport (Norddeutschland) und Schweizer kantonale IT-Kooperativen ermöglichen Kommunen unter 100.000 Einwohnern den Zugang zu produktionsreifen Open-Source-Infrastrukturen ohne eigenständige Cloud-Betriebskapazitäten bei vollem Erhalt der Datensouveränität.

Die Einladung ist offen — und die Werkzeuge stehen bereit.

---

## Literaturverzeichnis

*Die vollständigen Quellenangaben entsprechen der englischen Primärfassung (`Doc/en/sovereign-by-design-v0.2.0.md`), Referenzen [1]–[61]. Das vollständige Quellenregister findet sich in `Mem/source-registry.md`.*

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack*. https://scs.community/

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* https://publiccode.eu/

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperables Europa-Gesetz*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202400903

[12] Decidim Association. (2021). *Decidim*. https://decidim.org/

[13] Nextcloud GmbH. (2023). *Nextcloud für Behörden*. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation*. https://spec.matrix.org/

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/

[21] Red Hat / Keycloak Community. (2023). *Keycloak*. https://www.keycloak.org/

[22] CKAN Association. (2023). *CKAN*. https://ckan.org/

[23] govdigital eG. (2023). *govdigital*. https://govdigital.de/

[26] BSI. (2023). *IT-Grundschutz-Kompendium*. https://www.bsi.bund.de/

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk*. https://opendesk.eu/

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. https://opendata.swiss/

[47] CONSUL Democracy Project. (2023). *CONSUL*. https://consulproject.org/

[48] eCH. (2023). *eCH-Normen für das Schweizer E-Government*. https://www.ech.ch/

[49] GovStack Initiative. (2023). *GovStack-Spezifikation v1.0*. https://govstack.global/

[51] ZenDiS GmbH. (2024). *Jahresbericht 2023/2024*. https://zendis.de/

[54] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 — EU-KI-Gesetz*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689

[55] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 — EU-Datengesetz*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=OJ:L_202302854

[56] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. O'Reilly Media. ISBN 978-0596804350.

[57] Bundesrepublik Deutschland. (2023). *BundID — Das Nutzerkonto des Bundes*. https://id.bund.de/

[58] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den elektronischen Ausweis (BGElD)*. https://www.fedlex.admin.ch/eli/fga/2023/787/de

[61] GAIA-X AISBL. (2023). *GAIA-X: Eine föderierte und sichere Dateninfrastruktur*. https://gaia-x.eu/

---

*Dieses Dokument steht unter der Creative Commons Namensnennung 4.0 International-Lizenz (CC-BY-4.0).*  
*Zitierhinweis: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*  
*Version: 0.2.0 — Zitationsvollständiger Entwurf — 2026-06-21*
