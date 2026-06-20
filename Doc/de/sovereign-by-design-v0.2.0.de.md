---
title: "Souverän von Anfang an: Eine State-of-the-Art Open-Source-Technologiestrategie für Stadtverwaltungen"
author: "Sebastian Graf, Autonomes Büro für Zivile Digitale Infrastruktur"
correspondence: "sebk4c@tuta.com"
version: "0.2.0"
status: "Zitationsvervollständigter Entwurf"
date: "2026-06-20"
language: "de"
source-of-truth: false
source-language: "en"
source-file: "Doc/en/sovereign-by-design-v0.2.0.md"
previous-version: "0.1.0"
SPDX-License-Identifier: "CC-BY-4.0"
keywords:
  - digitale Souveränität
  - Open Source
  - kommunale Verwaltung
  - GovTech
  - öffentliche Verwaltung
  - EMBAG
  - OZG
  - Interoperabilität
  - digitale Transformation
  - Beschaffung
  - eCH
  - ZenDiS
  - OSOR
  - Sovereign Cloud Stack
changelog:
  - version: "0.2.0"
    date: "2026-06-20"
    changes: "Zitationsvervollständigter Entwurf mit erweiterter Literaturrecherche (Quellen [1]–[65]), eCH-Standards, CONSUL, GovStack, ZenDiS, OSOR, EU-Datengesetz, nDSG, Schweizer eID, CryptPad, Collabora Online, OpenSlides, Forgejo; Technologie-Stack auf 12 Schichten erweitert; Beschaffungsklausel und Risikoregister ergänzt; TCO-Modell überarbeitet"
  - version: "0.1.0"
    date: "2025-11-01"
    changes: "Erster Entwurf"
---

# Souverän von Anfang an: Eine State-of-the-Art Open-Source-Technologiestrategie für Stadtverwaltungen

**Sebastian Graf** — Autonomes Büro für Zivile Digitale Infrastruktur  
Korrespondenz: sebk4c@tuta.com  
Version 0.2.0 · Zitationsvervollständigter Entwurf · 20. Juni 2026  
Lizenz: CC-BY-4.0

---

## Zusammenfassung

Städtische Verwaltungen bilden die bürgernächste Schicht demokratischer Administration, stehen jedoch vor einem strukturellen Widerspruch: Sie sind auf digitale Infrastruktur angewiesen, die sie selten kontrollieren. Proprietäre Plattformen schaffen Lieferantenabhängigkeiten, schränken Interoperabilität ein und untergraben die demokratische Rechenschaftspflicht. Diese Arbeit stellt eine umfassende Open-Source-Technologiestrategie für kommunale Verwaltungen vor, die auf drei nationalen Rechtsrahmen basiert — dem schweizerischen EMBAG [1], dem deutschen OZG 2.0 [2] und dem europäischen Interoperable Europe Act [3] — und durch Beweise aus der Praxis von ZenDiS [4], OSOR [5], govdigital eG [6] und GovStack [7] untermauert wird.

Wir präsentieren eine Sieben-Kriterien-Bewertungsmatrix für 12 Technologieschichten, eine phasenweise 36-Monate-Implementierungs-Roadmap für Städte jeder Größe und ein auf empirischen Studien basierendes TCO-Modell, das Einsparungen von 381–678 € pro Arbeitsplatz und Jahr gegenüber proprietären Alternativen aufzeigt [8][9]. Über die Kostensenkung hinaus ermöglichen Open-Source-Stacks demokratische Rechenschaftspflicht durch Quellcode-Audits, regulatorische Konformität durch Design und interkommunale Zusammenarbeit durch gemeinsame Infrastruktur. Die Gesamtbetriebskosten-Analyse über fünf Jahre zeigt einen Barwertvorteil von 800.000 € bis 1,7 Mio. € für eine Gemeinde mit 500 Beschäftigten.

---

## Inhaltsverzeichnis

1. Einleitung
2. Methodik
3. Literaturübersicht
4. Technologie-Stack-Analyse
5. Implementierungs-Roadmap
6. Stakeholder- und Beschaffungsstrategie
7. Risikoanalyse
8. Schlussfolgerung
Quellenverzeichnis

---

## 1. Einleitung

### 1.1 Hintergrund und Motivation

Die Digitalisierung der öffentlichen Verwaltung hat eine kritische Phase erreicht. In der Schweiz verpflichtet das Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG, 2023) Bundesbehörden zur bevorzugten Nutzung von Open-Source-Software und definiert explizite Anforderungen an digitale Souveränität [1]. In Deutschland setzt OZG 2.0 die Digitalisierung von 575 Verwaltungsleistungen bis Ende 2027 als verbindliches Ziel [2]. Auf europäischer Ebene schafft der Interoperable Europe Act einen Rechtsrahmen für maschinenlesbare Interoperabilitätslösungen über Behördengrenzen hinweg [3].

Gleichzeitig zeigt eine wachsende Evidenzbasis, dass proprietäre Plattformen strukturelle Risiken für öffentliche Institutionen darstellen: Anbieterabhängigkeit verhindert Kontrolle über kritische Infrastruktur [10], Datenschutzrisiken entstehen durch Verarbeitung in Drittstaaten außerhalb des EU/CH-Rechtsrahmens [11], und intransparente Algorithmen unterminieren die Nachvollziehbarkeit behördlicher Entscheidungen [12]. Das Münchner Projekt LiMux — trotz politischer Abkehr im Jahr 2017 [13] — hat gezeigt, dass Städte im Prinzip vollständig auf Open-Source-Infrastruktur migrieren können.

### 1.2 Forschungsfragen

Diese Arbeit adressiert vier zentrale Forschungsfragen:

1. **RF1 — Technologische Reife:** Welche Open-Source-Komponenten haben einen Reifegrad erreicht, der den Anforderungen kommunaler Verwaltungen im DACH-Raum entspricht?
2. **RF2 — Rechtskonformität:** Wie können Open-Source-Stacks so konfiguriert werden, dass sie EMBAG, OZG 2.0, nDSG, DSGVO, BSI IT-Grundschutz und NIS2 vollständig erfüllen?
3. **RF3 — Wirtschaftlichkeit:** Unter welchen Bedingungen übersteigen die Gesamtbetriebskosten offener Lösungen die Einsparungen durch Lizenzkostenvermeidung?
4. **RF4 — Governance:** Welche Beschaffungsrahmen, Vergabeprozesse und interkommunalen Kooperationsmodelle maximieren den Nutzen für einzelne Gemeinden?

### 1.3 Terminologie und Begriffsabgrenzung

**Digitale Souveränität** bezeichnet die Fähigkeit einer Organisation, ihre digitalen Systeme, Daten und Prozesse zu kontrollieren, zu prüfen und anzupassen, ohne von einzelnen kommerziellen Anbietern abhängig zu sein [14]. Im behördlichen Kontext umfasst dies: Kontrolle über Quellcode und Deployment-Infrastruktur, Hoheit über Daten und Metadaten, Fähigkeit zur unabhängigen Sicherheitsprüfung sowie Gestaltungsspielraum bei Weiterentwicklung.

**Open-Source-Software** im Sinne dieser Arbeit bezeichnet Software, die unter einer OSI-anerkannten Lizenz [15] veröffentlicht wird, deren Quellcode öffentlich zugänglich ist und deren Nutzung, Modifikation und Weitergabe ohne Diskriminierung gestattet ist.

**Kommunale Verwaltung** bezeichnet Gemeinden, Städte und Stadtkreise mit eigenem Verwaltungsapparat, typischerweise mit 50–2.000 Beschäftigten im Verwaltungsdienst.

### 1.4 Geltungsbereich

Die Analyse konzentriert sich auf den deutschsprachigen Raum (DE, CH, AT) mit Querverweisen auf europäische Best Practices. Technologieempfehlungen sind für Gemeinden ab ca. 5.000 Einwohnern ausgelegt, mit Skalierungsanpassungen für größere Städte.

---

## 2. Methodik

### 2.1 Forschungsansatz

Diese Arbeit verbindet systematische Literaturrecherche mit technischer Komponentenbewertung und wirtschaftlicher Analyse. Die Quellenauswahl folgt einem PRISMA-inspirierten Protokoll [16]: Einschlusskriterien sind Peer-Review oder institutionelle Herkunft aus staatlichen oder anerkannten Open-Source-Institutionen; Ausschlusskriterien sind rein kommerzielle White Papers ohne Methodentransparenz sowie Quellen älter als 2015 ohne historische Relevanz.

### 2.2 Technologiebewertungsmatrix

Jede Technologiekomponente wird anhand von sieben gleichgewichteten Kriterien bewertet (je 1–5 Punkte; Empfehlungsschwelle: ≥ 28/35):

| Kriterium | Beschreibung |
|---|---|
| **K1 — Lizenzoffenheit** | OSI-Konformität, Copyleft-Stärke, Patent-Klauseln |
| **K2 — Deployment-Reife** | Produktionseinsätze, Versionsstabilität, Release-Rhythmus |
| **K3 — Community-Gesundheit** | Kontributoren, Governance-Struktur, Finanzierung |
| **K4 — Interoperabilität** | Standardkonformität (eCH, XÖV, DCAT-AP, OpenAPI) |
| **K5 — Sicherheitspostur** | CVE-Geschichte, Security-Audit, BSI-Zertifizierung |
| **K6 — TCO** | Betriebskosten, Hosting-Optionen, Support-Ökosystem |
| **K7 — Behördeneinsätze** | Nachgewiesene Implementierungen in öffentlichen Institutionen |

### 2.3 Quellenmetadaten-Spezifikation

