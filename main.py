"""Programa principal del Sistema (datos ficticios).

Uso:  python main.py        -> menú interactivo
      python main.py demo   -> recorrido automático para la evidencia
"""
import sys
from paciente import Paciente
from medico import Medico
from cita import Cita

pacientes = []
medicos = []
citas = []


# ---------- Paradigma estructurado: funciones, listas y validaciones ----------

def buscar_por_codigo(coleccion, codigo):
    """Recorre la lista con un for; devuelve el objeto o None si no existe."""
    for elemento in coleccion:
        if elemento.codigo == codigo:
            return elemento
    return None


def registrar_paciente(codigo, nombre, edad):
    if buscar_por_codigo(pacientes, codigo) is not None:
        raise ValueError(f"El código {codigo} ya está registrado.")
    paciente = Paciente(codigo, nombre, edad)
    pacientes.append(paciente)
    return paciente


def registrar_medico(codigo, nombre, especialidad):
    if buscar_por_codigo(medicos, codigo) is not None:
        raise ValueError(f"El código {codigo} ya está registrado.")
    if not especialidad:
        raise ValueError("La especialidad es obligatoria.")
    medico = Medico(codigo, nombre, especialidad)
    medicos.append(medico)
    return medico


def programar_cita(codigo, cod_paciente, cod_medico, fecha):
    if buscar_por_codigo(citas, codigo) is not None:
        raise ValueError(f"La cita {codigo} ya existe.")
    paciente = buscar_por_codigo(pacientes, cod_paciente)
    if paciente is None:
        raise ValueError(f"Paciente no registrado: {cod_paciente}")
    medico = buscar_por_codigo(medicos, cod_medico)
    if medico is None:
        raise ValueError(f"Médico no registrado: {cod_medico}")
    cita = Cita(codigo, paciente, medico, fecha)
    citas.append(cita)
    return cita


def registrar_atencion(codigo_cita, diagnostico):
    cita = buscar_por_codigo(citas, codigo_cita)
    if cita is None:
        raise ValueError(f"Cita no registrada: {codigo_cita}")
    cita.registrar_atencion(diagnostico)
    return cita


# ---------- Paradigma funcional: filter() y lambda sin modificar las listas ----------

def filtrar_medicos_por_especialidad(especialidad):
    return list(filter(lambda m: m.especialidad.lower() == especialidad.lower(), medicos))


def historial_texto(paciente):
    return [cita.resumen() + f" | {cita.diagnostico}" for cita in paciente.historial]


# ---------- Menú ----------

def pedir_edad():
    try:
        return int(input("Edad: "))
    except ValueError:
        raise ValueError("La edad debe ser un número entero entre 0 y 120.")


def mostrar_menu():
    print("\n=== SISTEMA (datos ficticios) ===")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar por código")
    print("4. Programar cita")
    print("5. Registrar atención")
    print("6. Consultar historial de un paciente")
    print("7. Buscar médicos por especialidad")
    print("0. Salir")


def ejecutar_opcion(opcion):
    if opcion == "1":
        codigo, nombre = input("Código (ej. P001): "), input("Nombre ficticio: ")
        print("Registrado:", registrar_paciente(codigo, nombre, pedir_edad()).resumen())
    elif opcion == "2":
        codigo, nombre = input("Código (ej. M001): "), input("Nombre ficticio: ")
        print("Registrado:", registrar_medico(codigo, nombre, input("Especialidad: ")).resumen())
    elif opcion == "3":
        codigo = input("Código a buscar: ")
        encontrado = buscar_por_codigo(pacientes, codigo) or buscar_por_codigo(medicos, codigo)
        print(encontrado.resumen() if encontrado else "No se encontró ese código.")
    elif opcion == "4":
        cita = programar_cita(input("Código de cita (ej. C001): "), input("Código de paciente: "),
                              input("Código de médico: "), input("Fecha (DD/MM/AAAA): "))
        print("Cita creada:", cita.resumen())
    elif opcion == "5":
        registrar_atencion(input("Código de cita: "), input("Diagnóstico ficticio: "))
        print("Atención registrada en el historial.")
    elif opcion == "6":
        paciente = buscar_por_codigo(pacientes, input("Código de paciente: "))
        if paciente is None:
            print("Paciente no registrado.")
        else:
            lineas = historial_texto(paciente)
            print("\n".join(lineas) if lineas else "Sin atenciones registradas.")
    elif opcion == "7":
        lista = filtrar_medicos_por_especialidad(input("Especialidad: "))
        print("\n".join(m.resumen() for m in lista) if lista else "Sin coincidencias.")
    else:
        print("Opción no válida.")


def menu():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        try:
            ejecutar_opcion(opcion)
        except ValueError as error:   # el error se muestra y el programa continúa
            print("Error:", error)


def demo():
    print("--- Recorrido automático ---")
    print(registrar_paciente("P001", "Juan", 22).resumen())
    print(registrar_medico("M001", "Oscar Torres", "Cardiologia").resumen())
    print(registrar_medico("M002", "Ana Ruiz", "Pediatria").resumen())
    try:
        registrar_paciente("P001", "Otro", 30)
    except ValueError as error:
        print("Duplicado rechazado ->", error)
    print("Cita programada:", programar_cita("C001", "P001", "M001", "04/11/2026").resumen())
    try:
        programar_cita("C002", "P999", "M001", "04/11/2026")
    except ValueError as error:
        print("Referencia inválida ->", error)
    registrar_atencion("C001", "Control general")
    print("Historial de P001:", historial_texto(buscar_por_codigo(pacientes, "P001")))
    print("Médicos de Pediatria:", [m.resumen() for m in filtrar_medicos_por_especialidad("Pediatria")])
    print("Médicos de Neurologia:", filtrar_medicos_por_especialidad("Neurologia"))


if __name__ == "__main__":
    demo() if len(sys.argv) > 1 and sys.argv[1] == "demo" else menu()
