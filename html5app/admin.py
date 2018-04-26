from django.contrib import admin
from html5app.models import *
# Register your models here.

#Html5Course Admin start
class Html5CourseAdmin(admin.ModelAdmin):
    list_display = ['id','directory','content','html5code','html5image','time']
    list_filter = ['directory']
    search_fields = ['directory']
    list_per_page = 10
    fieldsets = [
        ('title',{'fields':['directory']}),
        ('content',{'fields':['content']}),
        ('codeing',{'fields':['html5code','html5image']}),
        ('footer',{'fields':['time']}),
    ]



admin.site.register(Html5DirectTitle)
admin.site.register(Html5Directory)
admin.site.register(Html5Course,Html5CourseAdmin)

