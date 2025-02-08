
if __name__ == "__main__":
    model = YOLO("yolov8m.pt")

    results = model("pexels-catherinesheila-2409022.jpg", save=True)