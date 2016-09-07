from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, TemplateView, DetailView, CreateView
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from .models import Mobile
from mobile.forms import UserForm, AddMobileForm


# Create your views here.

class IndexView(ListView):
    model = Mobile


class UserFormView(View):
    form_class = UserForm
    template_name = 'signup.html'

    # on get request sent a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # on the post request
    def post(self, request):
        form = self.form_class(request.POST)

        # verify the posted data
        if form.is_valid():

            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class HomePageView(TemplateView):
    template_name = 'index.html'


class Detail(DetailView):
    model = Mobile
    template_name = 'mobile/mobiledetail.html'


class AddMobileView(CreateView):
    model = Mobile
    form_class = AddMobileForm
    template_name = 'mobile/mobile_form.html'
    success_url = '/home/'

    


