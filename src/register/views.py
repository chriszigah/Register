from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm, CreateRecordForm

from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from . models import Record, Department

from django.contrib import messages

from . helpers import unique_id_generator

     
class Home(TemplateView):
    template_name = 'register/index.html'

# - Register
class Register(View):

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
class Login(View):

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
        
        return reverse_lazy('dashboard')
            
# Users DashBoard
class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        my_records = Record.objects.filter(user=self.request.user.id).order_by('creation_date')
        context = {'records': my_records}
  
        return render(request, 'register/dashboard.html', context=context)
  
# Create Record
class CreateRecord(LoginRequiredMixin, CreateView):
    model = Record
    form_class = CreateRecordForm
    template_name = 'register/create-record.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.record_id = unique_id_generator("REG", 6)
        form.instance.user = self.request.user
        return super().form_valid(form)
        
 
# Update Record
class UpdateRecord(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = CreateRecordForm
    template_name = 'register/update-record.html'
    success_url = reverse_lazy('dashboard')
    
# Read / View a singular record
class ViewRecord(LoginRequiredMixin, View):
    def get(self, request, pk):
        all_records = Record.objects.get(record_id=pk)
        context = {'record': all_records}
        return render(request, 'register/view-record.html', context=context)

# Delete a record
class DeleteRecord(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'register/delete-record.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'my_record'


