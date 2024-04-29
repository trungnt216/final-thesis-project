# piMeter - a SmartMeter for Raspberry Pi - Final Thesis Project

This repo contains the software for the [piMeter_hardware](https://github.com/digitaldex/piMeter_hardware) project.

## Tech Stack
```
 QT-Python(UI)
 C++(Firmware)
 PostgresDB
 Python
```

## Setup Raspberry Pi

### Enable SPI

```
sudo raspi-config
-> Interface Option
-> Enable SPI
```

### Install Dependencies

```
// Install bcm2835 Library
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.52.tar.gz
tar zxvf bcm2835-1.52.tar.gz
./configure
make
sudo make check
sudo make install
```

### Build piMeter

```
g++ main.cpp spiComm.cpp -o piMeter -lbcm2835
```

### Run piMeter

```
// bcm2835 Lib needs root
sudo ./piMeter &
```

## Run cronjob service

1.  Install prerequisites packages

```
  pip install psycopg2
```

2. Run service

```
 py readfile-service.py
```
