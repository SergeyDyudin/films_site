from django.urls import path
from records import views


urlpatterns = [
    path('', views.records_list, name='records-list'),
    path('record_<int:record_id>', views.record, name='record'),
]