import cv2
import numpy as np
import json

def move_mask(target_image_path, mask_points_path, res_path):
    # Load the target image
    target_image = cv2.imread(target_image_path)
    with open(mask_points_path, 'r') as file:
        mask_points = json.load(file)

    # Convert mask_points to a numpy array
    mask_points = np.array(mask_points, dtype=np.int32)

    # Initialize mask position (offsets)
    dx, dy = 0, 0

    while True:
        # Create a copy of the target image to work with
        display_image = target_image.copy()

        # Create a mask using the polygon
        mask = np.ones_like(target_image)
        cv2.fillPoly(mask, [mask_points + [dx, dy]], (255, 255, 255))

        # Invert the mask (so the polygon area is visible, the rest is black)
        inverted_mask = cv2.bitwise_not(mask)

        # Apply the inverted mask to the target image
        result_image = cv2.bitwise_and(display_image, inverted_mask)

        # Show the result in a window
        cv2.imshow("Real-Time Mask Movement", result_image)

        # Capture key press events
        key = cv2.waitKey(1) & 0xFF

        # Handle key press events
        if key == ord("q"):  # Press 'q' to exit
            break
        elif key == ord("w"):  # Press 'w' to move the mask up
            dy -= 10
        elif key == ord("s"):  # Press 's' to move the mask down
            dy += 10
        elif key == ord("a"):  # Press 'a' to move the mask left
            dx -= 10
        elif key == ord("d"):  # Press 'd' to move the mask right
            dx += 10

    # Save the result image
    cv2.imwrite(res_path, result_image)

    # Release OpenCV windows and cleanup
    cv2.destroyAllWindows()

    return (dx, dy)

