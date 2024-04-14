import tkinter as tk
from tkinter import messagebox

class IDEWindow:
    def __init__(self, master):
        self.master = master
        master.title("Proyecto #2 - LFP - Keitlyn Tunchez - 202201139")

        window_width = 800  # Ancho 
        window_height = 600  # Alto 
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        master.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

        # Barra de menú
        self.menubar = tk.Menu(master)
        master.config(menu=self.menubar)

        # Crear los menús
        self.file_menu = tk.Menu(self.menubar)
        self.edit_menu = tk.Menu(self.menubar)
        self.view_menu = tk.Menu(self.menubar)
        self.help_menu = tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menubar.add_cascade(label="Análisis", menu=self.edit_menu)
        self.menubar.add_cascade(label="Tokens", menu=self.view_menu)
        self.menubar.add_cascade(label="Errores", menu=self.help_menu)

        # Opciones del menú Archivo
        self.file_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_command(label="Guardar Como", command=self.guardar_como_archivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.salir)

        # Opción del menú Análisis
        self.edit_menu.add_command(label="Generar sentencias MongoDB", command=self.generar_mongodb)

        # Opción del menú Tokens
        self.view_menu.add_command(label="Ver Tokens", command=self.ver_tokens)

        # Crear el área de edición de código
        self.code_label = tk.Label(master, text="Archivo de entrada:")
        self.code_label.pack(anchor="w", padx=10, pady=5)

        self.code_area = tk.Text(master, font=("Consolas", 12), height=20, width=100)
        self.code_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def nuevo_archivo(self):
        
        print("Nuevo archivo")

    def abrir_archivo(self):
        
        print("Abrir archivo")

    def guardar_archivo(self):
        
        print("Guardar archivo")

    def guardar_como_archivo(self):
        
        print("Guardar como archivo")

    def salir(self):
        confirmar_salir = messagebox.askyesno("Salir", "¿Está seguro que desea salir del programa?")
        if confirmar_salir:
            print("Saliendo del programa")
            self.master.destroy()

    def generar_mongodb(self):
        
        print("Generar sentencias MongoDB")

    def ver_tokens(self):
        
        print("Ver Tokens")


root = tk.Tk()
ide_window = IDEWindow(root)
root.mainloop()
