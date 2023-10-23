from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.blogs, name='blogs'),
    path('new/', views.new, name='new'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/delete_confirm/', views.delete_confirm, name='delete_confirm'),
    path('access_denied/', views.access_denied, name='access_denied'),
]
#You should update the above paths If you want to try out the class based views