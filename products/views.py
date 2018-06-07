from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, SetProductsSerializer, CatalogSerializer
from .filters import ProductFilter
from .permission import IsAuthenticatedPermission


class ProductCRUD(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProductFilter
    permission_classes = (IsAuthenticatedPermission,)


class UpdateSetProducts(generics.UpdateAPIView):
    serializer_class = SetProductsSerializer
    permission_classes = (IsAuthenticatedPermission,)

    def update(self, request, *args, **kwargs):
        for pr in request.data['products']:
            try:
                pr_queryset = Product.objects.get(pk=pr['id'])
                serializer = ProductSerializer(pr_queryset, data=pr)
                if serializer.is_valid():
                    serializer.save()
            except Product.DoesNotExist:
                pass
        return Response(request.data)


class PaginationView(generics.ListAPIView):
    serializer_class = CatalogSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProductFilter
    permission_classes = (IsAuthenticatedPermission, )
