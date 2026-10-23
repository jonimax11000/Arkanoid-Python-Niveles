# INVESTIGACIÓN DE ARQUITECTURA Y STACK: Arkanoid Python Niveles

Documento pre-generado automáticamente por **Jarvis Génesis 2.0**.
*Fecha de generación: 2026-10-23 14:00:08*

---

## 1. Ecosistema Tecnológico Seleccionado
- **Lenguaje Principal:** `Python`
- **Framework / Motor:** `Pygame`
- **Gestor de Paquetes:** `pip / venv`
- **Test Runner (TDD):** `pytest`

---

## 2. Decisiones Arquitectónicas Clave
1. **Separación de Responsabilidades (Clean Architecture):**
   - Entidades / Modelo de Datos desacoplado de la vista y eventos de entrada.
   - Bucle de actualización desacoplado de la tasa de renderizado si aplica.
2. **Modularidad Estricta:**
   - No crear archivos monolíticos gigantes. Cada módulo tiene un único propósito.
3. **Multi-OS y Rutas:**
   - Prohibido hardcodear rutas absolutas de Windows en código distribuible.
   - Usar rutas relativas o abstracciones multiplataforma (`pathlib` o `path.join`).

---

## 3. Comandos de Desarrollo y Verificación
- **Ejecutar Pruebas (TDD):** `pytest`
- **Entorno de Ejecución:** `python main.py`

---

## 4. Estándares de Seguridad y Calidad
- Auditoría periódica con Strix (`analizar_seguridad`).
- Mantenimiento del AST vivo con Graphify (`graphify extract . --code-only`).
- Generación de mapa interactivo con Archify (`generar_diagrama_arquitectura`).