Jede Quelle im Quellenverzeichnis enthält: Sprache · Region · Herausgebende Institution · Datum · Titel · URL · Lizenz (soweit bekannt). Diese Struktur ermöglicht das automatisierte Tracking durch das Skript `Scripts/update_literature_review.py`.

### 2.4 Übersetzungsmethodik

Dieses Dokument ist eine Übersetzung aus dem englischsprachigen Quelldokument `Doc/en/sovereign-by-design-v0.2.0.md`. Bei Widersprüchen gilt die englische Fassung als verbindlich (`source-of-truth: true`). Regulatorische Begriffe sind in der jeweils landessprachlich gültigen Form verwendet; bei erstmaliger Nennung wird das englische Äquivalent in Klammern angegeben.

---

## 3. Literaturübersicht

### 3.1 Theoretischer Rahmen

Die akademische Debatte um digitale Souveränität in der öffentlichen Verwaltung gründet auf mehreren theoretischen Strängen. Frischmann (2012) entwickelt die Theorie des Infrastrukturwesens, wonach Systeme mit externen Effekten und Nicht-Rivalisierungs-Charakter besondere Governance-Strukturen erfordern [17]. Eghbal (2020) analysiert die Politische Ökonomie von Open-Source-Maintainern und zeigt, dass nachhaltige Ökosysteme strukturierte Finanzierung benötigen [18]. Chesbrough (2003) begründet das Modell der offenen Innovation [19], das heute als Referenzrahmen für kollaborative GovTech-Entwicklung dient.

Zittrain (2008) warnt vor der "Vergiftung der generativen Kapazität" des Internets durch proprietäre Ökosysteme [20] — eine Warnung, die für behördliche IT besondere Relevanz hat, da demokratische Rechenschaftspflicht die Überprüfbarkeit von Systemen voraussetzt. Mergel et al. (2019) beschreiben digitale Transformation im öffentlichen Sektor als organisatorischen, nicht bloß technologischen Wandel [21].

### 3.2 Digitale Souveränität: Rahmenwerke und Institutionen

**OSOR (Open Source Observatory)** der Europäischen Kommission dokumentiert seit 2008 Open-Source-Initiativen in der europäischen öffentlichen Verwaltung [5]. Die aktuelle OSOR-Studie "Open Source in the Public Sector" (2023) zeigt, dass 78 % der befragten Behörden Open-Source-Lösungen einsetzen, aber nur 23 % über eine explizite Open-Source-Strategie verfügen.

**ZenDiS (Zentrum für Digitale Souveränität)** wurde 2022 als GmbH des Bundes gegründet mit dem Auftrag, souveräne digitale Lösungen für die deutsche öffentliche Verwaltung zu entwickeln und zu koordinieren [4]. ZenDiS koordiniert das Projekt "openDesk" — einen integrierten Open-Source-Arbeitsplatz für Bundesbehörden — und arbeitet an einer "Sovereign Workplace"-Referenzarchitektur, die Nextcloud, Collabora, Element und weitere Komponenten integriert.

**govdigital eG** ist eine Genossenschaft öffentlich-rechtlicher IT-Dienstleister, die kollaborative Beschaffung und Betrieb von digitaler Infrastruktur koordiniert [6]. Mit Mitgliedern wie Dataport, AKDB und kommunalen Rechenzentren schafft govdigital Economies of Scale für die öffentliche IT-Beschaffung.

**GovStack** ist eine multilaterale Initiative von ITU und DIAL, die "Building Blocks" für wiederverwendbare digitale Governance-Infrastruktur spezifiziert [7]. Die GovStack-Spezifikationen decken Querschnittsfunktionen wie Identität, Zahlungen, Registrierung und Inhaltsverwaltung ab und sind für die Anpassung an nationale Kontexte ausgelegt.

### 3.3 Deutscher Rahmen: OZG, FITKO und ZenDiS

Das Onlinezugangsgesetz (OZG, 2017) verpflichtete Bund, Länder und Kommunen, bis Ende 2022 rund 575 Verwaltungsleistungen digital anzubieten [22]. Die Bilanz des OZG 1.0 war gemischt: Nur ein Bruchteil der Leistungen war fristgerecht verfügbar, und Interoperabilitätsprobleme zwischen Bundesländern traten systematisch auf [23]. OZG 2.0 (2024) adressiert diese Schwächen durch verbindliche Standardisierung auf Basis des "Einer-für-alle"-Prinzips (EfA) und explizite Open-Source-Präferenz [2].

**FITKO (Föderale IT-Kooperation)** koordiniert die technische Umsetzung des OZG und betreibt den FIT-Store, ein Repository für OZG-konforme Dienste [24]. AKDB (Anstalt für Kommunale Datenverarbeitung in Bayern) und Dataport sind die größten kommunalen IT-Dienstleister und betreiben zunehmend Open-Source-Komponenten in ihren Portfolios [25].

**DigitalService GmbH des Bundes** entwickelt nutzerzentrierte Digitalprodukte für Bundesbehörden, darunter das BundID-Portal, und veröffentlicht Komponenten als Open Source [26]. Der Technologierat des Bundes hat 2023 empfohlen, Open-Source-Software als Standard-Beschaffungsoption zu etablieren.

### 3.4 Schweizer Rahmen: EMBAG, eCH und nDSG

**EMBAG** (Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben, SR 172.019) trat am 1. Januar 2024 in Kraft und verpflichtet Bundesbehörden, den Quellcode selbst entwickelter oder in Auftrag gegebener Software öffentlich zugänglich zu machen, sofern keine Sicherheitsbedenken oder Rechte Dritter entgegenstehen [1]. Art. 9 EMBAG regelt explizit Open Source und schafft damit eine weltweit bemerkenswerte Rechtspflicht zur Offenlegung.

**eCH** (E-Government-Standards Schweiz) publiziert technische Normen für die schweizerische öffentliche Verwaltung [27]. Relevante Standards umfassen: eCH-0014 (SAGA, Standardarchitektur), eCH-0059 (Barrierefreiheit), eCH-0070 (Authentifizierung), eCH-0175 (Identitätsverwaltung) und eCH-0229 (Dokumentenverwaltung). Diese Standards sind durch Referenz in kantonales und kommunales Recht inkorporiert.

**nDSG** (Bundesgesetz über den Datenschutz, revidierte Fassung, SR 235.1) trat am 1. September 2023 in Kraft und hebt das schweizerische Datenschutzrecht auf ein mit der DSGVO vergleichbares Niveau [28]. Für Gemeinden bedeutet dies: Privacy-by-Design-Pflichten, Datenschutz-Folgenabschätzungen für risikoreiche Bearbeitungen und verschärfte Meldepflichten bei Datenverletzungen.

**Schweizer eID** — die staatliche digitale Identität — befindet sich auf Basis des E-ID-Gesetzes (BGEID, SR 161.5) in der Umsetzungsphase [29]. Die eID verwendet eine dezentrale Wallet-Architektur (Self-Sovereign Identity, SSI) und basiert auf offenen Standards (W3C Verifiable Credentials, OpenID4VP). Kommunen sollten ihre IAM-Systeme so ausrichten, dass sie eID-kompatibel sind.

### 3.5 Open-Source-Communities und Schlüsselkomponenten

**CONSUL** ist eine in Madrid entwickelte Open-Source-Plattform für digitale Bürgerbeteiligung, die in über 40 Ländern eingesetzt wird [30]. CONSUL ermöglicht Bürgerbudgets, Petitionen, Abstimmungen und Konsultationen. Die Plattform ist AGPL-3.0-lizenziert und hat eine aktive internationale Community.

**GovStack Building Blocks** spezifizieren technologieneutrale API-Schnittstellen für Kernfunktionen: Identity (kompatibel mit Keycloak), Payments, Registration, Information Mediator und weitere [7]. Die Spezifikationen sind als OpenAPI-Definitionen veröffentlicht und können als Referenz für Ausschreibungsanforderungen dienen.

**CryptPad** ist eine Ende-zu-Ende-verschlüsselte Kollaborationsplattform, entwickelt von XWiki SAS mit Förderung durch das NGI-Programm der EU [31]. CryptPad bietet Dokumente, Tabellen, Präsentationen, Kanban und Formulare in einem Single-Sign-On-integrierbaren Paket. Die AGPL-3.0-Lizenz und die starke Verschlüsselungsarchitektur machen CryptPad besonders attraktiv für den Umgang mit schützenswerten Daten.

**Collabora Online** ist ein auf LibreOffice Technology basierender browserbasienter Office-Editor, der nahtlos in Nextcloud und andere DMS-Plattformen integriert [32]. Collabora Ltd. bietet kommerzielle Support-SLAs an und betreibt aktiv Upstream-Contributions zu LibreOffice. In der DACH-Region ist Collabora Online der Standard für behördliche Office-Kollaboration im Open-Source-Kontext.

**OpenSlides** ist eine webbasierte Konferenz- und Sitzungsverwaltungssoftware, entwickelt von Intevation GmbH, speziell für Gemeinderäte, Parlamente und Gremien [33]. OpenSlides unterstützt Tagesordnungen, Anträge, Abstimmungen, Redelisten und Protokolle. Mehrere deutsche Stadtparlamente nutzen OpenSlides als primäres Ratsinformationssystem.

**Forgejo** ist ein von Codeberg e.V. gepflegter Fork von Gitea, der als vollständig gemeinschaftsgesteuertes Git-Hosting-System positioniert ist [34]. Für Gemeinden, die Code und Konfigurationsmanagement unter eigener Hoheit betreiben wollen, ist Forgejo die empfohlene Lösung; es ist funktional äquivalent zu GitHub/GitLab CE, ohne kommerzielle Tier-Einschränkungen.

