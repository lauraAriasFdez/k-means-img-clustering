from image_utils import *

def k_means(image,k):
    """performs a complete k_means computation. In other words creates a list with the main
        cluster in the images and then another list in which each pixel has a number
        representing the cluster they belong to"""
    means = []
    for i in range(k):
        means.append(random_color())

    #computing the first assigment
    list_of_lists = update_assigments(image,means)

    #initial condition for while loop
    update_means (image,list_of_lists,k,means)
    new_list_of_lists = update_assigments(image,means)

    #loop until there is not change for list_of_lists               
    while (new_list_of_lists != list_of_lists):
        list_of_lists = new_list_of_lists
        update_means (image,list_of_lists,k,means)
        new_list_of_lists = update_assigments(image,means)

    return (means,list_of_lists)



def compute_distance(col1,col2):
    """
    PURPOSE: A function to compute the “distance” between two colors using the euclidean distance
        
    PARAMETERS:
            -col1: The tuple representing the r,g,b values of the image pixel
            -col2: the tuple representing the r,g,b values of the cluster
            
    RETURN: The distance(difference) between the 2 colors
    """
    return (((col1[0] - col2[0])**2 + (col1[1] - col2[1])**2 + (col1[2] - col2[2])**2)**.5)

def nearest_centroid (color_pixel, means):
    """
    PURPOSE: A function that computes which of the k centroids does that pixel belog to 
        
    PARAMETERS:
        -color_pixel: a tuple representing the r,g,b values of 1 pixel
        -means: list containign the color of each cluster.
            
    RETURN: An integer representing the cluster that pixel belongs to 
    """
    cluster_number = 0
    distance_min = compute_distance(color_pixel,means[0])
    for i in range (1, len(means)):
        current_distance = compute_distance (color_pixel,means[i])
        if current_distance < distance_min:
            cluster_number = i
            distance_min = current_distance
    return cluster_number



def avg_color (assigned_colors):
    """
    PURPOSE: A function that finds the average color (avg red, avg blue, avg green) given a list of colors
        
    PARAMETERS:
            -assigned_colors: a list of colors(tuple with r,g,b values)
            
    RETURN: A tuple that represents the avg color (r,g,b)
    """
    r = 0
    g = 0
    b = 0
    total_colors = len(assigned_colors)
    
    if (total_colors == 0): #return black as a color
        return (0,0,0)
    
    for color in assigned_colors:
        r += color[0]
        g+= color[1]
        b +=color[2]
    
    return (round(r/total_colors), round(g/total_colors),round(b/total_colors))

def find_colors (image,list_of_lists,val):
    """
        PURPOSE: A function that finds the average color for each current cluster and overwrites the
        means list with the new colors
        
        PARAMETERS:
            -image:2d grid of colors each represeting the color at that [x] [y] position
            -list_of_lists:  2d grid organized identically to the images, each element has an int represeting the cluster it belongs to
            -val: represents the group cluster number
            
        RETURN: A list of colors(tuples with r,g,b values) that belong to the group cluster number (parameter)
    """
    colors = []
    for col in range(len(list_of_lists)):
        for row in range (len(list_of_lists[col])):
            if list_of_lists[col] [row] == val:
                colors.append(image[col] [row])
    return colors 
    
def update_means (image,list_of_lists,k,means):
    """
        PURPOSE: A function that finds the average color for each current cluster and overwrites the
        means list with the new colors
        
        PARAMETERS:
            -image:2d grid of colors each represeting the color at that [x] [y] position
            -list_of_lists:  2d grid organized identically to the images, each element has an int represeting the cluster it belongs to
            -k: number of clusters
            -means: list containign the color of each cluster.
            
        RETURN: None
    """
    for i in range (k):
        assigned_colors = find_colors(image,list_of_lists,i)
        means[i] = avg_color(assigned_colors)


def update_assigments(image,means):
    """
        PURPOSE: A function that given the cluster colors and the image, it creates a new assigment of cluster for each pixel
        
        PARAMETERS:
            -image:2d grid of colors each represeting the color at that [x] [y] position
            -means: list containign the color of each cluster.
            
        RETURN: a new assigment list that represents the image, with each pixel having a value representing the cluster it belongs to
    """
    new_list_of_lists = []
    for col in range(len(image)):
        lst = []
        for row in range(len(image[col])):
             color_pixel = image[col][row]               
             lst.append(nearest_centroid(color_pixel,means))
             
        new_list_of_lists.append(lst)
        
    return new_list_of_lists 


    
