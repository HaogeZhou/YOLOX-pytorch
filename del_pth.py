
import os
folder_path = r'logs_lr_quarter' # 文件路径

pth_path   = os.listdir(folder_path)

for i in pth_path:
    if i.endswith(".pth"):
        if int(i[2:5]) == 1:
            continue
        if int(i[2:5]) % 10 != 0:
            os.remove(os.path.join(folder_path, i)) # 则删除

