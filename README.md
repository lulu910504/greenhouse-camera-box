# Greenhouse Camera System

<img width="888" src="https://github.com/user-attachments/assets/cae8f1d8-9edc-45e6-a767-127bc8aae625" />
<img width="1108" src="https://github.com/user-attachments/assets/77e531ca-5ce0-4263-9bb0-76e7420ed961" />

Raspberry Pi–based camera system for automated plant monitoring with remote access and API control.



## Overview
<img width="611" height="301" alt="image" src="https://github.com/user-attachments/assets/d0f021a0-8cba-40a6-acb1-315f4bdbcc66" />

This project implements a camera monitoring system designed for greenhouse environments.  
Images are captured periodically and can also be triggered remotely via API.  
All images are stored locally and served through a web interface.



## System Architecture

Camera → Raspberry Pi → FastAPI → Local Storage → Remote Access (Tailscale)


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

Edit cron job:

```bash
crontab -e

0 8 * * * python3 scripts/daily_capture.py
```
Run Server

Start FastAPI server:
```bash 
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```
Auto Start (systemd)

Create service file:
```bash
sudo nano /etc/systemd/system/daily_camera.service
```
daily_camera.service
```bash
[Unit]
Description=Camera API
After=network-online.target

[Service]
User=pi
WorkingDirectory=/home/pi/project
ExecStart=/usr/bin/python3 -m uvicorn backend.app:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable daily_camera.service
sudo systemctl start daily_camera.service
```
