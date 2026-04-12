#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
from datetime import datetime
from PIL import Image
from picamera2 import Picamera2
from libcamera import controls  # for AfModeEnum

APP_ROOT = os.path.dirname(__file__)
DAILY_DIR = os.path.join(APP_ROOT, "static", "daily_photos")
os.makedirs(DAILY_DIR, exist_ok=True)

CAMERA_SIZE = (4608, 2592) 
#CAMERA_SIZE = (2304, 1296)    
ROTATE_DEG = 0               

def main():
    cam = Picamera2()
    cfg = cam.create_still_configuration({"size": CAMERA_SIZE})
    cam.configure(cfg)

    cam.start()
    time.sleep(1.0)  

    try:
        cam.set_controls({
            "AfMode":    controls.AfModeEnum.Auto,    
            "AfSpeed":   controls.AfSpeedEnum.Normal,   

            "AfMetering": controls.AfMeteringEnum.CentreWeighted,
        })
        cam.autofocus_cycle()      
        time.sleep(0.6)     
    except Exception as e:
        print("[AF ERR]", e)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    filepath = os.path.join(DAILY_DIR, filename)

    cam.capture_file(filepath)
    cam.stop()

    if ROTATE_DEG != 0:
        try:
            with Image.open(filepath) as im:
                im = im.rotate(ROTATE_DEG, expand=True)
                im.save(filepath, "JPEG", quality=92, optimize=True, progressive=True)
        except Exception as e:
            print("[IMG ROTATE ERR]", e)

    print("[OK] saved:", filepath)

if __name__ == "__main__":
    main()
ZE = (2304, 1296)    
#ROTATE_DEG = -90              # 不需旋轉就改成 0
ROTATE_DEG = 0 
def main():
    cam = Picamera2()
    cfg = cam.create_still_configuration({"size": CAMERA_SIZE})
    cam.configure(cfg)

    cam.set_controls({"AfMode": controls.AfModeEnum.Continuous})

    cam.start()
    time.sleep(1.0)  

 
    try:
        cam.autofocus_cycle()
    except Exception:
        pass

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    filepath = os.path.join(DAILY_DIR, filename)

    cam.capture_file(filepath)
    cam.stop()


    if ROTATE_DEG != 0:
        try:
            with Image.open(filepath) as im:
                im = im.rotate(ROTATE_DEG, expand=True)
                im.save(filepath, "JPEG", quality=92, optimize=True, progressive=True)
        except Exception as e:
            print("[IMG ROTATE ERR]", e)

    print("[OK] saved:", filepath)

if __name__ == "__main__":
    main()

