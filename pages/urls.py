from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.page_detail, name="page_detail"
    ),  # slug уже подхвачен из родительского урла
]
