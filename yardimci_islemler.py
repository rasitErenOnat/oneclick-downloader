import os
import yt_dlp

def klasor_olustur(yol):
    if not os.path.exists(yol):
        os.makedirs(yol)
    
def link_kontrol(link):
    if link == "" or not link.startswith("http"):
        return False
    else:
        return True
        
