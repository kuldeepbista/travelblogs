from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
		path('', views.homepage, name = 'homepage'),
		path('portfolio/', views.portfoliopage, name = 'portfoliopage'),
		path('contact/', views.contactpage, name = 'contactpage'),
		path('blog/', views.blogpage, name = 'blogpage'),
		
]