# Messagator
Messagator is a multithreaded application which provides a GUI to set parameters to fetch messages from Whatsapp and performs translation and Text to Speech operations on it.

## Threads
It uses two threads created using the threading modules:
  1. Interface Thread - This thread runs the GUI interface built using tkinter which allows us to set contact name , source language and destination language.
  2. Message Thread - This runs runs the selenium configured with chrome driver to extract the messages from Whatsappweb

## Preview

![image](https://user-images.githubusercontent.com/89783934/210997696-23f5a8c9-724e-455f-83d6-5007bb4fac29.png)

## Flow Diagram

![image](https://user-images.githubusercontent.com/89783934/210999113-29a40339-9f6f-41d9-a750-81d11e063b2f.png)


