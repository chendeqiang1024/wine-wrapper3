#!/bin/bash
ROOTDIR=$(pwd)

if [ ! -d build ];then
	mkdir build
fi

if [ ! -d release ];then
	mkdir release
fi

help(){
	echo "
-h,--help			help
-s,--submodule		init submodule
"
	exit
}

if [ "$1" == "" ];then
	help
fi

while [ "$1" != "" ]
do
	case $1 in
	"-h" | "--help")
		help
		;;
	"-s" | "--submodule")
		cd wine
		git submodule init
		git submodule update
		;;
	*)
		help
		;;
	esac
done
