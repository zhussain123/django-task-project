from django.urls import path
from .views import (
    PremiumUsersView,
    ActivePremiumUsersView,
    CompanyRevenueView,
    ExecutivesInfoView,
    DigestEmailStatsView,
)

urlpatterns = [
    path('premium-users/', PremiumUsersView.as_view()),
    path('active-premium-users/', ActivePremiumUsersView.as_view()),
    path('company-revenue/', CompanyRevenueView.as_view()),
    path('executives-info/', ExecutivesInfoView.as_view()),
    path('digest-stats/', DigestEmailStatsView.as_view()),
]
