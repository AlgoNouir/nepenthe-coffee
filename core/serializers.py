
from drf_extra_fields.fields import Base64FileField as B64F


class Base64FileField(B64F):
    ALLOWED_TYPES = ["all"]

    def get_file_extension(self, *args, **kwargs):
        return "all"