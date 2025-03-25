from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('childrecord/', TemplateView.as_view(template_name='childrecord.html'), name='childrecord'),
    path('registerchild/', TemplateView.as_view(template_name='registerchild.html'), name='registerchild'),
    path('medication/', views.medication_view, name='medication'),
]