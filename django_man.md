{% extends 'template.html' %} - использование(вставка) другого html-шаблона в html-шаблоне  
django.setup() - загрузка настроек проекта из *settings.py*. Например для работы в python-shell с командой *django*  
export DJANGO_SETTINGS_MODULE=films_site.settings - в коммандной строке для использования django в ней.  

get_list_or_404() и get_object_or_404() - использовать в представлениях вместо Model.filter() и Model.get(). Получает QueriSet[] или вызывает исключение HTTP404, если нет объектов.

