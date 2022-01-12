
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Items
from .serializers import CategorySerializer,ItemsSerializer
class CategoryView(APIView):
    
    def get(self,request):
        items = Category.objects.all()
        serialized_data = CategorySerializer(items,many=True)
        
        return Response(
            dict(
                sucess=True,
                data=serialized_data.data
            ),
            status=status.HTTP_200_OK
        )
        
    def post(self,request):
        
        serializer = CategorySerializer(data=requet.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                dict(
                    succes=True,
                    data= serializer.data
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

        serializer = CategorySerializer(data=requet.data,partial=True)
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
