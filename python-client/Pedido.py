import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import requests
from datetime import date

# ===== CONFIG =====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

API_URL = "http://localhost:8080/api/pedidos"
detalles = []

# =============================
# FUNCIONES
# =============================
def mostrar_estado(msg, color="white"):
    label_estado.configure(text=msg, text_color=color)

def limpiar_campos_producto():
    entry_id_producto.delete(0, "end")
    entry_precio.delete(0, "end")
    entry_cantidad.delete(0, "end")
    entry_descuento.delete(0, "end")

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)

    for item in detalles:
        tabla.insert("", "end", values=(
            item["idProducto"],
            item["precioUnidad"],
            item["cantidad"],
            item["descuento"]
        ))

def agregar_producto():
    try:
        item = {
            "idProducto": int(entry_id_producto.get()),
            "precioUnidad": float(entry_precio.get()),
            "cantidad": int(entry_cantidad.get()),
            "descuento": float(entry_descuento.get())
        }

        if item["precioUnidad"] <= 0 or item["cantidad"] <= 0:
            mostrar_estado("Precio y cantidad deben ser > 0", "orange")
            return

        detalles.append(item)
        actualizar_tabla()
        limpiar_campos_producto()
        mostrar_estado("Producto agregado", "green")

    except:
        mostrar_estado("Datos inválidos", "red")

def eliminar_producto():
    try:
        selected = tabla.selection()[0]
        index = tabla.index(selected)

        detalles.pop(index)
        actualizar_tabla()
        mostrar_estado("Producto eliminado", "green")
    except:
        mostrar_estado("Selecciona un producto", "orange")

def limpiar_lista():
    detalles.clear()
    actualizar_tabla()
    mostrar_estado("Lista limpiada", "green")

def registrar_pedido():
    try:
        if not entry_cliente.get():
            mostrar_estado("ID Cliente requerido", "orange")
            return

        if len(detalles) == 0:
            mostrar_estado("Agrega productos", "orange")
            return

        data = {
            "idCliente": entry_cliente.get(),
            "idEmpleado": int(entry_empleado.get()),
            "fechaPedido": str(date.today()),
            "fechaEntrega": str(date.today()),
            "fechaEnvio": str(date.today()),
            "formaEnvio": int(entry_envio.get()),
            "cargo": float(entry_cargo.get()),
            "destinatario": entry_destinatario.get(),
            "direccionDestinatario": entry_direccion.get(),
            "ciudadDestinatario": entry_ciudad.get(),
            "regionDestinatario": entry_region.get(),
            "codPostalDestinatario": entry_postal.get(),
            "paisDestinatario": entry_pais.get(),
            "detalles": detalles
        }

        response = requests.post(API_URL, json=data)

        if response.status_code in (200, 201):
            mostrar_estado("Pedido registrado correctamente", "green")
            detalles.clear()
            actualizar_tabla()
        else:
            mostrar_estado(response.text, "red")

    except requests.exceptions.ConnectionError:
        mostrar_estado("No conexión con backend", "red")
    except Exception as e:
        mostrar_estado(str(e), "red")

# =============================
# UI
# =============================
app = ctk.CTk()
app.title("Sistema de Pedidos")
app.geometry("1100x650")

app.grid_columnconfigure((0,1), weight=1)
app.grid_rowconfigure(0, weight=1)

# ===== PANEL IZQUIERDO =====
frame_left = ctk.CTkFrame(app)
frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

ctk.CTkLabel(frame_left, text="🧾 Datos del Pedido", font=("Arial", 20, "bold")).pack(pady=10)

entry_cliente = ctk.CTkEntry(frame_left, placeholder_text="ID Cliente")
entry_cliente.pack(pady=5, fill="x")

entry_empleado = ctk.CTkEntry(frame_left, placeholder_text="ID Empleado")
entry_empleado.pack(pady=5, fill="x")

entry_envio = ctk.CTkEntry(frame_left, placeholder_text="Forma Envío")
entry_envio.pack(pady=5, fill="x")

entry_cargo = ctk.CTkEntry(frame_left, placeholder_text="Cargo")
entry_cargo.pack(pady=5, fill="x")

entry_destinatario = ctk.CTkEntry(frame_left, placeholder_text="Destinatario")
entry_destinatario.pack(pady=5, fill="x")

entry_direccion = ctk.CTkEntry(frame_left, placeholder_text="Dirección")
entry_direccion.pack(pady=5, fill="x")

entry_ciudad = ctk.CTkEntry(frame_left, placeholder_text="Ciudad")
entry_ciudad.pack(pady=5, fill="x")

entry_region = ctk.CTkEntry(frame_left, placeholder_text="Región")
entry_region.pack(pady=5, fill="x")

entry_postal = ctk.CTkEntry(frame_left, placeholder_text="Código Postal")
entry_postal.pack(pady=5, fill="x")

entry_pais = ctk.CTkEntry(frame_left, placeholder_text="País")
entry_pais.pack(pady=5, fill="x")

ctk.CTkButton(frame_left, text="📤 Registrar Pedido", height=40, command=registrar_pedido).pack(pady=15, fill="x")

# ===== PANEL DERECHO =====
frame_right = ctk.CTkFrame(app)
frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

ctk.CTkLabel(frame_right, text="🛒 Detalle del Pedido", font=("Arial", 20, "bold")).pack(pady=10)

entry_id_producto = ctk.CTkEntry(frame_right, placeholder_text="ID Producto")
entry_id_producto.pack(pady=5, fill="x")

entry_precio = ctk.CTkEntry(frame_right, placeholder_text="Precio")
entry_precio.pack(pady=5, fill="x")

entry_cantidad = ctk.CTkEntry(frame_right, placeholder_text="Cantidad")
entry_cantidad.pack(pady=5, fill="x")

entry_descuento = ctk.CTkEntry(frame_right, placeholder_text="Descuento")
entry_descuento.pack(pady=5, fill="x")

btn_frame = ctk.CTkFrame(frame_right)
btn_frame.pack(pady=5, fill="x")

ctk.CTkButton(btn_frame, text="➕ Agregar", command=agregar_producto).pack(side="left", expand=True, fill="x", padx=5)
ctk.CTkButton(btn_frame, text="❌ Eliminar", command=eliminar_producto).pack(side="left", expand=True, fill="x", padx=5)
ctk.CTkButton(btn_frame, text="🗑 Limpiar", command=limpiar_lista).pack(side="left", expand=True, fill="x", padx=5)

# ===== TABLA PROFESIONAL =====
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
    background="#2b2b2b",
    foreground="white",
    rowheight=28,
    fieldbackground="#2b2b2b"
)

style.map("Treeview", background=[("selected", "#4CAF50")])

tabla = ttk.Treeview(frame_right, columns=("ID","Precio","Cantidad","Descuento"), show="headings")

tabla.heading("ID", text="ID Producto")
tabla.heading("Precio", text="Precio")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Descuento", text="Descuento")

tabla.column("ID", anchor="center", width=100)
tabla.column("Precio", anchor="center", width=100)
tabla.column("Cantidad", anchor="center", width=100)
tabla.column("Descuento", anchor="center", width=100)

tabla.pack(pady=10, fill="both", expand=True)

# ===== ESTADO =====
label_estado = ctk.CTkLabel(app, text="", font=("Arial", 14))
label_estado.grid(row=1, column=0, columnspan=2, pady=10)

app.mainloop()