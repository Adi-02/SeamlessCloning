import cv2

class RegionSelector:
    def __init__(self):
        self.points = []

    def draw_brush(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append((x, y))
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            self.points.append((x, y))

    def select_region(self, image_path):
        img = cv2.imread(image_path)
        cv2.namedWindow("Select Region - Enter to Save")
        cv2.setMouseCallback("Select Region - Enter to Save", self.draw_brush)

        while True:
            temp_img = img.copy()
            for i in range(len(self.points)):
                cv2.circle(temp_img, self.points[i], 3, (0, 0, 255), -1, cv2.LINE_AA)
                if i > 0:
                    cv2.line(temp_img, self.points[i - 1], self.points[i], (0, 255, 0), 3, cv2.LINE_AA)

            cv2.imshow("Select Region - Enter to Save", temp_img)
            k = cv2.waitKey(1) & 0xFF

            # Press 'Enter' to finish selecting region
            if k == 13:
                break

        cv2.destroyAllWindows()
        return self.points

