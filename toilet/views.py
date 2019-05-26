from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from os import chdir


file_path = "toilet.csv"
#from .models import 
# Create your views here.

def index(request):
    with open("toilet/toilet.csv", 'r') as f:
        for row in f:
            lux = row
        return render(request, 'toilet/index.html',
                     {'time': lux.split(',')[0],
                      'is_exist': lux.split(',')[1]})


def papirus(request):
    time = request.POST["time"]
    lux = request.POST["lux"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + lux)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()
    #return render(request, 'toilet/index.html')