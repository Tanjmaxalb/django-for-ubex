from django.conf.urls import include, url

from applications.core.views import CoreListCreateView, CoreDetailView


urlpatterns = [
    url(r"^api/(?P<app_label>\w+)/(?P<model_name>\w+)$",
        CoreListCreateView.as_view()),
    url(r"^api/(?P<app_label>\w+)/(?P<model_name>\w+)/(?P<pk>\d+)$",
        CoreDetailView.as_view(), name="detail"),
]
