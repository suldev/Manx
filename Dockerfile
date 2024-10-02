FROM archlinux:latest

WORKDIR /manx

RUN pacman -Sy --noconfirm --noprogressbar -q dnsmasq python python-requests

COPY src/*.py /usr/share/manx

ENTRYPOINT ["/usr/bin/python", "/usr/share/manx/main.py", "-v", "-o", "/manx/blacklist.txt", "-w", "/manx/whitelist.txt", "/manx/blocklist.txt"]