import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from vendita_libri.models import Autore, Libro, Indirizzo, Utente

fake = Faker()

class Command(BaseCommand):
    help = 'Genera 1000 dati fittizi per gli autori, libri, indirizzi e utenti'

    def handle(self, *args, **kwargs):
        # Creare 1000 autori unici
        autori = []
        for _ in range(1000):  # 1000 autori
            nome = fake.first_name()
            cognome = fake.last_name()
            data_nascita = fake.date_of_birth(minimum_age=18, maximum_age=80)

            # Aggiungere autore
            autore = Autore.objects.create(
                nome=nome,
                cognome=cognome,
                data_nascita=data_nascita
            )
            autori.append(autore)

        # Creare 1000 libri unici
        for _ in range(1000):  # 1000 libri
            titolo = fake.sentence(nb_words=5)
            descrizione = fake.text(max_nb_chars=200)
            prezzo = round(random.uniform(5, 50), 2)
            quantita = random.randint(1, 100)
            data_pubblicazione = fake.date_this_decade()
            autore = random.choice(autori)
            isbn = fake.unique.isbn13()  # ISBN unici

            Libro.objects.create(
                titolo=titolo,
                descrizione=descrizione,
                prezzo=prezzo,
                quantita=quantita,
                data_pubblicazione=data_pubblicazione,
                autore=autore,
                isbn=isbn
            )

        # Creare 1000 indirizzi unici
        for autore in autori:
            via = fake.street_address()
            città = fake.city()
            cap = fake.zipcode()
            provincia = fake.state()
            stato = fake.country()
            nazionalita = fake.country()

            Indirizzo.objects.create(
                via=via,
                città=città,
                cap=cap,
                provincia=provincia,
                stato=stato,
                nazionalita=nazionalita,
                autore=autore
            )

        # Creare 1000 utenti unici
        for _ in range(1000):  # 1000 utenti
            username = fake.user_name()
            email = fake.unique.email()  # Email uniche
            password = fake.password()

            try:
                Utente.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
            except IntegrityError:
                # Se c'è un errore di integrità (come l'email già esistente), lo ignoriamo e procediamo
                self.stdout.write(self.style.WARNING(f'Utente con email {email} già esistente, ignorato.'))

        self.stdout.write(self.style.SUCCESS('1000 dati fittizi generati con successo per ogni tabella!'))
