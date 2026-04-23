import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import requests
import json

# ===== CONFIG =====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

API_URL = "http://localhost:8080/api/productos"

# =============================
# FUNCIONES
# =============================
def mostrar_estado(msg, color="white"):
    label_estado.configure(text=msg, text_color=color)

def limpiar_campos():
    for entry in [entry_nombre, entry_proveedor, entry_categoria,
                  entry_cantidad_unidad, entry_precio,
                  entry_existencia, entry_pedido, entry_nivel]:
        entry.delete(0, "end")

def crear_producto():
    try:
        if not entry_nombre.get():
            mostrar_estado("Nombre obligatorio", "orange")
            return

        data = {
            "nombreProducto": entry_nombre.get(),
            "idProveedor": int(entry_proveedor.get() or 0),
            "idCategoria": int(entry_categoria.get() or 0),
            "cantidadPorUnidad": entry_cantidad_unidad.get(),
            "precioUnidad": float(entry_precio.get() or 0),
            "unidadesEnExistencia": int(entry_existencia.get() or 0),
            "unidadesEnPedido": int(entry_pedido.get() or 0),
            "nivelNuevoPedido": int(entry_nivel.get() or 0),
            "suspendido": "VERDADERO" if combo_suspendido.get() == "SI" else "FALSO"
        }

        response = requests.post(API_URL, json=data)

        if response.status_code in (200, 201):
            mostrar_estado("Producto creado correctamente", "green")
            limpiar_campos()
            listar_productos()
        else:
            mostrar_estado(response.text, "red")

    except ValueError:
        mostrar_estado("Error: revisa campos numéricos", "red")
    except Exception as e:
        mostrar_estado(str(e), "red")

def listar_productos():
    try:
        response = requests.get(API_URL)

        for row in tabla.get_children():
            tabla.delete(row)

        if response.status_code == 200:
            productos = response.json()

            for p in productos:
                tabla.insert("", "end", values=(
                    p.get("idProducto"),
                    p.get("nombreProducto"),
                    p.get("precioUnidad"),
                    p.get("unidadesEnExistencia"),
                    "SI" if p.get("suspendido") == "VERDADERO" else "NO"
                ))

            mostrar_estado("Lista actualizada", "green")
        else:
            mostrar_estado("Error al obtener productos", "red")

    except:
        mostrar_estado("Error de conexión", "red")

def buscar_producto():
    try:
        idp = int(entry_buscar.get())
        response = requests.get(f"{API_URL}/{idp}")

        if response.status_code == 200:
            producto = response.json()

            texto_json = json.dumps(producto, indent=4, ensure_ascii=False)

            textbox_resultado.delete("1.0", "end")
            textbox_resultado.insert("end", texto_json)

            mostrar_estado("Producto encontrado", "green")

        elif response.status_code == 404:
            mostrar_estado("Producto no encontrado", "orange")

        else:
            mostrar_estado("Error en búsqueda", "red")

    except:
        mostrar_estado("ID inválido", "red")

# =============================
# UI
# =============================
app = ctk.CTk()
app.title("Gestión de Productos")
app.geometry("1100x700")

app.grid_columnconfigure((0,1), weight=1)
app.grid_rowconfigure(0, weight=1)

# ===== PANEL IZQUIERDO =====
frame_left = ctk.CTkFrame(app)
frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

ctk.CTkLabel(frame_left, text="➕ Crear Producto", font=("Arial", 20, "bold")).pack(pady=10)

entry_nombre = ctk.CTkEntry(frame_left, placeholder_text="Nombre")
entry_nombre.pack(pady=5, fill="x")

entry_proveedor = ctk.CTkEntry(frame_left, placeholder_text="ID Proveedor")
entry_proveedor.pack(pady=5, fill="x")

entry_categoria = ctk.CTkEntry(frame_left, placeholder_text="ID Categoría")
entry_categoria.pack(pady=5, fill="x")

entry_cantidad_unidad = ctk.CTkEntry(frame_left, placeholder_text="Cantidad por unidad")
entry_cantidad_unidad.pack(pady=5, fill="x")

entry_precio = ctk.CTkEntry(frame_left, placeholder_text="Precio")
entry_precio.pack(pady=5, fill="x")

entry_existencia = ctk.CTkEntry(frame_left, placeholder_text="Unidades en existencia")
entry_existencia.pack(pady=5, fill="x")

entry_pedido = ctk.CTkEntry(frame_left, placeholder_text="Unidades en pedido")
entry_pedido.pack(pady=5, fill="x")

entry_nivel = ctk.CTkEntry(frame_left, placeholder_text="Nivel nuevo pedido")
entry_nivel.pack(pady=5, fill="x")

combo_suspendido = ctk.CTkComboBox(frame_left, values=["NO", "SI"])
combo_suspendido.set("NO")
combo_suspendido.pack(pady=5, fill="x")

ctk.CTkButton(frame_left, text="Crear Producto", command=crear_producto).pack(pady=10, fill="x")

# ===== PANEL DERECHO =====
frame_right = ctk.CTkFrame(app)
frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

ctk.CTkLabel(frame_right, text="📋 Lista de Productos", font=("Arial", 20, "bold")).pack(pady=10)

# ===== TABLA =====
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
    background="#2b2b2b",
    foreground="white",
    rowheight=28,
    fieldbackground="#2b2b2b"
)

style.map("Treeview", background=[("selected", "#4CAF50")])

tabla = ttk.Treeview(frame_right, columns=("ID","Nombre","Precio","Stock","Estado"), show="headings")

tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Precio", text="Precio")
tabla.heading("Stock", text="Stock")
tabla.heading("Estado", text="Suspendido")

tabla.column("ID", width=50, anchor="center")
tabla.column("Nombre", width=180)
tabla.column("Precio", width=80, anchor="center")
tabla.column("Stock", width=80, anchor="center")
tabla.column("Estado", width=100, anchor="center")

tabla.pack(pady=10, fill="both", expand=True)

# ===== BOTONES =====
btn_frame = ctk.CTkFrame(frame_right)
btn_frame.pack(fill="x")

ctk.CTkButton(btn_frame, text="🔄 Actualizar", command=listar_productos)\
    .pack(side="left", expand=True, fill="x", padx=5)

# ===== BUSCAR =====
entry_buscar = ctk.CTkEntry(frame_right, placeholder_text="Buscar por ID")
entry_buscar.pack(pady=5, fill="x")

ctk.CTkButton(frame_right, text="🔍 Buscar", command=buscar_producto)\
    .pack(fill="x")

# ===== JSON RESULTADO =====
ctk.CTkLabel(frame_right, text="📦 Resultado JSON").pack(pady=5)

textbox_resultado = ctk.CTkTextbox(frame_right, height=150)
textbox_resultado.pack(pady=5, fill="both", expand=True)

# ===== ESTADO =====
label_estado = ctk.CTkLabel(app, text="", font=("Consolas", 13))
label_estado.grid(row=1, column=0, columnspan=2, pady=10)

app.mainloop()