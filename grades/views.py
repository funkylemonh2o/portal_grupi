from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade

@login_required
def student_grades(request):
    grades = Grade.objects.filter(student=request.user).select_related('subject')
    return render(request, 'grades/student_grades.html', {'grades': grades})

@login_required
def all_grades(request):
    if not request.user.is_staff:
        return render(request, '403.html', status=403)
    grades = Grade.objects.select_related('student', 'subject')
    return render(request, 'grades/all_grades.html', {'grades': grades})