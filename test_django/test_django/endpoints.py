from urllib import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
import os



@api_view(['GET'])
def get_test(request):
     return JsonResponse({"success": True, "data": "everything is working"})


