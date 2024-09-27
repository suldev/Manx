#!/bin/bash

STATUS_NOT_ROOT=1

if [[ $EUID > 0 ]]; then
    echo Must be root
    exit $STATUS_NOT_ROOT
fi

MANXLIB=/usr/lib/manx/
MANXBIN=/usr/bin/
MANXCFG=/etc/manx/
SYSTEMD=/etc/systemd/

mkdir $MANXLIB $MANXCFG
cp src/* $MANXLIB
cp bin/* $MANXBIN
cp blacklist.txt $MANXCFG
cp whitelist.txt $MANXCFG
cp systemd/* $SYSTEMD

systemctl --reload-daemon
systemctl enable manx.timer
systemctl start manx.timer

exit 0