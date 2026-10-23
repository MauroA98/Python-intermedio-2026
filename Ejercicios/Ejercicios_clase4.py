from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    """Clase base abstracta: no se puede instanciar directamente."""

    def __init__(self, titular, cbu, saldo=0):
        self.titular = titular      # atributo público
        self._cbu = cbu             # protegido, solo lectura
        self._saldo = 0             # protegido
        self.saldo = saldo          # pasa por el setter (valida)

    # ---------- Encapsulamiento ----------
    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser menor a cero.")
        self._saldo = valor

    # ---------- Métodos concretos ----------
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self._saldo += monto

    def __str__(self):
        return (f"[{type(self).__name__}] TITULAR: {self.titular} | "
                f"CBU: {self.cbu} | SALDO: ${self.saldo:.2f}")

    # ---------- Método abstracto ----------
    @abstractmethod
    def extraer(self, monto):
        pass


class CuentaAhorro(CuentaBancaria):
    TASA_INTERES = 0.001  # 0.1%

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a 0.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= monto

    def aplicar_interes(self):
        self._saldo += self._saldo * self.TASA_INTERES


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, cbu, saldo=0, limite_descubierto=500):
        super().__init__(titular, cbu, saldo)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a 0.")
        if monto > self._saldo + self.limite_descubierto:
            raise ValueError("Supera el saldo + límite de descubierto.")
        # Se usa _saldo directo porque el setter no permite negativos
        self._saldo -= monto


class CuentaCheque(CuentaBancaria):
    def __init__(self, titular, cbu, saldo=0, costo_emision=50):
        super().__init__(titular, cbu, saldo)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a 0.")
        total = monto + self.costo_emision
        if total > self._saldo:
            raise ValueError("Saldo insuficiente (monto + costo de emisión).")
        self._saldo -= total


# ---------- Prueba de polimorfismo ----------
if __name__ == "__main__":
    cuentas = [
        CuentaAhorro("Ana", "0001", 1000),
        CuentaCorriente("Luis", "0002", 200),
        CuentaCheque("Marta", "0003", 500),
    ]

    for c in cuentas:
        print(c)
        try:
            c.extraer(300)   # misma llamada, comportamiento distinto
            print("  Extracción OK ->", c)
        except ValueError as e:
            print("  Error:", e)

    cuentas[0].aplicar_interes()
    print(cuentas[0])

    try:
        CuentaBancaria("X", "0000")   # abstracta: da TypeError
    except TypeError as e:
        print("TypeError:", e)
