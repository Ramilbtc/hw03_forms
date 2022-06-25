# импортируем CreateView чтобы создать ему наследника
from django.views.generic import CreateView
# функция reverse_lazy позволяет получить URL по параметрам path()
from django.urls import reverse_lazy
# испортируем класс-формы, чобы сослаться на него во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm   # с какой формой будет работать этот View-класс
    success_url = reverse_lazy('posts:index')  # куда переадресовать пользователя после успешной отправки формы регистрации
    template_name = 'users/signup.html'  # имя шаблона, куда будет передана переменная form с объектом html-формы
