from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeFun, name='home'),
    path('addUsingGetUrl',views.addUsingGetFun, name='addGet'),
    path('addUsingPostUrl',views.addUsingPostFun, name='addPost'),
    path('ok',views.okFun, name='ok')
]