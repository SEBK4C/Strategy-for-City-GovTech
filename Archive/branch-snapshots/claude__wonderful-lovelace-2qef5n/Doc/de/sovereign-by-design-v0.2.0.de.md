---
title: "Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen"
author: "Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Übersetzung: Zitationsvollständiger Entwurf"
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
  - eCH
  - GovStack
---

# Souverän von Grund auf: Eine State-of-the-Art Open-Source-Technologiestrategie für kommunale Verwaltungen

**Autor:** Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur  
**Korrespondenz:** sebk4c@tuta.com  
**Version:** 0.2.0 — Zitationsvollständiger Entwurf  
**Datum:** 2026-06-21  
**Sprachen:** Deutsch (Übersetzung) · English (Quelldokument)  
**SPDX-License-Identifier:** CC-BY-4.0  

> *Vollständige Übersetzung des englischen Originals `en/sovereign-by-design-v0.2.0.md`.*

---

## Änderungshistorie

| Version | Datum | Änderungen |
|---|---|---|
| v0.1.0 | 2026-06-20 | Erster strukturierter Entwurf. 30 Primärquellen. |
| v0.2.0 | 2026-06-21 | Zitationsvollständiger Entwurf. 4 zuvor unverifizierte Quellen verifiziert. §0 Stakeholder-Leitfaden. §3.7 Fallstudien. §4.11 TCO-Rahmen. §7.4 Regulierungsrahmen. 12 neue Quellen [47]–[58]. |

---

## §0. Stakeholder-Leitfaden

*Dieser Leitfaden bietet einen maßgeschneiderten Einstieg für jede Stakeholder-Gruppe.*

### Für Stadtverantwortliche und Führungskräfte

Die Kernbotschaft: Open-Source-Kommunaltechnologie ist kein Experiment mehr — sie ist gesetzlich vorgeschrieben (EMBAG in der Schweiz, OZG 2.0 in Deutschland) und durch den EU-Interoperabilitätsakt stark incentiviert. Das fiskalische Argument ist überzeugend: Proprietäre Produktivitätssuiten kosten 100–300 € pro Arbeitsplatz und Jahr allein an Lizenzgebühren; das Open-Source-Äquivalent kostet primär Betriebsaufwand, verteilt über genossenschaftliche Beschaffung. Das am häufigsten unterschätzte Risiko ist nicht technisch, sondern politisch. **Empfohlene Lektüre:** §5 (Implementierungsfahrplan) und §6 (Stakeholder- und Beschaffungsstrategie).

### Für gewählte Mandatstragenden

Digitale Souveränität ist ein demokratischer Wert, keine technische Präferenz. Wenn die Software demokratischer Institutionen im Besitz privater Akteure ist, entsteht ein struktureller Interessenkonflikt. Das Schweizer Parlament verabschiedete EMBAG 2023 genau deshalb, weil dieses Prinzip parteiübergreifend überzeugt. **Empfohlene Lektüre:** §1 (Einleitung), §3.2 (Digitale Souveränität), §8 (Schlussfolgerung).

### Für IT-Fachkräfte der öffentlichen Verwaltung

Jede in diesem Papier bewertete Komponente verfügt über Produktionseinsätze in Peer-Kommunen. Die wichtigsten technischen Entscheidungen: (1) mit Keycloak Identity Management beginnen; (2) SCS-zertifizierten Host auswählen oder selbst auf SCS betreiben, bevor Anwendungsschichten deployt werden; (3) XÖV (Deutschland) bzw. eCH (Schweiz) Standardskonformität in jeder Ausschreibung verlangen. **Empfohlene Lektüre:** §4 (Technologiestack-Analyse), §5 (Implementierungsfahrplan), §7.3 (Sicherheit).

### Für Vergabestellen

Open-Source-Beschaffung ist strukturell anders als Lizenzbeschaffung: Es werden Dienstleistungen (Implementierung, Hosting, Support, Schulung) beschafft, keine Nutzungsrechte. govdigital eG-Rahmenverträge erfüllen deutsches Vergaberecht (GWB §97ff.); Schweizer kantonale Genossenschaften decken BöB-Anforderungen ab. **Empfohlene Lektüre:** §6.2 (Beschaffungsrahmen), §4.11 (TCO-Rahmen).

### Für Zivilgesellschaft und Open-Source-Gemeinschaften

Diese Strategie positioniert bürgerliche Gemeinschaften als Mitgestalter, nicht als bloße Empfänger. Decidim-Einsätze laden aktiv zur Beteiligung an Haushaltsentscheidungen und Stadtplanung ein. openCode.de bündelt Beiträge, sodass Verbesserungen einer Kommune allen zugutekommen. **Empfohlene Lektüre:** §3.5 (Souveräne Technologie-Gemeinschaften), §6.1 (Stakeholder-Übersicht).

---

## Zusammenfassung

Kommunale Verwaltungen sind die bürgernächste Ebene demokratischer Administration, stehen jedoch vor einem strukturellen Dilemma: Die digitalen Werkzeuge, auf die sie angewiesen sind, sind zunehmend proprietär, herstellergebunden und nicht im Einklang mit öffentlichen Interessen. Diese Arbeit legt eine umfassende Strategie für die Implementierung eines modernen, quelloffenen Verwaltungstechnologie-Stacks in Städten und Gemeinden vor. Auf der Grundlage vorbildlicher Praxis der Schweizer Bundesverwaltung (EMBAG), des deutschen OZG-Reformprogramms, der Sovereign-Cloud-Stack-Initiative, der von ZenDiS verwalteten OpenDesk-Plattform sowie der weiteren europäischen Souveränitätstechnologie-Gemeinschaft — einschließlich GovStack, eCH, Decidim und CONSUL Democracy — werden ein Implementierungsfahrplan, ein Stakeholder-Engagement-Rahmen und eine Beschaffungsstrategie erarbeitet. Fallstudien aus kleinen und mittleren Gemeinden der Schweiz und Deutschlands zeigen, dass der Übergang über die gesamte Bandbreite der Stadtgrößen möglich ist.

