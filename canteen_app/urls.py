from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'canteen_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='canteen_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='canteen_app/logout.html'), name='logout'),
    path('menumain/', views.category, name='menumain'),
    path('menu/<int:food_type_id>/', views.menu_list, name='menu_list'),
    path('bill/', views.bill, name='bill'),
    path('menu1/<int:menu_id>/', views.cart, name='cart'),
    path('orders_list/', views.orders_list, name='order'),
    path('orders_list1/<int:order_id>/', views.full_fill, name='fulfill'),

    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('form/', views.form, name="form"),
    path('form/food/', views.food, name="food"),
]