from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Curriculum, Resource
from . import choices


def curriculum(request):
    curriculum = get_list_or_404(Curriculum)
    context = {'curriculum': curriculum}
    return render(request, template_name='curriculum/curriculum.html', context=context)


def subject(request, slug):
    subject = get_object_or_404(Curriculum, slug=slug)
    courses = subject.resource_set.filter(medium=choices.COURSE)
    books = subject.resource_set.filter(medium=choices.BOOK)
    videos = subject.resource_set.filter(medium=choices.VIDEO)
    lectures = subject.resource_set.filter(medium=choices.LECTURE)
    online_resources = subject.resource_set.filter(medium=choices.ONLINE)
    context = {
        'subject': subject,
        'mediums': (courses, online_resources, videos, lectures, books),
    }
    return render(request, template_name='curriculum/subject.html', context=context)