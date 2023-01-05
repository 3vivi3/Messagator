from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
from gtts import gTTS
import os
import time
import threading
import queue

message_queue = queue.Queue()
contact_translation=''
source=''
dest=''

def get_messages(contact_name):
    driver = webdriver.Chrome(executable_path="C:\\Users\\vibha\\Desktop\\DELL-VIBHA\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    time.sleep(30)
    search_box = driver.find_element(By.XPATH, "//div[@title='Search input textbox']")
    search_box.send_keys(contact_name)
    
    wait = WebDriverWait(driver, 10)
    contact_title = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title,' +"'" + contact_name +"'"+ ')]')))
    time.sleep(10)
    contact_title.click()
    time.sleep(10)
    messages = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div')
    
    for message in messages:
        message_queue.put(message.text)
    # driver.close()

def fetch_messages(contact):
    message_thread = threading.Thread(target=get_messages, args=[contact])
    message_thread.start()
    message_thread.join()
    messagebox.showinfo("Alert", "Messages from "+contact_translation+" have been extracted")


def interface(): 
    global contact_translation
    global source 
    global dest
    root = Tk()
    root.geometry('800x600')

    frame1=Frame(root,width=300,height=400,bg="cyan")
    frame2=Frame(root,width=300,height=400,bg="pink")
    frame3=Frame(root,width=600,height=200,highlightbackground="black",highlightthickness=1)
    frame4=Frame(frame3,width=500,height=150,highlightbackground="black",highlightthickness=1)
    frame5=Frame(frame3,width=100,height=150,highlightbackground="black",highlightthickness=1)
    frame6=Frame(frame3,width=600,height=50,highlightbackground="black",highlightthickness=1)

    #frames
    frame1.grid(row=0,column=0,sticky="nsew")
    frame2.grid(row=0,column=1,sticky="nsew")

    #frame3
    frame3.grid(row=1,column=0,rowspan=2,columnspan=2,sticky="new")
    frame4.grid(row=0,column=0,sticky="nsew")
    frame5.grid(row=0,column=1,sticky="nsew")
    frame6.grid(row=2,column=0,rowspan=2,columnspan=2,sticky="nsew")

    #frame configuration
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    frame3.columnconfigure(0,weight=2)
    frame3.columnconfigure(1,weight=1)

    #text box
    text_box1=Text(frame1,bg="light pink",fg="black",relief="solid")
    text_box2=Text(frame2,bg="light yellow",fg="black",relief="solid")
    text_box1.grid(row=0,column=0,sticky="nsew")
    text_box2.grid(row=0,column=1,sticky="nsew")
    text_box1.rowconfigure(0,weight=1)
    text_box1.columnconfigure(0,weight=1)
    text_box2.columnconfigure(1,weight=1)
    text_box1.pack(expand=True,fill=BOTH)
    text_box2.pack(expand=True,fill=BOTH)

    #button
    btn=Button(frame5,text="Fetch Messages",bg="light blue",relief='ridge',font=('Helvetica',10,'bold'), command= lambda: fetch_messages(contact_translation))
    btn.grid(row=1,column=0)
    
    def convert_audio():
        text_info =  textBox2.get("1.0", "end-1c")
        myObj=gTTS(text=text_info,lang='hi',slow=False)               
        myObj.save('SpeechTest.mp3')
        os.system("SpeechTest.mp3")
    photo=PhotoImage(file="C:/Users/vibha/Desktop/GSOP/Speaker.svg.png")
    speakerbtn=Button(frame5,image=photo, command=convert_audio)
    speakerbtn.grid(row=0,column=0,pady=15)
    
    
    def callback(*arg):
        global contact_translation
        contact_translation=box.get()

    #combo box1
    contact_combotext=tk.StringVar()
    contact_combotext.set('Type or enter Contact')
    names=["Kara", "Vidhisha Gat", "Amodh"]
    box=ttk.Combobox(frame6, values=names, textvariable=contact_combotext)
    box.grid(row=0,column=0,sticky="nsew")  
    contact_combotext.trace('w', callback)

    def callback_source(*arg):
        global source
        source=sbox.get()
    
    #combo box2
    source_language=StringVar()
    source_language.set('Source Language')
    sbox=ttk.Combobox(frame6,textvariable=source_language,state="read-only")
    sbox['values']=("English",
                    "Kannada",
                    "Hindi",
                    "French",
                    "Korean")
    sbox.grid(row=0,column=1,sticky="nsew")
    source_language.trace('w', callback_source)  

    def callback_dest(*arg):
        global dest
        dest=dbox.get()
        
    #combo box3
    destination_language=StringVar()
    destination_language.set('Destination Language')
    dbox=ttk.Combobox(frame6,textvariable=destination_language,state="read-only")
    dbox['values']=("English",
                    "Kannada",
                    "Hindi",
                    "French",
                    "Korean")
    dbox.grid(row=0,column=2,sticky="nsew")  
    destination_language.trace('w', callback_dest)  
    
    #combo box configuration
    frame6.columnconfigure(0,weight=1)
    frame6.columnconfigure(1,weight=1)
    frame6.columnconfigure(2,weight=1)

    #________________________________
    textBox1 = Text(root)
    textBox2 = Text(root)
    lang_dict = {
        "English": "en",
        "Kannada": "ka",
        "Hindi": "hi",
        "French": "fr",
        "Korean": "ko"
    }

    
    #********************
    textBox1.grid(row=0, column=0)
    textBox1.tag_add("l1", "1.0", "1.50")
    textBox1.tag_configure("l1",background = "white",foreground= "red")
    textBox1.tag_add("l2", "2.0", "2.50")
    textBox1.tag_configure("l2",foreground= "blue")


    textBox2.grid(row=0, column=1)
    textBox2.tag_add("l1", "1.0", "1.50")
    textBox2.tag_configure("l1",foreground= "red")
    textBox2.tag_add("l2", "2.0", "2.50")
    textBox2.tag_configure("l2",foreground= "blue")

    while not message_queue.empty():
        text = message_queue.get()
        textBox1.insert(INSERT, text)
        textTranslated = Translator().translate(text, src=lang_dict[source], dest=lang_dict[dest])
        textBox2.insert(INSERT, textTranslated.text+"\n")

    root.call('encoding', 'system', 'utf-8')
    root.mainloop()


interface_thread = threading.Thread(target=interface, args=[])
interface_thread.start()
interface_thread.join()

if not message_queue.empty():
    interface_thread2 = threading.Thread(target=interface, args=[])
    interface_thread2.start()
    interface_thread2.join()
print("Terminating applicaton...")          