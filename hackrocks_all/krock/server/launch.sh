#!/bin/bash

#
# launch
#
timeout --foreground 28800 qemu-system-x86_64 \
	-m 128M \
	-kernel /home/ctf/bzImage \
	-initrd /home/ctf/initramfs.cpio.gz \
	-nographic \
	-monitor none \
	-no-reboot\
	-append "console=ttyS0 kaslr nosmap nosmep quiet panic=1"
