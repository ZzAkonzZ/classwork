from django.urls import path, re_path
from bboard.views import index, by_rubric, BbCreateView, form_example, l20_e1

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
    re_path(r'^(?P<page_num>[0-9]/)?$', index, name="index"),
    path('form-example/', form_example, name='form-example'),
    path('lesson-20/example-1', l20_e1, name='l20-e1'),
]