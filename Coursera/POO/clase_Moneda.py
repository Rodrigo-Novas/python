class currency(object):
    def __init__(self, moneda, simbolo, factor):
        self.moneda=moneda
        self.simbolo= simbolo
        self.factor = factor #la diferencia de valor
    
    def __repr__(self):
        return self.moneda, simbolo
    
    def convert_amount_to_base(self, numero):
        return numero / self.factor
    
    def convert_base_to_amount(self, numero):
        return numero * self.factor

class moneda(object):
    
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __repr__(self): #es lo que te muestra si lo imprimis
        return f"{self.amount} {self.currency}"
    
    
    
if __name__ == "__main__":
    peso=currency("peso", "$")
    dolar=currency("dolar", "u$d")
    moneda1=(1,peso)
    moneda2=(2,dolar)