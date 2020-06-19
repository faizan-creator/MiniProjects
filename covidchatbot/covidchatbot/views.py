from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages,admin
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
#from tkinter import messagebox

def welcome(self):
    return render(self,'welcome.html')

def intro(self):
    print(admin.site.login_template.__dir__())
    return render(self,'intro.html')
    #return HttpResponse('Faizan Mushtaque Shaikh')

def signup(self):
    #print('Faizan1')
    if self.method == 'POST':
        #print('Faizan2')
        username = self.POST.get('username')
        if len(username) > 10:
            messages.error(self, "Username shouldn't exceeds 10 characters.")
            return redirect('/')
        if not username.isalnum():
            messages.error(self, "Username must be alphanumeric. It should only contains letters or numbers.")
            return redirect('/')
        firstname = self.POST.get('firtsname')
        lastname = self.POST.get('lastname')
        pass1 = self.POST.get('pass1')
        pass2 = self.POST.get('pass2')
        if pass1 != pass2:
            messages.error(self, "Passwords do not match.")
            return redirect('/')
        emailing = self.POST.get('emailing')
        op = User.objects.filter(username=username)
        print('Faizan1')
        print(op)
        print('Faizan2')
        #if ( str(op[0]).upper().strip() == str(username).upper().strip() ):
        if (op.exists()):
            print('Faizan3')
            messages.error(self, str("User "+username+" Already Exists. Kindly use another username."))
            return redirect('/')
        print('Faizan4')
        myuser = User.objects.create_user(username, emailing, pass1)
        print('Faizan5')
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(self, 'Your account has been successfully created.')
        print('Faizan3')
        return redirect('/')
    else:
        return HttpResponse("404 Not Found.")

def loginhandle(self):
    if self.method == 'POST':
        username = self.POST.get('loginusername')
        password = self.POST.get('loginpass1')
        user = authenticate(username=username,password=password)
        #print('FaizanUser')
        #print(user)
        if user is not None:
            login(self,user)
            #messages.success(self,'successfully logged in.')
            return redirect('/intro/')
        else:
            messages.error(self, 'Invalid Credentials.')
            return redirect('/')
    else:
        return HttpResponse("404 Not Found.")

def logouthandle(self):
    if self.method == 'POST':
        #MsgBox = messagebox.askyesno('Logout', 'Are you sure you want to Logout from the application')
        #if MsgBox == 'yes':
        logout(self)
        messages.success(self,'You have successfully logged out.')
        return redirect('/')
        #else:
           # return render(self, 'welcome.html')
    else:
        return HttpResponse("404 Not Found.")