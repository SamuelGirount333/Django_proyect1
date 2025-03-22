from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> Bienvenido a little lemon! </h1>")

def index(request):
    path = request.path
    method = request.method
    content = '''
<center>
<h2>Testing Django Request Response Objects</h2>
<p>Request path : " {}</p>
<p>Request Method :{}</p>
</center>
'''.format(path, method)
    return HttpResponse(content)

def pathview(request, name, id):
    return HttpResponse('Name: {} UserID: {}'.format(name, id))


def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {} UserID: {}".format(name, id))