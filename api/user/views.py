from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.http import JsonResponse
import random
import re
import string


def generate_session_token(length=10):
    letters = string.ascii_letters + "1234567890"
    token = "".join(random.sample(letters,length))
    return token

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only.'})

    username = request.POST['email']
    password = request.POST['password']

    # Validation Part
    if not re.match("^[\w\.-]+@[\w\.-]+\.\w{2,4}$", username):
        print("username:", username)
        return JsonResponse({'error': 'Enter a valid email.'})

    if len(password) < 8:
        return JsonResponse({'error': 'Password needs to be at least 8 characters.'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()
            user_dict.pop('password')

            if user.session_token != "0":
                user.session_token == "0"
                user.save()
                return JsonResponse({'error': 'Previous Session Exist.'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': user_dict})
        else:
            return JsonResponse({'error': 'Invalid Password.'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email.'})


@csrf_exempt
def signout(request, id):
    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid User ID.'})

    return JsonResponse({'success': 'Logout Successful.'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
