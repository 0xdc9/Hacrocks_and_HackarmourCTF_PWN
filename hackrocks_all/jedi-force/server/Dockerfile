FROM debian:11

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash jediforce

WORKDIR /home/jediforce

COPY ./flag.txt .
COPY ./jedi_force .
COPY ./run.sh ./run
COPY ./ld-2.31.so .
COPY ./libc-2.31.so .
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall

RUN chown -R root:jediforce /home/jediforce && chmod -R 550 /home/jediforce
RUN chmod 440 flag.txt && chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

CMD ["/usr/bin/startchall"]