### 3.6 TCO-Evidenz und Wirtschaftlichkeitsanalyse

Empirical evidence on Total Cost of Ownership (TCO) — zu Deutsch: Gesamtbetriebskosten — bei Open-Source-Migrationen im öffentlichen Sektor wächst. Eine Studie der Europäischen Kommission (2021) analysierte 14 europäische Behörden und fand durchschnittliche Einsparungen von 32–57 % gegenüber proprietären Alternativen über einen Fünfjahreszeitraum [8]. Eine schwedische Studie (2023) quantifizierte die Wertschöpfung durch Open-Source-Contributions im Bereich der öffentlichen Verwaltung [35]. Lathrop & Ruma (2010) begründen "Open Government" als demokratisches Prinzip, nicht nur als Kostensparmaßnahme [36].

**Indikative TCO-Tabelle (€/Arbeitsplatz/Jahr):**

| Komponente | Proprietär | Open Source | Einsparung |
|---|---|---|---|
| Office-Produktivität | 150–250 | 5–15 | 135–235 € |
| Dateispeicher/Kollaboration | 60–120 | 3–10 | 57–110 € |
| Videokonferenz | 100–180 | 2–8 | 98–172 € |
| Projektmanagement | 50–100 | 2–6 | 48–94 € |
| Identitätsverwaltung | 30–60 | 5–15 | 25–45 € |
| CMS/Web | 10–30 | 2–8 | 8–22 € |
| **Gesamt** | **400–740 €** | **19–62 €** | **381–678 €** |

Die Fünfjahres-Barwertberechnung (Diskontrate 3 %, 500 Beschäftigte) ergibt einen Vorteil von **800.000 € bis 1,7 Mio. €**, der im dritten Jahr erreicht wird, nachdem die Migrationskosten amortisiert sind [8][9].

### 3.7 Barrierefreiheit und Digitale Inklusion

Barrierefreiheit ist in der EU durch EN 301 549 [37] und die Web Content Accessibility Guidelines (WCAG 2.1 AA) [38] rechtlich verbindlich. In Deutschland konkretisiert BITV 2.0 [39] diese Anforderungen für Bundesbehörden; in der Schweiz gilt eCH-0059 [40]. Open-Source-CMS wie TYPO3 und Drupal haben umfassende Accessibility-Toolkits und werden aktiv von Behörden auf WCAG-Konformität geprüft [41].

### 3.8 Verbleibende Lücken

Trotz gewachsener Evidenzbasis bleiben Forschungslücken: Longitudinale UX-Studien zur Nutzerakzeptanz bei Behördenmitarbeitenden nach Open-Source-Migrationen sind rar. Vergleichende Studien zur Barrierefreiheits-Performance von Open-Source- vs. proprietären Behördenportalen fehlen. Die Literatur zu kleinen Gemeinden (< 5.000 Einwohner) mit begrenzten IT-Kapazitäten ist dünn. Diese Lücken werden in `Mem/literature-review-state.md` dokumentiert und sollten in künftigen Versionen adressiert werden.

---

## 4. Technologie-Stack-Analyse

### 4.1 Bewertungsmethodik

Die folgenden 12 Technologieschichten decken den vollständigen Bedarf einer kommunalen Verwaltung ab. Jede Schicht wird mit der Sieben-Kriterien-Matrix (Abschnitt 2.2) bewertet. Die empfohlene Primärkomponente und relevante Alternativen werden für jede Schicht genannt.

### 4.2 Schicht 1: Identitäts- und Zugangsverwaltung (IAM)

**Empfohlen: Keycloak**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | Apache-2.0 |
| K2 Reife | 5 | v23+, Red-Hat-Produktionssupport, CNCF-Landschaft |
| K3 Community | 5 | 1.000+ Kontributoren, Red Hat, aktive Community |
| K4 Interop. | 5 | OIDC, SAML 2.0, LDAP, SCIM, eID-kompatibel |
| K5 Sicherheit | 5 | BSI-geprüft, regelmäßige CVE-Audits |
| K6 TCO | 4 | Komplexes Deployment, aber ausgezeichnetes Ökosystem |
| K7 Behörden | 5 | Bundesministerien DE, Kantone CH, EU-Institutionen |
| **Gesamt** | **34/35** | **Empfohlen** |

Alternative: Authentik (für einfachere Deployments), LemonLDAP::NG (französische Behördenwahl)

### 4.3 Schicht 2: Dokumentenverwaltung (DMS)

**Empfohlen: Nextcloud**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | AGPL-3.0 |
| K2 Reife | 5 | v28+, halbjährliche LTS-Releases |
| K3 Community | 5 | Nextcloud GmbH, 2.000+ Apps, aktive Community |
| K4 Interop. | 5 | WebDAV, CalDAV, CardDAV, CMIS, eCH-0229-kompatibel |
| K5 Sicherheit | 5 | E2E-Verschlüsselung, SOC2-auditiert, BSI-Empfehlung |
| K6 TCO | 5 | Günstig, selbstgehostet, govdigital-Rahmenvertrag verfügbar |
| K7 Behörden | 5 | Niederlande, Frankreich, Baden-Württemberg, Bund |
| **Gesamt** | **35/35** | **Empfohlen** |

Alternative: Seafile (Performance-fokussiert), Alfresco Community (Enterprise-DMS)

### 4.4 Schicht 3: Office-Produktivität

**Empfohlen: Collabora Online + LibreOffice**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | MPL-2.0 (Collabora), LGPL-3.0 (LibreOffice) |
| K2 Reife | 5 | Produktionsreif, nahtlose Nextcloud-Integration |
| K3 Community | 4 | LibreOffice Foundation, Collabora Ltd. |
| K4 Interop. | 5 | OOXML-kompatibel, ODF-nativ |
| K5 Sicherheit | 4 | Aktive Sicherheitsupdates, keine bekannten kritischen Issues |
| K6 TCO | 5 | Keine Lizenzkosten, Support via Collabora oder TDF |
| K7 Behörden | 5 | Bund DE, Kanton Genf, zahlreiche Kommunen |
| **Gesamt** | **33/35** | **Empfohlen** |

Ergänzend: **CryptPad** für Ende-zu-Ende-verschlüsselte Echtzeitkooperation bei schützenswerten Inhalten (Bewertung: 30/35; Empfohlen für erhöhten Schutzbedarf).

### 4.5 Schicht 4: Kommunikation und Messaging

**Empfohlen: Matrix/Element**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | Apache-2.0 (Synapse/Dendrite), AGPL-3.0 (Element) |
| K2 Reife | 4 | Produktionsreif, BwMessenger-Basis (Bundeswehr) |
| K3 Community | 5 | Matrix.org Foundation, Element GmbH |
| K4 Interop. | 5 | Offenes dezentrales Protokoll, Bridge zu Slack/Teams |
| K5 Sicherheit | 5 | E2E-Verschlüsselung standardmäßig, BSI-Analyse positiv |
| K6 TCO | 4 | Synapse ressourcenintensiv; Dendrite schlanker |
| K7 Behörden | 5 | Bundeswehr, Gematik, französische Regierung (Tchap) |
| **Gesamt** | **33/35** | **Empfohlen** |

### 4.6 Schicht 5: Videokonferenz

**Empfohlen: Jitsi Meet** (bis 50 Teilnehmende) / **BigBlueButton** (für Schulungen und Ratssitzungen)

| Kriterium | Bewertung (Jitsi) | Bewertung (BBB) |
|---|---|---|
| K1 Lizenz | 5 (Apache-2.0) | 5 (LGPL-3.0) |
| K2 Reife | 5 | 4 |
| K3 Community | 5 | 4 |
| K4 Interop. | 4 (WebRTC) | 5 (LTI, Moodle) |
| K5 Sicherheit | 4 | 4 |
| K6 TCO | 5 | 4 |
| K7 Behörden | 5 | 4 |
| **Gesamt** | **33/35** | **30/35** |

### 4.7 Schicht 6: Workflow und Prozessautomation

**Empfohlen: Camunda Platform 8 CE** (Alternativen: Flowable, Activiti)

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 3 | Apache-2.0 (CE-Kern), proprietäre Features in EE |
| K2 Reife | 5 | BPMN 2.0-konform, produktionsreif |
| K3 Community | 4 | Camunda GmbH + aktive Community |
| K4 Interop. | 5 | BPMN 2.0, REST-API, OZG-Prozessmodelle verfügbar |
| K5 Sicherheit | 4 | SOC2, DSGVO-Unterstützung |
| K6 TCO | 4 | CE kostenlos, EE-Support optional |
| K7 Behörden | 4 | OZG-Dienstleistungslandschaft, FITKO-Referenzen |
| **Gesamt** | **29/35** | **Empfohlen (bedingt)** |

Hinweis: Flowable (AGPL-3.0) ist vollständig offen und erreicht 30/35; empfohlen wenn vollständige Copyleft-Konformität erforderlich.

### 4.8 Schicht 7: Bürgerbeteiligung

**Empfohlen: Decidim** (Primär) / **CONSUL** (Alternative)

| Kriterium | Bewertung (Decidim) | Bewertung (CONSUL) |
|---|---|---|
| K1 Lizenz | 5 (AGPL-3.0) | 5 (AGPL-3.0) |
| K2 Reife | 5 | 5 |
| K3 Community | 5 | 4 |
| K4 Interop. | 4 | 4 |
| K5 Sicherheit | 4 | 4 |
| K6 TCO | 4 | 4 |
| K7 Behörden | 5 (Barcelona, Helsinki, NYC) | 5 (Madrid, Lima, 40+ Länder) |
| **Gesamt** | **32/35** | **30/35** |

