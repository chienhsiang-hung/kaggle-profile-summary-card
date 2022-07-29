import base64

def img_to_datauri(image_file):
    return base64.b64encode( image_file.read() ).decode()