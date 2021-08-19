from django.conf.urls.static import static
from django.shortcuts import redirect
from .views import *
from django.views.generic import TemplateView
from django.urls import path
# from blog.views import views as question_views
app_name='shorter'  


urlpatterns = [
    path('generate/', CreateShortUrl.as_view(), name = 'generate'),
    path('r/<str:string>/', redirect_to_long , name = 'redirect-to-long',)

]


