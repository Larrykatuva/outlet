from django.conf.urls.static import static
from django.urls import path
from src.views.outlet_views import CreateOutletAPIView, OutletsAPIView, OutletAPIView, FoodCreateAPIView, FoodsAPIView,\
    FoodAPIView, FoodRatingAPIView, FoodRatingsAPIView, CommentsAPIView, FoodCommentsAPIView, FoodCommentAPIView
from outlet import settings


urlpatterns = [
    path('create', CreateOutletAPIView.as_view(), name='create-outlet'),
    path('all', OutletsAPIView.as_view(), name="list-outlets"),
    path('outlet/<id>', OutletAPIView.as_view(), name="outlet"),
    path('food/create', FoodCreateAPIView.as_view(), name="create-food"),
    path('food/all', FoodsAPIView.as_view(), name="list-foods"),
    path('food/<id>', FoodAPIView.as_view(), name="food"),
    path('food/rating/create', FoodRatingAPIView.as_view(), name="create-rating"),
    path('food/<id>/ratings', FoodRatingsAPIView.as_view(), name="food-ratings"),
    path('food/comment/create', CommentsAPIView.as_view(), name="create-comment"),
    path('food/comment/<id>', FoodCommentAPIView.as_view(), name="food-comment"),
    path('food/<id>/comments', FoodCommentsAPIView.as_view(), name="food-comments")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
