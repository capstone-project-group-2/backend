from django.conf.urls import url
from django.urls import path
from invoice import views

urlpatterns = [
    path('invoices/', views.invoice_list),
    path('invoices/<pk>', views.invoice_detail),
]