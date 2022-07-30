#!/bin/sh
TARGET_DIR=/mnt/data_ext/pkt/$(date +%Y-%m-%d)
FILE_SIZE_MB=100
ROTATE_AFTER_SEC=1800
echo "Will capture to $TARGET_DIR/ALL"
test -d $TARGET_DIR || mkdir -vp $TARGET_DIR
cd "$TARGET_DIR"
exec tcpdump -w ALL -C $FILE_SIZE_MB -G $ROTATE_AFTER_SEC -K -n
