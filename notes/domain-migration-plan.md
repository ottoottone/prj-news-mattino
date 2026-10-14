# Piano di migrazione — `un minuto`

**Decisione di brand:** `un minuto`  
**Sottotitolo editoriale:** *Germania, in breve.*

## Obiettivo

Passare dall'URL tecnico `https://ottoottone.github.io/prj-news-mattino/` al dominio canonico `https://unminuto.news/`, mantenendo il sito statico su GitHub Pages e senza cambiare la cadenza o l'archivio editoriale.

## Stato di partenza — 14 ottobre 2026

- Repository pubblico: `ottoottone/prj-news-mattino`, branch `master`.
- GitHub Pages è pubblicato via workflow e raggiungibile in HTTPS all'URL tecnico (HTTP 200).
- Non è configurato alcun dominio personalizzato (`cname: null`).
- Non è configurato Google Analytics nel sito (`google_analytics_id` assente).
- Metriche GitHub del repository: 0 stelle, 0 fork, 0 issue aperte. Non sono metriche di lettura del sito.
- Il modulo newsletter esistente usa Kit: i risultati di iscrizione restano misurabili nel dashboard Kit.

## Dominio: decisione e verifica

### Prima scelta

`unminuto.news` è il candidato da trattare come dominio principale: è breve, corrisponde esattamente al nome e comunica una testata/briefing. La lingua e il focus sono chiariti dal sottotitolo, non dal dominio.

La verifica presso l'endpoint RDAP ufficiale del registry `.news` (`rdap.identitydigital.services`) ha restituito `404 Object not found` il 14 ottobre 2026: `unminuto.news` risulta **non registrato al momento del controllo**. Il DNS non restituisce record A. Non è comunque una prenotazione: va acquistato nel carrello di un registrar prima di qualsiasi annuncio o modifica tecnica.

### Alternative da verificare solo se la prima scelta non è acquistabile

1. `unminuto.eu` — coerente con lettori italiani in Germania e con il perimetro europeo.
2. `unminuto.de` — il RDAP DENIC ha restituito `404` (nessun dominio trovato) il 14 ottobre 2026; è un segnale preliminare, non una conferma del registrar.
3. `unminuto.it` — RDAP pubblico ha restituito `404` il 14 ottobre 2026; stessa cautela.

Non scegliere un'estensione o acquistare varianti difensive senza controllare prima: disponibilità live, prezzo di rinnovo, trasferibilità, rinnovi automatici, marchi/nome commerciale e omonimie. Esiste già il prodotto ispanofono “En Un Minuto”; prima del lancio serve una rapida verifica legale e di posizionamento, soprattutto per marchi e handle social.

## Architettura proposta

- **Registrar/DNS:** un registrar con DNS affidabile e accesso completo ai record; Cloudflare è una scelta adatta se il TLD è supportato e il prezzo di rinnovo è accettato.
- **Hosting:** invariato, GitHub Pages con workflow esistente.
- **Canonico:** `https://unminuto.news/`; `www.unminuto.news` deve reindirizzare al dominio nudo o viceversa. La scelta consigliata è il dominio nudo per avere URL editoriali più corti.
- **DNS:** record `A` e `AAAA` richiesti da GitHub Pages per l'apice, più `CNAME` di `www` verso `ottoottone.github.io`; inserire i valori esatti indicati da GitHub al momento della configurazione, non valori copiati da guide datate.
- **Sicurezza:** abilitare HTTPS enforcement in GitHub Pages, poi verificare certificato, URL canonici, feed RSS, sitemap e tutti i link con il nuovo `url` e `baseurl: ""`.
- **URL storico:** GitHub Pages non permette di governare header 301 per il dominio `github.io`. Il vecchio URL tecnico può restare accessibile; il sito dovrà dichiarare il nuovo URL come canonico e aggiornare i link pubblici. Non promettere un redirect 301 dal sottodominio GitHub senza un host che si controlli.

## Piano operativo

### 1. Prima dell'acquisto

