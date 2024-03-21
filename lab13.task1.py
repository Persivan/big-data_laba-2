# pip install imageai
# pip install torch torchvision tensorflow opencv-python

from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()

path = "assets/retinanet_resnet50_fpn_coco-eeacb38b.pth"
detector.setModelPath(path)
detector.loadModel()



# Вариант 1
list = detector.detectObjectsFromImage(
    input_image="assets/dogs.png", output_image_path="output/dogs1.png"
)


# Вариант 2
# list = detector.detectObjectsFromImage(
#     input_image="assets/dogs.png",
#     output_image_path="output/dogs2.png",
#     minimum_percentage_probability=30,
#     display_percentage_probability=False,
#     display_object_name=False,
# )

