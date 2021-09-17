from PIL import Image, ImageFont, ImageDraw

def add_watermark_text(original_image_path, save_image_path, text, pos):
    photo = Image.open(original_image_path)

    drawing = ImageDraw.Draw(photo)

    color = (80, 79, 84)
    font = ImageFont.truetype("fonts/Rhesmanisa.otf", 70)
    drawing.text(pos, text, fill=color, font=font)
    photo.show()
    photo.save(save_image_path)

if __name__ == '__main__':
    img = 'photos/tour_da_parish.jpg'
    add_watermark_text(img, 'photos/watermarked/tour_da_parish_text_watermark.jpg', text='Natalie Misasi', pos=(15, 35))

# ___________________________________________________________________________________________________________

def watermark_with_transparency(original_image_path, save_image_path, watermark_image_path, position):

    base_image = Image.open(original_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(save_image_path)


if __name__ == '__main__':
    img = 'photos/tour_da_parish.jpg'
    watermark_with_transparency(img, 'photos/watermarked/tour_da_parish_pic_watermark.jpg', 'transparent_signature_watermark.png',  position=(15, 590))
