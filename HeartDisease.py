#Basic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow
import warnings
warnings.filterwarnings('ignore')
def nextPage():
    #root.destroy()
    import Showdataset
    
from tkinter import *  
root = Tk()  
root.geometry("400x250")
label1 = Label(root, text="HEART DISEASE DETECTION", font=('Impact', -35), fg='#0080ff')
label1.config()
label1.place(x=100, y=20)
btn = Button(root, text="Load Dataset",command=nextPage)
btn.config()
btn.place(x=50, y=100)
btn1 = Button(root, text="Classification",command=nextPage)
btn1.config()
btn1.place(x=50, y=140)
btn2 = Button(root, text="Disease Detection",command=nextPage)
btn2.config()
btn2.place(x=50, y=180)
root.mainloop()  
