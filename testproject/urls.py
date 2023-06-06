from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('homebase.urls')),
    path('admin/', admin.site.urls),
    path('blog/register/', user_views.register, name='register'),
    path('blog/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('blog/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/password-reset', 
        view=auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password-reset'),
    path('blog/password-reset/done', 
        view=auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('blog/password-reset/complete', 
        view=auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path('blog/password-reset-confirm/<uidb64>/<token>/', 
        view=auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('blog/profile/', user_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)