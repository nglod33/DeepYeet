#Authors: Nate Glod

import sys, getopt, os, io

def whatLogo(imgURI):
    """Detects logos in photos"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = imgURI

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    if(len(logos) == 0):
        print("No logos detected")
        return ""
    else:
        print(logos[0].description)
        return logos[0].description

def main(imgURI):
    whatLogo(imgURI)

if __name__ == "__main__":
    main(sys.argv[1])
