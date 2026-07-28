class Transaction:
    def __init__(self, charged_amount, given_amount, currency_units=None):
        # --- Composition: Transaction is composed of amounts + currency units ---
        if currency_units is None:
            currency_units = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
        self.currency_units = currency_units   # uses setter
        self.charged_amount = charged_amount   # uses setter
        self.given_amount = given_amount       # uses setter

    #  Copy constructor
    def __init_copy__(self, other):
        self._currency_units = other._currency_units.copy()
        self._charged_amount = other._charged_amount
        self._given_amount = other._given_amount

    # Properties with Encapsulation + Validation 
    @property
    def currency_units(self):
        return self._currency_units

    @currency_units.setter
    def currency_units(self, units):
        if not units or any(u <= 0 for u in units):
            raise ValueError("Currency units must be positive numbers")
        self._currency_units = sorted(units, reverse=True)

    @property
    def charged_amount(self):
        return self._charged_amount

    @charged_amount.setter
    def charged_amount(self, value):
        if value < 0:
            raise ValueError("Charged amount cannot be negative")
        self._charged_amount = value

    @property
    def given_amount(self):
        return self._given_amount

    @given_amount.setter
    def given_amount(self, value):
        if value < 0:
            raise ValueError("Given amount cannot be negative")
        self._given_amount = value


    def make_change(self):
        change = self._given_amount - self._charged_amount
        if change < 0:
            raise ValueError("Given amount is not enough")

        print(f"Total Change: PKR {change}")
        change_breakdown = {}

        for unit in self._currency_units:
            count = change // unit
            if count > 0:
                change_breakdown[unit] = count
                print(f"{unit} : {count}")
                change -= unit * count
        return change_breakdown







