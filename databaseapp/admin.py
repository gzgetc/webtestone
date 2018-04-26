from django.contrib import admin
from databaseapp.models import *
# Register your models here.

#DatabaseCourse Admin start
class DataCourseAdmin(admin.ModelAdmin):
    list_display = ['id','directory','content','datacode','dataimage','time']
    list_filter = ['directory']
    search_fields = ['directory']
    list_per_page = 10
    fieldsets = [
        ('title',{'fields':['directory']}),
        ('content',{'fields':['content']}),
        ('datacode',{'fields':['datacode','dataimage']}),
        ('footer',{'fields':['time']}),
    ]



admin.site.register(DataDirectTitle)
admin.site.register(DataDirectory)
admin.site.register(DataCourse,DataCourseAdmin)

