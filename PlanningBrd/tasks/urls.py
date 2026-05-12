from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tasks/", views.task_list, name="task_list"),
    path("create/", views.create_task, name="create_task"),
    path("create/<int:project_id>/", views.create_task, name="create_task_for_project"),
    path("<int:pk>/edit/", views.edit_task, name="edit_task"),
    path("<int:pk>/delete/", views.delete_task, name="delete_task"),
    path("<int:pk>/toggle/", views.toggle_task_completed, name="toggle_task_completed"),
    path("<int:pk>/", views.task_detail, name="task_detail"),

    path("projects/", views.project_list, name="project_list"),
    path("projects/create/", views.create_project, name="create_project"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("projects/<int:pk>/edit/", views.edit_project, name="edit_project"),
    path("projects/<int:pk>/delete/", views.delete_project, name="delete_project"),
    path("projects/<int:pk>/toggle-completed/", views.toggle_project_completed, name="toggle_project_completed"),
    path("create-project-from-calendar/", views.create_project_from_calendar, name="create_project_from_calendar"),
    path("settings/", views.user_settings, name="user_settings"),
    
    path("calendars/", views.calendar_view, name="calendar_list"),
    path("calendars/create/", views.create_calendar, name="create_calendar"),

    path("calendar-view/", views.calendar_view, name="calendar_view"),
    path("calendar-events/", views.calendar_events, name="calendar_events"),
    path("todos/", views.todo_list, name="todo_list"),
    path("todos/create/", views.create_todo, name="create_todo"),
    path("todos/<int:pk>/edit/", views.edit_todo, name="edit_todo"),
    path("todos/<int:pk>/delete/", views.delete_todo, name="delete_todo"),
    path("todos/<int:pk>/toggle/", views.toggle_todo_completed, name="toggle_todo_completed"),

]
