from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def index(request, page_num='1/'):
    template = loader.get_template('bboard/index.html')

    limit = 2
    bbs_per_page = int(page_num[:-1]) * limit

    bbs = Bb.objects.order_by('-published')
    pages = [i for i in range(1, round(len(bbs) / limit) + 1)]
    bbs = bbs[bbs_per_page-limit:bbs_per_page]

    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics': rubrics, 'pages': pages}
    return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    template = loader.get_template('bboard/by_rubric.html')
    bbs = Bb.objects.filter(rubric=rubric_id)
    # rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'current_rubric':current_rubric}
    return HttpResponse(template.render(context, request))

    # bbs = Bb.objects.filter(rubric=rubric_id)
    # rubrics = Rubric.objects.all()
    # current_rubric = Rubric.objects.get(pk=rubric_id)
    # context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric':current_rubric}
    # return render(request, 'bboard/by_rubric.html', context)

def form_example(request):
    if request.method == 'POST':
        # str = '<pre>' + str(request) + '</pre>'
        return HttpResponse(request.POST['name'])
    else:
        template = loader.get_template('bboard/form_example.html')
        return HttpResponse(template.render({}, request))

def l20_e1(request):
    resp = HttpResponse("Здесь будет")
    resp.write(" главная")
    resp.writelines((" страница", " сайта"))
    resp["keywords"] = 'Python, Django'
    return resp

def create_rubric(request):
    if request.method == "POST":
        post = request.POST
        rubric = Rubric(name = post['name'])

        rubric.save()

        return HttpResponseRedirect('/')
    else:
        template = loader.get_template('bboard/create_rubric.html')
        rubrics = Rubric.objects.all()
        return HttpResponse(template.render({'rubrics': rubrics}, request))