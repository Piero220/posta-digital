class Medico:
    """Médico del centro de salud (datos ficticios)."""

    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self._nombre = nombre
        self._especialidad = especialidad

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def especialidad(self):
        return self._especialidad

    # Setters
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._especialidad}"
