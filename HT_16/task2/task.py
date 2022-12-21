"""
2. Викорисовуючи Scrapy, написати скрипт, який буде приймати на вхід назву
та ID категорії (у форматі назва/id/) із сайту https://rozetka.com.ua і буде
збирати всі товари із цієї категорії, збирати по ним всі можливі дані
(бренд, категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл
(наприклад, якщо передана категорія mobile-phones/c80003/,
то файл буде називатися c80003_products.csv)
"""


from scrapy.crawler import CrawlerProcess

from rozetka_categories.spiders.rozetka import RozetkaSpider


CATEGORY = 'digital_pianos/c284868/'


def main():
    category_id = CATEGORY.split('/')[1]
    process = CrawlerProcess(settings={'FEEDS': {f'{category_id}_products.csv':
        {
            'format': 'csv',
            'header': True
        }
    }})

    process.crawl(RozetkaSpider, category=CATEGORY)
    process.start()


if __name__ == '__main__':
    main()
