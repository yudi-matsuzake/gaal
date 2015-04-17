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

#GAMBIARRA
echo \
"#!/bin/bash
cd \"$GAAL_PATH\"
./gaal.py
cd -
" > "$WHEREIS_GAAL"

if [ $? ]
then
	chmod +x "$WHEREIS_GAAL"
	echo "Instalação concluída"
fi