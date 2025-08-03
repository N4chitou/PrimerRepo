import customtkinter as ctk



class PaginaInicial(ctk.CTkFrame):
    def __init__(self, master, ir_a_pagina_2, ir_a_pagina_3):
        super().__init__(master)
        self.entry = ctk.CTkEntry(self, placeholder_text="Escribe algo")
        self.entry.pack(pady=20)
        # Botón para ir a la Página 2
        self.boton2 = ctk.CTkButton(self, text="Ir a Página 2", command=ir_a_pagina_2)
        self.boton2.pack(pady=10)
        # Botón para ir a la Página 3
        self.boton3 = ctk.CTkButton(self, text="Ir a Página 3", command=ir_a_pagina_3)
        self.boton3.pack(pady=10)
    
    def limpiar(self):
        self.entry.delete(0, "end")

class PaginaDos(ctk.CTkFrame):
    def __init__(self, master, volver_callback):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="¡Estás en la página 2!")
        self.label.grid(row=1, column=0, pady=40, padx=1, sticky="new")
        self.label = ctk.CTkLabel(self, text="Esta es la segunda página")
        self.label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_callback)
        self.boton_volver.grid(row=0, column=0, pady=10, padx=10, sticky="nw")
        # Configuración de la cuadrícula para que ocupe todo el espacio disponible
        self.grid_rowconfigure([0,1], weight=1)
        self.grid_columnconfigure(0, weight=1)

class PaginaTres(ctk.CTkFrame):
    def __init__(self, master, volver_callback):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="¡Estás en la página 3!")
        self.label.pack(pady=20)
        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_callback)
        self.boton_volver.pack(pady=10)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo multipágina")
        self.geometry("300x250")

        # Creamos las páginas y pasamos los callbacks apropiados
        self.pagina_inicial = PaginaInicial(self, self.ir_a_pagina_dos, self.ir_a_pagina_tres)
        self.pagina_dos = PaginaDos(self, self.ir_a_pagina_inicial)
        self.pagina_tres = PaginaTres(self, self.ir_a_pagina_inicial)
        
        # Mostramos la página inicial
        self.pagina_inicial.pack(fill="both", expand=True)
        self.pagina_dos.pack_forget()
        self.pagina_tres.pack_forget()
    
    def ir_a_pagina_dos(self):
        self.pagina_inicial.limpiar()
        self.pagina_inicial.pack_forget()
        self.pagina_tres.pack_forget()
        self.pagina_dos.pack(fill="both", expand=True)
    
    def ir_a_pagina_tres(self):
        self.pagina_inicial.limpiar()
        self.pagina_inicial.pack_forget()
        self.pagina_dos.pack_forget()
        self.pagina_tres.pack(fill="both", expand=True)
    
    def ir_a_pagina_inicial(self):
        self.pagina_dos.pack_forget()
        self.pagina_tres.pack_forget()
        self.pagina_inicial.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()