from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question

# Create your views here.

def index(request):
    try:
       obj = Question.objects.order_by('-pub_date')
    except:
        raise Http404("Model doesn't exists")   
    output = ','.join(q.question_text for q in obj)
    context = {"data":obj}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    obj = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/details.html",context={"question":obj})

def result(request,question_id):
    response = "result of:"+str(question_id)
    return HttpResponse(response)

def vote(request,question_id):
    response = "vote of:"+str(question_id)
    return HttpResponse(response)