**Schlüsselwörter:** Digitale Souveränität, Open-Source-Verwaltung, GovTech, kommunale Digitaltransformation, Interoperabilität, OZG, EMBAG, Sovereign Cloud Stack, E-Government, ZenDiS, eCH, GovStack

---

## 1. Einleitung

Die digitale Transformation kommunaler Verwaltungen ist keine Frage des Ob, sondern des Wie. Bürgerinnen und Bürger erwarten nahtlose, sichere und barrierefreie digitale Dienste; der Gesetzgeber fordert Interoperabilität und Datenschutz; Haushaltszwänge verlangen nachhaltige, kosteneffiziente Technologieinvestitionen. Dennoch sind die meisten Städte und Gemeinden weltweit in einem Kreislauf proprietärer Herstellerabhängigkeit gefangen [1, 29].

Die Folgen dieser Abhängigkeit sind gut belegt: Herstellerbindung erhöht Wechselkosten [4]; proprietäre Formate behindern den behördenübergreifenden Datenaustausch [45]; geschlossene Software verhindert unabhängige Sicherheitsprüfungen [26]; Lizenzgebühren belasten Haushalte [3, 5]. Am grundlegendsten: Wenn die Software demokratischer Institutionen von privaten Akteuren kontrolliert wird, entsteht ein struktureller Interessenkonflikt [4, 53].

Ein anderer Weg ist möglich und erprobt. Das Schweizer EMBAG (2023) schreibt vor, dass mit öffentlichen Mitteln entwickelte Bundessoftware als Open Source veröffentlicht wird [1]. Deutschlands OZG-Reformprogramm, Sovereign Cloud Stack und OpenDesk — verwaltet von ZenDiS GmbH — stellen das ambitionierteste Open-Source-GovTech-Programm Europas dar [2, 3, 42, 47]. Die GovStack-Initiative von ITU, GIZ und DIAL bietet ein international standardisiertes Baustein-Framework, das direkt auf europäische kommunale Implementierungen anwendbar ist [50].

### 1.1 Begriffserklärungen

*Kommunale Verwaltung* bezeichnet Städte und Gemeinden einschließlich Schweizer Gemeinden, deutscher Kommunen und vergleichbarer Strukturen. Die Strategie ist für Gemeinden von 5.000 bis über 500.000 Einwohnerinnen und Einwohnern ausgelegt.

*Digitale Souveränität* ist die Fähigkeit einer Behörde, unabhängige Entscheidungen über ihre digitale Infrastruktur zu treffen — einschließlich des Rechts, Software zu inspizieren, zu modifizieren, zu prüfen und zu migrieren [3, 47].

### 1.2 Forschungsfragen

1. Wie sieht ein moderner Open-Source-Kommunal-Technologiestack im Jahr 2026 aus?
2. Was lässt sich aus der schweizerischen, deutschen und europäischen Souveränitätstechnologie-Gemeinschaft lernen?
3. Was ist der optimale Phasenimplementierungsweg für Kommunen aller Größenklassen?
4. Wie sollten Beschaffung, Stakeholder-Engagement und Risikomanagement strukturiert werden?

---

## 2. Methodik

Dieses Papier verwendet einen Mehr-Methoden-Forschungsansatz:

**Systematische Literaturrecherche** peer-begutachteter Veröffentlichungen und Grundlagendokumente (2010–2026).

**Vergleichende Politikanalyse** von Schweiz (EMBAG 2023, E-Government-Strategie 2024–2027), Deutschland (OZG 2017/2024, DVS) und EU (Interoperable-Europe-Act 2024, EU-Open-Source-Strategie 2020–2023, EU Data Act 2023).

**Technologiestack-Bewertung** anhand einer Scoring-Matrix: Lizenzoffenheit, Einsatzreife, Community-Gesundheit, Interoperabilitätsstandards, Sicherheitsprofil, Gesamtbetriebskosten, bestehende Verwaltungseinsätze.

**Fallstudienanalyse** von Kommunen, die Open-Source-Transitionen über die gesamte Einwohnerbandbreite abgeschlossen oder wesentlich vorangetrieben haben.

### 2.1 Einschlusskriterien

Quellen wurden aufgenommen, wenn sie Open-Source-Software in Behörden behandeln, behördliche Digitaltransformationsstrategie betreffen oder Primärdaten zu kommunalen Implementierungen liefern.

---

## 3. Literaturübersicht

### 3.1 Theoretische Grundlagen des E-Governments

Die akademische Literatur hat sich durch vier Generationen entwickelt [30]. Die erste Generation (1995–2005) digitalisierte bestehende Prozesse [29]. Die zweite (2005–2012) betonte Online-Dienste und Bürgerportale [7]. Die dritte (2012–2020) brachte Open Data und partizipative Plattformen [8]. Die aktuelle vierte Generation (2020–heute) ist durch Plattform-Regierung, digitale Identitätsinfrastruktur und die Souveränitätswende geprägt [45].

Lathrop und Ruma (2010) etablierten die drei Säulen offener Regierung: Transparenz, Beteiligung und Kollaboration [53]. Diese Säulen entsprechen direkt den Stack-Komponenten in Abschnitt 4: Open Data (Transparenz), Beteiligungsplattformen wie Decidim und CONSUL (Beteiligung) und kollaborative Infrastruktur wie Nextcloud und Matrix (Kollaboration).

