import cv2
import matplotlib.pyplot as plt


def convert_to_greyscale(image):
    '''
    Function that converts the original image to greyscale
    '''
    greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return greyscale_image


def invert_image(image_to_invert):
    '''
    Function that inverts the image by using bitwise not on the pixels.    
    '''
    inverted_image = cv2.bitwise_not(image_to_invert)
    return inverted_image


def blur_image(inverted_image):
    '''
    Function that takes the inverted image and blurs it using Gaussian Blur.
    '''
    blurred_image = cv2.GaussianBlur(inverted_image, (21,21), 0)
    return blurred_image


def read_photo(image_file):
    '''
    Function that reads the filepath inputted by the user and sets it to the image.
    '''
    image = cv2.imread(image_file)
    return image


def sketch(greyscale_image, inverted_blurred_image):
    '''
    Function that uses the greyscale image and the inverted blurred image to divide 
    and convert to a bit pattern for the sketch.
    '''
    sketched_image = cv2.divide(greyscale_image, inverted_blurred_image, scale=256.0)
    return sketched_image


def save_sketch(output_file, sketched_image):
    '''
    Function that saves the sketched image to the file directory that the user chooses.
    '''
    cv2.imwrite(output_file, sketched_image)


def display(original_image, sketched_image):
    '''
    Function that displays the original and sketched image side-by-side using matplotlib.
    '''
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
    '''
    Entry-point to the program. Takes user input for the image source and sketched image destination.
    Program utilizes CV2 as the main libary to read, convert to greyscale, invert, blur, invert, and sketch.
    '''
    # Get image file path from user
    image_file = input("Enter file to pencilize: ")

    # Get sketch output file path from user
    output_file = input("\nEnter the name of the filename for the sketch output including the file extension (jpg, png, etc): ")

    '''
    Error handling if file inputed is not found.
    '''
    try:
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
    except:
        print("The file requested to pencilize does not exist, please try again with the correct path and extension") 

if __name__ == "__main__":
    main()