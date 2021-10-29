"""roche URL Configuration

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
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from .views import dashboard, login_page, logut_page, registerpage
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('register/', registerpage, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logut_page, name='logout'),
    path('events/', include('events.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

# path('reset_password/',
#      auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
#      name="reset_password"),
#
#     path('reset_password_sent/',
#         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
#         name="password_reset_done"),
#
#     path('reset/<uidb64>/<token>/',
#      auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
#      name="password_reset_confirm"),
#
#     path('reset_password_complete/',
#         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
#         name="password_reset_complete"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)