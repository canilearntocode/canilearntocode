from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Curriculum, Resource
from . import choices


def curriculum(request):
    curriculum = get_list_or_404(Curriculum)
    context = {'curriculum': curriculum}
    return render(request, template_name='curriculum/curriculum.html', context=context)


def subject(request, slug):
    subject = get_object_or_404(Curriculum, slug=slug)
    recommended_resources = subject.resource_set.filter(recommended=True).order_by('medium')
    additional_resources = subject.resource_set.filter(recommended=False).order_by('medium')
    context = {
        'subject': subject,
        'recommended_resources': recommended_resources,
        'additional_resources': additional_resources,
    }
    return render(request, template_name='curriculum/subject.html', context=context)