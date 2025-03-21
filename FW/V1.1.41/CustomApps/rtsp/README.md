via cross-compile
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
