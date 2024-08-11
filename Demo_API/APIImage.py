import openai
from openai import OpenAI

import io
import urllib.request


from PIL import Image
import matplotlib.pyplot as plt

client=OpenAI()


def createImage(text):
    prefixPrompt = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: "
    response = client.images.generate(
      model="dall-e-3",
      prompt=text,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    return response.data[0].url



def createImageEdit(text, imgBase, imgMask):
    response = client.images.edit(
      model="dall-e-2",
      image=open(imgBase, "rb"),
      mask=open(imgMask, "rb"),
      prompt=text,
      n=1,
      size="1024x1024"
    )
    return response.data[0].url



def createImageVariation(imgToVarient):
    response = client.images.create_variation(
      model="dall-e-2",
      image=open(imgToVarient, "rb"),
      n=1,
      size="1024x1024"
    )
    return response.data[0].url


imgBase="Data/imgBase.png"
imgMask="Data/imgMask.png"

imgBase1="Data/imgBase1.png"
imgMask1="Data/imgMask1.png"






#urlImage = createImage("A Polar bar dancing on the water with colorfuk fireworks around")
#urlImage = createImageEdit("a child playing in the pool", imgBase1, imgMask1)
urlImage = createImageVariation(imgBase1)


urllib.request.urlretrieve(urlImage, "TempImageName.png") 
img = Image.open("TempImageName.png") 
img.show()


