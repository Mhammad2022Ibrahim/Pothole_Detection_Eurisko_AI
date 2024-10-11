from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('Models/yolov8_fine_tuning.pt')

model2 = YOLO('Models/yolov11_fine_tuning.pt')
# results = model('test/1 (78).mp4', save=True, show=True)
# results = model('test/test_M3.webp', save=True, show=True)
# results = model('test/test_M4.jpg', save=True, show=True)

# results = model('test/3.mp4', conf=0.7, iou=0.7, save=True, show=True)

results = model2('test/p.mp4', conf=0.7, iou=0.6, save=True, show=True)