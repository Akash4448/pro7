from django import dispatch
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,'dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs): 
        json_data = request.body
        stream = io.BytesIO(json_data)      #convert (json_data to sterm)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata) #convert ()

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data isss created..'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') 

    def put(self,request,*args,**kwargs): 
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id') 
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'da is updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')    

    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)  
        stu.delete() 
        res = {'msg':'da is deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json') 
        return JsonResponse(res,safe=False)

        # non dict----safe=False
        # dict -----default -- safe=True
        


# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id',None)

#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')

    
#     #----Create-----
    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)      #convert (json_data to sterm)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata) #convert ()

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'data isss created..'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json') 

#      #----Updated-----

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id') 
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'da is updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

#          #----Delete-----

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)  
#         stu.delete() 
#         res = {'msg':'da is deleted'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data,content_type='application/json') 
#         return JsonResponse(res,safe=False)
    

    
