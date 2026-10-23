---
id: "SPEC-001"
title: "Arkanoid Python Niveles - Sprint 1: Setup de Entorno y Estructura Base"
version: "1.0.0"
status: "APPROVED"
sprint_id: "sprint_01"
created_at: "2026-10-23 21:40:00"
updated_at: "2026-10-23 21:40:00"
approved_by: "SDD-Architect"
---
# SPEC-001 — Arkanoid Python Niveles: Setup de Entorno y Estructura Base

## 1. Context
Inicio del desarrollo del videojuego 'Arkanoid Python Niveles' con generación procedural, vidas, puntuación, power-ups y HUD retro neón. Este Sprint 1 establece la estructura base del repositorio, dependencias y punto de entrada modular.

## 2. Goal
Configurar el entorno de ejecución, dependencias (`requirements.txt` con `pygame`, `numpy`, `pytest`), módulos base en `src/` (`config.py`, `main.py`) y una suite de pruebas unitarias verificables en `tests/` (`test_basic.py`) que valide la inicialización limpia.

## 3. Users
Desarrolladores y jugadores del proyecto Arkanoid.

## 4. Scope
### In scope
- Archivo de dependencias `requirements.txt` con `pygame>=2.5.0`, `numpy>=1.24.0`, `pytest>=7.0.0`.
- Módulo `src/__init__.py` y `src/config.py` con constantes de resolución (800x600), colores retro neón (NEON_CYAN, NEON_PINK, etc.) y FPS (60).
- Punto de entrada `src/main.py` con la función `init_game()` y bucle de juego seguro compatible con modo headless.
- Suite de tests `tests/__init__.py` y `tests/test_basic.py` que verifique la configuración y la inicialización de Pygame con código de salida 0.

### Out of scope
- Lógica de paddle, pelotas y colisiones complejas (reservado para Sprint 2 y 3).
- Generación de niveles procedurales y power-ups (Sprints 4 y 5).

## 5. Requirements
### R1: Dependencias y Configuración del Proyecto
- Definir `requirements.txt` con `pygame>=2.5.0`, `numpy>=1.24.0` y `pytest>=7.0.0`.
- Implementar `src/config.py` con `SCREEN_WIDTH = 800`, `SCREEN_HEIGHT = 600`, `FPS = 60`, y la paleta de colores RGB `COLOR_BG = (10, 10, 25)`, `COLOR_NEON_CYAN = (0, 255, 240)`, `COLOR_NEON_PINK = (255, 0, 128)`.

### R2: Módulo Principal y Punto de Entrada
- Implementar `src/main.py` conteniendo la función `init_game() -> dict` que inicializa pygame de forma segura (respetando variables de entorno como `SDL_VIDEODRIVER`), configura la resolución y retorna el estado inicial `{"status": "initialized", "screen_size": (800, 600)}`.

### R3: Suite de Pruebas Unitarias Verificables
- Implementar `tests/test_basic.py` conteniendo pruebas unitarias que validen:
  1. Que las constantes de `src/config.py` tengan tipos y valores correctos.
  2. Que `init_game()` de `src/main.py` inicialice sin excepciones y retorne `status == "initialized"`.

## 6. Business Rules
- La pantalla debe ser determinista (800x600, 60 FPS).
- La inicialización de Pygame debe ejecutarse limpiamente tanto con pantalla física como en modo headless (`SDL_VIDEODRIVER=dummy`).

## 7. User Flow
1. El usuario o sistema ejecuta `python src/main.py` o corre `pytest tests/`.
2. Pygame y la configuración cargan sin excepciones.

## 8. Acceptance Criteria
### Scenario 1: Inicialización correcta del entorno y componentes
Given el proyecto ha sido configurado en `L:/arkanoid-python-niveles`
When se ejecutan los tests unitarios o el punto de entrada
Then el sistema inicializa sin excepciones y con código de salida 0

### Scenario 2: Ejecución de lógica de dominio y verificación de límites
Given los componentes principales están instanciados
When se procesa una interacción válida del usuario o entrada de datos
Then el estado interno se actualiza correctamente respetando las reglas de negocio

## 9. Edge Cases
- Ejecución en entornos CI/CD sin pantalla gráfica (garantizado con `SDL_VIDEODRIVER=dummy`).

## 10. Open Questions
- Todas las dudas resueltas. Spec formalmente aprobada para desarrollo SDD.
