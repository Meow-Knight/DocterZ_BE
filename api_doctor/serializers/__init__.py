from .Hospital import HospitalSerializer, HospitalCUDSerializer, HospitalWithNameSerializer
from .Clinic import ClinicSerializer, ClinicCUDSerializer, ClinicWithNameSerializer
from .Department import DepartmentSerializer
from .Doctor import DoctorSerializer, RegisterDoctorSerializer, GeneralInfoDoctorSerializer, \
    EditDoctorProfileSerializer, ItemDoctorSerializer, ListDoctorSerializer, AdminEditDoctorSerializer, \
    EditOwnDoctorProfileSerializer
from .Review import ReviewSerializer, ShowReviewByDoctorSerializer
