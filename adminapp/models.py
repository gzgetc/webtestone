from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(User):
    signature=models.CharField(max_length=128, default='This guy is too lazy to levave anything here.')
    phone=models.CharField(max_length=11)
    portrait=models.ImageField(upload_to='userinfo',default='userinfo/initial.jpg.jpg')

    def __unicode__(self):
        return self.username

    class Meta:
        db_table='userinfo'