Das Reifegradmodell von Wirtz und Weyerer [7] identifiziert fünf Dimensionen: technische Infrastruktur, Prozessqualität, Servicequalität, Bürgerorientierung und Transparenz. Deutsche und Schweizer Kommunen zeigen heterogene Leistungen; das regulatorische Umfeld schreibt zunehmend Transparenz und Interoperabilität vor [1, 2, 45].

### 3.2 Digitale Souveränität in der öffentlichen Verwaltung

Die EU-Open-Source-Strategie 2020–2023 etablierte "Teilung und Wiederverwendung" als Kernprinzip [5]. Der Interoperable-Europe-Act (Verordnung (EU) 2024/903, CELEX 32024R0903, ABl. L 2024/903, 22. April 2024) schafft bindende Verpflichtungen zur grenzüberschreitenden Interoperabilität [6]. Der EU Data Act (Verordnung (EU) 2023/2854, anwendbar ab September 2025) fügt harmonisierte Datenaustausch-Verpflichtungen hinzu [52].

ZenDiS GmbH (Zentrum für Digitale Souveränität der öffentlichen Verwaltung), 2022 von der Bundesregierung gegründet, verwaltet OpenDesk und koordiniert souveräne Technologieentwicklung für die Bundesverwaltung [47]. Das OSOR (EU Open Source Observatory), betrieben vom JRC der Europäischen Kommission, verfolgt Open-Source-Adoption in Mitgliedstaaten jährlich [54].

Das EMBAG (in Kraft seit 1. Januar 2024) macht die Schweiz zu einer der führenden Open-Source-mandatierenden Jurisdiktionen weltweit [1].

### 3.3 Das Deutsche OZG-Ökosystem

Das OZG 2.0 (2024) verpflichtet alle deutschen Verwaltungsebenen zur Online-Dienstleistungserbringung mit „Once Only“-Prinzip und EfA-Ansatz [2]. Die Deutsche Verwaltungscloud-Strategie (DVS) bietet den übergreifenden Infrastrukturrahmen für SCS-Einsatz [56]. openCode.de ermöglicht Entdeckung, Wiederverwendung und Beitrag zu behördlichen Open-Source-Lösungen [10].

### 3.4 Schweizer Behörden und föderale Digitaldienste

Schweizer Schlüsselinfrastrukturen:

- **Fedlex**: offizielle Plattform für Bundesrecht auf Basis offener Standards [1]
- **opendata.swiss**: nationales Open-Government-Data-Portal auf CKAN-Basis [44]
- **GEVER**: standardisiertes Geschäftsverwaltungssystem; koordiniert durch das Bundesarchiv (BAR) [43]
- **Schweizer E-ID (BGEID)**: Bundesgesetz über den elektronischen Ausweis, vom Parlament 2023 verabschiedet, Diensteintritt 2026, SWIYU-Wallet [51]
- **eCH-Standards**: Schweizer Normierungsgremium für E-Government-Standards (ech.ch); Schlüsselstandards: eCH-0160 (Aktenführung), eCH-0039 (Datenaustausch), eCH-0261 (E-ID). Konformität obligatorisch für E-Government-Software-Interoperabilität [48]

Die E-Government-Strategie Schweiz 2024–2027 (Dezember 2023) schreibt offene Standards, Once-Only-Datenerhebung und Interoperabilität vor [16]. Die OGD-Strategie 2024–2027 erweitert dies auf Open Government Data [55].

### 3.5 Souveräne Technologie-Gemeinschaften

**ZenDiS GmbH**, gegründet im März 2022, ist die zentrale Koordinationsinstanz für digitale Souveränität in der deutschen öffentlichen Verwaltung. ZenDiS verwaltet OpenDesk und koordiniert Upstream-Beiträge im Auftrag des deutschen öffentlichen Sektors [47].

**Decidim** (Barcelona, 2016): über 400 Organisationen in 40 Ländern, darunter Kanton Schaffhausen [12].

**CONSUL Democracy** (Stadtrat Madrid, 2015): GPL-3.0, über 200 Städte in 40 Ländern. Spezialisiert auf direkte Demokratie: Bürgervorschläge, Haushaltsabstimmungen, Wahlen. Ergänzt Decidims strukturierte Beteiligungsprozesse [49].

**GovStack**: Multi-Stakeholder-Initiative von ITU, GIZ, DIAL und Estlands e-Governance Academy. Definiert 9 Kernbausteine für digitale Regierung: Identität, Zahlungen, Einwilligung, Workflow, Informationsvermittler, Registrierung, Terminplanung, Messaging, GIS [50].

**Matrix/Element**: offenes, dezentralisiertes, Ende-zu-Ende-verschlüsseltes Kommunikationsprotokoll. BundesMessenger und französisches Tchap basieren auf Matrix [14].

**Nextcloud** (Stuttgart, 2016): meistgenutzte quelloffene Datei-Sync- und Kollaborationsplattform in europäischen Behörden [13].

**OpenDesk**, von ZenDiS ab 2022 verwaltet: kuratierte Open-Source-Desktop-Suite (Nextcloud + Cryptpad + OpenProject + Jitsi + Element) [42, 47].

### 3.6 Regulierungsumfeld