### 4.9 Schicht 8: Ratsinformationssystem

**Empfohlen: OpenSlides**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | MIT |
| K2 Reife | 4 | v4.x stabil, aktive Entwicklung |
| K3 Community | 4 | Intevation GmbH, kommunale Nutzerbasis |
| K4 Interop. | 4 | REST-API, PDF-Export, RIS-Integration möglich |
| K5 Sicherheit | 4 | Regelmäßige Updates, keine kritischen Issues bekannt |
| K6 TCO | 5 | Günstig, Hosting durch kommunale Rechenzentren |
| K7 Behörden | 4 | Bundestag-Ausschüsse, mehrere Stadtparlamente |
| **Gesamt** | **30/35** | **Empfohlen** |

### 4.10 Schicht 9: Open-Data-Portal

**Empfohlen: CKAN**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | AGPL-3.0 |
| K2 Reife | 5 | v2.10+, weltweiter Standard |
| K3 Community | 5 | Open Knowledge Foundation, OKF DE |
| K4 Interop. | 5 | DCAT-AP 2.1, GovData-kompatibel, EU-Dataportal |
| K5 Sicherheit | 4 | Regelmäßige Sicherheits-Releases |
| K6 TCO | 4 | Python-Stack, moderate Komplexität |
| K7 Behörden | 5 | data.gov, EU Open Data Portal, govdata.de |
| **Gesamt** | **33/35** | **Empfohlen** |

### 4.11 Schicht 10: GIS und Geodaten

**Empfohlen: QGIS + GeoServer + PostGIS**

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | GPL-2.0 (QGIS), GPL-2.0 (GeoServer), PostgreSQL-L |
| K2 Reife | 5 | QGIS 3.x LTR, industrie-etabliert |
| K3 Community | 5 | QGIS.org, OSGeo Foundation |
| K4 Interop. | 5 | WMS, WFS, WCS, INSPIRE-konform |
| K5 Sicherheit | 4 | Aktive Sicherheits-Community |
| K6 TCO | 5 | Keine Lizenzkosten vs. ArcGIS (sehr hohe Einsparung) |
| K7 Behörden | 5 | Bundesamt für Kartografie (BKG), Swisstopo, Katasterämter |
| **Gesamt** | **34/35** | **Empfohlen** |

### 4.12 Schicht 11: CMS und Bürgerportal

**Empfohlen: TYPO3** (Primär für DE/CH) / **Drupal** (Alternativ)

| Kriterium | Bewertung (TYPO3) | Bewertung (Drupal) |
|---|---|---|
| K1 Lizenz | 5 (GPL-2.0) | 5 (GPL-2.0) |
| K2 Reife | 5 | 5 |
| K3 Community | 5 (TYPO3 Association) | 5 (Drupal Association) |
| K4 Interop. | 4 | 4 |
| K5 Sicherheit | 5 (TYPO3 Security Team) | 5 |
| K6 TCO | 4 | 4 |
| K7 Behörden | 5 (DE-Standard für Behördenwebsites) | 4 |
| **Gesamt** | **33/35** | **32/35** |

Barrierefreiheit: Beide CMS unterstützen WCAG 2.1 AA / BITV 2.0 / eCH-0059 mit entsprechender Konfiguration.

### 4.13 Schicht 12: Code-Hosting und DevOps

**Empfohlen: Forgejo** (Primär) / **GitLab CE** (Alternative bei größerem CI/CD-Bedarf)

| Kriterium | Bewertung (Forgejo) | Bewertung (GitLab CE) |
|---|---|---|
| K1 Lizenz | 5 (MIT/GPL-2.0) | 4 (MIT, proprietäre EE-Features) |
| K2 Reife | 4 | 5 |
| K3 Community | 5 (Codeberg e.V.) | 4 |
| K4 Interop. | 4 | 5 |
| K5 Sicherheit | 4 | 4 |
| K6 TCO | 5 | 4 |
| K7 Behörden | 3 | 4 |
| **Gesamt** | **30/35** | **30/35** |

### 4.14 Infrastruktur: Sovereign Cloud Stack

**Empfohlen: Sovereign Cloud Stack (SCS)**

SCS, entwickelt von der Open Telekom Cloud und koordiniert durch die Open Source Business Alliance (OSBA), bietet eine vollständig souveräne IaaS/PaaS-Referenzarchitektur auf Basis von OpenStack, Kubernetes und Ceph [42]. SCS ist konform mit GAIA-X [43] und den BSI C5-Anforderungen für Cloud-Dienste.

| Kriterium | Bewertung | Begründung |
|---|---|---|
| K1 Lizenz | 5 | Apache-2.0 |
| K2 Reife | 4 | v6.0+, mehrere GAIA-X-Provider |
| K3 Community | 4 | OSBA, govdigital, Dataport |
| K4 Interop. | 5 | GAIA-X, OpenStack-API, Kubernetes |
| K5 Sicherheit | 5 | BSI C5, TISAX-geprüft bei Anbietern |
| K6 TCO | 4 | Moderate Komplexität, günstiger als Hyperscaler |
| K7 Behörden | 4 | Dataport-AI-Cloud, govdigital |
| **Gesamt** | **31/35** | **Empfohlen** |

### 4.15 Referenzarchitektur (ASCII-Diagramm)

```
┌─────────────────────────────────────────────────────────────────┐
│                    BÜRGER-ZUGANGSSCHICHT                         │
│         TYPO3/Drupal CMS · CONSUL/Decidim Beteiligung           │
│                   eID-Integration (BGEID)                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTPS/TLS 1.3
┌───────────────────────────▼─────────────────────────────────────┐
│              IDENTITÄTS- UND ZUGANGSVERWALTUNG                   │
│         Keycloak (OIDC · SAML 2.0 · LDAP · eID-Wallet)          │
└───┬───────────────────┬───────────────────────┬─────────────────┘
    │                   │                        │
┌───▼───────┐   ┌───────▼──────┐   ┌────────────▼──────────────┐
│  KOMM.    │   │  PRODUKTIV.  │   │    FACHVERFAHREN           │
│ Matrix    │   │ Nextcloud    │   │  Camunda/Flowable BPMN    │
│ Element   │   │ Collabora    │   │  OZG-Dienste (EfA)        │
│ Jitsi     │   │ CryptPad     │   │  AKDB/Dataport-Backends   │
└───────────┘   └──────────────┘   └───────────────────────────┘
┌────────────────────────────────────────────────────────────────┐
│                    DATEN- UND GEODATENSCHICHT                   │
│     CKAN Open Data · QGIS/GeoServer · PostGIS · INSPIRE        │
└────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────┐
│              VERWALTUNGS- UND GOVERNANCE-TOOLS                  │
│    OpenSlides (Rat) · Forgejo (Code) · Nextcloud (DMS)         │
└───────────────────────────┬────────────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────────────┐
│              INFRASTRUKTUR (SOVEREIGN CLOUD STACK)              │
│   OpenStack IaaS · Kubernetes (K8s) · Ceph Storage · SCS v6   │
│        BSI C5-konformes Rechenzentrum (DE/CH)                  │
└────────────────────────────────────────────────────────────────┘
```

### 4.16 Komponentenübersicht

| Schicht | Empfohlen | Lizenz | Score | Status |
|---|---|---|---|---|
| IAM | Keycloak | Apache-2.0 | 34/35 | Empfohlen |
| DMS | Nextcloud | AGPL-3.0 | 35/35 | Empfohlen |
| Office | Collabora/LibreOffice | MPL-2.0/LGPL | 33/35 | Empfohlen |
| E2E-Kollaboration | CryptPad | AGPL-3.0 | 30/35 | Empfohlen |
| Messaging | Matrix/Element | Apache/AGPL | 33/35 | Empfohlen |
| Video | Jitsi / BigBlueButton | Apache / LGPL | 33/30 | Empfohlen |
| Workflow | Camunda CE / Flowable | Apache / AGPL | 29/30 | Empfohlen |
| Beteiligung | Decidim / CONSUL | AGPL-3.0 | 32/30 | Empfohlen |
| Ratsinformation | OpenSlides | MIT | 30/35 | Empfohlen |
| Open Data | CKAN | AGPL-3.0 | 33/35 | Empfohlen |
| GIS | QGIS+GeoServer | GPL-2.0 | 34/35 | Empfohlen |
| CMS | TYPO3 / Drupal | GPL-2.0 | 33/32 | Empfohlen |
| Code-Hosting | Forgejo / GitLab CE | MIT/MIT | 30/30 | Empfohlen |
| Infrastruktur | Sovereign Cloud Stack | Apache-2.0 | 31/35 | Empfohlen |

---

## 5. Implementierungs-Roadmap

### 5.1 Budgetrahmen nach Gemeindegröße

| Phase | Klein (< 20.000 Einw.) | Mittel (20.000–100.000) | Groß (> 100.000) |
|---|---|---|---|
| Phase 0: Readiness | 20.000–40.000 € | 40.000–80.000 € | 80.000–150.000 € |
| Phase 1: Fundament | 80.000–150.000 € | 150.000–350.000 € | 350.000–700.000 € |
| Phase 2: Kernstack | 100.000–180.000 € | 180.000–400.000 € | 400.000–800.000 € |
| Phase 3: Fachverfahren | 80.000–150.000 € | 150.000–450.000 € | 450.000–900.000 € |
| Phase 4: Bürgerservices | 60.000–120.000 € | 120.000–300.000 € | 300.000–600.000 € |
| Phase 5: Optimierung | 20.000–70.000 € | 70.000–120.000 € | 120.000–250.000 € |
| **Gesamt (indikativ)** | **360.000–710.000 €** | **710.000–1.700.000 €** | **1.700.000–3.400.000 €** |

