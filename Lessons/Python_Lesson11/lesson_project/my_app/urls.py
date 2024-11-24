from django.urls import path, re_path
from my_app.views import index, get_bboard, bboard_create

urlpatterns = [
    re_path(r"index/.+$", index),
    path("index",index),
    # path("index",lambda: None),
    path("bboard/<int:bboard_id>/", get_bboard),
    path("bboards_create/", bboard_create),
    re_path(r"^.+$", index),
]