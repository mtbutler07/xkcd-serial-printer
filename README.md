# Random XKCD Comic Printer

## Description

Python3 script to download a random XKCD comic, transfer the image via serial to a Zebra thermal printer, and print a label.

## Setup

Download Python dependencies

```bash
$ python3 -m pip install -r requirements.txt -U --user
```

Configure the COM port in the `xkcd-printer.py` script

Example `com_port = "COM3"`

## Run the script

```bash
$ python3 xkcd-printer.py
```

## Resources

[**ZPL II Command Reference**](https://www.zebra.com/content/dam/zebra/manuals/printers/common/programming/zpl-zbi2-pm-en.pdf)
