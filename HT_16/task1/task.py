"""
1. Використовуючи Scrapy, заходите на
"https://chrome.google.com/webstore/sitemap", переходите на кожен лінк
з тегів <loc>, з кожного лінка берете посилання на сторінки екстеншинів,
парсите їх і зберігаєте в CSV файл ID, назву та короткий опис кожного
екстеншена (пошукайте уважно де його можна взяти).

Наприклад:
“aapbdbdomjkkjkaonfhkkikfgjllcleb”,
“Google Translate”,
“View translations easily as you browse the web. By the Google Translate team.”
"""


from scrapy.crawler import CrawlerProcess

from task1.spiders.chrome_webstore_spider import ChromeWebstoreSpider


def main():
    process = CrawlerProcess(settings={'FEEDS': {'chrome_webstore_extensions.csv':
        {
            'format': 'csv',
            'header': True
        }
    }})

    process.crawl(ChromeWebstoreSpider)
    process.start()


if __name__ == '__main__':
    main()
