from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from src.serializers.outlet_serializers import OutletSerializer, ReadOnlyOutletSerializer, FoodSerializer, \
    ReadOnlyFoodSerializer, ReadOnlyCommentSerializer, StarSerializer, ReadOnlyStarSerializer, CommentSerializer,\
    UpdateCommentSerializer
from src.services.outlet.outlet_service import OutletService
from src.services.outlet.food_service import FoodService


class CreateOutletAPIView(CreateAPIView):
    serializer_class = OutletSerializer
    outlet_service = OutletService()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            image = request.FILES.get('image')
            data = serializer.data
            data['image'] = image
            data['user'] = request.user
            outlet = self.outlet_service.create_outlet(kwargs=data)
            self.serializer_class = ReadOnlyOutletSerializer
            serialized_data = self.serializer_class(outlet)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class OutletsAPIView(ListAPIView):
    serializer_class = ReadOnlyOutletSerializer
    queryset = OutletService().get_all_outlets()

    def get_queryset(self):
        return self.queryset


class OutletAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OutletSerializer
    outlet_service = OutletService()
    queryset = outlet_service.get_all_outlets()
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            if self.request.data.get('image'):
                outlet_id = self.kwargs.get('id')
                self.outlet_service.delete_outlet_logo(id=outlet_id)
        self.serializer_class = ReadOnlyOutletSerializer
        return self.queryset.filter()


class FoodCreateAPIView(CreateAPIView):
    serializer_class = FoodSerializer
    food_service = FoodService()
    outlet_service = OutletService()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            image = request.FILES.get('image')
            data = serializer.data
            data['image'] = image
            outlet = self.outlet_service.get_user_outlet(request.user.id)
            print(outlet)
            data['outlet'] = outlet
            food = self.food_service.create_food(kwargs=data)
            self.serializer_class = ReadOnlyFoodSerializer
            serialized_data = self.serializer_class(food)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class FoodsAPIView(ListAPIView):
    serializer_class = ReadOnlyFoodSerializer
    queryset = FoodService().get_all_foods()

    def get_queryset(self):
        return self.queryset


class FoodAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = FoodService().get_all_foods()
    food_service = FoodService()
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            if self.request.data.get('image'):
                food_id = self.kwargs.get('id')
                self.food_service.delete_food_image(id=food_id)
        self.serializer_class = ReadOnlyFoodSerializer
        return self.queryset.filter()


class FoodRatingAPIView(CreateAPIView):
    serializer_class = StarSerializer
    food_service = FoodService()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            rating = self.food_service.add_food_rating(user=request.user.id, value=data.get('value'), food=data.get('food'))
            self.serializer_class = ReadOnlyStarSerializer
            serialized_data = self.serializer_class(rating)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class FoodRatingsAPIView(ListAPIView):
    serializer_class = ReadOnlyStarSerializer
    food_service = FoodService()

    def get_queryset(self):
        food = self.kwargs.get('id')
        queryset = self.food_service.get_food_ratings(food=food)
        return queryset


class CommentsAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    food_service = FoodService()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            comment = self.food_service.create_food_comment(user=request.user, desc=data.get('description'),
                                                            food=data.get('food'))
            self.serializer_class = ReadOnlyCommentSerializer
            serialized_data = self.serializer_class(comment)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class FoodCommentsAPIView(ListAPIView):
    serializer_class = ReadOnlyCommentSerializer
    food_service = FoodService()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        food = self.kwargs.get('id')
        queryset = self.food_service.get_food_comments(food=food)
        return queryset


class FoodCommentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateCommentSerializer
    queryset = FoodService().get_all_comments()
    lookup_field = 'id'

    def get_queryset(self):
        self.serializer_class = ReadOnlyCommentSerializer
        return self.queryset.filter()
