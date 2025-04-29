import pandas as pd
import numpy as np

# Đường dẫn tới Google Sheets (dạng Excel)
url = "https://docs.google.com/spreadsheets/d/1BnOzoEG0s6c8MpiUANZ0_pawXNHqdkid/export?format=xlsx"

# Đọc dữ liệu từ Google Sheets
df = pd.read_excel(url)

# Đảm bảo các cột liên quan là số (nếu có dữ liệu rỗng hoặc sai định dạng thì sẽ chuyển thành NaN)
df["vpv2"] = pd.to_numeric(df["vpv2"], errors="coerce")
df["pDisCharge"] = pd.to_numeric(df["pDisCharge"], errors="coerce")
df["prec"] = pd.to_numeric(df["prec"], errors="coerce")
df["vBus1"] = pd.to_numeric(df["vBus1"], errors="coerce")
df["vBus2"] = pd.to_numeric(df["vBus2"], errors="coerce")

# Lọc dữ liệu theo điều kiện:
filtered_df = df[
    (df["vpv2"] % 2 == 0) &        # vpv2 là chẵn
    (df["pDisCharge"] % 2 == 0) &  # pDisCharge là chẵn
    (df["prec"] % 2 == 1)          # prec là lẻ
]

# Tạo cột Sum_vBUS = vBus1 + vBus2
filtered_df["Sum_vBUS"] = filtered_df["vBus1"] + filtered_df["vBus2"]

# Lưu kết quả vào file CSV mới
filtered_df.to_csv("dulieu.csv", index=False, encoding="utf-8-sig")

print("Dữ liệu đã được lọc và lưu vào 'dulieu.csv'")
