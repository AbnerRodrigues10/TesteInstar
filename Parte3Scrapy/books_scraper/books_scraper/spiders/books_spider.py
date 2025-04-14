import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        livros = response.css('article.product_pod')

        for livro in livros:
            yield {
                'titulo': livro.css('h3 a::attr(title)').get(),
                'preco': livro.css('.price_color::text').get(),
                'imagem': response.urljoin(livro.css('img::attr(src)').get())
            }

        # Paginação
        proxima_pagina = response.css('li.next a::attr(href)').get()
        if proxima_pagina:
            yield response.follow(proxima_pagina, callback=self.parse)
