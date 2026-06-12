from django.db import models

# Create your models here.

class Theater(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    theater=models.ForeignKey(Theater,on_delete=models.CASCADE,related_name='th')

    def __str__(self):
        return self.name

# theater expensive move ullath

# ooro theater ethra movies count



