from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('partytime/', views.partytime, name='partytime'),
    path('partytime/services/', views.services, name='services'),
    path('partytime/about/', views.about, name='about'), 
    path('partytime/contact/', views.contact, name='contact'),
    path('partytime/faq/', views.faq, name='faq'),
    path('partytime/blogs/', views.blogs, name='blogs'),
    path('partytime/checkout/', views.checkout, name='checkout'),
    path('partytime/blogs/<str:description>',views.blog_display, name='blog_display'),
]
