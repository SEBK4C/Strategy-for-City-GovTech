---
title: "Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvollständiger Entwurf"
date: "2026-06-21"
language: "de"
source-of-truth: false
translated-from: "Doc/en/sovereign-by-design-v0.2.0.md"
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
  - BürgerTechnologie
  - Deutschland-Stack
  - OpenDesk
  - ZenDiS
---

# Souverän by Design: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Englisch (Quelle) · Deutsch (diese Fassung)  
**SPDX-Lizenz-Kennung:** CC-BY-4.0  

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernahste Ebene der demokratischen Verwaltung, stehen jedoch vor einer gravierenden strukturellen Spannung: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellerabhängig und nicht mit dem öffentlichen Interesse vereinbar. Dieses Papier präsentiert eine umfassende Strategie zur Implementierung eines modernen, digitalsouveränen Open-Source-Technologie-Stacks in Städten und Gemeinden. Basierend auf den beispielhaften Praktiken der Schweizer Bundesverwaltung (EMBAG SR 172.019, in Kraft seit 2024), des deutschen OZG-2.0-Reformprogramms, des Sovereign Cloud Stack, der ZenDiS- und OpenDesk-Initiativen sowie der europäischen souveränen Technologiegemeinschaft werden ein grundlagenbasierter Umsetzungsfahrplan, ein Stakeholder-Engagementrahmen und eine Beschaffungsstrategie entwickelt.

Zehn zentrale Technologiekomponenten werden bewertet: Identitätsverwaltung, Dokumentenmanagement, Bürosoftware, Prozessautomatisierung, Bürgerbeteiligung, sichere Kommunikation, Open-Data-Veröffentlichung, Geoinformation, Web-Präsenz und Cloud-Infrastruktur. Wirtschaftliche Belege aus der Schleswig-Holstein-Linux-Migration (30.000 Arbeitsplätze), der Münchner LiMux-Nachanalyse sowie der EU-Erkenntnis, dass jeder in Open Source investierte Euro mindestens vier Euro wirtschaftlichen Mehrwert erzeugt, bestätigen die fiskalische Argumentation. Das EU-Gesetz über interoperable Europa (Verordnung (EU) 2024/903, in Kraft April 2024) und Deutschlands NIS-2-Umsetzungsgesetz (in Kraft Dezember 2025) schaffen verbindliche rechtliche Verpflichtungen, die proprietäre Systeme dauerhaft nicht erfüllen können.

Das Papier bietet einen phasenbasierten 36-Monats-Umsetzungsfahrplan mit konkreter Beschaffungsanleitung und EU-Förderwegen für alle relevanten Stakeholder.

**Schlüsselwörter:** digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitalisierung, Interoperabilität, OZG 2.0, EMBAG, Sovereign Cloud Stack, OpenDesk, Deutschland-Stack, E-Government, Civic Technology

---

## 1. Einleitung

Die digitale Transformation der kommunalen Verwaltung ist keine Option mehr. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienstleistungen; Regulierungsbehörden verlangen Interoperabilität und Datenschutz; und Haushaltszwänge erfordern nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Stadtverwaltungen in einem Kreislauf aus proprietärer Herstellerabhängigkeit, teuren Lizenzverträgen und fragmentierten Systemen gefangen, die gute Verwaltung eher behindern als ermöglichen [1, 29].

Die Folgen sind gut dokumentiert: Herstellerbindung erhöht Wechselkosten und Verhandlungsasymmetrie [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch und die Transparenz [45]; geschlossene Infrastruktur verhindert unabhängige Sicherheitsprüfungen [26]; und wiederkehrende Lizenzgebühren belasten Haushalte, die andernfalls für die Leistungserbringung genutzt werden könnten [3, 5].

Ein anderer Weg ist möglich und erprobt. Die Schweizer EMBAG-Gesetzgebung (SR 172.019, in Kraft 1. Januar 2024) verpflichtet dazu, mit öffentlichen Mitteln entwickelte Software standardmäßig als Open Source zu veröffentlichen [1]. Das OZG 2.0 (in Kraft 24. Juli 2024) verpflichtet öffentliche Beschaffer zur Priorisierung von Open-Source-Lösungen [2]. Der Sovereign Cloud Stack erreichte Release 8 im April 2025 [55], und die OpenDesk-Bürosuite — verwaltet von der ZenDiS GmbH — überschritt 100.000 Nutzende [42, 50]. Schleswig-Holstein migriert 30.000 Arbeitsplätze auf Linux, LibreOffice, Nextcloud und offene Standards [51]. Das EU-Gesetz über interoperable Europa (April 2024) schafft verbindliche grenzüberschreitende Interoperabilitätsverpflichtungen [6].

Wirtschaftlich ist die Rückkehr zu Windows nach Münchens LiMux-Projekt auf geschätzte 100 Millionen Euro veranschlagt worden [56] — eine Zahl, die die wahren Kosten einer proprietären Abhängigkeit verdeutlicht. Die EU berechnet, dass jeder in Open Source investierte Euro mindestens vier Euro wirtschaftlichen Mehrwert in Europa erzeugt [62].

### 1.1 Geltungsbereich und Definitionen

*Kommunale Verwaltung* bezeichnet städtische und lokale Behörden, einschließlich Gemeinden, Kommunen, Städte und äquivalente Strukturen in Schweizer Kantonen. Die Strategie skaliert von kleinen Gemeinden (5.000–50.000 Einwohnende) bis zu Großstädten (500.000+).

*Open-Source-Technologie-Stack* bezeichnet Softwarekomponenten unter OSI-genehmigten Lizenzen, betrieben auf Infrastruktur, die die Gemeinde kontrolliert oder ohne unzumutbare Kosten verlassen kann.

*Digitale Souveränität* ist die Fähigkeit einer Verwaltung, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu prüfen, anzupassen, zu prüfen und ohne Herstellerabhängigkeit zu migrieren [3].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Technologie-Stack für Kommunalverwaltungen im Jahr 2026 aus?
2. Welche Lehren können aus den Erfahrungen der Schweiz, Deutschlands und der europäischen souveränen Technologiegemeinschaft gezogen werden?
3. Wie gestaltet sich der optimale, phasenbasierte Umsetzungsweg für eine Stadtverwaltung mit 50.000–500.000 Einwohnenden?
4. Wie sollten Beschaffung, Stakeholder-Einbindung, Risikomanagement und EU-Fördermittelzugang gestaltet werden, um die Erfolgswahrscheinlichkeit zu maximieren?

---

## 2. Methodik

Dieses Papier verwendet einen multi-methodischen Forschungsansatz:

**Systematische Literaturübersicht** über Peer-reviewed-Publikationen, Graue Literatur und Politikdokumente (2010–2026) zu E-Government, digitaler Souveränität, Open-Source-Software in der öffentlichen Verwaltung und kommunaler digitaler Transformation.

**Vergleichende Politikanalyse** zu Technologiegesetzgebung und Strategien der Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027, eCH-Standards), Deutschlands (OZG 2.0 2024, Deutsche Verwaltungscloud-Strategie, Deutschland-Stack 2025) und der EU (Interoperables-Europa-Gesetz 2024, KI-Verordnung 2024, NIS2 2022/2025, Programm Digitales Europa 2021–2027).

