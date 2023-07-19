#!/bin/bash

cat acii.txt
echo -e "\e[1;31m Plz make sure u've installed prerequisities \e[0m"
echo -e "\e[32m Current Directory: \e[0m $(pwd)"
echo -e "\e[32m Current Directory List: \e[1;33m $(ls -m -d */) \e[0m"

#read -p "Enter the DIR of dataset : " dt
echo -ne "\e[32m Enter the DIR of dataset: \e[0m" && read dt
echo -ne "\e[32m Enter desired number of images: \e[0m" && read name

#read -p "${GREEN}Enter desired number of images: ${NC}" name
#read -p "Enter desired number of images : " name
# Execute the Python script and pass the user input as an argument
python augment_img_spec_num.py "$dt" "$name" 



