import color
from PIL import Image
from io import BytesIO


def create_png(size, color_int):
    image = Image.new("RGB", size, color_int)
    return image


def create_solid_image_stream(color_int):
    bio = BytesIO()
    bio.name = 'color.png'
    image = create_png(
        (200, 200),
        (color.red_component(color_int),
         color.blue_component(color_int),
         color.green_component(color_int))
    )

    image.save(bio, 'PNG')
    bio.seek(0)

    return bio
