from conta import Conta
from cliente import Cliente

if __name__ == "__main__":
	cliente1 = Cliente('João', 'Silva', '123456789-10')
	cliente2 = Cliente("Rafael", "das Dores", "123456789-11")

	cc1 = Conta('123-4', cliente1, 120.0, 1000.0)
	cc2 = Conta("123-5", cliente2, 0.0)
	cc1.depositar(20.0)
	cc1.saca(50.0)
	cc1.extrato()
	cc1.transfere(cc2, 50.0)
	cc1.historico.imprime()

	cc2.historico.imprime()
