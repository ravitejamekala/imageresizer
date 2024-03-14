import cv2

if __name__ == '__main__':
    image = cv2.imread('lambo.jpg')
    height = int(input("Enter new height of the image:  "))
    width = int(input("Enter new width of the image:  "))
    print("original image dimensions", image.shape)
    resized_img = cv2.resize(image, (height, width))
    cv2.imwrite("new_img.jpg", resized_img)
    print("new image dimensions", height, "x", width)
