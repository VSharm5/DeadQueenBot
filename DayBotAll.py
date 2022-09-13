from groupy import Client
import datetime
import meme as m
from PIL import Image, ImageDraw, ImageFont

def day(): #calculates how many days since the queen's death
    now=datetime.date.today()
    then=datetime.date(2022,9,8) #date of queen's death
    return (now-then).days

def caption_image(image_file, caption, caption2, font="impact.ttf"):
    img = Image.open(image_file)
    draw = ImageDraw.Draw(img)
    fs=int(img.size[1]/5)
    font = ImageFont.truetype("impact.ttf", fs)
    tts=font.getsize(caption)
    bts=font.getsize(caption2)
    while tts[0]>img.size[0]-20 or bts[0]>img.size[0]-20:
        fs=fs-1
        font = ImageFont.truetype("impact.ttf", fs)
        tts=font.getsize(caption)
        bts=font.getsize(caption2)
    caption_w, caption_h = draw.textsize(caption, font=font)
    caption2_w, caption_h = draw.textsize(caption2, font=font)
    draw.text(((img.width-caption_w)/2, (img.height-caption_h)/16), # position
              caption, # text
              (255,255,255), # color
              font=font, # font
              stroke_width=2, # text outline width
              stroke_fill=(0,0,0)) # text outline color
    draw.text(((img.width-caption2_w)/2, (img.height-caption_h)*15/16),
             caption2,
             (255,255,255),
             font=font,
             stroke_width=2,
             stroke_fill=(0,0,0))
    img.save("output.png")
    img.close()

def deadQueenDay(): #creates a message containing text and an image (meme) to be sent to GroupMe chat of choice
    client=Client.from_token("<YOUR AUTH TOKEN>") #auth token
    for group in client.groups.list(): #for each group in list of groups aka group chats
        if group.name=="<YOUR GROUP>": break   #Find the group with this specific name
                                        #GroupMe group name order changes frequently - in order of the youngest messaage
                                        #Hence it's probably easiest to just manually check each group name
    n=str(day()) #get number of days
    with open ('krabs.png', 'rb') as f:
        m.caption_image(f,"DAY "+n,"GIVE IT UP FOR DAY "+n) #draws text on the image to make the meme, saves it as 'output.png'
    with open ('output.png', 'rb') as f:
        image1=client.images.from_file(f) #sends the image to GroupMe for uploading and gets the image URL back for attatchment
    group.post(text='Day '+n+' of the Queen being dead', attachments=[image1]) #posts the text and image to the specified group

if __name__ == "__main__":
    deadQueenDay()