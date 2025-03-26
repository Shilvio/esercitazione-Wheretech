from django.db import models
from django.contrib.auth.models import AbstractUser


class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.cognome}'

class Libro(models.Model):
    titolo = models.CharField(max_length=255)
    descrizione = models.TextField(null=True, blank=True)
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    quantita = models.PositiveIntegerField(default=0)
    data_pubblicazione = models.DateField()
    autore = models.ForeignKey(Autore, related_name='libri', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titolo

class Indirizzo(models.Model):
    via = models.CharField(max_length=255)
    città = models.CharField(max_length=100)
    cap = models.CharField(max_length=10)
    provincia = models.CharField(max_length=100)
    stato = models.CharField(max_length=100)
    nazionalita = models.CharField(max_length=100, null=True, blank=True) 
    autore = models.OneToOneField('Autore', related_name='indirizzo', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.via}, {self.città}, {self.stato}'

class Utente(AbstractUser):
    indirizzo_email = models.EmailField(unique=True)

    # Aggiungi related_name personalizzati per evitare conflitti
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utente_set',  # Usa un nome personalizzato per il reverse accessor
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utente_set',  # Usa un nome personalizzato per il reverse accessor
        blank=True
    )

    def __str__(self):
        return self.username
