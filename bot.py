import discord

import requests
from PIL import Image
import shutil
import sys

import socket

# msgFromClient       = "https://images.unsplash.com/photo-1481349518771-20055b2a7b24?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cmFuZG9tfGVufDB8fDB8fHww&w=1000&q=80"
serverAddressPort   = ("192.168.137.211", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
def send_message(message: str) -> str:
    UDPClientSocket.sendto(message.encode(), serverAddressPort)
    # Get response from server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    return msgFromServer[0].decode()


def download_image(url: str, filename: str):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def display_image(filename: str):
    img = Image.open(filename)
    img.show()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel

    if message.content.startswith('hello'):
        await message.channel.send('Hello, welcome to your new job at Blossom Co. I am your guide and narrator throughout this journey. To begin your first day type "begin"')
    if message.content.startswith('begin'):
        await message.channel.send('Welcome to your first day at Blossom Co. Fist you are on coffe duty, post a picture of a coffee company')
    
    # if user uploads an image
    if message.attachments and message.attachments[0].content_type.startswith("image/"):
        # get image URL
        attachment = message.attachments[0]
        url = attachment.url
        print(f"detected image, URL: {url}")

        # # download the image
        # print("Detected an attachment, downloading image from: " + url)
        # download_image(url, "testing.png")
        # display_image("testing.png")

        # # send the image right back to them
        # await channel.send(file=discord.File('testing.png'))
        
        # send the URL to the recognition server and print out how it classifies the image
        classify_response = send_message(url)
        print(classify_response)
        await message.channel.send(classify_response)


client.run('MTEyMzI2OTI1MjMzNDQ4OTc2Mw.Grp_SU.5TUPsHZwwAp0vRcUkCDkzIERKCHTjiCaHdRnVw')