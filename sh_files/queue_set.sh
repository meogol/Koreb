#!/bin/bash
# блокировка трафика для спуфера
iptables -I FORWARD -j NFQUEUE --queue-num 0
# создание очереди
echo 1 > /proc/sys/net/ipv4/ip_forward

