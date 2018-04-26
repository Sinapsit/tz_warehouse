from django.urls import path, re_path
from order import views

urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path(r'item/<int:number>/', views.OrderItemView.as_view(), name='order_item'),
]