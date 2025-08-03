import customtkinter as ctk

# Configuración del tema de CustomTkinter
ctk.set_default_color_theme("green")

# Variables utiles 
dispositivo_conectado = "No hay dispositivo conectado"
control_conectado = "Teclado"
modo_uso = "Automatico"
 

class frame_principal(ctk.CTkFrame):
    #pagina donde se muestra las opciones a donde ir a trabajar con el robot(controlar o configurar)
    def __init__(self, master, go_frame_control, go_frame_configuraciones, go_frame_ayuda):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Bienvenido al robot")
        self.label.pack(pady=20)

        # Botón para ir a la página de control
        self.boton_control = ctk.CTkButton(self, text="Controlar Robot", command=go_frame_control)
        self.boton_control.pack(pady=10)

        # Botón para ir a la página de configuraciones
        self.boton_configuraciones = ctk.CTkButton(self, text="Configuraciones", command=go_frame_configuraciones)
        self.boton_configuraciones.pack(pady=10)

        # Botón para ir a la pagina de ayuda 
        self.boton_ayuda = ctk.CTkButton(self, text="Ayuda", command=go_frame_ayuda)
        self.boton_ayuda.pack(pady=10)

# Página Control (uso arduino bluetooth)
class frame_Control(ctk.CTkFrame):
    def __init__(self, master, volver_frame_principal):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Control Bluetooth")
        self.label.pack(pady=20)

        # Después tengo que configurar para que el nombre sea una variable que dependa de cual sea
        ## el dispositivo esclavo bluetooth
        if bool(dispositivo_conectado) == True:
            self.label_nombre_robot = ctk.CTkLabel(self, text=f"Robot: {dispositivo_conectado}")
            self.label_nombre_robot.pack(pady=10)
        else:
            self.label_nombre_robot = ctk.CTkLabel(self, text="Robot: Desconocido")
            self.label_nombre_robot.pack(pady=10)

        #En un futuro agregar los distintos botones o entradas que interacturan con el Robot


        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_frame_principal)
        self.boton_volver.pack(pady=10)

class frame_Configuraciones(ctk.CTkFrame):
    def __init__(self, master, volver_principal, ir_dispositivo, ir_controles, ir_modo):
        
        super().__init__(master)
        # Habilitar la configuracion con grid
        self.grid_rowconfigure([0,1,2,3,4], weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Titulo del frame y boton de volver
        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_principal)
        self.boton_volver.grid(row=0, column=0, pady=10, padx=10, sticky="nw")
        self.label = ctk.CTkLabel(self, text="Configuraciones del Robot")
        self.label.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        #Agregar todas las opciones que desee configurar desde esta pagina (ej: conexion bluetooth,disposicion controles etc.)
        self.boton_dispositivo = ctk.CTkButton(self, text="Dispositivo", command=ir_dispositivo)
        self.boton_dispositivo.grid(row=2, column=0, pady=10, padx=10, sticky="wns")
        self.label_dispositivo = ctk.CTkLabel(self, text=dispositivo_conectado)
        self.label_dispositivo.grid(row=2, column=0, pady=10, padx=10, sticky="nse")

        self.boton_controles = ctk.CTkButton(self, text="Mando", command=ir_controles)
        self.boton_controles.grid(row=3, column=0, pady=10, padx=10, sticky="wns")
        self.label_controles = ctk.CTkLabel(self, text=control_conectado)
        self.label_controles.grid(row=3, column=0, pady=10, padx=10, sticky="nse")

        self.boton_modo = ctk.CTkButton(self, text="Modo", command=ir_modo)
        self.boton_modo.grid(row=4, column=0, pady=10, padx=10, sticky="wns")
        self.label_modo = ctk.CTkLabel(self, text=modo_uso)
        self.label_modo.grid(row=4, column=0, pady=10, padx=10, sticky="nse")

