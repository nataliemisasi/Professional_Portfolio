from PIL import Image, ImageFont, ImageDraw

def watermark_text(input_image_path, output_image_path, text, pos):
    photo = Image.open(input_image_path)

    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("Satisfy-Regular.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)

if __name__ == '__main__':
    img = 'tour_da_parish.jpg'
    watermark_text(img, 'tour_da_parish_watermarked.jpg', text='Natalie Misasi', pos=(5, 5))
