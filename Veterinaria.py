import sqlite3
from tkinter import *
from tkinter import messagebox


def init_db():
    conn = sqlite3.connect('veterinaria.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        especie TEXT,
        raza TEXT,
        edad INTEGER,
        propietario TEXT
    )
    ''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS propietarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        direccion TEXT,
        telefono TEXT
    )
    ''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS medicamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        cantidad INTEGER,
        precio REAL
    )
    ''')
    conn.commit()
    conn.close()


class Paciente:
    def __init__(self, nombre, especie, raza, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario

    def registrar(self):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('INSERT INTO pacientes (nombre, especie, raza, edad, propietario) VALUES (?, ?, ?, ?, ?)',
                  (self.nombre, self.especie, self.raza, self.edad, self.propietario))
        conn.commit()
        conn.close()

    def actualizar(self, id, nombre, especie, raza, edad, propietario):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('''
        UPDATE pacientes
        SET nombre = ?, especie = ?, raza = ?, edad = ?, propietario = ?
        WHERE id = ?
        ''', (nombre, especie, raza, edad, propietario, id))
        conn.commit()
        conn.close()

class Medicamento:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def registrar(self):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('INSERT INTO medicamentos (nombre, cantidad, precio) VALUES (?, ?, ?)',
                  (self.nombre, self.cantidad, self.precio))
        conn.commit()
        conn.close()

    def actualizar(self, id, nombre, cantidad, precio):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('''
        UPDATE medicamentos
        SET nombre = ?, cantidad = ?, precio = ?
        WHERE id = ?
        ''', (nombre, cantidad, precio, id))
        conn.commit()
        conn.close()
        

class Cita:
    def __init__(self, paciente_id, fecha, hora, motivo):
        self.paciente_id = paciente_id
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

    def programar(self):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('INSERT INTO medicamentos (nombre, cantidad, precio) VALUES (?, ?, ?)',
                  (self.paciente_id, self.fecha, self.hora, self.motivo))
        conn.commit()
        conn.close()
        
class HistorialMedico:
    def __init__(self, paciente_id, fecha, descripcion, diagnostico, tratamiento):
        self.paciente_id = paciente_id
        self.fecha = fecha
        self.descripcion = descripcion
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def registrar(self):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('''
        INSERT INTO historial_medico (paciente_id, fecha, descripcion, diagnostico, tratamiento)
        VALUES (?, ?, ?, ?, ?)
        ''', (self.paciente_id, self.fecha, self.descripcion, self.diagnostico, self.tratamiento))
        conn.commit()
        conn.close()

    @staticmethod
    def consultar(paciente_id):
        conn = sqlite3.connect('veterinaria.db')
        c = conn.cursor()
        c.execute('''
        SELECT fecha, descripcion, diagnostico, tratamiento
        FROM historial_medico
        WHERE paciente_id = ?
        ''', (paciente_id,))
        historial = c.fetchall()
        conn.close()
        return historial



class AplicacionVeterinaria:
    def __init__(self, root):
        self.root = root
        self.root.title("Clínica Veterinaria JBE")
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Clínica Veterinaria JBE")
        self.label.pack()

        self.label = Label(self.root, text="CLINICA VETERINARIA JBE", font=("ink free", 16, "bold"), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.registrar_paciente_btn = Button(self.root, text="Registrar Paciente", command=self.registrar_paciente, font=("ink free", 12), bg="#62a07b", fg="white")
        self.registrar_paciente_btn.pack(pady=5)

        self.actualizar_paciente_btn = Button(self.root, text="Actualizar Paciente", command=self.actualizar_paciente, font=("ink free", 12), bg="#4f8b89", fg="white")
        self.actualizar_paciente_btn.pack(pady=5)

        self.registrar_medicamento_btn = Button(self.root, text="Registrar Medicamento", command=self.registrar_medicamento, font=("ink free", 12), bg="#536c8d", fg="white")
        self.registrar_medicamento_btn.pack(pady=5)

        self.actualizar_medicamento_btn = Button(self.root, text="Actualizar Medicamento", command=self.actualizar_medicamento, font=("ink free", 12), bg="#5c4f79", fg="white")
        self.actualizar_medicamento_btn.pack(pady=5)

        self.actualizar_medicamento_btn = Button(self.root, text="Programar Cita", command=self.actualizar_medicamento, font=("ink free", 12), bg="#5c4f79", fg="white")
        self.actualizar_medicamento_btn.pack(pady=5)
        
        self.registrar_historial_btn = Button(self.root, text="Registrar Historial Médico", command=self.registrar_historial, font=("ink free", 12), bg="#613860", fg="white")
        self.registrar_historial_btn.pack(pady=5)

        self.consultar_historial_btn = Button(self.root, text="Consultar Historial Médico", command=self.consultar_historial, font=("ink free", 12), bg="#3F51B5", fg="white")
        self.consultar_historial_btn.pack(pady=5)
        
    def registrar_paciente(self):
        self.new_window = Toplevel(self.root)
        self.app = RegistrarPaciente(self.new_window)

    def actualizar_paciente(self):
        self.new_window = Toplevel(self.root)
        self.app = ActualizarPaciente(self.new_window)

    def registrar_medicamento(self):
        self.new_window = Toplevel(self.root)
        self.app = RegistrarMedicamento(self.new_window)

    def actualizar_medicamento(self):
        self.new_window = Toplevel(self.root)
        self.app = ActualizarMedicamento(self.new_window)

    def programar_cita(self):
        self.new_window = Toplevel(self.root)
        self.app = ProgramarCita(self.new_window)
        
    def registrar_historial(self):
        self.new_window = Toplevel(self.root)
        self.app = RegistrarHistorial(self.new_window)

    def consultar_historial(self):
        self.new_window = Toplevel(self.root)
        self.app = ConsultarHistorial(self.new_window)
        
class RegistrarPaciente:
    def __init__(self, master):
        self.master = master
        self.master.title("Registrar Paciente")
        self.master.configure(bg="#e0f7fa")
        
        self.label_nombre = Label(self.master, text="Nombre", font=("ink free", 12), bg="#62a07b")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = Entry(self.master, font=("Helvetica", 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.label_especie = Label(self.master, text="Especie", font=("ink free", 12), bg="#62a07b")
        self.label_especie.grid(row=1, column=0, padx=10, pady=5)
        self.entry_especie = Entry(self.master, font=("Helvetica", 12))
        self.entry_especie.grid(row=1, column=1, padx=10, pady=5)

        self.label_raza = Label(self.master, text="Raza", font=("ink free", 12), bg="#62a07b")
        self.label_raza.grid(row=2, column=0, padx=10, pady=5)
        self.entry_raza = Entry(self.master, font=("Helvetica", 12))
        self.entry_raza.grid(row=2, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Edad", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)

        self.registrar_btn = Button(self.master, text="Registrar", command=self.registrar_paciente)
        self.registrar_btn.grid(row=5, column=1)

    def registrar_paciente(self):
        nombre = self.entry_nombre.get()
        especie = self.entry_especie.get()
        raza = self.entry_raza.get()
        edad = self.entry_edad.get()
        propietario = self.entry_propietario.get()

        paciente = Paciente(nombre, especie, raza, edad, propietario)
        paciente.registrar()
        messagebox.showinfo("Éxito", "Paciente registrado exitosamente")
        self.master.destroy()

class ActualizarPaciente:
    def __init__(self, master):
        self.master = master
        self.master.title("Actualizar Paciente")

        self.label_nombre = Label(self.master, text="ID del Paciente", font=("ink free", 12), bg="#4f8b89")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = Entry(self.master, font=("Helvetica", 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.label_especie = Label(self.master, text="Nuevo Nombre", font=("ink free", 12), bg="#4f8b89")
        self.label_especie.grid(row=1, column=0, padx=10, pady=5)
        self.entry_especie = Entry(self.master, font=("Helvetica", 12))
        self.entry_especie.grid(row=1, column=1, padx=10, pady=5)

        self.label_raza = Label(self.master, text="Nueva Especie", font=("ink free", 12), bg="#4f8b89")
        self.label_raza.grid(row=2, column=0, padx=10, pady=5)
        self.entry_raza = Entry(self.master, font=("Helvetica", 12))
        self.entry_raza.grid(row=2, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Raza Nueva ", font=("ink free", 12), bg="#4f8b89")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Nueva Edad", font=("ink free", 12), bg="#4f8b89")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Nuevo Propietario", font=("ink free", 12), bg="#4f8b89")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)
        
        self.actualizar_btn = Button(self.master, text="Actualizar", command=self.actualizar_paciente)
        self.actualizar_btn.grid(row=6, column=1)
        
    def actualizar_paciente(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        especie = self.entry_especie.get()
        raza = self.entry_raza.get()
        edad = self.entry_edad.get()
        propietario = self.entry_propietario.get()

        paciente = Paciente(nombre, especie, raza, edad, propietario)
        paciente.actualizar(id, nombre, especie, raza, edad, propietario)
        messagebox.showinfo("Éxito", "Paciente actualizado exitosamente")
        self.master.destroy()

class RegistrarMedicamento:
    def __init__(self, master):
        self.master = master
        self.master.title("Registrar Medicamento")

        self.label_edad = Label(self.master, text="Nombre ", font=("ink free", 12), bg="#536c8d")
        self.label_edad.grid(row=0, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=0, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Cantidad", font=("ink free", 12), bg="#536c8d")
        self.label_edad.grid(row=1, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=1, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Precio", font=("ink free", 12), bg="#536c8d")
        self.label_edad.grid(row=2, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=2, column=1, padx=10, pady=5)

        self.registrar_btn = Button(self.master, text="Registrar", command=self.registrar_medicamento)
        self.registrar_btn.grid(row=3, column=1)

    def registrar_medicamento(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()

        medicamento = Medicamento(nombre, cantidad, precio)
        medicamento.registrar(nombre, cantidad, precio)
        messagebox.showinfo( "Medicamento registrado")
        self.master.destroy()

class ActualizarMedicamento:
    def __init__(self, master):
        self.master = master
        self.master.title("Actualizar Medicamento")

        self.label_edad = Label(self.master, text="ID del Medicamento", font=("ink free", 12), bg="#5c4f79")
        self.label_edad.grid(row=0, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=0, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Nuevo Nombre", font=("ink free", 12), bg="#5c4f79")
        self.label_edad.grid(row=1, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=0, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Nueva Cantidad", font=("ink free", 12), bg="#5c4f79")
        self.label_edad.grid(row=1, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=1, column=1, padx=10, pady=5)
        
        self.label_edad = Label(self.master, text="Nuevo Precio", font=("ink free", 12), bg="#5c4f79")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)       

        self.actualizar_btn = Button(self.master, text="Actualizar", command=self.actualizar_medicamento)
        self.actualizar_btn.grid(row=4, column=1)

    def actualizar_medicamento(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()

        medicamento = Medicamento(nombre, cantidad, precio)
        medicamento.actualizar(id, nombre, cantidad, precio)
        messagebox.showinfo("Éxito", "Medicamento actualizado ")
        self.master.destroy()
        
class ProgramarCita:
    def __init__(self, master):
        self.master = master
        self.master.title("Programar nueva cita")

        self.label_id = Label(self.master, text="Paciente")
        self.label_id.grid(row=0, column=0)
        self.entry_id = Entry(self.master)
        self.entry_id.grid(row=0, column=1)

        self.label_edad = Label(self.master, text="Paciente", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Tipo de cita", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Fecha de la cita", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)
        
        self.label_edad = Label(self.master, text="Propietario", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5) 

        self.actualizar_btn = Button(self.master, text="Actualizar", command=self.programar_cita)
        self.actualizar_btn.grid(row=4, column=1)

    def programar_cita (self):
        paciente_id = self.entry_id.get()
        fecha = self.entry_nombre.get()
        hora = self.entry_cantidad.get()
        motivo = self.entry_precio.get()

        cita = Cita(paciente_id, fecha, hora, motivo)
        cita.actualizar(paciente_id, fecha, hora, motivo)
        messagebox.showinfo("Éxito", "Cita programada")
        self.master.destroy()
        
        

        self.registrar_btn = Button(self.master, text="Registrar", command=self.programar_cita)
        self.registrar_btn.grid(row=5, column=1)
        
class RegistrarHistorial:
    def __init__(self, master):
        self.master = master
        self.master.title("Registrar Historial Médico")

        self.label_edad = Label(self.master, text="ID del paciente", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=0, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=0, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Fecha (YYYY-MM-DD)", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=1, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=1, column=1, padx=10, pady=5)

        self.label_edad = Label(self.master, text="Descripción", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=2, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=2, column=1, padx=10, pady=5)
        
        self.label_edad = Label(self.master, text="Diagnóstico", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=3, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=5)  
        
        self.label_edad = Label(self.master, text="Tratamiento", font=("ink free", 12), bg="#62a07b")
        self.label_edad.grid(row=4, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=4, column=1, padx=10, pady=5)  
    
        self.registrar_btn = Button(self.master, text="Registrar", command=self.registrar_historial)
        self.registrar_btn.grid(row=5, column=1)

    def registrar_historial(self):
        paciente_id = self.entry_paciente_id.get()
        fecha = self.entry_fecha.get()
        descripcion = self.entry_descripcion.get()
        diagnostico = self.entry_diagnostico.get()
        tratamiento = self.entry_tratamiento.get()

        historial = HistorialMedico(paciente_id, fecha, descripcion, diagnostico, tratamiento)
        historial.registrar()
        messagebox.showinfo("Éxito", "Historial médico registrado exitosamente")
        self.master.destroy()

class ConsultarHistorial:
    def __init__(self, master):
        self.master = master
        self.master.title("Consultar Historial Médico")

        self.label_edad = Label(self.master, text="ID del paciente", font=("ink free", 12), bg="#3F51B5")
        self.label_edad.grid(row=0, column=0, padx=10, pady=5)
        self.entry_edad = Entry(self.master, font=("Helvetica", 12))
        self.entry_edad.grid(row=0, column=1)  

        self.consultar_btn = Button(self.master, text="Consultar", command=self.consultar_historial)
        self.consultar_btn.grid(row=1, column=1)

        self.text_historial = Text(self.master)
        self.text_historial.grid(row=2, column=0, columnspan=2)

    def consultar_historial(self):
        paciente_id = self.entry_paciente_id.get()
        historial = HistorialMedico.consultar(paciente_id)
        self.text_historial.delete(1.0, END)
        for registro in historial:
            self.text_historial.insert(END, f"Fecha: {registro[0]}\nDescripción: {registro[1]}\nDiagnóstico: {registro[2]}\nTratamiento: {registro[3]}\n\n")

if __name__ == "__main__":
    init_db()
    root = Tk()
    app = AplicacionVeterinaria(root)
    root.mainloop()

