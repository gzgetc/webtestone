from django.contrib import admin
from linuxapp.models import *
# Register your models here.




#LinuxCourse Admin start
class LinuxCourseAdmin(admin.ModelAdmin):
    list_display = ['id','directory','content','linuxcode','time']
    list_filter = ['directory']
    search_fields = ['directory']
    list_per_page = 10
    fieldsets = [
        ('title',{'fields':['directory']}),
        ('content',{'fields':['content']}),
        ('linuxcode',{'fields':['linuxcode']}),
        ('footer',{'fields':['time']}),
    ]



admin.site.register(LinuxDirectTitle)
admin.site.register(LinuxDirectory)
admin.site.register(LinuxCourse,LinuxCourseAdmin)
