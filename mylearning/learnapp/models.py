from django.db import models
import datetime


# Create your models here.

class ProfileModel(models.Model):
    profile_id = models.CharField(max_length=20, editable=False)
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        name = self.name
        date = datetime.date.today()
        self.profile_id = f"{name}{date}"
        super(ProfileModel, self).save(*args, **kwargs)
