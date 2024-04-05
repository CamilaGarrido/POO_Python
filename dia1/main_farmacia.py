from medicamento import Medicamento



precio = int(input("Ingrese un precio a validar: "))
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado No es válido")

#instancia clase medicamento
paracetamol = Medicamento()
aspirina = Medicamento()


if paracetamol.descuento == aspirina.descuento and paracetamol.IVA == aspirina.IVA:
    print("Todos los valores son iguales en las instancias")
    print(paracetamol.IVA, aspirina.IVA)
    print(paracetamol.descuento,aspirina.descuento)

#print(aspirina.validar_mayor_a_cero(0))

paracetamol.asigna_precio(1)

print(paracetamol.precio)#1000

print(aspirina.precio)#1000
    
    