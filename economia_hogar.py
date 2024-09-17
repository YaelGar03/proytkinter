import tkinter as tk
from tkinter import messagebox
from login import EstadoUsuario

class EconomiaHogarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Economía del Hogar")

        self.ingresos = {}
        self.gastos = {}

        # Nombre de la persona (actual)
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)
        
        usuario_actual = EstadoUsuario.usuario_actual if EstadoUsuario.usuario_actual else ""
        self.entry_nombre.insert(0, usuario_actual)
        self.entry_nombre.config(state='readonly')

        # Botón para cerrar sesión
        self.btn_cerrar_sesion = tk.Button(root, text="Cerrar Sesión", command=self.cerrar_sesion)
        self.btn_cerrar_sesion.grid(row=0, column=2)

        # Ingreso mensual
        self.label_sueldo_mensual = tk.Label(root, text="Sueldo Mensual:")
        self.label_sueldo_mensual.grid(row=1, column=0)
        self.entry_sueldo_mensual = tk.Entry(root)
        self.entry_sueldo_mensual.grid(row=1, column=1)

        self.btn_agregar_sueldo = tk.Button(root, text="Agregar Sueldo", command=self.agregar_sueldo)
        self.btn_agregar_sueldo.grid(row=2, column=0, columnspan=2)

        # Ingreso extra
        self.label_fecha_extra = tk.Label(root, text="Fecha (Ingreso Extra):")
        self.label_fecha_extra.grid(row=3, column=0)
        self.entry_fecha_extra = tk.Entry(root)
        self.entry_fecha_extra.grid(row=3, column=1)

        self.label_tipo_ingreso_extra = tk.Label(root, text="Tipo (Ingreso Extra):")
        self.label_tipo_ingreso_extra.grid(row=4, column=0)
        self.entry_tipo_ingreso_extra = tk.Entry(root)
        self.entry_tipo_ingreso_extra.grid(row=4, column=1)

        self.label_ingreso_extra = tk.Label(root, text="Ingreso Extra:")
        self.label_ingreso_extra.grid(row=5, column=0)
        self.entry_ingreso_extra = tk.Entry(root)
        self.entry_ingreso_extra.grid(row=5, column=1)

        self.btn_agregar_ingreso_extra = tk.Button(root, text="Agregar Ingreso Extra", command=self.agregar_ingreso_extra)
        self.btn_agregar_ingreso_extra.grid(row=6, column=0, columnspan=2)

        # Lista de ingresos
        self.label_lista_ingresos = tk.Label(root, text="Lista de Ingresos:")
        self.label_lista_ingresos.grid(row=7, column=0)
        self.listbox_ingresos = tk.Listbox(root)
        self.listbox_ingresos.grid(row=7, column=1)

        self.label_total_ingreso = tk.Label(root, text="Total Ingreso del Hogar:")
        self.label_total_ingreso.grid(row=8, column=0)
        self.label_total_ingreso_valor = tk.Label(root, text="0")
        self.label_total_ingreso_valor.grid(row=8, column=1)

        # Gasto mensual
        self.label_gasto_mensual = tk.Label(root, text="Gasto Mensual:")
        self.label_gasto_mensual.grid(row=9, column=0)
        self.entry_gasto_mensual = tk.Entry(root)
        self.entry_gasto_mensual.grid(row=9, column=1)

        self.btn_agregar_gasto = tk.Button(root, text="Agregar Gasto", command=self.agregar_gasto)
        self.btn_agregar_gasto.grid(row=10, column=0, columnspan=2)

        # Gasto extra
        self.label_fecha_gasto_extra = tk.Label(root, text="Fecha (Gasto Extra):")
        self.label_fecha_gasto_extra.grid(row=11, column=0)
        self.entry_fecha_gasto_extra = tk.Entry(root)
        self.entry_fecha_gasto_extra.grid(row=11, column=1)

        self.label_tipo_gasto_extra = tk.Label(root, text="Tipo (Gasto Extra):")
        self.label_tipo_gasto_extra.grid(row=12, column=0)
        self.entry_tipo_gasto_extra = tk.Entry(root)
        self.entry_tipo_gasto_extra.grid(row=12, column=1)

        self.label_gasto_extra = tk.Label(root, text="Gasto Extra:")
        self.label_gasto_extra.grid(row=13, column=0)
        self.entry_gasto_extra = tk.Entry(root)
        self.entry_gasto_extra.grid(row=13, column=1)

        self.btn_agregar_gasto_extra = tk.Button(root, text="Agregar Gasto Extra", command=self.agregar_gasto_extra)
        self.btn_agregar_gasto_extra.grid(row=14, column=0, columnspan=2)

        # Lista de gastos
        self.label_lista_gastos = tk.Label(root, text="Lista de Gastos:")
        self.label_lista_gastos.grid(row=15, column=0)
        self.listbox_gastos = tk.Listbox(root)
        self.listbox_gastos.grid(row=15, column=1)

        self.label_total_gasto = tk.Label(root, text="Total Gastos del Hogar:")
        self.label_total_gasto.grid(row=16, column=0)
        self.label_total_gasto_valor = tk.Label(root, text="0")
        self.label_total_gasto_valor.grid(row=16, column=1)

        # Botón para calcular saldo y resumen
        self.btn_calcular_saldo = tk.Button(root, text="Calcular Saldo y Resumen", command=self.calcular_saldo_y_resumen)
        self.btn_calcular_saldo.grid(row=17, column=0, columnspan=2)

    def cerrar_sesion(self):
        EstadoUsuario.usuario_actual = None
        self.root.destroy()
        import login
        login.main()

    def agregar_sueldo(self):
        nombre = EstadoUsuario.usuario_actual
        sueldo_mensual = float(self.entry_sueldo_mensual.get() or 0)
        if nombre in self.ingresos:
            self.ingresos[nombre]['total'] += sueldo_mensual
        else:
            self.ingresos[nombre] = {'total': sueldo_mensual, 'extra': []}
        self.actualizar_lista_ingresos()
        self.actualizar_total_ingreso_hogar()

    def agregar_ingreso_extra(self):
        nombre = EstadoUsuario.usuario_actual
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
        nombre = EstadoUsuario.usuario_actual
        gasto_mensual = float(self.entry_gasto_mensual.get() or 0)
        if nombre in self.gastos:
            self.gastos[nombre]['total'] += gasto_mensual
        else:
            self.gastos[nombre] = {'total': gasto_mensual, 'extra': []}
        self.actualizar_lista_gastos()
        self.actualizar_total_gasto_hogar()

    def agregar_gasto_extra(self):
        nombre = EstadoUsuario.usuario_actual
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
        self.listbox_ingresos.delete(0, tk.END)
        nombre = EstadoUsuario.usuario_actual
        if nombre in self.ingresos:
            detalles = self.ingresos[nombre]
            self.listbox_ingresos.insert(tk.END, f"{nombre}: {detalles['total']}")
            for extra in detalles['extra']:
                self.listbox_ingresos.insert(tk.END, f"  {extra[1]}: {extra[2]}")  # Omitir la fecha

    def actualizar_lista_gastos(self):
        self.listbox_gastos.delete(0, tk.END)
        nombre = EstadoUsuario.usuario_actual
        if nombre in self.gastos:
            detalles = self.gastos[nombre]
            self.listbox_gastos.insert(tk.END, f"{nombre}: {detalles['total']}")
            for extra in detalles['extra']:
                self.listbox_gastos.insert(tk.END, f"  {extra[1]}: {extra[2]}")  # Omitir la fecha

    def actualizar_total_ingreso_hogar(self):
        total_ingreso = sum(detalles['total'] for detalles in self.ingresos.values())
        self.label_total_ingreso_valor.config(text=f"{total_ingreso:.2f}")

    def actualizar_total_gasto_hogar(self):
        total_gasto = sum(detalles['total'] for detalles in self.gastos.values())
        self.label_total_gasto_valor.config(text=f"{total_gasto:.2f}")

    def calcular_saldo_y_resumen(self):
        nombre = EstadoUsuario.usuario_actual
        saldo_total = 0
        resumen = []

        if nombre in self.ingresos:
            ingresos_detalles = self.ingresos[nombre]
            saldo_total += ingresos_detalles['total']
            resumen.append(f"**Ingresos**")
            resumen.append(f"Sueldo Mensual: {ingresos_detalles['total']:.2f}")
            for extra in ingresos_detalles['extra']:
                resumen.append(f"{extra[0]} - {extra[1]}: {extra[2]:.2f}")

        if nombre in self.gastos:
            gastos_detalles = self.gastos[nombre]
            saldo_total -= gastos_detalles['total']
            resumen.append(f"**Gastos**")
            resumen.append(f"Gasto Mensual: {gastos_detalles['total']:.2f}")
            for extra in gastos_detalles['extra']:
                resumen.append(f"{extra[0]} - {extra[1]}: {extra[2]:.2f}")

        resumen.append(f"**Saldo Total**: {saldo_total:.2f}")

        # Mostrar el resumen en un mensaje emergente
        resumen_mensaje = "\n".join(resumen)
        messagebox.showinfo("Resumen", resumen_mensaje)

if __name__ == "__main__":
    root = tk.Tk()
    app = EconomiaHogarApp(root)
    root.mainloop()


