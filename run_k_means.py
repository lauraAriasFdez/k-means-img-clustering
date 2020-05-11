"""
1. run k means.py.
2.input a ﬁle name for the image to load
3. input the number k of colors
4. input the name of the output ﬁle. 

5. the program should load the image
6. runs k-means clustering on that image,
7. then create a new image where each pixel is replaced with the color speciﬁed by the k-means model (see the pictures on the ﬁrst page for examples of how this might look). This image should then be saved to the ﬁle speciﬁed by the user. Care should be made to have useful prompts so that the correct use of this program is self-evident to users who have not read its source code.
"""

from k_means import k_means
from image_utils import *

# input
filename = input ("File name for the image: ")
k = int(input ("The number of clusters: "))
output_file = input('Name for your output file: ')


#read image
image = read_ppm(filename)

#run k and change image
means,list_of_lists = k_means(image,k)

width, height = get_width_height(image)
for x in range(width):
    for y in range(height):
        r, g, b = means[list_of_lists[x][y]]
        image[x][y] = (r,g,b)
        
#output image
save_ppm(output_file,image)


#REFERENCE TIMING
# UMN picture Medium 4 clusters - 25 seconds
# UMN picture Medium 6 clusters - 1:45
#CIVIL ENGINERIGN LARGE 5 clusters - 2:20

