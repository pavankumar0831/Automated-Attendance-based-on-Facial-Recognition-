import tkinter as tk
import random
from tkinter import Text,Message,messagebox
import cv2,os
#import face_recognition
import csv
import numpy as np
from PIL import ImageTk
from PIL import Image
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as fonts
import os
#from openpyxl import *
import datetime
import math
from tkinter import simpledialog
import requests
import yaml
import json
import base64
import tempfile
from io import BytesIO
root = tk.Tk()
root.maxsize(1600,1080)
root.minsize(width=1200, height=900)
root.title("Automated Attendance System Based on Facial Recognition")
window=root
abcd=root

ab=0
global k,confirm,fid,fpass,fname,r
count= 1
# while count == 1:
#     number = random.randint(1,18)
#     #q=random.randint(1,18)
#     if number == 1:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\1.png"
#         p='right'
#         q="limegreen"
#         count = 0
#         gh='left'
        
#     elif number == 2:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\2.png"
#         p='left'
#         count = 0
#         q="lightblue"
#         gh='right'
        
#     elif number == 3:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\3.png"
#         p='right'
#         count = 0
#         q="orange"
#         gh='left'
        
#     elif number == 4:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\4.png"
#         p='left'
#         count = 0
#         q="cyan"
#         gh='right'
        
#     elif number == 5:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\5.png"
#         p='right'
#         count = 0
#         q="lime"
#         gh='left'
        
#     elif number == 6:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\6.png"
#         p='right'
#         count = 0
#         q="teal"
#         gh='left'
        
#     elif number == 7:
#         myimg= "C:\\Users\\Pavan\\Pictures\\Screenshots\\7.png"
#         p='right'
#         count=0
#         q="teal"
#         gh='left'
        
#     elif number == 8:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\8.png"
#         count = 0
#         p='left'
#         q="Lavender"
#         gh='right'
        
#     elif number == 9:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\9.png"
#         count = 0
#         p='right'
#         q="brown"
#         gh='left'
        
#     elif number == 10:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\10.png"
#         count = 0
#         p='right'
#         q="beige"
#         gh='left'
        
#     elif number == 11:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\11.png"
#         count = 0
#         p='right'
#         q="olive"
#         gh='left'
        
#     elif number == 12:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\12.png"
#         count = 0
#         p='right'
#         q="cyan"
#         gh='left'
        
#     elif number == 13:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\13.png"
#         count = 0
#         p='right'
#         q="olive"
#         gh='left'
        
#     elif number == 14:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\14.png"
#         count=0
#         p='right'
#         q="orange"
#         gh='left'
        
#     elif number == 15:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\15.png"
#         count = 0
#         p='right'
#         q="beige"
#         gh='left'
        
#     elif number == 16:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\16.png"
#         count = 0
#         p='right'
#         q="lightgreen"
#         gh='left'
        
#     elif number == 17:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\17.png"
#         count = 0
#         p='right'
#         q="cyan"
#         gh='left'
        
#     elif number == 18:
#         myimg = "C:\\Users\\Pavan\\Pictures\\Screenshots\\18.png"
#         count=0
#         p='right'
#         q="orange"
#         gh='left'
p='right'
q="limegreen"
count = 0
gh='left'
myimg="https://www.asu.edu/sites/default/files/2022-04/Charter-FullWidth-AcademicLeadership.jpeg"     
response = requests.get(myimg)
img_bytes = BytesIO(response.content)
image = Image.open(img_bytes)
image=image.resize((1600,1080))
photo = ImageTk.PhotoImage(image)
global login_by,logs
global message
global message2
global i,e1,e2,txt,txt2,x,abc,abcde,txt3
i=3

