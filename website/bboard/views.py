from django.http import HttpResponse
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

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics': rubrics}
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