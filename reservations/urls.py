from django.urls import path
from .views import reservation_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', reservation_view, name='reservation'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