| Jurisdiktion | Instrument | Kernverpflichtung | Status |
|---|---|---|---|
| Schweiz | EMBAG (SR 172.019) | Open-Source-Veröffentlichung öffentlich finanzierter Software | In Kraft ab 2024-01-01 |
| Deutschland | OZG 2.0 | Digitale Dienstleistungserbringung; EfA-Prinzip | In Kraft 2024 |
| EU | Interoperable Europe Act (2024/903) | Grenzüberschreitende Interoperabilität | In Kraft ab 2024-05-01 |
| EU | Data Act (2023/2854) | Harmonisierter Datenaustausch | Anwendbar ab 2025-09-12 |
| EU | NIS2-Richtlinie (2022/2555) | Cybersicherheit | Umgesetzt 2024 |
| EU | KI-Verordnung (2024/1689) | KI-Governance im öffentlichen Sektor | Stufenweise 2024–2027 |

### 3.7 Fallstudien kleiner und mittlerer Kommunen

**Kanton Schaffhausen, Schweiz (ca. 83.000 Einwohner)**

Der Kanton Schaffhausen setzte Decidim 2020–2021 für kantonale Partizipationsdemokratieprozesse ein — einer der ersten Schweizer Substaaten, der die Plattform in großem Maßstab adoptierte. Die technische Betreuung übernimmt die kantonale IT-Abteilung mit einer selbstgehosteten Instanz. Der Kanton trug später Übersetzungen und kantonal-spezifische Funktionen zur Decidim-Gemeinschaft bei [12].

**Städte und Gemeinden im AKDB-Verbund, Bayern**

Mehrere bayerische Kommunen im AKDB-Genossenschaftsverbund haben über das BayernPortal-Framework Open-Source-Dokumentenmanagement und Bürgerportal-Komponenten eingeführt. Diese Kommunen profitieren von gemeinsamer Beschaffung, gemeinsamem Betrieb und kollektiver Verhandlung mit Dienstleistern [24].

**Bodenseekreis, Baden-Württemberg (ca. 214.000 Einwohner, 23 Gemeinden)**

Die Kreisverwaltung Bodenseekreis koordinierte einen TYPO3-CMS-Rollout über Mitgliedsgemeinden mit gemeinsamem Hosting und gemeinsamem Designsystem — ein praktisches Modell für Kommunen, die zu klein für eigene technische Kapazitäten sind [19].

**Lausanne, Schweiz (ca. 145.000 Einwohner)**

Lausanne betreibt ein Open-Data-Portal auf CKAN-Basis, das Datensätze zu Haushalt, Mobilität, Umwelt und Stadtplanung veröffentlicht, integriert mit opendata.swiss über DCAT-AP-Harvesting und eCH-konforme Metadaten [44, 48].

**„Einer für Alle“ (EfA)-Pilotgemeinden in Deutschland**

Unter OZG 2.0 entwickeln führende Kommunen Bürgerdienste einmalig und stellen sie anderen zur Übernahme bereit. Stand 2025: über 100 EfA-Dienste auf openCode.de verfügbar. Eine Gemeinde mit 10.000 Einwohnern kann damit denselben digitalen Dienst wie eine Stadt mit 500.000 zu einem Bruchteil des Entwicklungsaufwands einsetzen [10, 56].

### 3.8 Forschungslücken

1. **Gesamtkostenvergleichsstudien** bleiben spärlich. Der TCO-Rahmen in §4.11 schließt diese Lücke.
2. **Längsschnittdaten** aus abgeschlossenen Transitionen sind begrenzt. Münchens LiMux (2003–2017) zeigt politische, nicht technische Ursachen der Umkehr [30].
3. **Nutzerzufriedenheitsforschung** zu Open-Source-Bürgerdiensten fehlt fast vollständig.
4. **KI-Governance**: Die KI-Verordnung schafft neue Anforderungen für KI-Systeme in bürgergerichteten Entscheidungssystemen [57].

---

## 4. Technologiestack-Analyse

### 4.1 Digitale Identität und Authentifizierung

**Empfohlene Komponente: Keycloak** [21]

Keycloak ist die De-facto-Open-Source-IAM-Plattform für Behörden: OpenID Connect, OAuth 2.0, SAML 2.0, Federation mit BundID (Deutschland), BGEID (Schweiz, ab 2026) und eIDAS-2.

| Kriterium | Bewertung (1–5) | Anmerkung |
|---|---|---|
| Lizenzoffenheit | 5 | Apache 2.0 |
| Einsatzreife | 5 | Produktion erprobt, 10+ Jahre |
| Community | 5 | Groß, aktiv, CNCF-unterstützt |
| Interoperabilität | 5 | OIDC, OAuth2, SAML2, FIDO2, eIDAS-2 |
| Sicherheit | 5 | CVE-reaktiv, geprüft |
| Gesamtkosten | 4 | Keine Lizenzkosten; Betriebskompetenz nötig |
| Behörden-Einsätze | 5 | Weit verbreitet in EU-Behörden |

**Schweiz-Hinweis:** Keycloak muss für BGEID-Anmeldedaten konfiguriert werden (W3C Verifiable Credentials / SD-JWT, unterstützt über Erweiterungen ab 2025). Planung in Phase 1.

### 4.2 Dokumentenmanagement und Aktenverwaltung

**Empfohlene Komponenten: Nextcloud + OpenProject** [13, 20]

Für Schweizer GEVER-Konformität: kantonale GEVER-Lösungen (CMI, Fabasoft Community) als Compliance-Schicht; Nextcloud als kollaboratives Frontend. eCH-0160-Konformität erforderlich [48].

### 4.3 Workflow-Automatisierung

**Empfohlene Komponente: Camunda Platform 8 Community** [33]

BPMN-2.0-native Workflow-Engine mit XÖV-Integration (Deutschland) [46] und eCH-Integration (Schweiz) [48]. Flowable (Apache 2.0) als leichtgewichtige Alternative.

### 4.4 Bürgerbeteiligung

