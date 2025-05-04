from typing import Any

from django.db import models 
from django.utils.translation import gettext_lazy as _

class StatusEnum(models.TextChoices):
    

    increase: Any = "INCREASE", _("Increase")
    premium: Any = "DECREASE ", _("Decrease")
    
class StatusOrderEnum(models.TextChoices):
    
    pending: Any  ='pending', _("En attente"),
    in_progress: Any = "In_progress",_("En cours")  
    completed : Any = "Completed" , _("Terminée") 
    canceled : Any = "Canceled" , _("Annulée")
        
        
    
    
    