from django.urls import path,include
from account import views
urlpatterns = [
    path ('',views.get_article,name='get_article'),
    # path ('create_reporter/',views.create_reporter,name='create_reporter'),
    # path ('create_article/',views.create_article,name='create_article'),
    # path('<pk>/delete_article', views.delete_article,name='delete_article' ),
    # path('<pk>/update_article',views.update_article,name='update_article')

    # path ('add_article',views.add_article,name='add_article'),
    # path ('',views.all_article,name='all_article')




]