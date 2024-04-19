import tkinter as tk
from tkinter import messagebox
import qrcode






##-------Funciones del sistema----------



def generar():
    url = entry_generar_qr.get()
    nombre = entry_nombre.get()
    cadena = f"./Codigos_QR/{nombre}.png"
    
   

    # Creamo objeto qr
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )


    # Añadimos los datos que se reciben en la entrada
    qr.add_data(url) ##Le agregamos los datos
    qr.make(fit=True) ## Generamos los patrones, con la opcion de que se ajusten para adaptarse a los datos

    # Creamos imagen del qr
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    imagen_qr.save(cadena)


    
    ##Alertamos que se ha generado con exito
    messagebox.showinfo("Codigo qr generado con exito")
    
    entry_generar_qr.delete(0,tk.END)
    entry_nombre.delete(0,tk.END)
    

    


#-----GUI--------------
##Ventana
ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Generador QR")
ventana.config(bg='black')
##Entry para asociarle un nombre
entry_nombre = tk.Entry(ventana,)
entry_nombre.pack(pady=20)
entry_nombre.config(width=50)
entry_nombre.delete(0, "end")
entry_nombre.insert(0, "Ingrese el nombre que desea darle al codigo QR")
##Entry para Generar QR
entry_generar_qr = tk.Entry(ventana)
entry_generar_qr.pack(pady= 20)
entry_generar_qr.config(width=50)
entry_generar_qr.delete(0, "end")
entry_generar_qr.insert(0, "Ingrese el link o informacion que desea")
##Boton para Generar QR
generar_qr = tk.Button(ventana, text="Generar QR", command=generar)
generar_qr.pack(padx=20)




ventana.mainloop()

 
    




