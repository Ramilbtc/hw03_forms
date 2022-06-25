from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from . import views

app_name = 'users'


# Class Based View это view на основе классов, поэтому с ними используется .as_view()
urlpatterns = [
    # регистрация
    path('signup/', views.SignUp.as_view(), name='signup'),
    # авторизация
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    # выход из аккаунта и показ прощальной страницы
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),  # прямо тут можно указать шаблон для view-класса
        name='logout',
    ),
    # смена пароля
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='password_change'),
        name='password_change',
    ),
    # сообщение об успешном изменении пароля
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='password_change_done'),
        name='password_change_done',
    ),
    # восстановление/сброс пароля
    path(
        'password_reset/',
        PasswordResetView.as_view(template_name='users/password_reset_form.html'),
        name='password_reset_form',
    ),
    # сообщение об отправке ссылки на восстановление пароля
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done',
    ),
    # вход по ссылке для восстановления пароля
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm'),
        name='password_reset_confirm',
    ),
    # успешная смена пароля
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete'),
        name='password_reset_complete',
    ),

]
