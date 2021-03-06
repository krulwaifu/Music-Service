from django.http import HttpResponse
from django.shortcuts import render, redirect
import pyrebase
from django.contrib import auth
from django.contrib.auth import get_user_model, login, authenticate

from accounts.forms import LoginForm, RegisterForm

User = get_user_model()
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            #attempt = request.session.get("attempt") or 0
            #request.session['attempt'] = attempt + 1
            request.session['register_error']=1 # 1==true
    return render(request, "signup.html", {"form": form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            #attempt = request.session.get("attempt") or 0
            #request.session['attempt'] = attempt + 1
            request.session['invalid_user']=1 # 1==true
    return render(request, "signIn.html", {"form": form})
def logout_view(request):
    logout(request)
    return render(request, 'home.html')
# Create your views here.

firebaseConfig = {
    'apiKey': "AIzaSyAvuXfqqP234QrjR4y3qXI8IMDJpPSpGO8",
    'authDomain': "onlysans-d5bc4.firebaseapp.com",
    'projectId': "onlysans-d5bc4",
    'storageBucket': "onlysans-d5bc4.appspot.com",
    'messagingSenderId': "107568749850",
    'appId': "1:107568749850:web:c5490064ed1032f5d6a0a3",
    'measurementId': "G-Q12ZCN7ZFF",
    'databaseURL':"ref"
}
firebase=pyrebase.initialize_app(firebaseConfig)
authe=firebase.auth()
database=firebase.database()
#login
def signIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('passw')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid credentials"
        return render(request, "signIn.html", {"message":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"home.html",{"e":email})

def logout(request):
    try:
        del request.session['token_id']
    except KeyError:
        pass
    return render(request, "home.html")


def signup(request):
    return render(request,"signup.html")

def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('passw')
    try:
        user=authe.create_user_with_email_and_password(email,passw)

    except:
        message="Unable to create account try again"
        return render(request, "signIn.html", {"message":message})
        uid = user['localId']
    authe.send_email_verification(user['idToken'])
    data={"name":name,"status":"1"}

  #  database.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")

def get_all_users(request,):
    global response
    if request.method == "GET":
        User = get_user_model()
        users = User.objects.all()
        context = {'users': users,
                   'title': 'audios'}
        return render(request, 'showUser.html', context)

def get_user(request,id):
    global response
    if request.method == "GET":
        User = get_user_model()
        users = User.objects.get(id = int(id))
        list = [users]
        context = {'users': list,
                   'title': 'users'}
    return render(request,'showUser.html', context)
def delete_user(request,id):
    if request.method == "GET":
        User = get_user_model()
        users = User.objects.get(id = int(id))
        users.delete()
    return HttpResponse("User deleted successfully")

def edit_name(request,id,new_username):
    if request.method == "GET":
        User = get_user_model()
        users = User.objects.get(id = int(id))
        users.username = new_username
        users.save(update_fields=["username"])
    return HttpResponse("User edited successfully")

def home(request):
    return render(request, "home.html")