from django.http import HttpResponse
from django.shortcuts import render
import random
def index(request):
    n="Avinash"
    le=8
    context = {'user': n ,'length' : le ,'duration': None}
    if request.method == "POST":
        #handle the form
        uname = request.POST.get('uname', False)
        data = request.POST.get('password', False)
        #print(uname , data)
        if "generate" in request.POST:

            #print("HEllO @@@@@@@@@@@4$%%")
            chars="abcdefgh@#?%ijklmnopqrstuvwxyzASDFGHJKLZXCVBNMQWERTYUIOP#@?"
            length= int(data)
            value=""
            for i in range(length):
                value+=random.choice(chars)
            print("Avi..............")

            context ={'user': uname , 'length':data ,'duration':value}

            #return HttpResponse("Home")
            #return render(request,"index.html", context)
            #return HttpResponse("HEy ITS MY INDEX PAGE")
            return render(request,"home.html",context)
        if "reject" in request.POST:
            chars = "abcdefgh@#?%ijklmnopqrstuvwxyzASDFGHJKLZXCVBNMQWERTYUIOP#@?"
            length = int(data)
            value = ""
            for i in range(length):
                value += random.choice(chars)
            print("Avi..............")

            context = {'user': uname, 'length': data, 'duration': value}

            # return HttpResponse("Home")
            # return render(request,"index.html", context)
            # return HttpResponse("HEy ITS MY INDEX PAGE")
            return render(request, "home.html", context)
        if "accept" in request.POST:
            return HttpResponse("<h1 style='margin: auto;width: 60%;border: 3px solid #73AD21; padding: 10px; text-align:center; background-color: rgba(0, 0, 0, 0.15);'> "
                                "Password Accepted </h1>")
    return render(request, "home.html", context)
    #return HttpResponse("HEy ITS MY INDEX PAGE")