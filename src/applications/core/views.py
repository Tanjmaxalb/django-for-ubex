import copy

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)
from django.apps import apps

from .serializers import CoreSerializer
from applications.wsgi import application


class CoreListCreateView(ListCreateAPIView):
    def get_queryset(self):
        params = self.get_params_from_request()
        queryset = self.get_model().objects

        order_by = params.pop("order_by", None)
        limit = params.pop("limit", None)
        filters = self.get_filters_by_params(params)

        if filters:
            queryset = queryset.filter(**filters)

        if order_by:
            queryset = queryset.order_by(order_by[0])

        queryset = queryset.all()

        if limit:
            limit = int(limit[0])
            queryset = queryset[:limit]

        return queryset

    def get_model(self):
        app_label = self.kwargs["app_label"]
        model_name = self.kwargs["model_name"]
        model = apps.get_model(app_label, model_name)

        return model

    def get_serializer_class(self):
        class Serializer(CoreSerializer):
            class Meta:
                model = self.get_model()
                fields = self.get_model_fields()

        return Serializer

    def get_model_fields(self):
        return tuple(f.name for f in self.get_model()._meta.get_fields())

    def get_params_from_request(self):
        return copy.copy(self.request.query_params)

    def get_filters_by_params(self, params):
        models_fields = self.get_model_fields()
        result = dict()

        for field in params:
            if field not in models_fields:
                raise NotFound(f"Unknown {field} field")

            result[field] = params[field]

        return result


class CoreDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.get_model().objects.all()

    def get_serializer_class(self):
        class Serializer(CoreSerializer):
            class Meta:
                model = self.get_model()
                fields = self.get_model_fields()

        return Serializer

    def get_model(self):
        app_label = self.kwargs["app_label"]
        model_name = self.kwargs["model_name"]
        model = apps.get_model(app_label, model_name)

        return model

    def get_model_fields(self):
        return tuple(f.name for f in self.get_model()._meta.get_fields())
