import logging

from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from metering_billing.models import APIToken, Organization
from metering_billing.permissions import HasUserAPIKey
from metering_billing.utils import now_utc
from rest_framework.authentication import BaseAuthentication

logger = logging.getLogger("django.server")


class OrganizationInsertMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if request.user.is_authenticated:
                organization = request.user.organization
            else:
                api_key_checker = HasUserAPIKey()
                api_key = api_key_checker.get_key(request)
                if api_key is None:
                    organization = None
                else:
                    prefix, _, _ = api_key.partition(".")
                    organization_pk = cache.get(prefix)
                    if not organization_pk:
                        try:
                            api_token = APIToken.objects.get_from_key(api_key)
                            organization = api_token.organization
                            organization_pk = api_token.organization.pk
                            expiry_date = api_token.expiry_date
                            timeout = (
                                60 * 60 * 24
                                if expiry_date is None
                                else (expiry_date - now_utc()).total_seconds()
                            )
                            cache.set(prefix, organization_pk, timeout)
                        except:
                            organization = None
                    else:
                        organization = Organization.objects.get(pk=organization_pk)
            logger.debug(
                f"OrganizationInsertMiddleware: {organization}, {request.user}"
            )
            request.organization = organization
        except Exception as e:
            logger.error(f"OrganizationInsertMiddleware: {e}")
            pass
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        return response
