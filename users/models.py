from django.contrib.auth.models import AbstractUser
from django.db import models

SESSO = (
    ("Maschio", "Maschio"),
    ("Femmina", "Femmina"),
    ("Nessuno", "Nessuno")
)


class CustomUser(AbstractUser):
    anni = models.PositiveIntegerField(default=18)
    immagine = models.ImageField(default='default.png')
    cover = models.ImageField(upload_to='bg_pic/', default='background.jpg')
    sesso = models.TextField(choices=SESSO, default="Nessuno")
    descrizione = models.CharField(max_length=4000, default="La tua fantastica descrizione")
