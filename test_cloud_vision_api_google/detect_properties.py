from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)
def convert_rgb_to_name(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]

def convert_google_api_color_to_rgb_tuple(google_api_color):
    return (int(google_api_color.color.red), int(google_api_color.color.green), int(google_api_color.color.blue))

def detect_properties(path):
    """Detects image properties in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    rgb_tuple = convert_google_api_color_to_rgb_tuple(props.dominant_colors.colors[0])

    print("MAIN COLOR IS:")
    print(convert_rgb_to_name(rgb_tuple))

    # print('Properties:')

    # for color in props.dominant_colors.colors:
    #     print('fraction: {}'.format(color.pixel_fraction))
    #     print('\tr: {}'.format(color.color.red))
    #     print('\tg: {}'.format(color.color.green))
    #     print('\tb: {}'.format(color.color.blue))
    #     print('\ta: {}'.format(color.color.alpha))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))