#!/bin/bash

#setup bash file to load in env parameters and activate

read -p "Create new conda env called bayesvs(y/n)?" CONT

case $CONT in
	n|N) echo "exit";;
	y|Y) 
		conda create --name bayesvs --file "bayesvs.txt" 
		case "${unameOut}" in
			MINGW*)     
					conda activate bayesvs
					;;
			*)      source activate bayesvs
					;;
		esac
		echo "bayesvs environment has been activated"
		;;
esac
