from flask import Flask, request
import torch
from PIL import Image

# Yolov5 모델 초기화
model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt', force_reload=True)

app = Flask(__name__)


@app.route('/photo', methods=['POST'])
def recognizePhoto():  # put application's code here
    print(request.headers)
    if 'file' not in request.files:
        return 'No file found in request', 400

    photo = request.files['file']
    image = Image.open(photo)

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

    result = []
    for cs in c:
        result.append(int(cs))

    return result, 200


if __name__ == '__main__':
    app.run()
