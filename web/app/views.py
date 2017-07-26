from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import User
from app.APISerializer import UserSerializer

def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

class UserController:
    @api_view(['GET'])
    def get(request, idx):
        try:
            user = User.objects.get(idx=idx)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return HttpResponse(status=405)