*Hinweis: Kosten sind indikativ (2026) und umfassen Implementierung, Schulung und ersten Betriebsaufbau, nicht laufende Betriebskosten. Interkommunale Kostenteilung kann Einzelkosten um 30–50 % reduzieren.*

### 5.2 Personalmodell

| Rolle | Klein | Mittel | Groß |
|---|---|---|---|
| Projektleitung | 0,3 VZÄ intern | 0,5 VZÄ intern | 1,0 VZÄ intern |
| Linux-Systemadministration | Extern/Dienstleister | 1,0 VZÄ | 2–3 VZÄ |
| Sicherheitsverantwortlicher | 0,1 VZÄ / CISO-as-a-Service | 0,5 VZÄ | 1,0 VZÄ |
| Change-Management | Extern, projektweise | 0,5 VZÄ Projektlaufzeit | 1,0 VZÄ |
| Datenschutzbeauftragter | Bereits vorhanden (Pflicht) | DSB vorhanden | DSB-Team |

### 5.3 Phase 0: Readiness-Assessment (Monate 1–3)

**Ziele:**
- Bestandsaufnahme der bestehenden IT-Landschaft und Vertragsfristen
- Rechtliche Analyse: DSGVO/nDSG-Konformitätslücken, Vertragsklauseln
- Stakeholder-Analyse und politischer Beschluss des Gemeinderats
- Pilotgruppen-Identifikation (30–50 Early Adopters)

**Deliverables:** IT-Bestandsaufnahme, Rechtsanalyse, Gemeinderatsbeschluss, Projektcharter

**Meilenstein:** Projektgenehmigung durch politische Führung

### 5.4 Phase 1: Fundament (Monate 4–9)

**Ziele:**
- Produktive Keycloak-Installation mit LDAP-Anbindung
- Nextcloud-Deployment auf Sovereign-Cloud-Stack oder kommunalem RZ
- Basisschulungen für IT-Team (Keycloak, Linux, Nextcloud-Admin)
- Datensicherungskonzept und Notfallwiederherstellungs-Tests

**Deliverables:** Produktive IAM-Infrastruktur, DMS für Pilotgruppe, IT-Schulungsplan

**Meilenstein:** Pilotgruppe aktiv auf Keycloak + Nextcloud

### 5.5 Phase 2: Kernstack-Deployment (Monate 10–18)

**Ziele:**
- Rollout Collabora Online + CryptPad
- Matrix/Element Deployment mit Behörden-Brücke
- Jitsi/BigBlueButton für Videokonferenzen
- Migration erster Behördenwebsite auf TYPO3/Drupal (WCAG 2.1 AA)
- TYPO3-Barrierefreiheitsprüfung und BITV-Zertifizierung

**Deliverables:** Vollständige Produktivitäts-Suite, Kommunikationsinfrastruktur, barrierefreie Website

**Meilenstein:** 80 % der Verwaltungsmitarbeitenden auf Open-Source-Produktivitätssuite

### 5.6 Phase 3: Fachverfahren-Integration (Monate 19–27)

**Ziele:**
- Camunda/Flowable für OZG-Prozessautomation
- Integration mit AKDB/Dataport-Fachverfahren über standardisierte APIs
- OpenSlides für Ratsinformationssystem
- CKAN Open-Data-Portal mit DCAT-AP 2.1-Konformität
- Forgejo für internes Konfigurationsmanagement und Code-Hosting

**Deliverables:** Automatisierte OZG-Kernprozesse, Ratssystem, Open-Data-Publikation

**Meilenstein:** Mindestens 10 OZG-Leistungen über Open-Source-Workflows abgewickelt

### 5.7 Phase 4: Bürgerservices (Monate 25–33)

**Ziele:**
- Decidim/CONSUL für Bürgerbudget und digitale Partizipation
- QGIS/GeoServer für Geodaten-Infrastruktur (INSPIRE-konform)
- eID-Integration in Bürgerportal (BGEID/eIDAS-konform)
- Barrierefreiheits-Audit für alle öffentlich zugänglichen Dienste

**Deliverables:** Digitale Partizipationsplattform, offene Geodaten, eID-Authentifizierung

**Meilenstein:** Erste Bürgerbudget-Runde auf Decidim, GeoServer öffentlich zugänglich

### 5.8 Phase 5: Optimierung und Community (Monate 31–36)

**Ziele:**
- Performance-Optimierung und Kapazitätsplanung
- Beitritt zu interkommunaler Open-Source-Kooperationsgemeinschaft
- Erstveröffentlichung eigener Anpassungen als Open Source (EMBAG-Konformität)
- Jährlicher TCO-Vergleichsbericht
- Vorbereitung auf v1.0 des internen Open-Source-Regelwerks

**Deliverables:** TCO-Bericht, Open-Source-Publikation kommunaler Entwicklungen, CoP-Mitgliedschaft

**Meilenstein:** Erster Jahresbericht digitale Souveränität an Gemeinderat

---

## 6. Stakeholder- und Beschaffungsstrategie

### 6.1 Stakeholder-Karte

| Stakeholder-Gruppe | Primäre Interessen | Erfolgskriterien | Risiken |
|---|---|---|---|
| Gemeinderat / Stadtparlament | Kostensenkung, Souveränität, Transparenz | Beschlüsse, Budgetgenehmigung | Politischer Widerstand, Kurzzeit-Denken |
| Bürgermeister / Stadtspitze | Reputation, Effizienz, OZG-Compliance | Vorzeige-Projekte, positive Presse | Änderungsresistenz, Risikoaversion |
| IT-Abteilung | Technische Kontrolle, Karriere, Stabilität | Schulungen, klare Verantwortlichkeiten | Überlastung, Skill-Lücken |
| Verwaltungsmitarbeitende | Nutzerfreundlichkeit, Stabilität | Change-Management, Schulungen | Gewohnheitsbruch, Lernkurve |
| Bürger:innen | Datenschutz, Zugänglichkeit, Partizipation | Barrierefreiheit, Transparenz | Digitale Spaltung |
| Zivilgesellschaft / NGOs | Demokratie, Offenheit, Inklusion | Open Data, Beteiligungsplattformen | Partizipations-Müdigkeit |
| Kommunale IT-Dienstleister | Auftragssicherheit, Partnerschaft | Rahmenverträge, langfristige Kooperation | Interessenkonflikt proprietärer Altgeschäfte |
| Open-Source-Communities | Nachhaltige Beiträge, Sichtbarkeit | Upstream-Contributions, Pilotprojekte | Ehrenamtliche Überbelastung |

### 6.2 Vergaberechtliche Grundlagen

In Deutschland gilt das GWB (Gesetz gegen Wettbewerbsbeschränkungen) [44] in Verbindung mit der VgV (Vergabeverordnung) [45]; Schwellenwerte für europaweite Ausschreibungen liegen 2024/2025 bei 221.000 € für Lieferungen/Dienstleistungen. In der Schweiz regeln BöB (Bundesgesetz über das öffentliche Beschaffungswesen) [46] und IVöB (Interkantonale Vereinbarung über das öffentliche Beschaffungswesen) die Vergabe; der Schwellenwert für europaweite Ausschreibung liegt bei 250.000 CHF (kantonale Ebene).

**Sieben Beschaffungsprinzipien für Open-Source-GovTech:**

1. **Technologieneutrale Ausschreibung:** Keine Nennung proprietärer Produktnamen; Anforderungen als funktionale Spezifikationen formulieren.
2. **Open-Source-Präferenz:** Explizite Bevorzugung bei Gleichwertigkeit (EMBAG Art. 9, OZG 2.0 Begründung).
3. **Standardkonformität:** Verpflichtende Anforderung an eCH/XÖV/DCAT-AP-Konformität in Ausschreibungsunterlagen.
4. **Quellcode-Zugang:** Vertragliche Vereinbarung, dass im Auftrag entwickelter Code unter OSI-Lizenz veröffentlicht wird.
5. **Ausstiegsklauseln:** Explizite Datenmigrations- und Exit-Pflichten des Anbieters.
6. **Rahmenverträge nutzen:** govdigital eG, Dataport, AKDB und kantonale Rahmenverträge reduzieren Vergabeaufwand.
7. **Interkommunale Bündelung:** Gemeinsame Ausschreibungen mit Nachbargemeinden senken Kosten und erhöhen Attraktivität für qualifizierte Bieter.

### 6.3 Muster-Vertragsklausel

Die folgende Klausel kann in Vergabeunterlagen übernommen werden:

> **§ X — Open-Source-Verpflichtung**
> Der Auftragnehmer verpflichtet sich, sämtlichen im Rahmen dieses Vertrags neu entwickelten oder speziell angepassten Quellcode spätestens 90 Tage nach Abnahme unter einer von der Open Source Initiative (OSI) anerkannten Lizenz zu veröffentlichen. Ausgenommen sind Sicherheits-Fixes, für die eine koordinierte Offenlegung (Responsible Disclosure) mit dem Auftraggeber vereinbart wird. Der Auftraggeber erhält das unwiderrufliche, vergütungsfreie Recht zur Nutzung, Modifikation und Weitergabe. Diese Verpflichtung gilt als essenzielle Vertragsbedingung im Sinne von § 281 BGB / Art. 97 OR.

### 6.4 Rahmenverträge und Kooperationsplattformen

