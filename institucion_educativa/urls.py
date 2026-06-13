from django.urls import path
from .views import InstitucionListCreateView, InstitucionDetailView

urlpatterns = [

    path('instituciones/', InstitucionListCreateView.as_view(), name='instituciones-list'),
    path('instituciones/<int:pk>/', InstitucionDetailView.as_view(), name='instituciones-detail'),
]