from django.urls import path
from .views import ProductDetailView, ProductRecordFormView, FormSuccessView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('new_record', ProductRecordFormView.as_view(), name="book_record" ),
    path('entry_success', FormSuccessView.as_view(), name="form_success" ),
    path('product_record_create', ProductCreateView.as_view(), name='product_create'),
    path('product_record_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name="product_delete"),
    path('delete_success', FormSuccessView.as_view(), name="form_success" ),
]