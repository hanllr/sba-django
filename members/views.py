from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.
def index(req):
    print(dir(req))
    return HttpResponse("hello")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        #if username == 'exit' :
        #    return HttpResponse('나가기')
       # elif username == 'codingon' :
        #    return render(req, 'login.html')
        member = Members(
                username = username ,
                useremail = email
        )       

        member.save()
        res_data = {}
        res_data['res']='등록성공'
        return render(req, 'index.html', res_data)
    return render(req, 'index.html')
