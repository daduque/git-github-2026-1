class Olympics:
    
    def __init__(self):
        
      self.events = []

    def create_event(self):
        event = " ".join(input("Ingrese el nombre del evento: ").strip().lower().title().split())
        
        if event:
            if len(self.events) == 0:
                self.events.append(event)
                print(f"El evento '{event}' se ha creado exitosamente.")
                return
        
        #Que no empiece con un número
        words = event.split()
        if not(words[0].isalpha()):
            print("El nombre del evento no puede comenzar con un número.")
            return
        
        if event[0].isdigit():
            print("El nombre del evento no puede comenzar con un número.")
            return
        
        #Verificar si el eento ya existe en la lista de eventos
        if event in self.events:
            print("El evento ya existe.")
            return
        
        
        
        self.events.append(event)
        
        for index, event in  enumerate(self.events, 1):
            print(f"{index}- {event}")

olympics = Olympics()

while True:
    
    print()
    print("*-" * 20)
    print("1. para crear un evento")
    print("2. para registrar un participante")
    print("3. para crear una simulación")
    print("4. para generar un informe")
    print("5. para salir")
    print("*-" * 20)
    print()

    option = input("Por favor seleccione una opción: ")
    
    match option:
        case "1":
            olympics.create_event()
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Gracias por utilizar el sistema de juegos Olímpicos, hasta luego")
            break
        case _:
            print(f"La opción { option } no es válida, por favor intente de nuevo")