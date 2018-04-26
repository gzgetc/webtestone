from django.db import models

# Create your models here.


#create title tables
class LinuxDirectTitle(models.Model):
    title=models.CharField(max_length=20)
    conut=models.IntegerField()
    def __str__(self):
        return self.title.encode('utf-8')
    class Meat:
        db_table='linuxdirecttitle'

#create Table of Contents
class LinuxDirectory(models.Model):
    ldtitle = models.ForeignKey(LinuxDirectTitle)
    ldnumber=models.CharField(max_length=20)
    ldcontent=models.CharField(max_length=20)
    def __str__(self):
        return self.ldcontent.encode('utf-8')

#create Tutorial table
class LinuxCourse(models.Model):
    directory=models.ForeignKey(LinuxDirectory)
    content=models.TextField()
    linuxcode=models.TextField()
    time = models.DateTimeField()
    delete = models.BooleanField(default=False)
    class Meta:
        db_table='linuxcourse'
