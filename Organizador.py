import os
import shutil
import tkinter
from tkinter import filedialog


def escolher_pasta():
    pasta = filedialog.askdirectory()
    return pasta

def criar_pastas(folder):
    lista_pastas =["PDF","JSON","XLSX","IMG","Audio","Video","DOC","TXT"]
    for nm_pasta in lista_pastas:
        if not os.path.exists(os.path.join(folder,nm_pasta)):
            os.makedirs(os.path.join(folder,nm_pasta))
        else:
            print(f"A pasta {nm_pasta}, já existe!")


def main(folder):
    criar_pastas(folder)
    os.chdir(folder)
    lista_arquivos = os.listdir(folder)
    txt = os.path.join(folder,"TXT")
    pdf = os.path.join(folder,"PDF")
    json = os.path.join(folder,"JSON")
    xlsx = os.path.join(folder,"XLSX")
    img = os.path.join(folder,"IMG")
    audio = os.path.join(folder,"Audio")
    video = os.path.join(folder,"Video")
    doc = os.path.join(folder,"DOC")

    for arquivo in lista_arquivos:
        if os.path.isdir(os.path.join(folder,arquivo)):
            continue
        if arquivo.lower().endswith(".txt"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(txt, arquivo))
        elif arquivo.lower().endswith(".pdf") :
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(pdf,arquivo))
        elif arquivo.lower().endswith(".json"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(json,arquivo))
        elif arquivo.lower().endswith(".xlsx") or arquivo.lower().endswith(".csv"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(xlsx,arquivo))
        elif arquivo.lower().endswith(".doc") or arquivo.lower().endswith(".docx"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(doc,arquivo))
        elif arquivo.lower().endswith(".mp3") or arquivo.lower().endswith(".wav"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(audio,arquivo))
        elif arquivo.lower().endswith(".mp4") or arquivo.lower().endswith(".wav") or arquivo.lower().endswith(".mov"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(video,arquivo))
        elif arquivo.lower().endswith(".jpg") or arquivo.lower().endswith(".jpeg") or arquivo.lower().endswith(".jfif") or arquivo.lower().endswith(".png"):
            print(arquivo)
            shutil.move(os.path.join(folder, arquivo), os.path.join(img,arquivo))
pasta = escolher_pasta()
main(pasta)