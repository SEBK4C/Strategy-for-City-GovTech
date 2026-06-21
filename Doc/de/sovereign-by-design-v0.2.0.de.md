---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Regierungen"
author: "Sebastian Graf, Autonomes Büro für Digitale Zivilinfrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitierfähiger Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
translated-from: "Doc/en/sovereign-by-design-v0.2.0.md"
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
  - Bürgertechnologie
  - ZenDiS
  - OpenDesk
  - eCH-Standards
  - GovStack
  - Total Cost of Ownership
changelog:
  - version: "0.2.0"
    date: "2026-06-21"
    changes:
      - "Vollständige deutsche Übersetzung von v0.2.0 (zitierfähiger Entwurf)"
      - "Abschnitt 3.6 — TCO-Belege (kritische Lücke behoben)"
      - "Abschnitt 3.7 — Fallstudien kleiner Kommunen (kritische Lücke behoben)"
      - "Abschnitt 3.8 — ZenDiS und institutionelle Architektur"
      - "eCH-Standards, CONSUL Democracy, GovStack, Schweizer E-ID, EU-Datengesetz"
      - "62 Quellen im Quellenverzeichnis"
  - version: "0.1.0"
    date: "2026-06-20"
    changes:
      - "Erster strukturierter Entwurf — vollständige Gliederung, 46 Quellen"
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Regierungen

**Autor:** Sebastian Graf, Autonomes Büro für Digitale Zivilinfrastruktur
**Korrespondenz:** sebk4c@tuta.com
**Version:** 0.2.0 — Zitierfähiger Entwurf
**Datum:** 2026-06-21
**Sprachen:** Deutsch (Übersetzung) · English (Wahrheitsquelle)
**SPDX-License-Identifier:** CC-BY-4.0

---

## Zusammenfassung

Kommunalverwaltungen sind die der Bürgerschaft nächste Schicht demokratischer Administration, stehen jedoch vor einer akuten strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, anbieterseitig eingesperrt und im Widerspruch zu gemeinwohlorientierten Werten. Dieses Papier präsentiert eine umfassende Strategie für die Implementierung eines zukunftsweisenden, quelloffenen Technologie-Stacks in kommunalen Verwaltungen. Gestützt auf Vorzeigebeispiele aus der Schweizer Bundesverwaltung (EMBAG-Gesetzgebung), Deutschlands OZG-Reformprogramm, ZenDiS und der Sovereign-Cloud-Stack-Initiative sowie der breiteren europäischen Gemeinschaft für souveräne Technologien — einschließlich des GovStack-Baustein-Rahmens, CONSUL Democracy und des geteilten eVaka-Ressourcenmodells — leiten wir einen grundlegenden Implementierungsfahrplan, einen Stakeholder-Einbindungsrahmen und eine Beschaffungsstrategie ab.

Wir bewerten die Kerntechnologiekomponenten — Identitätsmanagement, Dokumentenverwaltung, Workflow-Automatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformationssysteme, öffentliche Websites und Cloud-Infrastruktur — anhand der Kriterien digitale Souveränität, Interoperabilität, Gesamtbetriebskosten und bürgerliche Ausrichtung.

Wir präsentieren empirische Gesamtkostenbelege: Das GendBuntu-Projekt der Gendarmerie Nationale erzielte eine 40-prozentige TCO-Reduktion und zwei Millionen Euro jährliche Lizenzersparnis bei 103.164 Arbeitsplätzen; die Stadt Toulouse dokumentierte 1,8 Millionen Euro Einsparungen über drei Jahre nach der Open-Source-Desktop-Migration. Wir kommen zu dem Schluss, dass quelloffene Kommunaltechnologie-Stacks nicht nur technisch machbar, sondern fiskalisch überlegen, demokratisch notwendig und in einer wachsenden Zahl von Rechtssystemen gesetzlich vorgeschrieben sind. Das Papier enthält einen phasenweisen 36-monatigen Implementierungsfahrplan mit einer spezifischen Spur für kleine Kommunen sowie konkrete Beschaffungsleitlinien.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale digitale Transformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, ZenDiS, OpenDesk, eCH-Standards, GovStack, Gesamtbetriebskosten

---

## 1. Einleitung

Die digitale Transformation der kommunalen Selbstverwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und zugängliche digitale Dienste; Regulierungsbehörden fordern Interoperabilität und Datenschutz; und finanzielle Rahmenbedingungen erfordern nachhaltige, kostenwirksame Technologieinvestitionen. Dennoch bleibt die Mehrheit der Kommunen weltweit in einem Kreislauf aus proprietären Anbieterabhängigkeiten, teuren Lizenzverträgen und fragmentierten Systemen gefangen, die gutes Verwaltungshandeln eher behindern als unterstützen [1, 29].

Die Folgen dieser Abhängigkeit sind hinlänglich dokumentiert: Anbietereinschluss erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Quellinfrastruktur verhindert unabhängige Sicherheitsaudits [26]; und wiederkehrende Lizenzgebühren entziehen Budgets, die andernfalls für die Leistungserbringung eingesetzt werden könnten [3, 5]. Grundlegender noch: Wenn die Software, die demokratische Institutionen betreibt, im Besitz privater Akteure ist und von diesen kontrolliert wird, entsteht ein struktureller Interessenkonflikt zwischen öffentlichem Interesse und unternehmerischen Imperativen [4]. Das philosophische Fundament dieses Wandels formulierten Lathrop und Ruma in *Open Government* (2010): Daten, die durch öffentliche Prozesse generiert und mit öffentlichen Mitteln finanziert werden, sollten als Standard öffentlich verfügbar sein [60].

