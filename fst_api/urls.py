"""fst_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from core.views import TestView
from core.views import ScholarshipView
from core.views import PhoneNumberView
from core.views import ContactView
from core.views import EventView
from core.views import NewsFeedView
from core.views import PositionView
from core.views import GeoJSONFeatureView
from core.views import GeometryObjectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
    path('testview/', TestView.as_view()),
    path('contact/', ContactView.as_view()),
    path('scholarship/', ScholarshipView.as_view()),
    path('phone/', PhoneNumberView.as_view()),
    path('events/', EventView.as_view()),
    path('newsfeed/', NewsFeedView.as_view()),
    path('position/', PositionView.as_view()),
    path('feature/',GeoJSONFeatureView.as_view()),
    path('geometryobject/', GeometryObjectView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)