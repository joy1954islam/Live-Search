from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee
import json


class EmployeeListView(ListView):
    model = Employee
    template_name = 'main.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Employee.objects.values()))
        return context
