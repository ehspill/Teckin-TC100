# Teckin-TC100
Device Security: 1/10

+ No Telnet/ssh
+ No ftpd
+ no known default root PW (only md5 tho)


Binwalk:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DECIMAL                            HEXADECIMAL                        DESCRIPTION
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
135128                             0x20FD8                            CRC32 polynomial table, little endian
233472                             0x39000                            uImage firmware image, header size: 64 bytes, data size: 1420384 bytes, compression: none, CPU: ARM, OS: Linux, image type: OS Kernel
                                                                      Image, load address: 0x81B08000, entry point: 0x81B08040, creation time: 2020-08-19 06:47:48, image name: "Linux-3.4.35"
2338816                            0x23B000                           SquashFS file system, little endian, version: 4.0, compression: xz, inode count: 337, block size: 131072, image size: 1204664 bytes,
                                                                      created: 2020-10-26 03:49:12
3911680                            0x3BB000                           JFFS2 filesystem, little endian, nodes: 172, total size: 507916 bytes
4423680                            0x438000                           SquashFS file system, little endian, version: 4.0, compression: xz, inode count: 144, block size: 131072, image size: 3323202 bytes,
                                                                      created: 2020-10-26 03:49:13
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Tree:

0x23B000 - / Root Filesystem - SquashFS (RO)


