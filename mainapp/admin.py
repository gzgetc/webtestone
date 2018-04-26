from django.contrib import admin
from mainapp.models import *

# Register your models here.




#HeadCaption  Admin start
class HeadCaptionAdmin(admin.ModelAdmin):
    list_display = ['id','identification','maxtitle','mintitle']
    list_filter = ['identification']
    search_fields = ['identification']
    list_per_page = 30
    fieldsets = [
        ('Mark',{'fields':['identification']}),
        ('MaxFont',{'fields':['maxtitle']}),
        ('MinFont',{'fields':['mintitle']}),
    ]

#PhotoLbum Admin start

class PhotoLbumAdmin(admin.ModelAdmin):
    list_display = ['id','imgorder','imgname','image','imgtitle']
    list_filter = ['imgorder']
    search_fields = ['imgname']
    list_per_page = 4
    fieldsets = [
        ('info',{'fields':['imgorder','imgname']}),
        ('title',{'fields':['imgtitle']}),
        ('images',{'fields':['image']}),
    ]

#PhotoDescrib Admin start
class PhotoDescribAdmin(admin.ModelAdmin):
    list_display = ['id','imgorder','imgname','image','texttitle','textcontent']
    list_filter = ['imgorder']
    search_fields = ['imgname']
    list_per_page = 50
    fieldsets = [
        ('info',{'fields':['imgorder','imgname']}),
        ('images',{'fields':['image']}),
        ('text',{'fields':['texttitle','textcontent']}),
    ]

admin.site.register(HeadCaption,HeadCaptionAdmin)
admin.site.register(PhotoLbum,PhotoLbumAdmin)
admin.site.register(PhotoDescrib,PhotoDescribAdmin)



#
