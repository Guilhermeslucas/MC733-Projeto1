# GNU Gzip
## O que faz? Para que serve?
Serve para (des)comprimir arquivos em geral, conservando as permissões dos arquivos. Considerado o melhor algoritmo para compressão em geral e utilizado como padrão na internet.
## Por que é bom para medir desempenho?
É um programa que, dependendo da entrada, precisa utilizar de forma extremamente eficaz o processador, disco e memória.
## Onde baixar
 http://ftp.gnu.org/gnu/gzip/ (via HTTP)

 ftp://ftp.gnu.org/gnu/gzip/ (via FTP)

## Como compilar/instalar
A maioria das distribuições GNU/Linux já vem com o gzip instalado por padrão. Para verificar se ele já esta instalado, basta digitar:
```
gzip --version
```
Caso algo seja retornado, isso significa que este já está instalado e você pode pular essa parte. Caso contrário, siga os comandos abaixo, seguindo a distribuição que esta usando:

**Sistemas baseados em Debian (Ubuntu, Mint) ou que usam Apt-get:**
```
sudo apt-get install gzip gunzip
```

**Sistemas baseados em RedHat(Fedora, CentOS) ou que usam Yum:**
```
sudo yum -y install gzip gunzip
```

**OSX (Mac)**
```
brew install gzip
```

## Como executar
Instruções para execução. Se seu programa precisa de entradas, você deve fornece-las para que todos executem corretamente.
## Como medir o desempenho
Como que o desempenho é medido através deste programa? Se for através de tempo, você deve especificar claramente qual tempo deverá ser utilizado e indicar o motivo aqui. Quantas vezes a medida deverá ser feita? O que fazer com ela (média, etc) ? Não especificar o tempo será considerado falha grave.
## Como apresentar o desempenho
Como o desempenho deverá ser mostrado. Margem de erro, etc.
## Medições base (uma máquina)
Inclua a especificação dos componentes relevantes e os resultados de desempenho.
