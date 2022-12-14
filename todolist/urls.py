from django.urls import path
from todolist.views import delete_task, new_todolist, show_todolist, register, login_user, logout_user, status_change, get_data_json, new_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('create-task/', new_todolist, name = 'new_todolist'),
    path('delete-task/<int:id>', delete_task, name = 'delete_task'),
    path('status-change/<int:id>', status_change, name = 'status_change'),
    path('json/', get_data_json, name="get_data_json"),
    path('add/', new_todolist_ajax, name="new_todolist_ajax" ),
]