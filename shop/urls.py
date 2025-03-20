from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('home_page/', home_page, name='home_page'),
    path('order_page/', order_page, name='order_page'),
    path('order/', main_page, name='main_order'),
]
