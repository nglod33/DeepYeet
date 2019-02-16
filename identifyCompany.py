#Authors: Nate Glod

import sys, getopt, os, io

def whatLogo(imgPath):
    """Detects logos in photos"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    file_name = os.path.join(os.path.dirname(__file__),
    imgPath)


    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    if(len(logos) == 0):
        print('No logos detected')
    else:
        for logo in logos:
            print(logo.description)
    return len(logos)

def main(imgPath):
    whatLogo(imgPath)

if __name__ == "__main__":
    main(sys.argv[1])