**Technologie-Stack-Bewertung** anhand einer strukturierten Bewertungsmatrix für jede Komponente: (a) Lizenzoffenheit, (b) Einsatzreife, (c) Community-Gesundheit, (d) Interoperabilitätsstandards, (e) Sicherheitspostur, (f) Gesamtbetriebskosten (TCO), (g) öffentlich-sektorale Einsatze.

**Wirtschaftliche Analyse** auf Basis veröffentlichter Kostendaten aus München (LiMux), Schleswig-Holstein und EU-weiten Bewertungen wirtschaftlicher Open-Source-Effekte.

Die Literaturübersicht ist für kontinuierliche Verbesserung ausgelegt: Das Quellenverzeichnis (`Mem/source-registry.md`) und der Literaturübersichts-Status (`Mem/literature-review-state.md`) werden regelmäßig aktualisiert.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie: (a) Open-Source-Software in der öffentlichen Verwaltung behandeln; (b) Strategien zur digitalen Verwaltungstransformation thematisieren; (c) den europäischen, schweizerischen oder deutschen Regulierungskontext betreffen; oder (d) Primärdaten zu kommunalen Technologieimplementierungen liefern.

### 2.2 Einschränkungen

Dies ist ein zitationsvollständiger Entwurf (v0.2.0). Alle Zitate wurden gegen Primärquellen verifiziert oder deutlich als ausstehend markiert. Technologie-Stack-Bewertungen spiegeln öffentlich verfügbare Informationen vom Juni 2026 wider. Implementierungskostenschätzungen sind indikativ.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische E-Government-Literatur hat sich in vier Phasen entwickelt [30]. Erste Generation (1995–2005): Digitalisierung bestehender Prozesse und Webpräsenzen. Zweite Generation (2005–2012): Online-Dienstleistungserbringung, Bürgerportale und Back-Office-Integration [7]. Dritte Generation (2012–2020): Open Data, Beteiligungsplattformen und Mobile-First-Servicedesign [8]. Die aktuelle vierte Generation (2020–heute) ist gekennzeichnet durch Plattform-Government, digitale Identitätsinfrastruktur, Datenräume und den Souveränitätswandel — die Erkenntnis, dass digitale Autonomie eine Voraussetzung für demokratische Selbstverwaltung ist [45].

Die GovStack-Initiative (ITU/DIAL) bietet einen Bausteinrahmen für die digitale Verwaltung, der eng mit dem in Abschnitt 4 vorgestellten Open-Source-Stack korrespondiert [53]. GovStack's Cloud-Infrastruktur-Bausteinspezifikation wurde formell in die Sovereign-Cloud-Stack-Community integriert [55].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Digitale Souveränität ist vom akademischen Konzept zur politischen Notwendigkeit geworden [3, 5]. Die EU-Open-Source-Strategie 2020–2023 etablierte "Teilen und Wiederverwenden" als Kernprinzip [5]. Das Interoperables-Europa-Gesetz (Verordnung (EU) 2024/903, in Kraft 11. April 2024, materielle Pflichten ab 12. Januar 2025) schafft verbindliche grenzüberschreitende Interoperabilitätsverpflichtungen und unterstützt ausdrücklich freie Open-Source-Software [6]. Das Europäische Parlament und der Rat haben 77 Millionen Euro im Arbeitsprogramm Digitales Europa 2025–2027 für die Umsetzung bereitgestellt [6, 62].

Der **Sovereign Tech Fund** (STF GmbH) der deutschen Bundesregierung hat bis Ende 2024 rund 23,5 Millionen Euro in über 60 kritische Open-Source-Projekte investiert, bei einem Jahresbudget von 17 Millionen Euro [49].

Der **Sovereign Cloud Stack (SCS)** erreichte Release 8 am 9. April 2025 [55]. Obwohl die BMWK-Projektförderung im Dezember 2024 endete, werden Standards und Referenzimplementierung von Unternehmen und Organisationen weiterentwickelt. Mehr als ein halbes Dutzend Anbieter betreiben Produktionsclouds auf SCS-Basis [55].

Die **KI-Verordnung** (Verordnung (EU) 2024/1689, in Kraft August 2024) und das **NIS-2-Umsetzungsgesetz** (in Kraft 5. Dezember 2025) schaffen neue Verpflichtungen für öffentliche Verwaltungen. KI-Systeme in der öffentlichen Verwaltung für bürgerbezogene Entscheidungen gelten als Hochrisiko-KI-Systeme [64]. Das NIS-2-Umsetzungsgesetz macht IT-Grundschutz-basiertes Risikomanagement für Bundesbehörden und öffentlich organisierte IT-Dienstleister verpflichtend [57].

### 3.3 Das deutsche OZG-Ökosystem

Das Onlinezugangsgesetz (OZG, 2017), in der Reform von 2024 als OZG 2.0 (in Kraft 24. Juli 2024) erheblich gestärkt, verpflichtet alle Verwaltungsebenen zur Digitalisierung ihrer Verwaltungsleistungen [2]. OZG 2.0 führt einen Rechtsanspruch auf digitale Verwaltungsleistungen ab 2029 ein und verpflichtet öffentliche IT-Beschaffer, "Open-Source-Lösungen und offene Standards zu bevorzugen" [2, 47].

Der Umsetzungsfortschritt war bis Ende 2023 hinter den Erwartungen zurückgeblieben: Nur 81 von 581 Leistungen waren vollständig digitalisiert [2]. OZG 2.0 begegnet dem durch verstärktes Monitoring (unabhängige wissenschaftliche Evaluation alle drei Jahre) und die Einführung der DeutschlandID auf Basis von BundID und eID [2].

Die **Deutsche Verwaltungscloud (DVC)** wurde im März 2025 symbolisch auf der Fachkonferenz des IT-Planungsrats gestartet [2, 23]. Der **Deutschland-Stack** aus dem Koalitionsvertrag 2025 setzt OpenDesk, SCS, DVC und Interoperabilität mit Est-lands X-Road als integrierte Bausteine nationaler digitaler Infrastruktur mit Zieldatum 2028 [54].

