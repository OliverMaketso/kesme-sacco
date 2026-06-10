"""
KESME SACCO – Root URL Configuration
All API routes are prefixed with /api/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from accounts.serializers import MemberTokenObtainSerializer


class MemberTokenObtainView(TokenObtainPairView):
    serializer_class = MemberTokenObtainSerializer


urlpatterns = [
    #ROOT HEALTH CHECK
    path('', lambda request: HttpResponse("KESME SACCO API is running!")),
    
    # Django admin
    path('admin/', admin.site.urls),

    # JWT auth
    path('api/auth/login/',   MemberTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(),     name='token_refresh'),
    path('api/auth/logout/',  TokenBlacklistView.as_view(),   name='token_blacklist'),

    # App routers
    path('api/members/',      include('accounts.urls')),
    path('api/savings/',      include('savings.urls')),
    path('api/loans/',        include('loans.urls')),
    path('api/news/',         include('news.urls')),
    path('api/contact/',      include('contact.urls')),
    path('api/agribusiness/', include('agribusiness.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
