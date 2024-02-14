# maazbackend/urls.py
from django.contrib import admin
from django.urls import path
from maazserver.views import YourModelListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('your-model-list/', YourModelListView.as_view(), name='your-model-list'),
]
