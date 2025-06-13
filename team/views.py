from django.shortcuts import render, redirect
from .models import TeamMember
from .forms import TeamMemberForm
from .utils import login_required



def team_list(request, degree):
    members = TeamMember.objects.filter(degree=degree)
    return render(
        request, f"team/team_list.html", {"members": members, "degree": degree}
    )

@login_required
def add_member(request):
    if request.method == "POST":
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("team_" + form.cleaned_data["degree"])
    else:
        form = TeamMemberForm()
    return render(request, "team/add_member.html", {"form": form})
