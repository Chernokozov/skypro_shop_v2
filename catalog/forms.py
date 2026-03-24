from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта',
        'биржа', 'дешево', 'бесплатно',
        'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        """Стилизация формы"""
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'is_published':
                # Чекбокс
                field.widget.attrs['class'] = 'form-check-input'
            elif field_name != 'image':
                # Текстовые поля, select и т.д.
                field.widget.attrs['class'] = 'form-control'

            # Дополнительные атрибуты
            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Введите название продукта'
            elif field_name == 'price':
                field.widget.attrs['placeholder'] = '0.00'
                field.widget.attrs['step'] = '0.01'
                field.widget.attrs['min'] = '0'

        # Поле image (если есть)
        if 'image' in self.fields:
            self.fields['image'].widget.attrs['class'] = 'form-control'
            self.fields['image'].widget.attrs['accept'] = 'image/jpeg,image/png'

    def _check_forbidden_words(self, text, field_name):
        """Вспомогательный метод для проверки запрещенных слов"""
        for word in self.FORBIDDEN_WORDS:
            if word in text:
                raise ValidationError(f'{field_name.capitalize()} содержит запрещенное слово: "{word}"')
        return text

    def clean_name(self):
        """Валидация названия на запрещенные слова"""
        name = self.cleaned_data.get('name', '')
        if name:  # Проверяем только если есть текст
            return self._check_forbidden_words(name.lower(), 'названии')
        return name

    def clean_description(self):
        """Валидация описания на запрещенные слова"""
        description = self.cleaned_data.get('description', '')
        if description:  # Проверяем только если есть текст
            return self._check_forbidden_words(description.lower(), 'описании')
        return description

    def clean_price(self):
        """Валидация цены"""
        price = self.cleaned_data['price']
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        """Валидация изображения (дополнительное задание)"""
        image = self.cleaned_data.get('image')

        if not image:
            return image

        allowed_formats = ['image/jpeg', 'image/png', 'image/jpg']
        if image.content_type not in allowed_formats:
            raise ValidationError('Допустимые форматы изображений: JPEG, PNG')

        if image.size > 5 * 1024 * 1024:
            raise ValidationError('Размер изображения не должен превышать 5 МБ')

        return image


class StyleFormMixin:
    pass