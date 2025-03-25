#! /bin/sh
mount --bind /mnt/tempshadow /etc/jffs2/shadow
mount --bind /mnt/tempwificreds /etc/jffs2/anyka_cfg.ini
/bin/tcpsvd 0 21 ftpd -w / -t 600 &
/sbin/telnetd &
kill cmd_serverd
/usr/sbin/net_manage.sh &
