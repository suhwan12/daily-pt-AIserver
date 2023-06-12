from flask import Flask

import torch
from PIL import Image

# Yolov5 모델 초기화
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt', force_reload=True)

app = Flask(__name__)

#음 나는 이게 맘에 안들어


@app.route('/xxx')
def hello_world():  # put application's code here
    # 이미지 파일 로드
    image_path = '1686225993677_IMG_1077.jpg'
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