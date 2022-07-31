from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to='Media/course-image',null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title

class Teacher(models.Model):
    image = models.ImageField(upload_to='Media/teacher-image',null=True,blank=True)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name

#salom
# class Application(models.Model):
#     client_name = models.CharField(max_length=50)
#     client_lastname = models.CharField(max_length=50)
#     client_phone_number = models.CharField(max_length=50)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
#     def __str__(self) -> str:
#         return self.client_name

class Application(models.Model):
    client_name = models.CharField(max_length=100,verbose_name='Ismingizni kiriting')
    client_last_name = models.CharField(max_length=100,verbose_name='Familyangizni kiriting')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='Kursni tanlang:')
    client_phone_number = models.CharField(max_length=50,verbose_name='Telefon raqamingizni kiriting:')

    def __str__(self):
        return f'{self.client_name} - {self.client_last_name} - {self.client_phone_number} - {self.course} '
    

