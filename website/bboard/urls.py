from django.urls import path, re_path
from bboard.views import index, by_rubric, BbCreateView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
    re_path(r'^(?P<page_num>[0-9]/)?$', index, name="index"),
]