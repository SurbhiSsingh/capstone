# from django.shortcuts import render
# from .models import FacultyMember

# from django.shortcuts import render, get_object_or_404

# def faculty_list(request):
#     faculties = FacultyMember.objects.all()
#     return render(request, 'faculty/faculty_list.html', {'faculties': faculties})

# def faculty_detail(request, faculty_id):
#     faculty = get_object_or_404(FacultyMember, id=faculty_id)
#     return render(request, 'faculty/faculty_detail.html', {'faculty': faculty})
from django.shortcuts import render, get_object_or_404
from .models import Faculty
from .models import Affiliation


def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty/faculty_list.html', {'faculties': faculties})

def faculty_detail(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    return render(request, 'faculty/faculty_detail.html', {'faculty': faculty})

def affiliation_detail(request, slug):
    affiliation = get_object_or_404(Affiliation, slug=slug)
    return render(request, 'faculty/affiliation_detail.html', {'affiliation': affiliation})
