from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

STATUS = (
    ("Privata", "Privata"),
    ("Pubblica", "Pubblica")
)

class TodoList(models.Model): #Todolist able name that inherits models.Model
    titolo = models.CharField(max_length=250) # a varchar
    autore = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    contenuto = models.TextField(blank=True) # a text field 
    creato = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    scade_il = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    orario = models.TimeField()
    tag = models.TextField(blank=True) # a foreignkey
    pubblica = models.TextField(choices=STATUS, default="Privata")

    class Meta:
        ordering = ["-creato"] #ordering by the created field
    def __str__(self):
        return self.titolo #name to be shown when called

    def get_absolute_url(self):
        return reverse('todo_dettaglio', args=[str(self.id)])    

class Comment(models.Model):
    todo = models.ForeignKey(TodoList,on_delete=models.CASCADE,related_name='comments')
    autore = models.CharField(max_length=80)
    testo = models.TextField()
    creato = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creato']

    def __str__(self):
        return 'Commento {} di {}'.format(self.testo, self.autore)
