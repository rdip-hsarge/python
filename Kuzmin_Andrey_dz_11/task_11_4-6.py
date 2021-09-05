class OfficeEcuipment:
    quantity = 0


class Printer(OfficeEcuipment):
    name = 'Printer'


class Scanner(OfficeEcuipment):
    name = 'Scanner'


class Copier(OfficeEcuipment):
    name = 'Copier'


class WareHouse:
    inventory = {Printer.name: Printer.quantity,
                 Scanner.name: Scanner.quantity,
                 Copier.name: Copier.quantity}

    def arrive(self, equip, value):
        WareHouse.inventory[equip] += value
        return WareHouse.inventory[equip]

    def transfer(self, equip, value):
        if WareHouse.inventory[equip] >= value:
            WareHouse.inventory[equip] -= value
            return WareHouse.inventory[equip]
        else:
            raise ValueError(f'На складе нет столько {equip}')


y = WareHouse()

y.arrive('Printer', 50)
y.arrive('Scanner', 30)
y.arrive('Printer', 22)
y.arrive('Copier', 10)
y.transfer('Printer', 44)
# y.transfer('Copier', 44)

print(y.inventory['Printer'])