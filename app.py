from flask import Flask

import torch
from PIL import Image

# Yolov5 모델 초기화
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt', force_reload=True)

app = Flask(__name__)


@app.route('/xxx')
def hello_world():  # put application's code here
    # 이미지 파일 로드
    image_path = 'image1.png'
    image = Image.open(image_path)

    # 이미지 추론
    results = model(image)

    # 추론 결과 파싱
    detections = results.pandas().xyxy[0]
    num_detections = len(detections)

    # 결과 출력

    print(f'Number of detections: {num_detections}')
    print(detections)

    d = detections['name'].tolist()
    c = detections['class'].tolist()

    for food in d:
        print(food.split()[1])

    for cs in c:
        print(cs)



    return 'Hello World!'




if __name__ == '__main__':
    app.run()


# import torch
# from PIL import Image
#
# # Yolov5 모델 초기화
# model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt', force_reload=True)
#
# # # 모델 저장 및 불러오기
# # torch.save(model, 'best.pth')
# #
# #
# # # 학습된 가중치 로드
# # weights_path = 'best.pt'
# # model.load_state_dict(torch.load(weights_path, map_location=torch.device('cpu')), strict=False)
#
# # 이미지 파일 로드
# image_path = 'image1.png'
# image = Image.open(image_path)
#
# # 이미지 추론
# results = model(image)
#
# # 추론 결과 파싱
# detections = results.pandas().xyxy[0]
# num_detections = len(detections)
#
# # 결과 출력
#
# print(f'Number of detections: {num_detections}')
# print(detections)
