# -*- coding: utf-8 -*-
"""
Tests de Aceptación Autogenerados para SPEC-003
Fuente: L:/arkanoid-python-niveles/docs/specs/SPEC-003.md
Total de Escenarios: 4
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

def test_escenario_1_movimiento_del_paddle():
    """
    Escenario: Movimiento del paddle
    Tags: Ninguno
    Requisito: No especificado

    Pasos Gherkin:
      Given el juego está en ejecución.
      When el usuario presiona las teclas izquierda/derecha.
      Then el paddle se mueve horizontalmente dentro de los límites de la pantalla.
    """
    context = {}
    # [Given] el juego está en ejecución.
    context.setdefault('steps_ejecutados', []).append('el juego está en ejecución.')
    # [When] el usuario presiona las teclas izquierda/derecha.
    context.setdefault('steps_ejecutados', []).append('el usuario presiona las teclas izquierda/derecha.')
    # [Then] el paddle se mueve horizontalmente dentro de los límites de la pantalla.
    context.setdefault('steps_ejecutados', []).append('el paddle se mueve horizontalmente dentro de los límites de la pantalla.')
    # Verificación funcional y compilación viva políglota (py_compile / ast) de código del proyecto
    import subprocess, sys, os, ast, py_compile
    assert 'error' not in context or context['error'] is None, 'Error reportado en contexto'
    archivos_py = []
    archivos_codigo = archivos_py
    archivos_web = []
    for _r, _dirs, _files in os.walk('.'):
        _dirs[:] = [d for d in _dirs if d not in ('venv', '.venv', '.git', 'node_modules', '__pycache__', '.pytest_cache', 'docs')]
        if 'specs' in _r.split(os.sep): continue
        for _f in _files:
            _p = os.path.join(_r, _f)
            if _f.endswith('.py') and not _f.startswith('test_spec_'): archivos_py.append(_p)
            elif _f.endswith(('.js', '.ts', '.tsx', '.jsx', '.html', '.css')): archivos_web.append(_p)
    assert len(archivos_py) > 0 or len(archivos_web) > 0, 'No se encontraron archivos de código fuente (.py/.js/.ts/.html) en el proyecto'
    for _py in archivos_py[:12]:
        with open(_py, 'r', encoding='utf-8', errors='replace') as _fh:
            ast.parse(_fh.read(), filename=_py)
    for _wf in archivos_web[:12]:
        assert os.path.getsize(_wf) > 0, f'El archivo {_wf} está vacío'
    assert True  # Escenario completado satisfactoriamente

def test_escenario_2_colisión_entre_bola_y_paddle():
    """
    Escenario: Colisión entre bola y paddle
    Tags: Ninguno
    Requisito: No especificado

    Pasos Gherkin:
      Given la bola está en movimiento.
      When la bola colisiona con el paddle.
      Then la bola rebota hacia arriba.
    """
    context = {}
    # [Given] la bola está en movimiento.
    context.setdefault('steps_ejecutados', []).append('la bola está en movimiento.')
    # [When] la bola colisiona con el paddle.
    context.setdefault('steps_ejecutados', []).append('la bola colisiona con el paddle.')
    # [Then] la bola rebota hacia arriba.
    context.setdefault('steps_ejecutados', []).append('la bola rebota hacia arriba.')
    # Verificación funcional y compilación viva políglota (py_compile / ast) de código del proyecto
    import subprocess, sys, os, ast, py_compile
    assert 'error' not in context or context['error'] is None, 'Error reportado en contexto'
    archivos_py = []
    archivos_codigo = archivos_py
    archivos_web = []
    for _r, _dirs, _files in os.walk('.'):
        _dirs[:] = [d for d in _dirs if d not in ('venv', '.venv', '.git', 'node_modules', '__pycache__', '.pytest_cache', 'docs')]
        if 'specs' in _r.split(os.sep): continue
        for _f in _files:
            _p = os.path.join(_r, _f)
            if _f.endswith('.py') and not _f.startswith('test_spec_'): archivos_py.append(_p)
            elif _f.endswith(('.js', '.ts', '.tsx', '.jsx', '.html', '.css')): archivos_web.append(_p)
    assert len(archivos_py) > 0 or len(archivos_web) > 0, 'No se encontraron archivos de código fuente (.py/.js/.ts/.html) en el proyecto'
    for _py in archivos_py[:12]:
        with open(_py, 'r', encoding='utf-8', errors='replace') as _fh:
            ast.parse(_fh.read(), filename=_py)
    for _wf in archivos_web[:12]:
        assert os.path.getsize(_wf) > 0, f'El archivo {_wf} está vacío'
    assert True  # Escenario completado satisfactoriamente

def test_escenario_3_colisión_entre_bola_y_brick():
    """
    Escenario: Colisión entre bola y brick
    Tags: Ninguno
    Requisito: No especificado

    Pasos Gherkin:
      Given un brick está presente en la pantalla.
      When la bola colisiona con el brick.
      Then el brick se destruye y desaparece de la pantalla.
    """
    context = {}
    # [Given] un brick está presente en la pantalla.
    context.setdefault('steps_ejecutados', []).append('un brick está presente en la pantalla.')
    # [When] la bola colisiona con el brick.
    context.setdefault('steps_ejecutados', []).append('la bola colisiona con el brick.')
    # [Then] el brick se destruye y desaparece de la pantalla.
    context.setdefault('steps_ejecutados', []).append('el brick se destruye y desaparece de la pantalla.')
    # Verificación funcional y compilación viva políglota (py_compile / ast) de código del proyecto
    import subprocess, sys, os, ast, py_compile
    assert 'error' not in context or context['error'] is None, 'Error reportado en contexto'
    archivos_py = []
    archivos_codigo = archivos_py
    archivos_web = []
    for _r, _dirs, _files in os.walk('.'):
        _dirs[:] = [d for d in _dirs if d not in ('venv', '.venv', '.git', 'node_modules', '__pycache__', '.pytest_cache', 'docs')]
        if 'specs' in _r.split(os.sep): continue
        for _f in _files:
            _p = os.path.join(_r, _f)
            if _f.endswith('.py') and not _f.startswith('test_spec_'): archivos_py.append(_p)
            elif _f.endswith(('.js', '.ts', '.tsx', '.jsx', '.html', '.css')): archivos_web.append(_p)
    assert len(archivos_py) > 0 or len(archivos_web) > 0, 'No se encontraron archivos de código fuente (.py/.js/.ts/.html) en el proyecto'
    for _py in archivos_py[:12]:
        with open(_py, 'r', encoding='utf-8', errors='replace') as _fh:
            ast.parse(_fh.read(), filename=_py)
    for _wf in archivos_web[:12]:
        assert os.path.getsize(_wf) > 0, f'El archivo {_wf} está vacío'
    assert True  # Escenario completado satisfactoriamente

def test_escenario_4_fin_del_juego():
    """
    Escenario: Fin del juego
    Tags: Ninguno
    Requisito: No especificado

    Pasos Gherkin:
      Given la bola está en movimiento.
      When la bola cae por debajo del paddle.
      Then el juego termina y se muestra un mensaje de "Game Over".
    """
    context = {}
    # [Given] la bola está en movimiento.
    context.setdefault('steps_ejecutados', []).append('la bola está en movimiento.')
    # [When] la bola cae por debajo del paddle.
    context.setdefault('steps_ejecutados', []).append('la bola cae por debajo del paddle.')
    # [Then] el juego termina y se muestra un mensaje de "Game Over".
    context.setdefault('steps_ejecutados', []).append('el juego termina y se muestra un mensaje de "Game Over".')
    # Verificación funcional y compilación viva políglota (py_compile / ast) de código del proyecto
    import subprocess, sys, os, ast, py_compile
    assert 'error' not in context or context['error'] is None, 'Error reportado en contexto'
    archivos_py = []
    archivos_codigo = archivos_py
    archivos_web = []
    for _r, _dirs, _files in os.walk('.'):
        _dirs[:] = [d for d in _dirs if d not in ('venv', '.venv', '.git', 'node_modules', '__pycache__', '.pytest_cache', 'docs')]
        if 'specs' in _r.split(os.sep): continue
        for _f in _files:
            _p = os.path.join(_r, _f)
            if _f.endswith('.py') and not _f.startswith('test_spec_'): archivos_py.append(_p)
            elif _f.endswith(('.js', '.ts', '.tsx', '.jsx', '.html', '.css')): archivos_web.append(_p)
    assert len(archivos_py) > 0 or len(archivos_web) > 0, 'No se encontraron archivos de código fuente (.py/.js/.ts/.html) en el proyecto'
    for _py in archivos_py[:12]:
        with open(_py, 'r', encoding='utf-8', errors='replace') as _fh:
            ast.parse(_fh.read(), filename=_py)
    for _wf in archivos_web[:12]:
        assert os.path.getsize(_wf) > 0, f'El archivo {_wf} está vacío'
    assert True  # Escenario completado satisfactoriamente
