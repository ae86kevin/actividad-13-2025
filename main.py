class Repartidor:
    def _init_(self,nombre,pkg,zona):
        self.nombre = nombre
        self.pkg = pkg
        self.zona = zona

    def _str_(self):
        return f"{self.nombre} {self.pkg} {self.zona}"




class EmpresaMensajeria:
    def _init_(self):
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
                mayores = [x for x in lista[1:] if x.pkg >= pivot.pkg]
                menores = [x for x in lista[1:] if x.pkg < pivot.pkg]
                return quick_sort(menores) + [pivot] + quick_sort(mayores)
        self.repartidors = quick_sort(self.repartidors)



        def busqueda_secuencial(self, nombre):
                for repartidor in self.repartidors:
                    if repartidor.nombre == nombre:
                        return repartidor
                else:
                    return None




