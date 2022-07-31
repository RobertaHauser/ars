from django.shortcuts import render, redirect

from django.contrib import messages
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.sites.shortcuts import get_current_site

#from django.template.loader import render_to_string
#from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
#from .utils import generate_token
#from django.core.mail import EmailMessage
#from django.conf import settings
#import threading

from validate_email import validate_email
#from django.urls import reverse
from .models import CustomUser

# Create your views here.
### REGISTER
#@auth_user_should_not_access
def register(request):
    
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'A senha deve ter pelo menos 6 caracteres')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Senha incorreta')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Digite um endereço de e-mail válido')
            context['has_error'] = True

        if CustomUser.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'E-mail já cadastado, escolha outro')
            context['has_error'] = True

        if not first_name:
            messages.add_message(request, messages.ERROR,
                                 'O campo nome é obrigatório')
            context['has_error'] = True

        if not last_name:
            messages.add_message(request, messages.ERROR,
                                 'O campo sobrenome é obrigatório')
            context['has_error'] = True


            #### TUTORIAL CRYCE TRULLY, AULA 29
            #return render(request, 'register.html', context, status=409)

        if context['has_error']:
            return render(request, 'register.html', context)

        #user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
        user = CustomUser.objects.create_user(email=email, first_name=first_name, last_name=last_name,password=password)
        user.set_password(password)
        user.save()

        #send_activation_email(user, request)

        messages.add_message(request, messages.SUCCESS,'Conta criada, você pode logar')
        #messages.add_message(request, messages.SUCCESS,'Enviamos um e-mail para verificar sua conta')

        #return redirect('login')
    
    return render(request, 'register.html')