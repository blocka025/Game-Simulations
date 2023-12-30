from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# Define the card suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
font_size = 100  # Change this value to adjust font size
card_width, card_height = 400, 600
# Create a function to generate and save card images
prefixes = ['A','B','C','D']
def generate_card_images():
    # Define card dimensions and fonts
    font = ImageFont.truetype("arial.ttf", font_size)

    for i, suit in enumerate(suits):
        suit_image = Image.open(f'C:/Users/blake/Documents/VSCode/Python/FreeCell/Suits/{suit[:-1]}.png') 
        suit_image.thumbnail((card_width, card_height))
        suit_image2 = Image.open(f'C:/Users/blake/Documents/VSCode/Python/FreeCell/Suits/{suit[:-1]}.png')
        suit_image2.thumbnail((card_width // 5, card_height // 5))
        for j, rank in enumerate(ranks):
            # Create a new blank image for each card
            card = Image.new('RGB', (card_width, card_height), color='white')
            draw = ImageDraw.Draw(card)

            # Calculate positions to place the suit images in corners of the card
            offset = 15
            top_right_position = (card_width - suit_image2.width - offset, offset)
            bottom_left_position = (offset, card_height - suit_image2.height - offset)

            # Paste the suit images onto the card in top-right and bottom-left corners
            card.paste(suit_image2, top_right_position, mask=suit_image2)
            card.paste(suit_image2, bottom_left_position, mask=suit_image2)
            #make black order
            draw.rectangle([(0, 0), (card_width-1, card_height-1)], outline="black")

            suit_position = ((card_width - suit_image.width) // 2, (card_height - suit_image.height) // 2)

            # Paste the suit image onto the card
            card.paste(suit_image, suit_position, mask=suit_image)
            if suit in ['Hearts', 'Diamonds']:
                font_color = 'red'
            else:
                font_color = 'black'

            # Add card value at each corner with respective font color
            corner_offset = font_size // 9  # Adjust the offset according to font size
            draw.text((corner_offset, corner_offset/2), rank, fill=font_color, font=font)
            draw.text((card_width - corner_offset/1.4 - font_size, card_height - corner_offset/2 - font_size), rank, fill=font_color, font=font)

            # card = Image.new('RGB', (card_width + border_width, card_height + border_width), color='black')
            # Save the card image as a PNG file
            if j < 9:
                card.save('C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/'+prefixes[i]+f'{j+1}_of_{suit}.png')
            else:
                card.save('C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/'+prefixes[i]+prefixes[i]+f'{j+1}_of_{suit}.png')

def generate_special_card_images():
    freecell = Image.new('RGB', (card_width, card_height))
    draw = ImageDraw.Draw(freecell)
    draw.rectangle([(0, 0), (card_width-4, card_height-4)], outline="gray",fill =(0,81,44),width=3)
    freecell.save('C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/freecell.png')
    for suit in suits:
        stack = Image.new('RGB', (card_width, card_height))
        draw = ImageDraw.Draw(stack)
        draw.rectangle([(0, 0), (card_width-4, card_height-4)], outline="gray",fill =(0,81,44),width=3)

        suit_image = Image.open(f'C:/Users/blake/Documents/VSCode/Python/FreeCell/Suits/Gray{suit[:-1]}.png') 
        suit_image.thumbnail((card_width, card_height))
        stack.paste(suit_image, ((card_width - suit_image.width) // 2, (card_height - suit_image.height) // 2), mask=suit_image)

        stack.save('C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/'+suit[:-1]+'.png')


# Generate and save card images
generate_card_images()
generate_special_card_images()

