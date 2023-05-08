import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk
from trackers import EuclideanDistTracker


class TrafficApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Violation")
        self.master.geometry("1100x800")
        
        self.home() 
          
        file_frame = tk.Frame(master)
        file_frame.pack(pady=10)
        self.paused = False

        self.file_path = ""
        self.cap = None
        self.tracker = EuclideanDistTracker()
        self.object_detector = cv2.createBackgroundSubtractorMOG2(history=None,varThreshold=None)
        self.kernalOp = np.ones((3,3),np.uint8)
        self.kernalOp2 = np.ones((5,5),np.uint8)
        self.kernalCl = np.ones((11,11),np.uint8)
        self.fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
        self.kernal_e = np.ones((5,5),np.uint8)
        self.end = 0
     
    
    

    def home(self):
        

        for widget in self.master.winfo_children():
            widget.destroy()
   
        master=self.master
        button_framel = tk.Frame(master)
        button_framel.pack()
        

        file_label = tk.Label(button_framel, text="Lựa chọn video để nhận diện vi phạm:", font=('times', 18, 'bold'),  width=30,foreground='blue')
        file_label.pack(side='top', pady=7)

        file_button = tk.Button(button_framel, text="Browse", command=self.browse_file, foreground='black', font=('arial', 12, 'bold'), width=10,height=1)
        file_button.pack()
      
# Tạo Canvas hiển thị video
        self.canvas = tk.Canvas(master, width=1000, height=590, bg="gray")
        self.canvas.pack(side=tk.TOP, pady=10)


  
# Tạo Frame chứa Start và Quit Button
        button_frame = tk.Frame(master)
        button_frame.pack()
       
    
        start_button = tk.Button(button_frame, text="Start", command=self.start_detecting, foreground='black', font=('arial', 12, 'bold'), width=8,height=1)
        start_button.pack(side=tk.LEFT, padx=7)

        stop_button = tk.Button(button_frame, text="Stop", command=self.stop_detecting, foreground='black', font=('arial', 12, 'bold'), width=8,height=1)
        stop_button.pack(side=tk.LEFT, padx=7)
        button2 = tk.Button(self.master, text='Vi phạm',width=8,height=1, command=self.display_images, font=('arial', 12, 'bold'))
        button2.pack(side='top', pady=20)
     


        
    def display_images(self):

        for widget in self.master.winfo_children():
            widget.destroy()

   
        l1 = tk.Label( self.master, text='Ảnh xe vi phạm Tốc Độ', foreground='blue', font=('time', 18, 'bold'))
        l1.pack(side='top', pady=20)

        img_dir = "C://py//text//Nhom10//Nhom10//speed111//data//data1" # directory path where images are stored
        img_paths = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if f.endswith(('jpg', 'png'))]

        frame = tk.Frame( self.master)
        frame.pack(side='top')
      
        canvas = tk.Canvas(self.master)
        canvas.pack(side='top')
        count = 0 # Counter for the number of images displayed
        for img_path in img_paths:
            img = Image.open(img_path) # read the image file
            img = img.resize((170, 170)) # new width & height
            img = ImageTk.PhotoImage(img)

            label = tk.Label(canvas, image=img, padx=50, pady=50)
            label.image = img # keep a reference! by attaching it to a widget attribute

        # Calculate the x, y coordinates for this label based on the count
            x = (count % 4) * 200 + 100
            y = (count // 4) * 200 + 100

            canvas.create_window(x, y, anchor='center', window=label)

            count += 1

    # Resize the canvas to fit all the images
        width = 800
        height = ((count - 1) // 4 + 1) * 200
        canvas.config(width=width, height=height)

        

        button_frame1 = tk.Frame(self.master)
        button_frame1.pack()
       
        Xuli_button = tk.Button(button_frame1, text='Xứ lí', font=('arial', 12, 'bold'), width=10, command=self.xuli)
        Xuli_button.pack(side=tk.LEFT, padx=7)

    
        back_button = tk.Button(button_frame1,text='Back', font=('arial', 12, 'bold'), width=10, command=self.home)
        back_button.pack(side=tk.LEFT, padx=7)



        # button2 = tk.Button(self.master, text='Back', font=('arial', 12, 'bold'), width=10, command=self.home)
        # button2.pack(side='left', padx=350, pady=5)

        # button3 = tk.Button(self.master, text='Xứ lí', font=('arial', 12, 'bold'), width=10, command=self.xuli)
        # button3.pack(side='right', padx=350, pady=5)
        
        
       # Button(self.master,width=10,pady=7,text='Xử lí',fg='black',border=0,font=('arial', 16, 'bold') ,command=self.xuli).place(x=0, y=0)



    def xuli(self):
        root.destroy()
        import tt 

    def browse_file(self):
        self.file_path = filedialog.askopenfilename()
    
   
    def stop_detecting(self):
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
    

    def start_detecting(self):
        end = 0
        if not self.file_path:
            print("No file selected.")
            return

        self.cap = cv2.VideoCapture(self.file_path)
        f = 25
        w = int(1000 / (f - 1))

        frame_count = 0
        start_time = None
        while True:
             
            ret, frame = self.cap.read()
            
            if not ret:
                break       
            frame_count += 1                    
            # frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            # height, width, _ = frame.shape

            # roi = frame[50:540, 200:960]
            roi = frame[0:590,400:1000]
            mask = self.object_detector.apply(roi)
            _, mask = cv2.threshold(mask, 255, 255, cv2.THRESH_BINARY)

            fgmask = self.fgbg.apply(roi)
            ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
            mask1 = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, self.kernalOp)
            mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, self.kernalCl)
            e_img = cv2.erode(mask2, self.kernal_e)

            contours, _ = cv2.findContours(e_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            detections = []

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area >5000:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    detections.append([x, y, w, h])
                    if start_time is None:
                        start_time = (frame_count-1)/f

            boxes_ids = self.tracker.update(detections)
            for box_id in boxes_ids:
                x, y, w, h, id = box_id

                if (self.tracker.getsp(id) < self.tracker.limitmax() ):
                    cv2.putText(roi, str(id) + " " + str(self.tracker.getsp(id)), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
                else:
                    cv2.putText(roi, str(id) + " " + str(self.tracker.getsp(id)), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 3)
            
                s = self.tracker.getsp(id)
                if (self.tracker.f[id] == 1 and s != 0):
                      self.tracker.capture(roi, x, y, h, w, s, id)
               
            
              
                
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.canvas.update()
  
            if cv2.waitKey(w) & 0xFF == 27:
                cv2.destroyAllWindows()
                break
        if(end!=1):
            self.tracker.end()
        
        self.cap.release()
        cv2.destroyAllWindows()

root= tk.Tk()
 
app = TrafficApp(root)
root.mainloop()