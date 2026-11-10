class Paciente:
    """Paciente del centro de salud (datos ficticios)."""

    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = None
        self.edad = edad          # se asigna con el setter para validar la edad
        self._historial = []      # lista de citas atendidas

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def nombre_oculto(self):
        """Muestra solo la inicial para no exponer el nombre completo."""
        return self._nombre[:1] + "***"

    @property
    def edad(self):
        return self._edad

    @property
    def historial(self):
        # Se devuelve una tupla para que no se modifique la lista original.
        return tuple(self._historial)

    # Setters
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int) or not 0 <= valor <= 120:
            raise ValueError("La edad debe ser un número entero entre 0 y 120.")
        self._edad = valor

    def agregar_atencion(self, cita):
        """Agrega una cita atendida al historial del paciente."""
        self._historial.append(cita)

    def resumen(self):
        return f"{self._codigo} - {self.nombre_oculto} - {self._edad}"
