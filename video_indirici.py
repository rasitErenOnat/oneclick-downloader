import yt_dlp
from yardimci_islemler import link_kontrol, klasor_olustur
import os


def indirme_yap(link, format):
    if not link_kontrol(link):
        print("Gecersiz link!")
        return False
    hedef_klasor = "Indirilenler"
    klasor_olustur(hedef_klasor)

    if format == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(hedef_klasor, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
    elif format == "mp4":
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(hedef_klasor, '%(title)s.%(ext)s'),
        }
    else:
        print("Gecersiz format.")
        return False
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("Indirme basarili!")
            return True
    except Exception as e:
        print("Indirme sirasinda hata olustu:", e)
        return False
    

    



    
    
