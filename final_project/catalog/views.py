from django.shortcuts import render
from .const import courses_list, authors_list


def index(request):
    template = 'index.html'
    return render(request, template)


def info(request):
    template = 'info.html'
    return render(request, template)


def not_found(request, exception):
    template = 'not_found.html'
    return render(request, template, status=404)


def courses(request):
    template = 'courses.html'
    context = {
        'courses': courses_list
        }
    return render(request, template, context)


def course_detail(request, pk):
    course = courses_list[pk]
    author = next(
        author for author in authors_list
        if author['name'] == course['author']
    )
    context = {
        'course': course,
        'author': author,
    }
    return render(request, 'course_detail.html', context)


def authors(request):
    template = 'authors.html'
    context = {
        'authors': authors_list
        }
    return render(request, template, context)


def author_detail(request, pk):
    author = authors_list[pk]
    courses = [
        course for course in courses_list
        if course['author'] == author['name']
    ]
    context = {
        'author': author,
        'courses': courses,
    }
    return render(request, 'author_details.html', context)
