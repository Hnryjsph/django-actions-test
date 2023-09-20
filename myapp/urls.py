from django.urls import path
from .views import new_feature_view

urlpatterns = [
    path('new-feature/', new_feature_view, name='new_feature_view'),
    # ... other URL patterns
]
