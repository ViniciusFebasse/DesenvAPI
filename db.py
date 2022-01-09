import sqlite3

class BancoDeDados:
    def __init__(self):
        self.banco = sqlite3.connect("banco.db")
        self.cursor = self.banco.cursor()
        self.query_registros = """SELECT * FROM usuarios"""

    def registros(self):
        self.cursor.execute(self.query_registros)
        return self.cursor.fetchall()

    def especifico(self, especifico):
        self.cursor.execute(f"""SELECT * FROM usuarios WHERE nome = '{especifico}'""")
        return self.cursor.fetchall()

    def inserir(self, nome):
        self.cursor.execute(f"""INSERT INTO usuarios (nome) VALUES('{nome}')""")
        self.banco.commit()

    def alterar(self, id, nome_novo):
        self.cursor.execute(f"""UPDATE usuarios SET nome = '{nome_novo}' WHERE id = '{id}'""")
        self.banco.commit()

if __name__ == "__main__":
    banco = BancoDeDados()
    # print(banco.especifico("Vinícius"))
    # banco.inserir("Thábita")
    banco.alterar(2, "ViniciusFebasse2")
    print(banco.registros())
