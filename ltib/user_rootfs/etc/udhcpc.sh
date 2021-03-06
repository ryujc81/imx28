#!/bin/sh
# Sample udhcpc renew script

RESOLV_CONF="/etc/resolv.conf"

[ -n "$broadcast" ] && BROADCAST="broadcast $broadcast"
[ -n "$subnet" ] && NETMASK="netmask $subnet"

/sbin/ifconfig $interface $ip $BROADCAST $NETMASK up

if [ -n "$router" ]
then
    echo "deleting routers"
    while /sbin/route del default gw 0.0.0.0 dev $interface^M
    do :
    done

    metric=0
    for i in $router
        do
        /sbin/route add default gw $i dev $interface metric $((metric++))
        done
fi
    echo -n > $RESOLV_CONF
    [ -n "$domain" ] && echo domain $domain >> $RESOLV_CONF
    for i in $dns
        do
        echo adding dns $i
        echo nameserver $i >> $RESOLV_CONF
        done
