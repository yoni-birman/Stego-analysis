# Stego-analysis

LSB steganography <h1>

Steganography is the practice of concealing data (the secret) inside other data (cover) such that hidden data cannot be noticed by an unaware party. In presentation, we demonstrated   LSB steganography, where the secret data is encoded into and communicated in one or several least significant bits of the cover image. This could the LSB of the pixel's values of the cover image, defined as spatial domain steganography. 
Alternatively, there are images formats such JPEG, where the image is represented by frequencies, using one of several possible transforms (DCT, DWT, etc). When the LSBs of the secret message are embedded in coefficients of frequencies of the cover image, it is defined as frequency domain steganography. 
During the presentation, we secretly embedded the content of six books in the background of the live presentation.

This the cover image:

This the secret data:

It can be seen that the cover image is gradually distorted with embedding of the data:

Finally, with the embedding of the 6 books the distortion is noticeable:
