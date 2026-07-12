from ultralytics import YOLO
import os

# Load the trained model
model = YOLO("model/best.pt")


def detect_defects(image_path):

    results = model.predict(
        source=image_path,
        save=True,
        project="outputs",
        name="prediction",
        exist_ok=True
    )

    result = results[0]

    detections = []

    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        confidence = float(box.conf[0])

        detections.append({
            "defect": class_name,
            "confidence": round(confidence * 100, 2)
        })

    # Use YOLO's actual saved image path
    annotated_image = os.path.join(
        result.save_dir,
        os.path.basename(image_path)
    )

    print("Save Directory:", result.save_dir)
    print("Annotated Image:", annotated_image)
    return annotated_image, detections