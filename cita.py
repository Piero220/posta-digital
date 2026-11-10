from datetime import datetime


class Cita:
    """Cita médica: une un paciente con un médico en una fecha."""

    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = None
        self.fecha = fecha        # se asigna con el setter para validar el formato
        self._diagnostico = None

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    @property
    def diagnostico(self):
        return self._diagnostico

    @property
    def atendida(self):
        return self._diagnostico is not None

    # Setters
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor

    @medico.setter
    def medico(self, valor):
        self._medico = valor

    @fecha.setter
    def fecha(self, valor):
        try:
            datetime.strptime(valor, "%d/%m/%Y")
        except (ValueError, TypeError):
            raise ValueError("La fecha debe tener el formato DD/MM/AAAA.")
        self._fecha = valor

    def registrar_atencion(self, diagnostico):
        """Guarda el diagnóstico (ficticio) y agrega la cita al historial del paciente."""
        if self.atendida:
            raise ValueError(f"La cita {self._codigo} ya fue atendida.")
        if not diagnostico or not diagnostico.strip():
            raise ValueError("El diagnóstico (ficticio) es obligatorio.")
        self._diagnostico = diagnostico
        self._paciente.agregar_atencion(self)

    def resumen(self):
        return (f"{self._codigo} - {self._paciente.nombre_oculto} con el Dr. "
                f"{self._medico.nombre} el {self._fecha}")