**Dataport AöR** (für Hamburg, Schleswig-Holstein, Bremen, Mecklenburg-Vorpommern, Sachsen-Anhalt, Thüringen) und **AKDB** (für Bayern) sind die kooperativen IT-Dienstleister für die meisten deutschen Kommunen. Dataport plant den Einsatz einer Matrix-basierten Lösung für bis zu 500.000 Nutzende in Schleswig-Holstein und Hamburg [59].

### 3.4 Schweizerische kantonale und Bundesdigitalleistungen

Das EMBAG (SR 172.019, in Kraft 1. Januar 2024) ist wegweisende Open-Source-Gesetzgebung. Schlüsselartikel: Art. 3 (Digital by Default); Art. 9 (Open-Source-Veröffentlichungspflicht für behördlich finanzierte Software); Art. 10 (Open Data by Default); Art. 12–15 (Standards, Schnittstellen, Interoperabilität) [1].

Die **eCH-Vereinigung** publiziert Schweizer E-Government-Standards, die Datenformate, Schnittstellen und Prozesse für die kantonale und kommunale Digitalverwaltung definieren [47] — das Schweizer Äquivalent zu Deutschlands XÖV-Standards. Die **Schweizer eID** (post-Volksabstimmung 2021) bietet eine staatlich betriebene, datenschutzfreundliche digitale Identität, die künftig kantonal Lösungen ersetzt und mit eIDAS 2.0 interoperiert [16].

Wichtige Schweizer Digitalinfrastruktur umfasst: **Fedlex** (maschinenlesbare Bundesgesetzgebung), **opendata.swiss** (nationales Open-Government-Data-Portal, CKAN-basiert) [44], **GEVER** (standardisierte Aktenverwaltung, BAR-verpflichtend für die Bundesverwaltung) [43], und die **E-Government-Strategie Schweiz 2024–2027** [16].

### 3.5 Fallstudien zur Open-Source-Kommunaltransformation

#### 3.5.1 Schleswig-Holstein: Systemweite Migration

Schleswig-Holstein repräsentiert die ambitionierteste laufende Open-Source-Migration im öffentlichen Sektor Europas. Im April 2024 kündigte das Land die Migration von 30.000 Beamtenarbeitsplätzen von Windows/Microsoft Office auf Linux, LibreOffice, Nextcloud und Thunderbird an [51]. Im Oktober 2025 schloss das Land die E-Mail-Infrastrukturmigration ab: über 40.000 Postfächer wurden von Microsoft Exchange und Outlook auf Open-Xchange und Thunderbird umgestellt [51]. Nextcloud wählte Schleswig-Holstein als "Umsetzungs-Vorbild" für digitale Souveränität aus [58].

#### 3.5.2 Barcelona: Decidim und Open Data

Barcelonas Digitale Souveränitätsstrategie (Digitaler Plan 2017) verbindet die Decidim-Beteiligungsplattform mit Open-Data-Veröffentlichung und Open-Source-Präferenz in der Beschaffung [12]. Decidim wurde von Barcelona entwickelt und als Open Source veröffentlicht; heute wird es in Helsinki, New York, dem Kanton Schaffhausen und hunderten weiterer Organisationen weltweit eingesetzt [12].

#### 3.5.3 Frankreich: Île-de-France und nationale Initiativen

Die Region Île-de-France hat eine Nextcloud-basierte souveräne Cloud-Plattform für 550.000 Schülerinnen, Schüler und Mitarbeitende eingeführt [58]. Frankreichs Tchap-Messaging-App (Matrix-basiert) dient Regierungsangestellten. Der französische KI-Assistent "Albert" läuft auf souveräner Infrastruktur mit Open-Source-Modellen [64].

#### 3.5.4 München LiMux: Lehren aus dem Rückschritt

Münchens LiMux-Projekt (2003–2017) migrierte rund 14.800 von 29.000 Beamtenarbeitsplätzen auf Linux und LibreOffice und generierte dokumentierte Einsparungen von über 10 Millionen Euro [56]. Die Rückkehr zu Windows 2017 war durch einen politischen Führungswechsel verursacht — nicht durch technisches Versagen [30]. Die Rückmigrationskosten werden auf rund 100 Millionen Euro geschätzt [56]. Die wichtigste Schlussfolgerung: Digitale Souveränität muss gesetzlich verankert werden, nicht nur in Verwaltungspräferenzen.

### 3.6 Open-Source-Communities und souveräne Technologieanbieter

**Decidim** (Barcelona, 2016) ist die weltweit meistgenutzte Open-Source-Beteiligungsplattform [12]. **Matrix/Element** bietet ein offenes, dezentrales, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll. Der **BundesMessenger** (BWI, Dezember 2023) speichert alle Daten auf behördeneigenen Servern und stellt seinen Quellcode auf openCode.de bereit [59]. Dataport plant Matrix-Einsatz für 500.000 Nutzende [59].

**Nextcloud** meldete 2025 über 500.000 weltweit laufende Server-Instanzen [58]. Neue Behördenkunden umfassen das österreichische BMWET, die Stadt Stuttgart, die Region Île-de-France (550.000 Nutzende) und die dänische Bundesverwaltung [58].

**OpenDesk** (ZenDiS, v1.0 veröffentlicht 20. Oktober 2024) vereint Nextcloud, Collabora Online, OpenProject, Jitsi, Element und CryptPad. Im April 2025 schloss BWI einen Siebenjahresvertrag für den Bundeswehr-Einsatz. Im Juni 2025 kündigte das Robert-Koch-Institut openDesk für 7.000 Nutzende des Bundesgesundheitsministeriums an. Gesamtüber 100.000 Nutzende [42, 50].

**Forgejo** (MIT-Lizenz) wurde vom niederländischen OSPO des Innenministeriums als Grundlage für **code.overheid.nl** ausgewählt — eine selbstgehostete Plattform für öffentliche Open-Source-Software nach dem Prinzip "Public Money? Public Code!" [60].

**TYPO3** betreibt über 35 % der deutschen Behördenwebseiten [19]. Der neue **Government Site Builder (GSB) 11** (2024) ist der Bundesstandard für ministerielle und kommunale Webseiten [19].

### 3.7 Wirtschaftliche Evidenz

Die Europäische Kommission ermittelt, dass jeder in Open Source investierte Euro mindestens vier Euro wirtschaftlichen Mehrwert in Europa generiert [62]. Eine Gemeinde mit 500 Beschäftigten, die Microsoft 365 durch OpenDesk/Nextcloud/LibreOffice ersetzt, eliminiert 50.000–150.000 Euro jährliche Lizenzkosten. Die 100 Millionen Euro teuren LiMux-Rückmigration [56] verdeutlicht die wahren Kosten von Herstellerhängigkeit. Der Sovereign Tech Fund mit 17 Millionen Euro Jahresbudget und 23,5 Millionen Euro kumulativer Investition in über 60 Open-Source-Projekte [49] wirkt als öffentliche Versicherungsprämie für die gemeinsame digitale Infrastruktur.

