from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("profile_id"):
            return redirect("login")  # Redirect to the login page if not logged in
        return view_func(request, *args, **kwargs)
    return wrapper