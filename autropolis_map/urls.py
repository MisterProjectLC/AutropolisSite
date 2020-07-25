from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('status', views.LocalListView.as_view(), name='status'),
    path('<pagername>', views.page, name='page'),
]
