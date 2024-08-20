#!/bin/bash

value_on=$(python3 /./home/sps/examen/scripts/py/read.py | grep "ON-SH" | cut -d " " -f3 | cut -b 24-28)
value_off=$(python3 /./home/sps/examen/scripts/py/read.py | grep "OFF-SH" | cut -d " " -f3 | cut -b 24-29)


value_on_c=$(python3 /./home/sps/examen/scripts/py/read.py | grep "ON-C" | cut -d " " -f3 | cut -b 24-27)
value_off_c=$(python3 /./home/sps/examen/scripts/py/read.py | grep "OFF-C" | cut -d " " -f3 | cut -b 24-28)


value_on_asm=$(python3 /./home/sps/examen/scripts/py/read.py | grep "ON-ASM" | cut -d " " -f3 | cut -b 24-29)
value_off_asm=$(python3 /./home/sps/examen/scripts/py/read.py | grep "OFF-ASM" | cut -d " " -f3 | cut -b 24-30)

if [ $value_on == "ON-SH" ]
then        
    sudo /home/sps/examen/scripts/sh/on.sh
    echo $value_on
    echo 1 > /home/sps/examen/status/status.txt
    
    else 
        if [ $value_off == "OFF-SH" ] 
        then
            sudo /home/sps/examen/scripts/sh/off.sh
            echo $value_off
            echo 0 > /home/sps/examen/status/status.txt
    fi
fi

if [ $value_on_c == "ON-C" ]
then        
    sudo /home/sps/examen/scripts/c/on
    echo $value_on_c
    echo 1 > /home/sps/examen/status/status.txt
    
    else 
        if [ $value_off_c == "OFF-C" ] 
        then
            sudo /home/sps/examen/scripts/c/off
            echo $value_off_c
            echo 0 > /home/sps/examen/status/status.txt
    fi
fi


if [ $value_on_asm == "ON-ASM" ]
then        
    sudo /home/sps/examen/scripts/asm/uthonremoto
    echo $value_on_asm
    echo 1 > /home/sps/examen/status/status.txt
    
    else 
        if [ $value_off_asm == "OFF-ASM" ] 
        then
            sudo /home/sps/examen/scripts/asm/uthoffremoto
            echo $value_off_asm
            echo 0 > /home/sps/examen/status/status.txt
    fi
fi