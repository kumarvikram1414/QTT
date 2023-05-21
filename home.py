import tkinter as tk
import os
from PIL import ImageTk, Image





class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Main Page")
        self.master.geometry("500x500")

        img = Image.open("happy.PNG")
        img = img.resize((500, 500), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(img)


        

        
        self.button1 = tk.Button(self, text="Notepad",bg="#FF5733", fg="#FFF", command=self.open_file1)
        self.button1.pack(side=tk.TOP, padx=10, pady=10)
        
        self.button2 = tk.Button(self, text="Spelling",bg="#C70039", fg="#FFF", command=self.open_file2)
        self.button2.pack(side=tk.TOP, padx=10, pady=10)
        
        self.button3 = tk.Button(self, text="Ide",bg="#900C3F", fg="#FFF", command=self.open_file3)
        self.button3.pack(side=tk.TOP, padx=10, pady=10)
        

        
    def open_file1(self):
        os.system("python Notepad.py")
    
    def open_file2(self):
        os.system("python Spelling.py")
    
    def open_file3(self):
        os.system("python Ide.py")
    


if __name__ == "__main__":
    root = tk.Tk()
    app = MainPage(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
