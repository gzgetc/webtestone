from django.db import models

# Create your models here.


#create title tables
class JavaDirectTitle(models.Model):
    title=models.CharField(max_length=20)
    conut=models.IntegerField()
    def __str__(self):
        return self.title.encode('utf-8')
    class Meat:
        db_table='javadirecttitle'

#create Table of Contents
class JavaDirectory(models.Model):
    jdtitle = models.ForeignKey(JavaDirectTitle)
    jdnumber=models.CharField(max_length=20)
    jdcontent=models.CharField(max_length=20)
    def __str__(self):
        return self.jdcontent.encode('utf-8')

#create Tutorial table
class JavaCourse(models.Model):
    directory=models.ForeignKey(JavaDirectory)
    content=models.TextField()
    javacode=models.TextField()
    time = models.DateTimeField()
    delete = models.BooleanField(default=False)
    class Meta:
        db_table='javacourse'
