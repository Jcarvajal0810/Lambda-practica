from Ventas import Ventas
import csv
from collections import defaultdict

class VentasMain:
    def __init__(self, file_path):
        self.file_path = file_path

    def procesar_ventas(self):
        ventas_dict = {
            "total_ventas": 0,
            "total_autos_clasicos": 0,
            "total_ventas_autos_clasicos": 0,
            "total_motocicletas": 0,
            "total_ventas_motocicletas": 0,
            "ventas_por_cliente_ny": defaultdict(lambda: {"autos": 0, "total": 0}),
            "cliente_mas_autos_ny": "",
            "ventas_por_cliente": defaultdict(lambda: {"autos": 0, "total": 0}),
            "cliente_mas_compras": "",
            "cliente_menos_compras": ""
        }

        ventas_list = []

        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                venta = Ventas(
                    row['ORDERNUMBER'],
                    row['QUANTITYORDERED'],
                    row['PRICEEACH'],
                    row['ORDERLINENUMBER'],
                    row['SALES'],
                    row['ORDERDATE'],
                    row['STATUS'],
                    row['QTR_ID'],
                    row['MONTH_ID'],
                    row['YEAR_ID'],
                    row['PRODUCTLINE'],
                    row['MSRP'],
                    row['PRODUCTCODE'],
                    row['CUSTOMERNAME'],
                    row['PHONE'],
                    row['ADDRESSLINE1'],
                    row['ADDRESSLINE2'],
                    row['CITY'],
                    row['STATE'],
                    row['POSTALCODE'],
                    row['COUNTRY'],
                    row['TERRITORY'],
                    row['CONTACTLASTNAME'],
                    row['CONTACTFIRSTNAME'],
                    row['DEALSIZE']
                )

                venta.actualizar_ventas_dict(ventas_dict)
                ventas_list.append(venta)

        return ventas_dict, ventas_list

    def imprimir_total_ventas(self):
        ventas_dict, _ = self.procesar_ventas()
        print(f"El total de ventas es de ${ventas_dict['total_ventas']}")

    def imprimir_ventas_autos_clasicos(self):
        ventas_dict, _ = self.procesar_ventas()
        print(f"Se vendieron {ventas_dict['total_autos_clasicos']} autos clásicos en total")

    def imprimir_ventas_autos_clasicos_ny(self):
        ventas_dict, _ = self.procesar_ventas()
        print(f"El total de ventas de autos clásicos en NY es de ${ventas_dict['total_ventas_autos_clasicos']}")

    def imprimir_ventas_motocicletas(self):
        ventas_dict, _ = self.procesar_ventas()
        print(f"Se vendieron {ventas_dict['total_motocicletas']} motocicletas en total")

    def imprimir_ventas_motocicletas_ny(self):
        ventas_dict, _ = self.procesar_ventas()
        print(f"El total de ventas de motocicletas en NY es de ${ventas_dict['total_ventas_motocicletas']}")

    def imprimir_cliente_mas_autos_ny(self):
        ventas_dict, _ = self.procesar_ventas()

        if ventas_dict["ventas_por_cliente_ny"]:
            cliente_mas_autos_ny = max(
                ventas_dict["ventas_por_cliente_ny"],
                key=lambda k: ventas_dict["ventas_por_cliente_ny"][k]["autos"]
            )

            print(f"El cliente de NY que más autos compró es {cliente_mas_autos_ny}")

    def imprimir_cliente_mas_compras(self):
        ventas_dict, _ = self.procesar_ventas()

        if ventas_dict["ventas_por_cliente"]:
            cliente_mas_compras = max(
                ventas_dict["ventas_por_cliente"],
                key=lambda k: ventas_dict["ventas_por_cliente"][k]["total"]
            )

            print(f"El cliente que más compró es {cliente_mas_compras}")

    def imprimir_cliente_menos_compras(self):
        ventas_dict, _ = self.procesar_ventas()

        if ventas_dict["ventas_por_cliente"]:
            cliente_menos_compras = min(
                ventas_dict["ventas_por_cliente"],
                key=lambda k: ventas_dict["ventas_por_cliente"][k]["total"]
            )

            print(f"El cliente que menos compró es {cliente_menos_compras}")

vm = VentasMain("sales_data.csv")

while True:
    print("Menu:")
    print("1. ¿Cuánto fue el total de ventas de New York?")
    print("2. ¿Cuántos autos clásicos vendió New York?")
    print("3. ¿Cuánto fue el total de ventas de Autos Clásicos en New York?")
    print("4. ¿Cuántas Motocicletas vendió New York?")
    print("5. ¿Cuánto fue el total de ventas de Motocicletas en New York?")
    print("6. ¿Cuál fue el cliente de New York qué más autos compró?")
    print("7. ¿Cuál fue el cliente de todo el archivo qué más compró?")
    print("8. ¿Cuál fue el cliente de todo el archivo qué menos compró?")
    print("9. Salir del programa")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        vm.imprimir_total_ventas()
    elif opcion == 2:
        vm.imprimir_ventas_autos_clasicos()
    elif opcion == 3:
        vm.imprimir_ventas_autos_clasicos_ny()
    elif opcion == 4:
        vm.imprimir_ventas_motocicletas()
    elif opcion == 5:
        vm.imprimir_ventas_motocicletas_ny()
    elif opcion == 6:
        vm.imprimir_cliente_mas_autos_ny()
    elif opcion == 7:
        vm.imprimir_cliente_mas_compras()
    elif opcion == 8:
        vm.imprimir_cliente_menos_compras()
    elif opcion == 9:
        break
    else:
        print("Opción inválida, selecciona una opción del menú")
