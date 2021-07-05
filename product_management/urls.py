from django.urls import path
from .views import ProductRecordFormView, FormSuccessView

urlpatterns = [
    path('new_record', ProductRecordFormView.as_view(), name="book_record" ),
    path('entry_success', FormSuccessView.as_view(), name="form_success" )
]
