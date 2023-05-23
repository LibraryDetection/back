from django.shortcuts import render
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import APIView
# from rest_framework import generics
# from rest_framework import mixins
# from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt  # CSRF 보안 임시 해제
from django.utils.decorators import method_decorator
from .stringToRGB import stringToRGB
from django.http import JsonResponse


#CRUD 한 번에 처리
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@method_decorator(csrf_exempt, name='dispatch')
def upload_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('data')
        rgb = stringToRGB(image_url.split(',')[1])
        # todo 모델 가져오기 및 감지해야 함
        print(rgb)
        return JsonResponse({'message': '데이터가 성공적으로 전송되었습니다.'})
    else:
        return JsonResponse({'message': 'POST 요청이 아닙니다.'}, status=400)

'''
class StuNumViewSet(viewsets.ViewSet):
    #GET
    def list(self, request):
        reacts = React.objects.all()
        serializer = ReactSerializer(reacts, many=True)
        return Response(serializer.data)
    
    #POST
    def create(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #GET specific item
    def retrieve(self, request, pk=None):
        queryset = React.objects.all()
        react = get_object_or_404(queryset, pk=pk)
        serializer = ReactSerializer(react)
        return Response(serializer.data)
    
    #UPDATE
    def update(self, request, pk=None):
        react = React.objects.get(pk=pk)

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    def destroy(self, request, pk=None):
        react = React.objects.get(pk=pk)
        react.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''

'''
class StuNum(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = React.objects.all()
    serializer_class = ReactSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
'''

'''
class StuNum(APIView):
    def get(self, request):
        reacts = React.objects.all()
        serializer = ReactSerializer(reacts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''    