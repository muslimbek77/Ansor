from django.contrib import admin
from blog.models import Course, Teacher, Application
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'course', 'client_phone_number']
    

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Application, ApplicationAdmin)
