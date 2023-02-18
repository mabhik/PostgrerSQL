from django.db import models

# Create your models here.


class topic(models.Model):
    topic_name=models.CharField(max_length=40,primary_key=True)
    pages=models.IntegerField()

class webpage(models.Model):
    topic_name=models.ForeignKey(topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    url=models.URLField()

#sai database
class number(models.Model):
    fstnum=models.IntegerField(primary_key=True)
    lstnum=models.IntegerField()