Ein anderer Weg ist sowohl möglich als auch erprobt. Die Schweizer EMBAG-Gesetzgebung (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht werden muss [1]. Deutschlands OZG-Reformprogramm, ZenDiS und seine OpenDesk-Initiative, der Sovereign Cloud Stack sowie die openCode.de-Plattform repräsentieren das ambitionierteste koordinierte Open-Source-Regierungstechnologieprogramm in Europa [2, 3, 42, 47]. Die FSFE-Kampagne „Public Money? Public Code!", von über 200 Organisationen in 30 Ländern unterstützt, benennt das demokratische Prinzip: Mit öffentlichen Mitteln finanzierte Software muss der Öffentlichkeit zur Verfügung stehen [4].

### 1.1 Geltungsbereich und Definitionen

*Kommunalverwaltung* bezeichnet kommunale und lokale Gebietskörperschaften, einschließlich Gemeinden, Kommunen, Städte und gleichwertige Strukturen in Schweizer Kantonen. Die Strategie ist darauf ausgelegt, von kleinen Gemeinden (5.000–50.000 Einwohner) bis zu Großstädten (500.000+) zu skalieren, mit spezifischer Anpassung in der Kleinkommune-Spur in Abschnitt 5.6.

*Open-Source-Technologie-Stack* bezeichnet Softwarekomponenten unter OSI-genehmigten Lizenzen, die auf Infrastruktur betrieben werden, die die Gemeinde kontrolliert oder ohne übermäßige Kosten oder Hürden migrieren kann.

*Digitale Souveränität* ist die Fähigkeit einer Regierung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen, einschließlich des Rechts, Software ohne Abhängigkeit von einem einzelnen Anbieter zu prüfen, zu modifizieren, zu auditieren und zu migrieren [3, 59].

### 1.2 Forschungsfragen

1. Wie sieht ein zukunftsweisender quelloffener kommunaler Technologie-Stack im Jahr 2026 aus?
2. Welche Erkenntnisse lassen sich aus den Schweizer, deutschen und europäischen Gemeinschaften für souveräne Technologie ziehen?
3. Was ist der optimale phasenweise Implementierungsweg für Kommunalverwaltungen unterschiedlicher Größe?
4. Wie sollten Beschaffung, Stakeholder-Einbindung und Risikomanagement strukturiert werden, um die Erfolgswahrscheinlichkeit zu maximieren?

---

## 2. Methodik

Dieses Papier verwendet ein Multi-Methoden-Forschungsdesign, das folgendes kombiniert:

**Systematische Literaturauswertung** wissenschaftlich begutachteter Publikationen, grauer Literatur und Politikdokumente aus den Jahren 2010 bis 2026 zu E-Government-Theorie, digitaler Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunaler digitaler Transformation. Die Literaturauswertung ist so konzipiert, dass sie sich selbst verbessert: Das Quellenverzeichnis (`Mem/source-registry.md`) und der Literaturauswertungsstand (`Mem/literature-review-state.md`) sind versionierte Dokumente, die im Quartalstakt aktualisiert werden.

**Vergleichende Politikanalyse** der Technologiegesetzgebung und -strategien der Schweiz (EMBAG 2023 [1], E-Government-Strategie 2024–2027 [16], Strategie Digitale Schweiz 2025 [61], E-ID-Gesetz 2024 [56]), Deutschlands (OZG 2017/2024 [2], ZenDiS-Mandat [47], openCode.de [10]) und der Europäischen Union (Interoperable Europe Act 2024 [6], EU Open Source Strategy 2020–2023 [5], EU-Datengesetz 2023 [51], Datenverwaltungsgesetz 2022 [52]).

**Technologie-Stack-Bewertung** anhand einer strukturierten Bewertungsmatrix für jede Komponente nach: (a) Lizenzoffenheit, (b) Deployment-Reife, (c) Community-Gesundheit, (d) Interoperabilitätsstandardkonformität, (e) Sicherheitsposition, (f) Gesamtbetriebskosten und (g) bestehende Einsätze im öffentlichen Sektor.

**Gesamtkostenanalyse** auf Basis verfügbarer empirischer Fallstudien aus Frankreich, Italien und Tschechien zur Bereitstellung quantitativer Referenzwerte für die kommunale Budgetplanung.

---

## 3. Literaturauswertung

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische E-Government-Literatur hat sich durch vier breite Phasen entwickelt [30]. Die erste Generation (1995–2005) konzentrierte sich auf die Digitalisierung bestehender Prozesse und die Einrichtung von Behörden-Websites [29]. Die zweite Generation (2005–2012) betonte Online-Leistungserbringung, Bürgerportale und Backoffice-Integration [7]. Die dritte Generation (2012–2020) führte offene Daten, Partizipationsplattformen und mobilitätsorientiertes Servicedesign ein [8]. Die aktuelle vierte Generation (2020–heute) ist geprägt durch Plattform-Regierung, digitale Identitätsinfrastruktur, Datenräume und die Souveränitätswende [45].

Wirtz und Weyrers ganzheitliches E-Government-Reifegradmodell identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz [7]. Lathrop und Ruma argumentierten in *Open Government* (2010) grundlegend, dass Regierungsdaten als Standard öffentlich sein sollten [60]. Der UN E-Government Survey 2022 fand, dass digitale Behördendienste zunehmend zentral für das Vertrauen der Bürger in öffentliche Institutionen sind [29]. Die EPRS-Studie 2023 zu digitaler Souveränität in der öffentlichen Verwaltung [59] konsolidiert den akademischen Konsens: Digitale Souveränität ist nicht durch Grundsatzerklärungen erreichbar, sondern nur durch konkrete Infrastrukturentscheidungen.

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Das Konzept der digitalen Souveränität hat sich von einem akademischen Konzept zu einem politischen Imperativ im europäischen Kontext entwickelt [3, 5, 59]. Die EU Open Source Strategy 2020–2023 etablierte „Teilen und Wiederverwenden" als Kernprinzip [5]. Der Interoperable Europe Act 2024 schafft verbindliche Interoperabilitätsverpflichtungen [6].

Deutschlands **Sovereign Cloud Stack (SCS)**, entwickelt von der Open Source Business Alliance (OSBA) und teilweise vom BMWK gefördert, stellt die konkreteste Realisierung digitaler Souveränität in der Cloud-Infrastruktur dar [3]. SCS bietet eine vollständig quelloffene, selbst betreibbare Cloud-Plattform (OpenStack + Kubernetes + Ceph) [11]. SCS-zertifizierte Cloud-Betreiber wie plusserver und OSISM bieten verwaltetes Hosting an. Die Genossenschaft govdigital eG betreibt SCS-basierte gemeinsame Infrastruktur im Rahmen von Rahmenverträgen, die dem deutschen öffentlichen Vergaberecht entsprechen [23].

Die **EMBAG-Gesetzgebung** der Schweiz, die am 1. Januar 2024 in Kraft trat, verlangt, dass mit öffentlichen Mitteln entwickelte Bundessoftware standardmäßig als Open Source veröffentlicht wird [1]. Sie stellt die Schweiz zu den progressivsten Open-Source-mandatierenden Rechtssystemen weltweit.

Das **EU-Datengesetz** (Verordnung EU 2023/2854), in Kraft ab Januar 2024 und anwendbar ab September 2025, erweitert Souveränitätsverpflichtungen in eine neue Richtung [51]. Kommunen, die Smart-City-Infrastruktur betreiben — Sensoren, intelligente Zähler, vernetzte Mobilität, öffentliches WLAN — müssen die Datenteilungsverpflichtungen des Datengesetzes in diese Systeme eindesignen.

Das **EU-Datenverwaltungsgesetz** (Verordnung EU 2022/868, anwendbar ab September 2023) schafft einen Ermöglichungsrahmen für europäische gemeinsame Datenräume [52]. Kommunen können sich als Datenaltruismusorganisationen registrieren und an europäischen Datenräumen teilnehmen.

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG), 2017 erlassen und 2024 grundlegend reformiert (OZG 2.0), verpflichtet alle deutschen Bundes-, Landes- und Kommunalbehörden dazu, ihre Verwaltungsdienstleistungen online anzubieten [2]. Die OZG-2.0-Reform adressiert Mängel der ersten Generation durch das „Once Only"-Prinzip, den „Einer für Alle"-Ansatz (EfA), BundID und den FITKO-Rahmen [9, 10].

**Umsetzungsstand** Anfang 2025: Der Bund hatte seine 115 priorisierten OZG-Dienste bis Ende 2024 vollständig digitalisiert. Jedoch waren bundesweit nur 196 von 575 landesverwaltlichen Diensten verfügbar — weniger als 34 % des Ziels [62]. Kommunale Dienste liegen weit hinter Landesdiensten zurück.

