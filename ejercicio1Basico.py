import tkinter as tk
from tkinter import messagebox


class ListaCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not producto.strip():
            return "El producto está vacío"

        if producto not in self.productos:
            self.productos.append(producto)
            return f"{producto} agregado"
        return f"{producto} ya existe"

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            return f"{producto} eliminado"
        return f"{producto} no encontrado"

    def buscar_producto(self, producto):
        return producto in self.productos

    def contar_productos(self):
        return len(self.productos)

    def obtener_lista(self):
        return self.productos


class AppListaCompras:
    def __init__(self, root):
        self.lista = ListaCompras()

        root.title("🛒 Lista de Compras")
        root.geometry("400x450")
        root.configure(bg="#f5f5f5")

        # Título
        self.titulo = tk.Label(root, text="Lista de Compras", font=("Arial", 16, "bold"), bg="#f5f5f5")
        self.titulo.pack(pady=10)

        # Input
        self.entrada = tk.Entry(root, font=("Arial", 12))
        self.entrada.pack(pady=5)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar", bg="#4CAF50", fg="white", command=self.agregar)
        self.btn_agregar.pack(fill="x", padx=20, pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar", bg="#f44336", fg="white", command=self.eliminar)
        self.btn_eliminar.pack(fill="x", padx=20, pady=5)

        self.btn_buscar = tk.Button(root, text="Buscar", bg="#2196F3", fg="white", command=self.buscar)
        self.btn_buscar.pack(fill="x", padx=20, pady=5)

        self.btn_mostrar = tk.Button(root, text="Mostrar Lista", bg="#9C27B0", fg="white", command=self.mostrar)
        self.btn_mostrar.pack(fill="x", padx=20, pady=5)

        self.btn_contar = tk.Button(root, text="Contar Productos", bg="#FF9800", fg="white", command=self.contar)
        self.btn_contar.pack(fill="x", padx=20, pady=5)

        # Lista visual
        self.lista_box = tk.Listbox(root, font=("Arial", 12))
        self.lista_box.pack(fill="both", expand=True, padx=20, pady=10)

    def obtener_input(self):
        return self.entrada.get().strip()

    def limpiar_input(self):
        self.entrada.delete(0, tk.END)

    def actualizar_lista_visual(self):
        self.lista_box.delete(0, tk.END)
        for producto in self.lista.obtener_lista():
            self.lista_box.insert(tk.END, producto)

    def agregar(self):
        producto = self.obtener_input()
        mensaje = self.lista.agregar_producto(producto)
        messagebox.showinfo("Resultado", mensaje)
        self.actualizar_lista_visual()
        self.limpiar_input()

    def eliminar(self):
        producto = self.obtener_input()
        mensaje = self.lista.eliminar_producto(producto)
        messagebox.showinfo("Resultado", mensaje)
        self.actualizar_lista_visual()
        self.limpiar_input()

    def buscar(self):
        producto = self.obtener_input()
        encontrado = self.lista.buscar_producto(producto)
        mensaje = f"{producto} está en la lista" if encontrado else f"{producto} no está en la lista"
        messagebox.showinfo("Buscar", mensaje)

    def mostrar(self):
        self.actualizar_lista_visual()

    def contar(self):
        total = self.lista.contar_productos()
        messagebox.showinfo("Total", f"Productos: {total}")


# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = AppListaCompras(root)
    root.mainloop()