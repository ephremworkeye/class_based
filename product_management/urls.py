from django.urls import path
from .views import ProductRecordFormView, FormSuccessView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('new_record', ProductRecordFormView.as_view(), name="book_record" ),
    path('entry_success', FormSuccessView.as_view(), name="form_success" ),
    path('product_record_create', ProductCreateView.as_view(), name='product_create'),
    path('product_record_update/<int:pk>', ProductUpdateView.as_view(), name='product_update')
]