import yolov5
from django.conf import settings
import os

yolo_weightsdir = settings.YOLOV5_WEIGTHS_DIR
model = yolov5.load(os.path.join(yolo_weightsdir, 'best.pt'))

# 좌석 bbox 저장(순서대로 지정) -(cloth 탐지 안됨 7번좌석)
seat_bbox = [[1.53400e+02, 3.89327e+02, 2.67870e+02, 4.98872e+02],
             [2.62981e+02, 3.98840e+02, 3.76151e+02, 4.86027e+02],
             [3.69372e+02, 4.05868e+02, 4.77888e+02, 4.83721e+02],
             [5.71221e+02, 3.96502e+02, 6.74413e+02, 4.93971e+02],
             [6.69845e+02, 4.02149e+02, 7.74995e+02, 4.85139e+02],
             [7.75539e+02, 3.99870e+02, 8.83480e+02, 4.89714e+02],
             [0.00000e+00, 4.97598e+02, 1.06412e+02, 7.15886e+02],
             [1.08951e+02, 4.98115e+02, 2.85020e+02, 7.04519e+02],
             [2.98685e+02, 5.03596e+02, 4.56541e+02, 7.18624e+02],
             [6.28295e+02, 4.98507e+02, 7.82224e+02, 7.19146e+02],
             [7.98725e+02, 5.04688e+02, 9.60054e+02, 7.05412e+02],
             [9.56734e+02, 5.02194e+02, 1.10400e+03, 7.07798e+02]]

def seat_detection(img_rgb):
    pred = model(img_rgb)

    person_bbox = []
    obj_bbox = []

    print(pred.pandas().xyxy[0])
    # pred.show()

    # 탐지된 객체의 bounding box 좌표 가져오기
    boxes = pred.xyxy[0][:, :].cpu()
    classes = pred.xyxy[0][:, -1]

    for i in range(len(boxes)):
        if boxes[i][5] == 0:
            person_bbox.append(boxes[i][:4])
        else:
            obj_bbox.append(boxes[i][:4])

    seat_status = {}

    # seat와 겹치는 영역과 물체의 영역 계산
    for i in range(len(seat_bbox)):
        seat_status[i + 1] = 'EMPTY'

        for j in range(len(person_bbox)):
            # 사람과 seat 겹치는 영역
            intersection_person_area = max(0, min(person_bbox[j][2], seat_bbox[i][2]) - max(person_bbox[j][0],
                                                                                            seat_bbox[i][0])) * \
                                       max(0, min(person_bbox[j][3], seat_bbox[i][3]) - max(person_bbox[j][1],
                                                                                            seat_bbox[i][1]))
            # 사람 bbox 영역
            box_person_area = (person_bbox[j][2] - person_bbox[j][0]) * (person_bbox[j][3] - person_bbox[j][1])
            # 값 확인
            # print('seat', i+1, 'person', j, 'intersection_person_area: ', intersection_person_area , 'box_person_area: ', box_person_area)

            # 겹치는 영역/탐지 bbox 영역 비율로 seat 상태 정의
            # 사람은 많이 겹치기 때문에 높여도 될 것 같긴 함
            if (intersection_person_area / box_person_area >= 0.5):
                seat_status[i + 1] = 'USE'
                break

        for k in range(len(obj_bbox)):
            if seat_status[i + 1] == 'USE':
                break
            # 짐과 seat 겹치는 영역
            intersection_obj_area = max(0,
                                        min(obj_bbox[k][2], seat_bbox[i][2]) - max(obj_bbox[k][0], seat_bbox[i][0])) * \
                                    max(0, min(obj_bbox[k][3], seat_bbox[i][3]) - max(obj_bbox[k][1], seat_bbox[i][1]))
            # 짐 bbox 영역
            box_obj_area = (obj_bbox[k][2] - obj_bbox[k][0]) * (obj_bbox[k][3] - obj_bbox[k][1])

            # 값 확인
            # print('seat', i+1,'obj', k, 'intersection:', intersection_obj_area, 'box_obj_area:', box_obj_area, 'intersection_obj_area / box_obj_area: ', intersection_obj_area / box_obj_area)

            # 겹치는 영역/탐지 bbox 영역 비율로 seat 상태 정의
            # 아이패드가 작아서 짐 thredhold 0.1 설정
            if (intersection_obj_area / box_obj_area >= 0.1):
                seat_status[i + 1] = 'PRIVATE'
                break

    return seat_status


