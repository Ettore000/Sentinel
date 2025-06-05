# Sentinel

Un semplice bot Telegram scritto in Python.

## Requisiti

- Python 3.8+
- La libreria `python-telegram-bot`

## Configurazione

Impostare la variabile d'ambiente `TELEGRAM_TOKEN` con il token fornito da BotFather.

```bash
export TELEGRAM_TOKEN=il_tuo_token
```

## Avvio

Eseguire il file principale:

```bash
python3 sentinel.py
```

## Struttura del progetto

- `sentinel.py` – punto di ingresso dell'applicazione
- `util/` – funzioni di utilità
- `handlers/` – un file per ogni comando utilizzabile su Telegram

## Comandi principali

- `/start` registra l'utente
- `/aggiungi <minuti>` aggiunge minuti al contatore
- `/status` mostra il tempo accumulato
- `/attuale` mostra l'attività corrente
- `/ferma` mette in pausa i reminder
- `/riprendi` riattiva i reminder
- `/annulla` annulla l'ultima aggiunta
- `/piano` mostra il piano attivo
- `/set_piano <nome>` cambia piano
- `/test_giornaliero` e `/test_settimanale` generano i grafici (placeholder)
