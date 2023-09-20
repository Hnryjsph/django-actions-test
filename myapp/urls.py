from django.urls import path
from .views import new_feature_view, webhook

urlpatterns = [
    path('', new_feature_view, name='new_feature_view'),
    path('update-server', webhook, name='webhook'),
    # ... other URL patterns
]
