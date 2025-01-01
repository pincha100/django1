from django.shortcuts import render

def function_based_view(request):
    return render(request, "second_task/function_template.html")

from django.views.generic import TemplateView

class ClassBasedView(TemplateView):
    template_name = "second_task/class_template.html"
