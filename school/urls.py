from django.urls import path
from school import views


urlpatterns = [
    path ('',views.get_student,name='views')

]