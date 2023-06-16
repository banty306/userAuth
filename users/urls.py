from django.urls import include, re_path
from django.urls import path
from users.views import TemplateView

urlpatterns = [
    re_path(r'^user/conversation/create', TemplateView.as_view())

]
