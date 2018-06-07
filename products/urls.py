from products.views import ProductCRUD, UpdateSetProducts, PaginationView
from django.conf.urls import url
from django.urls import include
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'product_crud', ProductCRUD)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^update-set-products/', UpdateSetProducts.as_view()),
    url(r'^pagination-list/', PaginationView.as_view()),
    url(r'^login/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
