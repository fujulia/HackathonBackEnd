from rest_framework import mixins, parsers, viewsets

from uploader.models import Document, Image
from uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer


class CreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all() #  pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,  # Permite exclusão
                         viewsets.GenericViewSet):
    queryset = Image.objects.all()  # Consulta todas as imagens
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]