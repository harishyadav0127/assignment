from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, OrderForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from models import CreateQueryModel, CreateUserQueryModel


def signup_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    # request.method = 'POST'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            # login(request, user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)


from django.contrib.auth.models import User


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    # request.method = 'POST'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        mentorusers = User.objects.filter(is_superuser=True, username=username)
        if mentorusers:
            return redirect('query_list')
        if user is not None:
            login(request, user)
            return redirect('query')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard.html')


@login_required(login_url='login')
def createquery(request):
    # request.method = 'POST'
    formset = OrderForm()
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        formset = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            query = formset.cleaned_data.get('query')
            CreateUserQueryModel.objects.create(user=user, query=query)
            return redirect('home')

    context = {'form': formset}
    return render(request, 'queries.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def userqurylist(request):
    querys = CreateUserQueryModel.objects.all()
    return render(request, 'query_list.html', {'results': querys})
