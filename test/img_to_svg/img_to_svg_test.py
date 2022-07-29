import base64

def get_image_file_as_base64_data(logo=True):
    '''https://stackoverflow.com/questions/38329909/pdfkit-not-converting-image-to-pdf'''
    if logo:
        with open('./h_logo.png', 'rb') as image_file:
            # To return a string worth use in Html you should use ` base64.b64encode(image_file.read()).decode()` – SATYAJEET RANJAN
            return base64.b64encode(image_file.read()).decode()
    else:
        with open('./randy-fath-unsplash.jpg', 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode()