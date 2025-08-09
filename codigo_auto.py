import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No se detectó ningún joystick")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Usando: {joystick.get_name()}")

    running = True
    while running:
        deadzone = 0.1  # Ajusta el valor de la zona muerta según sea necesario
        def aplicar_deadzone(valor):
            if abs(valor) < deadzone:
                return 0
            return valor
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Botón {event.button} presionado")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Botón {event.button} liberado")
            elif event.type == pygame.JOYAXISMOTION:
                valor = aplicar_deadzone(event.value)
                if valor != 0:
                    print(f"Eje {event.axis}: {valor}")
