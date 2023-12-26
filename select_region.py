import cv2 
import os 
import json 
import sys 

# Initialize list to store points
points = []

def draw_polygon(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

def select_region(image_path):
    global points
    img = cv2.imread(image_path)
    cv2.namedWindow("Select Region")
    cv2.setMouseCallback("Select Region", draw_polygon)

    while True:
        temp_img = img.copy()
        for i in range(len(points)):
            cv2.circle(temp_img, points[i], 3, (0, 0, 255), -1, cv2.LINE_AA)
            if i > 0:
                cv2.line(temp_img, points[i-1], points[i], (0, 255, 0), 3,cv2.LINE_AA)

        cv2.imshow("Select Region", temp_img)
        k = cv2.waitKey(1) & 0xFF

        # Press 'Enter' to finish selecting region
        if k == 13:
            break

    cv2.destroyAllWindows()

    # Save the coordinates
    with open('selected_polygon.json', 'w') as file:
        json.dump(points, file)

if __name__ == "__main__":
    src_img_path = sys.argv[1]
    select_region(src_img_path)  # Replace with your image path

