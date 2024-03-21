from PIL import Image, ImageFilter, ImageFont, ImageDraw

# Применяем фильтры
img = Image.open("assets/img1.jpg")

# Apply each filter
# img_blur = img.filter(ImageFilter.BLUR)
# img_contour = img.filter(ImageFilter.CONTOUR)
# img_detail = img.filter(ImageFilter.DETAIL)
# img_edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)
# img_edge_enhance_more = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
# img_emboss = img.filter(ImageFilter.EMBOSS)
# img_find_edges = img.filter(ImageFilter.FIND_EDGES)
# img_sharpen = img.filter(ImageFilter.SHARPEN)
# img_smooth = img.filter(ImageFilter.SMOOTH)
# img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
#
# # Show the images
# img_blur.show()
# img_contour.show()
# img_detail.show()
# img_edge_enhance.show()
# img_edge_enhance_more.show()
# img_emboss.show()
# img_find_edges.show()
# img_sharpen.show()
# img_smooth.show()
# img_smooth_more.show()


# И вариант для скрина
# Load the original image
original_img = Image.open("assets/img1.jpg")

# Define the list of filter names
filter_names = [
    "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE",
    "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"
]

# Define a font for the titles
font = ImageFont.truetype("arial.ttf", 20)

# Calculate the grid size based on the number of filters
num_filters = len(filter_names)
cols = 3  # Number of columns in the grid
rows = (num_filters + 1) // cols  # Plus one for the original image
if (num_filters + 1) % cols != 0:
    rows += 1

# Calculate the size of each cell in the grid
cell_width = original_img.width
cell_height = original_img.height

# Create a blank canvas for the big image
big_image_width = cols * cell_width
big_image_height = rows * cell_height + (rows - 1) * 50  # 50 pixels spacing between rows
big_image = Image.new("RGB", (big_image_width, big_image_height), color="white")
draw = ImageDraw.Draw(big_image)

# Paste the original image with its title
y_offset = 0
draw.text((10, y_offset), "Original Image", fill="black", font=font)
big_image.paste(original_img, (0, y_offset + 30))

# Apply each filter, add the filtered image with its title to the big image
for i, filter_name in enumerate(filter_names):
    col = i % cols
    row = i // cols + 1  # Start from the second row to leave space for the original image
    x_offset = col * cell_width
    y_offset = row * cell_height + (row - 1) * 50

    filter_img = original_img.filter(getattr(ImageFilter, filter_name))
    draw.text((x_offset + 10, y_offset), filter_name, fill="black", font=font)
    big_image.paste(filter_img, (x_offset, y_offset + 30))

# Save or display the big image
big_image.show()
big_image.save('output/big_image.jpg')