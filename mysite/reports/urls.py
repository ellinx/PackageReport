from django.urls import path

from . import views

app_name = "reports"
urlpatterns = [
    # ex: /reports/
    path('', views.index, name='index'),
    # ex: /reports/5/
    path('<int:package_id>/', views.detail, name='detail'),
    # ex: /reports/group/
    path("group/", views.group, name = "group"),
    ### wx api
    path("wx_all", views.wx_all, name = "wx_all"),
    path("wx_update", views.wx_update, name = "wx_update"),
    path("wx_create", views.wx_create, name = "wx_create"),
    path("wx_delete", views.wx_delete, name = "wx_delete"),
]

