from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord
from . import forms
# Create your views here.
def index(req):
    webpg_data=AccessRecord.objects.order_by('date')
    dict_content={'access_records':webpg_data}
    return render(req,'first_app/index.html',context=dict_content)
def form_view(req):
    form=forms.FormName()
    if req.method=='POST':
        form=forms.FormName(req.POST)
        if form.is_valid():
            print('Validation Success!!')
            print('Name:'+form.cleaned_data['name'])
            print('Email:'+form.cleaned_data['email'])
            print('Description:'+form.cleaned_data['description'])

    return render(req,'first_app/form.html',context={'form':form})
