from django.db import models

from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.PROTECT)
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    content = models.TextField("Content")

