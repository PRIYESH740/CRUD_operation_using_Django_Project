from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator

# Create your models here.
class Student(models.Model):
    roll=models.CharField(max_length=10,validators=[MinLengthValidator(1),MaxLengthValidator(10)])
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=150,blank=True, null=True)
    phone=models.CharField(RegexValidator(regex=r'^\+?1?\d{9,15}$'),max_length=17,blank=True, null=True)

    def __str__(self):
        return self.name