'''final code for login section  is start here  '''    
l_login=tk.Label(image=photo)
global lidz,lidp,lidy,flogin,may,btnx
GITHUB_TOKEN = "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"
def upload_to_DB(repo_url, file_path, df, branch='main'):
    # Convert DataFrame to CSV string
    csv_content = df.to_csv(index=False)

    # Encode file content to base64
    encoded_content = base64.b64encode(csv_content.encode()).decode()

    # Create URL for API endpoint
    api_url = f"{repo_url.rstrip('/')}/contents/{file_path.lstrip('/')}"

    # Make GET request to fetch existing file details
    response = requests.get(api_url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    if response.status_code == 200:
        existing_file = response.json()
        sha = existing_file['sha']
    elif response.status_code == 404:
        # File does not exist, SHA is not needed
        sha = None
    else:
        print(f"Failed to fetch file details. Status code: {response.status_code}")
        print(response.json())
        return

    # Create payload for creating/updating the file
    payload = {
        "message": "Upload file",
        "content": encoded_content,
        "branch": branch,
        "sha": sha  # Include the SHA hash
    }

    # Make PUT request to create/update file
    response = requests.put(api_url, json=payload, headers={"Authorization": f"token {GITHUB_TOKEN}"})

    if response.status_code == 200:
        print("File uploaded successfully.")
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
        print(response.json())
        
def get_file_sha(repo_url, file_path, token):
    # API URL for fetching file details
    api_url = f"{repo_url}/contents/{file_path}"
    
    # Make GET request to fetch file details
    headers = {"Authorization": f"token {token}"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        file_details = response.json()
        return file_details['sha']
    else:
        print(f"Failed to fetch file details. Status code: {response.status_code}")
        print(response.json())
        return None

def upload_list_to_DB(repo_url, file_path, my_list, headers, token,branch='main'):
    # Convert the list to CSV format
    csv_data = '\n'.join(','.join(map(str, row)) for row in [headers] + my_list) if headers else '\n'.join(','.join(map(str, row)) for row in my_list)
    print(csv_data)
    # Create payload for creating/updating the file
    encoded_content = base64.b64encode(csv_data.encode()).decode()
    payload = {
        "message": "Upload CSV list",
        "content": encoded_content,
        "branch": branch,  # Specify the branch,
        "sha": get_file_sha(repo_url, file_path, token) 
    }

    # API URL for the file endpoint
    api_url = f"{repo_url}/contents/{file_path}"

    # Make PUT request to create/update the file
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.put(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("List uploaded successfully as CSV.")
    else:
        print(f"Failed to upload list as CSV. Status code: {response.status_code}")
        print(response.json())

def exit():
    global flogin,btnx,i
    i=3
    lb8=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=7,pady="10")
    flogin.destroy()
    root.after(0,root.iconify)
    root.after(0,root.deiconify)
    
def Done():
    
    global lidz,lidp,lidy,flogin,may,btnx
    x=lidz.get()
    y=lidp.get()
    a=lid.get()
    b=lpass.get()
    c=lidy.get()
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
    data=pd.read_csv(url)

    d=data["Name"][may]
    if x!="" and y!="":
        if x==y:
            lbo=tk.Label(flogin,text="Enter New Password:",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lbm=tk.Label(flogin,text="Confirm New Password:",font="lucida 10 bold").grid(column=0,row=4,pady="4")
       
            lines=list()
            qp=0
            temp_file_path = tempfile.NamedTemporaryFile(mode='w', delete=False).name
            data.to_csv(temp_file_path, index=False)
            with open(temp_file_path, 'r') as readFile:
                reader = csv.reader(readFile)
                i=0
                for row in reader:
                    if row:
                        lines.append(row)
                        if qp!=1:
                            if row[0]!=''and row[0]!="Id":
                                if str(int(float(row[0]))) == str(a):
                                    lines.remove(row)
                                    qp=1
                                    
                        
            i=0         
            while i<len(lines):
                j=0
                
                while j<4:
                    if lines[i][j]=='':
                        
                        lines.pop(i)
                        i-=1
                        break
            
                    j+=1    
                i+=1            
                       
#             with open(url, 'w') as writeFile:
#                 writer = csv.writer(writeFile)
#                 writer.writerows(lines)
#             writeFile.close()
            row=[a,d,x,c]
            lines.append(row)
            repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
            file_path = "data/FacultyDetails.csv"
            upload_list_to_DB(repo_url, file_path, lines[1:], headers=lines[0], token=GITHUB_TOKEN)
#             upload = pd.DataFrame(lines, columns=['Id', 'Name','Password','DOB'])
#             upload_to_DB(repo_url, file_path, upload)
#             with open(url,'a+') as csvFile:
#                     writer = csv.writer(csvFile)
#                     writer.writerow(row)
#             csvFile.close()
           # line=list()
           # with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\FacultyDetails\\FacultyDetails.csv', 'r') as readFile:
            #    reader = csv.reader(readFile)
             #   for row in reader:
              #      if row:
               #         line.append(row)
            #with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\FacultyDetails\\FacultyDetails.csv', 'w') as writeFile:
             #   writer = csv.writer(writeFile)
              #  writer.writerows(line)
            #writeFile.close()            
            lba=tk.Label(flogin,text="Password Changed Successfully",bg="green",fg="black",font="lucida 10 bold",width="35",pady="4").grid(columnspan=2,row=6,pady="10")
            btn=tk.Button(flogin,text="Exit",bg="white",fg="black",width="10",font="lucida 10 bold",command=exit)
            btn.grid(columnspan=3,row=5,pady="10")
            btnx.destroy()
            #root.withdraw() #hide the window
            root.after(0,root.iconify)
            root.after(0,root.deiconify)
        else:
            lba=tk.Label(flogin,text="Passwords Mismatched",bg="red",fg="black",font="lucida 10 bold",width="35",pady="4").grid(columnspan=2,row=6,pady="10")
    else:
        if x=="" and y=="":
            lbo=tk.Label(flogin,text="Enter New Password:",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lbm=tk.Label(flogin,text="Confirm New Password:",bg="red",font="lucida 10 bold").grid(column=0,row=4,pady="4")
        elif x=="" and y!="":
            lbo=tk.Label(flogin,text="Enter New Password:",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lbm=tk.Label(flogin,text="Confirm New Password:",font="lucida 10 bold").grid(column=0,row=4,pady="4")
        
        elif x!="" and y=="":
            lbo=tk.Label(flogin,text="Enter New Password:",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lbm=tk.Label(flogin,text="Confirm New Password:",bg="red",font="lucida 10 bold").grid(column=0,row=4,pady="4")
            
def Update():
    global lidz,lidp,lidy,may,flogin
    l=lidy.get()
    
    if l!="":
        url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
        data=pd.read_csv(url)
        lbn=tk.Label(flogin,text="what is your date of birth:",width=28,font="lucida 10 bold").grid(column=0,row=2,pady="4")
        if str(l)==str(data["DOB"][may]):
            lbn=tk.Label(flogin,text="what is your date of birth:",width=29,font="lucida 10 bold").grid(column=0,row=2,pady="4")     

            lba=tk.Label(flogin,text="Date of Births Matched",bg="limegreen",fg="black",font="lucida 10 bold",width="35",pady="4").grid(columnspan=2,row=6,pady="10")
            lbo=tk.Label(flogin,text="Enter New Password:",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lidz=tk.StringVar()
            ea=tk.Entry(flogin,textvariable=lidz,width="28").grid(column=1,row=3)
            lbm=tk.Label(flogin,text="Confirm New Password:",font="lucida 10 bold").grid(column=0,row=4,pady="4")
            lidp=tk.StringVar()
            eb=tk.Entry(flogin,textvariable=lidp,width="28",show="*").grid(column=1,row=4)
            btn=tk.Button(flogin,text="Done",bg="limegreen",fg="white",width="10",font="lucida 10 bold",command=Done)
            btn.grid(columnspan=3,row=5,pady="10")
            #root.iconify()
            #root.withdraw() #hide the window
            root.after(0,root.iconify)
            root.after(0,root.deiconify)
    
        else:
            lbn=tk.Label(flogin,text="what is your date of birth:",bg="red",width=29,font="lucida 10 bold").grid(column=0,row=2,pady="4")     

            lba=tk.Label(flogin,text="Date of Births Mismatched",bg="red",fg="black",font="lucida 10 bold",width="35",pady="4").grid(columnspan=2,row=6,pady="10")
    else:
        lbn=tk.Label(flogin,text="what is your date of birth:",bg="red",width=29,font="lucida 10 bold").grid(column=0,row=2,pady="4")     


global roo        
def forgot():
    global i
    i=3
    lid1=lid.get()
    lpass1=lpass.get()
    global btnx,logs,roo
    if logs==1:
        logs=0
        roo.destroy()
    lb8=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=7,pady="10")    
    if lid1!="":
        r=0
        g=0
        if is_number(lid1):
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
            ad=pd.read_csv(url)
            while r<ad["Id"].size:
                if not math.isnan(ad["Id"][r]):
                    if str(ad["Id"][r])==str(lid1):
                        g=1
                        break
                    if int(ad["Id"][r])==int(lid1):
                        g=1
                        break
                r+=1
            if g==1:    
                lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                root.after(0,root.iconify)
        #root.overrideredirect(1)
            #root.withdraw() #hide the window
                root.after(0,root.deiconify)
                global lidz,lidp,lidy,flogin,may
                lidx=lid.get()
    
                flogin=tk.Frame(l_login,pady=60)
                lbo=tk.Label(flogin,text="Forgot/Change Password",bg="orange",fg="blue",font="lucida 10 bold",width="45",pady="4").grid(columnspan=3,row=0,pady="10")
                data=pd.read_csv(url)
                lbm=tk.Label(flogin,text="Security Question",bg="white",fg="black",font="lucida 10 bold underline",width="35",pady="4").grid(columnspan=2,row=1,pady="10")
                lbn=tk.Label(flogin,text="what is your date of birth:",width=28,font="lucida 10 bold").grid(column=0,row=2,pady="4")
                lidy=tk.StringVar()
                e=tk.Entry(flogin,textvariable=lidy,width="15").grid(column=1,row=2)
                j=0
    
                while j<data["Id"].size:
        
                    if not math.isnan(data["Id"][j]):
                        if str(data["Id"][j])==str(lid1):
                            may=j
                
                            break
                        if str(int(data["Id"][j]))==str(lid1):
                            may=j
                            break
                    j+=1
    
    
        
                l=lidy.get()
                btn1=tk.Button(flogin,text="Update",bg="green",fg="white",width="10",font="lucida 10 bold",command=Update)
                btn1.grid(columnspan=3,row=5,pady="10")
                btnx=tk.Button(flogin,text="Exit",bg="white",fg="black",width="10",font="lucida 10",command=exit)
                btnx.grid(columnspan=3,row=7,pady="10")
                flogin.pack(pady="130",side=gh)
            else:
                lb1=tk.Label(f_login,text="Login ID: ",bg="red",font="lucida 10 bold").grid(column=0,row=2,pady="4")
        else:
            lb1=tk.Label(f_login,text="Login*ID*: ",bg="red",font="lucida 9 bold").grid(column=0,row=2,pady="4")
    else:
        lb1=tk.Label(f_login,text="Login ID: ",bg="red",font="lucida 10 bold").grid(column=0,row=2,pady="4")


    

def logout():
    global roo,logs
    if logs==1:
        roo.destroy()
        logs=0
global counts,dob
counts=0
logs=0
def is_numbes(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
def Logi():
    lid1=lid.get()
    lpass1=lpass.get()
    if lid1!="" and lpass1!="":
        if is_numbes(lid1):
            url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
            data=pd.read_csv(url)
            j=0
            flag=0
            #lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
        #print(lid1)
            while j<data["Id"].size:
                if  not math.isnan(data["Id"][j]):
            
                    if int(data["Id"][j])!=int(lid1):
                        flag=1
                  
                    else:
                    
                        flag=0
                        abc=j
                        break
                j+=1
            if data["Password"].size!=0 and flag==0 and (str(data["Password"][j])==str(lpass1) or (is_number(data["Password"][j]) and str(int(data["Password"][j]))==str(lpass1))) :
                lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                lb7=tk.Label(f_login,width="42",pady="4").grid(columnspan=2,row=8,pady="10")
                lb6=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=5,pady="10")
                lb5=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=6,pady="10")
                btn=tk.Button(f_login,text="Login/Signup",bg="green",fg="black",width="13",font="lucida 10 bold",command=Login)
                btn.grid(column=0,row=5,pady="10")
                btn1=tk.Button(f_login,text="Forgot/Change Password",fg="black",width="22",font="lucida 8",command=forgot)
                btn1.grid(column=1,row=6,pady="10")
                btn2=tk.Button(f_login,text="Logout",fg="black",width="10",font="lucida 8",command=logout)
                btn2.grid(columnspan=1,row=6,pady="10")
                Login()
            
            else:
                if j<data["Id"].size and (str(data["Password"][j])==str(lpass1)or (is_number(data["Password"][j]) and str(int(data["Password"][j]))==str(lpass1))):
                    lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                    lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                    Login()
                elif j<data["Id"].size:
                    lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                    lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                    lb6=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=5,pady="10")
                    lb5=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=6,pady="10")
                    btn1=tk.Button(f_login,text="Forgot/Change Password",fg="black",width="22",font="lucida 8",command=forgot)
                    btn1.grid(columnspan=1,row=5,pady="10")
                    btn2=tk.Button(f_login,text="Logout",fg="black",width="10",font="lucida 8",command=logout)
                    btn2.grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=7,pady="10")
                    Login()
        else:
            #lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb1=tk.Label(f_login,text="Login *ID*:",bg="red",font="lucida 9 bold").grid(column=0,row=2,pady="4")
            
    else:
        if lpass1=="" and lid1!="":
            lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
       
    
        elif lid1=="" and lpass1!="":
        
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold",bg="red").grid(column=0,row=2,pady="4")
        
            lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
        elif lid1=="" and lpass1=="":
        
            lb1=tk.Label(f_login,text="Login ID: ",bg="red",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
global e1,e2,mnq
mnq=0
def Login():
    
    lb6=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=7,pady="10")
    global login_by,e1,e2,mnq
    global message,logs,counts,dob,roo
    global i
    global k,confirm,fid,fpass,fname,r,abc,abcde
    lid1=lid.get()
    lpass1=lpass.get()
    facultyId=lid1
    facultypassword=lpass1
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
    data=pd.read_csv(url)
    if is_numbes(lid1) and (lid1!="" and lpass1!=""):
        j=0
        flag=0
    
        while j<data["Id"].size:
            if not math.isnan(data["Id"][j]):
            
                if int(data["Id"][j])!=int(lid1):
                    flag=1
            
                else:
                    
                    flag=2
                    abc=j
                    break
            j+=1
        
    
        if(flag==2):
            if(lpass1!=""):
                
                if (str(data["Password"][abc])==str(lpass1)) or(is_number(data["Password"][abc]) and str(int(data["Password"][abc]))==str(lpass1)):
                    if logs==0:
                        logs=1
                            
                        login_allow()
                    
                    
                    else:
                        
                        logs=1
                        roo.destroy()
                    
                    #e1=tk.Entry(f_login,textvariable=lid,width="26").grid(column=1,row=2)
                        login_allow()
                
                else:
                    mnq=1
                    p=str(i-1)
                    lb5=tk.Label(f_login,text=p+" Attempts Left",bg="red",fg="blue",font="lucida 10 bold",width="17",pady="3").grid(columnspan=1,row=7,pady="10")    
                    if(i-1)==0:
                        i=4
                    #e1.delete(first=0,last=26)
                    #e2.delete(first=s0,last=26)
                    #window.destroy()
                        lb6=tk.Label(f_login,width="42",borderwidth="2",pady="4").grid(columnspan=2,row=7,pady="10")
                    
                    if logs==1:
                        roo.destroy()
                        logs=0
                    i=i-1
            else:
                lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold",bg="red").grid(column=0,row=2,pady="4")
                lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
           
        
        elif(flag==1or data["Id"].size==0):
        
            if lpass1!="":
                if logs==1:
                    logs=0
                    roo.destroy()
                lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")

                lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="18",pady="4").grid(columnspan=1,row=5,pady="10")
                fname=tk.StringVar()
                e1=tk.Entry(f_login,textvariable=fname,width="23",borderwidth=4).grid(column=1,row=5)
                lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="18",pady="4").grid(columnspan=1,row=6,pady="10")
           
                confirm=tk.StringVar()
                e2=tk.Entry(f_login,textvariable=confirm,width="23",show="*",borderwidth=4).grid(column=1,row=6)
                lb7=tk.Label(f_login,text="DOB(dd/mm/yyyy):",fg="black",font="lucida 10 bold",width="18",pady="4").grid(columnspan=1,row=7,pady="10")
                dob=tk.StringVar()
                e3=tk.Entry(f_login,textvariable=dob,width="23",borderwidth=4).grid(column=1,row=7)
                btn=tk.Button(f_login,text="Signup",bg="green",fg="white",width="8",pady="0",font="lucida 9 bold",command=Signup)
                btn.grid(columnspan=1,row=8,pady="10")
                btn1=tk.Button(f_login,text="Login",bg="green",fg="white",width="8",pady="0",font="lucida 9 bold",command=Logi)
                btn1.grid(column=1,row=8,pady="10")
                x=fname.get()
                abcde=x
        
            else:
                lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
    else:
        #lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
        if(lid1!="" and lpass1!=""):
            lb1=tk.Label(f_login,text="Login *ID*:",bg="red",font="lucida 9 bold").grid(column=0,row=2,pady="4")
            lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")

        elif lpass1=="" and lid1!="":
            lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
       
    
        elif lid1=="" and lpass1!="":
        
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold",bg="red").grid(column=0,row=2,pady="4")
        
            lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
        elif lid1=="" and lpass1=="":
        
            lb1=tk.Label(f_login,text="Login ID: ",bg="red",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")


    
f_login=tk.Frame(l_login,pady="45")
lb0=tk.Label(f_login,text="Enter Details",bg="orange",fg="blue",font="lucida 10 bold",width="35",pady="4").grid(columnspan=3,row=0,pady="10")
lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
lid=tk.StringVar()
e1=tk.Entry(f_login,textvariable=lid,width="26").grid(column=1,row=2)

lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
lpass=tk.StringVar()
e2=tk.Entry(f_login,textvariable=lpass,width="26",show="*").grid(column=1,row=3)
btn=tk.Button(f_login,text="Login/Signup",bg="green",fg="black",width="13",font="lucida 10 bold",command=Login)
ark=0
btn.grid(column=0,row=5,pady="10")
btn1=tk.Button(f_login,text="Forgot/Change Password",fg="black",width="22",font="lucida 8",command=forgot)
btn1.grid(column=1,row=6,pady="10")
btn2=tk.Button(f_login,text="Logout",fg="black",width="10",font="lucida 8",command=logout)
btn2.grid(columnspan=1,row=6,pady="10")
f_login.pack(pady="130",side=p)
l_login.pack(ipady="150",ipadx="165",fill=tk.BOTH)

def xm():
    global roo,logs
    if logs==1:
        logs=0
        roo.destroy()
    root.destroy()    
root.protocol('WM_DELETE_WINDOW',xm)

        
k=0
def Signup():
    global roo,k,confirm,fid,fname,fpass,r,dob,logs,mnq

    global f_login
    if mnq==1:
        mnq=0
        Login()
    pqr=lid.get()
    fpass=lpass.get()
    r=confirm.get()
    m=fname.get()
    fid=lid.get()
    birth=dob.get()
    if pqr!="" and fpass!="":
        j=0
        flag=1
        url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
        data=pd.read_csv(url)
        while j<data["Id"].size:
            if not math.isnan(data["Id"][j]):
                
                if str(int(data["Id"][j]))!=str(pqr):
                    flag=1
                
                else:
                    
                    flag=2
                    abc=j
                    break
            j+=1
        lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
        lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")    
        if flag==1:
            
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
            lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
            lb7=tk.Label(f_login,text="DOB(dd/mm/yyyy):",fg="black",font="lucida 10 bold",width="18",pady="4").grid(columnspan=1,row=7,pady="10")
            if m!="" and r!="" and birth!="" and m.isalpha():
                od=len(birth)
                dd=""
                mm=""
                yyyy=""
                flask=0
                ot=0
                if od==10:
                    flask=0
                    if birth[2]=="/" and birth[5]=="/":
                        flask=0
                        ij=0
                        while ij<od:
                            if ij!=2 and ij!=5:
                                if birth[ij]=="0" or birth[ij]=="1" or birth[ij]=="2" or birth[ij]=="3" or birth[ij]=="4" or birth[ij]=="5" or birth[ij]=="6" or birth[ij]=="7" or birth[ij]=="8" or birth[ij]=="9":
                                    ot=1
                                else:
                                    ot=0
                                    break
                            ij+=1
                        if ot==1:
                            flask=0
                            dd=birth[0]+birth[1]
                            mm=birth[3]+birth[4]
                            yyyy=birth[6]+birth[7]+birth[8]+birth[9];
                            dd=int(dd)
                            mm=int(mm)
                            year=int(yyyy)
                            if (dd>=1and dd<=31) and (mm>=1 and mm<=12):
                                flask=0
                                if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
                                    if dd>=1 and dd<=31:
                                        flask=0
                                    else:
                                        flask=1
                                
                                elif mm!=2:
                                    if dd>=1 and dd<=30:
                                        flask=0
                                    else:
                                        flask=1
                                
                                else:
                                    ox=0
                                    if (year % 4) == 0:
                                        if (year % 100) == 0:
                                            if (year % 400) == 0:
                                                ox=0
                                            else:
                                                ox=1
                                        
                                        else:
                                            ox=0
                                    
                                    else:
                                        ox=1
                                
                                    if ox==0:
                                        if dd>=1 and dd<=29:
                                            flask=0
                                        else:
                                            flask=1
                                    else:
                                        if dd>=1 and dd<=28:
                                            flask=0
                                        else:
                                            flask=1
                            else:
                                flask=1
                        else:
                            flask=1                
                    else:
                        flask=1
                else:
                    flask=1
                if flask==0:
                    lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                    lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb7=tk.Label(f_login,text="DOB(dd/mm/yyyy):",fg="black",font="lucida 10 bold",width="18",pady="4").grid(columnspan=1,row=7,pady="10")
                    if(r==fpass):
                        lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                        lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")   
                        row=[fid,m,fpass,birth]
                        repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                        file_path = "data/FacultyDetails.csv"
                        #newrow = pd.DataFrame([row], columns=['Id', 'Name','Password','DOB'])
                        row=[fid, m,fpass,birth]
                        lines=data.values.tolist()
                        lines.append(row);
                        upload_list_to_DB(repo_url, file_path, lines, headers=['Id','Name','Password','DOB'], token=GITHUB_TOKEN)
                        #newrrow = pd.DataFrame.from_dict(row)
                        #updated_df = pd.concat([data, newrow], ignore_index=True)
                        #upload_to_DB(repo_url, file_path, updated_df)
#                         with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\FacultyDetails\\FacultyDetails.csv','a+') as csvFile:
#                                 writer = csv.writer(csvFile)
#                                 writer.writerow(row)
#                         csvFile.close()
                
                        lb6=tk.Label(f_login,width="42",pady="4").grid(columnspan=2,row=5,pady="10") 
                        bta=tk.Button(f_login,text="Login/Signup",bg="green",fg="black",width="10",font="lucida 10 bold",command=Login)
                        bta.grid(column=0,row=5,pady="10")
                        lb7=tk.Label(f_login,width="42",pady="4").grid(columnspan=2,row=6,pady="10")
                        btnn=tk.Button(f_login,text="Forgot/Change Password",fg="black",width="22",font="lucida 8",command=forgot)
                        btnn.grid(column=1,row=6,pady="10")
                        lb6=tk.Label(f_login,width="42",pady="4").grid(columnspan=2,row=7,pady="10")
                        btnm=tk.Button(f_login,text="Logout",fg="black",width="7",font="lucida 8",command=logout)
                        btnm.grid(columnspan=1,row=6,pady="10")
                        lbj=tk.Label(f_login,width="42",pady="4").grid(columnspan=3,row=8,pady="10")
                        lbi=tk.Label(f_login,text="Signed Up Successfully",bg="limegreen",fg="black",font="lucida 10 bold",width="35",pady="3").grid(columnspan=2,row=7,pady="10")
                        lb6=tk.Label(f_login,width="42",pady="4").grid(columnspan=2,row=8,pady="10")

                    else:
                        lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                        lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold",bg="red").grid(column=0,row=3,pady="4")
                        lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                        lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                        lb7=tk.Label(f_login,text="DOB(dd/mm/yyyy):",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")
                else:
                    lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                    lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb7=tk.Label(f_login,text="DOB(dd/mm/yyyy):",bg="red",fg="black",font="lucida 10 bold",width="18",pady="4").grid(columnspan=1,row=7,pady="10")

            else:
                lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
                lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
                if not m.isalpha() and m!="":
                    lb5=tk.Label(f_login,text="Enter *UserName*:",bg="red",fg="black",font="lucida 9 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    if r=="" and birth=="":
                        lb5=tk.Label(f_login,text="Enter *UserName*:",bg="red",fg="black",font="lucida 9 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                        lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                        lb7=tk.Label(f_login,text="Date of Birth:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")
                        
                    elif r!="" and birth=="":
                        lb5=tk.Label(f_login,text="Enter *UserName*:",bg="red",fg="black",font="lucida 9 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                        lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                        lb7=tk.Label(f_login,text="Date of Birth:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")
                    
                    elif r=="" and birth!="":
                        lb5=tk.Label(f_login,text="Enter *UserName*:",bg="red",fg="black",font="lucida 9 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                        lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                        lb7=tk.Label(f_login,text="Date of Birth:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")
                        
                elif m==""  and r=="" and birth=="":
                    lb5=tk.Label(f_login,text="Enter UserName:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")

            
                elif m!="" and r=="" and birth!="":
                    lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")

                elif m=="" and r!="" and birth=="":
                    lb5=tk.Label(f_login,text="Enter UserName:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")

                elif m=="" and r=="" and birth!="":
                    lb5=tk.Label(f_login,text="Enter UserName:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")

                elif m=="" and r!="" and birth!="":
                    lb5=tk.Label(f_login,text="Enter UserName:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")

                elif m!="" and r=="" and birth=="":
                    lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")

                elif m!="" and r!="" and birth=="":
                    lb5=tk.Label(f_login,text="Enter UserName:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=5,pady="10")
                    lb4=tk.Label(f_login,text="Confirm Password:",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=6,pady="10")
                    lb7=tk.Label(f_login,text="Date of Birth:",bg="red",fg="black",font="lucida 10 bold",width="15",pady="4").grid(columnspan=1,row=7,pady="10")
        else:
            lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            lb7=tk.Label(f_login,width="42",pady="4").grid(columnspan=2,row=8,pady="11")
            lb6=tk.Label(f_login,width="42",borderwidth="2",pady="5").grid(columnspan=2,row=5,pady="10")
            lb5=tk.Label(f_login,width="42",borderwidth="2",pady="5").grid(columnspan=2,row=6,pady="10")
            lb8=tk.Label(f_login,width="42",borderwidth="2",pady="5").grid(columnspan=2,row=7,pady="10")
            
            btn=tk.Button(f_login,text="Login/Signup",bg="green",fg="black",width="13",font="lucida 10 bold",command=Login)
            btn.grid(column=0,row=5,pady="10")
            btn1=tk.Button(f_login,text="Forgot/Change Password",fg="black",width="22",font="lucida 8",command=forgot)
            btn1.grid(column=1,row=6,pady="10")
            btn2=tk.Button(f_login,text="Logout",fg="black",borderwidth="2",width="10",font="lucida 8",command=logout)
            btn2.grid(columnspan=1,row=6,pady="10")
            
            
    else:
        if fpass=="" and pqr!="":
            lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
       
    
        elif pqr=="" and fpass!="":
        
            lb1=tk.Label(f_login,text="Login ID: ",font="lucida 10 bold",bg="red").grid(column=0,row=2,pady="4")
        
            lb2=tk.Label(f_login,text="Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
        elif pqr=="" and fpass=="":
        
            lb1=tk.Label(f_login,text="Login ID: ",bg="red",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            lb2=tk.Label(f_login,text="Password: ",bg="red",font="lucida 10 bold").grid(column=0,row=3,pady="4")

def quit(*fu):
    
    def quit(*args, **kwargs):
        global logs,counts
        logs=0
        counts=1
        for f in fu:
            f(*args, **kwargs)
            
    return quit

def login_allow():
    global roo
    global abc,logs
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
    data=pd.read_csv(url)
    roo = tk.Tk()
    mk=lid.get()
    global message
    global message2,txt,txt2,txt3
    logs=1
    x=0
    
    roo.title(str(data["Name"][abc])+"-Logged In")
   
    roo.configure(background=q)
    roo.grid_rowconfigure(0, weight=1)
    roo.grid_columnconfigure(0, weight=1)
    
    
    roo.protocol('WM_DELETE_WINDOW',quit(roo.destroy))
    roo.state('zoomed')   
    message = tk.Label(roo, text="Automated  Attendance  Based  On  Face  Recognition  System" ,bg="yellow"  ,fg="cornflowerblue"  ,width=49  ,height=3,font=( 'times',25, 'italic bold underline')) 

    message.place(x=300, y=10)
    lb3 = tk.Label(roo, text="Enter ID:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
    lb3.place(x=50, y=150)
    
    txt = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
    txt.place(x=350, y=165)
    lbl = tk.Label(roo, text="Enter Name:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=50, y=250)

    txt2 = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
    txt2.place(x=350, y=265)

    lbl2 = tk.Label(roo, text="Enter Password:",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=50, y=350)
    txt3 = tk.Entry(roo,width=20  ,bg="yellow"  ,show="*",fg="red",font=('times', 15, ' bold ')  )
    txt3.place(x=350, y=365)

    lbl3 = tk.Label(roo, text="Notification : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline ')) 
    lbl3.place(x=50, y=450)
    
    message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message.place(x=350, y=450)

    clearButton4 = tk.Button(roo, text="Register", command=register  ,fg="green"  ,bg="yellow"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton4.place(x=75, y=55)  

    clearButton = tk.Button(roo, text="Clear All", command=clear  ,fg="green"  ,bg="yellow"  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton.place(x=600, y=155)
    clearButton2 = tk.Button(roo, text="Edit Your Name", command=editname  ,fg="green"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton2.place(x=600, y=255)
    clearButton3 = tk.Button(roo, text="Forgot", command=forgo  ,fg="green"  ,bg="yellow"  ,width=8  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton3.place(x=600, y=355)
    clearButton3 = tk.Button(roo, text="Change Password", command=changepassword  ,fg="green"  ,bg="yellow"  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton3.place(x=715, y=355)
    takeImg = tk.Button(roo, text="Take Pictures", command=TakeImages  ,fg="green"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    takeImg.place(x=100, y=550)
    trainImg = tk.Button(roo, text="Train Your Face", command=TrainImages  ,fg="green"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    trainImg.place(x=400, y=550)
    trackImg = tk.Button(roo, text="Detect Images", command=TrackImages  ,fg="green"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    trackImg.place(x=700, y=550)
    
    quitWindow = tk.Button(roo ,text="Press 'q' and Click Here to Quit",command=quit(roo.destroy),fg="green"  ,bg="yellow"  ,width=30  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    quitWindow.place(x=1000, y=550)
    copyWrite = tk.Text(roo, background=roo.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
    copyWrite.tag_configure("superscript", offset=10)
    copyWrite.insert("insert", "Developed by B2 ","", "TEAM-3")
    copyWrite.configure(state="disabled",fg="darkmagenta"  )
    copyWrite.pack(side="left")
    copyWrite.place(x=1000, y=750)
    
global tx,ty,clearButtonef,lbab,clearButtonab,lbcd,clearButtoncd,clearButtongh,lbef,tt,b1,b2,b3,b4  
b1=0
b2=0
b3=0
b4=0

def chancs():
    
    global tx,roo,lbab,clearButtonab,lbcd,clearButtonef,txt,txt2,txt3
    
    lbab.destroy()
    clearButtonef.destroy()
    clearButtonab.destroy()    
    
    tx.destroy()
def register():
    global tx,ty,lbab,clearButtonab,message,roo,lbcd,clearButtoncd,clearButtongh,lbef,clearButtonef,tt,txt,txt2,txt3,b1,b2,b3,b4
    if b2==0 and b3==0 and b4==0:
        b1=1
        lb3 = tk.Label(roo, text="Enter ID:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
        lb3.place(x=50, y=150)
    
        txt = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
        txt.place(x=350, y=165)
        lbl = tk.Label(roo, text="Enter Name:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
        lbl.place(x=50, y=250)

        txt2 = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
        txt2.place(x=350, y=265)

        lbl2 = tk.Label(roo, text="Enter Password:",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold ')) 
        lbl2.place(x=50, y=350)
        txt3 = tk.Entry(roo,width=20  ,bg="yellow" ,show="*" ,fg="red",font=('times', 15, ' bold ')  )
        txt3.place(x=350, y=365)

        lbl3 = tk.Label(roo, text="Notification : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline ')) 
        lbl3.place(x=50, y=450)
        clearButtonef = tk.Button(roo, text="Quit", command=chancs  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButtonef.place(x=1180, y=250)
    
    #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    #message.place(x=350, y=450)
        res="Please Register(New User)/Trainning Purpose(Old User)" 
        message.configure(text=res)
        lbab = tk.Label(roo, text="Enter DOB(dd/mm/yyyy):",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
        lbab.place(x=900, y=150)
        tx = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
        tx.place(x=1200, y=165)
   
        clearButtonab = tk.Button(roo, text="Done", command=dones  ,fg="orange"  ,bg="red"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButtonab.place(x=1300, y=150)
    else:
        if b2==1:
            b2=0
            chats()
            register()
            #res="Please Quit from 'Edit Your Name'"
            #message.configure(text=res)
        elif b3==1:
            b3=0
            chants()
            register()
            #res="Please Quit from 'Forgot'"
            #message.configure(text=res)
        elif b4==1:
            b4=0
            chants()
            register()
            #res="Please Quit from 'Change Password'"
            #message.configure(text=res)
            
            
    
def dong():
    global tx,message,txt,ty,lbef,clearButtongh,tt,lbab,lbcd,clearButtonab,clearButtonef
    
    
    o=tx.get()
    p=txt.get()
    q=ty.get()
    if o!="" and q!="":
            url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
            df=pd.read_csv(url)
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                         
            res="Please Register(New User)/Trainning Purpose(Old User)" 
            message.configure(text=res)
            i=0
            flag=0
            while i<df["Id"].size:
                if not math.isnan(df["Id"][i]):
                    
                    if str(int(df["Id"][i]))==str(p) and str(df["DOB"][i])==str(o):
                        flag=1
                        k=i
                        break
                   
                i+=1        
            if flag==1:
                lines=list()
                qp=0
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
                temp_file_path = tempfile.NamedTemporaryFile(mode='w', delete=False).name
                df.to_csv(temp_file_path, index=False)
                with open(temp_file_path, 'r') as readFile:
                    reader = csv.reader(readFile)
                    
                    for row in reader:
                        if row:
                            lines.append(row)
                            
                            if qp!=1:
                                if row[0]!=''and row[0]!="Id":
                                    
                                    
                                    
                                    if str(int(float(row[0]))) == str(p):
                                        lines.remove(row)
                                        qp=1
                                            
                                
                    
                i=0         
                while i<len(lines):
                    j=0
                    while j<4:
                        if lines[i][j]=='':
                            lines.pop(i)
                            i-=1
                            break
            
                        j+=1    
                    i+=1            
                        
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv', 'w') as writeFile:
#                     writer = csv.writer(writeFile)
#                     writer.writerows(lines)
#                 writeFile.close()
                row=[df["Id"][k],df["Name"][k],q,df["DOB"][k]]
                lines.append(row)
                print("1147")
                print(lines)
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                file_path = "data/StudentDetails/StudentDetails.csv"
                upload_list_to_DB(repo_url, file_path, lines[1:], headers=lines[0], token=GITHUB_TOKEN)
                #upload = pd.DataFrame(lines, columns=['Id','Name','Password','DOB'])
                #upload_to_DB(repo_url, file_path, upload)
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv','a+') as csvFile:
#                     writer = csv.writer(csvFile)
#                     writer.writerow(row)
#                 csvFile.close()
                lbab.destroy()
                lbcd.destroy()
                clearButtonab.destroy()
                clearButtonef.destroy()
                tx.destroy()
                ty.destroy()
                lbef = tk.Label(roo, text="Your Password is Updated Successfully",width=35 ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                lbef.place(x=1000, y=250)
                #clearButtongh = tk.Button(roo, text="Quit", command=change  ,fg="green"  ,bg="yellow"  ,width=5 ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                #clearButtongh.place(x=1180, y=355)
                lbef.after(1000, lbef.destroy) 
                                        
            else:                                        
                res="Date Of Birth is Incorrect(dd/mm/yyyy)" 
                message.configure(text=res)
                                              
    else:
        if o!="" and q=="":
            res="Please Enter Your New Password"
            message.configure(text=res)   
        elif o=="" and q!="":
            res="Please Enter Your Date Of Birth"
            message.configure(text=res)
        elif o=="" and q=="":
            res="Please Enter Your Date Of Birth and New Password"
            message.configure(text=res)
def forgo():
    global tx,ty,lbab,clearButtonab,message,roo,lbcd,clearButtoncd,clearButtongh,lbef,clearButtonef,tt,txt,txt2,txt3,b1,b2,b3,b4
    n=txt.get()
    if b1==0 and b2==0 and b4==0:
        b3=1
        if n!="":
            res="Please Register(New User)/Trainning Purpose(Old User)" 
            message.configure(text=res)
        #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                             
            if is_number(n):
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                         
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
                i=0
                flag=0
                url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
                df=pd.read_csv(url)
                while i<df["Id"].size:
                    if not math.isnan(df["Id"][i]):
                        if int(df["Id"][i])==int(n):
                            flag=1
                            tt=i
                            break
                    i+=1
                if flag==1:
                    lbab = tk.Label(roo, text="What is your DOB?",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                    lbab.place(x=900, y=150)
                    tx = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
                    tx.place(x=1200, y=165)
                    lbcd = tk.Label(roo, text="Enter New Password:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                    lbcd.place(x=900, y=250)
                    ty = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
                    ty.place(x=1200, y=265)
                    clearButtonef = tk.Button(roo, text="Quit", command=chants  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                    clearButtonef.place(x=1180, y=350)
                
                    res="Please Register(New User)/Trainning Purpose(Old User)" 
                    message.configure(text=res)
                
                    clearButtonab = tk.Button(roo, text="Done", command=dong  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                    clearButtonab.place(x=1450, y=255)
                else:
                    res=" Please Enter Your Details(New User)"
                    message.configure(text=res)    
            else:
                res="Please Enter Your Numeric Id"
                message.configure(text=res)
        else:
            res="Please Enter Your Id" 
            message.configure(text=res) 
    else:
        if b1==1:
            b1=0
            chancs()
            forgo()
        elif b2==1:
            b2=0
            chats()
            forgo()
        elif b4==1:
            b4=0
            chants()
            forgo()
    
#def chan():
 #   global tx,roo,lbab,clearButtonab,lbcd,clearButtoncd,txt,txt2,txt3,clearButtonef
  #  txt.delete(0, 'end')    
   # txt2.delete(0,'end')
   # txt3.delete(0,'end')
  #  clearButtoncd.destroy()
  #  lbcd.destroy()
    
       
def dones():
    global tx,clearButtonef,lbab,clearButtonab,message,roo,lbcd,clearButtoncd,clearButtongh,lbef,tt,txt,txt2,txt3
    Id=(txt.get())
    name=(txt2.get())
    passw=(txt3.get())
    dob=(tx.get())
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
    df=pd.read_csv(url)    
    
    if Id!="" and name!="" and passw!=""and dob!="":
        i=0
        flag=0
        #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
        res="Please Register(New User)/Trainning Purpose(Old User)" 
        message.configure(text=res)

        while i<df["Id"].size:
            if not math.isnan(df["Id"][i]):
                if str(int(df["Id"][i]))==str(Id):
                    flag=1
                    break
            i+=1
        
        
        if flag==1:
            res="Already Registered with this ID" 
            message.configure(text=res)
             #message = tk.Label(roo, text="Already Registered with this ID" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
        else:
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
            res="Please Register(New User)/Trainning Purpose(Old User)" 
            message.configure(text=res)
            x=1
            i=0
            o=name
            birth=dob
            while i<len(o):
                if o[i]!="0" and o[i]!="1" and o[i]!="2" and o[i]!="3" and o[i]!="4" and o[i]!="5" and o[i]!="6" and o[i]!="7" and o[i]!="8" and o[i]!="9":
                    x=1
                else:
                    x=0
                    break
                i+=1
            od=len(birth)
            dd=""
            mm=""
            yyyy=""
            flask=0
            ot=0
            if od==10:
                flask=0
                if birth[2]=="/" and birth[5]=="/":
                    flask=0
                    ij=0
                    while ij<od:
                        if ij!=2 and ij!=5:
                            if birth[ij]=="0" or birth[ij]=="1" or birth[ij]=="2" or birth[ij]=="3" or birth[ij]=="4" or birth[ij]=="5" or birth[ij]=="6" or birth[ij]=="7" or birth[ij]=="8" or birth[ij]=="9":
                                ot=1
                            else:
                                ot=0
                                break
                        ij+=1
                    if ot==1:
                        flask=0
                        dd=birth[0]+birth[1]
                        mm=birth[3]+birth[4]
                        yyyy=birth[6]+birth[7]+birth[8]+birth[9];
                        dd=int(dd)
                        mm=int(mm)
                        year=int(yyyy)
                        if (dd>=1and dd<=31) and (mm>=1 and mm<=12):
                            flask=0
                            if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
                                if dd>=1 and dd<=31:
                                    flask=0
                                else:
                                    flask=1
                                
                            elif mm!=2:
                                if dd>=1 and dd<=30:
                                    flask=0
                                else:
                                    flask=1
                                
                            else:
                                ox=0
                                if (year % 4) == 0:
                                    if (year % 100) == 0:
                                        if (year % 400) == 0:
                                            ox=0
                                        else:
                                            ox=1
                                        
                                    else:
                                        ox=0
                                    
                                else:
                                    ox=1
                                
                                if ox==0:
                                    if dd>=1 and dd<=29:
                                        flask=0
                                    else:
                                        flask=1
                                else:
                                    if dd>=1 and dd<=28:
                                        flask=0
                                    else:
                                        flask=1
                        else:
                            flask=1
                    else:
                        flask=1                
                else:
                    flask=1
            else:
                flask=1
           
            if(is_number(Id) and x==1 and flask==0):
                
                row = [Id,name,passw,dob]
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                file_path = "data/StudentDetails/StudentDetails.csv"
                lines=df.values.tolist()
                lines.append(row);
                upload_list_to_DB(repo_url, file_path, lines, headers=['Id','Name','Password','DOB'], token=GITHUB_TOKEN)
#                 newrow = pd.DataFrame([row], columns=['Id', 'Name','Password','DOB'])
#                 updated_df = pd.concat([df, newrow], ignore_index=True)
#                 updated_df=pd.DataFrame(updated_df)
#                 upload_to_DB(repo_url, file_path, updated_df)
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv','a+') as csvFile:
#                     writer = csv.writer(csvFile)
#                     writer.writerow(row)
#                 csvFile.close()
                lbcd = tk.Label(roo, text="You have Registered Successfully",width=35 ,height=2  ,fg="green"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                lbcd.place(x=1000, y=250)
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
                #clearButtoncd = tk.Button(roo, text="Quit", command=chan  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                #clearButtoncd.place(x=1180, y=355)
                lbcd.after(1000, lbcd.destroy) 
                lbab.destroy()
                clearButtonab.destroy()
                clearButtonef.destroy()
                tx.destroy()
                
            else:
                if not name.isalpha():
                    res="Enter Alphabetical Name" 
                    message.configure(text=res)
    
                    #message = tk.Label(roo, text="Enter Alphabetical Name" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
                if not is_number(Id):
                    res= "Enter Numeric Id"
                    message.configure(text= res)
                    #message = tk.Label(roo, text="Enter Numeric Id" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
                if flask==1:
                
                    res="Invalid Date Of Birth"
                    message.configure(text=res)
                    #message = tk.Label(roo, text="Invalid Date Of Birth" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
            
    else:
        if Id=="" and name=="" and passw=="" and dob=="":
            res="Please Enter Your ID,Name,Password and Date Of Birth"
            message.configure(text=res)
        elif Id=="" and name=="" and passw=="" and dob!="":
            res="Please Enter Your ID,Name and Password"
            message.configure(text=res)
        elif Id=="" and name=="" and passw!="" and dob=="":
            res="Please Enter Your ID,Name and Date Of Birth"
            message.configure(text=res)
        elif Id=="" and name=="" and passw!="" and dob!="":
            res="Please Enter Your ID and Name"
            message.configure(text=res)    
        elif Id=="" and name!="" and passw=="" and dob=="":
            res="Please Enter Your ID,Password and Date Of Birth"
            message.configure(text=res)
        elif Id=="" and name!="" and passw=="" and dob!="":
            res="Please Enter Your ID and Password"
            message.configure(text=res)
        elif Id=="" and name!="" and passw!="" and dob=="":
            res="Please Enter Your ID and Date Of Birth"
            message.configure(text=res)    
        elif Id=="" and name!="" and passw!="" and dob!="":
            res="Please Enter Your ID"
            message.configure(text=res)
        elif Id!="" and name=="" and passw=="" and dob=="":
            res="Please Enter Your Name,Password and Date Of Birth"
            message.configure(text=res)      
        elif Id!="" and name=="" and passw=="" and dob!="":
            res="Please Enter Your Name and Password"
            message.configure(text=res)
        elif Id!="" and name=="" and passw!="" and dob=="":
            res="Please Enter Your Name and Date Of Birth"
            message.configure(text=res)
        elif Id!="" and name=="" and passw!="" and dob!="":
            res="Please Enter Your Name"
            message.configure(text=res)
        elif Id!="" and name!="" and passw=="" and dob=="":
            res="Please Enter Your Password and Date Of Birth"
            message.configure(text=res)
        elif Id!="" and name!="" and passw=="" and dob!="":
            res="Please Enter Your Password"
            message.configure(text=res)    
        elif Id!="" and name!="" and passw!="" and dob=="":
            res="Please Enter Your Date Of Birth"
            message.configure(text=res)
            
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


    
#def change():
 #   global lbef,clearButtongh
  #  lbef.destroy()
   # clearButtongh.destroy()
def dont():
    global tx,message,txt,ty,lbef,clearButtongh,tt,lbab,lbcd,clearButtonab,clearButtonef
    
    
    o=tx.get()
    p=txt.get()
    q=ty.get()
    if o!="" and q!="":
            url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
            df=pd.read_csv(url) 
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                         
            res="Please Register(New User)/Trainning Purpose(Old User)" 
            message.configure(text=res)
            i=0
            flag=0
            while i<df["Id"].size:
                if not math.isnan(df["Id"][i]):
                    if not is_number(df["Password"][i]):
                        if str(int(df["Id"][i]))==str(p) and str(df["Password"][i])==str(o):
                            flag=1
                            k=i
                            break
                    else:
                        if str(int(df["Id"][i]))==str(p) and str(int(df["Password"][i]))==str(o):
                            flag=1
                            k=i
                            break    
                i+=1        
            if flag==1:
                lines=list()
                qp=0
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
                temp_file_path = tempfile.NamedTemporaryFile(mode='w', delete=False).name
                df.to_csv(temp_file_path, index=False)
                with open(temp_file_path, 'r') as readFile:
                    reader = csv.reader(readFile)
                    
                    for row in reader:
                        if row:
                            lines.append(row)
                            
                            if qp!=1:
                                if row[0]!=''and row[0]!="Id":
                                    
                                    if str(int(float(row[0]))) == str(p):
                                        lines.remove(row)
                                        qp=1
                                            
                                
                    
                i=0         
                while i<len(lines):
                    j=0
                    while j<4:
                        if lines[i][j]=='':
                            lines.pop(i)
                            i-=1
                            break
            
                        j+=1    
                    i+=1            
                          
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv', 'w') as writeFile:
#                     writer = csv.writer(writeFile)
#                     writer.writerows(lines)
#                 writeFile.close()
                row=[df["Id"][k],df["Name"][k],q,df["DOB"][k]]
                lines.append(row)
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                file_path = "data/StudentDetails/StudentDetails.csv"
                upload_list_to_DB(repo_url, file_path, lines[1:], headers=lines[0], token=GITHUB_TOKEN)
#                 upload = pd.DataFrame(lines, columns=['Id', 'Name','Password','DOB'])
#                 upload_to_DB(repo_url, file_path, upload)
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv','a+') as csvFile:
#                     writer = csv.writer(csvFile)
#                     writer.writerow(row)
#                 csvFile.close()
                lbab.destroy()
                lbcd.destroy()
                clearButtonab.destroy()
                clearButtonef.destroy()
                tx.destroy()
                ty.destroy()
                lbef = tk.Label(roo, text="Your Password is Updated Successfully",width=35 ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                lbef.place(x=1000, y=250)
                #clearButtongh = tk.Button(roo, text="Quit", command=change  ,fg="green"  ,bg="yellow"  ,width=5 ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                #clearButtongh.place(x=1180, y=355)
                lbef.after(1000, lbef.destroy) 
                                        
            else:                                        
                res="Current Password is Incorrect" 
                message.configure(text=res)
                                              
    else:
        if o!="" and q=="":
            res="Please Enter Your New Password"
            message.configure(text=res)   
        elif o=="" and q!="":
            res="Please Enter Your Current Password"
            message.configure(text=res)
        elif o=="" and q=="":
            res="Please Enter Your Current Password and New Password"
            message.configure(text=res)

def chants():
    global tx,roo,lbab,clearButtonab,lbcd,clearButtonef,txt,txt2,txt3,ty,clearButtoncd,a1,a2,a3,a4
   
    lbab.destroy()
    a3=1
    a4=1
    clearButtonef.destroy()
    clearButtonab.destroy()
    lbcd.destroy()
    tx.destroy()
    ty.destroy()    
def changepassword():
    #global message,txt,tx,lbab,clearButtonab,tt,clearButtonef,ty,lbcd
    global tx,ty,lbab,clearButtonab,message,roo,lbcd,clearButtoncd,clearButtongh,lbef,clearButtonef,tt,txt,txt2,txt3,b1,b2,b3,b4
    if b1==0 and b2==0 and b3==0:
        b4=1
        n=txt.get()    
        if n!="":
            res="Please Register(New User)/Trainning Purpose(Old User)" 
            message.configure(text=res)
        #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                             
            if is_number(n):
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                         
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
                i=0
                flag=0
                url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
                df=pd.read_csv(url)
                while i<df["Id"].size:
                    if not math.isnan(df["Id"][i]):
                        if int(df["Id"][i])==int(n):
                            flag=1
                            tt=i
                            break
                    i+=1
                if flag==1:
                    lbab = tk.Label(roo, text="Enter Current Password:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                    lbab.place(x=900, y=150)
                    tx = tk.Entry(roo,width=20 ,show="*" ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
                    tx.place(x=1200, y=165)
                    lbcd = tk.Label(roo, text="Enter New Password:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                    lbcd.place(x=900, y=250)
                    ty = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
                    ty.place(x=1200, y=265)
                    clearButtonef = tk.Button(roo, text="Quit", command=chants  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                    clearButtonef.place(x=1180, y=350)
                
                    res="Please Register(New User)/Trainning Purpose(Old User)" 
                    message.configure(text=res)
                
                    clearButtonab = tk.Button(roo, text="Done", command=dont  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                    clearButtonab.place(x=1450, y=255)
                else:
                    res=" Please Enter Your Details(New User)"
                    message.configure(text=res)    
            else:
                res="Please Enter Your Numeric Id"
                message.configure(text=res)
        else:
            res="Please Enter Your Id" 
            message.configure(text=res) 
    else:
        if b1==1:
            b1=0
            chancs()
            changepassword()
        elif b2==1:
            b2=0
            chats()
            changepassword()
        elif b3==1:
            b3=0
            chants()
            changepassword()
        

def clear():
    global message,txt,txt2,txt3,b1,b2,b3,b4
    txt.delete(0, 'end')    
    txt2.delete(0,'end')
    txt3.delete(0,'end')
    if b1==1:
        b1=0
        chanc()
    elif b2==1:
        b2=0
        chats()
    elif b3==1:
        b3=0
        chants()
    elif b4==1:
        b4=0
        chants()
    


    
def don():
    global tx,message,lbab,clearButtonab,lbcd,clearButtoncd,txt,txt2,tt,clearButtonef
    p=txt.get()
    o=tx.get()
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
    df=pd.read_csv(url)
    #df=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv")
    if o!="":
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                         
            res="Please Register(New User)/Trainning Purpose(Old User)" 
            message.configure(text=res)
            x=1
            i=0
            while i<len(o):
                if o[i]!="0" and o[i]!="1" and o[i]!="2" and o[i]!="3" and o[i]!="4" and o[i]!="5" and o[i]!="6" and o[i]!="7" and o[i]!="8" and o[i]!="9":
                    x=1
                else:
                    x=0
                    break
                i+=1     
            if x==1:
                lines=list()
                qp=0
                temp_file_path = tempfile.NamedTemporaryFile(mode='w', delete=False).name
                df.to_csv(temp_file_path, index=False)
                with open(temp_file_path, 'r') as readFile:
                    reader = csv.reader(readFile)
                    
                    for row in reader:
                        if row:
                            lines.append(row)
                            #if lines[i][0]!='':
                            if qp!=1:
                                if row[0]!=''and row[0]!="Id":
                                    if str(int(float(row[0]))) == str(p):
                                        lines.remove(row)
                                        qp=1
                                            
                                
                i=0
                
                while i<len(lines):
                    j=0
                    while j<4:
                        if lines[i][j]=='':
                            lines.pop(i)
                            i-=1
                            break
            
                        j+=1    
                    i+=1            
                          
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv', 'w') as writeFile:
#                     writer = csv.writer(writeFile)
#                     writer.writerows(lines)
#                 writeFile.close()
                row=[p,o,df["Password"][tt],df["DOB"][tt]]
                lines.append(row)
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                file_path = "data/StudentDetails/StudentDetails.csv"
                upload_list_to_DB(repo_url, file_path, lines[1:], headers=lines[0], token=GITHUB_TOKEN)
#                 upload = pd.DataFrame(lines, columns=['Id', 'Name','Password','DOB'])
#                 upload_to_DB(repo_url, file_path, upload)
#                 with open('C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv','a+') as csvFile:
#                     writer = csv.writer(csvFile)
#                     writer.writerow(row)
#                 csvFile.close()
                lbcd = tk.Label(roo, text="Your Name is Updated Successfully",width=35 ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                lbcd.place(x=1000, y=250)
                #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
                #message.place(x=350, y=450)
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
                #clearButtoncd = tk.Button(roo, text="Quit", command=chaz  ,fg="green"  ,bg="yellow"  ,width=5 ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                #clearButtoncd.place(x=1180, y=355)
                lbcd.after(1000, lbcd.destroy) 
                lbab.destroy()
                clearButtonab.destroy()
                clearButtonef.destroy()
                tx.destroy()
            else:
                res = "Enter Alphabetical Name"
                message.configure(text= res) 
                
    else:
        res = "Please Enter Your New Name"
        message.configure(text= res)
        

def chats():
    global message,txt,txt2,tx,lbab,clearButtonab,tt,txt3,clearButtonef,a1,a2,a3,a4
    lbab.destroy()
    a2=1
    clearButtonab.destroy()
    clearButtonef.destroy()
    tx.destroy()    

def editname():
        #global message,txt,txt2,tx,lbab,clearButtonab,tt,clearButtonef
        global tx,ty,lbab,clearButtonab,message,roo,lbcd,clearButtoncd,clearButtongh,lbef,clearButtonef,tt,txt,txt2,txt3
        global b1,b2,b3,b4
        if b1==0 and b3==0 and b4==0:
            b2=1
            m=txt2.get()
            n=txt.get()
        
            if n!="":
                res="Please Register(New User)/Trainning Purpose(Old User)" 
                message.configure(text=res)
            #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                         
                if is_number(n):
                #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))                                     
                    res="Please Register(New User)/Trainning Purpose(Old User)" 
                    message.configure(text=res)
                    i=0
                    flag=0
                    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
                    df=pd.read_csv(url)
                    #df=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv")
                    while i<df["Id"].size:
                        if not math.isnan(df["Id"][i]):
                            if int(df["Id"][i])==int(n):
                                flag=1
                                tt=i
                                break
                        i+=1
                    if flag==1:
                    #message = tk.Label(roo, text="Please Register(New User)/Trainning Purpose(Old User)" ,bg="yellow"  ,fg="red"  ,width=42  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
                    #message.place(x=350, y=450)
                        res="Please Register(New User)/Trainning Purpose(Old User)" 
                        message.configure(text=res)
                        lbab = tk.Label(roo, text="Enter Your New Name:",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
                        lbab.place(x=900, y=150)
                        tx = tk.Entry(roo,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
                        tx.place(x=1200, y=165)
                        clearButtonef = tk.Button(roo, text="Quit", command=chats  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                        clearButtonef.place(x=1180, y=250)
                        clearButtonab = tk.Button(roo, text="Done", command=don  ,fg="green"  ,bg="yellow"  ,width=5  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
                        clearButtonab.place(x=1450, y=155)
                    else:
                        res=" Please Enter Your Details(New User)"
                        message.configure(text=res)    
                else:
                    res="Please Enter Your Numeric Id"
                    message.configure(text=res)
            else:
                res="Please Enter Your Id" 
                message.configure(text=res)    
    
        else:
            if b1==1:
                b1=0
                chancs()
                editname()
            elif b3==1:
                b3=0
                chants()
                editname()
            elif b4==1:
                b4=0
                chants()
                editname()
                
def is_file_present(repo_url, file_path, branch='main', token=None):
    # Create URL for API endpoint
    api_url = f"{repo_url.rstrip('/')}/contents/{file_path.lstrip('/')}"

    # Make GET request to fetch existing file details
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return True  # File exists
    elif response.status_code == 404:
        return False  # File does not exist
    else:
        print(f"Failed to fetch file details. Status code: {response.status_code}")
        print(response.json())
        return None  # Error occurred

def create_folder_if_not_exists(repo_url, folder_path, branch='main', token=None):
    # Create a dummy file inside the folder
    dummy_file_path = f"{folder_path}/.gitkeep"
    dummy_file_content = "This is a dummy file to create the folder."
    
    # Encode file content to base64
    encoded_content = base64.b64encode(dummy_file_content.encode()).decode()

    # Create payload for creating the dummy file
    payload = {
        "message": "Create folder",
        "content": encoded_content,
        "branch": branch
    }

    # Create URL for API endpoint
    api_url = f"{repo_url.rstrip('/')}/contents/{dummy_file_path.lstrip('/')}"
    
    # Make PUT request to create dummy file
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.put(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Folder '{folder_path}' created successfully.")
    elif response.status_code == 422:
        print(f"The folder '{folder_path}' already exists in the repository.")
    else:
        print(f"Failed to create folder '{folder_path}'. Status code: {response.status_code}")
        print(response.json())

def upload_image_to_DB(repo_url, folder_path, image_path, image, branch='main', token=None):
    
    # Check if the image was read successfully
    if image is None:
        print(f"Failed to read the image at '{image_path}'.")
        return
    
    # Save the image locally
    local_image_path = "temp_image.jpg"
    cv2.imwrite(local_image_path, image)
    
    # Read the image content
#     with open(local_image_path, 'rb') as file:
#         image_content = file.read()
    _, image_content = cv2.imencode('.jpg', image)

    # Encode image content to base64
    encoded_content = base64.b64encode(image_content).decode()

    # Create payload for creating the image file
    payload = {
        "message": f"Upload image '{image_path}'",
        "content": encoded_content,
        "branch": branch
    }

    # Create URL for API endpoint
    api_url = f"{repo_url.rstrip('/')}/contents/{folder_path.lstrip('/')}/{image_path.lstrip('/')}"
    
    # Make PUT request to create the image file
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.put(api_url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code==201:
        print(f"Image '{image_path}' uploaded successfully to '{folder_path}' folder.")
    else:
        print(f"Failed to upload image '{image_path}' to '{folder_path}' folder. Status code: {response.status_code}")
        print(response.json())

    # Remove the temporary image file
    #os.remove(local_image_path)


# def TakeImages():
#     global message,txt,txt2,txt3,roo
#     Id=(txt.get())
#     name=(txt2.get())
#     passw=(txt3.get())
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         roo.destroy()
#     url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
#     df=pd.read_csv(url)
#     #df=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv")
    
    
#     if Id!="" and name!="" and passw!="":
#         i=0
#         flag=0
#         kr=0
#         while i<df["Id"].size:
#             if not math.isnan(df["Id"][i]):
#                 if str(int(df["Id"][i]))==str(Id):
#                     kr=1
#                     break
#             i+=1
#         i=0    
#         while i<df["Id"].size:
#             if not math.isnan(df["Id"][i]):
#                 if not is_number(df["Password"][i]):
#                     if str(int(df["Id"][i]))==str(Id) and str(df["Password"][i])==str(passw):
#                         flag=1
#                         break
#                 else:
#                     if str(int(df["Id"][i]))==str(Id) and str(int(df["Password"][i]))==str(passw):
#                         flag=1
#                         break        
#             i+=1
#         print(flag)
#         print(kr)
#         if(flag==1 and kr==1): 
#             x=1
#             i=0
#             o=name
#             while i<len(o):
#                 if o[i]!="0" and o[i]!="1" and o[i]!="2" and o[i]!="3" and o[i]!="4" and o[i]!="5" and o[i]!="6" and o[i]!="7" and o[i]!="8" and o[i]!="9":
#                     x=1
#                 else:
#                     x=0
#                     break
#                 i+=1  
#             if(is_number(Id) and x==1):
#                 cam = cv2.VideoCapture(0)
#                 i=1
#                 repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
#                 file_path = "data/TrainingImage/"
#                 while is_file_present(repo_url,file_path+str(int(Id)) +"/"+str(int(Id))+"."+ str(i)+".jpg"):
#                 #while os.path.exists("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImage\\"+str(int(Id)) +"\\"+str(int(Id))+"."+ str(i)+".jpg"):
#                     i+=1
#                 if i>1:
#                     sampleNum=i-1
#                 else:
#                     sampleNum=i
#                 asd=i+50
#                 url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/faces.xml"
#                 facepath = cv2.CascadeClassifier(url)
#                 #detector=cv2.CascadeClassifier(harcascadePath)
#                 #eyepath= cv2.CascadeClassifier("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\automated attendence\\eyes.xml")
#                 while(True):
#                     ret, img = cam.read()
#                     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                     faces = facepath.detectMultiScale(gray, 1.3, 5)
#                     for (x,y,w,h) in faces:
#                         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
#                 #incrementing sample number 
#                         sampleNum=sampleNum+1
#                         roi_gray = gray[y:y+h, x:x+w]
#                         #eye=eyepath.detectMultiScale(roi_gray)
#                         #roi_color = img[y:y+h, x:x+w]
#                         if not is_file_present(repo_url,file_path+str(int(Id))):
#                             create_folder_if_not_exists(repo_url,file_path+str(int(Id))
#                                 #os.mkdir("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImage\\"+str(int(Id)))

#                 #saving the captured face in the dataset folder TrainingImage
#                         #folder_path = "data/TrainingImage/"
#                         image_path=str(int(Id))+"."+ str(sampleNum)+".jpg"
#                         upload_image_to_DB(repo_url, "data/TrainingImage/" + str(int(Id)), image_path, gray[y:y+h,x:x+w])
#                         #cv2.imwrite("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImage\\"+str(int(Id))+"\\"+str(int(Id)) +"."+ str(sampleNum)+".jpg" , gray[y:y+h,x:x+w])
#                 #display the frame
#                         cv2.imshow('frame',img)
#             #wait for 100 miliseconds 
#                     if cv2.waitKey(100) & 0xFF == ord('q'):
#                         break
#             # break if the sample number is morethan 80
#                     elif sampleNum>asd:
#                         break
#                 cam.release()
#                 cv2.destroyAllWindows() 
#                 res = "Images Saved for ID : " + Id +" Name : "+ name
            
#                 message.configure(text= res)
#             else:
#                 if(not name.isalpha()):
#                     res = "Enter Alphabetical Name"
#                     message.configure(text= res) 
#                 if(not is_number(Id)):
#                     res = "Enter Numeric Id"
#                     message.configure(text= res)
#         else:
#             if kr==0:
#                 res="Please Register Your ID"
#                 message.configure(text=res)
#             if kr==1 and flag==0:
#                 res="Invalid Password for Your ID"
#                 message.configure(text=res)
#     else:
#         if Id=="" and name=="" and passw=="":
#             res="Please Enter Your ID,Name and Password"
#             message.configure(text=res)
#         elif Id=="" and name=="" and passw!="":
#             res="Please Enter Your ID and Name"
#             message.configure(text=res)
#         elif Id=="" and name!="" and passw=="":
#             res="Please Enter Your ID and Password"
#             message.configure(text=res)
#         elif Id=="" and name!="" and passw!="":
#             res="Please Enter Your ID"
#             message.configure(text=res)    
#         elif Id!="" and name=="" and passw=="":
#             res="Please Enter Your Name and Password"
#             message.configure(text=res)
#         elif Id!="" and name=="" and passw!="":
#             res="Please Enter Your Name"
#             message.configure(text=res)
#         elif Id!="" and name!="" and passw=="":
#             res="Please Enter Your Password"
#             message.configure(text=res)    

def TakeImages():
    global message, txt, txt2, txt3, roo
    Id = txt.get()
    name = txt2.get()
    passw = txt3.get()
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        roo.destroy()
        
    url = "https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
    df = pd.read_csv(url)
    
    if Id != "" and name != "" and passw != "":
        i = 0
        flag = 0
        kr = 0
        
        while i < df["Id"].size:
            if not pd.isnull(df["Id"][i]):
                if str(int(df["Id"][i])) == str(Id):
                    kr = 1
                    break
            i += 1
        
        i = 0    
        while i < df["Id"].size:
            if not pd.isnull(df["Id"][i]):
                if not pd.isnull(df["Password"][i]):
                    if str(int(df["Id"][i])) == str(Id) and str(df["Password"][i]) == str(passw):
                        flag = 1
                        break
                else:
                    if str(int(df["Id"][i])) == str(Id) and str(int(df["Password"][i])) == str(passw):
                        flag = 1
                        break        
            i += 1
        
        if flag == 1 and kr == 1: 
            x = 1
            i = 0
            o = name
            
            while i < len(o):
                if o[i] not in "0123456789":
                    x = 1
                else:
                    x = 0
                    break
                i += 1  
                
            if is_number(Id) and x == 1:
                cam = cv2.VideoCapture(0)
                i = 1
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                file_path = "data/TrainingImage/"
                
                while is_file_present(repo_url, file_path + str(int(Id)) + "/" + str(int(Id)) + "." + str(i) + ".jpg"):
                    i += 1
                    
                if i > 1:
                    sampleNum = i - 1
                else:
                    sampleNum = i
                    
                asd = i + 50
                url = "https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/faces.xml"
                response = requests.get(url)
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(response.content)
                    temp_file_path = temp_file.name
                facepath =cv2.CascadeClassifier(temp_file_path)
                os.unlink(temp_file_path)
                #facepath = cv2.CascadeClassifier(url)
                
                while True:
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = facepath.detectMultiScale(gray, 1.3, 5)
                    
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)        
                        sampleNum = sampleNum + 1
                        roi_gray = gray[y:y+h, x:x+w]
                        
                        if not is_file_present(repo_url, file_path + str(int(Id))):
                            create_folder_if_not_exists(repo_url, file_path + str(int(Id)))
                        
                        image_path = str(int(Id)) + "." + str(sampleNum) + ".jpg"
                        upload_image_to_DB(repo_url, "data/TrainingImage/" + str(int(Id)), image_path, gray[y:y+h,x:x+w])
                        
                    cv2.imshow('frame', img)
                    
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    
                    if sampleNum > asd:
                        break
                        
                cam.release()
                cv2.destroyAllWindows() 
                res = "Images Saved for ID: " + Id + " Name: " + name
                message.configure(text=res)
            else:
                if not name.isalpha():
                    res = "Enter Alphabetical Name"
                    message.configure(text=res) 
                    
                if not is_number(Id):
                    res = "Enter Numeric Id"
                    message.configure(text=res)
        else:
            if kr == 0:
                res = "Please Register Your ID"
                message.configure(text=res)
                
            if kr == 1 and flag == 0:
                res = "Invalid Password for Your ID"
                message.configure(text=res)
    else:
        if Id == "" and name == "" and passw == "":
            res = "Please Enter Your ID, Name and Password"
            message.configure(text=res)
            
        elif Id == "" and name == "" and passw != "":
            res = "Please Enter Your ID and Name"
            message.configure(text=res)
            
        elif Id == "" and name != "" and passw == "":
            res = "Please Enter Your ID and Password"
            message.configure(text=res)
            
        elif Id == "" and name != "" and passw != "":
            res = "Please Enter Your ID"
            message.configure(text=res)    
            
        elif Id != "" and name == "" and passw == "":
            res = "Please Enter Your Name and Password"
            message.configure(text=res)
            
        elif Id != "" and name == "" and passw != "":
            res = "Please Enter Your Name"
            message.configure(text=res)
            
        elif Id != "" and name != "" and passw == "":
            res = "Please Enter Your Password"
            message.configure(text=res)


def save_recog_to_DB(repo_url, file_path, recog_model, branch='main'):
    local_recog_path = "temp_image.yml"
    recog_model.save(local_recog_path)

    # Read the .yml file content
    with open(local_recog_path, 'rb') as f:
        file_content = f.read()

    # Convert file content to base64-encoded string
    #encoded_content = file_content.decode('latin1')
    encoded_content = base64.b64encode(file_content).decode('utf-8')
    # Create URL for API endpoint
    api_url = f"{repo_url.rstrip('/')}/contents/{file_path.lstrip('/')}"

    # Make GET request to fetch existing file details
    response = requests.get(api_url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    if response.status_code == 200:
        existing_file = response.json()
        sha = existing_file['sha']
    elif response.status_code == 404:
        # File does not exist, SHA is not needed
        sha = None
    else:
        print(f"Failed to fetch file details. Status code: {response.status_code}")
        print(response.json())
        return

    # Create payload for creating/updating the file
    payload = {
        "message": f"Upload {file_path}",
        "content": encoded_content,
        "branch": branch,
        "sha": sha  # Include the SHA hash
    }

    # Make PUT request to create/update file
    response = requests.put(api_url, json=payload, headers={"Authorization": f"token {GITHUB_TOKEN}"})

    if response.status_code == 200 or response.status_code == 201:
        print(f"{file_path} uploaded successfully.")
    else:
        print(f"Failed to upload {file_path}. Status code: {response.status_code}")
        print(response.json())

    # Remove the temporary image file
    os.remove(local_recog_path)

    
def TrainImages():
    global message,txt,txt2,roo,txt3
    ad=txt.get()
    af=txt2.get()
    recog=list()
    aw=txt3.get()
      
    
    if ad!="" and af!="" and aw!="":
        i=0
        kr=0
        url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
        df=pd.read_csv(url)                                                 
        #df=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv")
        
        while i<df["Id"].size:
            if not math.isnan(df["Id"][i]):
                if str(int(df["Id"][i]))==str(ad):
                    kr=1
                    break
            i+=1
        j=0
        flag=0
        
        while j<df["Id"].size:
            if not math.isnan(df["Id"][j]):
                if not is_number(df["Password"][j]):
                    if str(int(df["Id"][j]))==str(ad) and str(df["Password"][j])==str(aw):
                        flag=1
                        break
                else:
                    if str(int(df["Id"][j]))==str(ad) and str(int(df["Password"][j]))==str(aw):
                        flag=1
                        break
                    
            j+=1
        op=0
        og=0
        while op<df["Id"].size:
            recog.append(cv2.face.LBPHFaceRecognizer_create())
            if not math.isnan(df["Id"][op]):
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                file_path="data/TrainingImageLabel/"                                            
                if not is_file_present(repo_url,file_path+"Trainner"+"."+str(int(df["Id"][op]))+".yml"):                                            
                #if not os.path.exists("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImageLabel\\Trainner"+"."+str(int(df["Id"][op]))+".yml"):
                    av=int(df["Id"][op])
                    og=op
                    break
                else:
                    if is_file_present(repo_url,file_path+"Trainner"+"."+str(int(ad))+".yml"):                                        
                    #if os.path.exists("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImageLabel\\Trainner"+"."+str(int(ad))+".yml"):
                        av=int(ad)
                        og=op
                        break
                       
            op+=1       
                
        
        if kr==1 and flag==1:  
            url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/faces.xml"
            harcascadePath = url
            response = requests.get(url)
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(response.content)
                    temp_file_path = temp_file.name
            detector =cv2.CascadeClassifier(temp_file_path)
            os.unlink(temp_file_path)
#             xml_content = np.frombuffer(response.content, np.uint8)
#             detector =cv2.CascadeClassifier(xml_content)
            #eyepath= cv2.CascadeClassifier("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\automated attendence\\eyes.xml")
            repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
            folder_path = "data/TrainingImage/"+str(int(ad))
            faces,Id = get_images_and_labels(repo_url, folder_path)                                                
            #faces,Id = getImagesAndLabels("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImage\\"+str(int(ad)))
            recog[og].update(faces, np.array(Id))
            file_path="data/TrainingImageLabel/Trainner."+str(Id[0]) +".yml"
            #m="C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImageLabel\\Trainner"+"."+str(av)+".yml"
            save_recog_to_DB(repo_url, file_path, recog[og])
            #recog[og].save(m)
            res = "Image Trained"
            message.configure(text= res)
        else:
            if kr==0 and flag==1:
                res="Please Register Your ID"
                message.configure(text=res)
            if kr==1 and flag==0:
                res="Invalid Password for Your ID"
                message.configure(text=res)
    else:
        if ad=="" and af=="" and aw=="":
            res="Please Enter Your ID,Name and Password"
            message.configure(text=res)
        elif ad=="" and af!="" and aw=="":
            res="Please Enter Your ID and Password"
            message.configure(text=res)
        elif ad=="" and af=="" and aw!="":
            res="Please Enter Your ID and Name"
            message.configure(text=res)
        elif ad=="" and af!="" and aw!="":
            res="Please Enter Your ID"
            message.configure(text=res)    
        elif ad!="" and af=="" and aw=="":
            res="Please Enter Your Name and Password"
            message.configure(text=res) 
        elif ad!="" and af=="" and aw!="":
            res="PLease Enter Your Name"
            message.configure(text=res)
        elif ad!="" and af!="" and aw=="":
            res="Please Enter Your Password"
            message.configure(text=res)    
    if cv2.waitKey(100) and 0xFF==ord('q'):
            roo.destroy() 
                                                            
def get_images_and_labels(repo_url, folder_path):
    # Create URL for fetching contents of the folder
    api_url = f"{repo_url.rstrip('/')}/contents/{folder_path.lstrip('/')}"
    
    i_d=folder_path.split('/')
    label=int(i_d[-1])
    
    # Make GET request to fetch contents of the folder
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the list of files in the folder
        files = response.json()
        
        # Initialize lists to store faces and IDs
        faces = []
        Ids = []
        
        # Loop through each file in the folder
        for file in files:
            # Check if the file is an image (you may need to modify this condition based on your file naming convention)
            if file['type'] == 'file' and file['name'].endswith(('.jpg', '.jpeg', '.png')):
                # Get the download URL of the image
                download_url = file['download_url']
                print(download_url)
                print(file['name'])
                print(os.path.splitext(file['name'])[0])
                
                # Read the image from the download URL
                image = Image.open(requests.get(download_url, stream=True).raw).convert('L')
                
                # Convert PIL image to numpy array
                image_np = np.array(image, dtype=np.uint8)
                
                # Extract the label from the file name (assuming the file name contains the label)
                #label = int(os.path.splitext(file['name'])[0])
                
                # Append the image and label to the lists
                faces.append(image_np)
                Ids.append(label)
        
        return faces, Ids
    else:
        print(f"Failed to fetch contents of folder. Status code: {response.status_code}")
                                                            
# def getImagesAndLabels(path):
#     #get the path of all the files in the folder
#     imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
#     global message,txt,txt2
#     ad=txt.get()
#     af=txt2.get()
#     #create empth face list
#     faces=[]
#     #create empty ID list
#     Ids=[]
#     #now looping through all the image paths and loading the Ids and the images
#     for imagePath in imagePaths:
#         #loading the image and converting it to gray scale
#         pilImage=Image.open(imagePath).convert('L')
#         #Now we are converting the PIL image into numpy array
#         Id=int(ad)
#         # extract the face from the training image sample
#         imageNp=np.array(pilImage, 'uint8')
#         faces.append(imageNp)
#         Ids.append(Id)
#     return faces,Ids
def get_number_of_files(repo_url, folder_path, branch='main'):
    # Create URL for API endpoint to get contents of the folder
    api_url = f"{repo_url.rstrip('/')}/contents/{folder_path.lstrip('/')}?ref={branch}"

    # Make GET request to fetch folder contents
    response = requests.get(api_url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        folder_contents = response.json()

        # Count the number of files in the folder
        num_files = sum(1 for item in folder_contents if item['type'] == 'file')

        return num_files
    else:
        print(f"Failed to get folder contents. Status code: {response.status_code}")
        return None   

def TrackImages():
    recognizer=list()
    oj=0
    og=0
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
    da=pd.read_csv(url) 
    print(da["Id"][oj])
    #da=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv")
    while oj<da["Id"].size:
        if not math.isnan(da["Id"][oj]):
            recognizer.append(cv2.face.LBPHFaceRecognizer_create())
            repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
            file_path="data/TrainingImageLabel/" +"Trainner"+"."+str(int(da["Id"][oj]))+".yml"                                           
            if is_file_present(repo_url,file_path):                                                
            #if ("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\TrainingImageLabel\\Trainner"+"."+str(int(da["Id"][oj]))+".yml"):
                #recognizer.append(cv2.face.LBPHFaceRecognizer_create())
                # Fetch the raw content of the YAML file from GitHub
                rep_url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                raw_url = f"{rep_url.rstrip('/')}/main/{file_path.lstrip('/')}"
                response = requests.get(raw_url)
                content = response.content.decode('utf-8')#response.json()["content"]
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                    temp_file.write(content)
                    temp_file_path = temp_file.name
                print("og"+str(og))
                recognizer[og].read(temp_file_path)
                os.unlink(temp_file_path)
            og+=1
        oj+=1    
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/faces.xml"
    harcascadePath = url
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(response.content)
        temp_file_path = temp_file.name
    faceCascade =cv2.CascadeClassifier(temp_file_path)
    os.unlink(temp_file_path)
#     xml_content = np.frombuffer(response.content, np.uint8)
#     faceCascade =cv2.CascadeClassifier(xml_content) 
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/StudentDetails/StudentDetails.csv"
    df=pd.read_csv(url)
    #df=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\StudentDetails\\StudentDetails.csv")
    global message2
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)
    co=0
    ok=0
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        
        faces=faceCascade.detectMultiScale(gray,1.2,5)  
        
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            ma=1000
            ot=0
        
            while ot<og:
                co+=1
                Id, conf = recognizer[ot].predict(gray[y:y+h,x:x+w])
                #print(conf)
                #print(Id)
                if conf<ma:
                    ma=conf
                    xy=Id
                    aj=ot
                #print(recognizer[ot].predict(gray[y:y+h,x:x+w]))
                ot+=1
                   
            Id, conf=recognizer[aj].predict(gray[y:y+h,x:x+w])
            #print(Id)
            #print(conf)
            if(conf<50):
            
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                
                
                
                tt=str(Id)+"-"+aa
                
                
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
            
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
                folder_path="data/ImagesUnknown"
                noOfFile=get_number_of_files(repo_url, folder_path)
                image_path= "Image"+str(noOfFile) + ".jpg"                                           
                upload_image_to_DB(repo_url, folder_path, image_path, im[y:y+h,x:x+w])
                #noOfFile=len(os.listdir("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\ImagesUnknown"))+1
                #cv2.imwrite("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\ImagesUnknown\\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
        
        #cv2.namedWindow('Attendance', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('im', 600,500)
        cv2.imshow('Attendance',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    
    #print(ma)
    #print(xy)
    url="https://raw.githubusercontent.com/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-/main/data/FacultyDetails.csv"
    data=pd.read_csv(url)
    #data=pd.read_csv("C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\FacultyDetails\\FacultyDetails.csv")        
    global abc
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    repo_url = "https://api.github.com/repos/pavankumar0831/Automated-Attendance-based-on-Facial-Recognition-"
    file_path="data/Attendance"+"/"+str(data["Id"][abc])+"_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    #fileName="C:\\Users\\Pavan\\Desktop\\B Tech Final Year Project\\Face-Recognition-Based-Attendance-System-master\\Attendance\\"+str(data["Id"][abc])+"_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance = attendance.sort_values(by ='Id' )
    lines=attendance.values.tolist()
    upload_list_to_DB(repo_url, file_path, lines, headers=['Id','Name','Password','DOB'], token=GITHUB_TOKEN)
    #upload_to_DB(repo_url, file_path, attendance)
    #attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    print(attendance)
    res=attendance
    #message2.configure(text=res)
    rot = tk.Tk()
    rot.title("Attendence Verficaton")
    rot.geometry("300x300")
    scrollbar = tk.Scrollbar(rot, orient="vertical")
    lb = tk.Listbox(rot, yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)
    
    scrollbar.pack(side="right", fill="y")
    lb.pack(side="left",fill="both", expand=True)
    lb.insert("end","S.No    "+"ID    "+"NAME     "+" DATE")
    k=0
    while k<attendance["Id"].size: 
        lb.insert("end", str(k+1)+"       "+str(attendance["Id"][k])+"    "+str(attendance["Name"][k])+"    "+str(attendance["Date"][k]))
        k+=1
    rot.mainloop()
root.mainloop()       
