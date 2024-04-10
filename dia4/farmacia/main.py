from medicamento import Medicamento

nombre = input("Ingrese nombre del medicamento:\n")
stock = int(input("Ingrese stock del medicamento:\n"))
precio_bruto = int(input("Ingrese precio bruto del medicamento:\n"))

paracetamol = Medicamento(nombre, stock)
#llamado al metodo set
paracetamol.precio = precio_bruto

print(f"El precio bruto del medicamento {paracetamol.nombre} es {paracetamol.precio_bruto}")

if paracetamol.descuento:
    print(f"Tiene un descuento de {paracetamol.descuento * 100}%")

print(f"El precio final del medicamento es {paracetamol.precio_final}")