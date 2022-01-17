
from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Items
from .serializers import CategorySerializer,ItemsSerializer, PostItemsSerializer


class CategoryView(APIView):

    def get(self, request):
        items = Category.objects.all()
        serialized_data = CategorySerializer(items, many=True)

        return Response(
            dict(
                sucess=True,
                data=serialized_data.data
            ),
            status=status.HTTP_200_OK
        )

    def post(self, request):

        serializer = CategorySerializer(data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                dict(
                    succes=True,
                    data=serializer.data
                ),
                status=status.HTTP_201_CREATED
            )

        return Response(
            dict(
                succes=False,
                errors=serializer.errors,
            ),
            status=status.HTTP_400_BAD_REQUEST
        )


class ItembyCategoryView(APIView):

    def get(self, request, pk):

        items = Items.objects.filter(
            category_id=pk
        )
        print(items.values())
        serialized_data = ItemsSerializer(items, many=True)

        return Response(
            dict(
                success=True,
                data=serialized_data.data
            ), status=status.HTTP_200_OK
        )


class ItemsView(APIView):

    def get(self, request):
        items = Items.objects.all()
        serialized_data = ItemsSerializer(items, many=True)

        return Response(
            dict(
                sucess=True,
                data=serialized_data.data
            ),
            status=status.HTTP_200_OK
        )

    def post(self, request):

        serializer = PostItemsSerializer(data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                dict(
                    succes=True,
                    data=serializer.data
                ),
                status=status.HTTP_201_CREATED
            )

        return Response(
            dict(
                succes=False,
                errors=serializer.errors,
            ),
            status=status.HTTP_400_BAD_REQUEST
        )


class ItemViewDetail(APIView):

    def get(self, request, pk):

        item = Items.objects.filter(
            pk=pk
        ).first()

        serialized_data = ItemsSerializer(item)

        return Response(
            dict(
                success=True,
                data=serialized_data.data
            )
        )

    def put(self, request, pk):

        item = Items.objects.filter(
            pk=pk
        ).first()

        serialized_data = ItemsSerializer(
            item, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(
                dict(
                    success=True,
                    data=serialized_data.data
                ),
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            dict(
                success=False,
                errors=serialized_data.errors(),
            ),
            status=status.HTTP_400_BAD_REQUEST
        )
