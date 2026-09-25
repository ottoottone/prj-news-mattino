# Germania, in breve

Sito Jekyll in italiano per il briefing mattutino sulla Germania.

## Stato

La prima implementazione usa il tema open-source [Nord Newsletter](https://github.com/systemhalted/jekyll-theme-nord-newsletter) come base locale e aggiunge un livello editoriale italiano dedicato al progetto.

## Sviluppo locale

```sh
bundle install
bundle exec jekyll serve --livereload
```

Apri `http://127.0.0.1:4000`.

## Struttura editoriale

- `collections/_newsletter/` contiene le edizioni quotidiane.
- `_data/taxonomy.yml` definisce i temi.
- `assets/css/briefing.css` contiene l’identità visiva del briefing.
- `notes/implementation-queue.md` registra le 25 migliorie e il loro stato.
