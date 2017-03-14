#!/bin/bash

wget http://ftp.gnu.org/gnu/gzip/gzip-1.8.tar.xz
tar -xvf gzip-1.8.tar.xz
cd gzip-1.8
sudo ./configure && make && make install