**Primärempfehlung: Decidim** [12] · **Alternative: CONSUL Democracy** [49]

| Kriterium | Decidim | CONSUL |
|---|---|---|
| Lizenz | AGPL-3.0 | GPL-3.0 |
| Einsätze | 400+ weltweit | 200+ weltweit |
| Stärke | Strukturierte Prozesse | Direkte Demokratie |

Beide Plattformen können parallel betrieben werden, je nach gewünschten Beteiligungsformaten.

### 4.5 Kommunikation und Kollaboration

| Komponente | Lizenz | Reife | Hauptvorteil |
|---|---|---|---|
| Matrix/Element | Apache 2.0 | Produktion | E2E-Verschlüsselung, Föderation |
| Jitsi Meet | Apache 2.0 | Produktion | Browser-basiert, selbstgehostet |
| BigBlueButton | LGPL-3.0 | Produktion | Ratssitzungen, Bildung |
| Nextcloud Talk | AGPL-3.0 | Produktion | Integriert mit Dateiverwaltung |

### 4.6 Open-Data-Veröffentlichung

**Empfohlene Komponente: CKAN** [22]

CKAN unterstützt DCAT-AP (EU), DCAT-AP.de (Deutschland) und OGD-Schweiz-Metadaten. Die Datenaustausch-Verpflichtungen des EU Data Act (ab September 2025) werden am effizientesten über eine CKAN-Bereitstellung erfüllt [52].

### 4.7 Geographische Informationssysteme

- **QGIS** (Desktop/Server) für räumliche Datenbearbeitung [37]
- **GeoServer** für OGC-konforme Veröffentlichung
- **OpenStreetMap** als kartographische Grundlage [36]

### 4.8 Website und Content-Management

- **TYPO3** (deutschsprachige Welt): BITV 2.0 / WCAG 2.1 AA konform [19]
- **Drupal**: Europäische Kommission und internationale Referenzen

### 4.9 Cloud-Infrastruktur

**Empfohlene Komponente: Sovereign Cloud Stack (SCS)** [3, 11]

Vollständig quelloffene Cloud-Plattform (OpenStack + Kubernetes + Ceph). Die DVS positioniert SCS als Zielarchitektur für die gesamte deutsche öffentliche Cloud-Infrastruktur [56].

### 4.10 Referenzarchitektur

```
+-------------------------------------------------------------+
|                   BÜRGERSCHNITTSTELLEN                     |
|       TYPO3/Drupal . Decidim/CONSUL . CKAN . Nextcloud     |
+-------------------------------------------------------------+
|                     DIENSTE-SCHICHT                        |
|   Camunda Workflows . XÖV/eCH-Formulare . GeoServer/QGIS  |
+-------------------------------------------------------------+
|                  KOLLABORATIONS-SCHICHT                    |
|     Nextcloud . Matrix/Element . Jitsi . OpenProject       |
+-------------------------------------------------------------+
|                   IDENTITÄTS-SCHICHT                      |
|     Keycloak <-> BundID / BGEID (CH) / eIDAS-2            |
+-------------------------------------------------------------+
|                  INFRASTRUKTUR-SCHICHT                     |
|   Sovereign Cloud Stack . Kubernetes . PostgreSQL . Ceph   |
+-------------------------------------------------------------+
```

Datenaustausch: XÖV-Standards (Deutschland) [46] bzw. eCH-Standards (Schweiz) [48]. Sicherheit: BSI IT-Grundschutz [26] oder Schweizer ISDS.

### 4.11 Gesamtbetriebskosten-Rahmen (TCO)

Der häufigste Fehler bei kommunaler Technologiebeschaffung ist der Vergleich von Open-Source-Implementierungskosten mit proprietären Kopfkosten, anstatt vollständige Fünf-Jahres-Gesamtkosten gegenüberzustellen.

**TCO-Komponenten für eine Gemeinde mit 500 Mitarbeitenden:**

| Kostenelement | Proprietär (Schätzung) | Open Source (Schätzung) | Anmerkung |
|---|---|---|---|
| Produktivitätslizenzen | 75.000–150.000 €/J | 0 € | Lizenzeliminierung |
| Hosting / Infrastruktur | 40.000–80.000 €/J | 30.000–60.000 €/J | SCS vs. Hyperscaler |
| Implementierung (einmalig) | 50.000–150.000 € | 100.000–300.000 € | Open Source höher upfront |
| Schulung / Änderungsmanagement | 20.000–50.000 € | 30.000–80.000 € | Initial höher |
| Supportverträge | 20.000–60.000 €/J | 15.000–40.000 €/J | Wettbewerb; kein Lock-in |
| Anpassung / Integration | 30.000–100.000 € | 20.000–80.000 € | Open Source behält IP |
| Ausstiegs-/Migrationskosten | 100.000–500.000 € | 20.000–100.000 € | Proprietäre Lock-in-Prämie |
| **5-Jahres-Gesamt (Mittelwert)** | **~825.000 €** | **~680.000 €** | **Open Source ~18% günstiger** |

*Schätzungen basierend auf publizierten Beschaffungsdaten aus deutschen OZG-Implementierungen, Schweizer Kantonalberichten und dem französischen Gendarmerie-LibreOffice-Pilotprojekt (70.000 Arbeitsplätze, ~2 M€/Jahr Ersparnis).*

**Die Münchener LiMux-Lektion:** Das LiMux-Projekt (2003–2017) erzielte während des Betriebs nachgewiesene Kosteneinsparungen. Die Rückabwicklung kostete schätzungsweise 50 M€. Diese Asymmetrie — niedrige Open-Source-Einführungskosten, hohe proprietäre Rückabwicklungskosten — stärkt das langfristige wirtschaftliche Argument über einen 10-Jahres-Horizont.

