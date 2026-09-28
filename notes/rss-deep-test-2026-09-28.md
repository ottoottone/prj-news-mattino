# Audit profondo RSS/Atom — 28 settembre 2026

## Risultato operativo

Il test conferma che il flusso RSS può aumentare la copertura, ma non tutte le testate della whitelist espongono un feed utilizzabile nello stesso modo. Il cronjob deve quindi usare RSS/Atom come primo percorso, registrare il risultato per ogni fonte e passare alla pagina dell'articolo solo come fallback dichiarato.

## Feed verificati

| Fonte | Feed ufficiale testato | Esito | Nota |
|---|---|---|---|
| Deutsche Welle | `https://rss.dw.com/atom/rss-de-all` oppure `https://rss.dw.com/rdf/rss-de-all` | disponibile | Il feed RDF usa namespace RSS 1.0; non cercare solo elementi RSS 2.0 `item`. |
| DER SPIEGEL | `https://www.spiegel.de/schlagzeilen/eilmeldungen/index.rss` | disponibile | Feed RSS valido; il primo tentativo con parser limitato agli elementi senza namespace può restituire zero elementi: usare un parser RSS completo. |
| Tagesschau | `https://www.tagesschau.de/xml/rss2` | disponibile | 40 elementi rilevati nel test. |
| Deutschlandfunk | `https://www.deutschlandfunk.de/nachrichten-100.rss` | disponibile | 35 elementi rilevati nel test; la pagina RSS ufficiale indica anche `politikportal-100.rss`. |
| FAZ | `https://www.faz.net/rss/aktuell` | disponibile | 159 elementi rilevati nel test; verificare sempre che il link sia all'articolo preciso. |
| Handelsblatt | `https://www.handelsblatt.com/contentexport/feed/politik` | disponibile | 20 elementi rilevati nel test; la pagina ufficiale dei feed segnala limitazioni d'uso commerciale. |
| Süddeutsche Zeitung | `https://rss.sueddeutsche.de/rss/Alles` e `https://rss.sueddeutsche.de/rss/Politik` | disponibile | 15 elementi rilevati nel test; la pagina ufficiale conferma che i link devono puntare agli articoli SZ. |
| POLITICO Europe | `https://www.politico.eu/feed/` | disponibile con accesso variabile | Il feed ha risposto 200 con un client HTTP che dichiarava un browser, ma 403 con il client Python predefinito. Non cambiare user-agent per eludere il blocco: trattare il feed come accesso condizionato e usare solo strumenti compatibili e leciti, poi fallback all'articolo esatto. |
| Reuters | feed pubblico non confermato | non disponibile nel test | Il vecchio endpoint `feeds.reuters.com` non risolve. Non sostituire Reuters con aggregatori o fonti esterne; cercare l'eventuale feed ufficiale corrente durante ogni esecuzione e, se assente, usare l'articolo Reuters esatto solo se reperibile lecitamente. |
| DIE ZEIT | `https://newsfeed.zeit.de/index` | disponibile | Risponde 200 con `application/rss+xml`; il vecchio tentativo sulla homepage ha restituito 403. Usare questo feed ufficiale per i candidati, poi verificare l'articolo preciso. |
| Governo federale tedesco | `https://www.bundesregierung.de/service/opendata/breg-de/pressemitteilungen-1584990.xml` | disponibile | Il vecchio percorso `/breg-de/service/rss-feeds` restituisce 404; il sito espone una nuova pagina RSS e feed XML per le comunicazioni. Verificare anche ministero/autorità direttamente pertinenti. |

## User-agent rilevato

- Browser reale della sessione: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/153.0.0.0 Safari/537.36`.
- Fetch HTTP Python predefinito: `Python-urllib`.
- Non è stato usato un user-agent falso per aggirare paywall, CAPTCHA, robots.txt o blocchi. Un 403 deve essere registrato come accesso condizionato/inaccessibile, non aggirato.

## Correzioni richieste al processo

1. Per ogni fonte, provare prima il feed ufficiale e i feed tematici ufficiali.
2. Supportare RSS 0.9/1.0, RSS 2.0, RDF e Atom; non contare gli elementi con un solo XPath.
3. Validare titolo, URL canonico, data di pubblicazione/aggiornamento e descrizione di ogni item.
4. Filtrare gli item nelle 36 ore, deduplicare per URL canonico e raggruppare per evento.
5. Controllare anche le prime notizie/front page della fonte quando il feed tematico non è sufficiente.
6. Se il feed è vuoto, obsoleto, incompleto o bloccato, documentare lo stato e usare la pagina web solo come fallback.
7. Non usare feed di aggregatori, RSS proxy o fonti fuori whitelist.
8. Non presentare un feed disponibile come prova che l'articolo completo sia accessibile: il link finale deve restare l'articolo preciso.

## Limite del test

Questo audit verifica endpoint e comportamento di accesso, non certifica che ogni item rilevato sia pertinente alla Germania o alla finestra editoriale del briefing. Il cronjob deve fare quel filtraggio in tempo reale e deve preferire più notizie realmente pertinenti, non riempire l'edizione con item generici o duplicati.