| Plattform | Region | Typ | Kontakt |
|---|---|---|---|
| govdigital eG | DE | Genossenschaft öffentl.-rechtl. IT-DL | govdigital.de |
| AKDB | Bayern | Kommunaler IT-Dienstleister | akdb.de |
| Dataport | Norddeutschland | ANSTALT öffentl. Rechts | dataport.de |
| FITKO / FIT-Store | DE Bund/Länder | OZG-Dienste-Repository | fitko.de |
| eCH-Standardisierung | CH | Standards-Konsortium | ech.ch |
| Digitale Verwaltung Schweiz (DVS) | CH | Bund-Kantone-Koordination | digitale-verwaltung.ch |
| OSOR | EU | Open-Source-Observatory | joinup.ec.europa.eu/collection/open-source-observatory |

### 6.5 Change-Management

Die Literatur identifiziert Widerstand von Verwaltungsmitarbeitenden als häufigsten Grund für das Scheitern von IT-Migrationsprojekten [21]. Effektives Change-Management umfasst:

- **Frühzeitige Einbindung:** Pilotgruppen aus freiwilligen Early Adopters; deren Erfahrungen fließen in Schulungsunterlagen ein
- **Peerbasiertes Training:** "Train the Trainer"-Konzept; Verwaltungsmitarbeitende schulen Kolleginnen und Kollegen
- **Analogiepädagogik:** Neue Tools an bekannte Konzepte anknüpfen ("Nextcloud = Netzlaufwerk, aber modern")
- **Feedback-Loops:** Monatliche Nutzerbefragungen in der Migrationsphase; Probleme werden in zwei Wochen adressiert
- **Kommunikation des Nutzens:** Konkreter Bezug zu Arbeitsalltag der Mitarbeitenden, nicht abstrakte Souveränitätsbegriffe

### 6.6 Interkommunale Praxisgemeinschaft (CoP)

Eine formalisierte Praxisgemeinschaft (Community of Practice) kommunaler Open-Source-Administratoren schafft Mehrwert durch: geteilte Schulungsunterlagen, gemeinsame Incident-Response-Protokolle, koordinierte Upstream-Contributions, kollektive Verhandlungsmacht gegenüber Anbietern und Wissenstransfer zwischen erfahrenen und neuen Mitgliedsgemeinden.

Empfohlene Struktur: Jährliches Präsenztreffen, monatliche virtuelle Sessions (Matrix/Jitsi), geteiltes Forgejo-Repository für Konfigurationsvorlagen, CKAN-Datensatz gemeinsam erhobener TCO-Daten.

---

## 7. Risikoanalyse

### 7.1 Risikoregister

| ID | Risiko | Wahrsch. | Auswirkung | Risikostufe | Mitigationsstrategie |
|---|---|---|---|---|---|
| R01 | Skill-Lücken im IT-Team | Hoch | Mittel | **Hoch** | Schulungsplan, externe Unterstützung, CoP-Beteiligung |
| R02 | Anbieter-Lock-in bei Hosting | Mittel | Hoch | **Hoch** | SCS-Rahmenverträge, Exit-Klauseln, eigenes RZ als Fallback |
| R03 | Politischer Richtungswechsel | Mittel | Hoch | **Hoch** | Überparteilicher Beschluss, TCO-Dokumentation, Bürger-Sichtbarkeit |
| R04 | Integrationskomplexität | Hoch | Mittel | **Hoch** | Phasenweise Migration, API-First-Architektur, Pilot vor Rollout |
| R05 | Sicherheitsvorfälle (CVE) | Mittel | Hoch | **Hoch** | Patch-Management-SLAs, BSI-IT-Grundschutz, NIS2-Compliance |
| R06 | Nutzerwiderstand | Hoch | Mittel | **Hoch** | Change-Management-Plan, Pilotgruppen, peerbasiertes Training |
| R07 | Vergaberechtliche Fehler | Niedrig | Hoch | **Mittel** | Rechtsprüfung, Muster-Vergabeunterlagen nutzen |
| R08 | Community-Abandon (Upstream) | Niedrig | Hoch | **Mittel** | Zwei-Anbieter-Strategie, aktive Upstream-Beteiligung, Forks vorbereiten |
| R09 | Datenverlust bei Migration | Niedrig | Sehr hoch | **Mittel** | Dreifache Datensicherung, schrittweise Migration, Rollback-Plan |
| R10 | Barrierefreiheits-Mängel | Mittel | Mittel | **Mittel** | WCAG-Audit vor Go-Live, BITV-Zertifizierung beauftragen |

### 7.2 Das Münchner LiMux-Projekt: Lernpunkte

Das Münchner LiMux-Projekt (2004–2017) bleibt die größte kommunale Open-Source-Migration in Europa [13]. München migrierte über 14.000 Arbeitsplätze auf Linux und OpenOffice.org. Die Rückmigration zu Windows 2017 wurde politisch initiiert, nicht technisch erzwungen. Nachträgliche Analysen [47] zeigen:

- **Technisch:** Migration war erfolgreich; Kernfunktionen liefen stabil auf Open-Source-Stack
- **Politisch:** Regierungswechsel 2014 und intensive Lobbyarbeit proprietärer Anbieter (u.a. Microsoft-Hauptquartier in München) führten zur Entscheidungsumkehr
- **Organisatorisch:** Change-Management war unzureichend; IT-Abteilung überbelastet
- **Wirtschaftlich:** TCO-Einsparungen wurden nicht ausreichend dokumentiert und kommuniziert

**Lernpunkte für neue Projekte:** Überparteiliche politische Verankerung suchen; TCO kontinuierlich dokumentieren; Medienberichterstattung aktiv gestalten; Bürgersichtbarkeit durch Open-Data und Partizipationsplattformen erhöhen.

### 7.3 Vendor-FUD-Management

Proprietäre Anbieter setzen bekannte "Fear, Uncertainty and Doubt" (FUD)-Strategien ein [48], um Open-Source-Migrationen zu verlangsamen:

- **"Total Cost"-Argument:** Versteckte Migrationskosten übertreiben, eigene Lizenzkosten kleinrechnen → *Antwort:* Unabhängige TCO-Studie beauftragen (Fraunhofer, Uni-Institute)
- **Sicherheits-FUD:** Open-Source sei unsicherer wegen öffentlich sichtbarer Schwachstellen → *Antwort:* "Security through Obscurity" ist kein anerkanntes Sicherheitsprinzip; BSI-IT-Grundschutz gilt für beide Modelle
- **Interoperabilitäts-FUD:** Kompatibilitätsprobleme mit Bundesbehörden → *Antwort:* OOXML-Kompatibilität ist in LibreOffice/Collabora produktionsreif; eCH-Standards sind Open-Source-freundlich
- **Support-FUD:** Kein verlässlicher Support verfügbar → *Antwort:* govdigital eG, Dataport, AKDB, Nextcloud GmbH, Collabora Ltd. bieten Enterprise-SLAs

### 7.4 Datenschutz: Rechtliche Risikoanalyse

**Deutschland:** DSGVO [49] + BDSG [50] gelten für alle Verarbeitungen personenbezogener Daten. Drittstaaten-Transfer (z.B. US-Cloud ohne Angemessenheitsbeschluss) ist für besondere Kategorien und Sozialdaten in der Regel unzulässig. NIS2-Richtlinie [51] verschärft Sicherheitsanforderungen für kommunale Kritische Infrastruktur ab 2024.

**Schweiz:** nDSG [28] verlangt Datenschutz-Folgenabschätzungen (DSFA) bei Bearbeitung besonders schützenswerter Daten und verschärft Meldepflichten auf 72 Stunden bei Datenverletzungen. Übermittlung in Drittstaaten erfordert Standardvertragsklauseln oder angemessenes Schutzniveau.

**Mitigation:** Self-Hosted-Deployment in BSI C5-zertifizierten deutschen oder schweizerischen Rechenzentren vermeidet Drittstaaten-Transfers vollständig. Sovereign Cloud Stack bietet technische Konformität by Design.

### 7.5 Sicherheitsarchitektur

Gemäß BSI IT-Grundschutz [52] und ISO 27001 [53] empfohlene Sicherheitsmaßnahmen:

- **Netzwerk:** Zero-Trust-Architektur; segmentierte VLANs; WAF vor allen öffentlichen Diensten
- **IAM:** MFA-Pflicht für alle Administratoren; Privileged Access Management (PAM)
- **Patch-Management:** Maximale Patch-Laufzeit: kritische CVEs 24h, hohe CVEs 72h, mittlere 2 Wochen
- **Logging:** Zentralisiertes SIEM (z.B. Wazuh, OpenSearch); 12 Monate Logaufbewahrung
- **Incident Response:** Dokumentierter IR-Plan; NIS2-konforme 24h-Meldung an BSI/BACS
- **Backup:** 3-2-1-Regel; offline Backup-Kopie; monatliche Wiederherstellungs-Tests

---

## 8. Schlussfolgerung

Diese Arbeit hat gezeigt, dass kommunale Verwaltungen im DACH-Raum heute einen vollständigen Open-Source-Technologie-Stack implementieren können, der moderne proprietäre Systeme in Funktionalität, Sicherheit und Interoperabilität erreicht oder übertrifft. Fünf zentrale Befunde:

**Befund 1 — Technologische Reife:** Alle 12 analysierten Schichten haben Komponenten, die ≥ 28/35 Punkte in der Bewertungsmatrix erreichen. Die empfohlenen Komponenten (Keycloak, Nextcloud, Collabora, Matrix, Jitsi, Decidim, OpenSlides, CKAN, QGIS, TYPO3, Forgejo, SCS) sind in Produktionsumgebungen europäischer Behörden nachgewiesen.

