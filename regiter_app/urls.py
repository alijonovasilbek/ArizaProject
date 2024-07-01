from django.urls import path
from .views import user_information_view
from django.views.generic import TemplateView


urlpatterns = [
    path('', user_information_view, name='user_information'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
