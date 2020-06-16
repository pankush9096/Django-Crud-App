from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from . import forms
from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Register
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

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

    def post(self, request):

        # values = self.get_object()
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            json = JSONRenderer().render(serializer.data)
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Update_LoginList(APIView):

    queryset = Register.objects.all()
    serializer_class = LoginSerializer

    def get_object(self, pk):
        try:
            return Register.objects.get(pk=pk)
        except Register.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, pk):
        values = self.get_object(pk)
        Serializer = LoginSerializer(values)
        return Response(Serializer.data)

    def put(self, request, pk):
        values = self.get_object(pk)
        serializer = LoginSerializer(values,data=request.data)
        if serializer.is_valid():
            serializer.save()
            json = JSONRenderer().render(serializer.data)
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        value = self.get_object(pk)
        value.delete()
        values = Register.objects.all()
        serializer = LoginSerializer(values, many= True)
        return Response(serializer.data)


def json(request): # rendering json type data
    data= {1:{'Name': 'Pankush', 'Age': 29}, 2: { 'Name': 'Aashi', 'Age': 30 }}
    return JsonResponse(data)
