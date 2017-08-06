from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from app.models import User
from app.APISerializer import UserSerializer

def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

class UserController:

    @api_view(['POST'])
    def auth(self, request):
        action = request.data['action']
        if(action == None):
            return;
        try:
            result = {
                'signup': self.sign_up(),
                'signin': self.sign_in(),
            }
        except:
            return HttpResponse(status=404)
        return HttpResponse(status=200)

    def sign_up(self):
        return 0
    def sign_in(self):
        return 0

    # request.data (request json data)
    @api_view(['GET'])
    def user(request, idx):
        try:
            user = User.objects.get(idx=idx)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        else:
            return HttpResponse(status=405)
