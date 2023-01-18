from django.shortcuts import render,redirect
from .forms import RegisterForm, PostQuestion,PostChoises
from .models import Question, Choice
from django.contrib import messages


# Create your views here.

#AUTHENTICATION
#Registration!

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})





def index(request):
    questions = Question.objects.all()
    return render (request,'temp/index.html',{'questions': questions})




def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    return render (request,'temp/vote.html',{'question':question, 'options': options })




def result(request,pk):
     question = Question.objects.get(id=pk)
     options = question.choices.all()
     if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()

     return render (request,'temp/result.html',{'question': question, 'options': options})




#POST QUESTION AND CHOICE

def Post(request):
    if request.method == "POST":
        fm = PostQuestion(request.POST)
       
        if fm.is_valid():
         fm.save()
        
        return redirect("/choice")
    
    else:
     fm = PostQuestion()
    return render(request,'temp/question.html',{"form":fm})



def Postchoice(request):
    if request.method == "POST":
        fm = PostChoises(request.POST)
       
        if fm.is_valid():
         fm.save()
        
        return redirect("/choice")
    
    else:
     fm = PostChoises()
    return render(request,'temp/choice.html',{"form":fm})



#USER PROFILE
def profile(request):
    context = {
        'user': request.user, 'question':Question.objects.all()
    }
   
    
    return render(request,'profile/profile.html',context)