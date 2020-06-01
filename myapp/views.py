from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from . import forms
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Register

# Create your views here.


def home(request):
    return HttpResponse('Congrats your first webpage')

def about(request):
    return HttpResponse('i am a data science developer')

def contact(request):
    return HttpResponse('reach me on pankush9096@gamil.com')

def templaterendering(request):
    return render(request,'index.html')

# def form_view(request):
#
#     if request.method=='POST':
#         form= forms.Loginform(request.POST)
#         if form.is_valid():
#             print("validation worked")
#             # print('Name:'+ form.cleaned_data['name'])
#             # print('email:' + form.cleaned_data['email'])
#             # print('text:' + form.cleaned_data['text'])
#         return redirect('thanks')
#     # integrating forms.py to register.html to get form
#     form= forms.Loginform # thsi form will be injected into html file
#     return render(request, 'register.html', {'form': form})
#     # giving template tag to pass form variable attributes to template tag which is key in dictionary {'form' : form}

# Modelform and saving it

def form_view(request):

    if request.method=='POST':
        form= forms.Loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('thanks')
            except:
                print("Error Saving")

    else:
        form= forms.Loginform # this form will be injected into html file
    return render(request, 'register.html', {'form': form})
    # giving template tag to pass form variable attributes to template tag which is key in dictionary {'form' : form}

def thanks(request):
    return render(request, 'home.html')


class LoginList(APIView):
    def get(self,request):
        values = Register.objects.all()
        Serializer = LoginSerializer(values, many= True)
        return Response(Serializer.data)

def json(request): # rendering json type data
    data= {1:{'Name': 'Pankush', 'Age': 29}, 2: { 'Name': 'Aashi', 'Age': 30 }}
    return JsonResponse(data)
