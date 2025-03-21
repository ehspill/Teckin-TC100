via cross-compile
```
arm-anykav200-linux-uclibcgnueabi-gcc -fno-strict-aliasing -Os -Wall -Werror -D_GNU_SOURCE -std=c99 -fms-extensions -I/ak3918ev300v18/platform/libplat/include -I/ak3918ev300v18/platform/libapp/../libplat/include_inner -I/ak3918ev300v18/platform/libmpi/include -I/ak3918ev300v18/platform/libapp/include -c ak_rtsp_demo.c -o ak_rtsp_demo.o
arm-anykav200-linux-uclibcgnueabi-g++ ak_rtsp_demo.o -L/ak3918ev300v18/platform/libplat/lib -L/ak3918ev300v18/platform/libmpi/lib -L/ak3918ev300v18/platform/libapp/lib -lakuio -lakv_encode -lakispsdk -lplat_common -lplat_thread -lplat_vi -lplat_drv -lplat_vpss -lplat_ipcsrv -lplat_venc_cb -lmpi_venc -lapp_rtsp -lapp_net -lrt -lpthread -ldl -Wl,-rpath=/mnt -rdynamic -Xlinker "-("  -Xlinker "-)" -o ak_rtsp_demo
```
