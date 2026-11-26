import os
import shutil
folder = r"C:\Users\hp\OneDrive\Desktop\test_folder"
def func(b,i):
    path = os.path.join(folder,b)
    os.makedirs(path,exist_ok=True)
    src = os.path.join(folder,i)
    shutil.move(src,path)
for i in os.listdir(folder):
    ext = os.path.splitext(i)
    a = ext[-1]
    match a:
        case ".jpg" | ".png":
             b = "Images"
             func(b,i)
        case ".mp3":
            b = "Music"
            func(b,i)
        case ".docx" | ".txt":
            b = "Documents"
            func(b,i)
        case ".pdf":
            b = "pdfs"
            func(b,i)















