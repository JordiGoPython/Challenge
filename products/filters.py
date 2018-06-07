from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Product


def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class ProductFilter(filters.FilterSet):
    text = filters.CharFilter(name="text", method='filter_search_product')
    pagination = filters.CharFilter(name="pagination", method='filter_pagination')

    def filter_pagination(self, queryset, name, value):
        array_string = value.split(",")
        if array_string and IsInt(array_string[0]) and IsInt(array_string[1]):
            page, page_size = [int(x) for x in value.split(",")]
            start = page_size*(page-1)
            end = start + page_size
            return queryset[start:end]
        return queryset

    def filter_is_variation(self, queryset, name, value):
        active = True
        if value == '1':
            active = False
        return queryset.filter(is_variation=active)

    def filter_search_product(self, queryset, name, value):
        return queryset.filter(Q(name__contains=value) | Q(description__contains=value))

    class Meta:
        model = Product
        fields = ['pagination', 'text', 'is_variation', 'is_complement', 'is_delete', 'is_active']
