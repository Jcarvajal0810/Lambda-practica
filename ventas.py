import csv
from collections import defaultdict

class Ventas:
    def __init__(self, ordernumber, quantityordered, priceeach, orderlinenumber, sales, orderdate,
                 status, qtr_id, month_id, year_id, productline, msrp, productcode, customername,
                 phone, addressline1, addressline2, city, state, postalcode, country, territory,
                 contactlastname, contactfirstname, dealsize):
        self.ordernumber = ordernumber
        self.quantityordered = quantityordered
        self.priceeach = priceeach
        self.orderlinenumber = orderlinenumber
        self.sales = sales
        self.orderdate = orderdate
        self.status = status
        self.qtr_id = qtr_id
        self.month_id = month_id
        self.year_id = year_id
        self.productline = productline
        self.msrp = msrp
        self.productcode = productcode
        self.customername = customername
        self.phone = phone
        self.addressline1 = addressline1
        self.addressline2 = addressline2
        self.city = city
        self.state = state
        self.postalcode = postalcode
        self.country = country
        self.territory = territory
        self.contactlastname = contactlastname
        self.contactfirstname = contactfirstname
        self.dealsize = dealsize
    
    def __repr__(self):
        return str(self.__dict__)
    
    @property
    def es_auto_clasico(self):
        return self.productline == "Classic Cars"
    
    @property
    def es_motocicleta(self):
        return self.productline == "Motorcycles"
    
    def actualizar_ventas_dict(self, ventas_dict):
        ventas_dict["total_ventas"] += float(self.sales)
        if self.es_auto_clasico:
            ventas_dict["total_autos_clasicos"] += int(self.quantityordered)
            ventas_dict["total_ventas_autos_clasicos"] += float(self.sales)
        if self.es_motocicleta:
            ventas_dict["total_motocicletas"] += int(self.quantityordered)
            ventas_dict["total_ventas_motocicletas"] += float(self.sales)
        if self.city == "New York":
            ventas_dict["ventas_por_cliente_ny"][self.customername]["autos"] += int(self.quantityordered)
            ventas_dict["ventas_por_cliente_ny"][self.customername]["total"] += float(self.sales)
        ventas_dict["ventas_por_cliente"][self.customername]["autos"] += int(self.quantityordered)
        ventas_dict["ventas_por_cliente"][self.customername]["total"] += float(self.sales)

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
    "cliente_menos_compras": "",
}

ventas_list = []
with open('sales_data.csv') as csvfile:
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
# Buscar al cliente de New York que más autos compró
if ventas_dict["ventas_por_cliente_ny"]:
    cliente_mas_autos_ny = max(ventas_dict["ventas_por_cliente_ny"], key=lambda k: ventas_dict["ventas_por_cliente_ny"][k]["autos"])
    ventas_dict["cliente_mas_autos_ny"] = cliente_mas_autos_ny

# Buscar al cliente que más y menos compró en el archivo completo
if ventas_dict["ventas_por_cliente"]:
    cliente_mas_compras = max(ventas_dict["ventas_por_cliente"], key=lambda k: ventas_dict["ventas_por_cliente"][k]["total"])
    cliente_menos_compras = min(ventas_dict["ventas_por_cliente"], key=lambda k: ventas_dict["ventas_por_cliente"][k]["total"])
    ventas_dict["cliente_mas_compras"] = cliente_mas_compras
    ventas_dict["cliente_menos_compras"] = cliente_menos_compras
