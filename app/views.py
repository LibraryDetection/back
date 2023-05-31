from django.shortcuts import render
from .models import Reservation, DummyModel
from .serializers import ReservationSerializer, DummyModelSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt  # CSRF 보안 임시 해제
from django.utils.decorators import method_decorator
from .stringToRGB import stringToRGB
from django.http import JsonResponse
import os
from django.conf import settings
import yolov5

yolo_weightsdir = settings.YOLOV5_WEIGTHS_DIR

model = yolov5.load(os.path.join(yolo_weightsdir, 'best.pt'))

#CRUD 한 번에 처리
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class DummyModelViewSet(viewsets.ModelViewSet):
    queryset = DummyModel.objects.all()
    serializer_class = DummyModelSerializer

    def get(self, request):
        dummy = DummyModel.objects.all()
        serializer = DummyModelSerializer(dummy, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
def upload_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('data')
        rgb = stringToRGB(image_url.split(',')[1])
        results = model(rgb)
        df = results.pandas().xyxy[0]
        # print(df) # 탐지 결과 출력
        # results.show() # 탐지 결과 이미지 띄우기
        # todo 모델 가져오기 및 감지해야 함
        name_dict = {}
        for i in df['name'].unique():
            name_dict[i] = len(df.loc[df['name'] == i])
        # DummyModel DB update
        for i in df['name'].unique():
            update_dummy = DummyModel.objects.get(className=i)
            update_dummy.classCount = name_dict[i]
            update_dummy.save()
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
