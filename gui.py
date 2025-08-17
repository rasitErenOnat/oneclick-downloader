import customtkinter as ctk
from video_sarki_indirici import indirme_yap
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("OneClick - Video/Ses İndirici")
app.geometry("800x600")

baslik = ctk.CTkLabel(master=app, text="OneClick - Video/Ses İndirici", font=("Arial", 23, "bold"))
baslik.pack(pady=40)

link_entry = ctk.CTkEntry(master=app, width=500, placeholder_text="Linki buraya yapıştırın")
link_entry.pack(pady=50)

durum_label = ctk.CTkLabel(master=app, text="", font=("Arial", 16))
durum_label.pack(pady=10)

def mp3_indir():
    def thread_icerigi():
        link = link_entry.get().strip()
        app.after(0, lambda: durum_label.configure(text="İndirme başladı..."))
        sonuc = indirme_yap(link, "mp3")
        app.after(0, lambda: durum_label.configure(
            text="İndirme başarılı!" if sonuc else "İndirme başarısız!"))
    threading.Thread(target=thread_icerigi, daemon=True).start()

def mp4_indir():
    def thread_icerigi():
        link = link_entry.get().strip()
        app.after(0, lambda: durum_label.configure(text="İndirme başladı..."))
        sonuc = indirme_yap(link, "mp4")
        app.after(0, lambda: durum_label.configure(
            text="İndirme tamamlandı!" if sonuc else "İndirme başarısız!"))
    threading.Thread(target=thread_icerigi, daemon=True).start()

mp3_buton = ctk.CTkButton(master=app, text="MP3 indir", command=mp3_indir)
mp3_buton.pack(pady=20)

mp4_buton = ctk.CTkButton(master=app, text="MP4 indir", command=mp4_indir)
mp4_buton.pack(pady=20)

app.mainloop()

