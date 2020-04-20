from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^login/', views.user_login,name='user_login'),
    url(r'^dashboard/', views.dashboard,name='dashboard'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^signup/', views.authentication_view, name='signup'),
    url(r'^book/', views.book, name='book'),
    url(r'^mybookings/', views.mybookings, name='mybookings'),
    url(r'^allbookings_admin/', views.allbookings_admin, name='allbookings_admin'),
    url(r'^currentbookings_admin/', views.currentbookings_admin, name='currentbookings_admin'),

]