**BundID**: Rund 5,3 Millionen aktive Konten Ende 2024, circa 6 Millionen bis März 2025, mit 154.000 neuen Konten pro Monat seit Mai 2025 [62]. Die monatliche Anmeldezahl verdoppelte sich 2024 auf 2025 auf 2 Millionen. Trotzdem sind erst 7,5 % der 72 Millionen berechtigten Bürger registriert. Kommunen sollten Keycloak-Identitätsföderationen entwerfen, die BundID als hochsicheren Weg unterstützen und gleichzeitig zugängliche Rückfall-Authentifizierungsabläufe mit klaren Upgrade-Pfaden bereitstellen.

**ZenDiS GmbH** (Zentrum Digitale Souveränität der Öffentlichen Verwaltung) [47] ist der institutionelle Akteur, der das föderale OZG-Mandat mit der praktischen kommunalen Umsetzung verbindet. Im Dezember 2022 vom BMI gegründet, verwaltet ZenDiS OpenDesk und openCode.de. **OpenDesk** — eine kuratierte Open-Source-Arbeitsplatzsuite auf Basis von Nextcloud, Cryptpad, OpenProject, Jitsi, Element und Collabora Office — wurde Ende 2024 offiziell als SaaS gestartet [42]. ZenDiS ist der wichtigste institutionelle Partner für deutsche Kommunen bei der Verfolgung einer Open-Source-Digitaltransformation.

Die **openCode.de-Plattform** [10], mitverwaltet von ZenDiS, bietet ein zentrales Repository für behördliche Open-Source-Software mit über 300 Repositories. Das EfA-Prinzip — einen hochwertigen Dienst einmal bauen und allen Kommunen zur Verfügung stellen — ist die operative Logik von openCode.de und des kooperativen Beschaffungsansatzes.

Das **Fraunhofer IESE** bestätigt in seiner Forschung von 2024 zur kommunalen OSS-Einführung [58]: Die Hindernisse für die kommunale OSS-Adoption sind nicht technischer Natur (die Softwarereife ist ausreichend), sondern organisatorischer und politischer. Personalwiderstand gegen Veränderungen, mangelnde interne OSS-Expertise und Interoperabilitätsherausforderungen mit Landessystemen sind die bindenden Einschränkungen.

### 3.4 Digitale Dienste in Schweizer Kantonen und Bund

Die Bundesstruktur der Schweiz schafft sowohl Herausforderungen als auch Chancen für die kommunale Digitaltransformation. Wichtige digitale Infrastrukturen umfassen Fedlex, opendata.swiss [44], GEVER [43] und die E-Government-Strategie Schweiz 2024–2027 [16].

**eCH-Standards** [49] sind das Schweizer Äquivalent zur deutschen XÖV/KoSIT-Standardfamilie. Der Verein eCH fördert, entwickelt und verabschiedet E-Government-Standards für die Schweiz, die elektronische Zusammenarbeit zwischen Behörden, Unternehmen und Privatpersonen ermöglichen. Die Standards haben den formellen Status von Empfehlungen, können aber von Bund, Kantonen und Gemeinden für verbindlich erklärt werden. Wichtige eCH-Standards für Kommunen:
- **eCH-0007**: Historisiertes Gemeindeverzeichnis
- **eCH-0010**: Postadressformat
- **eCH-0044**: Personenidentifikation
- **eCH-0058**: Zustellschnittstelle für sichere Dokumentenzustellung zwischen Behörden
- **eCH-0211**: Baubewilligung — ermöglicht Datenaustausch zwischen Gemeinden und Kantonen (Referenzimplementierung Kanton Zürich)

Die **Schweizer E-ID** [56] stellt eine transformative Entwicklung für kommunale digitale Dienste dar. Das BGEID wurde am 20. Dezember 2024 vom Parlament verabschiedet und am 28. September 2025 in einer Volksabstimmung mit 50,39 % Ja-Stimmen gebilligt — ein knapper Sieg nach der Ablehnung des privatrechtlichen Modells 2021 (64,4 % Nein). Das System ist vollständig staatlich verwaltet, ohne zentrale Datenspeicherung. Budget: 182 Millionen Franken für 2023–2028. Ziel: Verfügbarkeit Sommer 2026. Keycloak-Föderationen in Schweizer Kommunen sollten für die Integration mit der E-ID geplant werden.

### 3.5 Open-Source-Gemeinschaften und souveräne Technologie

**Decidim** (Barcelona, 2016): Über 400 Deployments in 40 Ländern, darunter Barcelona, Helsinki und der Kanton Schaffhausen [12]. Stärker in Nord- und Westeuropa mit gutem Deutsch-Support.

**CONSUL Democracy** (Madrid, 2015; Stiftung 2019): 250+ weltweite Deployments, 45 Sprachen, über 100 Millionen Bürger [50]. Stärker in der spanischsprachigen Welt. AGPL-3.0. EU OSOR-Fallstudie verfügbar [55]. Für Schweizer und deutsche Kommunen: Decidim ist die primäre Empfehlung aufgrund seiner stärkeren deutschsprachigen Community; CONSUL ist eine valide Alternative für Städte mit südeuropäischen Partnerschaften.

**Matrix/Element** [14]: Dezentrales, E2E-verschlüsseltes Kommunikationsprotokoll. Deutsches BundesMessenger und französisches Tchap basieren auf Matrix.

**Nextcloud** [13]: Die am weitesten verbreitete Open-Source-Dateisynchronisations- und Kollaborationsplattform in der europäischen öffentlichen Verwaltung.

**OpenDesk** [42]: Ende 2024 von ZenDiS gestartet. Komponenten: Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora Office, verfügbar als SaaS.

**GovStack** [48]: Multi-Stakeholder-Initiative von ITU, DIAL, BMZ und Estland. Stellt neun digitale „Baustein"-Spezifikationen bereit: Zahlungen, Register, Identifikation, digitales Messaging, Informationsvermittlung, Einwilligung, E-Signatur, GIS, Terminplanung. Angewendet in Montenegro (Dezember 2024: 25 lokale Selbstverwaltungen), Ruanda, Kenia und Äthiopien. Für Schweizer und deutsche Kommunen bietet GovStack einen Beschaffungs- und Architektur-Referenzrahmen.

### 3.6 Gesamtkostenbelege

**Gendarmerie Nationale Frankreichs — GendBuntu** [53]: Seit 2004 Umstieg auf Linux (Ubuntu) und LibreOffice. Bis Juni 2024: 103.164 Arbeitsplätze (97 % des Computerbestands). Dokumentierte Ergebnisse: ~40 % TCO-Reduktion, ~2 Millionen Euro jährliche Lizenzersparnis. Größte und am längsten laufende dokumentierte Open-Source-Regierungsdesktop-Migration.

**Stadt Toulouse** [54]: 1,8 Millionen Euro Einsparungen über drei Jahre nach Migration von 90 % der kommunalen Desktops auf Open-Source-Lösungen.

