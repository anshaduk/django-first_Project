from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord
# Create your views here.
def index(req):
    webpg_data=AccessRecord.objects.order_by('date')
    dict_content={'access_records':webpg_data}
    return render(req,'first_app/index.html',context=dict_content)