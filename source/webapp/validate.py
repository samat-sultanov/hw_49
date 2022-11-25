from django.core.exceptions import ValidationError


def validate_summary(value):
    if len(value) > 20:
        raise ValidationError('Заголовок не должен быть больше 20 символов!')
    return value
