from django.db import models
from utils import models as project_mixins
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings

AUTH_USER_MODEL = get_user_model()
DEFAULT_CURRENCY = settings.DEFAULT_CURRENCY


class Order(project_mixins.ProjectBaseMixin):
    """
    The main order model
    """
    number = models.CharField(
        _("Order number"), max_length=128, db_index=True, unique=True)

    # user = models.ForeignKey(
    #     AUTH_USER_MODEL, related_name='orders', null=True, blank=True,
    #     verbose_name=_("User"), on_delete=models.SET_NULL)

    currency = models.CharField(
        _("Currency"), max_length=12, default=DEFAULT_CURRENCY)

    # Use this field to indicate that an order is on hold / awaiting payment
    status = models.CharField(_("Status"), max_length=100, blank=True)

    total_incl_tax = models.DecimalField(
        _("Order total (inc. tax)"), decimal_places=2, max_digits=12)
    total_excl_tax = models.DecimalField(
        _("Order total (excl. tax)"), decimal_places=2, max_digits=12)

    # Shipping charges
    shipping_incl_tax = models.DecimalField(
        _("Shipping charge (inc. tax)"), decimal_places=2, max_digits=12,
        default=0)
    shipping_excl_tax = models.DecimalField(
        _("Shipping charge (excl. tax)"), decimal_places=2, max_digits=12,
        default=0)

