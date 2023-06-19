from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('oapp/index.html')
    context = {'oapp': 'oapp'}
    return HttpResponse(template.render(context, request))

