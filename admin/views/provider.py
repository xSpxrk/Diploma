from flask_admin.contrib.sqla import ModelView

from admin.views.offer import OfferInlineAdmin
from backend.app.models import Offer


class ProviderView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_list = ('name', 'email', 'phone_number')

    inline_models = (OfferInlineAdmin(Offer),)
