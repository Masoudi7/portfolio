from django.urls import path
from .views import home,detail

app_config='chrome'
urlpatterns=[
    path('',home,name='home'),
    path('detail/<slug:slug>',detail,name='detail')
]