from django.conf.urls import url
from webapp import views


urlpatterns = [
    url('',views.index,name='index')
]
