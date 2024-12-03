from typing import Any

from django.db import models
from django.utils.translation import gettext_lazy as _

class StatusEnum(models.TextChoices):
    

    increase: Any = "INCREASE", _("Increase")
    premium: Any = "DECREASE ", _("Decrease")
    
    
    