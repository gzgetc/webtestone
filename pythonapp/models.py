from django.db import models

# Create your models here.


#create title tables
class PythonDirectTitle(models.Model):
    title=models.CharField(max_length=20)
    conut=models.IntegerField()
    def __str__(self):
        return self.title.encode('utf-8')
    class Meat:
        db_table='pythondirecttitle'

#create Table of Contents
class PythonDirectory(models.Model):
    pdtitle = models.ForeignKey(PythonDirectTitle)
    pdnumber=models.CharField(max_length=20)
    pdcontent=models.CharField(max_length=20)
    def __str__(self):
        return self.pdcontent.encode('utf-8')

#create Tutorial table
class PythonCourse(models.Model):
    directory=models.ForeignKey(PythonDirectory)
    content=models.TextField()
    pythoncode=models.TextField()
    time = models.DateTimeField()
    delete = models.BooleanField(default=False)
    class Meta:
        db_table='pythoncourse'
