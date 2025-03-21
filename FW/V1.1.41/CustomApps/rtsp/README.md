# cross-compile 
https://github.com/ricardojlrufino/arm-anykav200-crosstool

Simple Dockerfile for Building
```
# Step 1: Use the latest Ubuntu image
FROM ubuntu:latest

# Step 2: Install SSH server, enable it, and map port 8022 -> 22
RUN apt-get update && apt-get install -y \
    openssh-server \
    && mkdir /var/run/sshd \
    && echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config \
    && echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config \
    && echo 'root:root' | chpasswd

# Step 3: Enable 32-bit support and install required libraries
RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y \
        lib32stdc++6 \
        libmpc-dev:i386 \
        libz1:i386 \
        libstdc++6:i386 \
        libgcc1:i386 \
        zlib1g:i386 \
        libc6:i386 \
        gcc-multilib \
        g++-multilib \
        libc6-dev-i386 \
        unzip \
        git \
        wget \
    && ln -s /lib/i386-linux-gnu/libmpfr.so.6 /lib/i386-linux-gnu/libmpfr.so.4

# Step 4: Clone the repository and unzip the toolchain
RUN git clone https://github.com/ricardojlrufino/arm-anykav200-crosstool.git /tmp/crosstool \
    && unzip /tmp/crosstool/arm-anykav200-crosstool.zip -d /opt/ \
    && rm -rf /tmp/crosstool

# Step 5: Set the environment variable for the toolchain
ENV PATH=$PATH:/opt/arm-anykav200-crosstool/usr/bin


# Step 6: Get the SDK
RUN mkdir /src \ 
    && git clone https://github.com/Nemobi/ak3918ev300v18.git /src/ak3918ev300v18

# Step 7: Build
RUN mkdir /src/custom \
    && wget -P /src/custom https://github.com/ehspill/Teckin-TC100/blob/main/FW/V1.1.41/CustomApps/rtsp/ak_rtsp_demo.c \
    && arm-anykav200-linux-uclibcgnueabi-gcc -fno-strict-aliasing -Os -Wall -Werror -D_GNU_SOURCE -std=c99 -fms-extensions -I/src/ak3918ev300v18/platform/libplat/include -I/src/ak3918ev300v18/platform/libapp/../libplat/include_inner -I/src/ak3918ev300v18/platform/libmpi/include -I/src/ak3918ev300v18/platform/libapp/include -c ak_rtsp_demo.c -o ak_rtsp_demo.o \
    && arm-anykav200-linux-uclibcgnueabi-g++ ak_rtsp_demo.o -L/src/ak3918ev300v18/platform/libplat/lib -L/src/ak3918ev300v18/platform/libmpi/lib -L/src/ak3918ev300v18/platform/libapp/lib -lakuio -lakv_encode -lakispsdk -lplat_common -lplat_thread -lplat_vi -lplat_drv -lplat_vpss -lplat_ipcsrv -lplat_venc_cb -lmpi_venc -lapp_rtsp -lapp_net -lrt -lpthread -ldl -Wl,-rpath=/mnt -rdynamic -Xlinker "-("  -Xlinker "-)" -o ak_rtsp_demo


# Start SSH server when container starts
CMD ["/usr/sbin/sshd", "-D"]
```
# sdk 
https://github.com/Nemobi/ak3918ev300v18

# ak_rtsp_demo.c 
based on https://github.com/MuhammedKalkan/Anyka-Camera-Firmware

```
arm-anykav200-linux-uclibcgnueabi-gcc -fno-strict-aliasing -Os -Wall -Werror -D_GNU_SOURCE -std=c99 -fms-extensions -I/ak3918ev300v18/platform/libplat/include -I/ak3918ev300v18/platform/libapp/../libplat/include_inner -I/ak3918ev300v18/platform/libmpi/include -I/ak3918ev300v18/platform/libapp/include -c ak_rtsp_demo.c -o ak_rtsp_demo.o
arm-anykav200-linux-uclibcgnueabi-g++ ak_rtsp_demo.o -L/ak3918ev300v18/platform/libplat/lib -L/ak3918ev300v18/platform/libmpi/lib -L/ak3918ev300v18/platform/libapp/lib -lakuio -lakv_encode -lakispsdk -lplat_common -lplat_thread -lplat_vi -lplat_drv -lplat_vpss -lplat_ipcsrv -lplat_venc_cb -lmpi_venc -lapp_rtsp -lapp_net -lrt -lpthread -ldl -Wl,-rpath=/mnt -rdynamic -Xlinker "-("  -Xlinker "-)" -o ak_rtsp_demo

[root@anyka /mnt]$ ./rtsp --help
./rtsp
        --help             -h        HELP
        --main-width       -a [NUM]  ( DEFAULT: 1920 )
        --main-height      -b [NUM]  ( DEFAULT: 1080 )
        --sub-width        -c [NUM]  ( DEFAULT: 640 )
        --sub-height       -d [NUM]  ( DEFAULT: 480 )
        --main-kbps        -e [NUM]  ( DEFAULT: 2048 )
        --sub-kbps         -f [NUM]  ( DEFAULT: 512 )
        --main-chn-name    -n [NAME] ( DEFAULT: 'vs0' )
        --sub-chn-name     -o [NAME] ( DEFAULT: 'vs1' )
        --gop              -p [NUM]  ( DEFAULT: 50 )
        --minqp            -q [NUM]  ( DEFAULT: 28 )
        --maxqp            -r [NUM]  ( DEFAULT: 42 )
        --main-fps         -g [NUM]  ( DEFAULT: 25 )
        --sub-fps          -i [NUM]  ( DEFAULT: 25 )
        --main-video-mode  -j [0|1]  BR_MODE_CBR: 0 | BR_MODE_VBR: 1( DEFAULT: 0 )
        --sub-video-mode   -k [0|1]  BR_MODE_CBR: 0 | BR_MODE_VBR: 1( DEFAULT: 0 )
        --main-enc-type    -l [0|2]  H264_ENC_TYPE: 0 | HEVC_ENC_TYPE: 2( DEFAULT: 0 )
        --sub-enc-type     -m [0|2]  H264_ENC_TYPE: 0 | HEVC_ENC_TYPE: 2( DEFAULT: 0 )
```