**Französische Ministerien** [53]: Elf Ministerien haben LibreOffice auf 500.000 Arbeitsplätzen installiert. Die Region Okzitanien startete 2023 eine Strategie zur digitalen Unabhängigkeit nach signifikantem Anstieg der Microsoft-Vertragskosten.

**Provinz Bozen-Südtirol, Italien**: Desktop-Migration zur Open-Source-Büroanwendung. Zentrales Fazit: „Die korrekte Bewältigung des Personalwiderstands gegen Veränderungen ist der wichtigste Faktor für einen erfolgreichen Übergang." Die technische Implementierung verlief reibungslos.

**Methodologische Anmerkung**: Keine unabhängige Vergleichsstudie deckt den vollständigen Open-Source-vs.-proprietären kommunalen Administrations-Stack ab. Die verfügbare Evidenz fokussiert auf Desktop-/Produktivitätsmigration. Ein vollständiges TCO-Modell muss umfassen: (a) eliminierte Lizenzkosten (typisch 100–300 Euro/Nutzer/Jahr für Produktivsoftware); (b) Implementierungskosten; (c) Hosting-Kosten; (d) Supportverträge; (e) Schulung und Change Management; (f) Ausstiegskosten (null für Open Source vs. erhebliche Lock-in-Prämie für Proprietär); (g) Opportunitätswert der Weiterentwicklung.

**TCO-Fazit**: Verfügbare Belege zeigen konsistent 30–40 % Kosteneinsparungen durch Open-Source-Desktop-Migration. Kooperative Beschaffungsstrukturen (govdigital eG, kantonale IT-Genossenschaften) verteilen Implementierungskosten auf viele Kommunen.

### 3.7 Fallstudien kleiner Kommunen

**eVaka — Espoo, Finnland** [57]: Open-Source-Plattform für frühkindliche Bildungsverwaltung. Geteiltes Ressourcenmodell: mehrere finnische Kommunen bündeln Ressourcen für Training, Wartung und Funktionsupdates. Ergebnis: reduzierte Kosten, beschleunigte Verbesserungen, auf GitHub verfügbar (LGPL-2.1). Finnisches Äquivalent des deutschen EfA-Ansatzes.

**Cityvizor — Tschechische Republik**: Open-Source-Plattform für kommunale Haushalttstransparenz. Modulares Design ermöglicht Adoption durch mehrere Kommunen mit minimalem Anpassungsaufwand. Shared-Governance-Modell analog zur Decidim-Association-Governance.

**Provinz Bozen-Südtirol, Italien**: Desktop-Migration in einem alpinen, mehrsprachigen (Deutsch, Italienisch, Ladinisch) Kontext — relevant für Schweizer Kommunen mit mehrsprachigen Verpflichtungen.

**EfA-Dienste für kleine deutsche Kommunen**: Der OZG EfA-Ansatz adressiert die Herausforderung, dass die meisten deutschen Gemeinden zu klein sind, um eigene Digitaldienste zu entwickeln. Ein Land oder Konsortium entwickelt einmal einen hochwertigen Dienst und macht ihn über openCode.de allen Kommunen verfügbar [10]. Dies ist das wirtschaftlich effizienteste Modell für Gemeinden unter ca. 50.000 Einwohnern.

**Kernerkenntnis**: Die bindende Einschränkung für kleine Kommunen ist nicht technische Kapazität, sondern *kooperative Teilnahme*. Kommunen, die govdigital eG beitreten, an EfA-Konsortien teilnehmen, OpenDesk von ZenDiS übernehmen oder Ressourcen durch kantonale IT-Genossenschaften teilen, erhalten Zugang zu Enterprise-Grade-Open-Source-Fähigkeiten zu einem Bruchteil der Kosten.

### 3.8 ZenDiS und die institutionelle Architektur der deutschen kommunalen digitalen Souveränität

ZenDiS GmbH [47] verdient gesonderte Behandlung als pivotaler institutioneller Akteur. Gegründet im Dezember 2022 vom Bundesinnenministerium (BMI), operiert ZenDiS an der Schnittstelle von föderaler Politik und kommunaler Umsetzung. ZenDiS verwaltet OpenDesk und openCode.de.

Die Beziehung zwischen ZenDiS, govdigital eG [23] und dem Sovereign Cloud Stack [3] schafft ein integriertes institutionelles Ökosystem für digitale Souveränität: ZenDiS kuratiert und verwaltet den Anwendungs-Stack; govdigital eG stellt kooperative Cloud-Infrastruktur (SCS-basiert) bereit; openCode.de dient als gemeinsames Code-Repository. Zusammen bieten diese drei Institutionen deutschen Kommunen einen vollständigen, souveränen digitalen Infrastrukturweg, den keine einzelne Gemeinde allein zusammenstellen muss.

---

## 4. Technologie-Stack-Analyse

### 4.1 Digitale Identität und Authentifizierung

**Empfehlung: Keycloak** (Red Hat / CNCF) [21]

De-facto-Open-Source-IAM für die europäische öffentliche Verwaltung. Implementiert OIDC, OAuth 2.0, SAML 2.0 und FIDO2. Federation mit BundID (DE) und Schweizer E-ID (CH).

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Deployment-Reife | 5 | 10+ Jahre Produktion |
| Community-Gesundheit | 5 | Groß, aktiv, CNCF |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheitsposition | 5 | CVE-reaktionsfähig |
| TCO | 4 | Keine Lizenzkosten; Betriebsexpertise erforderlich |
| Einsätze öff. Sektor | 5 | Weit verbreitet in EU-Behörden |

### 4.2 Dokumentenmanagement und Aktenführung

**Empfehlung: Nextcloud** [13] + **OpenProject** [20]

Für Schweizer Kommunen mit voller GEVER-Konformität: kantonale GEVER-Lösungen (CMI, Fabasoft Community) als Compliance-Schicht; Dokumentenaustausch mit kantonalen Behörden via eCH-0058 [49]. Für deutsche Kommunen: AKDB BayernPortal und Dataport-Komponenten im XÖV/OZG-Rahmen [46].

### 4.3 Workflow-Automatisierung und BPM

**Empfehlung: Camunda Platform 8 Community** [33]

BPMN 2.0-nativ, starke Unterstützung für XÖV-Datenstandards (DE) [46] und eCH-Schnittstellen (CH) [49]. Alternative: Flowable (Apache 2.0) bei Procurement-Einschränkungen.

### 4.4 Bürgerbeteiligung

**Primärempfehlung: Decidim** [12] — 400+ Deployments, AGPL-3.0, starker Deutsch-Support.

**Alternative: CONSUL Democracy** [50] — 250+ Deployments, 45 Sprachen, 100+ Millionen Bürger. AGPL-3.0. EU OSOR Fallstudie [55].

| Kriterium | Decidim | CONSUL Democracy |
|---|---|---|
| Lizenz | AGPL-3.0 | AGPL-3.0 |
| Deployments | 400+ | 250+ |
| Sprachen | 60+ | 45 |
| Deutschen Support | Stark | Mittel |
| EU OSOR Dokumentation | Mittel | Hoch [55] |

