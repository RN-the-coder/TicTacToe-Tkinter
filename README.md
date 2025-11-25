
Este proyecto es una implementación completa del clásico Tic Tac Toe (Tres en Raya) desarrollada en Python utilizando Tkinter como framework para la interfaz gráfica. El objetivo principal es ofrecer una experiencia fluida y visualmente agradable para dos jugadores locales, integrando una arquitectura simple, clara y fácilmente extensible.

La aplicación está construida sobre una matriz de botones que representa el tablero de 3x3. Cada interacción del usuario actualiza simultáneamente la interfaz y el estado interno del juego, garantizando coherencia entre la lógica y la representación visual. El sistema incorpora los siguientes componentes clave:

✅ Funcionalidades principales

Control de turnos automático entre los jugadores X y O.

Validación de jugadas, evitando movimientos inválidos o repetidos.

Detección automática de victoria, evaluando filas, columnas y diagonales.

Resaltado visual de la línea ganadora mediante cambios dinámicos de color.

Sistema de empate, notificando cuando el tablero se llena sin ganador.

Botón Reset, que restablece el juego sin cerrar la aplicación.

Centrado automático de la ventana, adaptándose a la resolución del usuario.

Diseño estético personalizado, con una paleta basada en tonos tierra, fuente Consolas y tipografía consistente.

🛠️ Arquitectura y diseño

El programa utiliza un enfoque basado en funciones para gestionar acciones específicas del juego, como la actualización del turno, el control del estado del tablero y la verificación de condiciones de victoria. Esto permite mantener un código claro, fácilmente entendible y modulable para futuras ampliaciones (por ejemplo, agregar modo IA o puntajes).

La interfaz gráfica utiliza el sistema de grid de Tkinter para organizar el tablero y los elementos de información dentro de un Frame, lo que permite mantener un layout limpio y escalable.

🎓 Créditos

Aunque el proyecto incluye decisiones de diseño, estructura visual y mejoras propias, parte del razonamiento sobre la lógica del tablero y el manejo del flujo del juego estuvo inspirado en el contenido educativo del creador Kenny Yip Coding, a quien se reconoce por su aporte a la base técnica de este desarrollo.
