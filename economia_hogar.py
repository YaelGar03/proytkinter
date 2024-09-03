import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

class EconomiaHogarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Economía del Hogar")

        # Diccionarios para almacenar ingresos y gastos
        self.ingresos = {}
        self.gastos = {}
        
        # Nombre de la persona
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)

        # Ingreso mensual
        self.label_sueldo_mensual = tk.Label(root, text="Sueldo Mensual:")
        self.label_sueldo_mensual.grid(row=1, column=0)
        self.entry_sueldo_mensual = tk.Entry(root)
        self.entry_sueldo_mensual.grid(row=1, column=1)

        # Botón para agregar ingreso mensual
        self.btn_add_sueldo = tk.Button(root, text="Agregar Sueldo Mensual", command=self.agregar_sueldo)
        self.btn_add_sueldo.grid(row=2, column=0, columnspan=2)

        # Ingreso extra
        self.label_fecha_extra = tk.Label(root, text="Fecha (dd/mm/aa):")
        self.label_fecha_extra.grid(row=3, column=0)
        self.entry_fecha_extra = tk.Entry(root)
        self.entry_fecha_extra.grid(row=3, column=1)

        self.label_tipo_ingreso_extra = tk.Label(root, text="Tipo de Ingreso Extra:")
        self.label_tipo_ingreso_extra.grid(row=4, column=0)
        self.entry_tipo_ingreso_extra = tk.Entry(root)
        self.entry_tipo_ingreso_extra.grid(row=4, column=1)

        self.label_ingreso_extra = tk.Label(root, text="Ingreso Extra:")
        self.label_ingreso_extra.grid(row=5, column=0)
        self.entry_ingreso_extra = tk.Entry(root)
        self.entry_ingreso_extra.grid(row=5, column=1)

        # Botón para agregar ingreso extra
        self.btn_add_ingreso_extra = tk.Button(root, text="Agregar Ingreso Extra", command=self.agregar_ingreso_extra)
        self.btn_add_ingreso_extra.grid(row=6, column=0, columnspan=2)

        # Lista de ingresos
        self.label_lista_ingresos = tk.Label(root, text="Lista de Ingresos:")
        self.label_lista_ingresos.grid(row=7, column=0)
        self.listbox_ingresos = tk.Listbox(root, selectbackground=root.cget("background"))
        self.listbox_ingresos.grid(row=7, column=1)

        # Total ingreso del hogar
        self.label_total_ingreso = tk.Label(root, text="Total Ingreso del Hogar:")
        self.label_total_ingreso.grid(row=8, column=0)
        self.label_total_ingreso_valor = tk.Label(root, text="0")
        self.label_total_ingreso_valor.grid(row=8, column=1)

        # Gastos
        self.label_gasto_mensual = tk.Label(root, text="Gasto Mensual:")
        self.label_gasto_mensual.grid(row=9, column=0)
        self.entry_gasto_mensual = tk.Entry(root)
        self.entry_gasto_mensual.grid(row=9, column=1)

        # Botón para agregar gasto mensual
        self.btn_add_gasto = tk.Button(root, text="Agregar Gasto Mensual", command=self.agregar_gasto)
        self.btn_add_gasto.grid(row=10, column=0, columnspan=2)

        # Gasto extra
        self.label_fecha_gasto_extra = tk.Label(root, text="Fecha (dd/mm/aa):")
        self.label_fecha_gasto_extra.grid(row=11, column=0)
        self.entry_fecha_gasto_extra = tk.Entry(root)
        self.entry_fecha_gasto_extra.grid(row=11, column=1)

        self.label_tipo_gasto_extra = tk.Label(root, text="Tipo de Gasto Extra:")
        self.label_tipo_gasto_extra.grid(row=12, column=0)
        self.entry_tipo_gasto_extra = tk.Entry(root)
        self.entry_tipo_gasto_extra.grid(row=12, column=1)

        self.label_gasto_extra = tk.Label(root, text="Gasto Extra:")
        self.label_gasto_extra.grid(row=13, column=0)
        self.entry_gasto_extra = tk.Entry(root)
        self.entry_gasto_extra.grid(row=13, column=1)

        # Botón para agregar gasto extra
        self.btn_add_gasto_extra = tk.Button(root, text="Agregar Gasto Extra", command=self.agregar_gasto_extra)
        self.btn_add_gasto_extra.grid(row=14, column=0, columnspan=2)

        # Lista de gastos
        self.label_lista_gastos = tk.Label(root, text="Lista de Gastos:")
        self.label_lista_gastos.grid(row=15, column=0)
        self.listbox_gastos = tk.Listbox(root, selectbackground=root.cget("background"))
        self.listbox_gastos.grid(row=15, column=1)

        # Total gastos del hogar
        self.label_total_gasto = tk.Label(root, text="Total Gastos del Hogar:")
        self.label_total_gasto.grid(row=16, column=0)
        self.label_total_gasto_valor = tk.Label(root, text="0")
        self.label_total_gasto_valor.grid(row=16, column=1)

        # Botón para calcular y mostrar el saldo
        self.btn_calcular_saldo = tk.Button(root, text="Calcular Saldo y Resumen", command=self.calcular_saldo_y_resumen)
        self.btn_calcular_saldo.grid(row=17, column=0, columnspan=2)

        # Desactivar selección
        self.listbox_ingresos.bind("<Button-1>", lambda event: "break")
        self.listbox_gastos.bind("<Button-1>", lambda event: "break")

    def agregar_sueldo(self):
        nombre = self.entry_nombre.get()
        sueldo_mensual = float(self.entry_sueldo_mensual.get() or 0)
        if nombre in self.ingresos:
            self.ingresos[nombre]['total'] += sueldo_mensual
        else:
            self.ingresos[nombre] = {'total': sueldo_mensual, 'extra': []}

        self.actualizar_lista_ingresos()
        self.actualizar_total_ingreso_hogar()

    def agregar_ingreso_extra(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha_extra.get()
        tipo = self.entry_tipo_ingreso_extra.get()
        ingreso_extra = float(self.entry_ingreso_extra.get() or 0)
        
        if nombre in self.ingresos:
            self.ingresos[nombre]['extra'].append((fecha, tipo, ingreso_extra))
            self.ingresos[nombre]['total'] += ingreso_extra
        else:
            self.ingresos[nombre] = {'total': ingreso_extra, 'extra': [(fecha, tipo, ingreso_extra)]}

        self.actualizar_lista_ingresos()
        self.actualizar_total_ingreso_hogar()

    def agregar_gasto(self):
        nombre = self.entry_nombre.get()
        gasto_mensual = float(self.entry_gasto_mensual.get() or 0)
        if nombre in self.gastos:
            self.gastos[nombre]['total'] += gasto_mensual
        else:
            self.gastos[nombre] = {'total': gasto_mensual, 'extra': []}

        self.actualizar_lista_gastos()
        self.actualizar_total_gasto_hogar()

    def agregar_gasto_extra(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha_gasto_extra.get()
        tipo = self.entry_tipo_gasto_extra.get()
        gasto_extra = float(self.entry_gasto_extra.get() or 0)
        
        if nombre in self.gastos:
            self.gastos[nombre]['extra'].append((fecha, tipo, gasto_extra))
            self.gastos[nombre]['total'] += gasto_extra
        else:
            self.gastos[nombre] = {'total': gasto_extra, 'extra': [(fecha, tipo, gasto_extra)]}

        self.actualizar_lista_gastos()
        self.actualizar_total_gasto_hogar()

    def actualizar_lista_ingresos(self):
        self.listbox_ingresos.delete(0, tk.END)  # Limpiar la lista
        for nombre, datos in self.ingresos.items():
            self.listbox_ingresos.insert(tk.END, f"{nombre}: {datos['total']}")

    def actualizar_lista_gastos(self):
        self.listbox_gastos.delete(0, tk.END)  # Limpiar la lista
        for nombre, datos in self.gastos.items():
            self.listbox_gastos.insert(tk.END, f"{nombre}: {datos['total']}")

    def actualizar_total_ingreso_hogar(self):
        total_ingreso = sum(datos['total'] for datos in self.ingresos.values())
        self.label_total_ingreso_valor.config(text=f"{total_ingreso}")

    def actualizar_total_gasto_hogar(self):
        total_gasto = sum(datos['total'] for datos in self.gastos.values())
        self.label_total_gasto_valor.config(text=f"{total_gasto}")

    def calcular_saldo_y_resumen(self):
        saldo_por_persona = {}
        for nombre in self.ingresos.keys():
            ingresos = self.ingresos[nombre]['total']
            gastos = self.gastos.get(nombre, {'total': 0})['total']
            saldo_por_persona[nombre] = ingresos - gastos

        total_ingresos_mes = sum([datos['total'] for datos in self.ingresos.values()])
        total_gastos_mes = sum([datos['total'] for datos in self.gastos.values()])
        saldo_total_mes = total_ingresos_mes - total_gastos_mes

        resumen = f"Saldo al finalizar el mes:\n"
        for nombre, saldo in saldo_por_persona.items():
            resumen += f"{nombre}: {saldo}\n"

        resumen += f"\nResumen mensual:\n"
        resumen += f"Total ingresos del mes: {total_ingresos_mes}\n"
        resumen += f"Total gastos del mes: {total_gastos_mes}\n"
        resumen += f"Saldo total del mes: {saldo_total_mes}\n"

        # Calcular la categoría con mayor gasto extra
        categorias_gastos = {}
        for datos in self.gastos.values():
            for fecha, tipo, monto in datos['extra']:
                if tipo in categorias_gastos:
                    categorias_gastos[tipo] += monto
                else:
                    categorias_gastos[tipo] = monto

        if categorias_gastos:
            categoria_mayor_gasto = max(categorias_gastos, key=categorias_gastos.get)
            resumen += f"\nCategoría con mayor gasto extra: {categoria_mayor_gasto} ({categorias_gastos[categoria_mayor_gasto]})\n"
            resumen += "Lista de categorías y sus gastos extra:\n"
            for categoria, monto in categorias_gastos.items():
                resumen += f"{categoria}: {monto}\n"

        messagebox.showinfo("Resumen Mensual", resumen)

if __name__ == "__main__":
    root = tk.Tk()
    app = EconomiaHogarApp(root)
    root.mainloop()

