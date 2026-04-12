# Greenhouse Camera System
<img width="888" height="666" alt="image" src="https://github.com/user-attachments/assets/cae8f1d8-9edc-45e6-a767-127bc8aae625" />

Raspberry Pi–based camera system for automated plant monitoring with remote access and API control.

## Overview

This project implements a camera monitoring system designed for greenhouse environments.  
Images are captured periodically and can also be triggered remotely via API.  
All images are stored locally and served through a web interface.

## System Architecture

Camera → Raspberry Pi → FastAPI → Local Storage → Dashboard / Remote Access

## Hardware

- Raspberry Pi 5
- Camera Module 3 Wide
- Raspberry Pi 5 CUBE Pi Case https://shop.playrobot.com/products/ceo0136
## Software Stack

- Python
- FastAPI
- Picamera2
- Pillow

## Features

- Scheduled image capture (cron)
- Manual capture via API
- Autofocus before each capture
- Local image storage
- REST API for remote control
- Dashboard integration
- Remote access via Tailscale

## Project Structure
