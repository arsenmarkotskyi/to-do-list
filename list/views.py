from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.urls import reverse_lazy

from list.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, "list/index.html", {"tasks": tasks})


class TagListView(generic.ListView):
    model = Tag
    template_name = "list/tag_list.html"
    context_object_name = "tags"


class TagListCreate(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagListUpdate(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagListDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TaskListDetail(generic.DetailView):
    model = Task
    context_object_name = "tasks"


class TaskListCreate(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:index")


class TaskListUpdate(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:index")


class TaskListDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:index")

class TaskStatusUpdateView(View):
    is_done: bool

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = self.is_done
        task.save()
        return redirect("list:index")


class CompleteTaskView(TaskStatusUpdateView):
    is_done = True


class UndoTaskView(TaskStatusUpdateView):
    is_done = False