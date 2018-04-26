from django.contrib import admin
from pythonapp.models import *
# Register your models here.




#PythonCourse Admin start
class PythonCourseAdmin(admin.ModelAdmin):
    list_display = ['id','directory','content','pythoncode','time']
    list_filter = ['directory']
    search_fields = ['directory']
    list_per_page = 10
    fieldsets = [
        ('title',{'fields':['directory']}),
        ('content',{'fields':['content']}),
        ('pythoncode',{'fields':['pythoncode']}),
        ('footer',{'fields':['time']}),
    ]



admin.site.register(PythonDirectTitle)
admin.site.register(PythonDirectory)
admin.site.register(PythonCourse,PythonCourseAdmin)
