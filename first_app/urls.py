from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index),
    path('form/',views.form_view),
    path('webpage/',views.web_page_view)
]
