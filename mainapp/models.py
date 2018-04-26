from django.db import models

# Create your models here.


# Headcaption tables start
class HeadCaption(models.Model):

    identification=models.CharField(max_length=10)
    maxtitle=models.CharField(max_length=50)
    mintitle=models.CharField(max_length=50)
    def __str__(self):
        return self.identification.encode('utf-8')

    class Meta:
        db_table='headcaption'

#Photolbum tables start
class PhotoLbum(models.Model):
    image=models.ImageField(upload_to='photolbum')
    imgorder=models.IntegerField()
    imgname=models.CharField(max_length=50)
    imgtitle=models.CharField(max_length=50)
    def __str__(self):
        return self.imgname.encode('utf-8')

    class Meta:
        db_table='photolbum'


#PhotoDescrib tables start
class PhotoDescrib(models.Model):
    image=models.ImageField(upload_to='photodescrib')
    imgorder=models.IntegerField()
    imgname=models.CharField(max_length=50)
    texttitle=models.CharField(max_length=50)
    textcontent=models.CharField(max_length=50)

    def __str__(self):
        return self.imgname.encode('utf-8')

    class Meta:
        db_table='photodescrib'