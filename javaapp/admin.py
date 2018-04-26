from django.contrib import admin
from javaapp.models import *
# Register your models here.




#JavaCourse Admin start
class JavaCourseAdmin(admin.ModelAdmin):
    list_display = ['id','directory','content','javacode','time']
    list_filter = ['directory']
    search_fields = ['directory']
    list_per_page = 10
    fieldsets = [
        ('title',{'fields':['directory']}),
        ('content',{'fields':['content']}),
        ('javacode',{'fields':['javacode']}),
        ('footer',{'fields':['time']}),
    ]



admin.site.register(JavaDirectTitle)
admin.site.register(JavaDirectory)
admin.site.register(JavaCourse,JavaCourseAdmin)
