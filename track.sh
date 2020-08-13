#!/bin/sh
#net 103.2.152.0/22 or net 74.125.0.0/16 or net 172.217.0.0/16
while [ true ]
do
sudo iftop -i wlp1s0 -f "net 103.2.152.0/22 or net 74.125.0.0/16 or net 172.217.0.0/16 or net 2404:c000::/32 or net 2404:6800::/32" -t -s 300 > "/home/udara/Documents/data_track/report/$(date +"%Y-%m-%d %T").txt"
done
