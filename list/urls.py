from list.views import index, TagListView, TagListCreate, TagListUpdate, TagListDelete, TaskListCreate, \
    TaskListUpdate, TaskListDelete, TaskListDetail, complete_task, undo_task
from django.urls import path

app_name = 'list'

urlpatterns = [
    path('', index, name='index'),
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('tag/create/', TagListCreate.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagListUpdate.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagListDelete.as_view(), name='tag-delete'),
    path('task/create/', TaskListCreate.as_view(), name='task-create'),
    path('task/<int:pk>/detail/', TaskListDetail.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', TaskListUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskListDelete.as_view(), name='task-delete'),
    path('task/<int:pk>/complete/', complete_task, name='task-complete'),
    path('task/<int:pk>/undo/', undo_task, name='task-undo'),

]