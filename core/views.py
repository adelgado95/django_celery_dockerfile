from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts
import logging

def UserList(request):
    """
    Función vista para la página inicio del sitio.
    """
    logger = logging.getLogger(__name__)
    #User.objects.all().delete()
    userss = User.objects.all()
    logger.error(User.objects.all().count())
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'core/users_list.html',
        context={'user_list':userss},
    )
class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('user_list')