from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about-us/', views.about_us, name='about_us',),
    path('contact-us/', views.contact_us, name='contact_us',),

    path('products/',views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    path('category/<int:pk>/', views.category_products, name='category_products',),

    path('404-test/', TemplateView.as_view(template_name="404.html"),),

]