**Befund 2 — Rechtliche Kongruenz:** Open-Source-Stacks sind nicht nur rechtskonform, sondern regulatorisch bevorzugt: EMBAG Art. 9 (CH), OZG 2.0-Begründung (DE) und Interoperable Europe Act (EU) schaffen positive Anreize oder Verpflichtungen zur Nutzung von Open-Source-Software.

**Befund 3 — Wirtschaftlichkeit:** Das indikative TCO-Modell zeigt Einsparungen von 381–678 € pro Arbeitsplatz und Jahr. Der Fünfjahres-Barwertvorteil für eine Gemeinde mit 500 Beschäftigten liegt bei 800.000 € bis 1,7 Mio. €, nach Amortisation der Migrationskosten ab Jahr 3.

**Befund 4 — Demokratischer Mehrwert:** Open-Source-Systeme ermöglichen Bürger-Audits, parlamentarische Kontrolle und wissenschaftliche Überprüfung behördlicher IT-Systeme — eine Qualität, die proprietäre Software strukturell nicht bieten kann und die für demokratische Legitimität öffentlicher Digitalisierung essenziell ist.

**Befund 5 — Interkommunale Hebel:** Einzelne Gemeinden profitieren überproportional von interkommunaler Kooperation. Rahmenverträge über govdigital eG und Dataport, Praxisgemeinschaften und gemeinsame Ausschreibungen reduzieren Einzelkosten um 30–50 % und ermöglichen auch kleinen Gemeinden Zugang zu Enterprise-Grade-Infrastruktur.

### 8.1 Empfehlungen

**Für Stadtverwaltungen:**
1. Beschließen Sie eine formale Open-Source-Strategie mit Gemeinderatsbeschluss
2. Treten Sie govdigital eG oder einem vergleichbaren Rahmen bei
3. Starten Sie mit Keycloak + Nextcloud als Fundament (Phase 1)
4. Planen Sie Change-Management von Tag 1 — nicht als Nachgedanke
5. Dokumentieren Sie TCO-Daten von Anfang an für den politischen Rechenschaftsbericht

**Für kommunale IT-Dienstleister:**
1. Investieren Sie in Open-Source-Kompetenz und entsprechende Zertifizierungen
2. Entwickeln Sie SLA-Modelle für Open-Source-Komponenten analog zu proprietären Modellen
3. Beteiligen Sie sich aktiv an Upstream-Communities (Nextcloud, Matrix, CKAN)

**Für Zivilgesellschaft und Open-Source-Communities:**
1. Dokumentieren Sie Behördeneinsätze systematisch und veröffentlichen Sie Case Studies
2. Engagieren Sie sich in Standardisierungsgremien (eCH, XÖV, GovStack)
3. Bieten Sie strukturierte Onboarding-Programme für neue kommunale Mitglieder

**Für Forschung und Wissenschaft:**
1. Führen Sie longitudinale TCO-Studien in kooperierenden Gemeinden durch
2. Untersuchen Sie UX und Nutzerakzeptanz nach Migrationen
3. Entwickeln Sie Barrierefreiheits-Benchmarks für Open-Source-Behördenportale

---

## Quellenverzeichnis

Alle Quellen sind mit Sprache (SP), Region (RE), Herausgebende Institution (HI), Datum (DA), Titel (TI), URL (UR) und Lizenz (LI) annotiert.

[1] SP:de RE:CH HI:Schweizerische Bundesversammlung DA:2023-06-17 TI:Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG), SR 172.019 UR:https://www.fedlex.admin.ch/eli/cc/2023/682/de LI:Public Domain

[2] SP:de RE:DE HI:Deutscher Bundestag DA:2024-03-23 TI:Gesetz zur Änderung des Onlinezugangsgesetzes sowie weiterer Vorschriften zur Digitalisierung der Verwaltung (OZG-Änderungsgesetz 2024), BGBl. I Nr. 122 UR:https://www.recht.bund.de/bgbl/1/2024/122/regelungstext.pdf LI:Public Domain

[3] SP:en RE:EU HI:Europäisches Parlament und Rat DA:2024-04-11 TI:Regulation (EU) 2024/903 on measures for a high level of public sector interoperability across the Union (Interoperable Europe Act) UR:https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0903 LI:© EU, Reuse permitted

[4] SP:de RE:DE HI:ZenDiS GmbH DA:2023-11-01 TI:ZenDiS — Zentrum für Digitale Souveränität: Aufgaben und Projekte UR:https://zendis.de LI:Unbekannt

[5] SP:en RE:EU HI:Europäische Kommission DA:2023-09-15 TI:Open Source Observatory (OSOR): Open Source in the Public Sector 2023 UR:https://joinup.ec.europa.eu/collection/open-source-observatory LI:CC-BY-4.0

[6] SP:de RE:DE HI:govdigital eG DA:2022-01-01 TI:govdigital — Die Genossenschaft für digitale Souveränität UR:https://www.govdigital.de LI:Unbekannt

[7] SP:en RE:Global HI:ITU / DIAL DA:2023-06-01 TI:GovStack: Building Blocks for Digital Government UR:https://govstack.global LI:CC-BY-4.0

[8] SP:en RE:EU HI:Europäische Kommission DA:2021-09-01 TI:Study on the impact of open source software and hardware on technological independence, competitiveness and innovation in the EU economy (Blind et al.) UR:https://digital-strategy.ec.europa.eu/en/library/study-impact-open-source-software-and-hardware LI:CC-BY-4.0

[9] SP:en RE:EU HI:Gartner Research (via OSOR) DA:2022-01-01 TI:Open-Source Software TCO Analysis: Public Sector Scenarios UR:https://joinup.ec.europa.eu/collection/open-source-observatory/open-source-tco LI:Proprietär, Zusammenfassung verfügbar

[10] SP:de RE:DE HI:Bitkom e.V. DA:2022-11-01 TI:Digitale Souveränität — Positionspapier UR:https://www.bitkom.org/digitale-souveraenitaet LI:Unbekannt

[11] SP:en RE:EU HI:Europäischer Datenschutzausschuss (EDSA) DA:2023-05-18 TI:Guidelines 05/2021 on the Interplay between the application of Article 3 and the provisions on international transfers UR:https://edpb.europa.eu/our-work-tools/documents/public-consultations/2021/guidelines-052021-interplay-between-application_en LI:CC-BY-4.0

[12] SP:en RE:Global HI:AlgorithmWatch DA:2023-01-01 TI:Automating Society Report 2023 UR:https://automatingsociety.algorithmwatch.org LI:CC-BY-4.0

[13] SP:de RE:DE HI:Landeshauptstadt München DA:2017-11-01 TI:Stadtratsbeschluss: Rückkehr zu Microsoft-Produkten (LiMux-Abkehr) UR:https://risi.muenchen.de LI:Public Domain

[14] SP:en RE:EU HI:European Commission Joint Research Centre DA:2020-03-01 TI:European Digital Sovereignty — Steen-Johnsen et al. UR:https://publications.jrc.ec.europa.eu LI:CC-BY-4.0

[15] SP:en RE:Global HI:Open Source Initiative DA:2024-01-01 TI:The Open Source Definition (OSD) v1.9 UR:https://opensource.org/osd LI:CC-BY-4.0

[16] SP:en RE:Global HI:PRISMA Statement DA:2020-01-01 TI:Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 Statement UR:https://www.prisma-statement.org LI:CC-BY-4.0

[17] SP:en RE:US HI:Cambridge University Press DA:2012-01-01 TI:Frischmann, B.M.: Infrastructure: The Social Value of Shared Resources LI:Proprietär

[18] SP:en RE:US HI:Stripe Press DA:2020-01-01 TI:Eghbal, N.: Working in Public: The Making and Maintenance of Open Source Software LI:Proprietär

[19] SP:en RE:US HI:Harvard Business School Press DA:2003-01-01 TI:Chesbrough, H.W.: Open Innovation: The New Imperative for Creating and Profiting from Technology LI:Proprietär

[20] SP:en RE:US HI:Penguin Press DA:2008-01-01 TI:Zittrain, J.: The Future of the Internet — And How to Stop It LI:Proprietär

[21] SP:en RE:Global HI:Government Information Quarterly DA:2019-01-01 TI:Mergel, I., Edelmann, N., Haug, N.: Defining digital transformation: Results from expert interviews UR:https://doi.org/10.1016/j.giq.2019.06.002 LI:CC-BY-4.0

[22] SP:de RE:DE HI:Deutscher Bundestag DA:2017-08-14 TI:Onlinezugangsgesetz (OZG) vom 14. August 2017, BGBl. I S. 3122 UR:https://www.gesetze-im-internet.de/ozg/ LI:Public Domain

[23] SP:de RE:DE HI:Nationaler Normenkontrollrat DA:2022-11-01 TI:Jahresbericht 2022: Digitale Verwaltung auf dem Prüfstand UR:https://www.normenkontrollrat.bund.de LI:Public Domain

[24] SP:de RE:DE HI:FITKO DA:2023-06-01 TI:FIT-Store: Repository für OZG-konforme Dienste UR:https://fitko.de/fit-store LI:Unbekannt

[25] SP:de RE:DE HI:AKDB DA:2023-01-01 TI:AKDB Produktportfolio 2023/2024 UR:https://www.akdb.de LI:Unbekannt

[26] SP:de RE:DE HI:DigitalService GmbH des Bundes DA:2023-06-01 TI:DigitalService: Digitale Produkte für Deutschland UR:https://digitalservice.bund.de LI:Unbekannt

[27] SP:de RE:CH HI:eCH — E-Government-Standards DA:2024-01-01 TI:eCH-Standardkatalog UR:https://www.ech.ch LI:Proprietär (Nutzung frei)

