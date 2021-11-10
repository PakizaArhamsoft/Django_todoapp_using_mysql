from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Employee
from .forms import PositionForm


class CustomLoginView(LoginView):
    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('employees')


class RegisterPage(FormView):
    template_name = 'todo_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('employees')
        return super(RegisterPage, self).get(*args, **kwargs)


class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = context['employees'].filter(user=self.request.user)
        return context


class EmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'todo_app/employee.html'


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['emp_name', 'emp_code', 'mobile','position']
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmployeeCreate, self).form_valid(form)


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['emp_name', 'emp_code', 'mobile','position']
    success_url = reverse_lazy('employees')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('employees')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class EmployeeReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_employee_order(positionList)

        return redirect(reverse_lazy('employees'))
