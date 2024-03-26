from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    dict_content={'view_content':'This text from views.py'}
    return render(req,'first_app/index.html',context=dict_content)