- Confermare `unminuto.news` al checkout presso il registrar scelto e documentare costo iniziale, costo di rinnovo e intestatario.
- Verificare in modo proporzionato marchi, ragione sociale e handle `unminuto` su Signal, Instagram, X, LinkedIn e YouTube.
- Decidere chi possiede account registrar, GitHub, Kit e analytics; attivare 2FA e registrare un contatto di recupero.

### 2. Preparazione tecnica in repository

- Impostare in `_config.yml` `url: https://unminuto.news` e `baseurl: ""` in un commit dedicato; rimuovere nello stesso commit il `--baseurl "/${{ github.event.repository.name }}"` dal workflow Pages, che altrimenti sovrascrive la configurazione di produzione.
- Aggiungere un file `CNAME` con `unminuto.news` dopo aver confermato il dominio.
- Ricostruire il sito e controllare canonical, Open Graph, JSON-LD, feed, sitemap, manifest e link relativi sull'URL di radice.
- Preparare una pagina privacy e una pagina contatti/colophon prima di attivare strumenti di misurazione.

### 3. Attivazione DNS e GitHub Pages

- Aggiungere il dominio in GitHub Pages e completare la verifica DNS con i valori mostrati dall'interfaccia GitHub.
- Pubblicare il commit, attendere la validazione del certificato, attivare HTTPS enforcement.
- Verificare in un browser: homepage, un'edizione, archivio, feed RSS, sitemap, manifest, form Kit e URL senza/col `www`.
- Controllare HTTP 200 e canonical `https://unminuto.news/...` per homepage e almeno tre pagine archiviate.

### 4. Comunicazione e consolidamento

- Sostituire il vecchio URL in profili, firma, feed, Kit e materiali sociali.
- Inviare una sola comunicazione agli iscritti: nuovo indirizzo, nessun cambio al contenuto o alla frequenza, link diretto al feed aggiornato.
- Inviare nuova sitemap a Google Search Console e Bing Webmaster Tools e monitorare indicizzazione/canonical per 30 giorni.

## Statistiche: configurazione consigliata

Usare tre fonti separate, ciascuna per il proprio compito:

1. **Plausible Analytics** (cloud o self-hosted): analytics web essenziali, senza cookie per la configurazione standard; dashboard con visitatori, fonti, pagine e paesi. È la scelta consigliata per un progetto editoriale sobrio. Prima dell'attivazione, confermare piano/costo e pubblicare l'informativa privacy.
2. **Google Search Console + Bing Webmaster Tools:** query di ricerca, impression, click, pagine indicizzate e problemi tecnici. Configurare una proprietà di dominio tramite record DNS, così copre `www` e non-`www`.
3. **Kit:** iscrizioni, aperture/click delle email e disiscrizioni. È la fonte autorevole per la crescita newsletter, non il contatore web.

Eventi minimi, senza profilazione superflua:

- visita e pagina di arrivo;
- provenienza (ricerca, diretto, social, referral);
- click verso iscrizione newsletter;
- click RSS;
- click alle fonti esterne, solo se utile alle decisioni editoriali.

Non usare una metrica unica chiamata “lettori”: riportare separatamente visitatori unici web, iscritti netti newsletter e traffico RSS, con periodo e fonte espliciti.

## Dashboard mensile

Preparare una nota mensile con:

- visitatori web e loro variazione mensile;
- top 10 pagine e fonti di acquisizione;
- query Search Console, impression, click e CTR;
- iscritti Kit: nuovi, disiscritti, totale netto, open rate e click rate;
- salute tecnica: pagine indicizzate, errori, Core Web Vitals se disponibili;
- decisione concreta per il mese successivo (tema, distribuzione o UX), non una lista di vanity metrics.

## Criteri di completamento

La migrazione è conclusa solo quando il dominio risponde in HTTPS, `www` converge al canonico, i canonical/feed/sitemap usano `unminuto.news`, il form newsletter funziona, le proprietà di ricerca sono verificate e il dashboard analytics registra dati reali per almeno sette giorni.
