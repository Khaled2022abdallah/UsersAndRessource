import json
import uuid
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from testapp.models import *


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data['name']
        job = data['job']
        user = Users(first_name=name, job=job)
        user.save()
        my_data = user.serializePOST()
    elif request.method == "GET":
        data = list(Users.objects.all().values("id", "email", "first_name", "last_name", "avatar"))
        support = list(Users.objects.all().values("urlSupport","textSupport"))
        my_data = {"data": data, "support": support}
    elif request.method == "PUT":
        data = json.loads(request.body)
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        avatar = data['avatar']
        urlSupport = data['url']
        text = data['text']
        if Users.objects.filter(first_name=first_name).exists():
            posts = Users.objects.get(first_name=first_name)
            my_data = {"data": posts.serialize(), "support": posts.serialize2()}
        else:
            user = Users(email=email, first_name=first_name, last_name=last_name, avatar=avatar, urlSupport=urlSupport,
                         textSupport=text)
            user.save()
            my_data = {"data": user.serialize(), "support": user.serialize2()}

    return JsonResponse(my_data)


@csrf_exempt
def checkUsers(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        name = data['name']
        job = data['job']
        user = Users(first_name=name, job=job)
        user.save()
        my_data = user.serializePUT()
    elif request.method == "PATCH":
        data = json.loads(request.body)
        name = data['name']
        job = data['job']
        user = Users(first_name=name, job=job)
        user.save()
        my_data = user.serializePUT()
    elif request.method == "DELETE":
        Users.objects.all().delete()
        my_data = {}
    elif Users.objects.filter(id=pk).exists():
        posts = Users.objects.get(id=pk)
        my_data = {"data": posts.serialize(), "support": posts.serialize2()}
    else:
        my_data = {}
    return JsonResponse(my_data)


@csrf_exempt
def resource(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data['name']
        year = data['year']
        color = data['color']
        pantone_value = data['pantone_value']
        urlSupport = data['url']
        text = data['text']
        user_id = data['id_user']
        resource = Resource(name=name, year=year, color=color, pantone_value=pantone_value,
                            urlSupport=urlSupport, textSupport=text, user_id=user_id)
        resource.save()
        my_data = {"data": resource.serialize(), "support": resource.serialize2()}
    elif request.method == "GET":
        data = list(Resource.objects.all().values("id", "name", "year", "color", "pantone_value"))
        support = list(Resource.objects.all().values("urlSupport", "textSupport"))
        my_data = {"data": data, "support": support}
    return JsonResponse(my_data)


def checkResource(request, pk):
    if Resource.objects.filter(id=pk).exists():
        posts = Resource.objects.get(id=pk)
        my_data = {"data": posts.serialize(), "support": posts.serialize2()}
    else:
        my_data = {}
    return JsonResponse(my_data)


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if password == "":
            my_data = {'error': 'Missing password!!'}
        else:
            user = User.objects.create_user(username=username, password=password)
            user_token = UserToken.objects.create(user=user, token=uuid.uuid4())
            user.save()
            my_data = {"id": user_token.id, "token": user_token.token}

    return JsonResponse(my_data)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = auth.authenticate(request,
                                 username=username,
                                 password=password)
        if user:
            value_token = UserToken.objects.get(user=user)
            my_data = {"token": value_token.token}
        else:
            my_data = {'error': 'Missing password!!'}
    return JsonResponse(my_data)


@csrf_exempt
def getResource(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data["user_id"]
        if Resource.objects.filter(user_id=user_id).exists():
            posts = Resource.objects.get(user_id=user_id)
            my_data = {"data": posts.serialize(), "support": posts.serialize2()}
        else:
            my_data = {}
        return JsonResponse(my_data)


@csrf_exempt
def getUser(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data["user_id"]
        if Users.objects.filter(id=user_id).exists():
            posts = Users.objects.get(id=user_id)
            my_data = {"data": posts.serialize(), "support": posts.serialize2()}
        else:
            my_data = {}
        return JsonResponse(my_data)