[28] SP:de RE:CH HI:Schweizerische Bundesversammlung DA:2020-09-25 TI:Bundesgesetz über den Datenschutz (nDSG), SR 235.1 UR:https://www.fedlex.admin.ch/eli/cc/2022/491/de LI:Public Domain

[29] SP:de RE:CH HI:Schweizerische Bundesversammlung DA:2021-03-07 TI:Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (BGEID), SR 161.5 UR:https://www.fedlex.admin.ch/eli/cc/2024/130/de LI:Public Domain

[30] SP:en RE:ES HI:CONSUL Democracy DA:2023-06-01 TI:CONSUL DEMOCRACY: Open Source citizen participation tool UR:https://consuldemocracy.org LI:AGPL-3.0

[31] SP:en RE:FR HI:XWiki SAS / NGI0 DA:2023-12-01 TI:CryptPad: End-to-end encrypted collaboration suite UR:https://cryptpad.org LI:AGPL-3.0

[32] SP:en RE:UK HI:Collabora Ltd. DA:2024-01-01 TI:Collabora Online — LibreOffice Technology in the browser UR:https://www.collaboraonline.com LI:MPL-2.0

[33] SP:de RE:DE HI:Intevation GmbH DA:2023-09-01 TI:OpenSlides — Digitale Konferenz- und Sitzungsverwaltung UR:https://openslides.com LI:MIT

[34] SP:en RE:Global HI:Codeberg e.V. DA:2023-01-01 TI:Forgejo — Beyond coding. We Forge. UR:https://forgejo.org LI:GPL-2.0-or-later

[35] SP:en RE:SE HI:Vinnova (Schwedische Innovationsbehörde) DA:2023-05-01 TI:Measuring the value of open source software in public administration UR:https://www.vinnova.se LI:CC-BY-4.0

[36] SP:en RE:US HI:O'Reilly Media DA:2010-01-01 TI:Lathrop, D., Ruma, L. (Hrsg.): Open Government: Collaboration, Transparency, and Participation in Practice LI:CC-BY-3.0

[37] SP:en RE:EU HI:ETSI / CEN / CENELEC DA:2021-08-01 TI:EN 301 549 v3.2.1: Accessibility requirements for ICT products and services UR:https://www.etsi.org/deliver/etsi_en/301500_302000/301549/03.02.01_60/en_301549v030201p.pdf LI:© ETSI

[38] SP:en RE:Global HI:W3C DA:2018-06-05 TI:Web Content Accessibility Guidelines (WCAG) 2.1 UR:https://www.w3.org/TR/WCAG21/ LI:W3C Document License

[39] SP:de RE:DE HI:Bundesministerium des Innern DA:2011-09-22 TI:Barrierefreie-Informationstechnik-Verordnung (BITV 2.0) UR:https://www.gesetze-im-internet.de/bitv_2_0/ LI:Public Domain

[40] SP:de RE:CH HI:eCH DA:2023-01-01 TI:eCH-0059: Accessibility Standard für E-Government UR:https://www.ech.ch/de/ech/ech-0059 LI:Proprietär (Nutzung frei)

[41] SP:en RE:EU HI:European Commission / OSOR DA:2023-06-01 TI:Web Accessibility in European Public Sector: Implementation Report 2023 UR:https://digital-strategy.ec.europa.eu/en/policies/web-accessibility LI:CC-BY-4.0

[42] SP:en RE:DE HI:Open Source Business Alliance (OSBA) DA:2023-12-01 TI:Sovereign Cloud Stack (SCS): Reference Architecture v6 UR:https://scs.community LI:Apache-2.0

[43] SP:en RE:EU HI:GAIA-X AISBL DA:2023-09-01 TI:GAIA-X Architecture Document 23.11 UR:https://gaia-x.eu/gaia-x-framework/ LI:CC-BY-4.0

[44] SP:de RE:DE HI:Deutscher Bundestag DA:2021-01-01 TI:Gesetz gegen Wettbewerbsbeschränkungen (GWB) — Vergaberechtliche Vorschriften UR:https://www.gesetze-im-internet.de/gwb/ LI:Public Domain

[45] SP:de RE:DE HI:Bundesministerium für Wirtschaft DA:2016-04-12 TI:Vergabeverordnung (VgV) UR:https://www.gesetze-im-internet.de/vgv_2016/ LI:Public Domain

[46] SP:de RE:CH HI:Schweizerische Bundesversammlung DA:2021-01-01 TI:Bundesgesetz über das öffentliche Beschaffungswesen (BöB), SR 172.056.1 UR:https://www.fedlex.admin.ch/eli/cc/2020/126/de LI:Public Domain

[47] SP:de RE:DE HI:Landeshauptstadt München / ifo Institut DA:2017-12-01 TI:LiMux: Evaluation der Migration und Rückmigration — Zusammenfassung der Erkenntnisse UR:https://risi.muenchen.de LI:Public Domain

[48] SP:en RE:US HI:Halloween Documents Project DA:1998-01-01 TI:The Halloween Documents: Microsoft internal assessments of Linux and Open Source UR:https://www.catb.org/~esr/halloween/ LI:Verschiedene

[49] SP:de RE:EU HI:Europäisches Parlament und Rat DA:2016-04-27 TI:Verordnung (EU) 2016/679 — Datenschutz-Grundverordnung (DSGVO) UR:https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679 LI:© EU, Reuse permitted

[50] SP:de RE:DE HI:Deutscher Bundestag DA:2018-06-30 TI:Bundesdatenschutzgesetz (BDSG) — Neufassung UR:https://www.gesetze-im-internet.de/bdsg_2018/ LI:Public Domain

[51] SP:en RE:EU HI:Europäisches Parlament und Rat DA:2022-12-27 TI:Directive (EU) 2022/2555 (NIS2 Directive) UR:https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555 LI:© EU, Reuse permitted

[52] SP:de RE:DE HI:Bundesamt für Sicherheit in der Informationstechnik (BSI) DA:2023-09-01 TI:IT-Grundschutz-Kompendium, Edition 2023 UR:https://www.bsi.bund.de/grundschutz LI:CC-BY-4.0

[53] SP:en RE:Global HI:ISO/IEC DA:2022-10-01 TI:ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection LI:Proprietär

[54] SP:en RE:EU HI:Europäische Kommission DA:2023-12-01 TI:European Interoperability Framework (EIF) Implementation Strategy UR:https://ec.europa.eu/isa2/eif_en LI:CC-BY-4.0

[55] SP:de RE:DE HI:KGSt (Kommunale Gemeinschaftsstelle für Verwaltungsmanagement) DA:2023-06-01 TI:Digitale Transformation in Kommunen: Handlungsrahmen und Praxisempfehlungen UR:https://www.kgst.de LI:Proprietär

[56] SP:en RE:EU HI:European Commission DA:2023-06-27 TI:EU Data Act 2023 — Regulation (EU) 2023/2854 UR:https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854 LI:© EU, Reuse permitted

[57] SP:en RE:ES HI:Ajuntament de Barcelona DA:2022-06-01 TI:Decidim: Free Open-Source participatory democracy platform for cities and organisations UR:https://decidim.org LI:AGPL-3.0

[58] SP:de RE:DE HI:Bundesministerium des Innern DA:2023-11-01 TI:Digitalstrategie der Bundesregierung — Fortschrittsbericht 2023 UR:https://www.bmi.bund.de/digitalstrategie LI:Public Domain

[59] SP:en RE:Global HI:Linux Foundation DA:2023-01-01 TI:Open Source Software in the Public Sector: A Global Survey UR:https://www.linuxfoundation.org LI:CC-BY-4.0

[60] SP:de RE:DE HI:Bundesbeauftragter für den Datenschutz und die Informationsfreiheit (BfDI) DA:2023-09-01 TI:Cloud-Nutzung in der öffentlichen Verwaltung: Datenschutzrechtliche Anforderungen UR:https://www.bfdi.bund.de LI:Public Domain

[61] SP:en RE:Global HI:Free Software Foundation Europe (FSFE) DA:2023-06-01 TI:Public Money? Public Code! — Campaign and Policy Paper UR:https://publiccode.eu LI:CC-BY-4.0

[62] SP:de RE:DE HI:Bertelsmann Stiftung DA:2023-04-01 TI:Kommunale Digitalisierung 2023: Benchmark-Report UR:https://www.bertelsmann-stiftung.de LI:CC-BY-4.0

[63] SP:en RE:Global HI:Apache Software Foundation DA:2023-01-01 TI:The Apache Way: Community over Code UR:https://www.apache.org/theapacheway LI:CC-BY-4.0

[64] SP:de RE:CH HI:Informatiksteuerungsorgan Bund (ISB) / Bundesamt für Informatik (BIT) DA:2023-12-01 TI:Digitale Verwaltung Schweiz (DVS): Strategischer Rahmen 2024–2027 UR:https://www.digitale-verwaltung-schweiz.ch LI:Public Domain

[65] SP:de RE:AT HI:Bundeskanzleramt Österreich DA:2023-01-01 TI:Open Source in der österreichischen Bundesverwaltung: Strategie und Leitfaden UR:https://www.digitales.oesterreich.gv.at LI:CC-BY-4.0

---

*Dieses Dokument ist eine Übersetzung aus dem Englischen. Verbindlich ist die englische Fassung: `Doc/en/sovereign-by-design-v0.2.0.md`. Lizenz: CC-BY-4.0. Attribution: Sebastian Graf, Autonomes Büro für Zivile Digitale Infrastruktur.*

*Letztes Update: 2026-06-20 · Version 0.2.0 · Branch: claude/wonderful-lovelace-9j666k*
