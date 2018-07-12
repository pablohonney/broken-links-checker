Usage
-------------

Configure urls to parse in config.py. Then, run:

    scrapy runspider broken_links_spider.py -o output.json
    scrapy runspider broken_links_spider.py -o output.json -a domains=help.github.com,github.com -a urls=https://help.github.com

Then check 404 items in the output.json file. 