### 3.8 Forschungslücken

1. **Langzeitige TCO-Studien für kleine Kommunen** bleiben spärlich.
2. **Nutzerforschung** zum Vergleich der Bürgerzufriedenheit mit Open-Source- vs. proprietären Kommunaldiensten fehlt fast vollständig.
3. **KI-Verordnungs-Compliance-Kosten** für Open-Source- vs. proprietäre KI in der Verwaltung sind eine aufkommende Forschungslücke.
4. **Kleingemeinde-Perspektiven** sind unterrepräsentiert.

Siehe `Mem/literature-review-state.md` für die vollständige Lückenanalyse und den Verbesserungsfahrplan.

---

## 4. Technologie-Stack-Analyse

Ein kommunaler Technologie-Stack kann in zehn Funktionsebenen aufgeteilt werden. Die folgende Analyse bewertet die führenden Open-Source-Optionen für jede Ebene anhand der in Abschnitt 2 definierten Kriterien. Alle Komponenten werden mit Stand Juni 2026 bewertet.

### 4.1 Digitale Identität und Authentifizierung

**Funktion:** Authentifizierung von Bürgerinnen/Bürgern und Mitarbeitenden; Identitätsföderation; Single Sign-On (SSO).

**Empfohlene Komponente: Keycloak** (Red Hat / CNCF) [21]

Keycloak ist die De-facto-Standard-IAM-Plattform für die öffentliche Verwaltung. Es implementiert OpenID Connect, OAuth 2.0, SAML 2.0 und FIDO2/WebAuthn und ermöglicht die Föderation mit DeutschlandID/BundID (Deutschland), Schweizer eID und eIDAS 2.0. Eingesetzt von EU-Institutionen, deutschen Ländern und Schweizer Kantonen.

| Kriterium | Bewertung (1–5) | Anmerkungen |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Einsatzreife | 5 | Produktionserprobt, 10+ Jahre |
| Community-Gesundheit | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2 |
| Sicherheitspostur | 5 | CVE-reaktionsfähig, weit geprüft |
| Gesamtbetriebskosten | 4 | Keine Lizenzkosten; Betriebsexpertise erforderlich |
| Öffentliche Einsatze | 5 | Weit verbreitet in EU-Verwaltungen |

### 4.2 Dokumentenmanagement und Aktenführung

**Funktion:** Speicherung, Abruf, Klassifizierung und Aufbewahrung amtlicher Unterlagen; GEVER-konforme Workflows.

**Empfohlene Komponenten: Nextcloud** (kollaboratives Dateimanagement) + **OpenProject** (Projekt- und Aktenverknüpfung) [13, 20]

Für Schweizer Gemeinden mit GEVER-Compliance-Anforderungen liefern kantonale GEVER-Lösungen (CMI GEVER, Fabasoft eGov Community) die Compliance-Schicht, mit Nextcloud als kollaboratives Frontend [43]. Für deutsche Kommunen integriert die OpenDesk-Suite Nextcloud und OpenProject [42].

### 4.3 Bürosoftware

**Funktion:** Textverarbeitung, Tabellenkalkulation, Präsentationen, Echtzeit-kollaboratives Editieren.

**Empfohlene Komponenten: LibreOffice** (Desktop) + **Collabora Online** (Browser-basiert, WOPI-kompatibel) [63]

LibreOffice unterstützt vollständig das ODF-Format (Open Document Format) und ist in Schleswig-Holsteins 30.000-Sitz-Migration und im OpenDesk-Stack integriert [51, 42]. **Open-Xchange** bietet Open-Source-E-Mail, Kalender und Kontakte (Groupware) — von Schleswig-Holstein im Oktober 2025 erfolgreich als Exchange-Ersatz für 40.000+ Postfächer eingesetzt [51].

### 4.4 Prozessautomatisierung und Geschäftsprozessmanagement

**Funktion:** Automatisierung von Verwaltungsabläufen; BPMN-Modellierung, Ausführung und Überwachung.

**Empfohlene Komponente: Camunda Platform Community** [33]

Camunda bietet eine BPMN-2.0-native Workflow-Engine mit starker Unterstützung für komplexe Verwaltungsprozesse und XÖV/eCH-Datenstandards [46, 47]. **Flowable** (Apache 2.0) ist eine leichtgewichtige Alternative bei Lizenzierungsproblemen.

### 4.5 Bürgerbeteiligung

**Funktion:** Konsultation, Partizipativer Haushalt, Initiativsammlung, Deliberationsplattformen.

**Empfohlene Komponente: Decidim** [12]

Decidem ist die weltweit meistgenutzte Open-Source-Beteiligungsplattform. Die Decidim Association veröffentlicht einen Social Contract, der demokratische Werte, Transparenz und offene Beteiligung zusichert. Bestätigte Einsatze: Barcelona, Helsinki, New York, Kanton Schaffhausen [12].

**Alternative:** CONSUL Democracy (Madrid), ebenfalls AGPL-3.0 [48].

### 4.6 Kommunikation und Zusammenarbeit

**Funktion:** Interne Messaging, Videokonferenz, E-Mail; sichere behördenübergreifende Kommunikation.

**Empfohlene Komponenten:**
- **Matrix/Element** für Messaging und sichere behördenübergreifende Kommunikation [14]
- **BundesMessenger** als Referenzimplementierung für deutsche Kommunen [59]
- **Jitsi Meet** oder **BigBlueButton** für Videokonferenzen [34, 35]
- **Open-Xchange** für E-Mail/Groupware
- **Nextcloud Talk** für integrierte Team-Kommunikation [13]

### 4.7 Open-Data-Veröffentlichung

**Funktion:** Veröffentlichung maschinenlesbarer Datensätze; Datenkatalogisierung; API-Zugang; Einhaltung von PSI-/Open-Data-Richtlinien.

**Empfohlene Komponente: CKAN** [22]

CKAN betreibt opendata.swiss, govdata.de, data.europa.eu, data.gov (USA) und data.gov.uk [22]. Seine Plugin-Architektur ermöglicht volle Konformität mit DCAT-AP (EU), DCAT-AP.de (Deutschland) und OGD-Schweiz-Metadatenstandards.

### 4.8 Geoinformationssysteme

**Funktion:** Kartenbasierte Bürgerservices; Stadtplanung; räumliche Datenpublikation.

**Empfohlene Komponenten:** **QGIS** (Desktop/Server) [37] + **GeoServer** + **OpenStreetMap** [36]. Swisstopo und das BKG liefern hochwertige öffentliche Basiskartendaten unter offenen Lizenzen.

