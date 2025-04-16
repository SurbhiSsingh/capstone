from django.shortcuts import render,get_object_or_404
from .models import Student
from django.http import JsonResponse
from django.core.serializers import serialize

def student_list(request):
    students = Student.objects.all()
    students_json = serialize("json", students)
    print(students_json)
    return render(request, "students/students_list.html", {"students": students})

def student_detail(request,slug):
    student = get_object_or_404(Student, slug=slug)
    print(student)
    return render(request, "students/student_details.html", {"student": student})

# def add_student(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("student_list")
#     else:
#         form = StudentForm()
#     return render(request, "students/add_student.html", {"form": form})
