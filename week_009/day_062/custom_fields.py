from wtforms import Field
from wtforms.widgets import Input


class RatingWidget(Input):
    input_type = 'number'

    def __call__(self, field, **settings):
        settings.setdefault('type', 'number')
        settings.setdefault('step', '1')
        settings['min'] = '0'
        settings['max'] = '5'
        return super(RatingWidget, self).__call__(field, **settings)


class RatingField(Field):

    widget = RatingWidget()

    def __init__(self, label='', validators=None, **kwargs):
        super(RatingField, self).__init__(label, validators, **kwargs)

    def _value(self):
        return str(self.data) if self.data else '0'

    def process_formdata(self, valuelist):
        self.data = int(valuelist[0]) if valuelist else 0

    def process_data(self, value):
        self.data = 0 if value is None else int(value)

    def pre_validate(self, form):
        if not (0 <= self.data <= 5):
            raise ValueError('Invalid rating')
