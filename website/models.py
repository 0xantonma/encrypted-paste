from django.db import models


# Create your models here.
class Texts(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now=True)
    seen = models.IntegerField(default=0)
    view_id = models.CharField(max_length=20, unique=True, default=0)

    def __str__(self):
        return self.view_id
