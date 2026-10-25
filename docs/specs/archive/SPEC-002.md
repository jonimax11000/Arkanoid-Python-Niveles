---
id: "SPEC-002"
title: "SPEC-002 — Sprint 2: Implementación del Core del Juego"
version: "1.0.0"
status: "ARCHIVED"
sprint_id: "T1792756893_1"
created_at: "2026-10-25 22:34:19"
updated_at: "2026-10-25 22:45:11"
approved_by: "SDD-Architect"
archived_at: "2026-10-25 22:45:11"
---
# SPEC-002 — Sprint 2: Implementación del Core del Juego

## 1. Context  
Este sprint se enfoca en la implementación del **módulo principal del juego**, que incluye la inicialización del juego, el bucle principal de ejecución y el sistema de puntuación. Este módulo forma la base funcional del juego, permitiendo su ejecución básica y la interacción con elementos del juego (como puntuación, colisiones, etc.). Se aplicará **TDD (Testing-Driven Development)** con **pytest** para garantizar la calidad del código.

---

## 2. Goal  
Implementar el **core del juego** con las siguientes funcionalidades:  
- Inicialización del estado del juego (configuración inicial de objetos, puntuación, etc.).  
- Bucle principal de ejecución del juego (actualización de estado, renderizado, manejo de eventos).  
- Sistema de puntuación que se actualice dinámicamente según las acciones del jugador.  
- Validación de funcionalidades mediante pruebas unitarias con **pytest**.  

---

## 3. Users  
- **Desarrolladores**: Implementar y mantener el core del juego.  
- **Equipo de QA**: Validar que el core funcione según los requisitos y que las pruebas cubran escenarios clave.  
- **Jugadores (futuros usuarios)**: Interactuar con el core del juego (aunque no se implementen funcionalidades visuales en este sprint).  

---

## 4. Scope  
### In scope  
- Clase `Game` con métodos para inicialización, bucle principal y gestión de puntuación.  
- Bucle principal que maneje eventos (ej: teclado, colisiones) y actualice el estado del juego.  
- Sistema de puntuación con métodos para incrementar, restablecer y obtener el valor actual.  
- Pruebas unitarias con **pytest** para validar el comportamiento de `Game` y sus componentes.  

### Out of scope  
- Interfaz gráfica (UI) o renderizado visual (ej: con **pygame** o **PyQt**).  
- Sonido, animaciones o mecánicas avanzadas (ej: vidas, niveles).  
- Implementación de objetos del juego (ej: `Paddle`, `Ball`, `Brick`) fuera del core.  
- Multiplayer o funcionalidades de red.  

---

## 5. Requirements  
### R1: Clase `Game`  
- **Descripción**: Clase principal que encapsula la lógica del juego.  
- **Responsabilidades**:  
  - Inicializar el estado del juego (ej: puntuación inicial, objetos del juego).  
  - Ejecutar el bucle principal del juego.  
  - Manejar eventos del juego (ej: colisiones, entrada del usuario).  
  - Actualizar y gestionar la puntuación.  

### R2: Bucle Principal del Juego  
- **Descripción**: Ciclo de ejecución que mantiene el juego activo hasta que se cumplan condiciones de finalización.  
- **Responsabilidades**:  
  - Procesar eventos (ej: teclado, colisiones).  
  - Actualizar el estado del juego (ej: posición de objetos, puntuación).  
  - Verificar condiciones de finalización (ej: puntuación máxima, pérdida de vidas).  

### R3: Sistema de Puntuación  
- **Descripción**: Mecanismo para registrar y actualizar la puntuación del jugador.  
- **Responsabilidades**:  
  - Incrementar la puntuación según acciones del jugador (ej: destruir bloques).  
  - Restablecer la puntuación al reiniciar el juego.  
  - Proporcionar acceso a la puntuación actual.  

### R4: Pruebas con pytest  
- **Descripción**: Validación del comportamiento del core del juego mediante pruebas unitarias.  
- **Responsabilidades**:  
  - Cubrir escenarios clave de `Game` (ej: inicialización, bucle, puntuación).  
  - Verificar que el bucle principal maneje eventos correctamente.  
  - Validar que el sistema de puntuación funcione según los requisitos.  

### R5: Manejo de Errores  
- **Descripción**: Implementar validaciones para evitar estados inválidos del juego.  
- **Responsabilidades**:  
  - Validar que la puntuación no sea negativa.  
  - Manejar excepciones en el bucle principal (ej: interrupciones inesperadas).  

---

## 6. Business Rules  
- La puntuación inicial del juego debe ser **0**.  
- El bucle principal del juego debe ejecutarse hasta que se cumplan condiciones de finalización (ej: puntuación máxima, pérdida de vidas).  
- La puntuación no puede ser negativa.  
- El sistema de puntuación debe actualizarse en tiempo real durante el juego.  

---

## 7. User Flow  
1. El usuario inicia el juego.  
2. El sistema inicializa el estado del juego (ej: puntuación = 0).  
3. El bucle principal del juego comienza:  
   a. Procesa eventos (ej: entrada del usuario, colisiones).  
   b. Actualiza el estado del juego (ej: posición de objetos, puntuación).  
   c. Verifica condiciones de finalización.  
4. Si el juego termina, se muestra la puntuación final.  

---

## 8. Acceptance Criteria  
### Escenario 1: Inicialización del juego  
**Given** el juego está en estado inicial.  
**When** se llama al método `initialize()` de `Game`.  
**Then** la puntuación debe ser **0** y el estado del juego debe estar listo para ejecutarse.  

### Escenario 2: Ejecución del bucle principal  
**Given** el juego está inicializado.  
**When** se llama al método `run()` de `Game`.  
**Then** el bucle principal debe ejecutarse hasta que se cumplan condiciones de finalización.  

### Escenario 3: Actualización de puntuación  
**Given** el juego está en ejecución.  
**When** el jugador destruye un bloque.  
**Then** la puntuación debe incrementarse en **10 puntos**.  

### Escenario 4: Manejo de errores en el bucle  
**Given** el juego está en ejecución.  
**When** ocurre una excepción inesperada en el bucle principal.  
**Then** el juego debe finalizar y mostrar un mensaje de error.  

---

## 9. Edge Cases  
- **Bucle principal interrumpido**: ¿Qué sucede si el bucle principal es interrumpido por una excepción no manejada?  
- **Puntuación máxima**: ¿Cómo se maneja si el jugador alcanza la puntuación máxima permitida?  
- **Entrada inválida**: ¿Qué pasa si se intenta actualizar la puntuación con un valor negativo?  

---

## 10. Open Questions  
1. ¿Debería el bucle principal del juego ejecutarse a una frecuencia específica (ej: 60 FPS)?  
2. ¿Qué valor se asignará a la puntuación por cada acción del jugador (ej: destruir un bloque)?  
3. ¿Cómo se manejarán las excepciones en el bucle principal (ej: interrupciones de teclado, errores de renderizado)?