from PIL import Image

def write_coords(path_to_img):

    # read image
    img = Image.open(path_to_img)
    w, h = img.size 
    print(w, h)
    data = img.load()

    # write coordinates to csv
    with open('coords.csv', 'w') as f:
        f.write('x,y\n')
        for x in range(w):
            for y in range(h):
                if data[x, y] == 0:
                    f.write('{},{}\n'.format(x, y))

def create_img_from_coords(coords, w=2040, h=2040):

    # create black canvas
    new_img = Image.new('1', (w, h))

    # read coordinates from csv
    with open(coords, 'r') as f:
        next(f)  # skip header
        for line in f:
            x, y = line.split(',')
            if int(x) > w or int(y) > h or int(x) < 0 or int(y) < 0:
                print(x, 'or', y, 'is out of range')
                continue
            print('x:', x, 'y:', y)
            new_img.putpixel((int(x), int(y)), 1)
            
            
    # save
    new_img.save('new_img.png')



# Instructions

## write_coords(image_path)
# you will need to pass the path to the image relative to the location of the script
# this will write the coordinates to a csv file called coords.csv

# write_coords('example.tif')  

## create_img_from_coords('coords.csv', width, height)
# width,height are optional and default to 2040x2040
# this will create a new image from the coordinates in coords.csv
# the new image will be saved as new_img.png

create_img_from_coords('coords.csv', 509, 507)
print('done')


# feel free to comment out to execute only the functions you want