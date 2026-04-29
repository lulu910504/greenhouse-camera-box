from PIL import Image
import glob
# glob.glob 回傳檔名清單
# sorted 檔名
frames = [Image.open(img) for img in sorted(glob.glob("daily_photos\*.jpg"))]
frames[4].save('0102to0129.gif',# 以第一張圖片為base 存成gif
               save_all=True, # 啟用儲存多張影格
               append_images=frames[5:], # 後續影格（第 2 張到最後一張）
               duration =500,  # 每一張影格顯示時間（單位：毫秒，1000ms = 1 秒）
               loop =0)  # GIF 播放次數，0 代表無限循環