**Auswahlhinweis**: Decidim für Schweizer/deutsche Kommunen mit deutschsprachigen Beteiligungsprozessen; CONSUL Democracy bei südeuropäischen Partnerschaften oder für Städte mit bedeutender romanischsprachiger Diaspora.

### 4.5 Kommunikation und Zusammenarbeit

| Komponente | Lizenz | Reifegrad | Hauptvorteil |
|---|---|---|---|
| Matrix/Element [14] | Apache 2.0 | Produktion | E2E-Verschlüsselung, Federation |
| Jitsi Meet [35] | Apache 2.0 | Produktion | Browserbasiert, selbst betreibbar |
| BigBlueButton [34] | LGPL-3.0 | Produktion | Ratssitzungsfokus |
| Nextcloud Talk [13] | AGPL-3.0 | Produktion | Integration mit Dateiverwaltung |

**OpenDesk-Integrationshinweis (Deutschland)**: Alle Kommunikationskomponenten (Jitsi, Element) sind in OpenDesk enthalten [42]. Deutsche Kommunen erhalten diese als Teil des integrierten SaaS-Angebots von ZenDiS [47].

### 4.6 Open-Data-Veröffentlichung

**Empfehlung: CKAN** [22] — Powers opendata.swiss, data.gov, data.gov.uk. Plugin-Architektur für DCAT-AP, DCAT-AP.de, OGD Schweiz. Automatisches Harvesting zu nationalen Katalogen.

**EU-Datenverwaltungsgesetz** [52]: Kommunen, die Open Data via CKAN veröffentlichen, können sich als Datenaltruismusorganisationen registrieren.

### 4.7 Geografische Informationssysteme

- **QGIS** [37] für Geodaten-Editing und -Analyse
- **GeoServer** für OGC-konforme Geodatenpublikation (WMS, WFS, WCS)
- **OpenStreetMap** [36] als kartografische Basisschicht
- swisstopo (CH) / BKG (DE) für offene behördliche Basiskartendaten

### 4.8 Öffentliche Website und Content-Management

- **TYPO3** [19]: Dominant in der deutschsprachigen öffentlichen Verwaltung; BITV 2.0 / WCAG 2.1 AA konform
- **Drupal**: International bewährt; genutzt von der Europäischen Kommission

### 4.9 Cloud-Infrastruktur und Hosting

**Empfehlung: Sovereign Cloud Stack (SCS)** [3, 11]

Vollständig quelloffener Cloud-Stack (OpenStack + Kubernetes + Ceph). Beschaffungsoptionen für Kommunen:
1. **Selbst betrieben** (Kommunen >500.000 mit eigenem Ops-Kapazität)
2. **SCS-zertifizierter Anbieter** (plusserver, OSISM) — verwaltet, souverän
3. **govdigital eG-Gemeinschaftsinfrastruktur** [23] — kooperativ, rahmenvertragskonform
4. **ZenDiS OpenDesk SaaS** [47] — Anwendungsschicht (nur Deutschland)
5. **Kantonale IT-Genossenschaft** (Schweiz)

### 4.10 Referenzarchitektur

```
+----------------------------------------------------------------+
|                    BÜRGER-TOUCHPOINTS                          |
|   TYPO3/Drupal . Decidim/CONSUL . CKAN . Nextcloud-Portal    |
+----------------------------------------------------------------+
|                       DIENSTE-SCHICHT                         |
|   Camunda-Workflows . XÖV/eCH-Formulare . GeoServer . QGIS   |
+----------------------------------------------------------------+
|                   ZUSAMMENARBEIT-SCHICHT                      |
| Nextcloud/OpenDesk . Matrix/Element . Jitsi . OpenProject     |
+----------------------------------------------------------------+
|                     IDENTITÄTS-SCHICHT                        |
|       Keycloak ←→ BundID (DE) / Schweizer E-ID (CH)          |
+----------------------------------------------------------------+
|                   DATEN & OFFENE DATEN                        |
|   CKAN . PostgreSQL . DCAT-AP . eCH/XÖV-Datenstandards       |
+----------------------------------------------------------------+
|                  INFRASTRUKTUR-SCHICHT                        |
| Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph . OSM  |
+----------------------------------------------------------------+

Horizontal: GovStack-Bausteine als Architektur-Referenz [48]
Sicherheit: BSI IT-Grundschutz (DE) [26] / Schweizer ISDS-Rahmen (CH)
Interoperabilität: XÖV [46] (DE) | eCH [49] (CH) | EU EIF [45] | DCAT-AP
```

### 4.11 Grenzüberschreitende Interoperabilitätsstandards

| Standard | Rechtsraum | Funktion | Schicht |
|---|---|---|---|
| XÖV (XPersonenstand, XMeld etc.) [46] | Deutschland | XML-Datenaustausch | Dienst, Daten |
| eCH-0007, -0010, -0044, -0058, -0211 [49] | Schweiz | Datenaustausch, Zustellung | Dienst, Daten |
| DCAT-AP / DCAT-AP.de [22] | EU / Deutschland | Open-Data-Metadaten | Offene Daten |
| EU EIF [45] | Europäische Union | Interoperabilitätsrahmen | Alle Schichten |
| OIDC / SAML2 [21] | International | Identitätsfederation | Identität |
| BPMN 2.0 [33] | International | Workflow-Modellierung | Dienst |
| Matrix-Protokoll [14] | International | Sichere Kommunikation | Kommunikation |
| GovStack-Bausteine [48] | International | Architektur-Referenz | Alle Schichten |

---

## 5. Implementierungsfahrplan

### Phase 0: Fundament (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand bewerten, Koalition aufbauen.

**Liefergegenstände:**
- Lenkungsausschuss Digitale Transformation eingesetzt
- Ist-Zustand-Technologieaudit abgeschlossen
- Stakeholder-Einbindungsplan verabschiedet
- Beschaffungsrahmen etabliert
- Absichtserklärung mit kooperativem IT-Dienstleister
- Datenschutz-Folgenabschätzung eingeleitet

**Entscheidungstor:** Politisches Mandat und Budget bestätigt.

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Die Fundamentschichten aufbauen, von denen alles weitere abhängt.

**Liefergegenstände:**
- SCS-Umgebung betriebsbereit (eigen, SCS-zertifizierter Anbieter oder govdigital eG / ZenDiS)
- Keycloak mit nationalem Identitätssystem föderiert (BundID / Schweizer E-ID)
- Nextcloud Basisbetrieb (oder OpenDesk SaaS für deutsche Kommunen)
- Matrix/Element-Messaging für Personal
- BSI IT-Grundschutz / Schweizer ISDS-Basisdokumentation
- Software Bill of Materials (SBOM) initiiert

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Die ersten fünf bürgernahen Dienste auf offener Infrastruktur migrieren oder aufbauen.