class frame_Dispositivo(ctk.CTkFrame):
    def __init__(self, master, volver_configuraciones):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Dispositivo")
        self.label.pack(pady=20)
        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_configuraciones)
        self.boton_volver.pack(pady=10)
        # Desarrollar las configuraciones respecto al dispositivo

class frame_Controles(ctk.CTkFrame):
    def __init__(self, master, volver_configuraciones):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Controles")
        self.label.pack(pady=20)
        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_configuraciones)
        self.boton_volver.pack(pady=10)
        # Desarrollar las configuraciones respecto a los controles

class frame_Modo(ctk.CTkFrame):
    def __init__(self, master, volver_configuraciones):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Modo de uso")
        self.label.pack(pady=20)
        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_configuraciones)
        self.boton_volver.pack(pady=10)
        # Desarrollar las configuraciones respecto al modo de uso
        

class frame_Ayuda(ctk.CTkFrame):
    def __init__(self, master, volver_frame_principal):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Ayuda")
        self.label.pack(pady=50)

        #Completar dependiendo de como se desarrollen los otros frames

        self.boton_volver = ctk.CTkButton(self, text="Volver", command=volver_frame_principal)
        self.boton_volver.pack(side="bottom", pady=50)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RobotIA XD")
        self.geometry("800x800")

        # Creamos los frames y pasamos los callbacks apropiados
        self.frame_principal = frame_principal(self, self.ir_frame_control, self.ir_frame_configuraciones, self.ir_frame_ayuda)
        self.frame_control = frame_Control(self, self.ir_frame_principal)
        self.frame_configuraciones = frame_Configuraciones(self, self.ir_frame_principal, self.ir_frame_dispositivo, self.ir_frame_controles, self.ir_frame_modo)
        self.frame_dispositivo = frame_Dispositivo(self, self.ir_frame_configuraciones)
        self.frame_controles = frame_Controles(self, self.ir_frame_configuraciones)
        self.frame_modo = frame_Modo(self, self.ir_frame_configuraciones)                                   
        self.frame_ayuda = frame_Ayuda(self, self.ir_frame_principal)

        # Mostrar frame principal
        self.frame_principal.pack(fill="both", expand=True)
        self.frame_control.pack_forget()
        self.frame_configuraciones.pack_forget()
        self.frame_ayuda.pack_forget()

    # Creamos las funciones para cambiar entre frames
    def ir_frame_principal(self):
        self.frame_principal.pack(fill="both", expand=True)
        self.frame_control.pack_forget()
        self.frame_configuraciones.pack_forget()
        self.frame_ayuda.pack_forget()

    def ir_frame_control(self):
        self.frame_principal.pack_forget()
        self.frame_control.pack(fill="both", expand=True)
        self.frame_configuraciones.pack_forget()
        self.frame_ayuda.pack_forget()

    def ir_frame_configuraciones(self):
        self.frame_principal.pack_forget()
        self.frame_control.pack_forget()
        self.frame_configuraciones.pack(fill="both", expand=True)
        self.frame_dispositivo.pack_forget()
        self.frame_controles.pack_forget()
        self.frame_modo.pack_forget()
        self.frame_ayuda.pack_forget()

    def ir_frame_dispositivo(self):
        self.frame_configuraciones.pack_forget()
        self.frame_dispositivo.pack(fill="both", expand=True)

    def ir_frame_controles(self):
        self.frame_configuraciones.pack_forget()
        self.frame_controles.pack(fill="both", expand=True)

    def ir_frame_modo(self):
        self.frame_configuraciones.pack_forget()
        self.frame_modo.pack(fill="both", expand=True)

    def ir_frame_ayuda(self):
        self.frame_principal.pack_forget()
        self.frame_control.pack_forget()
        self.frame_configuraciones.pack_forget()
        self.frame_ayuda.pack(fill="both", expand=True)

    #Generamos el loop para el programa
if __name__ == "__main__":
    app = App()
    app.mainloop()
