import os
import shutil
folder = r"C:\Users\hp\OneDrive\Desktop\test_folder"
for i in os.listdir(folder):
    ext = os.path.splitext(i)
    a = ext[-1]
    match a:
        case ".jpg" | ".png":
             path = os.path.join(folder,"Images")
             os.makedirs(path,exist_ok=True)
             src = os.path.join(folder,i)
             shutil.move(src,path)
        case ".mp3":
            path = os.path.join(folder,"Music")
            os.makedirs(path,exist_ok=True)
            src = os.path.join(folder,i)
            shutil.move(src,path)
        case ".docx" | ".txt":
            path = os.path.join(folder,"Documents")
            os.makedirs(path,exist_ok=True)
            src = os.path.join(folder,i)
            shutil.move(src,path)
        case ".pdf":
            path = os.path.join(folder,"pdfs")
            os.makedirs(path,exist_ok=True)
            src = os.path.join(folder,i)
            shutil.move(src,path)


















