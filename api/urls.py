from django.urls import path
from . import views

urlpatterns = [
    path('policies', views.getPolicies),
    path('get-policy/<int:id>', views.getPolicy),
    path('add-policy', views.addPolicy),
    path('update-policy/<int:id>', views.updatePolicy),
    path('delete-policy/<int:id>', views.deletePolicy)
]