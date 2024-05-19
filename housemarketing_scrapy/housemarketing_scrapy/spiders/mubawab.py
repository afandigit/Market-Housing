import scrapy
from housemarketing_scrapy.items import MubawabItem
from scrapy.loader import ItemLoader

class MubawabSpider(scrapy.Spider):
    name = "mubawab"
    allowed_domains = ["www.mubawab.ma"]
    start_urls = ["https://www.mubawab.ma/fr/sc/appartements-a-vendre"]


    def parse(self, response):

        """
        We target the central 'div' element on the main page which contain the list of all the house advertisements.
        The 'div' element contain the 'id' attribut with value 'mainListing'.
        """
        main_container = response.css('[id="mainListing"]')

        # house_advertisement__link_to_details_page = main_container.css("ul.ulListing div.contentBox > h2.listingTit > a::attr(href)").getall()

        """
        Here, my goal is to grap each advertisement of the house as a combo of link to details informations page and date of publication. 
        """
        house_advertisement__link_to_details_page_list = []
        house_advertisement__publication_date_list = []

        advertisement_element_list = main_container.css("ul.ulListing li.listingBox")

        for advertisement_element in advertisement_element_list:
            """
            Here, We gonna grap the link of the page that contain the details informations of the current house advertisement.
            """
            house_advertisement__link_to_details_page_list.append(advertisement_element.css("::attr(href)").get())
            """
            Now, We gonna grap the publication date of the current house advertisement.
            """
            house_advertisement__publication_date = advertisement_element.css("span.listingDetails").xpath("text()") 
            if len(house_advertisement__publication_date)> 1:
                house_advertisement__publication_date_list.append(house_advertisement__publication_date[1])
            else:
                house_advertisement__publication_date_list.append("None")

        for house_details_page_link, house_advertisement__publication_date in zip(house_advertisement__link_to_details_page_list, house_advertisement__publication_date_list):
            yield response.follow(house_details_page_link, callback=self.parse_house_advertisment_details_page, cb_kwargs={'house_advertisement__publication_date': house_advertisement__publication_date})

        next_page_container = response.css('[id="mainListing"] div.paginationDots')
        next_page_container_url = next_page_container.xpath('a[@class="Dots currentDot"]/following-sibling::a/@href').get()

        yield response.follow(next_page_container_url, callback=self.parse)


    def parse_house_advertisment_details_page(self, response, house_advertisement__publication_date):

        l = ItemLoader(item=MubawabItem(), selector=response)

        l.add_value('advertisement_url', response.url)

        try:
            l.add_xpath('title', '//h1[@class="searchTitle"]')
        except:
            l.add_xpath('title', '')

        try:
            l.add_xpath('price', '//h3[@class="orangeTit"]')
        except:
            l.add_value('price', '')

        try:
            l.add_value('publication_date', house_advertisement__publication_date)
        except:
            l.add_value('publication_date', '')

        try:
            l.add_xpath('location', '//h3[@class="greyTit"]')
        except:
            l.add_value('location', '')

        try:
            l.add_xpath('description', '//div[@class="disFlex adDetails"]//span')
        except:
            l.add_value('description', '')

        try:
            l.add_xpath('complete_description', '//div[@class="blockProp"]/p')
        except:
            l.add_value('complete_description', '')

        try:
            l.add_xpath('features_list', '//div[@class="adMainFeatureContent"]//p')
        except:
            l.add_value('features_list', '')
        
        

        yield l.load_item()


        # annonce_details = response.css("div.minDivider")
        # ad_title = annonce_details.xpath("//h1[@class='searchTitle']/text()").get()
        # ad_price = annonce_details.xpath("//h3[@class='orangeTit']/text()").get()
        # ad_location = annonce_details.xpath("//h3[@class='greyTit']/text()").get()
        # details_description_data = annonce_details.xpath("//div[@class='disFlex adDetails']//span//text()").getall() 
        # complete_description = annonce_details.xpath("//div[@class='blockProp']/p").get()
        # features_list_data = annonce_details.xpath("//div[@class='adMainFeatureContent']//p/text()").getall()
        # yield {
        #     "advertisement_url": response.url,
        #     "title": ad_title,
        #     "publication_date": house_advertisement__publication_date.get(),
        #     "price": ad_price,
        #     "location" : ad_location,
        #     "description" : ";".join(details_description_data),
        #     "complete_description" : complete_description,
        #     "features_list" : ";".join(features_list_data),
        # }

        
