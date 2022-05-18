from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name="patient_login"),
    path('logout/', LogoutView.as_view(next_page="/"), name="patient_logout"),
    path('register/', views.register, name='patient_register')
]
