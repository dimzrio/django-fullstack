from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Path to access the admin page
    path('admin/', admin.site.urls),
    # Path to render the Homepage
    path('', views.frontend, name='frontend'),
    # Path login/logout
    path('login/', include('django.contrib.auth.urls')),

    # Backend
    path('backend/', views.backend, name='backend'),

    # Add patient
    path('add_patient', views.add_patient, name='add_patient')
]
