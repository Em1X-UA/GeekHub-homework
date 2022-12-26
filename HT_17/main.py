"""
Автоматизувати процес замовлення робота за допомогою Selenium
1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv"
Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта,
не зберігайте файл локально.
2. Зайдіть на сайт "https://robotsparebinindustries.com/"
3. Перейдіть у вкладку "Order your robot"
4. Для кожного замовлення з файлу реалізуйте наступне:
    - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
    - оберіть/заповніть відповідні поля для замовлення
    - натисніть кнопку Preview та збережіть зображення отриманого робота.
    Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
    - натисніть кнопку Order та збережіть номер чеку.
    Увага! Інколи сервер тупить і видає помилку, але повторне натискання
    кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
    - переіменуйте отримане зображення у формат <номер чеку>_robot.
    Покладіть зображення в директорію output
    (яка має створюватися/очищатися під час запуску скрипта).
    - замовте наступного робота (шляхом натискання відповідної кнопки)
5. Для загального розуміння можна переглянути відео
https://www.youtube.com/watch?v=0uvexJyJwxA&ab_channel=Robocorp
** Додаткове завдання (необов'язково)
    - окрім збереження номеру чеку збережіть також HTML-код всього чеку
    - збережіть отриманий код в PDF файл
    - додайте до цього файлу отримане зображення робота
    (бажано на одній сторінці, але не принципово)
    - збережіть отриманий PDF файл у форматі <номер чеку>_robot
    в директорію output. Окремо зображення робота зберігати не потрібно.
"""


from modules.buyer_module import RobotSpareBinBuyer
from modules.order_reader import OrderReader

ORDERS_URL = 'https://robotsparebinindustries.com/orders.csv'


def main():
    with RobotSpareBinBuyer() as buyer:
        buyer.open_order_page()
        buyer.output_folder()
        for order in OrderReader(csv_url=ORDERS_URL).get_orders():
            buyer.order_placer(head=order['Head'],
                               body=order['Body'],
                               legs=order['Legs'],
                               address=order['Address'])
            buyer.order_another()


if __name__ == '__main__':
    main()