**Liefergegenstände:**
- Fünf meistgenutzte Verwaltungsdienste auf Camunda/XÖV (DE) oder Camunda/eCH (CH)
- TYPO3/Drupal-CMS-Migration abgeschlossen
- Open-Data-Portal (CKAN) mit ersten 20 Datensätzen gestartet
- Decidim oder CONSUL Democracy für ersten Beteiligungsprozess

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Liefergegenstände:**
- Alle Dienste via Keycloak SSO föderiert
- 80 % der Verwaltungsdienste digitalisiert
- Behördenübergreifender Datenaustausch via XÖV/eCH operativ
- Smart-City-IoT-Datenmanagement konform mit EU-Datengesetz [51]

### Phase 4: Optimierung und Community (Monate 22–30)

**Liefergegenstände:**
- Bürger-Zufriedenheitsumfrage (Ziel: NPS > 40)
- Erster Beitrag zu openCode.de / Upstream-Projekten
- Kommunale Open-Source-Community of Practice (≥ 3 Peer-Kommunen)
- TCO-Bericht (initial) veröffentlicht
- Barrierefreiheits-Audit (WCAG 2.1 AA / BITV 2.0)

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Liefergegenstände:**
- Vollständiges Audit aller Softwarekomponenten auf Lizenzkonformität und SBOM
- Datensouveränität zu 100 % auf souveräner Infrastruktur
- Playbook für Replikation durch Nachbarkommunen
- Strategiepapier v1.0 veröffentlicht

### 5.6 Implementierungsspur für kleine Kommunen

Für Kommunen mit weniger als 20.000 Einwohnern (die Mehrheit der europäischen Kommunen) wird eine vereinfachte Spur empfohlen:

**Leitprinzip:** An gemeinsamen Plattformen teilnehmen statt individuelle Implementierungen aufzubauen.

**Spur 0 (Monate 1–2):** Beitritt zu govdigital eG (Deutschland) oder kantonaler IT-Genossenschaft (Schweiz). Sofortiger Zugang zu SCS-basierter Cloud-Infrastruktur und Rahmenverträgen.

**Spur 1 (Monate 2–6):** Übernahme von OpenDesk SaaS von ZenDiS [47] (Deutschland) oder entsprechendem kantonalem Angebot (Schweiz). Nextcloud + Cryptpad + OpenProject + Jitsi + Element + Collabora in einem verwalteten Dienst.

**Spur 2 (Monate 4–9):** EfA-Dienste von openCode.de [10] für bürgernahe Prozesse (Deutschland) oder eCH-konforme kantonale Dienste (Schweiz). Vor Eigenentwicklung immer prüfen, ob EfA-Äquivalente existieren.

**Spur 3 (Monate 6–18):** Decidim oder CONSUL Democracy für ersten Beteiligungsprozess; CKAN starten; Keycloak mit BundID oder Schweizer E-ID integrieren.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Landkarte

| Stakeholder | Primäres Interesse | Einbindungsansatz |
|---|---|---|
| Bürgermeister / Führung | Politischer Erfolg, Kosten, Bürgerzustimmung | Executive Briefing, Fortschritts-Dashboard |
| Gemeinderat | Aufsicht, demokratische Legitimität | Quartalsberichte, öffentliche Ratssitzungen |
| IT-Team der Gemeinde | Technische Machbarkeit, Arbeitsaufwand | Co-Design, Schulung, Community-Mitgliedschaft |
| Vergabestelle | Rechtskonformität, Risiko | Rahmenverträge, rechtliche Briefings |
| Mitarbeitende (Endnutzer) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Change Management, Schulung |
| Bürgerinnen und Bürger | Servicequalität, Datenschutz, Beteiligung | Partizipatives Design via Decidim/CONSUL |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Offene Plattformzugänge, öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de-Teilnahme, Upstream-Beiträge |
| ZenDiS / govdigital eG | Partnerschaft, Deployment | Rahmenvertrag, Dienstvertrag |
| Datenschutzbeauftragte(r) | DSGVO, NIS2, Datengesetz | Privacy-by-Design-Review in jeder Phase |

### 6.2 Beschaffungsrahmen

**1. Dienste beschaffen, keine Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**2. Kooperative Beschaffungsstrukturen nutzen.** govdigital eG [23] und kantonale IT-Genossenschaften bieten Rahmenverträge, die dem öffentlichen Vergaberecht (GWB/Vergaberecht in Deutschland; BöB in der Schweiz) entsprechen. ZenDiS bietet einen direkten SaaS-Weg für OpenDesk [47].

**3. „Public Money? Public Code!"-Prinzip anwenden [4].** Alle unter Vertrag entwickelten Anpassungen müssen unter einer OSI-genehmigten Lizenz auf openCode.de veröffentlicht werden — als Vertragserfordernis.

**4. Gesamtbetriebskosten bewerten.** Ausschreibungsbewertung muss ein 5-Jahres-TCO-Modell umfassen. Referenz: Gendarmerie Nationale (40 % TCO-Reduktion) [53], Toulouse (1,8 Mio. Euro) [54].

**5. Interoperabilitätsstandards vorschreiben.** XÖV [46] (DE), eCH [49] (CH), DCAT-AP [22], GovStack-Baustein-Spezifikationen [48] als disqualifizierende Ausschlussmerkmale bei Nicht-Konformität.

**6. EU-Datengesetz und Datenverwaltungsgesetz beachten.** Smart-City-Beschaffung muss explizite Datengesetz-Konformitätsanforderungen [51] enthalten. DCAT-AP-konforme Open-Data-Infrastruktur sollte DGA-Datenaltruismus-Registrierung [52] als wünschenswerte Zukunftsfähigkeit referenzieren.

### 6.3 Change Management

Open-Source-Übergänge scheitern häufig nicht an technischen Problemen, sondern an menschlichen Faktoren. Fraunhofer IESE [58] und die Bolzano-Erfahrung bestätigen: Personalwiderstand gegen Veränderungen ist der wichtigste Faktor.

**Empfehlungen:**
- Einen **Digitaltransformations-Champion** auf Senior-Politikebene ernennen mit plattformübergreifendem Kontinuitätsplan
- **Open-Source-Champions** in jeder Abteilung mit Fortbildung und Peer-Support-Rolle etablieren
- **Parallelbetrieb** für mindestens drei Monate vor Abschaltung kritischer Systeme
- Frühe Erfolge dokumentieren und feiern
- Schulungsbudget: mindestens 15 % des Gesamtprojektbudgets

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|
| Politischer Kurswechsel nach Wahl | Mittel | Hoch | In Satzung/Verordnung verankern; parteiübergreifenden Konsens aufbauen; institutionelle Abhängigkeiten schaffen (govdigital-eG-Mitgliedschaft) |
| Anbieter-Lobbying / Desinformationskampagnen | Hoch | Mittel | TCO-Belege dokumentieren; Zivilgesellschaft einbinden; FSFE-Unterstützung nutzen |
| Skill-Gap im IT-Team | Hoch | Mittel | Schulungsprogramm (≥15 % des Budgets); kooperativer IT-Dienstleister; Community of Practice |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout mit Entscheidungstoren; XÖV/eCH-Konformitätstests |
| Datenverlust bei Migration | Gering | Kritisch | Vollständiges Backup; Parallelbetrieb; stufenweise Migration; SBOM-Tracking |
| EU-Datengesetz-Konformität (Smart City) | Mittel | Mittel | Smart-City-IoT-Deployments prüfen; offene Protokolle in Beschaffung vorschreiben |
| Nutzerakzeptanzversagen | Mittel | Hoch | Change Management (Abschnitt 6.3); UX-Tests; Schulung; Parallelsysteme |
| Sicherheitsvorf. | Gering | Kritisch | BSI IT-Grundschutz; NIS2 [27]; Pentests bei Phasengatern; SBOM-Pflege |
| Kostenüberschreitung | Mittel | Mittel | Phasengebundenes Budget; kooperative Beschaffung verteilt Risiko |

