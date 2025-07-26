import customtkinter as ctk
from video_indirici import indirme_yap

def mp3_indir():
    link = link_entry.get()
    indirme_yap(link, "mp3")

def mp4_indir():
    link = link_entry.get()
    indirme_yap(link, "mp4")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("OneClick - Video/Ses İndirici")
app.geometry("800x600")

baslik = ctk.CTkLabel(master=app, text="OneClick - Video/Ses İndirici", font=("Arial", 23, "bold"))
baslik.pack(pady=30)

link_entry = ctk.CTkEntry(master=app, width=500, placeholder_text="Linki buraya yapıştırın")
link_entry.pack(pady=50)

mp3_buton = ctk.CTkButton(master=app, text="MP3 indir", command=mp3_indir)
mp3_buton.pack(pady=20)

mp4_buton = ctk.CTkButton(master=app, text="MP4 indir", command=mp4_indir)
mp4_buton.pack(pady=20)

app.mainloop()


