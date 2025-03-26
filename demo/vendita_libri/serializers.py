from rest_framework import serializers
from .models import Autore, Libro, Indirizzo, Utente

class AutoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autore
        fields = ['id', 'nome', 'cognome', 'data_nascita']

class LibroSerializer(serializers.ModelSerializer):
    autore = AutoreSerializer()  # Embedded author details

    class Meta:
        model = Libro
        fields = ['id', 'titolo', 'descrizione', 'prezzo', 'quantita', 'data_pubblicazione', 'autore', 'isbn']

class IndirizzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indirizzo
        fields = ['id', 'via', 'città', 'cap', 'provincia', 'stato', 'autore']

class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = ['id', 'username', 'email', 'indirizzo_email']
