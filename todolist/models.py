from django.db import models
from django.utils import timezone

class Tasks(models.Model):

    name = models.CharField(max_length=200)
    pub_date = models.DateField("Date Published")
    must_finish_by = models.DateField("Date to be finished")


    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        super().save(*args, **kwargs)


# Create your models here.
