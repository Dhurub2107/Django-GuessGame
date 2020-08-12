from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
import random
# Create your views here.
def login(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        password=request.POST['password']
        print("uname",user_name)
        print("Pasword",password)
        user=auth.authenticate(username=user_name,password=password)
        print("user:",user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            #messages.info(request,"Welcome")
            
        else:
            messages.info(request,"Wrong Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        #first_name=request.POST['first_name']
        #last_name=request.POST['last_name']
        email=request.POST['Email']
        password1=request.POST['Password']
        RepeatPassword=request.POST['repeat_password']
        if password1==RepeatPassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,email=email,password=password1)
                user.save()
                print("user Created")
                #messages.info(request,"User account created sucessfully!!")
                return redirect('login')
        else:
            messages.info(request,"Password and Repeat Password Not Matched!")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def home(request):
    return render(request,'index.html')
def logout(request):
    auth.logout(request)
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def score(request):
    return render(request,'Score.html')
def game(request):
    x=random.randrange(1,20)
    context= {
        'x': x,
        }
    return render(request,'game.html',context)
    
def logic(request):
        i=0
        #context={}
        #context['x']=1414
        
        #person= {'firstname': 'Craig', 'lastname': 'Daniels'}
        #weather= "sunny"
        
        return render(request,'Score.html')
        #x=random.randrange(1,20)
        #context['v']=12121
        #x=random.randrange(1,20)
        while True:
            user_num=request.POST['Guess']
            #if int(user_num) is not None:
            if int(x)==int(user_num):
                return render(request,'Score.html')
            elif int(user_num)>int(x):
                print(x)
                print(user_num)
                messages.info(request,"Your Number is Greater than Randome Number ")
                return redirect('Game')
                #return render(request,'Wrong.html')
            else:
                messages.info(request,"Your Number is less than Randome Number ")
                return redirect('Game')
                #return False
            i=i+1
            print(i)
            if i==5:
                #print("Limit Exceed Max 5 Times!!")
                #print("Thank You For Playing")
                messages.info(request,"Limit Exceed Max 5 Times!!Game Over ")
                break
            
                

        #print(x)
        #print(user_num)
def update_score(request):
    if request.method == 'POST':
        score = score.objects.get()
        user.blur_quantity =  request.POST['score']
        score.save()
        message = 'update successful'
    return HttpResponse(message)

    

 
