import cv2

# Initialize variables to store rectangle coordinates
start_point = None
end_point = None
rectangles = []

def draw_rectangle(event, x, y,):
    global start_point, end_point

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        rectangles.append((start_point, end_point))

def select_regions(image_path):
    global rectangles
    img = cv2.imread(image_path)
    cv2.namedWindow("Select Regions")
    cv2.setMouseCallback("Select Regions", draw_rectangle)

    while True:
        temp_img = img.copy()
        for rect in rectangles:
            cv2.rectangle(temp_img, rect[0], rect[1], (0, 255, 0), 2)

        cv2.imshow("Select Regions", temp_img)
        k = cv2.waitKey(1) & 0xFF

        # Press 'Enter' to finish selecting regions
        if k == 13:
            break

    cv2.destroyAllWindows()

    return rectangles