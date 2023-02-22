import cv2
import matplotlib.pyplot as plt


def convert_to_greyscale(image):
    greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return greyscale_image

def invert_image(image_to_invert):
    inverted_image = cv2.bitwise_not(image_to_invert)
    return inverted_image


def blur_image(inverted_image):
    blurred_image = cv2.GaussianBlur(inverted_image, (21,21), 0)
    return blurred_image

def display_image(image):
    RGB_converted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(RGB_converted)
    plt.axis(False)
    plt.show()

def display_sketch(output_file, sketched_image):
    cv2.imshow(output_file, sketched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_photo(image_file):
    image = cv2.imread(image_file)
    return image


def sketch(greyscale_image, inverted_blurred_image):
    sketched_image = cv2.divide(greyscale_image, inverted_blurred_image, scale=256.0)
    return sketched_image

def save_sketch(output_file, sketched_image):
    cv2.imwrite(output_file, sketched_image)

def display(original_image, sketched_image):
    # Original Image Shown
    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(original_image)
    plt.axis('off')

    # Sketched Image Shown
    plt.subplot(1,2,2)
    plt.title('Sketch', size=18)
    rgb_sketch=cv2.cvtColor(sketched_image, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()




def main():

    # Get image file path from user
    image_file = input("Enter file to pencilize: ")

    # Get sketch output file path from user
    output_file = input("\nEnter the name of the filename for the sketch output:  ")

    # Read the photo using opencv
    image = read_photo(image_file)

    # Convert the image to greyscale
    greyscale_image = convert_to_greyscale(image)

    # Invert the greyscaled image
    inverted_image = invert_image(greyscale_image)

    # Blur the inverted image
    blurred_image = blur_image(inverted_image)

    # Invert the blurred image
    inverted_blurred_image = invert_image(blurred_image)

    # Sketch the image by using the greyscaled image and the inverted blurred image
    sketched_image = sketch(greyscale_image, inverted_blurred_image)

    # Save the sketch to the user's storage
    save_sketch(output_file, sketched_image)

    # Display the original image and the sketch
    display(image, sketched_image)

if __name__ == "__main__":
    main()