import serial
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
import zpl
import sys

# Setup/Create File Paths
xkcd_dir = Path.cwd() / "xkcd"
xkcd_dir.mkdir(parents=True, exist_ok=True)

# Random XKCD URL
xkcd_url = "https://dynamic.xkcd.com/comic/random"

# Serial Parameters
com_port = "COM3"


def parse_img_url(url):

    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        comic = soup.select("#comic img")
        return "https:" + comic[0].get("src")
    else:
        print("Bad Response")
    sys.exit(1)


def download_image(url, dest_dir):
    res = requests.get(url)
    if res.status_code == 200:
        img_path = dest_dir / Path(url).name

        with open(img_path, "wb") as f:
            f.write(res.content)

        print(f"Image Name: {Path(url).name}")
        print(f"Image Size: {img_path.stat().st_size} Bytes")
        return img_path


def print_image(image_path, com):

    label = zpl.Label(100, 60)
    height = 10
    image_width = 60
    label.origin((label.width - image_width) / 2, height)
    image_height = label.write_graphic(Image.open(image_path), image_width)
    label.endorigin()

    zpl_image = label.dumpZPL()

    with serial.Serial(com) as ser:

        print("Sending Image to Printer....")

        # Send Image
        ser.write(zpl_image.encode("utf-8"))


img_url = parse_img_url(xkcd_url)
img_path = download_image(img_url, xkcd_dir)
print_image(img_path, com_port)

