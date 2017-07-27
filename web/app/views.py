from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

from app.models import User
from app.APISerializer import UserSerializer

def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

class UserController:
    # request.data (request json data)
    @api_view(['GET'])
    def get(request, idx):
        try:
            user = User.objects.get(idx=idx)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        else:
            return HttpResponse(status=405)
