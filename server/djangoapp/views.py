from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):

    
    return render(request, 'djangoapp/about.html')
 


# Create a `contact` view to return a static contact page
def contact(request):
    

    
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
    
        username = request.POST['username']
        password = request.POST['psw']
  
        user = authenticate(username=username, password=password)
        if user is not None:
         
            login(request, user)
            return redirect('djangoapp:index.html')
        else:
      
            return render(request, 'djangoapp/index.html', context)
  

# Create a `logout_request` view to handle sign out request
def logout_request(request):
  
    print("Log out the user `{}`".format(request.user.username))
 
    logout(request)
 
    return redirect('djangoapp:index.html')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)

    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        password = request.POST.get('psw')

        # Check if user already exists
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
            logger.debug("{} already exists".format(username))
        except User.DoesNotExist:
            logger.debug("{} is a new user".format(username))

        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)

            # Log in the user
            login(request, user)

            # Redirect to course list page
            return redirect("djangoapp:index")
        else:
            context['message'] = 'User already exists.'
            return render(request, 'djangoapp/index.html', context)
 

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

