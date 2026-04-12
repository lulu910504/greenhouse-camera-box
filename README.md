# Greenhouse Camera System

<img width="888" src="https://github.com/user-attachments/assets/cae8f1d8-9edc-45e6-a767-127bc8aae625" />
<img width="1108" src="https://github.com/user-attachments/assets/77e531ca-5ce0-4263-9bb0-76e7420ed961" />

Raspberry Pi–based camera system for automated plant monitoring with remote access and API control.



## Overview

This project implements a camera monitoring system designed for greenhouse environments.  
Images are captured periodically and can also be triggered remotely via API.  
All images are stored locally and served through a web interface.



## System Architecture

Camera → Raspberry Pi → FastAPI → Local Storage → Dashboard → Remote Access (Tailscale)


## Hardware

- Raspberry Pi 5  
- Camera Module 3 Wide  
- Raspberry Pi 5 CUBE Pi Case  
  https://shop.playrobot.com/products/ceo0136  


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


## API Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| POST | /capture | Capture image manually |
| POST | /capture_daily | Trigger scheduled capture |
| GET  | /latest_daily_photo | Get latest image |
| POST | /ping | System health check |



## Tailscale (Remote Access)

<img width="1253" src="https://github.com/user-attachments/assets/42483bf8-4207-4dc2-8fbd-d7eda2df4024" />

Secure remote access without port forwarding.


## Automation (Cron)

```bash
crontab -e

