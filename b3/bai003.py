import pandas as pd

class Money_Time:
    def __init__(self):
        self.gia_tien = {
            "Xe đạp": 2000,
            "Xe máy": 5000,
            "Xe điện": 3500,
            "Ô tô": 10000
        }

    def cap_nhat_gia(self, loai_xe, gia_moi):
        self.gia_tien[loai_xe] = gia_moi

    def lay_gia(self, loai_xe):
        return self.gia_tien.get(loai_xe, 0)


class Info_Xe:
    def __init__(self, loai_xe, chu_xe, thoi_gian_gui, bien_so=""):
        self.loai_xe = loai_xe
        self.chu_xe = chu_xe
        self.thoi_gian_gui = thoi_gian_gui
        self.bien_so = bien_so

    def tinh_tien_gui(self, money_time: Money_Time):
        don_gia = money_time.lay_gia(self.loai_xe)
        return don_gia * self.thoi_gian_gui


class QuanLyBaiXe:
    def __init__(self):
        self.ds_xe = []
        self.money_time = Money_Time()

    def them_xe(self, xe: Info_Xe):
        self.ds_xe.append(xe)

    def xoa_xe(self, bien_so):
        self.ds_xe = [xe for xe in self.ds_xe if xe.bien_so != bien_so]

    def sua_xe(self, bien_so, loai_xe=None, chu_xe=None, thoi_gian_gui=None):
        for xe in self.ds_xe:
            if xe.bien_so == bien_so:
                if loai_xe: xe.loai_xe = loai_xe
                if chu_xe: xe.chu_xe = chu_xe
                if thoi_gian_gui is not None: xe.thoi_gian_gui = thoi_gian_gui
                return

    def xuat_ds_gui_tren_20k(self):
        return [
            {
                "Chủ xe": xe.chu_xe,
                "Loại xe": xe.loai_xe,
                "Biển số": xe.bien_so,
                "Thời gian gửi": xe.thoi_gian_gui,
                "Tiền gửi": xe.tinh_tien_gui(self.money_time)
            }
            for xe in self.ds_xe
            if xe.tinh_tien_gui(self.money_time) > 20000
        ]

    def xuat_excel(self, filename="guixe.xlsx"):
        data = [{
            "Chủ xe": xe.chu_xe,
            "Loại xe": xe.loai_xe,
            "Biển số": xe.bien_so,
            "Thời gian gửi": xe.thoi_gian_gui,
            "Tiền gửi": xe.tinh_tien_gui(self.money_time)
        } for xe in self.ds_xe]

        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Dữ liệu đã được ghi vào 'guixe.xlsx'")



# demo 
ql_bai_xe = QuanLyBaiXe()

# Thêm một vài xe
ql_bai_xe.them_xe(Info_Xe("Xe máy", "Nguyễn Nhung", 3, "59A1-123.45"))
ql_bai_xe.them_xe(Info_Xe("Xe đạp", "Trần Thị Bich", 5))
ql_bai_xe.them_xe(Info_Xe("Ô tô", "Lê Văn Cong", 2, "51G-678.90"))
ql_bai_xe.them_xe(Info_Xe("Xe điện", "Phạm Văn Deeptri", 7))

# Sửa thông tin xe
ql_bai_xe.sua_xe("51G-678.90", thoi_gian_gui=3)

# Xuất danh sách xe có tiền gửi trên 20k
ds_tren_20k = ql_bai_xe.xuat_ds_gui_tren_20k()
print("Danh sách người gửi xe trên 20k:")
for xe in ds_tren_20k:
    print(xe)

# Xuất toàn bộ danh sách ra Excel
ql_bai_xe.xuat_excel()
