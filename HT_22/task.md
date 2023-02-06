# HT #22

## Базуючись на попередній ДЗ, реалізувати наступний функціонал:
1. Додати Django REST Framework в свій магазин для всих своїх моделей.
2. Додавання до корзини, зміну кількості, очищення корзини або видалення одного продукта з неї зробити з використанням ajax запросів.

### Корисні посилання:
* https://www.django-rest-framework.org/
* https://www.geeksforgeeks.org/how-to-make-ajax-call-from-javascript/
* https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started
#### Уточнення по моделям:
* Модель категорії - тільки ListView
* Модель Продукта - ListView + Update / Delete, додати валідацію на апдейт / деліт продукта - його може зробити тільки суперюзер. (authentication_classes = (authentication.SessionAuthentication, ) )
#### Форма для ДЗ:
* https://forms.gle/ht8xLBemEAEeaCQj8