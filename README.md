## Uso de IA para geração de cenários de teste

### Função escolhida

`def calcular_media(lista):`

### Prompt utilizado

Crie uma tabela de planejamento de testes para a função abaixo:

calcular_media(lista):
    """Retorna a media de uma lista"""
    if len(lista) == 0:
        raise ValueError("Não pode lista vazia")
    return sum(lista) / len(lista)

A tabela deve conter as colunas:
- ID do teste;
- cenário;
- entrada;
- resultado esperado;
- tipo de cenário;
- observação.

Não gere código ainda.

# Cenários sugeridos pela IA

| ID | Cenário | Entrada | Resultado esperado | Tipo | Observação |
|---|---|---|---|---|---|
| T01 | Média de inteiros | `calcular_media([10, 8, 6])` | `8` | caso normal | caso básico |
| T02 | Média com negativos | `calcular_media([-2, -4, -6])` | `-4` | caso normal | verifica negativos |
| T03 | Média com decimais | `calcular_media([2.5, 7.5, 5.0])` | `5.0` | caso normal | verifica decimais |
| T04 | Lista com um elemento | `calcular_media([10])` | `10` | caso de borda | menor lista possível |
| T05 | Lista vazia | `calcular_media([])` | `ValueError` | caso de erro | lança exceção |

# Análise dos cenários

Aceitei todos os cenários que foi sugerido pela IA porque os resultados que eu estava esperando estavam todos corretos e eles cobriam os principais casos da função.

# Código final dos testes
```
def test_calcular_media_inteiros(self):
    self.assertEqual(calcular_media([10, 8, 6]), 8)
    self.assertEqual(calcular_media([-2, -4, -6]), -4)

def test_calcular_media_decimais(self):
    self.assertEqual(calcular_media([2.5, 7.5, 5.0]), 5.0)

def test_calcular_media_um_numero(self):
    self.assertEqual(calcular_media([10]), 10)

def test_calcular_media_vazia(self):
    with self.assertRaises(ValueError):
        calcular_media([])
```

# Saída do terminal

`python -m unittest test_calculadora.py`

# Link do GitHub
