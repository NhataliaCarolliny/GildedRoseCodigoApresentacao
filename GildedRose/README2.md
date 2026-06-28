# Gilded Rose
O projeto é o sistema de uma loja chamada GildedRose que atualiza a validade e a qualidade dos produtos conforme o passar dos dias
## Instalação
```bash
pip install -r requirements.txt
```
## Uso
```python
from gilded_rose import GildedRose, Item

itens = [Item("Aged Brie", validade = 2, qualidade = 0)]
loja = GildedRose(itens)
loja.atualiza_itens()
print(itens[0])
```

## Funcionalidades
- Atualiza a qualidade dos itens diariamente
- Suporta itens especiais (Aged Brie, Sulfuras, Backstage, Conjurado)
- Coberto por teste automatizados

## Como rodar os testes
```bash
pytest -v
```
