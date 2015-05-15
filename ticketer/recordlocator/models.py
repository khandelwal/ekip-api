from django.db import models

from localflavor.us.models import USZipCodeField


class Ticket(models.Model):
    """ This is a ticket. """

    record_locator = models.CharField(max_length=10, primary_key=True)
    timestamp_generated = models.DateTimeField(auto_now_add=True)
    origin_zipcode = USZipCodeField(max_length=5)
