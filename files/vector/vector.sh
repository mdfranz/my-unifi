#!/bin/ash
cd /mnt/data_ext/vector
killall -9 vector || true
nohup ./bin/vector -w="./vector.d/*.toml" --config-toml="./vector.d/*.toml" >/dev/null &
