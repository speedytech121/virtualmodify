from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contactpage/',views.contact,name='ContactUs'),
    path('analyze',views.analyze,name='analyze'),
    path('contactpage/analyze', views.analyze, name='analyze'),

]