### 7.2 Der Münchener Warnfall

Das LiMux-Projekt der Landeshauptstadt München (2003–2017) ist der meistzitierte Fall eines groß angelegten kommunalen Open-Source-Übergangs, der rückgängig gemacht wurde. Post-mortem-Analysen identifizieren drei primäre Rückgangsgründe: (a) Politischer Führungswechsel 2014 mit engeren Verbindungen zum proprietären Anbieter; (b) unzureichendes Change Management und Endnutzerschulung; (c) Kompatibilitätsprobleme mit Landessystemen, die keine offenen Standards unterstützten [30]. Die technische Umsetzung war generell erfolgreich.

Der Münchener Fall bestätigt: Politisches Risikomanagement — parteiübergreifender Konsens, legislative Verankerung, institutionelle Abhängigkeiten, die Wahlzyklen überdauern — ist ebenso wichtig wie technische Planung.

### 7.3 Sicherheitsüberlegungen

Das BSI IT-Grundschutz-Rahmenwerk [26] bietet eine umfassende Sicherheitsbasis. Schlüsselanforderungen:
- Regelmäßige Sicherheitsupdates für alle Serverkomponenten mit dokumentiertem Patch-Management
- Authentifizierung auf BSI Authenticator Assurance Level 2 (AAL2) für bürgernahe Dienste
- Datentransport verschlüsselt (TLS 1.3 minimum); Datenspeicherung für sensible Kategorien verschlüsselt
- Penetrationstests bei jedem Phasengate
- Software Bill of Materials (SBOM) für alle Open-Source-Abhängigkeiten
- Vorfallreaktionsplan gemäß NIS2-Pflichten [27]

---

## 8. Schlussfolgerung

Die in diesem Papier ausgewerteten Belege konvergieren auf fünf Erkenntnisse:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift und im Produktionseinsatz bewährt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch quelloffene Software mit dokumentierten Deployments bei Peer-Kommunen erfüllt werden.

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG (Schweiz), OZG 2.0 (Deutschland), Interoperable Europe Act, EU-Datengesetz (anwendbar September 2025) und NIS2 schaffen ein dichtes regulatorisches Geflecht, das proprietäre, anbieterseitig eingesperrte Infrastruktur zunehmend compliance-kostspielig macht.

**3. Der wirtschaftliche Fall ist überzeugend, wenn Gesamtkosten korrekt berechnet werden.** Die 40 % TCO-Reduktion der Gendarmerie Nationale, die 1,8 Millionen Euro Einsparung Toulouse' und das konsistente Muster von 30–40 % Kostensenkungen durch europäische Open-Source-Regierungsmigrationen bieten robuste Referenzwerte.

**4. Erfolg erfordert ebenso viel politische und organisatorische Investition wie technische.** Fraunhofer IESE, die Münchener LiMux-Post-mortems und die Bolzaner Gemeindeexperfahrung konvergieren auf dieselbe Erkenntnis: Personalwiderstand gegen Veränderungen, nicht technisches Versagen, ist das primäre Risiko.

**5. Das institutionelle Ökosystem ist nun reif genug, um kommunale Implementierung in großem Maßstab zu unterstützen.** ZenDiS' OpenDesk (Ende 2024 gestartet), govdigital eGs SCS-basierte Genossenschaftscloud, openCode.des 300+ Repositories und der GovStack-Baustein-Rahmen bieten deutschen Kommunen gemeinsam einen vollständigen, souveränen digitalen Infrastrukturweg. Schweizer Kommunen haben die analoge Unterstützung durch das E-ID-Gesetz (Sommer 2026), eCH-Standards, opendata.swiss und kantonale IT-Genossenschaften.

Städte, die zuerst handeln, profitieren von First-Mover-Vorteilen: kooperative Standards mitgestalten, internes Know-how aufbauen, zum Open-Source-Commons beitragen und Compliance-Kapital aufbauen, das spätere Einsteiger teurer erwerben müssen. Die Einladung ist offen.

---

## Referenzen

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. Bern: Schweizerische Eidgenossenschaft. https://www.fedlex.admin.ch/eli/cc/2023/682/de — [Open Access, CC0]

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. Berlin: BMI. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html — [Open Access, DL-DE/Zero 2.0]

[3] Open Source Business Alliance (OSBA). (2023). *Sovereign Cloud Stack: Technische und Governance-Übersicht*. Berlin: OSBA. https://scs.community/ — [Open Access, CC-BY-SA-4.0]

[4] Free Software Foundation Europe (FSFE). (2017). *Public Money? Public Code!* Berlin: FSFE. https://publiccode.eu/ — [Open Access, CC-BY-SA-4.0]

[5] Europäische Kommission. (2020). *Open Source Software Strategy 2020–2023: Think Open*. Brüssel: Europäische Kommission. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en — [Open Access]

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. Brüssel: Amtsblatt der EU. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400903 — [Open Access, EU-Gesetzgebung]

[7] Wirtz, B. W., & Weyerer, J. C. (2017). Conceptualization and creation of a holistic e-government maturity model. *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Föderale IT-Kooperation — Jahresbericht 2023*. Frankfurt: FITKO. https://www.fitko.de/

[10] openCode.de. (2022). *openCode — Open Source for Government*. Berlin: Digitalservice GmbH des Bundes. https://opencode.de/

[11] Sovereign Cloud Stack Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/ — [Apache 2.0]

[12] Decidim Association. (2021). *Decidim: Freie Open-Source partizipative Demokratie für Städte und Organisationen*. Barcelona: Decidim Association. https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). *Nextcloud für die Verwaltung*. Stuttgart: Nextcloud GmbH. https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation v1.x*. https://spec.matrix.org/ — [Apache 2.0]

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. Bern: Schweizerische Bundeskanzlei. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2023). *TYPO3 in der öffentlichen Verwaltung*. Düsseldorf: TYPO3 Association. https://typo3.org/project/association

[20] OpenProject GmbH. (2023). *OpenProject für die Verwaltung: Open-Source-Projektmanagement*. Berlin: OpenProject GmbH. https://www.openproject.org/ — [GPLv3]

[21] Red Hat / Keycloak Community. (2023). *Keycloak: Open Source Identity and Access Management*. https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). *CKAN: Open Source Data Portal Software*. https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). *govdigital: Genossenschaft für digitale Verwaltung*. Berlin: govdigital eG. https://govdigital.de/

[24] Dataport AöR. (2023). *Dataport: IT-Dienstleister für die öffentliche Verwaltung*. Hamburg: Dataport AöR. https://www.dataport.de/

