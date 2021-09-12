def pay_total(id, brand, pays):
    dict = {"Placa": id, "Marca": brand, "Pagos": pays}
    return sum(dict["Pagos"])


print(pay_total("TPQ-11F", "HONDA XRE 300 ABS", [100, 200, 800]))
