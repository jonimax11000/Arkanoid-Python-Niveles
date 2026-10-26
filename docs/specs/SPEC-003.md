---
id: "SPEC-003"
title: "arkanoid-python-niveles — Sprint 3: Mecánica Básica del Juego"
version: "1.0.0"
status: "APPROVED"
sprint_id: "T1792756894_2"
created_at: "2026-10-26 10:25:22"
updated_at: "2026-10-26 10:26:16"
approved_by: "SDD-Architect"
---
# SPEC-003 — Sprint 3: Mecánica Básica del Juego  

---

## 1. Context  
El proyecto **arkanoid-python-niveles** tiene como objetivo desarrollar una versión del clásico juego *Arkanoid* en Python, utilizando **Pygame** como motor gráfico. Este sprint (T1792756894_2) corresponde a la implementación de la **mecánica básica del juego**, incluyendo los elementos fundamentales como *paddle*, *ball*, *bricks* y un sistema de colisión básico.  

---

## 2. Goal  
Implementar las siguientes funcionalidades:  
- Un **paddle** controlable por el usuario.  
- Una **ball** que se mueva con física básica.  
- **Bricks** que se destruyan al ser golpeados por la bola.  
- Un sistema de **colisión básico** entre la bola, el paddle y los bricks.  
- Aplicar **TDD (Test-Driven Development)** para garantizar la calidad del código.  

---

## 3. Users  
- **Jugadores**: Usuarios finales que interactúan con el juego.  
- **Desarrolladores**: Equipo técnico responsable de la implementación.  
- **QA Engineers**: Equipo de pruebas que validará el cumplimiento de los criterios de aceptación.  

---

## 4. Scope  

### In Scope  
- Implementación de la clase `Paddle` con movimiento horizontal.  
- Implementación de la clase `Ball` con movimiento dinámico y colisión.  
- Implementación de la clase `Brick` con lógica de destrucción.  
- Sistema de colisión básico entre `Ball`, `Paddle` y `Brick`.  
- Pruebas unitarias y de integración usando **pytest** y **Pygame**.  

### Out of Scope  
- Implementación de niveles o mapas.  
- Sistema de puntuación o vidas.  
- Sonidos o animaciones avanzadas.  
- Implementación de power-ups o elementos adicionales.  

---

## 5. Requirements  

### R1: Clase `Paddle`  
- **Descripción**: Representa el controlador del jugador.  
- **Responsabilidades**:  
  - Moverse horizontalmente dentro de los límites de la pantalla.  
  - Detectar colisión con la bola.  
- **Métodos**:  
  - `update()`: Actualiza la posición del paddle según la entrada del usuario.  
  - `draw(screen)`: Dibuja el paddle en la pantalla.  

### R2: Clase `Ball`  
- **Descripción**: Representa la bola del juego.  
- **Responsabilidades**:  
  - Moverse con velocidad constante.  
  - Detectar colisión con el paddle, los bricks y los bordes de la pantalla.  
- **Métodos**:  
  - `update()`: Actualiza la posición de la bola según su velocidad.  
  - `draw(screen)`: Dibuja la bola en la pantalla.  
  - `bounce(direction)`: Cambia la dirección de la bola al colisionar.  

### R3: Clase `Brick`  
- **Descripción**: Representa los bloques que el jugador debe destruir.  
- **Responsabilidades**:  
  - Dibujarse en la pantalla.  
  - Ser destruido al ser golpeado por la bola.  
- **Métodos**:  
  - `draw(screen)`: Dibuja el brick en la pantalla.  
  - `is_destroyed()`: Retorna `True` si el brick está destruido.  

### R4: Sistema de Colisión Básico  
- **Descripción**: Maneja las interacciones entre la bola, el paddle y los bricks.  
- **Responsabilidades**:  
  - Detectar colisión entre la bola y el paddle.  
  - Detectar colisión entre la bola y los bricks.  
  - Actualizar el estado de los objetos afectados (ej: destruir brick).  
- **Métodos**:  
  - `check_collision(ball, paddle)`: Verifica colisión entre bola y paddle.  
  - `check_collision(ball, brick)`: Verifica colisión entre bola y brick.  

### R5: Implementación de TDD  
- **Descripción**: Aplicar TDD para todas las clases y métodos implementados.  
- **Responsabilidades**:  
  - Escribir pruebas unitarias para `Paddle`, `Ball`, `Brick` y el sistema de colisión.  
  - Validar que las pruebas pasen antes de implementar funcionalidad.  
- **Herramientas**:  
  - **pytest** para pruebas unitarias.  
  - **Pygame** para simulaciones de colisión.  

---

## 6. Business Rules  
1. El paddle solo puede moverse dentro de los límites de la pantalla.  
2. La bola rebota al colisionar con el paddle, los bricks o los bordes superior e izquierdo/derecho de la pantalla.  
3. La bola se pierde si cae por debajo del paddle (fin del juego).  
4. Los bricks se destruyen al ser golpeados por la bola.  
5. La velocidad de la bola es constante durante el juego.  

---

## 7. User Flow  
1. El jugador inicia el juego.  
2. El paddle se posiciona en la parte inferior de la pantalla.  
3. La bola se mueve en dirección aleatoria.  
4. El jugador mueve el paddle para golpear la bola.  
5. La bola colisiona con el paddle, rebotando hacia arriba.  
6. La bola colisiona con un brick, destruyéndolo.  
7. Si la bola cae por debajo del paddle, el juego termina.  

---

## 8. Acceptance Criteria  

### Escenario 1: Movimiento del paddle  
**Given** el juego está en ejecución.  
**When** el usuario presiona las teclas izquierda/derecha.  
**Then** el paddle se mueve horizontalmente dentro de los límites de la pantalla.  

### Escenario 2: Colisión entre bola y paddle  
**Given** la bola está en movimiento.  
**When** la bola colisiona con el paddle.  
**Then** la bola rebota hacia arriba.  

### Escenario 3: Colisión entre bola y brick  
**Given** un brick está presente en la pantalla.  
**When** la bola colisiona con el brick.  
**Then** el brick se destruye y desaparece de la pantalla.  

### Escenario 4: Fin del juego  
**Given** la bola está en movimiento.  
**When** la bola cae por debajo del paddle.  
**Then** el juego termina y se muestra un mensaje de "Game Over".  

---

## 9. Edge Cases  
1. La bola choca en la esquina del paddle, causando un rebote inesperado.  
2. La bola golpea múltiples bricks en un solo movimiento.  
3. El paddle está en el borde izquierdo/derecho de la pantalla y el usuario intenta moverlo más allá.  
4. La bola se mueve a una velocidad tan alta que no se detecta la colisión con el paddle.  

---

## 10. Open Questions  
1. ¿Debería el sistema de colisión usar bounding boxes o algoritmos más precisos (ej: pixel-perfect)?  
2. ¿Cuál será el tamaño inicial del paddle y la bola?  
3. ¿La velocidad de la bola será constante o aumentará con el tiempo?  
4. ¿Se permitirá que los bricks tengan diferentes tipos (ej: resistentes, frágiles)?