### 4.9 Web-Präsenz und Content-Management

**Funktion:** Öffentliche Webseite; Nachrichten; Leistungsverzeichnis.

**Empfohlene Komponenten:**
- **TYPO3 + Government Site Builder (GSB) 11** (deutschsprachig): betreibt über 35 % der deutschen Behördenwebseiten [19]; GSB 11 (2024) ist der Bundesstandard mit BITV-2.0-Konformität
- **Drupal**: starke internationale Bilanz, eingesetzt von der Europäischen Kommission

### 4.10 Code-Hosting und Inner Source

**Funktion:** Versionsverwaltung von Verwaltungssoftware; abteilungsübergreifende Inner-Source-Kollaboration; Open-Source-Veröffentlichung gemäß EMBAG/OZG.

**Empfohlene Komponenten:**
- **Forgejo** (souveräne, selbstgehostete Git-Plattform, MIT-Lizenz) [60]
- **openCode.de** (deutsche Regierungsplattform, ZenDiS-verwaltet) [10]

Forgejo wurde vom niedrländischen OSPO für code.overheid.nl gewählt [60]. Schweizer Gemeinden mit EMBAG-Pflichten und deutsche Kommunen unter OZG 2.0 können eine Forgejo-Instanz betreiben oder direkt zu openCode.de beitragen.

### 4.11 Cloud-Infrastruktur und Hosting

**Funktion:** Rechnen, Speicherung, Netzwerk, Container-Orchestrierung; digitale Souveränität auf Infrastrukturebene.

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11, 55]

SCS bietet einen vollständig offenen Cloud-Stack (OpenStack + Kubernetes + Ceph), der selbst gehostet, von einem kooperativen Anbieter (govdigital eG) betrieben oder bei zertifizierten SCS-Cloud-Betreibern (plusserver, ScaleUp Technologies, OSISM) gebucht werden kann. SCS Release 8 (April 2025) führt SLURP-Upgrade-Flexibilität, Ubuntu 24.04 LTS, OpenStack 2024.2 und aktuelles Kubernetes ein [55]. Die Deutsche Verwaltungscloud (DVC, gestartet März 2025) ermöglicht den Betrieb von Anwendungen über mehrere SCS-Standorte [2].

**Für Gemeinden ohne eigene Cloud-Betriebskapazität:** zertifizierte SCS-Hoster oder govdigital eG für kooperative Beschaffung nutzen [23].

### 4.12 Referenzarchitektur

```
+-----------------------------------------------------------------------+
|                        BÜRGER-KONTAKTPUNKTE                          |
|  TYPO3/GSB11 . Decidim . CKAN . Nextcloud . Forgejo (öffentlich)    |
+-----------------------------------------------------------------------+
|                          SERVICE-SCHICHT                             |
|  Camunda Workflows . XÖV/eCH-Formulare . GeoServer . QGIS Server   |
+-----------------------------------------------------------------------+
|                       KOLLABORATIONS-SCHICHT                         |
|  OpenDesk (Nextcloud + Collabora + OpenProject + Jitsi + Element)   |
|  Open-Xchange (E-Mail/Kalender) . Forgejo (Inner Source)            |
+-----------------------------------------------------------------------+
|                         IDENTITÄTS-SCHICHT                          |
|    Keycloak <-> DeutschlandID/BundID / Schweizer eID / eIDAS 2.0    |
+-----------------------------------------------------------------------+
|                     INFRASTRUKTUR-SCHICHT                            |
|  Sovereign Cloud Stack R8 . Kubernetes . PostgreSQL . Ceph . MinIO  |
+-----------------------------------------------------------------------+
```

Alle Schichten kommunizieren über offene APIs. Datenaustausch erfolgt per XÖV-Standards (Deutschland) [46] oder eCH-Standards (Schweiz) [47]. Die Sicherheits-Governance folgt BSI IT-Grundschutz++ (Deutschland, verpflichtend ab 1. Januar 2026) [57] oder dem Schweizer ISDS-Rahmenwerk. Open-Source-Veröffentlichung von eigenentwickelter Software erfolgt über Forgejo-Instanzen, die an openCode.de oder Schweizer öffentliche Repositories angebunden sind.

---

## 5. Umsetzungsfahrplan

Die Umsetzung ist als 36-monatiges Fünf-Phasen-Programm strukturiert. Jede Phase hat definierte Ergebnisse, Erfolgskriterien und Entscheidungs-Gates. Budgetangaben sind indikativ für eine Gemeinde mit 200–500 IT-nutzenden Mitarbeitenden.

### Phase 0: Grundlegung (Monate 1–3)

**Ziel:** Governance etablieren, Ist-Zustand analysieren, Koalition aufbauen.

**Ergebnisse:**
- Lenkungsausschuss für digitale Transformation gegründet (Stadtführung + IT + Zivilgesellschaft + Datenschutzbeauftragter)
- Technologie-Audit und Abhängigkeitskartierung abgeschlossen
- Stakeholder-Engagementplan verabschiedet
- Beschaffungsrahmen etabliert (Abschnitt 6)
- MoU mit kooperativem IT-Dienstleister (Dataport, AKDB, govdigital eG oder äquivalent)
- Kontakt mit openCode.de / opendata.swiss für Code-Veröffentlichungsweg hergestellt

**Erfolgskriterien:**
- Politisches Mandat gesichert (Gemeinderatsbeschluss oder Verwaltungsentscheidung)
- Budget genehmigt (indikativ: 200.000–500.000 Euro für Phasen 0–1)
- Projektleitung mit ausreichend Seniorität und Mandat benannt

**EU-Förderweg:** Antragsstellung im Rahmen des Programms Digitales Europa; Beratung über das Technical Support Instrument (TSI) [62].

### Phase 1: Identität und Infrastruktur (Monate 4–12)

**Ziel:** Grundlegende Schichten aufbauen, auf denen alles weitere aufbaut.

**Ergebnisse:**
- SCS-Umgebung betriebsbereit (eigener Betrieb oder zertifizierter Hoster)
- Keycloak-Identitätsanbieter deployed und mit DeutschlandID / Schweizer eID föderiert
- OpenDesk-Basisimplementierung für interne Kollaboration (Nextcloud + Collabora + Element)
- Migrations-plan für Open-Xchange oder Thunderbird erstellt
- Forgejo-Instanz für Inner-Source-Codeverwaltung deployed
- BSI IT-Grundschutz++-Basisdokumentation begonnen

