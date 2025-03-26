import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError
from vendita_libri.models import Autore, Libro, Indirizzo, Utente

class Command(BaseCommand):
    help = 'Genera dati fittizi per autori, libri, indirizzi e utenti'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker('it_IT')  # Specifico italiano per dati più realistici
        self.num_records = 1000

    def handle(self, *args, **kwargs):
        try:
            # Separate method to create all authors first
            authors = self.create_authors()
            self.create_books(authors)
            self.create_addresses(authors)
            self.create_users()
            
            self.stdout.write(self.style.SUCCESS(f'{self.num_records} dati fittizi generati con successo per ogni tabella!'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Errore durante la generazione dei dati: {e}'))

    def create_authors(self):
        """Genera autori unici"""
        authors = []
        for _ in range(self.num_records):
            author = Autore.objects.create(
                nome=self.fake.first_name(),
                cognome=self.fake.last_name(),
                data_nascita=self.fake.date_of_birth(minimum_age=18, maximum_age=80)
            )
            authors.append(author)
        return authors

    def create_books(self, authors):
        """Genera libri unici"""
        for _ in range(self.num_records):
            Libro.objects.create(
                titolo=self.fake.catch_phrase(),
                descrizione=self.fake.paragraph(nb_sentences=3),
                prezzo=round(random.uniform(5, 50), 2),
                quantita=random.randint(1, 100),
                data_pubblicazione=self.fake.date_this_decade(),
                autore=random.choice(authors),
                isbn=self.fake.unique.isbn13()
            )

    def create_addresses(self, authors):
        """Genera indirizzi per autori"""
        for author in authors:
            Indirizzo.objects.create(
                via=self.fake.street_address(),
                città=self.fake.city(),
                cap=self.fake.postcode(),
                provincia=self.fake.administrative_unit(),
                stato=self.fake.country(),
                nazionalita=self.fake.country(),
                autore=author
            )

    def create_users(self):
        """Genera utenti unici con gestione degli errori"""
        created_users = 0
        attempts = 0
        max_attempts = self.num_records * 2

        while created_users < self.num_records and attempts < max_attempts:
            try:
                username = self.fake.user_name()
                email = self.fake.unique.email()
                password = self.fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

                Utente.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                created_users += 1

            except IntegrityError:
                self.stdout.write(self.style.WARNING(f'Utente con email o username duplicato, riprovo.'))

            attempts += 1

        if created_users < self.num_records:
            self.stdout.write(self.style.WARNING(f'Generati solo {created_users} utenti invece di {self.num_records}'))