from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]


# from django.urls import path

# from . import views

# app_name = 'shop'

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('<slug:category_slug>/',
#          views.product_list,
#          name='product_list_by_category'),
#     path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
# ]
