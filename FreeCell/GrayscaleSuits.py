import cv2
import numpy as np
from PIL import Image, ImageDraw

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def remove_white_background_and_convert_to_grayscale(input_image_path, output_image_path):
    # Read the image
    img = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)

    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a mask to identify white areas
    _, mask = cv2.threshold(grayscale_img, 150, 255, cv2.THRESH_BINARY)

    # Invert the mask
    mask = cv2.bitwise_not(mask)
    g = 100
    # filled_img = np.zeros((*mask.shape, 3), dtype=np.uint8)
    # filled_img[mask != 0] = (g,g,g)

    filled_img = np.zeros((*mask.shape, 4), dtype=np.uint8)
    # Set the alpha channel values based on the mask
    filled_img[:, :, 3] = mask  # Set alpha values based on the mask

    # Convert the color to the appropriate format (BGR)
    bgr_color = (g,g,g)  # Reverse the RGB tuple to BGR for OpenCV

    # Fill the RGB channels with the specified color
    filled_img[:, :, :3] = bgr_color

    # # Apply the mask to the original image
    # img_without_white_bg = cv2.bitwise_and(grayscale_img, grayscale_img, mask=mask)


    # Save the resulting image
    cv2.imwrite(output_image_path, filled_img)


for suit in suits:
    input_image = f'C:/Users/blake/Documents/VSCode/Python/FreeCell/Suits/{suit[:-1]}.png'
    output_image = f'C:/Users/blake/Documents/VSCode/Python/FreeCell/Suits/Gray{suit[:-1]}.png'
    remove_white_background_and_convert_to_grayscale(input_image, output_image)

# card_width, card_height = 400, 600
# g =100
# transpar = 200

# freecell = Image.new('RGB', (card_width, card_height))
# draw = ImageDraw.Draw(freecell)
# draw.rectangle([(0, 0), (card_width-4, card_height-4)], outline="gray",fill =(g,g,g,50),width=3)
# freecell.save('C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/selected.png')