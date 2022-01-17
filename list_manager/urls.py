from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryView, ItemViewDetail, ItembyCategoryView, ItemsView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('list_per_category/<uuid:pk>', ItembyCategoryView.as_view()),
    path('super_list/', ItemsView.as_view()),
    path('super_list/<uuid:pk>', ItemViewDetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