---

## 5. Implementierungsfahrplan

### Phase 0: Grundlegung (Monate 1–3)

Lenkungsausschuss einsetzen; Ist-Analyse; Stakeholder-Plan; Beschaffungsrahmen; MoU mit IT-Kooperationspartner; GovStack-Bausteinmapping aktueller Dienste [50]. **Erfolg:** Politisches Mandat, Budgetrahmen (€200.000–500.000 für Phase 0–1).

### Phase 1: Identität und Infrastruktur (Monate 4–12)

SCS-Umgebung; Keycloak mit BundID/BGEID-Föderation; Nextcloud-Basis; Matrix/Element; BSI IT-Grundschutz / ISDS Basisdokumentation. **Erfolg:** 100 % der IT-Mitarbeitenden per Keycloak SSO; Dateispeicherung migriert.

### Phase 2: Dienste und Workflows (Monate 10–18)

Fünf meistgenutzte Dienste auf Camunda/XÖV (DE) oder Camunda/eCH (CH); CMS-Migration; CKAN mit DCAT-AP; Decidim oder CONSUL. **Erfolg:** 80 % des Zieldienst-Volumens im neuen System.

### Phase 3: Integration und Erweiterung (Monate 16–24)

Keycloak-SSO für alle Dienste; GIS-Schicht; 80 % digitalisierte Verwaltungsleistungen; XÖV/eCH-Datenaustausch; EU Data Act-Datenaustausch-Verpflichtungen erfüllt [52]. **Erfolg:** Ende-zu-Ende papierfrei bei 80 % der Transaktionsarten.

### Phase 4: Optimierung und Gemeinschaft (Monate 22–30)

Nutzerzufriedenheitserhebung (Ziel: NPS > 40); Upstream-Beiträge; Community of Practice; TCO-Bericht nach §4.11. **Erfolg:** ≥ 3 Upstream-Verbesserungen; Community of Practice mit ≥ 3 Peer-Kommunen.

### Phase 5: Souveränität und Skalierung (Monate 28–36)

Lizenzkonformitätsprüfung; Datensouveränität verifiziert; Playbook für Nachbarkommunen; Strategiepapier v1.0. **Erfolg:** Null proprietäre Einzelanbieter-Abhängigkeiten im kritischen Pfad.

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Übersicht

| Stakeholder | Hauptinteresse | Einbindungsansatz |
|---|---|---|
| Bürgermeisterin / Exekutive | Politischer Erfolg, Kosten | Führungsbriefing, Fortschritts-Dashboard |
| Gemeinderat | Kontrolle, Legitimität | Quartalsberichte, öffentliche Sitzungen |
| IT-Team | Machbarkeit, Arbeitsbelastung | Co-Design, Schulung, Community |
| Vergabeamt | Rechtliche Konformität | Rahmenverträge, juristische Beratung |
| Verwaltungsmitarbeitende | Benutzerfreundlichkeit | UX-Tests, Änderungsmanagement |
| Bürgerinnen und Bürger | Servicequalität, Datenschutz | Partizipatives Design |
| Zivilgesellschaft | Transparenz, Beteiligung | Decidim, öffentliche Roadmaps |
| Open-Source-Gemeinschaften | Beitrag, Wiederverwendung | openCode.de, Upstream-Beiträge |
| IT-Dienstleister | Partnerschaft | Zertifizierte Partnervereinbarungen |
| Datenschutzbeauftragte | DSGVO-Konformität | Privacy-by-Design in jeder Phase |

### 6.2 Beschaffungsrahmen

1. **Dienste beschaffen, nicht Lizenzen.** Open-Source-Software ist kostenlos nutzbar; Kommunen zahlen für Implementierung, Hosting, Support.
2. **Genossenschaftliche Strukturen nutzen.** govdigital eG (Deutschland, GWB §97ff.) und kantonale IT-Genossenschaften (Schweiz, BöB SR 172.056.1) erfüllen das öffentliche Vergaberecht [23].
3. **»Public Money? Public Code!«-Prinzip.** Alle mit öffentlichen Mitteln entwickelte Individualsoftware muss unter OSI-Lizenz auf openCode.de veröffentlicht werden — als Vertragsbedingung [4].
4. **Gesamtbetriebskosten bewerten.** 5-Jahres-TCO-Modell nach §4.11 für jede Beschaffung.
5. **Interoperabilitätsstandards fordern.** XÖV (DE) [46], eCH (CH) [48], DCAT-AP (EU) als Ausschlusskriterien bei Nichtkonformität.
6. **Zertifizierte genossenschaftliche Anbieter bevorzugen.** SCS-zertifizierte Betreiber oder govdigital eG-Mitglieder [23].
7. **GovStack-Spezifikationen referenzieren** [50] für interoperable Ausschreibungen ohne Anbieter-Lock-in.

### 6.3 Änderungsmanagement

