import math

import numpy as np
from PIL import Image
from skimage import color, io


def load(image_path):
    """Loads an image from a file path.

    HINT: Look up `skimage.io.imread()` function.

    Args:
        image_path: file path to the image.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    out = io.imread(image_path)

    ### YOUR CODE HERE
    # Use skimage io.imread
    ### END YOUR CODE

    # Let's convert the image to be between the correct range.
    out = out.astype(np.float64) / 255
    return out


def dim_image(image):
    """Change the value of every pixel by following

                        x_n = 0.5*x_p^2

    where x_n is the new value and x_p is the original value.

    Args:
        image: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = np.zeros(shape=(image.shape[0],image.shape[1],image.shape[2]))
    

    ### YOUR CODE HERE
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                out[i][j][k] = 0.5*(image[i][j][k])**2
    ### END YOUR CODE

    return out


def convert_to_grey_scale(image):
    """Change image to gray scale.

    HINT: Look at `skimage.color` library to see if there is a function
    there you can use.

    Args:
        image: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width).
    """
    out = color.rgb2gray(image)

    ### YOUR CODE HERE
    ### END YOUR CODE

    return out


def rgb_exclusion(image, channel):
    """Return image **excluding** the rgb channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "R", "G" or "B".

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    
    out = image
    dic = {"R":0,"G":1,"B":2}
    red = image[:,:,0]
    red = red.reshape(image.shape[0],image.shape[1],1)
    green = image[:,:,1]
    green = green.reshape(image.shape[0],image.shape[1],1)
    blue = image[:,:,2]
    blue = blue.reshape(image.shape[0],image.shape[1],1)
    black = np.zeros(shape=(image.shape[0],image.shape[1],1))
    if(channel=='R'):
        out = np.append(np.append(black,green,axis=2),blue,axis=2)
    elif(channel=='G'):
        out = np.append(np.append(red,black,axis=2),blue,axis=2)
    else:
        out = np.append(np.append(red,green,axis=2),black,axis=2)
      ### YOUR CODE HERE
#     ### END YOUR CODE
    #out = None
    return out


def lab_decomposition(image, channel):
    """Decomposes the image into LAB and only returns the channel specified.

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "L", "A" or "B".

    Returns:
        out: numpy array of shape(image_height, image_width).
    """

    lab = color.rgb2lab(image)
    L = lab[:,:,0]
    L = L.reshape(image.shape[0],image.shape[1],1)
    A = lab[:,:,1]
    A = A.reshape(image.shape[0],image.shape[1],1)
    B = lab[:,:,2]
    B = B.reshape(image.shape[0],image.shape[1],1)
    black = np.zeros(shape=(image.shape[0],image.shape[1],1))
    if(channel=='L'):
        out = np.append(np.append(L,black,axis=2),black,axis=2)
    elif(channel=='A'):
        out = np.append(np.append(black,A,axis=2),black,axis=2)
    else:
        out = np.append(np.append(black,black,axis=2),B,axis=2)
    return out


def hsv_decomposition(image, channel='H'):
    """Decomposes the image into HSV and only returns the channel specified.

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "H", "S" or "V".

    Returns:
        out: numpy array of shape(image_height, image_width).
    """

    lab = color.rgb2hsv(image)
    L = lab[:,:,0]
    L = L.reshape(image.shape[0],image.shape[1],1)
    A = lab[:,:,1]
    A = A.reshape(image.shape[0],image.shape[1],1)
    B = lab[:,:,2]
    B = B.reshape(image.shape[0],image.shape[1],1)
    black = np.zeros(shape=(image.shape[0],image.shape[1],1))
    if(channel=='H'):
        out = np.append(np.append(L,black,axis=2),black,axis=2)
    elif(channel=='S'):
        out = np.append(np.append(black,A,axis=2),black,axis=2)
    else:
        out = np.append(np.append(black,black,axis=2),B,axis=2)

    return out


def mix_images(image1, image2, channel1, channel2):
    """Combines image1 and image2 by taking the left half of image1
    and the right half of image2. The final combination also excludes
    channel1 from image1 and channel2 from image2 for each image.

    HINTS: Use `rgb_exclusion()` you implemented earlier as a helper
    function. Also look up `np.concatenate()` to help you combine images.

    Args:
        image1: numpy array of shape(image_height, image_width, 3).
        image2: numpy array of shape(image_height, image_width, 3).
        channel1: str specifying channel used for image1.
        channel2: str specifying channel used for image2.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out


def mix_quadrants(image):
    """THIS IS AN EXTRA CREDIT FUNCTION.

    This function takes an image, and performs a different operation
    to each of the 4 quadrants of the image. Then it combines the 4
    quadrants back together.

    Here are the 4 operations you should perform on the 4 quadrants:
        Top left quadrant: Remove the 'R' channel using `rgb_exclusion()`.
        Top right quadrant: Dim the quadrant using `dim_image()`.
        Bottom left quadrant: Brighthen the quadrant using the function:
            x_n = x_p^0.5
        Bottom right quadrant: Remove the 'R' channel using `rgb_exclusion()`.

    Args:
        image1: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    out = None

    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out
