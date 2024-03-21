# pip install imageai
# pip install torch torchvision tensorflow

from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()

detector.setModelPath("assets/yolov3.pt")
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    input_file_path="assets/tokyo.mp4",
    output_file_path="output/tokyo",
    frames_per_second=20,
    log_progress=True,
)
video_path
