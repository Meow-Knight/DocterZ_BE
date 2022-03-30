import cloudinary
import cloudinary.api
import cloudinary.uploader

from dotenv import load_dotenv
from rest_framework.exceptions import ValidationError

load_dotenv()


class CloudinaryService:
    @classmethod
    def upload_image(cls, image, folder_name):
        return cloudinary.uploader.upload(image, folder=folder_name)

    @classmethod
    def delete_image(cls, link, folder_name):
        if link:
            if not folder_name:
                raise ValidationError({"error": "ENV not loaded"})
            pub_id = folder_name + link.split("/")[-1].split(".")[0]
            res = cloudinary.uploader.destroy(pub_id, folder=folder_name)
            if res['result'] == "ok":
                return True
            return False
        return True
