from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc
# Create your views here.


class MainView( TemplateView):
    template_name = 'docs/main.html'

def file_upload_view(request):
    print(request)
    print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        print (my_file)
        Doc.objects.create(upload_to=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})
