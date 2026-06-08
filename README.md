# teste-unitario-python

Este repositório tem a resolução da atividade prática do Teste Unitário do campus virtual.

# Metodos implementados

# Tabela de planejamento

| ID | Cenário | Entrada | Resultado esperado | Tipo | Observação |
|---|---|---|---|---|---|
| T01 | Divisão exata | `dividir(10, 2)` | `5` | caso normal | caso básico |
| T02 | Divisão exata 2 | `dividir(9, 3)` | `3` | caso normal | outro caso básico |
| T03 | Divisão com decimal | `dividir(5, 2)` | `2.5` | caso normal | resultado não inteiro |
| T04 | Divisão com negativo | `dividir(-10, 2)` | `-5` | caso normal | verifica sinal negativo |
| T05 | Zero dividido por número | `dividir(0, 5)` | `0` | caso de borda | zero no numerador |
| T06 | Divisão por zero | `dividir(10, 0)` | `ZeroDivisionError` | caso de erro | lança exceção |