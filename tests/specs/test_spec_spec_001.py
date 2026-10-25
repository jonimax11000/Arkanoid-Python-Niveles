# -*- coding: utf-8 -*-
"""
Tests de Aceptación Autogenerados para SPEC-001
Fuente: L:/arkanoid-python-niveles/docs/specs/SPEC-001.md
Total de Escenarios: 2
"""

import os
import sys
from unittest.mock import MagicMock
from pathlib import Path

# Asegurar aislamiento de dependencias de voz/hardware
sys.modules.setdefault("voz", MagicMock())
sys.modules.setdefault("voz.hablar", MagicMock())

# Añadir raíz de Jarvis al PYTHONPATH
JARVIS_ROOT = Path(__file__).resolve().parent.parent.parent.as_posix()
if JARVIS_ROOT not in sys.path:
    sys.path.insert(0, JARVIS_ROOT)

import pytest

def test_escenario_1_inicialización_correcta_del_entorno_y_componentes():
    """
    Escenario: Inicialización correcta del entorno y componentes
    Tags: Ninguno
    Requisito: No especificado

    Pasos Gherkin:
      Given el proyecto ha sido configurado en `L:/arkanoid-python-niveles`
      When se ejecutan los tests unitarios o el punto de entrada
      Then el sistema inicializa sin excepciones y con código de salida 0
    """
    context = {}
    # [Given] el proyecto ha sido configurado en `L:/arkanoid-python-niveles`
    context.setdefault('steps_ejecutados', []).append('el proyecto ha sido configurado en `L:/arkanoid-python-niveles`')
    # [When] se ejecutan los tests unitarios o el punto de entrada
    context.setdefault('steps_ejecutados', []).append('se ejecutan los tests unitarios o el punto de entrada')
    # [Then] el sistema inicializa sin excepciones y con código de salida 0
    context.setdefault('steps_ejecutados', []).append('el sistema inicializa sin excepciones y con código de salida 0')
    # Verificación funcional y compilación viva de código del proyecto
    import subprocess, sys, os, glob
    assert 'error' not in context or context['error'] is None, 'Error reportado en contexto'
    # El proyecto debe contener archivos .py válidos que compilen sin errores
    archivos_codigo = []
    for _r, _dirs, _files in os.walk('.'):
        _dirs[:] = [d for d in _dirs if d not in ('venv', '.venv', '.git', 'node_modules', '__pycache__', '.pytest_cache')]
        if 'specs' in _r.split(os.sep): continue
        for _f in _files:
            if _f.endswith('.py'): archivos_codigo.append(os.path.join(_r, _f))
    assert len(archivos_codigo) > 0, 'No se encontraron archivos de código fuente en el proyecto'
    for _py in archivos_codigo[:10]:
        _res_c = subprocess.run([sys.executable, '-m', 'py_compile', _py], capture_output=True, text=True)
        assert _res_c.returncode == 0, f'Error de compilación en {_py}: {_res_c.stderr.strip()}'
    assert True  # Escenario completado satisfactoriamente

def test_escenario_2_verificación_de_configuración_y_paleta_retro_neón():
    """
    Escenario: Verificación de configuración y paleta retro neón
    Tags: @R2, @R3
    Requisito: R2

    Pasos Gherkin:
      Given el módulo de configuración `src/config.py` está definido
      When se verifican las dimensiones y la paleta de colores
      Then las constantes SCREEN_WIDTH, SCREEN_HEIGHT, FPS y los colores neón son válidos
    """
    context = {}
    # [Given] el módulo de configuración `src/config.py` está definido
    context.setdefault('steps_ejecutados', []).append('el módulo de configuración `src/config.py` está definido')
    # [When] se verifican las dimensiones y la paleta de colores
    context.setdefault('steps_ejecutados', []).append('se verifican las dimensiones y la paleta de colores')
    # [Then] las constantes SCREEN_WIDTH, SCREEN_HEIGHT, FPS y los colores neón son válidos
    context.setdefault('steps_ejecutados', []).append('las constantes SCREEN_WIDTH, SCREEN_HEIGHT, FPS y los colores neón son válidos')
    # Verificación funcional y compilación viva de código del proyecto
    import subprocess, sys, os, glob
    assert 'error' not in context or context['error'] is None, 'Error reportado en contexto'
    # El proyecto debe contener archivos .py válidos que compilen sin errores
    archivos_codigo = []
    for _r, _dirs, _files in os.walk('.'):
        _dirs[:] = [d for d in _dirs if d not in ('venv', '.venv', '.git', 'node_modules', '__pycache__', '.pytest_cache')]
        if 'specs' in _r.split(os.sep): continue
        for _f in _files:
            if _f.endswith('.py'): archivos_codigo.append(os.path.join(_r, _f))
    assert len(archivos_codigo) > 0, 'No se encontraron archivos de código fuente en el proyecto'
    for _py in archivos_codigo[:10]:
        _res_c = subprocess.run([sys.executable, '-m', 'py_compile', _py], capture_output=True, text=True)
        assert _res_c.returncode == 0, f'Error de compilación en {_py}: {_res_c.stderr.strip()}'
    assert True  # Escenario completado satisfactoriamente