**Erfolgskriterien:**
- 100 % der IT-Mitarbeitenden authentifizieren sich über Keycloak-SSO
- Dateispeicherung von proprietärer Cloud auf Nextcloud/OpenDesk migriert
- Verschlüsseltes Messaging (Matrix/Element) betriebsbereit
- Null proprietäre US-Cloud-Abhängigkeiten für interne Kommunikation

### Phase 2: Dienste und Workflows (Monate 10–18)

**Ziel:** Erste bürgerbezogene Leistungen auf offener Infrastruktur realisieren.

**Ergebnisse:**
- Fünf volumenstärkste Verwaltungsleistungen auf Camunda/XÖV- (oder Flowable/eCH-) Stack deployed
- TYPO3 GSB 11 (Deutschland) oder TYPO3/Drupal (Schweiz) CMS-Migration abgeschlossen
- CKAN Open-Data-Portal mit mindestens 20 Datensätzen gestartet; DCAT-AP/OGD-Metadaten-konform
- Decidim-Instanz für ersten Beteiligungsprozess deployed
- Open-Source-Code auf openCode.de oder Schweizer Repository gemäß EMBAG/OZG veröffentlicht

**Erfolgskriterien:**
- 80 % des Ziel-Servicevolumens über neues System
- Kein Rückgang der Servicevedfügbarkeit gegenüber dem Ausgangswert
- Erster Open-Data-Beitrag veröffentlicht

### Phase 3: Integration und Erweiterung (Monate 16–24)

**Ziel:** Alle Schichten integrieren; Serviceabdeckung auf 80 % der Vorgänge ausweiten.

**Ergebnisse:**
- Alle Dienste über Keycloak-SSO föderiert
- Nextcloud mit Dokumentenmanagement-Workflows integriert
- GIS-Schicht betriebsbereit (QGIS + GeoServer) mit offenen Basiskarten
- 80 % der Verwaltungsleistungen gemäß OZG 2.0 / kantonalen Anforderungen digitalisiert
- E-Mail-Infrastruktur auf Open-Xchange + Thunderbird migriert
- KI-Verordnungs-Compliance-Bewertung für KI-Komponenten abgeschlossen

**Erfolgskriterien:**
- Ende-zu-Ende papierlose Leistungserbringung für 80 % der Vorgangstypen
- Erste jährliche Open-Data-Berichterstattung veröffentlicht
- NIS-2/BSI-IT-Grundschutz++-Dokumentation vollständig

### Phase 4: Optimierung und Community (Monate 22–30)

**Ziel:** Nutzererfahrung optimieren; Open-Source-Communities beitragen; Ergebnisse veröffentlichen.

**Ergebnisse:**
- Zufriedenheitsumfrage (Ziel: NPS > 40)
- Mindestens drei Beiträge zu openCode.de / Upstream-Projekten
- Kommunale Open-Source-Community of Practice mit ≥ 3 Peer-Gemeinden aktiv
- TCO-Bericht (Open Access) veröffentlicht

**Erfolgskriterien:**
- Community of Practice aktiv
- Erste Anträge beim Sovereign Tech Fund oder Programm Digitales Europa für Mitfinanzierung

### Phase 5: Souveränität und Skalierung (Monate 28–36)

**Ziel:** Vollständige digitale Souveränität; Replizierung auf Nachbargemeinden vorbereiten.

**Ergebnisse:**
- Vollständige Prüfung: alle Software-Komponenten lizenzkonform; SBOM gepflegt
- Souveräne Datenhaltung auf SCS-Infrastruktur verifiziert
- Playbook für Replikation auf openCode.de veröffentlicht
- Strategiepapier v1.0 veröffentlicht

**Erfolgskriterien:**
- Null proprietäre Single-Vendor-Abhängigkeiten im kritischen Pfad
- Datenhaltung zu 100 % auf souveräner Infrastruktur
- Mindestens eine Peer-Gemeinde hat das Playbook übernommen

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder | Primäres Interesse | Einbindungsansatz |
|---|---|---|
| Bürgermeister / Verwaltungsleitung | Politischer Erfolg, Kosten, Bürgerzufriedenheit | Führungsbriefing, Fortschritts-Dashboard |
| Stadtrat | Kontrolle, demokratische Legitimation | Quartalsberichte, offene Ratssitzungen |
| IT-Team | Technische Machbarkeit, Arbeitsbelastung | Co-Design, Schulung, Community-Mitgliedschaft |
| Vergabestelle | Rechtliche Konformität, Risiko | Rahmenverträge, Rechtsberatung |
| Beamtinnen/Beamte (Endnutzende) | Benutzerfreundlichkeit, Zuverlässigkeit | UX-Tests, Change Management, Schulung |
| Bürgerinnen/Bürger | Servicequalität, Datenschutz | Partizipatives Design, Transparenzberichte |
| Zivilgesellschaft / NGOs | Transparenz, Zugang, Beteiligung | Decidim-Plattform, öffentliche Roadmaps |
| Open-Source-Communities | Beitrag, Wiederverwendung | openCode.de, Upstream-Beiträge |
| Souveräne Technologieanbieter | Partnerschaft, Deployment | Zertifizierte Partnervereinbarungen |
| Datenschutzbeauftragte/r | DSGVO / nDSG-Konformität | Privacy-by-Design-Prüfung in jeder Phase |
| KI-Verordnungs-Compliance | Hochrisiko-KI-Konformität | KI-Inventar, Konformitätsbewertungen |

### 6.2 Beschaffungsrahmen

**1. Dienste beschaffen, keine Lizenzen.** Open-Source-Software ist frei nutzbar; Kommunen zahlen für Implementierung, Hosting, Support, Anpassung und Schulung.

**2. Kooperative Beschaffungsstrukturen nutzen.** **govdigital eG** und Schweizer kantonale IT-Kooperativen bieten Rahmenverträge, die das Vergaberecht (GWB/Vergaberecht in Deutschland; BöB/VöB in der Schweiz) erfüllen [23].

**3. Das Prinzip „Öffentliches Geld? Öffentlicher Code!“ anwenden.** Alle unter Vertrag entwickelte Software muss unter einer OSI-genehmigten Lizenz veröffentlicht und auf openCode.de (Deutschland) oder einer kantonalen öffentlichen Plattform (Schweiz) bereitgestellt werden [4].

**4. Fünfjährige Gesamtbetriebskosten (TCO) bewerten.** Vergabepunkte müssen ein 5-Jahres-TCO-Modell einschließen. Die Münchner Rückmigrationskosten (100 Mio. Euro) [56] und der EU-Multiplikator (4 Euro pro investiertem Euro) [62] sind in der Wirtschaftlichkeitsrechnung zu berücksichtigen.