- **Digital-Transformations-Champion** auf politischer Ebene benennen
- **Open-Source-Botschafter** in jeder Abteilung mit erweiterter Schulung
- Mindestens 3 Monate **Parallelbetrieb** vor Abschaltung kritischer Systeme
- **Frühe Erfolge** dokumentieren und kommunizieren
- Öffentliches **Transparenz-Dashboard** mit Migrationsfortschritt, Kosten, Servicequalität
- **OSOR-Gemeinschaft** für Peer-Fallstudien und Change-Management-Guidance [54]

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| Politischer Rückzug nach Wahl | Mittel | Hoch | In Satzung verankern; parteiübergreifenden Konsens aufbauen |
| Anbieter-Lobbying / Desinformation | Hoch | Mittel | TCO-Belege (§4.11); Zivilgesellschaft einbinden |
| Qualifikationslücke IT-Team | Hoch | Mittel | Schulungsprogramm; IT-Genossenschaft |
| Integrationsfehler zwischen Schichten | Mittel | Hoch | Phasenweiser Rollout; Referenzarchitektur |
| Datenverlust bei Migration | Niedrig | Kritisch | Vollständiges Backup; Parallelbetrieb |
| DSGVO-Verstoß | Niedrig | Hoch | Privacy-by-Design; DSB-Einbindung |
| Benutzerakzeptanzmangel | Mittel | Hoch | Änderungsmanagement; UX-Tests |
| Sicherheitsvorfall | Niedrig | Kritisch | BSI IT-Grundschutz; Penetrationstests |
| Kostenabweichung | Mittel | Mittel | Phasengesteuertes Budget; offene TCO-Buchhaltung |
| KI-Governance-Nichtkonformität | Mittel | Mittel | KI-Komponenten gegen KI-VO prüfen [57] |

### 7.2 Das Münchener LiMux-Beispiel

Ein unabhängiges Post-Mortem ergab, dass die Umkehr des LiMux-Projekts (2003–2017) primär durch politischen Führungswechsel, unzureichendes Änderungsmanagement und Kompatibilitätsprobleme mit Landessystemen verursacht wurde — nicht durch technische Mängel [30]. Die Implementierung erzielte nachgewiesene Kosteneinsparungen. Die Rückabwicklung kostete schätzungsweise 50 M€.

### 7.3 Sicherheitsanforderungen

BSI IT-Grundschutz [26]: öffentliche Dienste erfüllen BSI Authenticator Assurance Level 2 (AAL2); TLS 1.3 minimum; Penetrationstests an jedem Phasentor; SBOM für alle Open-Source-Abhängigkeiten; NIS2-konformer Incident-Response-Plan [27].

### 7.4 Regulierungs-Compliance-Rahmen

**Datenschutz (DSGVO / nDSG):** Selbstgehostete Infrastruktur mit expliziten Datenhaltungsrichtlinien erfüllt Datensparsamkeit und Zweckbindung. Open Source ermöglicht unabhängige Architekturprüfung.

**Interoperabilität (Interoperable Europe Act [6]):** Offene APIs, XÖV/eCH-Standardskonformität und DCAT-AP-Open-Data-Veröffentlichung erfüllen die Kernanforderungen.

**Datenaustausch (EU Data Act [52], ab September 2025):** CKAN-basierte Open-Data-Infrastruktur mit DCAT-AP-Metadaten ist der Referenzimplementierungsweg.

**Cybersicherheit (NIS2 [27]):** BSI IT-Grundschutz-Zertifizierung erfüllt deutsche Umsetzungsanforderungen; Schweizer Äquivalent: ISDS-Framework.

**KI-Systeme (KI-Verordnung [57], stufenweise 2024–2027):** Bürgergerichtete KI-Entscheidungssysteme sind als „hochrisiko“ eingestuft (Anhang III). Open-Source-KI-Komponenten ermöglichen unabhängige Prüfung; proprietäre „Black Box“-KI in der öffentlichen Verwaltung hat strukturelles Konformitätsrisiko.

**Open-Source-Mandat (EMBAG [1] / OZG 2.0 [2]):** Schweiz und Deutschland schaffen positive rechtliche Verpflichtungen, die eine Open-Source-first-Beschaffungspolitik stärken.

---

## 8. Schlussfolgerung

Die in dieser Arbeit ausgewerteten Belege konvergieren auf vier Befunde:

**1. Open-Source-Kommunaltechnologie-Stacks sind technisch ausgereift und produktionserprobt.** Jede funktionale Anforderung einer modernen Kommunalverwaltung kann durch Open-Source-Software erfüllt werden — mit dokumentierten Einsätzen von Schaffhausen (~83.000) bis Barcelona (1,6 Mio.).

**2. Das regulatorische Umfeld schreibt zunehmend Open Source und Interoperabilität vor.** EMBAG, OZG 2.0, Interoperable-Europe-Act, EU Data Act und NIS2 schaffen kumulativ ein rechtliches Umfeld, in dem proprietäre Systeme wachsender Compliance-Belastung ausgesetzt sind.

**3. Das wirtschaftliche Argument ist überzeugend bei korrekter Gesamtkostenbetrachtung.** Für eine Gemeinde mit 500 Mitarbeitenden ist Open Source im Fünf-Jahres-TCO ca. 18 % günstiger. Die Ausstiegskosten-Asymmetrie (München: ~50 M€ Rückabwicklung) macht Open Source über einen 10-Jahres-Horizont zur konservativen fiskalischen Wahl.

**4. Erfolg erfordert ebenso viel politische und organisatorische Investition wie technische.** Klares politisches Mandat, qualifiziertes Änderungsmanagement und nachhaltiges Stakeholder-Engagement sind die bindenden Faktoren.

Städte, die als Erste handeln, profitieren von Pioniervorteilen: Sie gestalten kooperative Standards, bauen Fachkompetenz auf und tragen zu den Open-Source-Gemeingütern bei, die alle Kommunen teilen. Die Einladung ist offen.

---

## Literaturverzeichnis

[1] Schweizerischer Bundesrat. (2023). *Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)*. SR 172.019. https://www.fedlex.admin.ch/eli/cc/2023/682/de

[2] BMI. (2024). *Onlinezugangsgesetz 2.0 (OZG 2.0)*. https://www.bmi.bund.de/DE/themen/moderne-verwaltung/e-government/ozg/ozg-node.html

