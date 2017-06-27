from django.conf.urls import url
from django.conf.urls import include
from orders import views



urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]
