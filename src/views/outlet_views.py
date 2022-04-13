from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from src.serializers.outlet_serializers import OutletSerializer, ReadOnlyOutletSerializer
from src.services.outlet.outlet_service import OutletService


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
            outlet_id = self.kwargs.get('id')
            self.outlet_service.delete_outlet_logo(id=outlet_id)
        self.serializer_class = ReadOnlyOutletSerializer
        return self.queryset.filter()
