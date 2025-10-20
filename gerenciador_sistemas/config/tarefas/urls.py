from django .urls import path
from .imporviews
urlpatterns = [

    path('',views.listar_tarefas, name = 'listar_tarefas')
]