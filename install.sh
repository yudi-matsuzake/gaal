#!/bin/bash

#Você é root?
if [ $UID -ne 0 ]
then
	echo "ERRO de permissão"
	echo "Você não é root? af meu"
	exit
fi

#Caminhos
GAAL_PATH=`pwd -P`
FILE_NAME=gaal.py
WHEREIS_GAAL=/usr/bin/gaal

if [ -e $WHEREIS_GAAL ]
then
	echo -n "O arquivo já existe, deseja sobrescrevê-lo? ([sSyY]|.) "
	read opt
	
	case opt in
		y|Y|S|s)
			;;
		?)
			exit
			;;
	esac
fi

echo \
"
Criando link...
de $GAAL_PATH/$FILE_NAME
para $WHEREIS_GAAL
"

ln -vfs "$GAAL_PATH" "$WHEREIS_GAAL/$FILENAME" 