4.0K]  .
├── [4.0K]  ./bin
│   ├── [2.7K]  ./bin/[
│   ├── [2.7K]  ./bin/[[
│   ├── [2.7K]  ./bin/ash
│   ├── [2.7K]  ./bin/awk
│   ├── [2.7K]  ./bin/base64
│   ├── [2.8K]  ./bin/basename
│   ├── [2.7K]  ./bin/beep
│   ├── [2.7K]  ./bin/bunzip2
│   ├── [669K]  ./bin/busybox
│   ├── [2.7K]  ./bin/bzcat
│   ├── [2.7K]  ./bin/cal
│   ├── [2.7K]  ./bin/cat
│   ├── [2.7K]  ./bin/catv
│   ├── [2.7K]  ./bin/chmod
│   ├── [2.7K]  ./bin/chown
│   ├── [2.7K]  ./bin/chrt
│   ├── [2.7K]  ./bin/chvt
│   ├── [2.7K]  ./bin/cksum
│   ├── [2.7K]  ./bin/clear
│   ├── [2.7K]  ./bin/cmp
│   ├── [2.7K]  ./bin/cp
│   ├── [2.7K]  ./bin/crontab
│   ├── [2.8K]  ./bin/cttyhack
│   ├── [2.7K]  ./bin/cut
│   ├── [2.7K]  ./bin/date
│   ├── [2.7K]  ./bin/dc
│   ├── [2.7K]  ./bin/dd
│   ├── [2.7K]  ./bin/df
│   ├── [2.7K]  ./bin/diff
│   ├── [2.7K]  ./bin/dirname
│   ├── [2.7K]  ./bin/dmesg
│   ├── [2.8K]  ./bin/dnsdomainname
│   ├── [2.8K]  ./bin/dos2unix
│   ├── [2.7K]  ./bin/du
│   ├── [2.8K]  ./bin/dumpkmap
│   ├── [2.8K]  ./bin/dumpleases
│   ├── [2.7K]  ./bin/echo
│   ├── [2.7K]  ./bin/egrep
│   ├── [2.7K]  ./bin/eject
│   ├── [2.7K]  ./bin/env
│   ├── [2.7K]  ./bin/expand
│   ├── [2.7K]  ./bin/expr
│   ├── [2.7K]  ./bin/false
│   ├── [2.7K]  ./bin/fatattr
│   ├── [2.8K]  ./bin/fgconsole
│   ├── [2.7K]  ./bin/fgrep
│   ├── [2.7K]  ./bin/find
│   ├── [2.7K]  ./bin/fold
│   ├── [2.7K]  ./bin/free
│   ├── [2.7K]  ./bin/fsync
│   ├── [2.8K]  ./bin/ftpget
│   ├── [2.8K]  ./bin/ftpput
│   ├── [2.7K]  ./bin/fuser
│   ├── [2.7K]  ./bin/getopt
│   ├── [2.7K]  ./bin/grep
│   ├── [2.7K]  ./bin/groups
│   ├── [2.7K]  ./bin/hd
│   ├── [2.7K]  ./bin/head
│   ├── [2.7K]  ./bin/hexdump
│   ├── [2.7K]  ./bin/hostid
│   ├── [2.8K]  ./bin/hostname
│   ├── [2.7K]  ./bin/id
│   ├── [2.7K]  ./bin/install
│   ├── [2.7K]  ./bin/ionice
│   ├── [2.7K]  ./bin/iostat
│   ├── [2.7K]  ./bin/ipcalc
│   ├── [2.7K]  ./bin/ipcrm
│   ├── [2.7K]  ./bin/ipcs
│   ├── [2.8K]  ./bin/kbd_mode
│   ├── [2.7K]  ./bin/kill
│   ├── [2.7K]  ./bin/killall
│   ├── [2.7K]  ./bin/less
│   ├── [2.7K]  ./bin/linux32
│   ├── [2.7K]  ./bin/linux64
│   ├── [2.7K]  ./bin/ln
│   ├── [2.7K]  ./bin/logger
│   ├── [2.7K]  ./bin/login
│   ├── [2.7K]  ./bin/logname
│   ├── [2.7K]  ./bin/ls
│   ├── [2.7K]  ./bin/lsof
│   ├── [2.7K]  ./bin/lspci
│   ├── [2.7K]  ./bin/lsusb
│   ├── [2.8K]  ./bin/md5sum
│   ├── [2.7K]  ./bin/mesg
│   ├── [2.7K]  ./bin/mkdir
│   ├── [2.7K]  ./bin/mkfifo
│   ├── [2.7K]  ./bin/mknod
│   ├── [2.7K]  ./bin/more
│   ├── [2.7K]  ./bin/mount
│   ├── [2.8K]  ./bin/mountpoint
│   ├── [2.7K]  ./bin/mv
│   ├── [2.7K]  ./bin/nc
│   ├── [2.7K]  ./bin/netstat
│   ├── [2.7K]  ./bin/nice
│   ├── [2.7K]  ./bin/nmeter
│   ├── [2.8K]  ./bin/nslookup
│   ├── [2.7K]  ./bin/od
│   ├── [2.7K]  ./bin/passwd
│   ├── [2.7K]  ./bin/pgrep
│   ├── [2.7K]  ./bin/pidof
│   ├── [2.7K]  ./bin/ping
│   ├── [2.7K]  ./bin/pkill
│   ├── [2.7K]  ./bin/pmap
│   ├── [2.8K]  ./bin/printenv
│   ├── [2.7K]  ./bin/printf
│   ├── [2.7K]  ./bin/ps
│   ├── [2.7K]  ./bin/pscan
│   ├── [2.7K]  ./bin/pstree
│   ├── [2.7K]  ./bin/pwd
│   ├── [2.7K]  ./bin/pwdx
│   ├── [2.8K]  ./bin/readlink
│   ├── [2.8K]  ./bin/realpath
│   ├── [2.7K]  ./bin/renice
│   ├── [2.7K]  ./bin/reset
│   ├── [2.7K]  ./bin/resize
│   ├── [2.7K]  ./bin/rm
│   ├── [2.7K]  ./bin/rmdir
│   ├── [2.7K]  ./bin/rx
│   ├── [2.7K]  ./bin/script
│   ├── [2.8K]  ./bin/scriptreplay
│   ├── [2.7K]  ./bin/sed
│   ├── [2.7K]  ./bin/setarch
│   ├── [2.8K]  ./bin/setkeycodes
│   ├── [2.8K]  ./bin/setserial
│   ├── [2.7K]  ./bin/setsid
│   ├── [2.7K]  ./bin/sh
│   ├── [2.8K]  ./bin/sha1sum
│   ├── [2.8K]  ./bin/sha256sum
│   ├── [2.8K]  ./bin/sha3sum
│   ├── [2.8K]  ./bin/sha512sum
│   ├── [2.7K]  ./bin/showkey
│   ├── [2.7K]  ./bin/shuf
│   ├── [2.7K]  ./bin/sleep
│   ├── [2.7K]  ./bin/smemcap
│   ├── [2.7K]  ./bin/sort
│   ├── [2.7K]  ./bin/split
│   ├── [2.7K]  ./bin/stat
│   ├── [2.7K]  ./bin/strings
│   ├── [2.7K]  ./bin/stty
│   ├── [2.7K]  ./bin/sum
│   ├── [2.7K]  ./bin/sync
│   ├── [2.7K]  ./bin/tail
│   ├── [2.7K]  ./bin/tar
│   ├── [2.8K]  ./bin/tcpsvd
│   ├── [2.7K]  ./bin/tee
│   ├── [2.7K]  ./bin/telnet
│   ├── [2.7K]  ./bin/test
│   ├── [2.7K]  ./bin/tftp
│   ├── [2.7K]  ./bin/time
│   ├── [2.7K]  ./bin/timeout
│   ├── [2.7K]  ./bin/top
│   ├── [2.7K]  ./bin/touch
│   ├── [2.8K]  ./bin/traceroute
│   ├── [2.7K]  ./bin/true
│   ├── [2.8K]  ./bin/truncate
│   ├── [2.7K]  ./bin/tty
│   ├── [2.8K]  ./bin/udpsvd
│   ├── [2.7K]  ./bin/umount
│   ├── [2.7K]  ./bin/uname
│   ├── [2.8K]  ./bin/unix2dos
│   ├── [2.7K]  ./bin/unlink
│   ├── [2.7K]  ./bin/uptime
│   ├── [2.7K]  ./bin/usleep
│   ├── [2.8K]  ./bin/uudecode
│   ├── [2.8K]  ./bin/uuencode
│   ├── [2.7K]  ./bin/vi
│   ├── [2.7K]  ./bin/volname
│   ├── [2.7K]  ./bin/watch
│   ├── [2.7K]  ./bin/wc
│   ├── [2.7K]  ./bin/which
│   ├── [2.7K]  ./bin/whoami
│   ├── [2.7K]  ./bin/whois
│   ├── [2.7K]  ./bin/xargs
│   └── [2.7K]  ./bin/yes
├── [4.0K]  ./dev
├── [4.0K]  ./etc
│   ├── [ 823]  ./etc/fstab
│   ├── [  46]  ./etc/group
│   ├── [  84]  ./etc/host.conf
│   ├── [  46]  ./etc/hosts
│   ├── [4.0K]  ./etc/init.d
│   │   ├── [ 966]  ./etc/init.d/rc.local
│   │   └── [ 496]  ./etc/init.d/rcS
│   ├── [ 657]  ./etc/inittab
│   ├── [4.0K]  ./etc/jffs2
│   ├── [  14]  ./etc/ld.so.conf
│   ├── [1022]  ./etc/mdev.conf
│   ├── [ 349]  ./etc/nsswitch.conf
│   ├── [  12]  ./etc/passwd -> jffs2/passwd
│   ├── [ 889]  ./etc/profile
│   ├── [  17]  ./etc/resolv.conf -> jffs2/resolv.conf
│   ├── [ 325]  ./etc/services
│   ├── [  12]  ./etc/shadow -> jffs2/shadow
│   ├── [4.0K]  ./etc/sysconfig
│   │   └── [   7]  ./etc/sysconfig/HOSTNAME
│   └── [4.0K]  ./etc/udhcpd.conf
├── [2.7K]  ./init
├── [4.0K]  ./lib
│   ├── [ 25K]  ./lib/ld-uClibc-0.9.33.2.so
│   ├── [  21]  ./lib/ld-uClibc.so.0 -> ld-uClibc-0.9.33.2.so
│   ├── [  18]  ./lib/libatomic.so -> libatomic.so.1.0.0
│   ├── [  18]  ./lib/libatomic.so.1 -> libatomic.so.1.0.0
│   ├── [ 14K]  ./lib/libatomic.so.1.0.0
│   ├── [712K]  ./lib/libbusybox.so.1.24.1
│   ├── [ 13K]  ./lib/libcrypt-0.9.33.2.so
│   ├── [  20]  ./lib/libcrypt.so.0 -> libcrypt-0.9.33.2.so
│   ├── [  21]  ./lib/libc.so.0 -> libuClibc-0.9.33.2.so
│   ├── [ 13K]  ./lib/libdl-0.9.33.2.so
│   ├── [  17]  ./lib/libdl.so.0 -> libdl-0.9.33.2.so
│   ├── [ 132]  ./lib/libgcc_s.so
│   ├── [126K]  ./lib/libgcc_s.so.1
│   ├── [ 38K]  ./lib/libiw.so.29
│   ├── [ 61K]  ./lib/libm-0.9.33.2.so
│   ├── [  16]  ./lib/libm.so.0 -> libm-0.9.33.2.so
│   ├── [4.6K]  ./lib/libnsl-0.9.33.2.so
│   ├── [  18]  ./lib/libnsl.so.0 -> libnsl-0.9.33.2.so
│   ├── [ 94K]  ./lib/libpthread-0.9.33.2.so
│   ├── [  22]  ./lib/libpthread.so.0 -> libpthread-0.9.33.2.so
│   ├── [4.6K]  ./lib/libresolv-0.9.33.2.so
│   ├── [  21]  ./lib/libresolv.so.0 -> libresolv-0.9.33.2.so
│   ├── [ 13K]  ./lib/librt-0.9.33.2.so
│   ├── [  17]  ./lib/librt.so.0 -> librt-0.9.33.2.so
│   ├── [  19]  ./lib/libstdc++.so -> libstdc++.so.6.0.19
│   ├── [  19]  ./lib/libstdc++.so.6 -> libstdc++.so.6.0.19
│   ├── [726K]  ./lib/libstdc++.so.6.0.19
│   ├── [2.3K]  ./lib/libstdc++.so.6.0.19-gdb.py
│   ├── [4.7K]  ./lib/libubacktrace-0.9.33.2.so
│   ├── [  25]  ./lib/libubacktrace.so.0 -> libubacktrace-0.9.33.2.so
│   ├── [343K]  ./lib/libuClibc-0.9.33.2.so
│   ├── [4.6K]  ./lib/libutil-0.9.33.2.so
│   ├── [  19]  ./lib/libutil.so.0 -> libutil-0.9.33.2.so
│   └── [4.0K]  ./lib/modules
├── [4.0K]  ./mnt
├── [4.0K]  ./proc
├── [4.0K]  ./sbin
│   ├── [2.7K]  ./sbin/acpid
│   ├── [2.8K]  ./sbin/adjtimex
│   ├── [2.7K]  ./sbin/arp
│   ├── [2.7K]  ./sbin/arping
│   ├── [2.8K]  ./sbin/blockdev
│   ├── [2.8K]  ./sbin/bootchartd
│   ├── [2.7K]  ./sbin/brctl
│   ├── [2.7K]  ./sbin/chat
│   ├── [2.7K]  ./sbin/chroot
│   ├── [2.7K]  ./sbin/depmod
│   ├── [2.7K]  ./sbin/devmem
│   ├── [2.8K]  ./sbin/dhcprelay
│   ├── [6.2K]  ./sbin/env_ops
│   ├── [2.8K]  ./sbin/fakeidentd
│   ├── [2.7K]  ./sbin/fbset
│   ├── [2.8K]  ./sbin/fbsplash
│   ├── [2.7K]  ./sbin/fdisk
│   ├── [2.7K]  ./sbin/fstrim
│   ├── [2.7K]  ./sbin/ftpd
│   ├── [2.7K]  ./sbin/getty
│   ├── [2.7K]  ./sbin/halt
│   ├── [2.7K]  ./sbin/hwclock
│   ├── [2.8K]  ./sbin/i2cdetect
│   ├── [2.7K]  ./sbin/i2cdump
│   ├── [2.7K]  ./sbin/i2cget
│   ├── [2.7K]  ./sbin/i2cset
│   ├── [2.8K]  ./sbin/ifconfig
│   ├── [2.7K]  ./sbin/ifdown
│   ├── [2.8K]  ./sbin/ifenslave
│   ├── [2.7K]  ./sbin/ifplugd
│   ├── [2.7K]  ./sbin/ifup
│   ├── [2.7K]  ./sbin/inetd
│   ├── [2.7K]  ./sbin/init
│   ├── [2.8K]  ./sbin/inotifyd
│   ├── [2.7K]  ./sbin/insmod
│   ├── [2.7K]  ./sbin/ip
│   ├── [2.7K]  ./sbin/ipaddr
│   ├── [2.7K]  ./sbin/iplink
│   ├── [2.7K]  ./sbin/iproute
│   ├── [2.7K]  ./sbin/iprule
│   ├── [2.8K]  ./sbin/iptunnel
│   ├── [2.7K]  ./sbin/killall5
│   ├── [2.7K]  ./sbin/klogd
│   ├── [ 13K]  ./sbin/ldconfig
│   ├── [2.8K]  ./sbin/loadfont
│   ├── [2.8K]  ./sbin/loadkmap
│   ├── [2.7K]  ./sbin/logread
│   ├── [2.7K]  ./sbin/losetup
│   ├── [2.7K]  ./sbin/lsmod
│   ├── [2.8K]  ./sbin/makedevs
│   ├── [2.7K]  ./sbin/mdev
│   ├── [2.8K]  ./sbin/mkdosfs
│   ├── [2.8K]  ./sbin/mkfs.vfat
│   ├── [192K]  ./sbin/mmc_test
│   ├── [2.7K]  ./sbin/modinfo
│   ├── [2.8K]  ./sbin/modprobe
│   ├── [2.7K]  ./sbin/nameif
│   ├── [2.8K]  ./sbin/nanddump
│   ├── [2.8K]  ./sbin/nandwrite
│   ├── [2.8K]  ./sbin/nbd-client
│   ├── [2.7K]  ./sbin/ntpd
│   ├── [2.8K]  ./sbin/pivot_root
│   ├── [2.7K]  ./sbin/poweroff
│   ├── [2.8K]  ./sbin/powertop
│   ├── [2.7K]  ./sbin/rdate
│   ├── [2.7K]  ./sbin/rdev
│   ├── [2.8K]  ./sbin/readahead
│   ├── [2.8K]  ./sbin/readprofile
│   ├── [2.7K]  ./sbin/reboot
│   ├── [2.7K]  ./sbin/rmmod
│   ├── [2.7K]  ./sbin/route
│   ├── [2.7K]  ./sbin/rtcwake
│   ├── [2.8K]  ./sbin/setconsole
│   ├── [2.7K]  ./sbin/setfont
│   ├── [2.8K]  ./sbin/setlogcons
│   ├── [2.8K]  ./sbin/slattach
│   ├── [2.8K]  ./sbin/switch_root
│   ├── [2.7K]  ./sbin/sysctl
│   ├── [2.7K]  ./sbin/syslogd
│   ├── [2.7K]  ./sbin/telnetd
│   ├── [2.7K]  ./sbin/tftpd
│   ├── [2.7K]  ./sbin/tunctl
│   ├── [2.8K]  ./sbin/ubiattach
│   ├── [2.8K]  ./sbin/ubidetach
│   ├── [2.8K]  ./sbin/ubimkvol
│   ├── [2.8K]  ./sbin/ubirmvol
│   ├── [2.8K]  ./sbin/ubirsvol
│   ├── [2.8K]  ./sbin/ubiupdatevol
│   ├── [2.7K]  ./sbin/udhcpc
│   ├── [2.7K]  ./sbin/udhcpd
│   ├── [2.7K]  ./sbin/uevent
│   ├── [3.7K]  ./sbin/update_image.sh
│   ├── [ 26K]  ./sbin/updater
│   ├── [2.7K]  ./sbin/vconfig
│   └── [2.8K]  ./sbin/watchdog
├── [4.0K]  ./sys
├── [4.0K]  ./tmp
├── [4.0K]  ./usr
└── [4.0K]  ./var
    └── [4.0K]  ./var/run

0x3BB000 - /etc/jffs2 - JFFS2 (RW)

[4.0K]  .
├── [9.0K]  ./anyka_cfg.ini
├── [1.0K]  ./apecloud_cfg.ini
├── [  38]  ./custom_uid.txt
├── [ 176]  ./danale.conf
├── [1.9K]  ./hostapd.conf
├── [ 68K]  ./isp_f23_mipi2lane.conf
├── [  64]  ./nooie_uid.conf
├── [ 128]  ./passwd
├── [ 128]  ./passwd-
├── [  42]  ./resolv.conf
├── [ 136]  ./shadow
├── [ 136]  ./shadow-
├── [4.2K]  ./venc.cfg
├── [  17]  ./wifimac.txt
├── [1.5K]  ./wifi.map
└── [1.5K]  ./wpa_supplicant.conf

0x438000 - /usr User Filesystem - SquashFS (RO)
[4.0K]  .
├── [4.0K]  ./bin
│   ├── [7.4K]  ./bin/ak_adec_demo
│   ├── [8.9K]  ./bin/ak_aec_demo
│   ├── [ 11K]  ./bin/ak_aec_ex_demo
│   ├── [9.1K]  ./bin/ak_aenc_demo
│   ├── [5.9K]  ./bin/ak_ai_demo
│   ├── [6.5K]  ./bin/ak_ao_demo
│   ├── [4.3K]  ./bin/ak_drv_i2c_demo
│   ├── [3.9K]  ./bin/ak_drv_ir_demo
│   ├── [4.2K]  ./bin/ak_drv_key_demo
│   ├── [4.7K]  ./bin/ak_drv_ptz_demo
│   ├── [4.7K]  ./bin/ak_drv_pwm_demo
│   ├── [3.7K]  ./bin/ak_drv_wdt_demo
│   ├── [ 22K]  ./bin/ak_dvr_record_demo
│   ├── [6.6K]  ./bin/ak_effect_demo
│   ├── [6.3K]  ./bin/ak_lib_version
│   ├── [7.0K]  ./bin/ak_mask_demo
│   ├── [5.6K]  ./bin/ak_md_demo
│   ├── [ 13K]  ./bin/ak_mt_demo
│   ├── [5.8K]  ./bin/ak_od_demo
│   ├── [168K]  ./bin/ak_onvif_demo
│   ├── [8.4K]  ./bin/ak_osd_demo
│   ├── [ 16K]  ./bin/ak_rtsp_demo
│   ├── [5.9K]  ./bin/ak_tw_demo
│   ├── [ 12K]  ./bin/ak_venc_demo
│   ├── [5.6K]  ./bin/ak_vi_demo
│   ├── [ 10K]  ./bin/ak_vpss_demo
│   ├── [5.8K]  ./bin/ak_vpss_md_demo
│   ├── [2.0M]  ./bin/anyka_ipc
│   ├── [1.2K]  ./bin/ca.crt.pem
│   ├── [5.6K]  ./bin/ccli
│   ├── [6.4K]  ./bin/cmd_serverd
│   ├── [ 12K]  ./bin/daemon
│   ├── [5.9K]  ./bin/disk_repair
│   ├── [ 15K]  ./bin/getconf
│   ├── [ 14K]  ./bin/get_device_id
│   ├── [ 10K]  ./bin/get_nooie_uid
│   ├── [334K]  ./bin/hostapd
│   ├── [5.4K]  ./bin/iconv
│   ├── [ 26K]  ./bin/iwconfig
│   ├── [ 29K]  ./bin/iwlist
│   ├── [ 15K]  ./bin/iwpriv
│   ├── [7.4K]  ./bin/ldd
│   ├── [9.2K]  ./bin/set_nooie_ssid
│   ├── [ 16K]  ./bin/top_thread
│   ├── [154K]  ./bin/wpa_cli
│   ├── [ 98K]  ./bin/wpa_passphrase
│   └── [429K]  ./bin/wpa_supplicant
├── [4.0K]  ./lib
│   ├── [1.0M]  ./lib/libakaudiocodec.so
│   ├── [ 44K]  ./lib/libakaudiofilter.so
│   ├── [ 19K]  ./lib/libakispsdk.so
│   ├── [368K]  ./lib/libakmedialib.so
│   ├── [ 20K]  ./lib/libak_mt.so
│   ├── [ 16K]  ./lib/libakuio.so
│   ├── [353K]  ./lib/libakv_encode.so
│   ├── [ 16K]  ./lib/libapp_alarm.so
│   ├── [273K]  ./lib/libapp_dvr.so
│   ├── [ 14K]  ./lib/libapp_ini.so
│   ├── [ 13K]  ./lib/libapp_net.so
│   ├── [141K]  ./lib/libapp_onvif.so
│   ├── [ 20K]  ./lib/libapp_osd_ex.so
│   ├── [ 55K]  ./lib/libapp_rtsp.so
│   ├── [297K]  ./lib/libiconv.so
│   ├── [ 29K]  ./lib/libmpi_adec.so
│   ├── [ 28K]  ./lib/libmpi_aed.so
│   ├── [ 36K]  ./lib/libmpi_aenc.so
│   ├── [ 17K]  ./lib/libmpi_md.so
│   ├── [ 29K]  ./lib/libmpi_muxer.so
│   ├── [ 25K]  ./lib/libmpi_osd.so
│   ├── [ 67K]  ./lib/libmpi_venc.so
│   ├── [ 47K]  ./lib/libplat_ai.so
│   ├── [ 32K]  ./lib/libplat_ao.so
│   ├── [ 20K]  ./lib/libplat_ats.so
│   ├── [ 25K]  ./lib/libplat_common.so
│   ├── [ 36K]  ./lib/libplat_drv.so
│   ├── [ 18K]  ./lib/libplat_ipcsrv.so
│   ├── [ 14K]  ./lib/libplat_its.so
│   ├── [ 12K]  ./lib/libplat_thread.so
│   ├── [ 20K]  ./lib/libplat_tw.so
│   ├── [ 36K]  ./lib/libplat_venc_cb.so
│   ├── [103K]  ./lib/libplat_vi.so
│   ├── [ 34K]  ./lib/libplat_vpss.so
│   ├── [336K]  ./lib/libwolfmqtt.so.5
│   └── [131K]  ./lib/libzbar.so.0
├── [4.0K]  ./local
│   ├── [260K]  ./local/ak_font_16.bin
│   ├── [1.7K]  ./local/cloud_cfg.ini
│   ├── [8.4K]  ./local/factory_cfg.ini
│   ├── [   8]  ./local/factory_fw_version
│   ├── [ 68K]  ./local/isp_f23_mipi2lane.conf
│   └── [1.5K]  ./local/wpa_supplicant.conf
├── [4.0K]  ./modules
│   ├── [1.6M]  ./modules/8188fu.ko
│   ├── [ 26K]  ./modules/akcamera.ko
│   ├── [4.4K]  ./modules/ak_info_dump.ko
│   ├── [5.1K]  ./modules/ak_videobuf_block.ko
│   ├── [ 32K]  ./modules/g_file_storage.ko
│   ├── [ 44K]  ./modules/g_mass_storage.ko
│   ├── [ 24K]  ./modules/otg-hs.ko
│   ├── [4.7K]  ./modules/sdio_wifi.ko
│   ├── [8.7K]  ./modules/sensor_f23_mipi.ko
│   ├── [ 18K]  ./modules/udc.ko
│   └── [9.0K]  ./modules/usbburn.ko
├── [4.0K]  ./sbin
│   ├── [ 947]  ./sbin/anyka_ipc.sh
│   ├── [1.5K]  ./sbin/ap.sh
│   ├── [1.2K]  ./sbin/blue_led.sh
│   ├── [ 916]  ./sbin/camera.sh
│   ├── [1.0K]  ./sbin/device_save.sh
│   ├── [2.8K]  ./sbin/eth_manage.sh
│   ├── [ 201]  ./sbin/kill_pro.sh
│   ├── [1.2K]  ./sbin/led.sh
│   ├── [1.3K]  ./sbin/net_manage.sh
│   ├── [5.0K]  ./sbin/ota_nooie.sh
│   ├── [3.6K]  ./sbin/ota.sh
│   ├── [ 619]  ./sbin/recover_cfg.sh
│   ├── [1.2K]  ./sbin/red_led.sh
│   ├── [3.7K]  ./sbin/service.sh
│   ├── [ 535]  ./sbin/standby.sh
│   ├── [2.4K]  ./sbin/station_connect.sh
│   ├── [ 874]  ./sbin/udisk.sh
│   ├── [4.6K]  ./sbin/update_check.sh
│   ├── [3.9K]  ./sbin/update.sh
│   ├── [1.7K]  ./sbin/wifi_ap.sh
│   ├── [1.6K]  ./sbin/wifi_driver.sh
│   ├── [ 817]  ./sbin/wifi_manage.sh
│   ├── [9.1K]  ./sbin/wifi_run.sh
│   └── [ 11K]  ./sbin/wifi_station.sh
└── [4.0K]  ./share
    ├── [2.9K]  ./share/anyka_di_cn.mp3
    ├── [4.3K]  ./share/camera_is_now_online.mp3
    ├── [4.9K]  ./share/camera_reset_completed.mp3
    ├── [2.3K]  ./share/camera_upgrade_complete.mp3
    ├── [2.1K]  ./share/connecting_wi_fi.mp3
    ├── [3.9K]  ./share/failed_to_connect_the_Internet_please_check_your_connection.mp3
    ├── [4.2K]  ./share/failed_to_connect_wi_fi_please_try_again_after_reset.mp3
    ├── [3.7K]  ./share/failed_to_upgrade_camera_please_try_again.mp3
    ├── [4.7K]  ./share/incorrect_wi_fi_password_please_try_again_after_reset.mp3
    ├── [4.0K]  ./share/udhcpc
    │   └── [1.0K]  ./share/udhcpc/default.script
    ├── [3.8K]  ./share/upgrading_camera_please_do_not_cut_off_power.mp3
    └── [5.7K]  ./share/welcome_and_thanks_for_choosing_smart_camera_starting_up_please_stand_by.mp3



Certificates:
Embedded in binary "anyka_ipc"
│   ├── [4.0K]  ./bin/anyka_ipc.extracted
│   │   ├── [4.0K]  ./bin/anyka_ipc.extracted/135394
│   │   │   └── [1.7K]  ./bin/anyka_ipc.extracted/135394/pem.crt
│   │   ├── [4.0K]  ./bin/anyka_ipc.extracted/135A58
│   │   │   └── [1.6K]  ./bin/anyka_ipc.extracted/135A58/pem.key
│   │   └── [4.0K]  ./bin/anyka_ipc.extracted/1360E8
│   │       └── [1.2K]  ./bin/anyka_ipc.extracted/1360E8/pem.crt



FW: V1.1.41

Kernel & cmdline:
3.4.35
console=ttySAK0,115200n8 root=/dev/mtdblock4 rootfstype=squashfs init=/sbin/init mem=64M memsize=64M

BusyBox v1.24.1 (2018-10-17 20:46:15 CST) multi-call binary

Busybox Modules:
[root@anyka ~]$ busybox --list
[
[[
acpid
adjtimex
arp
arping
ash
awk
base64
basename
beep
blockdev
bootchartd
brctl
cal
cat
catv
chat
chmod
chown
chroot
chrt
chvt
cksum
clear
cmp
cp
crontab
cttyhack
cut
date
dc
dd
depmod
devmem
df
dhcprelay
diff
dirname
dmesg
dnsdomainname
dos2unix
du
dumpkmap
dumpleases
echo
egrep
eject
env
expand
expr
fakeidentd
false
fatattr
fbset
fbsplash
fgconsole
fgrep
find
fold
free
fstrim
fsync
ftpd
ftpget
ftpput
fuser
getopt
getty
grep
groups
halt
hd
head
hexdump
hostid
hostname
hwclock
i2cdetect
i2cdump
i2cget
i2cset
id
ifconfig
ifdown
ifenslave
ifplugd
ifup
inetd
init
inotifyd
insmod
install
ionice
iostat
ip
ipaddr
ipcalc
ipcrm
ipcs
iplink
iproute
iprule
iptunnel
kbd_mode
kill
killall
killall5
klogd
less
linux32
linux64
linuxrc
ln
loadfont
loadkmap
logger
login
logname
logread
losetup
ls
lsmod
lsof
lspci
lsusb
makedevs
md5sum
mdev
mesg
mkdir
mkdosfs
mkfifo
mkfs.vfat
mknod
modinfo
modprobe
more
mount
mountpoint
mv
nameif
nanddump
nandwrite
nbd-client
nc
netstat
nice
nslookup
ntpd
od
passwd
pgrep
pidof
ping
pivot_root
pkill
pmap
poweroff
powertop
printenv
printf
ps
pscan
pstree
pwd
pwdx
rdate
rdev
readahead
readlink
readprofile
realpath
reboot
renice
reset
resize
rm
rmdir
rmmod
route
rtcwake
rx
script
scriptreplay
sed
setarch
setconsole
setfont
setkeycodes
setlogcons
setserial
setsid
sh
sha1sum
sha256sum
sha3sum
sha512sum
showkey
shuf
slattach
sleep
smemcap
sort
split
stat
strings
stty
sum
switch_root
sync
sysctl
syslogd
tail
tar
tcpsvd
tee
telnet
telnetd
test
tftp
tftpd
time
timeout
top
touch
traceroute
true
truncate
tty
tunctl
ubiattach
ubidetach
ubimkvol
ubirmvol
ubirsvol
ubiupdatevol
udhcpc
udhcpd
udpsvd
uevent
umount
uname
unix2dos
unlink
uptime
usleep
uudecode
uuencode
vconfig
vi
volname
watch
watchdog
wc
which
whoami
whois
xargs
yes


Netstat:
[root@anyka ~]$ netstat -an
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 127.0.0.1:8782          0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:7000          0.0.0.0:*               LISTEN
tcp        0      0 192.168.178.97:57120    3.71.129.157:1883       ESTABLISHED
udp        0      0 192.168.178.97:53305    0.0.0.0:*
udp        0      0 0.0.0.0:32345           0.0.0.0:*


Diskspace:
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 1.3M      1.3M         0 100% /
/dev/mtdblock6            3.3M      3.3M         0 100% /usr
/dev/mtdblock5          500.0K    128.0K    372.0K  26% /etc/jffs2
/dev/loop0               95.0K       512     94.5K   1% /tmp/ramdisk


Memory Usage:
             total       used       free     shared    buffers     cached
Mem:         33384      33044        340          0       5664       9268
-/+ buffers/cache:      18112      15272
Swap:            0          0          0


Partitions:
major minor  #blocks  name

   7        0        100 loop0
  31        0       8192 mtdblock0
  31        1       2048 mtdblock1
  31        2          4 mtdblock2
  31        3          4 mtdblock3
  31        4       1536 mtdblock4
  31        5        500 mtdblock5
  31        6       3800 mtdblock6
 179        0   15267840 mmcblk0
 179        1   15263744 mmcblk0p1


Mountpoints:
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    defaults            0   0
tmpfs           /tmp            tmpfs   defaults            0   0
tmpfs           /var            tmpfs   defaults            0   0
devpts          /dev/pts        devpts  defaults                                                                                                                    0       0
tmpfs           /mnt            tmpfs   defaults            0   0
sysfs           /sys            sysfs   defaults            0   0


Blockdevices:
dev:    size   erasesize  name
mtd0: 00800000 00001000 "spi0.0"
mtd1: 00200000 00001000 "KERNEL"
mtd2: 00001000 00001000 "MAC"
mtd3: 00001000 00001000 "ENV"
mtd4: 00180000 00001000 "A"
mtd5: 0007d000 00001000 "B"
mtd6: 003b6000 00001000 "C"


SOC:
Processor       : ARM926EJ-S rev 5 (v5l)
BogoMIPS        : 199.06
Features        : swp half fastmult edsp java
CPU implementer : 0x41
CPU architecture: 5TEJ
CPU variant     : 0x0
CPU part        : 0x926
CPU revision    : 5


Hardware        : CLOUD39EV3_AK3918EV300_MNBD
Revision        : 0000
Serial          : 0000000000000000

Sensor:
isp_f23_mipi2lane.conf v.4.003


Boot Process:
::sysinit:/etc/init.d/rcS
    ->
    /etc/init.d/rc.local
        ->
        # mount usr file-system.
        /bin/mount -t squashfs /dev/mtdblock6 /usr
        # mount jffs2 file-system.
        /bin/mount -t jffs2 /dev/mtdblock5 /etc/jffs2
        /usr/sbin/camera.sh setup
        /usr/sbin/service.sh start &
            ->
            cfgfile="/etc/jffs2/anyka_cfg.ini"
            cmd_serverd
            if [ $WIFI_TEST = 1 ]; then
                #insmod /usr/modules/sdio_wifi.ko
                insmod /usr/modules/8188fu.ko
                /mnt/wifitest/wifi_test.sh
                echo "start wifi test."
            elif [ $FACTORY_TEST = 1 ]; then
                /mnt/usbnet/product_test &
                insmod /mnt/usbnet/otg-hs.ko
                insmod /mnt/usbnet/usbnet.ko
                insmod /mnt/usbnet/asix.ko
                #insmod /mnt/usbnet/udc.ko
                #insmod /mnt/usbnet/g_ether.ko
                sleep 1
                ifconfig eth0 up
                sleep 1
                /usr/sbin/eth_manage.sh start
                echo "start product test."
            elif [ $AGING_TEST = 1 ]; then
                #insmod /usr/modules/sdio_wifi.ko
                insmod /usr/modules/8188fu.ko
                sleep 1
                ifconfig wlan0 up
                sleep 1
                /tmp/aging_test
                echo "start aging test."
            else
                if [ $UPDATE_MODE = 1 ]; then
                    echo "to do software update check."
                    /usr/sbin/update_check.sh
                fi
                daemon
                echo 1 > /sys/class/leds/red_led/brightness
                /usr/sbin/anyka_ipc.sh start
                echo "start net service......"
            fi

            boot_from=`cat /proc/cmdline | grep nfsroot`
            if [ -z "$boot_from" ] && [ $FACTORY_TEST = 0 ] && [ $WIFI_TEST = 0 ] && [ $AGING_TEST = 0 ];then
                echo "start net service......"
                echo "[service.sh] find ssid = $ssid"
                export ssid
                /usr/sbin/net_manage.sh &
            else
                echo "## start from nfsroot, do not change ipaddress!"
            fi
            unset boot_from



            if test -e /dev/mmcblk0p1 ;then
                mount -rw /dev/mmcblk0p1 /mnt
            elif test -e /dev/mmcblk0 ;then
                mount -rw /dev/mmcblk0 /mnt
            fi

            if test -d /mnt/usbnet ;then
                FACTORY_TEST=1
                echo 0 > /sys/class/leds/red_led/brightness
                echo 1 > /sys/class/leds/blue_led/brightness
            else
                FACTORY_TEST=0
            fi

            if test -d /mnt/agingtest ;then
                AGING_TEST=1
                echo 0 > /sys/class/leds/red_led/brightness
                echo 1 > /sys/class/leds/blue_led/brightness
                cp /mnt/agingtest/aging_test /tmp/
            else
                AGING_TEST=0
            fi

            if test -d /mnt/wifitest ;then
                WIFI_TEST=1
                echo 0 > /sys/class/leds/red_led/brightness
                echo 1 > /sys/class/leds/blue_led/brightness
            else
                WIFI_TEST=0
            fi

            if test -d /mnt/update ;then
                UPDATE_MODE=1
            else
                UPDATE_MODE=0
            fi
            LOG_FILE="/mnt/debug/log.txt"
            if [ -f $LOG_FILE ];then
                # Close STDOUT file descriptor
                exec 1<&-
                # Close STDERR FD
                exec 2<&-

                # Open STDOUT as $LOG_FILE file for read and write.
                exec 1<>$LOG_FILE

                # Redirect STDERR to STDOUT
                exec 2>&1
                #
            else
                echo "NO DEBUG FILE"
            fi


Runtime Exploitation:
If the device has been configured before
Pick you Poison via FACTORY_TEST or WIFI_TEST or "encrypted" enable_telnetd.dat entrypoints on SDCard.

Example:
WIFI_TEST:
01. Format SD-CARD FAT32
02. create new shadowfile and save in sdcard root.
        Exammple shadow root password = tc100
02. Create "wifitest" folder in SDCard root
03. Create wifi_test.sh in wifitest folder.
04. Example wifi_test.sh: (only launches cmd_serverd, ftp and telned)
		#! /bin/sh
		mount --bind /mnt/tempshadow /etc/jffs2/shadow
		/bin/tcpsvd 0 21 ftpd -w / -t 600 &
		/sbin/telnetd &
		/usr/sbin/net_manage.sh &		#If the device has not been linked/configured before you have to also edit the wpa_supplicant config.

05. Optional: Debug Log & CoreDump on SDCard
    a. Create "debug" folder in SDCard root
    b. create "log.txt" in debug folder

Shadowfile:

openssl passwd -1 tc100
$1$HZ/jeDVN$8r2kBlyqHxyqhjYjS378Q.


Persistant Changes:

Option 1 - Repack Image and flash via SPI Programming
Option 2 - Repack Image and flash via DD
Option 3 - Repack Image and write wia nandwrite
Option 4 - Repack Imange and Flash via Uart / U-Boot
Option 5 - Repack and Upgrade via USB OTA
Option 6 - Just use an SDCard


Apps:

Watchdog:
[monitor_thread:404] interval: 3(sec), fifo[/tmp/daemon_fifo].size=50

anyka_ipc
ak_cmd_server_register(7000,"anyka_ipc7000");

cmd_serverd


Exploration Ideas:

- Enable Telnet
- Change Root Password
- Add Dropbear or run via SDCard
- Disable cloud
- Enable RTSP or Build from cross-compile https://github.com/ricardojlrufino/arm-anykav200-crosstool
- Change Encoding Settings (25FPS, Bitrate..)
- Remove Cloud binaries
- Anaylze Cloud binaries
- reverse cmd_serverd
- Change watchdog
- mitm the ssl connection to the cloud and map api endpoints
