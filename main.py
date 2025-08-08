class Repartidor:
    def __init__(self,nombre,pkg,zona):
        self.nombre = nombre
        self.pkg = pkg
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} {self.pkg} {self.zona}"




class EmpresaMensajeria:
    def __init__(self):
        self.repartidors = []

    def agregar(self,repartidor):
        if any(a.nombre == repartidor.nombre for a in self.repartidors):
            print("ya existe")
            return
        self.repartidors.append(repartidor)

    def ordenar(self):
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista

            else:
                pivot = lista[0]
                mayores=[x for x in lista[1:] if x.pkg >= pivot.pkg]
                menores=[x for x in lista[1:] if x.pkg <pivot.pkg]
                return quick_sort(menores) + [pivot] + quick_sort(mayores)
        self.repartidors = quick_sort(self.repartidors)


    def busqueda_secuencial(self,nombre):
            for repartidor in self.repartidors:
                if repartidor.nombre == nombre:
                    return repartidor
            else:
                return None








empresa = EmpresaMensajeria()

cantidad=int(input("Ingrese la cantidad de repartidors: "))
for i in range(cantidad):
    print(f"\nIngrese datos del repartidor {i+1}")
    nombre= input("Ingrese el nombre del repartidor: ")
    pkg= int(input("cantidad de paquetes: "))
    zona= input("Ingrese la zona del repartidor: ")


    repartidor = Repartidor(nombre,pkg,zona)
    empresa.agregar(repartidor)


print("\nDatos Ordenados")
for i in empresa.repartidors:
    print(f"nombre: {i.nombre} paquetes entregados: {i.pkg} zona asignada: {i.zona}")

busqueda=input("\nIngrese la nombre del repartidor: ")
resultado=empresa.busqueda_secuencial(busqueda)

if resultado:
    print(f"Datos del conductor: {resultado.nombre}  paquetes: {resultado.pkg}  zona: {resultado.zona}")

else:
    print("No existe la repartidor")


