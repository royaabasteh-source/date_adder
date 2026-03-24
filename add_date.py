import os
from datetime import date

# مسیر پوشه‌ای که فایل‌ها هستند
folder_path = "D:\xamk\courses\Tasks\date_adder\test_files"

# گرفتن تاریخ امروز
today = date.today().strftime("%Y-%m-%d")

# رفتن روی هر فایل در پوشه
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        new_name = f"{today}_{filename}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

print("All files have been renamed!")
