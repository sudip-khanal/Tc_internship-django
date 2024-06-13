from django.contrib import admin

# Register your models here.
from school.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Assignment)