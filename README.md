# esercitazione Wheretech

## Descrizione:

API Rest in Django per colloquio tecnico con Wheretech con utilizzo della libreria Rest-Framework.

diagramma:
## Requisiti:
- Python: Versione 3.11.9 e oltre.
- Pip: 25.0 e oltre.

## Installazione del Virtual Enviroment:

È consigliato l'utilizzo di un Virtual Enviroment per evitare conflitti con i pacchetti e librerie installati globalmente.

Eseguire i seguenti comandi da terminale dopo essersi posizionati nella caretella root della repository:

Generazione virtual enviroment nella cartella root sotto la cartella **venv**:

    python3 -m venv .venv

Attivare il Virtual Enviroment:

- per **Linux** e **MacOs**:

        source .venv/bin/activate

- per **Windows**:
    - in **Cmd**:

           venv\Scripts\activate.bat
    - in **PowerShell**:

               venv\Scripts\Activate.ps1

**N.B.** Per disattivare il Virtual Enviroment al termine delle operazioni, usare il comando:

    deactivate

## Installazione del Virtual Enviroment:
per installare le dipendenze richieste dalla WebApi rimanere nella cartella root ed eseguire i seguenti comandi:

- Aggiornare Pip:

        pip install -U pip

- Installare le dipendenze presenti nel file **requirements.txt**:

        pip install -r ./requirements.txt

## Avviare la WebApi:
Una volta aver attivato il Virtual Enviroment, recarsi da terminale nella cartella **esercitazionenephila** ed eseguire i seguenti comandi:

generazione del **DB** SQLite e prima migration:

    python3 manage.py migrate

avvio dell' applicazione:

    python3 manage.py runserver
