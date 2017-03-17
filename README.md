# GNU Gzip
## O que faz? Para que serve?
Serve para (des)comprimir arquivos em geral, conservando as permissões dos arquivos. Considerado o melhor algoritmo para compressão em geral e utilizado como padrão na internet.
## Por que é bom para medir desempenho?
É um programa que, dependendo da entrada, precisa utilizar de forma extremamente eficaz o processador, disco e memória. Além disso, existem opções que tornam possível
fazer uma melhor compressão, o que faz o computador demorar mais tempo para processar todos os dados, levando mais tempo o que torna a análise dos dados melhor e mais
realista.
## Onde baixar
 http://ftp.gnu.org/gnu/gzip/ (via HTTP)

 ftp://ftp.gnu.org/gnu/gzip/ (via FTP)

## Como compilar/instalar
A maioria das distribuições GNU/Linux já vem com o gzip instalado por padrão. Para verificar se ele já esta instalado, basta digitar:
```
gzip --version
```
Caso algo seja retornado, isso significa que este já está instalado e você pode pular essa parte. Caso contrário, use o comando abaixo para
instalá-lo e já executá-lo (não use se você já possuir o Gzip instalado):

```
./execute.sh
```

## Como executar
Para podermos realizar o benchmark desse programa vamos comprimir imagens de alta resolução. Para isso, acesse [esse link](http://imagecompression.info/test_images/rgb16bit_linear.zip) e baixe as imagens de demonstração. Após baixá-las, descompacte e vá até o diretório que as imagens foram extraídas. Após isso, rode o seguinte comando:
```
python benchmark.py
```
**-k:** Opção usada para manter a imagem original na pasta, além da comprimida.

**-9:** Maior nível de compressão. Usamos essa opção pois é a que demora mais tempo, auxiliando na análise dos dados.

Além disso, estamos usando essa imagem por ser a maior do dataset, o que também ajuda na análise dos dados.


## Como medir o desempenho
Para medir o desempenho, iremos utilizar o comando `/usr/bin/times -v`. Com ele iremos medir o tempo total de execução do `gzip`, o uso de CPU e o uso de memória. Selecionamos o tempo total de execução, pois o programa tem seu tempo de execução dividido entre espaço de usuário e sistema.

Criamos um script para executar o arquivo acima `n` vezes, calcular a média dos parâmetros e o desvio padrão.

## Como apresentar o desempenho
O resultado de cada um dos 3 parâmetros medidos pelo benchmark será a média de **n** análises feitas por `/usr/bin/times -v`, seguido de seu respectivos desvios padrão.
Além disso, é apresentado uma nota final **N**, calculada a partir da fórmula:

$ N = \dfrac{5*CPU\_TIME + 3*CPU\_USAGE + 2*MEMORY\_USAGE}{10} $

Quanto menor o N, melhor o desempenho do gzip no computador.

## Medições base (uma máquina)
OS: Ubuntu 14.04 LTS 64 bits
Processador: Intel Core i7-4500U CPU @ 1.80 GHz x 4
Memória: 8 GB DDR3

O seguinte comando foi executado 16 vezes: `/usr/bin/time -v gzip -f -k -9 ~/big_building.ppm`

A média dos resultados é apresentada abaixo:

|     Parâmetro    | Valor médio | Desvio padrão |
|:-----------------|:------------|:--------------|
| Tempo de CPU (s) |    10,78    |      0,01     |
| Uso de CPU (%)   |    99,75    |      0,56     |               
| Memória (kB)     |     815     |       3       |
