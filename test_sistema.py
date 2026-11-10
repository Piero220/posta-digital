"""Pruebas automáticas con pytest. Ejecutar: pytest -v"""
import pytest
import main as sistema
from paciente import Paciente
from cita import Cita


@pytest.fixture(autouse=True)
def datos_limpios():
    """Deja las listas vacías y carga un paciente y un médico antes de cada prueba."""
    sistema.pacientes.clear()
    sistema.medicos.clear()
    sistema.citas.clear()
    sistema.registrar_paciente("P001", "Juan", 22)
    sistema.registrar_medico("M001", "Oscar Torres", "Cardiologia")


def test_normal_programar_cita_y_registrar_atencion():
    sistema.programar_cita("C001", "P001", "M001", "04/11/2026")
    sistema.registrar_atencion("C001", "Control general")
    assert len(sistema.pacientes[0].historial) == 1


@pytest.mark.parametrize("edad", [0, 120])
def test_extremo_edades_validas(edad):
    assert Paciente("P010", "Ana", edad).edad == edad


@pytest.mark.parametrize("edad", [-1, 121])
def test_extremo_edades_fuera_de_rango(edad):
    with pytest.raises(ValueError):
        Paciente("P011", "Ana", edad)


def test_error_edad_no_numerica():
    with pytest.raises(ValueError):
        Paciente("P012", "Ana", "abc")


def test_duplicado_codigo():
    with pytest.raises(ValueError):
        sistema.registrar_paciente("P001", "Otro", 30)


def test_referencia_invalida_paciente():
    with pytest.raises(ValueError):
        sistema.programar_cita("C002", "P999", "M001", "04/11/2026")


def test_fecha_con_formato_incorrecto():
    with pytest.raises(ValueError):
        sistema.programar_cita("C003", "P001", "M001", "2026-11-04")


def test_buscar_por_codigo_existente_e_inexistente():
    assert sistema.buscar_por_codigo(sistema.pacientes, "P001").nombre == "Juan"
    assert sistema.buscar_por_codigo(sistema.pacientes, "P999") is None


def test_filtrar_medicos_con_y_sin_resultados():
    assert len(sistema.filtrar_medicos_por_especialidad("cardiologia")) == 1
    assert sistema.filtrar_medicos_por_especialidad("Pediatria") == []


def test_nombre_del_paciente_se_muestra_oculto():
    assert "Juan" not in sistema.pacientes[0].resumen()
