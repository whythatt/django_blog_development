"""django_blog_development URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users import views as users_views
from posts import views as posts_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls, name="hulahup"),
    path(
        "login/",
        TemplateView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", posts_views.post_page, name="post"),
    path("register/", users_views.register_request, name="register"),
    path("edit_profile/", users_views.edit_profile, name="edit_profile"),
    path("profile/<str:username>/", users_views.profile, name="profile"),
    path("<str:username>/", users_views.user_profile, name="user_profile"),
]

# for images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
