#!/bin/bash
STATUS_OK=0
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
chmod 755 bin/manx
chmod 744 bin/manx-daemon
cp bin/* $MANXBIN
cp blocklist.txt $MANXCFG
cp whitelist.txt $MANXCFG
cp -r systemd/* $SYSTEMD

systemctl daemon-reload
systemctl enable manx.timer
systemctl start manx.timer

exit $STATUS_OK