import cv2

# Load the image
image = cv2.imread('C:/Users/roope/thug duck.jpeg')

if image is not None:
    #convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #invert the image
    inverted_image = cv2.bitwise_not(gray_image)
    #blur the image
    blurred_image = cv2.GaussianBlur(inverted_image, (21,21), 0)
    #invert the image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    #combine gray and blurred image
    final_image = cv2.divide(gray_image, inverted_blurred_image, scale=237.0)

    #save the image
    cv2.imwrite('output.jpeg', final_image)
    print("done")

