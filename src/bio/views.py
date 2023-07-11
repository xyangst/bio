import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from bio.models import SocialPlatform, SocialUser
from random import choice
User = get_user_model()


def home_view(request):
    return render(request, "pages/home.html", {})


def login_view(request):
    return render(request, "pages/auth/main.html", {})


    
def signin(request):
    if request.method != "POST":
        return HttpResponse("ERROR")
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(home_view)
    else:
        messages.error(request, "Invalid username or password")
    return redirect(login_view)
def signup(request):
    if request.method != "POST":
        return HttpResponse("ERROR")
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if len(username) < 3 or len(username) > 15:
        messages.error(
        request, "Username should be between 3 and 15 characters.")
        return redirect(login_view)

    if len(password) < 5:
        messages.error(
            request, "Password should be at least 5 characters long.")
        return redirect(login_view)

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        messages.error(request, "Invalid email address.")
        return redirect(login_view)

    if User.objects.filter(username=username).exists():
        messages.error(request, "Username is already taken.")
        return redirect(login_view)

    user = User.objects.create_user(
        username=username, email=email, password=password)
    login(request, user)
    return redirect(dashboard)

@login_required
def update(request,route):
    if request.method != "POST":
        return HttpResponse("ERROR")
    if route == "customize":
        user = request.user
        # Update the user model fields
        user.displayName = request.POST.get('displayName')
        user.pfpImage = request.POST.get('pfpImage')
        user.bio = request.POST.get('bio')
        user.backgroundImage = request.POST.get('backgroundImage')
        user.textColor = request.POST.get("textColor")
        # Save the updated user object
        user.save()
        # Return a JSON response indicating success
        return JsonResponse({'message': 'Profile updated successfully.'})

    if route == "socials":
        form_data = request.POST

        for field_name, field_value in form_data.items():
            platforms = SocialPlatform.objects.filter(
                platform__iexact=field_name)
            if platforms.exists():
                platform = platforms.first()

                social_user = SocialUser.objects.filter(
                    user=request.user, platform=platform).first()
                if social_user:
                    if not field_value:
                        social_user.delete()
                        print("Deleted:", field_name)
                    else:
                        social_user.name = field_value
                        social_user.save()
                        print(field_name, field_value)
                else:
                    if field_value:
                        social_user = SocialUser(
                            user=request.user, platform=platform, name=field_value)
                        social_user.save()
                        print(field_name, field_value)

        return JsonResponse({'message': 'Profile updated successfully.'})
    if route == "music":

        request.user.songLink = request.POST.get('songLink')
        request.user.save()
        return JsonResponse({'message': 'success'})
    if route == "misc":
        user = request.user
        print(request.POST.get('show_views'))
        user.showViewCount = request.POST.get('show_views') == "on"
        user.showCard = request.POST.get('show_card') == "on"

        user.showSnowFlakes = request.POST.get('show_snowflakes') == "on"

        user.save()
        return JsonResponse({"message": 'not implemented'})

def bio(request, username):
    username = username.lower()
    user = get_object_or_404(User, username=username)
    user.views += 1
    user.save()
    views = None
    if user.showViewCount:
        views = user.views
    return render(request, "pages/user.html", {
        "username": user.username,
        "bio": user.bio,
        "pfpImage": user.pfpImage,
        "backgroundImage": user.backgroundImage,
        "displayName": user.displayName,
        "textColor": user.textColor,
        "socials": user.socials.all(),
        "platforms": SocialPlatform.objects.all(),
        "song": user.songLink,
        "views": views,
        "showCard": user.showCard,
        "snowflakes":user.showSnowFlakes
    })


class PlatformUser:
    def __init__(self, platform, user):
        self.platform = platform
        self.username = user
        try:
            self.social_user = SocialUser.objects.get(
                platform=self.platform, user=user)
        except SocialUser.DoesNotExist:
            self.social_user = ""


@login_required
def dashboard(request):
    if request.method == 'POST':
        pass
    user = request.user
    platforms = SocialPlatform.objects.all()
    platformss = [PlatformUser(platform, user) for platform in platforms]
    return render(request, "pages/dashboard.html", {
        "platforms": platformss,


    })

def randomuser(request):
    #https://stackoverflow.com/a/62530224
    pks = User.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_user = User.objects.get(pk=random_pk)
    return redirect('bio',random_user)


def log_out(request):
    logout(request)
    return redirect('login')
