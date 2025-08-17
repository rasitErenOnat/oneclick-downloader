# OneClick - Video/Ses İndirici

Bu proje, basit ve kullanıcı dostu bir **video/ses indirici**. 
`yt-dlp` kütüphanesi ve `ffmpeg` kullanarak **YouTube ve desteklenen diğer platformlardan** video(mp4)/müzik-ses(mp3) indirebilirsiniz.
Arayüz için ise **customtkinter** kullanılmıştır.

 **Yasal Uyarı**: Bu uygulama yalnızca **telif hakkı sahibinin izin verdiği içerikleri** indirmek için kullanılmalıdır. Kullanıcı, bulunduğu ülkenin yasalarına ve platformların kullanım koşullarına uymakla yükümlüdür.

 ---

##  Özellikler
-  MP3 indirme
-  MP4 indirme
-  Otomatik `Indirilenler/` klasörüne kaydetme
-  Karanlık tema arayüz
-  Tek tıkla kullanım

---

##  Gereksinimler

- Python 3.10 ve üzeri.
- [ffmpeg](https://ffmpeg.org/) (sisteme kurulu olmalı)
- `yt-dlp` 
- `customtkinter`

---

##  Kurulum
```bash
# Sanal ortam (önerilir)
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # macOS/Linux

# Gerekli kütüphaneler
pip install -r requirements.txt
```

`requirements.txt` içeriği:
```
yt-dlp
customtkinter
```

---

## Kullanım
```bash
python gui.py
```

- Linki kutuya yapıştır → MP3 veya MP4 indir butonuna tıkla  
- Dosyalar `Indirilenler/` klasörüne kaydedilir  

---

## Lisans
Bu proje [MIT LICENSE](LICENSE) ile lisanslanmıştır.  
İsteyen indirip kullanabilir, değiştirebilir ve paylaşabilir. Ancak herhangi bir garanti verilmez.