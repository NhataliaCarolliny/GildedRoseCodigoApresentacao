# Regras de Negócio - Gilded Rose

Bem-vindo à equipe. Sou a Allison, dona da loja Gilded Rose.
Aqui estão as regras de negócio do nosso sistema de inventário:

## Sobre os itens

Todos os itens têm:
- `nome` - identifica o item
- `validade` - número de dias até o vencimento
- `qualidade` - quanto o item vale (0 a 50, exceto exceções)

## Regras gerais

- Ao final de cada dia, o sistema diminui ambos os valores (`validade` e `qualidade`) de cada item.
- A qualidade de um item nunca é negativa.
- A qualidade de um item nunca é maior que 50.
- Após o vencimento (`validade < 0`), a qualidade degrada **duas vezes mais rápido**.

## Exceções

### Aged Brie
- Aumenta sua qualidade quanto mais velho fica.
- Após o vencimento, aumenta o dobro.

### Sulfuras
- Item lendário. Nunca tem que ser vendido.
- Nunca diminui qualidade nem validade.
- Sua qualidade é fixa em **80** (única exceção ao limite de 50).

### Backstage passes
- Aumenta sua qualidade conforme a data do show se aproxima.
- 11 ou mais dias antes: ganha 1 de qualidade por dia.
- 10 a 6 dias antes: ganha 2 de qualidade por dia.
- 5 a 0 dias antes: ganha 3 de qualidade por dia.
- Após o show (validade < 0): qualidade vira 0.

## Nova feature solicitada (escopo do projeto)

Quero adicionar um novo tipo de item: **"Conjurado"**.

- Itens conjurados degradam a qualidade **duas vezes mais rápido** que itens normais.
- Antes do vencimento: perdem 2 de qualidade por dia.
- Após o vencimento: perdem 4 de qualidade por dia.
- Demais regras seguem as gerais (qualidade não fica negativa, etc.).

**IMPORTANTE:** sinta-se à vontade pra refatorar como quiser, **mas a classe `Item` não pode ser modificada nem ter propriedades alteradas**, ela é fornecida pela Goblin (empresa parceira) e é usada por outros sistemas. Se você modificar a classe Item, eles vão ficar bravos comigo.

Boa sorte!

— Allison
