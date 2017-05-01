from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Curriculum


def curriculum(request):
    curriculum = get_list_or_404(Curriculum)
    context = {'curriculum': curriculum}
    return render(request, template_name='curriculum/curriculum.html', context=context)


def subject(request, slug):
    subject = get_object_or_404(Curriculum, slug=slug)
    context = {'subject': subject}
    return render(request, template_name='curriculum/subject.html', context=context)