import os
import sys
import numpy as np
from PIL import Image


# Function that creates stego image
def create_stego_image(src, message_file, dest):

    # Given Image path
    img = Image.open(src, 'r')
    # Image width and height
    width, height = img.size
    # Convert image to pixel array
    array = np.array(list(img.getdata()))

    # Determine if RGB( 3 color channels) or RGBA(4 channels) image
    if img.mode == 'RGB':
        n = 3
        m = 0
    elif img.mode == 'RGBA':
        n = 4
        m = 1

    # Total number of pixels
    total_pixels = array.size
    total_pixels_triples = array.size//n

    # Add delimiter to the secret message, in order to know when to stop decoding
    f = open(message_file, 'r')
    message = f.read()
    message += "T0G@NETW0RK$"
    # convert to binary
    b_message = ''.join([format(ord(i), "08b") for i in message])
    # size of the massage in binary
    req_pixels = len(b_message)

    # Determine if the host image has enough space for the secret data
    if req_pixels > total_pixels:
        print("ERROR: image too small...")
    else:
        index = 0
        # Embed the secret bit in the lsb of the host
        for p in range(total_pixels_triples):
            for q in range(m, n):
                if index < req_pixels:
                    t = int(b_message[index])
                    t1 = (array[p][q] & ~1) | t
                    array[p][q] = t1
                    index += 1

        # create new image and save the stego file
        array = array.reshape(height, width, n)
        stego_img = Image.fromarray(array.astype(np.uint8), img.mode)
        stego_img.save(dest)
        print('Stego ready!')


# Function that extracts the secret message from stego image
def extract_stego_image(src):

    # Get stego image pixels and put in array
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    # Determine if RGB( 3 color channels) or RGBA(4 channels) image
    if img.mode == 'RGB':
        n = 3
        m = 0
    elif img.mode == 'RGBA':
        n = 4
        m = 1

    # Total number of pixels
    total_pixels = array.size//n

    # Extract the secret message
    secret_massage = ""
    for p in range(total_pixels):
        for q in range(m, n):
            next = array[p][q]
            next = next & 1
            secret_massage += str(next)

    # Format bits to bytes
    secret_massage = [secret_massage[i:i+8] for i in range(0, len(secret_massage), 8)]

    message = ""
    len_secret = len(secret_massage)
    for i in range(len_secret):
        if message[-12:] == "T0G@NETW0RK$":
            break
        else:
            next_num = int(secret_massage[i], 2)
            message += chr(int(secret_massage[i], 2))

    # Determine if reached the delimiter
    if "T0G@NETW0RK$" in message:
        print("Secret data: ", message[:-12])
    else:
        print("No Stego image")


if __name__ == '__main__':

    print("Lest start creating some stego images...")
    print("Press: 1 - Create stego, 2 - Extract stego")
    input_func = input()

    if input_func == '1':
        print("Please enter Host Image path(BPM or JPG file)")
        src = input()
        # check if file exists
        if not os.path.isfile(src):
            print("File does not exist")
            sys.exit()
        print("Please enter secret message path(txt file)")
        secret = input()
        # check if file exists
        if not os.path.isfile(secret):
            print("File does not exist")
            sys.exit()
        print("Please enter stego image path")
        dest_path = input()
        print("Creating stego image...")
        create_stego_image(src, secret, dest_path)
        print("Done!")
    elif input_func == '2':
        print("Please enter stego image path(BPM or JPF file)")
        src = input()
        print("Extracting secret message...")
        extract_stego_image(src)
        print("Done!")
    else:
        print("Error: Invalid parameter...")
