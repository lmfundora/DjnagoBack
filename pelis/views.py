from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from pelis.models import PelisModel
from pelis.serializers import PelisSerializer, LabelSerializer
import math

# Create your views here.

class Pelis(generics.GenericAPIView):
    serializer_class = PelisSerializer
    queryset = PelisModel.objects.all()


    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        pelis = PelisModel.objects.all()
        total_pelis = pelis.count()
        if search_param:
            pelis = pelis.filter(title__icontains=search_param)
        serializer = self.serializer_class(pelis[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_pelis,
            "page": page_num,
            "last_page": math.ceil(total_pelis / limit_num),
            "pelis": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"peli": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PeliDetail(generics.GenericAPIView):
    queryset = PelisModel.objects.all()
    serializer_class = PelisSerializer

    def get_peli(self, pk):
        try:
            return PelisModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        peli = self.get_peli(pk=pk)
        if peli == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(peli)
        return Response({"status": "success", "data": {"note": serializer.data}})

    def patch(self, request, pk):
        note = self.get_peli(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            note, data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_peli(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)