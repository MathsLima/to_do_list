from django.contrib import admin
from django.urls import path


#from todos.views import todo_list
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView


urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", todo_list),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete")
]  
