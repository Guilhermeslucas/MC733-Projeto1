#!/bin/bash

#script usado para baixar, descompactar e instalar o gzip. Para rodá-lo, basta usar o comando ./install_script.sh

wget http://ftp.gnu.org/gnu/gzip/gzip-1.8.tar.xz
tar -xvf gzip-1.8.tar.xz
cd gzip-1.8
sudo ./configure && make && make install
python benchmark.py
