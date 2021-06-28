from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ResumebApp.models import Students
from ResumebApp.serializers import StudentSerializer


# Create your views here.
@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        students=Students.objects.all()
        students_serializer=StudentSerializer(students,many=True)
        return JsonResponse(students_serializer.data,safe=False)
    
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added!!",safe= False)
        return JsonResponse("Failed",safe=False)

    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Students.objects.get(StudentId=student_data['StudentId'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated!!",safe=False)
        return JsonResponse("Failed updation!!",safe=False)

    elif request.method=='DELETE':
        student=Students.objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Deleted!!",safe=False)