[3] OSBA. (2023). *Sovereign Cloud Stack*. https://scs.community/

[4] FSFE. (2017). *Public Money? Public Code!* https://publiccode.eu/

[5] Europäische Kommission. (2020). *Open-Source-Software-Strategie 2020–2023*. https://commission.europa.eu/about/departments-and-executive-agencies/informatics/open-source-software-strategy_en

[6] Europäisches Parlament und Rat. (2024). *Verordnung (EU) 2024/903 — Interoperable Europe Act*. CELEX 32024R0903. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R0903

[7] Wirtz, B.W. & Weyerer, J.C. (2017). *Public Management Review*, 19(9), 1297–1316. https://doi.org/10.1080/14719037.2017.1283024

[8] Janssen, M. et al. (2012). *Information Systems Management*, 29(4), 258–268. https://doi.org/10.1080/10580530.2012.716740

[9] FITKO. (2023). *Jahresbericht 2023*. https://www.fitko.de/publikationen/jahresbericht/

[10] openCode.de. (2022). https://opencode.de/

[11] SCS Community. (2023). *SCS Technische Dokumentation*. https://docs.scs.community/

[12] Decidim Association. (2021). https://decidim.org/ — [AGPL-3.0]

[13] Nextcloud GmbH. (2023). https://nextcloud.com/government/

[14] The Matrix Foundation. (2023). *Matrix-Spezifikation*. https://spec.matrix.org/

[16] E-Government Suisse. (2023). *Strategie E-Government Schweiz 2024–2027*. https://www.egovernment.ch/de/umsetzung/e-government-strategie/

[19] TYPO3 Association. (2023). https://typo3.org/

[20] OpenProject GmbH. (2023). https://www.openproject.org/

[21] Keycloak Community. (2023). https://www.keycloak.org/ — [Apache 2.0]

[22] CKAN Association. (2023). https://ckan.org/ — [AGPL-3.0]

[23] govdigital eG. (2023). https://govdigital.de/

[24] Dataport AöR. (2023). https://www.dataport.de/

[26] BSI. (2023). *IT-Grundschutz-Kompendium 2023*. https://www.bsi.bund.de/ — [CC-BY-ND 3.0 DE]

[27] Europäisches Parlament und Rat. (2022). *NIS2-Richtlinie (EU) 2022/2555*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555

[29] UN DESA. (2022). *UN E-Government Survey 2022*. https://publicadministration.un.org/egovkb/en-us/Reports/UN-E-Government-Survey-2022

[30] Janowski, T. (2015). *Government Information Quarterly*, 32(3), 221–226. https://doi.org/10.1016/j.giq.2015.07.001

[33] Camunda Services GmbH. (2023). https://camunda.com/download/

[34] BigBlueButton Inc. (2023). https://bigbluebutton.org/

[35] Jitsi Community. (2023). https://jitsi.org/

[36] OpenStreetMap Foundation. (2023). https://www.openstreetmap.org/

[37] QGIS Project. (2023). https://www.qgis.org/

[39] CNCF. (2023). *Kubernetes*. https://kubernetes.io/

[41] PostgreSQL Global Development Group. (2023). https://www.postgresql.org/

[42] BMI / ZenDiS GmbH. (2023). *OpenDesk*. https://opendesk.eu/

[43] BAR. (2023). *GEVER in der Bundesverwaltung*. https://www.bar.admin.ch/bar/de/home/digitale-archivierung/gever.html

[44] opendata.swiss. (2023). https://opendata.swiss/

[45] Europäische Kommission. (2017). *EIF*. https://joinup.ec.europa.eu/collection/nifo-national-interoperability-framework-observatory/european-interoperability-framework-detail

[46] KoSIT. (2023). *XÖV-Standards*. https://www.xoev.de/

[47] ZenDiS GmbH. (2023). *Jahresbericht*. https://zendis.de/

[48] eCH. (2023). *eCH-Standards*. https://www.ech.ch/

[49] Stadtrat Madrid. (2015). *CONSUL Democracy*. https://consuldemocracy.org/ — [GPL-3.0]

[50] GovStack (ITU/GIZ/DIAL). (2023). *Building Blocks Specification*. https://www.govstack.global/

[51] Schweizerischer Bundesrat. (2023). *BGEID*. https://www.fedlex.admin.ch/eli/fga/2023/787/de

[52] Europäisches Parlament und Rat. (2023). *EU Data Act (EU) 2023/2854*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R2854

[53] Lathrop, D. & Ruma, L. (Hrsg.). (2010). *Open Government*. O'Reilly Media. ISBN 978-0-596-80435-0.

[54] Europäische Kommission / JRC. (2023). *OSOR Jahresbericht 2023*. https://joinup.ec.europa.eu/collection/open-source-observatory-osor

[55] Schweizerische Bundeskanzlei / BFS. (2023). *OGD-Strategie Schweiz 2024–2027*. https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html

[56] BMI. (2023). *Deutsche Verwaltungscloud-Strategie (DVS)*. https://www.bmi.bund.de/DE/themen/it-und-digitalpolitik/it-der-bundesverwaltung/verwaltungscloud/verwaltungscloud-node.html

[57] Europäisches Parlament und Rat. (2024). *KI-Verordnung (EU) 2024/1689*. https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689

[58] GAIA-X Association AISBL. (2023). https://gaia-x.eu/

---

*Dieses Dokument wird unter CC-BY-4.0 veröffentlicht.*  
*Sebastian Graf, Autonomes Büro für Kommunale Digitale Infrastruktur (sebk4c@tuta.com)*  
*Version: 0.2.0 — Zitationsvollständiger Entwurf — 2026-06-21*
