from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    fever = models.FloatField()
    body_pain = models.IntegerField(help_text='0-No Pain, 1-Severe Pain')
    runny_nose = models.IntegerField(help_text='0-No, 1-Yes')
    diff_breath = models.IntegerField(help_text='-1-No Difficulty, 0-Medium Difficulty, 1-Severe Difficulty')

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'user' 
        indexes = [
            models.Index(fields=['id'])
        ]

class UserConsumption(models.Model):
    id = models.AutoField(primary_key=True)
    used_id = models.IntegerField()

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'user_consumption' 
        indexes = [
            models.Index(fields=['id'])
        ]
