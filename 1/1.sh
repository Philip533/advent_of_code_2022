#!/bin/bash
awk -F' ' '{sum+=$1;}{if($1 == ""){sum = 0}{print sum}}' elves.dat | sort -n
awk -F' ' '{sum+=$1;}{if($1 == ""){sum = 0}{print sum}}' elves.dat | sort -n | tail -n 3 | awk '{sum1+=$1}{print sum1}'
