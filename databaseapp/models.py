from django.db import models

# Create your models here.


#create title tables
class DataDirectTitle(models.Model):
    title=models.CharField(max_length=20)
    conut=models.IntegerField()
    def __str__(self):
        return self.title.encode('utf-8')
    class Meat:
        db_table='datadirecttitle'

#create Table of Contents
class DataDirectory(models.Model):
    ddtitle = models.ForeignKey(DataDirectTitle)
    ddnumber=models.CharField(max_length=20)
    ddcontent=models.CharField(max_length=20)
    def __str__(self):
        return self.ddcontent.encode('utf-8')

#create Tutorial table
class DataCourse(models.Model):
    directory=models.ForeignKey(DataDirectory)
    content=models.TextField()
    datacode=models.TextField()
    dataimage=models.ImageField(upload_to='datacourse')
    time = models.DateTimeField()
    delete = models.BooleanField(default=False)
    class Meta:
        db_table='datacourse'

