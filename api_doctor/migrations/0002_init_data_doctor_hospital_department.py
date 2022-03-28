import os

from django.contrib.auth.hashers import make_password
from django.db import migrations

def initial_data(apps, schema_editor):
    ward_model = apps.get_model("api_address", "Ward")
    clinic_model = apps.get_model("api_doctor", 'Clinic')
    department_model = apps.get_model("api_doctor", "Department")
    hospital_model = apps.get_model("api_doctor", "Hospital")
    doctor_model = apps.get_model("api_doctor", "Doctor")
    account_model = apps.get_model("api_account", "Account")
    role_model = apps.get_model("api_account", "Role")

    doctor_role = role_model.objects.filter(name="DOCTOR").first()

    hospitals = [
        hospital_model(name="Bệnh viện Đa khoa Quốc tế Vinmec Đà Nẵng",
                       detail_address="30 Tháng 4, Hoà Cường Bắc, Cẩm Lệ, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Hòa Cường Bắc").first()),
        hospital_model(name="Bệnh viện Đà Nẵng",
                       detail_address="124 Hải Phòng, Thạch Thang, Hải Châu, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Thạch Thang").first()),
        hospital_model(name="Bệnh viện Đa khoa Gia Đình Đà Nẵng",
                       detail_address="73 Nguyễn Hữu Thọ, Hòa Thuận Nam, Hải Châu, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Hòa Thuận Nam").first()),
        hospital_model(name="Bệnh viện Hoàn Mỹ Đà Nẵng",
                       detail_address="291 Nguyễn Văn Linh, Thạc Gián, Thanh Khê, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Thạc Gián").first()),
        hospital_model(name="Bệnh Viện Tâm Trí",
                       detail_address="64 Cách Mạng Tháng 8, Khuê Trung, Cẩm Lệ, Đà Nẵng, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Khuê Trung").first()),
        hospital_model(name="Bệnh viện Đa khoa Ngũ Hành Sơn",
                       detail_address="582 Lê Văn Hiến, Hoà Hải, Ngũ Hành Sơn, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Hoà Hải").first()),
        hospital_model(name="Thiện Nhân Hospital",
                       detail_address="278 Đống Đa, Thanh Bình, Hải Châu, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Thanh Bình").first()),
        hospital_model(name="Bệnh viện Phục hồi chức năng TP Đà Nẵng",
                       detail_address="Đinh Gia Trinh, Hoà Châu, Cẩm Lệ, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Hoà Châu").first()),
        hospital_model(name="Cổng Khám bệnh BV Ung bướu Đà Nẵng",
                       detail_address="Hoàng Trung Thông, Hoà Minh, Liên Chiểu, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Hoà Minh").first()),
        hospital_model(name="Bệnh viện Bình dân Đà Nẵng",
                       detail_address="Trần Cao Vân, Xuân Hà, Thanh Khê, Đà Nẵng 550000, Việt Nam",
                       ward=ward_model.objects.filter(name="Phường Xuân Hà").first()),
    ]

    hospitals = hospital_model.objects.bulk_create(hospitals)

    departments = [
        department_model(name="Gây mê - điều trị đau"),
        department_model(name="Răng - Hàm - Mặt"),
        department_model(name="Da liễu"),
        department_model(name="Phục hồi chức năng"),
        department_model(name="Hoạt động trị liệu"),
        department_model(name="Thẩm mỹ"),
        department_model(name="Phẫu thuật thẩm mỹ"),
        department_model(name="Tiêu hóa"),
        department_model(name="Ngoại Tim mạch"),
        department_model(name="Nội Hô hấp"),
        department_model(name="Ngoại Hô hấp"),
        department_model(name="Truyền nhiễm"),
        department_model(name="Phẫu Thuật chỉnh hình"),
        department_model(name="Tai - Mũi - Họng"),
        department_model(name="Nội Thận - Tiết niệu"),
        department_model(name="Ngoại Thận - Tiết niệu"),
        department_model(name="Ung bướu-Xạ trị"),
        department_model(name="Mắt"),
        department_model(name="Nam khoa"),
        department_model(name="Hỗ trợ sinh sản"),
        department_model(name="Nhi"),
        department_model(name="Nhi Thần kinh"),
        department_model(name="Nhi Ung bướu"),
        department_model(name="Nhi Truyền nhiễm"),
        department_model(name="Chẩn đoán hình ảnh"),
        department_model(name="Xét nghiệm vi sinh"),
        department_model(name="Ngoại Thần kinh"),
        department_model(name="Xét nghiệm"),
        department_model(name="Nhi Hô hấp"),
        department_model(name="Nhi Da liễu")
    ]

    departments = department_model.objects.bulk_create(departments)

    clinics = [
        clinic_model(name="Phòng Khám Đa Khoa Miền Trung",
                     detail_address="Tòa nhà Abtel Tower, 280 Nguyễn Hữu Thọ, Khuê Trung, Cẩm Lệ, Đà Nẵng, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Khuê Trung").first()),
        clinic_model(name="Phòng Khám Nam Khoa Đà Nẵng - 291.vn",
                     detail_address="291 Điện Biên Phủ, Hòa Khê, Thanh Khê, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hòa Khê").first()),
        clinic_model(name="Phòng khám Đa khoa Đông Phương",
                     detail_address="142 Triệu Nữ Vương, Hải Châu 2, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hải Châu").first()),
        clinic_model(name="Pasteur clinic Đà Nẵng",
                     detail_address="Lô 19 đường Nguyễn Tường P., Hoà Minh, Liên Chiểu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Minh").first()),
        clinic_model(name="Phòng khám Đa khoa An Phúc Đà Nẵng",
                     detail_address="143-145 Núi Thành, Hoà Cường Bắc, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Cường Bắc").first()),
        clinic_model(name="Phòng khám Đa khoa Hồng Phước",
                     detail_address="96 Triệu Nữ Vương, Hải Châu 2, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hải Châu").first()),
        clinic_model(name="phòng khám sản phụ khoa bác sĩ Trương Thị Chánhl",
                     detail_address="192 Nguyễn Hữu Thọ, Hoà Cường Bắc, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Cường Bắc").first()),
        clinic_model(name="Phòng khám Đa khoa Đông Phương",
                     detail_address="142 Triệu Nữ Vương, Hải Châu 2, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hải Châu").first()),
        clinic_model(name="Phòng khám Đa Khoa Hữu Nghị",
                     detail_address="291 Điện Biên Phủ, Hòa Khê, Thanh Khê, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hòa Khê").first()),
        clinic_model(name="Phòng khám Tim mạch Đà nẵng- XÉT NGHIỆM MÁU TỔNG QUÁT",
                     detail_address="108 Hải Phòng, Thạch Thang, Hải Châu, Đà Nẵng 103093, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Thạch Thang").first()),
    ]

    clinics = clinic_model.objects.bulk_create(clinics)

    accounts = [
        account_model(username="TranThanhTu", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="tranthanhtu@gmail.com"),
        account_model(username="VuongBaoNhac", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="vuongbaonhac@gmail.com"),
        account_model(username="LyUyenNhi", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="lyuyennhi@gmail.com"),
        account_model(username="TrieuNhaMong", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="trieunhamong@gmail.com"),
        account_model(username="BachTieuThuan", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="bachtieuthuan@gmail.com"),
        account_model(username="ChuTieuNha", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="chutieunha@gmail.com"),
        account_model(username="NguyenCongVinh", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="nguyencongvinh@gmail.com"),
        account_model(username="LeCaoVietHuy", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="lecaoviethuy@gmail.com"),
        account_model(username="NguyenMinhTien", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="nguyenminhtien@gmail.com"),
        account_model(username="NguyenThiLan", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="nguyenthilan@gmail.com"),
        account_model(username="VuNguyen", password=make_password(os.getenv('DEFAULT_CUSTOMER_PASSWORD')),
                      role=doctor_role, email="vunguyen@gmail.com"),
    ]

    accounts = account_model.objects.bulk_create(accounts)

    doctors = [
        doctor_model(full_name="Tran Thanh Tu", phone="0321569871", birthday="2000-02-01", gender="Nam",
                     email="tranthanhtu@gmail.com",
                     detail_address="291 Điện Biên Phủ, Hòa Khê, Thanh Khê, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hòa Khê").first(), hospital=hospitals[1],
                     department=departments[1], clinic=clinics[1], joined_date="2019-03-30", account=accounts[0]),
        doctor_model(full_name="Vuong Bao Nhac", phone="0021569874", birthday="2000-02-01", gender="Nam",
                     email="vuongbaonhac@gmail.com",
                     detail_address="73 Nguyễn Hữu Thọ, Hòa Thuận Nam, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hòa Thuận Nam").first(), hospital=hospitals[0],
                     department=departments[0], clinic=clinics[0], joined_date="2021-12-30", account=accounts[1]),
        doctor_model(full_name="Ly Uyen Nhi", phone="0321659874", birthday="2001-05-29", gender="Nu",
                     email="lyuuyennhi@gmail.com",
                     detail_address="142 Triệu Nữ Vương, Hải Châu 2, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hải Châu").first(), hospital=hospitals[2],
                     department=departments[2], clinic=clinics[2], joined_date="2022-01-15", account=accounts[2]),
        doctor_model(full_name="Trieu Nha Mong", phone="0325644519", birthday="2001-12-29", gender="Nu",
                     email="trieunhamong@gmail.com",
                     detail_address="Lô 19 đường Nguyễn Tường P., Hoà Minh, Liên Chiểu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Minh").first(), hospital=hospitals[3],
                     department=departments[3], clinic=clinics[3], joined_date="2022-02-15", account=accounts[3]),
        doctor_model(full_name="Trieu Nha Mong", phone="0325644519", birthday="2000-06-10", gender="Nu",
                     email="trieunhamong@gmail.com",
                     detail_address="Lô 19 đường Nguyễn Tường P., Hoà Minh, Liên Chiểu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Minh").first(), hospital=hospitals[3],
                     department=departments[3], clinic=clinics[3], joined_date="2022-02-15", account=accounts[3]),
        doctor_model(full_name="Bach Tieu Thuan", phone="0325569874", birthday="2000-03-29", gender="Nam",
                     email="bachtieuthuan@gmail.com",
                     detail_address="143-145 Núi Thành, Hoà Cường Bắc, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Cường Bắc").first(), hospital=hospitals[4],
                     department=departments[4], clinic=clinics[4], joined_date="2021-06-10", account=accounts[4]),
        doctor_model(full_name="Chu Tieu Nha", phone="0236996501", birthday="2002-01-12", gender="Nu",
                     email="chutieunha@gmail.com",
                     detail_address="96 Triệu Nữ Vương, Hải Châu 2, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hải Châu").first(), hospital=hospitals[5],
                     department=departments[5], clinic=clinics[5], joined_date="2022-05-20", account=accounts[5]),
        doctor_model(full_name="Nguyen Cong Vinh", phone="0327949281", birthday="2000-10-26", gender="Nam",
                     email="nguyencongvinh@gmail.com",
                     detail_address="192 Nguyễn Hữu Thọ, Hoà Cường Bắc, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hoà Cường Bắc").first(), hospital=hospitals[6],
                     department=departments[6], clinic=clinics[6], joined_date="2022-04-04", account=accounts[6]),
        doctor_model(full_name="Le Cao Viet Huy", phone="0325546225", birthday="2000-02-13", gender="Nam",
                     email="lecaoviethuy@gmail.com",
                     detail_address="142 Triệu Nữ Vương, Hải Châu 2, Hải Châu, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hải Châu").first(), hospital=hospitals[7],
                     department=departments[7], clinic=clinics[7], joined_date="2021-06-14", account=accounts[7]),
        doctor_model(full_name="Nguyen Minh Tien", phone="0366965212", birthday="2000-06-20", gender="Nam",
                     email="nguyenminhtien@gmail.com",
                     detail_address="291 Điện Biên Phủ, Hòa Khê, Thanh Khê, Đà Nẵng 550000, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Hòa Khê").first(), hospital=hospitals[8],
                     department=departments[8], clinic=clinics[8], joined_date="2022-03-01", account=accounts[8]),
        doctor_model(full_name="Nguyen Thi Lan", phone="0320125695", birthday="2000-05-12", gender="Nu",
                     email="nguyenthilan@gmail.com",
                     detail_address="108 Hải Phòng, Thạch Thang, Hải Châu, Đà Nẵng 103093, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Thạch Thang").first(), hospital=hospitals[9],
                     department=departments[9], clinic=clinics[9], joined_date="2021-06-14", account=accounts[9]),
        doctor_model(full_name="Vu Nguyen", phone="0332100256", birthday="2000-01-12", gender="Nam",
                     email="vunguyen@gmail.com",
                     detail_address="108 Hải Phòng, Thạch Thang, Hải Châu, Đà Nẵng 103093, Việt Nam",
                     ward=ward_model.objects.filter(name="Phường Thạch Thang").first(), hospital=hospitals[9],
                     department=departments[10], clinic=clinics[9], joined_date="2021-06-14", account=accounts[10]),
    ]

    doctor_model.objects.bulk_create(doctors)


def delete_all_data(apps, schema_editor):
    clinic_model = apps.get_model("api_doctor", 'Clinic')
    department_model = apps.get_model("api_doctor", "Department")
    hospital_model = apps.get_model("api_doctor", "Hospital")
    doctor_model = apps.get_model("api_doctor", "Doctor")
    account_model = apps.get_model("api_account", "Account")

    clinic_model.objects.all().delete()
    department_model.objects.all().delete()
    hospital_model.objects.all().delete()
    doctor_model.objects.all().delete()
    account_model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api_doctor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data, delete_all_data)
    ]
