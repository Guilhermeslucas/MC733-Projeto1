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
instalá-lo:

```
./install_script.sh
```

## Como executar
Para podermos realizar o benchmark desse programa vamos comprimir imagens de alta resolução. Para isso, acesse [esse link](http://imagecompression.info/test_images/rgb16bit_linear.zip) e baixe as imagens de demonstração. Após baixá-las, descompacte e vá até o diretório que as imagens foram extraídas. Após isso, rode o seguinte comando:
```
gzip -k -9 big_building.ppm
```
**-k:** Opção usada para manter a imagem original na pasta, além da comprimida.

**-9:** Maior nível de compressão. Usamos essa opção pois é a que demora mais tempo, auxiliando na análise dos dados.

Além disso, estamos usando essa imagem por ser a maior do dataset, o que também ajuda na análise dos dados.


## Como medir o desempenho
Para medir o desempenho, iremos utilizar o comando `perf`. Com ele iremos medir o tempo total de execução do `gzip`, o uso de cpu e o uso de memória. O comando `perf` tem a opção `-r n` que nos permite rodar o comando `n` vezes e ao fim ele nos retorna a média de cada parâmetro e seus respectivos desvios padrão.

## Como apresentar o desempenho
Como o desempenho deverá ser mostrado. Margem de erro, etc.
## Medições base (uma máquina)
OS: Ubuntu 14.04 LTS 64 bits
Processador: Intel Core i7-4500U CPU @ 1.80 GHz x 4
Memória: 8 GB DDR3

|      Parâmetro    | Valor médio  |
| :-----------------| :------------|
| Tempo de CPU (ms) | 11018,401621 |
| Uso de CPU (%)    | 100         |
| Memória (kB)      | Item Two     |

`sudo perf stat -r 10 gzip -f -k -9 ~/big_building.ppm`

A flag `-f` foi utilizada para evitar que o `gzip` perguntasse toda hora se queríamos sobrescrever o arquivo de saída.
