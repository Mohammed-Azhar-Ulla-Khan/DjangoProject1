from django.shortcuts import render
from myApp.models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class StudentView(ListView):
    model = Student
    context_object_name = 'Student_list'
    template_name = 'myApp/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'myApp/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'myApp/student_form.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = {'name', 'marks'}
    template_name = 'myApp/student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    template_name = 'myApp/student_confirm_delete.html'
