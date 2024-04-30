from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm, CreateRecordForm

from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from . models import Record, Department

from django.contrib import messages

   
class home(TemplateView):
    template_name = 'register/index.html'


# - Register
class register(View):

    def get(self, request):
        form = SignUpForm()
        context = {'form':form}
        return render(request, 'register/register.html', context=context)
       

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account Successfully Created!")

            return redirect('login')
        
        context = {'form':form}
        return render(request, 'register/register.html', context=context)
  

# Login a user
class login(View):

    def get(self, request):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'register/login.html', context=context)


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
        
        return redirect('dashboard')
            

# Users DashBoard
class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        my_records = Record.objects.filter(user=self.request.user.id).order_by('id')
        context = {'records': my_records}
  
        return render(request, 'register/dashboard.html', context=context)
  

# Create Record
class create_record(LoginRequiredMixin, CreateView):
    model = Record
    form_class = CreateRecordForm
    
    template_name = 'register/create-record.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
 
# Update Record

class update_record(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = CreateRecordForm
    template_name = 'register/update-record.html'
    success_url = reverse_lazy('dashboard')
    
  

# Read / View a singular record
class view_record(LoginRequiredMixin, View):
    def get(self, request, pk):
        all_records = Record.objects.get(id=pk)
        context = {'record': all_records}
        return render(request, 'register/view-record.html', context=context)


# Delete a record
class delete_record(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'register/delete-record.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'my_record'