[26] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2023). *BSI IT-Grundschutz-Kompendium Edition 2023*. Bonn: BSI. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *Richtlinie (EU) 2022/2555 — NIS2-Richtlinie*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555

[29] Vereinte Nationen DESA. (2022). *UN E-Government Survey 2022: The Future of Digital Government*. New York: Vereinte Nationen. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). Digital government evolution: From transformation to contextualization. *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). *Camunda Platform 8 Community Edition*. https://camunda.com/download/ — [Apache 2.0]

[34] BigBlueButton Inc. (2023). *BigBlueButton: Open Source Web Conferencing*. https://bigbluebutton.org/ — [LGPL-3.0]

[35] Jitsi Community. (2023). *Jitsi Meet: Open Source Video Conferencing*. https://jitsi.org/ — [Apache 2.0]

[36] OpenStreetMap Foundation. (2023). *OpenStreetMap*. https://www.openstreetmap.org/ — [ODbL-1.0]

[37] QGIS-Projekt. (2023). *QGIS: Ein freies und quelloffenes geographisches Informationssystem*. https://www.qgis.org/ — [GPL-2.0+]

[39] Cloud Native Computing Foundation (CNCF). (2023). *Kubernetes*. https://kubernetes.io/ — [Apache 2.0]

[41] PostgreSQL Global Development Group. (2023). *PostgreSQL*. https://www.postgresql.org/ — [PostgreSQL-Lizenz]

[42] ZenDiS GmbH / BMI. (2024). *OpenDesk: Der digitale Arbeitsplatz der Bundesverwaltung*. Berlin: ZenDiS GmbH. https://opendesk.eu/ — [AGPL-3.0]

[43] Schweizerisches Bundesarchiv (BAR). (2023). *Geschäftsverwaltung (GEVER) in der Bundesverwaltung*. Bern: BAR. https://www.bar.admin.ch/

[44] opendata.swiss. (2023). *Open Government Data Schweiz*. Bern: Schweizerische Bundeskanzlei. https://opendata.swiss/ — [CC-BY-4.0]

[45] Europäische Kommission. (2017). *Europäischer Interoperabilitätsrahmen (EIF)*. Brüssel: Europäische Kommission. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory — [CC-BY-4.0]

[46] KoSIT. (2023). *XÖV-Standards: XML in der öffentlichen Verwaltung*. Bremen: KoSIT. https://www.xoev.de/

[47] ZenDiS GmbH. (2024). *ZenDiS: Digitale Souveränität gemeinsam gestalten*. Berlin: Zentrum Digitale Souveränität der Öffentlichen Verwaltung GmbH. https://www.zendis.de/

[48] GovStack-Initiative / ITU. (2024). *GovStack: Digitale Bausteine für E-Government*. Genf: Internationale Fernmeldeunion / Digital Impact Alliance. https://www.govstack.global/

[49] eCH-Verein. (2024). *eCH E-Government-Standards*. Zürich: eCH. https://www.ech.ch/ — [Vgl. auch Schweizerische Bundeskanzlei: https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/vorgaben/ech-standards.html]

[50] CONSUL Democracy Foundation. (2024). *CONSUL Democracy: Open Government and E-Participation Web Software*. Madrid: CONSUL Democracy Foundation. https://consuldemocracy.org/ — [AGPL-3.0]

[51] Europäisches Parlament und Rat. (2023). *Verordnung (EU) 2023/2854 über harmonisierte Vorschriften für einen fairen Datenzugang und eine faire Datennutzung (Datengesetz)*. In Kraft: 11.01.2024; Anwendung: 12.09.2025. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854

[52] Europäisches Parlament und Rat. (2022). *Verordnung (EU) 2022/868 über europäische Daten-Governance (Datenverwaltungsgesetz)*. Anwendung ab September 2023. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R0868

[53] Gendarmerie Nationale Frankreich. (2024). *GendBuntu: Fallstudie Open-Source-Desktop-Migration*. Frankreich: Gendarmerie Nationale. Zitiert via: https://yeandel.co.uk/21-migration-case-studies/france-gendarmerie.html

[54] Ville de Toulouse. (2023). *Migration open source — Bilan de la ville de Toulouse*. Toulouse: Direction des Systèmes d'Information. — [Graue Literatur; 1,8 Mio. Euro Einsparungen über 3 Jahre, 90 % Desktop-Migration]

[55] Open Source Observatory (OSOR) / Interoperable Europe. (2023). *Fallstudie: CONSUL Democracy*. Brüssel: Interoperable Europe Portal. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/case-study-consul-democracy — [CC-BY-4.0]

[56] Schweizerischer Bundesrat. (2024). *Bundesgesetz über den elektronischen Ausweis und andere elektronische Nachweise (BGEID)*. Bern: Schweizerische Bundeskanzlei. https://www.eid.admin.ch/ — Parlament: 20.12.2024; Volksabstimmung: 28.09.2025 (50,39 % Ja); Einführung: Sommer 2026

[57] Stadt Espoo. (2023). *eVaka: Open-Source-Frühkindliche-Bildungsmanagement*. Espoo: Digitale Dienste der Stadt Espoo. https://github.com/espoon-voltti/evaka — [LGPL-2.1]

[58] Fraunhofer IESE. (2024). *Der Schlüssel zur digitalen Souveränität: Wie Kommunen Open-Source-Software etablieren können*. Kaiserslautern: Fraunhofer Institut für Experimentelles Software Engineering. https://www.iese.fraunhofer.de/en/media/press/pm-2024-01-24-open-source-software.html

[59] Europäischer Parlamentarischer Forschungsdienst. (2023). *Digitale Souveränität — STOA-Panel*. Brüssel: Europäisches Parlament. https://www.europarl.europa.eu/RegData/etudes/STUD/2023/737128/EPRS_STU(2023)737128_EN.pdf

[60] Lathrop, D., & Ruma, L. (Hrsg.). (2010). *Open Government: Collaboration, Transparency, and Participation in Practice*. Sebastopol: O'Reilly Media. Open-Access-Ausgabe: https://github.com/oreillymedia/open_government — [CC-BY]

[61] Schweizerischer Bundesrat. (2025). *Strategie Digitale Schweiz 2025*. Bern: Schweizerische Bundeskanzlei. https://www.bk.admin.ch/bk/de/home/digitale-transformation-ikt-lenkung/strategie-digitale-schweiz.html

[62] KOMMUNAL / FITKO. (2025). *Behörden-Digimeter 2025: Aktueller Stand der OZG-Umsetzung in Deutschland*. Frankfurt: FITKO / KOMMUNAL. https://kommunal.de/behoerden-digimeter-2025-so-weit-ist-das-ozg

---

*Dieses Dokument wird unter der Creative Commons Attribution 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*
*Bitte zitieren als: Sebastian Graf, Autonomes Büro für Digitale Zivilinfrastruktur (sebk4c@tuta.com)*
*Version 0.2.0 — Zitierfähiger Entwurf — 2026-06-21*
*Wahrheitsquelle: Englisch. Deutsche Übersetzung: dieses Dokument.*