**5. Interoperabilitätsstandards vorschreiben.** Alle beschafften Systeme müssen implementieren: XÖV (Deutschland) [46], eCH (Schweiz) [47], DCAT-AP (EU), eIDAS 2.0, NIS-2/BSI-IT-Grundschutz++ [57]. Nicht-Konformität ist Ausschlusskriterium.

**6. Zertifizierte kooperative Anbieter bevorzugen.** Für Infrastruktur SCS-zertifizierte Cloud-Betreiber oder govdigital-eG-Mitglieder bevorzugen [23].

### 6.3 EU-Förderwege

**Programm Digitales Europa (DIGITAL, 2021–2027):** 8,1 Milliarden Euro Gesamtvolumen; unterstützt digitale öffentliche Dienste und Interoperabilität. Das Interoperable-Europe-Board stellt 77 Millionen Euro im Arbeitsprogramm 2025–2027 bereit [6, 62].

**Horizont Europa (2021–2027):** 93,5 Milliarden Euro; das Next-Generation-Internet-Programm (NGI) fördert Open-Source-Projekte mit 5.000–50.000 Euro für Code-Verbesserungen [62].

**Sovereign Tech Fund (Deutschland):** 17 Millionen Euro Jahresbudget; fördert kritische Open-Source-Infrastruktur [49].

**Technical Support Instrument (TSI):** EU-finanzierte Beratungsunterstützung für öffentliche Dienstleistungsmodernisierung; keine Kofinanzierung erforderlich.

### 6.4 Change Management

Open-Source-Transitionen scheitern häufig nicht an technischen, sondern an menschlichen Faktoren: Widerstand bei Endnutzenden, unzureichende Schulung, Beharren auf mittlerem Management und politischer Rückschritt unter Herstellerlobbyismus. Der Münchner LiMux-Fall bestätigt: Politisches Risikomanagement ist ebenso wichtig wie technische Planung [30, 56].

**Empfehlungen:**
- **Digital-Transformation-Beauftragte/r** auf politischer Senior-Ebene mit explizitem, parteiübergreifendem Mandat ernennen
- **Open-Source-Champions** in jeder Fachabteilung mit vertiefter Schulung und Peer-Support-Rolle etablieren
- **Parallelbetrieb** mindestens drei Monate vor der Migration kritischer Systeme
- **Frühe Erfolge** (Kosteneinsparungen, neue Fähigkeiten, Bürger-Feedback) dokumentieren und öffentlich kommunizieren
- Öffentliches **Transparenz-Dashboard** mit Migrationsfortschritt, Kosten und Servicequalitätskennzahlen
- Open-Source-Präferenz in kommunaler Satzung oder Gesetz verankern — nicht nur in Verwaltungspräferenzen — um politische Wechsel zu überstehen

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Minderung |
|---|---|---|---|
| Politischer Rückkehr nach Wahl | Mittel | Hoch | In Satzung/Gesetz verankern; parteiübergreifenden Konsens aufbauen |
| Anbieterlobbyismus / Falschinformation | Hoch | Mittel | TCO-Evidenz dokumentieren; Zivilgesellschaft einbinden; Münchner Kosten zitieren |
| Qualifikationslücke im IT-Team | Hoch | Mittel | Schulungsprogramm; kooperativer IT-Anbieter; Community of Practice; Sovereign Tech Fund |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweise Einführung mit Entscheidungs-Gates; Referenzarchitektur-Einhaltung |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup-Protokoll; Parallelbetrieb; stufenweise Migration |
| DSGVO / nDSG-Verletzung | Niedrig | Hoch | Privacy-by-Design; DSB von Phase 0 einbinden; Datenkartierung |
| Benutzerakzeptanzversagen | Mittel | Hoch | Change Management; UX-Tests; Schulung; Parallelsysteme |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz++; Penetrationstests; Incident-Response-Plan; NIS-2-Konformität |
| KI-Verordnungs-Non-Compliance | Mittel | Hoch | KI-Inventar in Phase 0; Konformitätsbewertungen; Open-Source-KI bevorzugen |
| Supply-Chain-Angriff auf Open-Source | Niedrig | Hoch | SBOM-Pflege; Sovereign Tech Fund für kritische Abhängigkeiten; Abhängigkeitsaudit |
| Kostensüberschreitung | Mittel | Mittel | Phasierte Budgetierung; unabhängiges Projektbüro; offene TCO-Buchführung |

### 7.2 Der Münchner Fall

Münchens LiMux-Projekt (2003–2017) migrierte rund 14.800 Arbeitsplätze auf Linux und LibreOffice und erzielte dokumentierte Einsparungen von über 10 Millionen Euro. Die Umkehrentscheidung 2017 wurde primär durch politischen Führungswechsel verursacht, nicht durch technisches Versagen [30]. Die Rückkehr zu Windows wird auf rund 100 Millionen Euro geschätzt [56]. Fazit: Digitale Souveränität muss institutionell verankert werden, nicht nur administrativ präferiert.

### 7.3 KI-Verordnungs-Compliance

Die EU-KI-Verordnung (Verordnung (EU) 2024/1689, Hochrisiko-Bestimmungen anwendbar ab August 2026) klassifiziert KI-Systeme in der öffentlichen Verwaltung für bürgerbezogene Entscheidungen als **Hochrisiko-KI-Systeme** mit Pflichten für: Konformitätsbewertung, Registrierung in der EU-KI-Datenbank, menschliche Aufsicht und Erklärbarkeit [64]. Open-Source-KI-Systeme bieten Strukturvorteile für die Compliance, da Quellcode-Zugang technische Dokumentation für Konformitätsbewertungen ermöglicht.

### 7.4 Sicherheitsanforderungen

Das BSI IT-Grundschutz++-Rahmenwerk (Katalog veröffentlicht 1. Januar 2026, verpflichtend für deutsche Behörden gemäß NIS-2-Umsetzungsgesetz, in Kraft 5. Dezember 2025) [57] liefert die umfassende Sicherheitsbasis. Wichtige Anforderungen:

- Regelmäßige Sicherheitsupdates mit dokumentiertem Patch-Management-Prozess
- Authentifizierung auf BSI-AAL2-Niveau (oder äquivalent) für bürgerbezogene Dienste; FIDO2/WebAuthn bevorzugt
- Daten übertragungssicher: TLS 1.3 Minimum; ruhende Daten: verschlüsselt für sensible Kategorien
- Software Bill of Materials (SBOM) für alle Open-Source-Abhängigkeiten gepflegt
- Penetrationstests an jedem Phasen-Gate
- Incident-Response-Plan gemäß NIS-2-Verpflichtungen

---

## 8. Schlussfolgerungen

Die in diesem Papier geüberprüften Belege konvergieren auf fünf Erkenntnisse:

**1. Open-Source-kommunale Technologie-Stacks sind technisch reif und im Maßstab produktionserprobt.** Jede Funktion einer modernen Stadtverwaltung kann durch Open-Source-Software mit dokumentierten Einsätzen in vergleichbaren Kommunen abgedeckt werden — von Schleswig-Holsteins 30.000-Sitz-Migration bis Île-de-Frankreichs Nextcloud-Plattform für 550.000 Nutzende.

**2. Das Rechtsumfeld schreibt Open Source und Interoperabilität zunehmend vor.** EMBAG Art. 9 (Schweiz, 2024), OZG-2.0-Open-Source-Pflicht (Deutschland, Juli 2024), Interoperables-Europa-Gesetz (EU, April 2024) und deutsches NIS-2-Umsetzungsgesetz (Dezember 2025) schaffen kollektiv ein Umfeld, in dem proprietäre, herstellerabhängige Systeme Rechtsrisiken und Compliance-Schulden erzeugen.

**3. Die wirtschaftliche Argumentation ist überzeugend.** Der EU-Multiplikator von 4 Euro Mehrwert pro investiertem Euro [62], Münchens 100-Millionen-Euro-Rückkehrkosten [56] und der Sovereign Tech Fund mit 23,5 Millionen Euro in 60+ Projekten [49] bilden zusammen das fiskalische Argument.

**4. EU- und nationale Fördermechanismen senken die finanzielle Einstiegsbarriere.** Programm Digitales Europa (77 Millionen Euro earmarked 2025–27), Sovereign Tech Fund (17 Millionen Euro jährlich) und NGI innerhalb von Horizont Europa bieten strukturierte Kofinanzierungswege.

**5. Erfolg erfordert ebenso viel politische und organisatorische Investition wie technische.** Münchens Warnung und Schleswig-Holsteins laufender Erfolg bestätigen: klares politisches Mandat, parteiübergreifender Konsens, qualifiziertes Change Management und dauerhaftes Stakeholder-Engagement sind die bindenden Nebenbedingungen. Die Verankerung der Open-Source-Präferenz in kommunaler Satzung ist die wichtigste verfügbare Risikominderung.

Kommunen, die frühzeitig handeln, werden kooperative Standards prägen, interne Expertise aufbauen und zum Open-Source-Gemeingut beitragen, von dem alle Verwaltungen profitieren. Die Einladung — und zunehmend die Verpflichtung — ist offen.

---

## Quellenverzeichnis

*Alle Referenzen entsprechen denen des englischen Originaldokuments `Doc/en/sovereign-by-design-v0.2.0.md`, Verweise [1]–[64]. Die Quellenverzeichniseinträge sind identisch; die Referenznummern bleiben über beide Sprachversionen konsistent.*

[1] Swiss Federal Council. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. In Kraft ab 2024-01-01. https://www.fedlex.admin.ch/eli/cc/2023/682/de

[2] Bundesministerium des Innern und für Heimat (BMI). (2024). *OZG-Änderungsgesetz (OZG 2.0), in Kraft 2024-07-24*. https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/das-gesetz/ozg-aenderungsgesetz/ozg-aenderungsgesetz-node.html

[3] Open Source Business Alliance (OSBA). (2025). *Sovereign Cloud Stack: Community und Governance-Übersicht*. https://scs.community/

[4] Free Software Foundation Europe (FSFE). (2017). *Öffentliches Geld? Öffentlicher Code!* https://publiccode.eu/

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023: Think Open*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Rat der EU. (2024). *Verordnung (EU) 2024/903 — Interoperables-Europa-Gesetz, in Kraft 2024-04-11*. https://www.consilium.europa.eu/en/press/press-releases/2024/03/04/interoperable-europe-act-council-adopts-new-law-for-more-efficient-digital-public-services-across-the-eu/

[42] ZenDiS GmbH / BMI. (2024). *openDesk v1.0: Der digitale Arbeitsplatz der öffentlichen Verwaltung*. Veröffentlicht 2024-10-20. https://opendesk.eu/en/about

[47] eCH-Verein. (2025). *eCH-Standards für E-Government Schweiz*. https://www.ech.ch/

[49] Sovereign Tech Fund GmbH. (2024). *Sovereign Tech Fund: Investitionen in digitale Infrastruktur*. https://www.sovereigntechfund.de/

[51] Staatskanzlei Schleswig-Holstein. (2024–2025). *Linux-Migration: 30.000 Arbeitsplätze und E-Mail-Migration (Oktober 2025)*. https://www.schleswig-holstein.de/DE/landesregierung/themen/digitalisierung/linux-plus1/Projekt

[54] Deutsche Bundesregierung. (2025). *Koalitionsvertrag 2025: Deutschland-Stack*. https://www.bundesregierung.de/

[55] Sovereign Cloud Stack Community. (2025). *SCS Release 8 — 9. April 2025*. https://sovereigncloudstack.org/announcements/release8/

[56] OSOR / The Register. (2018). *Münchens Rückkehr zu Windows: geschätzte 100 Millionen Euro Kosten*. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/munichs-long-history-open-source-public-administration

[57] BSI. (2025). *NIS-2-Umsetzungsgesetz in Kraft (2025-12-05); IT-Grundschutz++ Katalog ab 2026-01-01*. https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2025/251205_NIS-2-Umsetzungsgesetz_in_Kraft.html

[58] Nextcloud GmbH. (2025). *Nextcloud 2025 Wrap-Up: 500.000 Server, Behördeneinsätze*. https://nextcloud.com/blog/nextcloud-2025-wrap-up/

[59] BWI GmbH / Element / OSOR. (2023–2025). *BundesMessenger: Matrix-basiertes Messaging für die deutsche öffentliche Verwaltung*. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/bundesmessenger-shared-reused-and-interoperable

[60] Niederländisches Innenministerium / OSPO. (2026). *code.overheid.nl: Souveräne Forgejo-basierte Code-Plattform*. https://www.opensourceforu.com/2026/04/dutch-government-backs-forgejo-for-sovereign-open-source-github-alternative/

[62] Europäische Kommission / Interoperable Europe Portal. (2024). *Förderungsmöglichkeiten für Open-Source im öffentlichen Sektor: 1 Euro = 4 Euro Mehrwert*. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/funding-opportunities-open-source-software-projects-public-sector

[64] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/1689 — KI-Verordnung, in Kraft 2024-08-01*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689

---

*Dieses Dokument wird unter der Creative-Commons-Namensnennung 4.0 International Lizenz (CC-BY-4.0) veröffentlicht.*  
*Zitieren als: Sebastian Graf, Autonomes Büro für zivile digitale Infrastruktur (sebk4c@tuta.com)*  
*Veröffentlicht unter: https://github.com/SEBK4C/Strategy-for-City-GovTech*
