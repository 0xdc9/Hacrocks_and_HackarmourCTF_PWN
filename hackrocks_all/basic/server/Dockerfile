FROM debian:10

RUN apt-get update && apt-get install -y qemu-system-x86 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m -s /bin/bash ctf

WORKDIR /home/ctf

COPY ./bzImage /home/ctf/bzImage
COPY ./initramfs.cpio.gz /home/ctf/initramfs.cpio.gz
COPY ./launch.sh /home/ctf/launch.sh
COPY ./ynetd /usr/bin/ynetd

RUN chown root:root /usr/bin/ynetd && chmod 755 /usr/bin/ynetd
RUN chmod 500 /home/ctf/launch.sh && chown -R ctf:ctf /home/ctf

CMD ["/usr/bin/ynetd", "-lt", "28800", "-p", "48453", "-sh", "y", "/home/ctf/launch.sh"]

