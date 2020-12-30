from django.urls import path
from . import views
"""hérna má koma punktur eða blog því þetta er inni í blog projectinu """

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
