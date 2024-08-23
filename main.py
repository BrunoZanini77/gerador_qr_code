from tkinter import *
import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox


# def create_image_window(image_path):
#     # Cria uma nova janela Tkinter
#     window_img = tk.Tk()

#     canvas = Canvas(window_img, width = 600, height = 600)
#     canvas.pack()
#     img = PhotoImage(file=image_path)
#     canvas.create_image(40,40, anchor=NW, image=img)

#     # Inicia o loop de eventos Tkinter
#     window_img.mainloop()

def create_image_window(image_path):
    # Cria uma nova janela Tkinter
    window = tk.Tk()

    # Abre o arquivo de imagem
    img = Image.open(image_path)

    # Converte a imagem para uma imagem de foto compatível com Tkinter
    tk_img = ImageTk.PhotoImage(img)

    # Cria um rótulo e adiciona a imagem a ele
    label = tk.Label(window, image=tk_img)
    label.pack()

    # Inicia o loop de eventos Tkinter
    window.mainloop()



def gera_qr_code():
    url = website_entry.get()
    if len(url) == 0:
        messagebox.showinfo(title="Erro!",message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
        title=url,
        message=f"O endereço URL é: \n "
                f"Endereço: {url} \n "
                f"Pronto para salvar?")

    if opcao_escolhida:
      qr = qrcode.QRCode(version=1, box_size=10, border=5)
      qr.add_data(url)
      qr.make(fit=True)
      img = qr.make_image(fill_color='black', back_color='white')
      img.save('qrExport.png')
      window.destroy()
      create_image_window('qrExport.png')

window = Tk()
window.title("Gerador de Código QR")
window.config(padx=10, pady=100)

# Labels
website_label = Label(text="URL:")
website_label.grid(row=2, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()
add_button = Button(text="Gerar QR Code", width=36, command=gera_qr_code)
add_button.grid(row=4, column=1, columnspan=2)

# Return Window


window.mainloop()