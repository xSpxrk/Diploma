from flask_admin.contrib.sqla import ModelView

from admin.views.order import OrderInlineAdmin
from backend.app.models import Order


class CustomerView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_list = ('name', 'email', 'phone_number')

    inline_models = (OrderInlineAdmin(Order),)
