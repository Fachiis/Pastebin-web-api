from django.db.models.query import InstanceCheckMeta
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from .serializers import SnippetSerializer
from api import serializers

class SnippetList(
    mixins.ListModeMixin, 
    mixins.CreateModelMixin, 
    mixins.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIview):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *agrs, **kwargs)
    return self.retrieve(request, *agrs, **kwargs)

    def put(self, request, *agrs, **kwargs):
        return self.update(request, *agrs, **kwargs)

    def delete(self, request, *agrs, **kwargs):
        return self.destroy(request, *agrs, **kwargs)