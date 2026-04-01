from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'student_form.html', {
        'form': form,
        'students': students
    })

def delete_unpaid(request):
    Student.objects.filter(fee_paid=False).delete()
    return redirect('/')