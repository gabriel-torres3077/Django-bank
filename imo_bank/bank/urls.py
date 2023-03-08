from django.urls import path, include
from .views import AccountDetail, AccountViewSet, TransactionDetail, Transfer


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', AccountViewSet.as_view()),
    path('account/<int:pk>/', AccountDetail.as_view()),
    path('transaction/<int:pk>/', TransactionDetail.as_view()),
    path('transfer/', Transfer.as_view())
]