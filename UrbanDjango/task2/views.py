from django.shortcuts import render
from django.views.generic import TemplateView


def task2_func(request):
    return render(request,
                  'second_task/template_for_a_functional_view.html',
                  )


# def task2_class(request):
#     return render(request,
#                   'second_task/template_for_a_class_view.html',
#                   )


class task2_class(TemplateView):
    template_name = 'second_task/template_for_a_class_view.html'
