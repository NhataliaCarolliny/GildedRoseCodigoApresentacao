import logging
logger = logging.getLogger("gildedRose")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
))

logger.addHandler(handler)

class Item:
    def __init__(self, nome: str, validade: int, qualidade: int):
        self.nome = nome
        self.validade = validade
        self.qualidade = qualidade

    def __repr__(self):
        return f"{self.nome}, {self.validade}, {self.qualidade}"           

class ItemComum:
    def __init__(self, item: Item):
        self.item = item 

    def atualizar_item_comum(self):
        self.item.validade -= 1

        if self.item.validade < 0:
            self.item.qualidade = max(0, self.item.qualidade - 2)
        else:
            self.item.qualidade = max(0, self.item.qualidade - 1)

        if self.item.qualidade > 50:
            self.item.qualidade = 50

class AgedBrie: 
    def __init__(self, item: Item):
        self.item = item
    def agedBrie_excecoes(self):
        self.item.validade -= 1
        if self.item.validade > 0:
            self.item.qualidade = max(0, self.item.qualidade + 1)
        else:
            self.item.qualidade = max(0, self.item.qualidade + 2)
        
        if self.item.qualidade > 50:
            self.item.qualidade = 50

class Sulfuras:
    def __init__(self, item: Item):
        self.item = item  

    def sulfuras_excecoes(self):
        self.item.qualidade = 80

class BackstagePasses:
    def __init__(self, item: Item):
        self.item = item 

    def backstagePasses_excecoes(self):
        self.item.validade -= 1
        if self.item.validade >= 11:
            self.item.qualidade = max(0, self.item.qualidade + 1)
        elif self.item.validade >= 6 and self.item.validade <= 10:
            self.item.qualidade = max(0, self.item.qualidade + 2)
        elif self.item.validade >= 0 and self.item.validade <= 5:
            self.item.qualidade = max(0, self.item.qualidade + 3)
        else:
            self.item.qualidade = 0

        if self.item.qualidade > 50:
            self.item.qualidade = 50

class Conjurado:  
    def __init__(self, item: Item):
        self.item = item

    def conjurado_excesoes(self):
        self.item.validade -= 1
        if self.item.validade > 0:
            self.item.qualidade = max(0, self.item.qualidade - 2)
        else:
            self.item.qualidade = max(0, self.item.qualidade - 4)
        
        if self.item.qualidade > 50:
            self.item.qualidade = 50

class GildedRose:
    def _init_(self, itens: list[Item]):
       self.itens = itens 

    def escolhe_item(self):
        for item in self.itens:
            if self.item.nome == "Aged Brie":
                atualizador = AgedBrie(item)
                atualizador.agedBrie_excecoes()
            elif self.item.nome == "Sulfuras":
                atualizador = Sulfuras(item)
                atualizador.sulfuras_excecoes()
            elif self.item.nome == "Backstage passes":
                atualizador = BackstagePasses(item)
                atualizador.backstagePasses_excecoes()
            elif self.item.nome == "Conjurado":
                atualizador = Conjurado(item)
                atualizador.conjurado_excesoes()
            else:
                atualizador = ItemComum(item)
                atualizador.atualizar_item_comum()

if __name__ == "__main__":
    itens = [
        Item("Espada normal", validade=10, qualidade=20),
        Item("Aged Brie", validade=2, qualidade=0),
        Item("Espada vencida", validade=0, qualidade=7),
        Item("Sulfuras", validade=0, qualidade=80),
        Item("Sulfuras vencido", validade=-1, qualidade=80),
        Item("Backstage passes", validade=15, qualidade=20),
        Item("Backstage passes", validade=10, qualidade=49),
        Item("Backstage passes", validade=5, qualidade=49),
        Item("Conjurado", validade=-2, qualidade=5)
    ]
    rose = GildedRose(itens)
    logger.info("Dia 0:")
    for item in rose.itens:
        logger.info(f"{item}")
    rose.escolhe_item()
    logger.info("\nDia 1:")
    for item in rose.itens:
        logger.info(f"{item}")
