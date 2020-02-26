#!/usr/bin/bash

time (for i in {1..20}; do IDS=('c5bc1b67-ce78-46eb-9c41-aab100df1e03' '45ae3e3e-f038-4b53-8b58-aab201159c42' '6dc941a4-87fa-4b28-9085-aab2014b7f4a') FIELDS=('password' 'username'); eval "time bw-simple get ${FIELDS[$((RANDOM % ${#FIELDS[@]}+1))]} ${IDS[$((RANDOM % ${#IDS[@]}+1))]} > /dev/null"; done)
