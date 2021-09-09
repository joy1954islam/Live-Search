from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee
import json
from django.http import JsonResponse
from django.db.models import Q


class EmployeeListView(ListView):
    model = Employee
    template_name = 'main.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Employee.objects.values()))
        return context


def search(request):
    if request.is_ajax and request.method == "GET":
        q = request.GET.get('search')
        if len(q) > 0:
            result = Employee.objects.filter(
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(email__icontains=q) |
                Q(address__icontains=q) |
                Q(age__icontains=q) |
                Q(city__icontains=q)
            )
            return JsonResponse({'data': list(result.values())})
        else:
            result = Employee.objects.all().values()
            return JsonResponse({'data': list(result)})
    return JsonResponse({})
