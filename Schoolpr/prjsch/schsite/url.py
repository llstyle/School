from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.main , name='main'),
    path('profile/regStud', views.regStud.as_view() , name='stud'),
    path('profile/addUrok/urok', views.UrokAdd.as_view() , name='addUrok'),
    path('profile/addUrok', views.AddUrok.as_view() ),
    path('profile/regTeacher', views.password , name='aaa'),
    path('profile/regTea', views.AddPassword.as_view() , name='teacher'),
    path('profile/<slug:slug>', views.Urok.as_view(), name="urok"),
    path('profile/<slug:slug>/<int:pk>', views.DetaUrok.as_view(), name="axe"),
    path('profile/login/', views.logView , name='a'),
    path('Student', views.AddReview.as_view(), name="addeview"),
    path('profile', views.Profile.as_view(), name="profile"),
    path('logn', views.login_view.as_view(), name="logn"),
    path('logout', views.logout_view, name="logout"),
]