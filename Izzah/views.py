from django.http import HttpResponse
from django.template import loader

def Izzah(request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())