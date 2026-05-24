import customtkinter as ctk

# Configura el modo de apariencia del sistema (opcional: 'dark' o 'light')
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

# Crea la ventana principal
app = ctk.CTk()
app.geometry("400x240")
app.title("Mi primera app en CustomTkinter")

# Agrega un botón
boton = ctk.CTkButton(master=app, text="Haz clic aquí", command=lambda: print("Botón presionado"))
boton.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Inicia la aplicación
app.mainloop()