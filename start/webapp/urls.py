from django.urls import path
from webapp.views import index_views, cat_stats_views

urlpatterns = [
    path('', index_views),
    path('cat_stats/', cat_stats_views),
]
