from django.shortcuts import render, redirect, get_object_or_404

from .forms import CourseForm
from .models import Course


# Create your views here.
def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('courses:index')
    else:
        form = CourseForm()

    return render(request, 'create.html', {'form': form})


def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('courses:index')


def course_show(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'show.html', {'course': course})
