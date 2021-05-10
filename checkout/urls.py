from django.urls import path

from checkout.views import LinkAPIView, OrderAPIView

urlpatterns=[
    path('links/<str:code>', LinkAPIView.as_view()),
    path('orders', OrderAPIView.as_view())
]