from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey(Author,related_name='book', on_delete=models.CASCADE)
    isbn_number=models.IntegerField()
    pages=models.IntegerField()
    pub_date=models.DateField()

    def __str__(self):
        return self.name


genders= [
        ('', 'Select  Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

class Student(models.Model):
   full_name=models.CharField(max_length=200)
   roll_no=models.IntegerField()
   gender=models.CharField(max_length=20,choices=genders)
   grade= models.CharField(max_length=1, blank=True, null=True)
    
   def __str__(self):
        return self.full_name


class Teacher(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=150)
    student=models.ManyToManyField(Student,related_name='course')
    teacher=models.ManyToManyField(Teacher,related_name='course',through='Assignment', through_fields=('course', 'teacher'))

    def __str__(self):
        return self.name

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    class Meta:
        unique_together = ('course', 'teacher')
