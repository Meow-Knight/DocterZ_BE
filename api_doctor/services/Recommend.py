from django.db import transaction
from django.db.models import Avg

from api_doctor.models import Review, Doctor
from api_doctor.serializers import ItemDoctorSerializer


class RecommendService:
    @classmethod
    @transaction.atomic
    def get_doctor_ids(cls, reviews):
        ids = []
        for review in reviews:
            ids.append(review['doctor'])
        return ids

    @classmethod
    @transaction.atomic
    def recommend(cls, request):
        len_doctors = int(request.query_params.get('len', '3'))
        reviews = Review.objects.values('doctor').annotate(rateAVG=Avg('rate')).order_by('-rateAVG')[:len_doctors]
        if reviews.exists():
            doctor_ids = cls.get_doctor_ids(reviews)
            doctors = Doctor.objects.filter(pk__in=doctor_ids)
            if doctors.exists():
                doctors = ItemDoctorSerializer(doctors, many=True)
                return doctors.data
