# -*- coding: utf-8 -*-

from urllib.parse import unquote
from typing import Optional, Any, Union

from django import template


register = template.Library()


@register.filter
def slice_to(value, count_chars: int) -> str:
    """ Обрезаем значени до указанного кол-ва символов """

    return value[:count_chars+1]


@register.filter
def get_file_name(value) -> str:
    """ Получаем имя файла из относительного местоположения его на сервере """

    # Example value /media/media/kazanAccounts_4n7XZl2.txt
    name = value.split('/')[-1] # kazanAccounts_4n7XZl2.txt
    name = name.split("_") # ['kazanAccounts', '4n7XZl2.txt']
    file_type = name[-1].split(".")[-1] # txt

    final_name = f"{name[0]}.{file_type}"
    final_name = unquote(final_name)

    return final_name # kazanAccounts.txt


@register.filter
def get_item(dictionary, key) -> Optional[Any]:
    """ Получаем значение словаря по его ключу """
    return dictionary.get(key)


@register.filter
def join(value: list) -> str:
    """ Соединяем список значений через запятую """
    return ", ".join(value)


@register.filter
def is_image_file(
        file_path: Union[str, None]=None,
        file_name: Union[str, None]=None,
    ) -> bool:
    """ Проверяет является ли файл картинкой """

    if file_path:
        file_name = get_file_name(file_path)

    if not file_name:
        return False

    file_type = file_name.split(".")[-1]

    if file_type in ('jpg', 'jpeg', 'png', 'gif'):
        return True
    else:
        return False
