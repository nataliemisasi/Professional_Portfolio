import PySimpleGUI as sg
from PIL import Image, ImageFont, ImageDraw


def add_watermark_text(original_image_path,
                    save_image_path,
                    text, pos):
    photo = Image.open(original_image_path)

    drawing = ImageDraw.Draw(photo)

    color = (80, 79, 84)
    font = ImageFont.truetype("fonts/Rhesmanisa.otf", 70)
    drawing.text(pos, text, fill=color, font=font)
    photo.show()
    photo.save(save_image_path)


def add_watermark_image(original_image_path,
                    save_image_path,
                    watermark_image_path,
                    position):

    base_image = Image.open(original_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(save_image_path)


sg.theme('BluePurple')

layout = [
    [sg.Text("")],
    [sg.Text("Original Photo: "), sg.Input(key='-ORIGINAL PHOTO-'), sg.FileBrowse()],
    [sg.Text("")],
    [sg.Text("To add a customizable text watermark, enter desired text below then save;")],
    [sg.Text("Watermark Text: "), sg.Input(key='-WATERMARK TEXT-'), sg.Button('Save', size=(4,1), key='-SAVE WATERMARK TEXT-')],
    [sg.Text("")],
    [sg.Text("To add a an image as your watermark, browse for the file below then save;")],
    [sg.Text("Watermark File: "), sg.Input(key='-WATERMARK FILE-'), sg.FileBrowse(), sg.Button('Save', size=(4,1), key='-SAVE WATERMARK IMAGE-')],
    [sg.Text("")],
    [sg.Button('Exit', size=(10, 3))],
    ]

window = sg.Window('Watermark GUI', layout, resizable=True)

while True:
    event, values = window.read()
    original_image_path = values['-ORIGINAL PHOTO-']
    save_image_path = values['-ORIGINAL PHOTO-'].split('.')[0]+'(watermarked).png'
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == '-SAVE WATERMARK TEXT-':
        add_watermark_text(original_image_path, save_image_path,
                           text=values['-WATERMARK TEXT-'],
                           pos=(15, 35))
    elif event == '-SAVE WATERMARK IMAGE-':
        add_watermark_image(original_image_path, save_image_path,
                            values['-WATERMARK FILE-'], position=(15, 590))

window.close()
