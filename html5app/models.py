from django.db import models

# Create your models here.


#create title tables
class Html5DirectTitle(models.Model):
    title=models.CharField(max_length=20)
    conut=models.IntegerField()
    def __str__(self):
        return self.title.encode('utf-8')
    class Meta:
        db_table='html5directtitle'

#create Table of Contents
class Html5Directory(models.Model):
    hdtitle = models.ForeignKey(Html5DirectTitle)
    hdnumber=models.CharField(max_length=20)
    hdcontent=models.CharField(max_length=20)
    def __str__(self):
        return self.hdcontent.encode('utf-8')

    class Meta:
        db_table='html5directory'

#create Tutorial table
class Html5Course(models.Model):
    directory=models.ForeignKey(Html5Directory)
    content=models.TextField()
    html5code=models.TextField()
    html5image=models.ImageField(upload_to='html5course')
    time = models.DateTimeField()
    delete = models.BooleanField(default=False)
    class Meta:
        db_table='html5course'

