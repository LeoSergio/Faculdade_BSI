## Trabalho Complementar da Unidade I ##
Trabalho Complementar da Unidade I para compor a média final.
Esse trabalho busca auxiliar o estudo da análise experimental de algoritmos.
Os algoritmos utilizados:
 - Fibonacci
 - BubleSort
 - MergeSort
 - QuickSort

## Requisitos do Ambiente ##
Para executar o experimento é necessário possuir instaldo:
 - python >= 3.9
 - Módulo [MathPlotLib](https://matplotlib.org/stable/install/index.html)

A execução do Algoritmo está centralizada no arquivo [ExecExperimento.py](./ExecExperimento.py)

### Executando no Terminal ###
Para executar o experimento abra um terminal na pasta com o código do projeto e execute: 
```
python ExecExperimento.py
```
### Executando no VSCode ####
Abra a pasta do projeto no VSCode e execute o arquivo ExecExperimento.py

### Exemplo de Execução ###
O Experimento realiza a execução sequencial de várias listas com entradas variando de 0 até n para o algoritmo selecioando. Por exemplo, para executar o Fibonacci-Recursivo:
```
python ExecExperimento.py
[1] -> Fibonacci-Iterativo
[2] -> Fibonacci-Recursivo
[3] -> BubleSort-Iterativo
[4] -> BubleSort-Recursivo
[5] -> BubleSort-Otimizado
[6] -> MergeSort-Iterativo
[7] -> MergeSort-Recursivo
[8] -> QuickSort-Iterativo
[9] -> QuickSort-Recursivo
Escolha qual algoritmo quer executar ou [0] para finalizar: 2
Informe o valor da máximo da entrada n: 2
Executando Fibonacci-Recursivo para entrada: 0
Executando Fibonacci-Recursivo para entrada: 1
Executando Fibonacci-Recursivo para entrada: 2
```

Ao executar o Fibonacci-Recursivo para uma entrada n = 2, o experimento irá executar o algoritmo 3 vezes, a primeira com n=0, a segunda com n=1, a terceira com n=2.
Os tempos de execução para cada entrada são salvos em arquivos texto com extensão .res na pasta resultados.
Esses arquivos serão usados na plotagem do gráfico.  

### Como executar o experimento ###
Inicie o experimento determinando o valor máximo da entrada que seu computador suportará para:
 - Fibonacci-Recursivo teste 10,20,30,40.
 - QuickSort-Recursivo teste 7000,8000,9000,10000
Caso seja retornado algum erro de max recurssion depth, assuma o valor anterior como o máximo.
Se não, execute até os limites de 40 e 10000 

# Experimento Fibonacci #
Execute o Script ExecExperimento.py para a entrada máxima dos algoritmos:
 - Fibonacci-Iterativo
 - Fibonacci-Recursivo.

# Experimento Bubble, Merge e Quick #
Execute o Script ExecExperimento.py para a entrada máxima do QuickSort nos algoritmos:
 - BubbleSort-Iterativo
 - BubbleSort-Recursivo
 - BubbleSort-Otimizado
 - MergeSort-Recursivo
 - MergeSort-Iterativo
 - QuickSort-Iterativo
 - QuickSort-Recursivo

 Teste todas as opções de lista ordenada, lista desordenada, lista não-ordenada

# Plotando no Gráfico #
Execute o Script PlotaGrafico.py no Terminal.
Ele recebe parâmetros [titulo do gráfico] [arquivo01] [arquivo02] ...
A quantidade de arquivos pode variar permitindo gerar gráficos de vários resultados
Exemplo:
 - python3.9 PlotaGrafico.py QuickSort resultados/QuickSort-Recursivo.res resultados/QuickSort-Iterativo.res
```
python3.9 PlotaGrafico.py QuickSort resultados/QuickSort-Recursivo.res resultados/QuickSort-Iterativo.res
```