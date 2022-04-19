# Pi-Thermo
Digital Thermometer made using Raspberry Pi 4B

This repository contains the python code for a digital thermometer made using AdaFruit DHT11 temperature and humidity sensor with Raspberry Pi 4B and a servo motor.

DHT11 python library was taken from https://github.com/binaryupdates/dht11-raspberrypi.git

## How It Works
Raspberry Pi captures the data come from the DHT11 sensor and read the measurements. Then it checks whether the measurement is valid. If its valid, then it rotates the servo motor according to the specified angle (which was given my duty cycle). If not, the measurement is ignored.

## Prerequisites
- Raspberry Pi 4B
- AdaFruit DHT11 Temperature and Humidity Sensor

## Setup
- Connect DHT11 sensor to GPIO 21
- Connect Servo motor to GPIO 17

*Disclaimer: This code was developed as a fulfillment for IoT for Big Data Analysis module in BSc. (Hons) in IT specializing in Data Science degree program of Sri Lanka Institute of Information Technology.*

