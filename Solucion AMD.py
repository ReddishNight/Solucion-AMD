import tkinter as tk
def create_dynamic_translucent_window():
    root = tk.Tk()
    root.overrideredirect(True)  # Sin bordes ni barra de título
    root.wm_attributes('-topmost', True)  # Siempre encima de otras ventanas
    root.wm_attributes('-transparentcolor', 'white')  # Color transparente, puedes cambiar 'white' por otro color
    root.geometry('1x1+0+0')  # Tamaño mínimo (1x1 píxeles) y posición (0,0)
    def update_transparency():
        try:
            color = root.winfo_rgb('#ffffff')  # Obtener color en formato RGB
            root.wm_attributes('-alpha', 0.5)  # Establecer nivel de transparencia (0.0 a 1.0)
            root.configure(bg='#ffffff')  # Establecer el fondo al color RGB obtenido
        except:
            pass
        root.after(1, update_transparency)  # Llamar recursivamente después de 1 ms
    update_transparency()
    root.mainloop()
create_dynamic_translucent_window()
#no me responsabilizo por mal funcioanmiento, o uso inadecuado del mismo.....
