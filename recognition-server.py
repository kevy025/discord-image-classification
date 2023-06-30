import socket
import jetson_inference
import jetson_utils
import requests
import shutil

net = jetson_inference.imageNet("resnet-18")


def send_response(message, return_address):
    UDPServerSocket.sendto(message.encode(), return_address)


def download_image(url: str, filename: str):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


localIP     = ""
localPort   = 20001
bufferSize  = 1024


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")


# Listen for incoming datagrams
while(True):
    # Get message from client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]
    print("Message from Client:{}".format(message))

    # Message should be an image URL: download it
    download_image(message, "testfile.jpg")

    # classify the image
    img = jetson_utils.loadImage("testfile.jpg")
    class_idx, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_idx)
    msg = "image is recognized as "+ str(class_desc) +" (class #"+ str(class_idx) +") with " + str(confidence*100)+"%% confidence"

    # Sending a reply to client
    UDPServerSocket.sendto(msg.encode(), address)