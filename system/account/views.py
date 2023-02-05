from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import RegisterUser


class RegisterUserView(TemplateView):

    def get(self, request):

        form = RegisterUser()

        context = {
            'form': form 
        }

        return render(request, 'registration/register.html', context)

    def post(self, request):

        form = RegisterUser(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

class RegisterUserView2(CreateView):

    form_class = RegisterUser
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')