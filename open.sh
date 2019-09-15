#!/bin/bash
 airodump-ng -w MyOutput --output-format csv $1  & PID=$!

sleep 10

kill -TERM $PID
echo 