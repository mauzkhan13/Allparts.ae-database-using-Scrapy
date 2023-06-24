import random
import scrapy

class SparepartsSpider(scrapy.Spider):
    name = "spareparts"

    start_urls = [
       'https://www.allparts.ae/ccatalogs/totalcatalog/'

        ]
    url_counter = 0

    def parse(self, response):
        for first_link in response.xpath('//a[contains(text(),"CMC")]/@href'):
            yield scrapy.Request(
                url=response.urljoin(first_link.extract()),
                callback=self.parse_links
            )
 
    def parse_links(self, response):
        self.url_counter += 1
        link = response.xpath('//tr[@class]/td/a')
        urls = link.xpath('./@href').getall()
        text = link.xpath('./text()').get()
        for url in urls:
            complete_url = response.urljoin(url)
            yield scrapy.Request(url=complete_url, meta={'text': text}, callback=self.parse_first_links)

    def parse_first_links(self, response): 
        self.url_counter += 1
        for link in response.xpath('//tr[@class="over"]/td/a'):
            url = link.xpath('./@href').getall()
            text = link.xpath('./text()').get()
            for u in url:
                complete_url = response.urljoin(u)
                yield scrapy.Request(url=complete_url, meta={'text': text}, callback=self.parse_second_links)

    def parse_second_links(self, response):
            self.url_counter += 1

    #Accessories
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Boot/Cargo Area")]/@href').get()),
                             callback=self.parse_item, meta={ 'category': 'Boot/Cargo Area' })

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Floor Mats")]/@href').get()),
                         callback=self.parse_item, meta={'category': 'Floor Mats'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Footwell Tray")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Footwell Tray'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wind Deflector")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wind Deflector'})
    #Air Conditioning
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Compressor / Parts")]/@href').get()),
                             callback=self.parse_item, meta={'category': 'Compressor / Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Condenser")]/@href').get()),
                             callback=self.parse_item, meta={'category': 'Condenser'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Controls/ Regulation")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Controls/ Regulation'})

            yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Battery'}) for
                link in response.xpath('//a[contains(text(),"Battery")]/@href').getall()]

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Battery")]/@href').get()),
                                callback=self.parse_item, meta={'category': 'Battery'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Dryer")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Dryer'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sensors")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sensors'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Switch")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Switch'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Valves")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Valves'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Vaporizer")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Vaporizer'})

    #Axle Drive
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Differential")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Differential'})


    # Axle Mounting/ Steering/ Wheels
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Axle Beam")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Axle Beam'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Axle Mounting")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Axle Mounting'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Axle Support / Chassis Sub-Frame")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Axle Support / Chassis Sub-Frame'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Mounting/Fastening")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Mounting/Fastening'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Steering Links (control arm, trailing link, diagonal arm)")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Steering Links (control arm, trailing link, diagonal arm)'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Ball Joint")]/@href').get()),
                               callback=self.parse_item, meta={'category': 'Ball Joint'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Mounting, suspension strut")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Mounting, suspension strut'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Coupling Rod")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Coupling Rod'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fasteners")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fasteners'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Self-Aligning Support")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Self-Aligning Support'})


            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Stabilizer")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Stabilizer'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Track widening")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Track widening'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tyre Pressure Control System")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tyre Pressure Control System'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wheel / Wheel Fastening")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wheel / Wheel Fastening'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wheel Bearing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wheel Bearing'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wheel Hub")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wheel Hub'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Kingpin")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Kingpin'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Stub Axle")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Stub Axle'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bearing, wheel bearing housing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bearing, wheel bearing housing'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Radial Oil Seal, drive shaft")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Radial Oil Seal, drive shaft'})

    #Belt Drive
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Alternator Freewheel Clutch")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Alternator Freewheel Clutch'})
            yield from [scrapy.Request(url=response.urljoin(link),callback=self.parse_item, meta={'category': 'Belt Pulley'})
                    for link in response.xpath('//a[contains(text(),"Belt Pulley")]/@href').getall()]
            yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Belt Tensioner (Tensioner Unit)'})
                    for link in response.xpath('//a[contains(text(),"Belt Tensioner (Tensioner Unit)")]/@href').getall()]
            yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Tensioner Pulley'})
                    for link in response.xpath('//a[contains(text(),"Tensioner Pulley")]/@href').getall()]
            yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Timing Belt'})
                    for link in response.xpath('//a[contains(text(),"Timing Belt")]/@href').getall()]
            yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Timing Belt Cover'})
                    for link in response.xpath('//a[contains(text(),"Timing Belt Cover")]/@href').getall()]
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Timing Belt Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Timing Belt Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Belt Tensioner (Tensioner Unit)")]/@href').get()),
                                callback=self.parse_item, meta={'category': 'Belt Tensioner (Tensioner Unit)'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Idler-/Guide Pulley")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Idler-/Guide Pulley'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tensioner")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tensioner'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tensioner Pulley")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tensioner Pulley'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"V-Ribbed Belt")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'V-Ribbed Belt'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"V-Ribbed Belt Kit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'V-Ribbed Belt Kit'})
    # Body

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, fog light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, fog light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fog Light/ Insert")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fog Light/ Insert'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, spotlight")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, spotlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bumper/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bumper/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Covers/ Caps")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Covers/ Caps'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Footboard/ Door Pillar")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Footboard/ Door Pillar'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Front Fairing/ Grille")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Front Fairing/ Grille'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Mudguard")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Mudguard'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rear-End Cowling")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rear-End Cowling'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Side Panel")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Side Panel'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Side/ Cross Member")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Side/ Cross Member'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wing/Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wing/Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Tank/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Tank/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gas Springs")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gas Springs'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bonnet/ Parts/ Silencing Material")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bonnet/ Parts/ Silencing Material'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Doors/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Doors/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, headlight")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, headlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Headlight/ Insert")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Headlight/ Insert'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Combination Rearlight")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Combination Rearlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fog Tail Lights, bulbs")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fog Tail Lights, bulbs'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rear Fog Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rear Fog Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, indicator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, indicator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Indicator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Indicator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Side Indicator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Side Indicator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Licence Plate Light Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Licence Plate Light Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, reverse light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, reverse light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Reverse Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Reverse Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Outline Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Outline Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Park-/Position Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Park-/Position Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Auxiliary Stop Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Auxiliary Stop Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, stop light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, stop light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tail Light Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tail Light Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Auxiliary Stop Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Auxiliary Stop Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Doors/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Doors/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Footboard/ Door Pillar")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Footboard/ Door Pillar'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Tank/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Tank/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Mirrors")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Mirrors'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Side Panel")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Side Panel'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Trim/Protective Strips")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Trim/Protective Strips'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bonnet/ Parts/ Silencing Material")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bonnet/ Parts/ Silencing Material'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bumper/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bumper/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Cover")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Engine Cover'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, fog light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, fog light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fog Light/ Insert")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fog Light/ Insert'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, headlight")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, headlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Headlight/ Insert")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Headlight/ Insert'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, indicator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, indicator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Front Fairing/ Grille")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Front Fairing/ Grille'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Trim/Protective Strips")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Trim/Protective Strips'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Outline Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Outline Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Park-/Position Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Park-/Position Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, spotlight")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, spotlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Windscreen")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Windscreen'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wing/Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wing/Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bonnet/ Parts/ Silencing Material")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bonnet/ Parts/ Silencing Material'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bumper/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bumper/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Combination Rearlight")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Combination Rearlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Cover")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Engine Cover'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fog Tail Lights, bulbs")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fog Tail Lights, bulbs'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rear Fog Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rear Fog Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Licence Plate Light Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Licence Plate Light Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Panelling")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Panelling'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Covers/ Caps")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Covers/ Caps'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gas Springs")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gas Springs'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Trim/Protective Strips")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Trim/Protective Strips'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bulb, reverse light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bulb, reverse light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Reverse Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Reverse Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Park-/Position Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Park-/Position Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tail Light Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tail Light Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Windows")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Windows'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Auxiliary Stop Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Auxiliary Stop Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Door Window / Side Window")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Door Window / Side Window'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Footboard/ Door Pillar")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Footboard/ Door Pillar'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Emblems")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Emblems'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Trim/Protective Strips")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Trim/Protective Strips'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Licence Plate Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Licence Plate Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Licence Plate Light Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Licence Plate Light Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rear Windscreen")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rear Windscreen'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Connecting Rod/Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Connecting Rod/Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Crankshaft/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Crankshaft/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Head Cover Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Head Cover Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Camshaft/ Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Camshaft/ Set'})

    #Brake System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Booster")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Booster'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Caliper Mounting")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Caliper Mounting'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Caliper Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Caliper Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Fluid")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Brake Fluid'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Hoses")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Brake Hoses'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Light Switch")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Brake Light Switch'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Master Cylinder")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Brake Master Cylinder'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Control Levers/ Cables")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Control Levers/ Cables'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Disc")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Disc'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Pad Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Pad Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Parts/ Accessories")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Parts/ Accessories'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Drive Dynamics Control")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Drive Dynamics Control'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Kit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Kit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Lining/ Shoe")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Lining/ Shoe'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Drum Brake Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Drum Brake Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wheel Cylinders")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wheel Cylinders'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"High Performance Brake Disc")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'High Performance Brake Disc'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Vacuum Pump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Vacuum Pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wheel Cylinders")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wheel Cylinders'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Handbrake")]/@href').get()),
                         callback=self.parse_item, meta={'category': 'Handbrake'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"High Performance Brake Pad")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'High Performance Brake Pad'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wear Indicator, brake pads")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wear Indicator, brake pads'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Brake Parts/ Accessories")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Brake Parts/ Accessories'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Accessories, disc brake")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Accessories, disc brake'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wear Indicator, brake linings")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wear Indicator, brake linings'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Pressure Accumulator/ - Switch")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Pressure Accumulator/ - Switch'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Dryer/ Cartridge")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Air Dryer/ Cartridge'})


#Carrier Equipment
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Roof Rack")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Roof Rack'})
#Clutch/ Parts
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Master Cylinder")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Master Cylinder'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Clutch Disc")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Clutch Disc'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Clutch Pressure Plate")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Clutch Pressure Plate'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Hydraulic Fluid")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Hydraulic Fluid'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Central Slave Cylinder")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Central Slave Cylinder'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Repair Kit, clutch complete")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Repair Kit, clutch complete'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Clutch Levers/ Linkage")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Clutch Levers/ Linkage'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Clutch Pedal")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Clutch Pedal'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Flywheel")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Flywheel'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Clutch Releaser")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Clutch Releaser'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Release Fork")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Release Fork'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sleeve")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sleeve'})

#Comfort Systems
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Preheater System (electric)")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Engine Preheater System (electric)'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Parking Assist / Reverse Alarm")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Parking Assist / Reverse Alarm'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Window Regulator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Window Regulator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cruise Control")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cruise Control'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cruise Control System")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cruise Control System'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rain Sensor")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rain Sensor'})


#Compressed Air System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Head, compressor")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Head, compressor'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Hoses/ Connector Pipes")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Hoses/ Connector Pipes'})

#Cooling System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Cooling")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Air Cooling'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Antifreeze")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Antifreeze'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Flanges")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Flanges'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Radiator Hoses")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Radiator Hoses'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Radiator Fan")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Radiator Fan'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Expansion Tank, engine coolant")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Expansion Tank, engine coolant'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Interior Heat Exchanger")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Interior Heat Exchanger'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Radiator /Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Radiator /Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sender Unit, coolant temperature")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sender Unit, coolant temperature'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Thermostat")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Thermostat'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Water Pump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Water Pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cooling Module")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cooling Module'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Pipes")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Pipes'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Cooler")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Cooler'})

#Electrics
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Alternator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Alternator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Generator/ Alternator Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Generator/ Alternator Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bend Light/-Parts")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Bend Light/-Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Central Electrics")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Central Electrics'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Harness")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Harness'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Parts, headlight")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Parts, headlight'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Headlight/ Insert")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Headlight/ Insert'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sender Units/ Sensors")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sender Units/ Sensors'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Light Switch/ Lever")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Light Switch/ Lever'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Combination Rearlight Bulb")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Combination Rearlight Bulb'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Daytime Running Light")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Daytime Running Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Boot-/Cargo Area Lights")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Boot-/Cargo Area Lights'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Light, passenger compartment")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Light, passenger compartment'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sensors")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sensors'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Starter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Starter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gauges")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gauges'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Light Switch/ Lever")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Light Switch/ Lever'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Solenoid Switch")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Solenoid Switch'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Starter Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Starter Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuse Box/- Holder")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuse Box/- Holder'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Xenon Light")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Xenon Light'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Reflectors/ Side Reflectors")]/@href').get()),
                                callback=self.parse_item, meta={'category': 'Reflectors/ Side Reflectors'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Glow Plug")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Glow Plug'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Glove Box Lighting")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Glove Box Lighting'})

    #Engine
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Alternator Freewheel Clutch")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Alternator Freewheel Clutch'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Belt Pulley")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Belt Pulley'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Complete Engine")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Complete Engine'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Crankcase")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Crankcase'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Piston Ring Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Piston Ring Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Radial Oil Seal/- Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Radial Oil Seal/- Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Head Bolt")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Head Bolt'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Head Cover/-Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Head Cover/-Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Head Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Head Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Intake Manifold Gasket/Sealing Ring")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Intake Manifold Gasket/Sealing Ring'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Seals, crank-/ camshaft")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Seals, crank-/ camshaft'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Vacuum Pump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Vacuum Pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Valve Guide/ Stem Seal/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Valve Guide/ Stem Seal/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinders/ Pistons")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinders/ Pistons'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Filter/ Housing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Air Filter/ Housing'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Charge Air Control")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Charge Air Control'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Charger Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Charger Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Charger/-parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Charger/-parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Intercooler")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Intercooler'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Throttle body")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Throttle body'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Camshaft")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Camshaft'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Centre Pivot-/End Pivot Rocker Arm")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Centre Pivot-/End Pivot Rocker Arm'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Push Rod / Tube")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Push Rod / Tube'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Valve Actuation")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Valve Actuation'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Valves/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Valves/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Cover")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Engine Cover'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Electrics")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Engine Electrics'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Mounting Bracket")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Engine Mounting Bracket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Mounting Complete")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Engine Mounting Complete'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Lambda Control")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Lambda Control'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Crankcase Gasket")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Crankcase Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Exhaust Manifold Gasket/Seal")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Exhaust Manifold Gasket/Seal'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket Set, complete")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket Set, complete'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, cylinder head")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, cylinder head'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, intake manifold")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, intake manifold'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, oil pan")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Gasket, oil pan'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, turbocharger")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, turbocharger'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Radial Oil Seal/- Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Radial Oil Seal/- Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rocker Cover Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rocker Cover Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Seal, valve stem")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Seal, valve stem'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Seals, oil circuit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Seals, oil circuit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Timing Case/ Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Timing Case/ Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Filter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Filter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Drain Screw")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Drain Screw'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, oil pan")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, oil pan'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wet Sump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wet Sump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Pressure Switch/ -Sensor /-Valve")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Pressure Switch/ -Sensor /-Valve'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Article Search via Graphic")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Article Search via Graphic'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Sleeve/ Kit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Sleeve/ Kit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Big End Bearings")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Big End Bearings'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Small End Bushes")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Small End Bushes'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Main Bearings, crankshaft")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Main Bearings, crankshaft'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Thrust Washers/ Thrust Bearing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Thrust Washers/ Thrust Bearing'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Piston, complete")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Piston, complete'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinder Head Bolt")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinder Head Bolt'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Intake Manifold Gasket/Sealing Ring")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Intake Manifold Gasket/Sealing Ring'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Filler Cap/ Seal")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Filler Cap/ Seal'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Seals, crank-/ camshaft")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Seals, crank-/ camshaft'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Valve Guide/ Stem Seal/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Valve Guide/ Stem Seal/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cylinders/ Pistons")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cylinders/ Pistons'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Charger Intake Hose")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Charger Intake Hose'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Intercooler")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Intercooler'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Control Flap")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Control Flap'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"EGR Exhaust Control")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'EGR Exhaust Control'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"EGR Impulse Valve")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'EGR Impulse Valve'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"EGR Vacuum Control Valve")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'EGR Vacuum Control Valve'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"EGR Valve/ Intake Manifold")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'EGR Valve/ Intake Manifold'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Pressure Transducer")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Pressure Transducer'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Shut-off Valve")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Shut-off Valve'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Hoses/ Lines")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Hoses/ Lines'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, cylinder head")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, cylinder head'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, turbocharger")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, turbocharger'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Seals, coolant circuit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Seals, coolant circuit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil Dipstick")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil Dipstick'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Crankshaft/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Crankshaft/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Exhaust Manifold Gasket/Sealing Ring")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Exhaust Manifold Gasket/Sealing Ring'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"O-Ring Set, cylinder liners")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'O-Ring Set, cylinder liners'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Breather")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Breather'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Timing Chain Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Timing Chain Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Engine Guard/Skid Plate")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Engine Guard/Skid Plate'})


    #Exhaust System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Clamp")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Clamp'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Charger")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Charger'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Exhaust Pipes")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Exhaust Pipes'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Exhaust System, complete")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Exhaust System, complete'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Lambda Sensor")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Lambda Sensor'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sensor/ Probe")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sensor/ Probe'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rubber Buffer")]/@href').get()),
                         callback=self.parse_item, meta={'category': 'Rubber Buffer'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Rubber Strip")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Rubber Strip'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Assembly Kit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Assembly Kit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Screws/Nuts/Rings")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Screws/Nuts/Rings'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Catalytic Converter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Catalytic Converter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Silencer")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Silencer'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Silencer, sport set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Silencer, sport set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sensor/ Probe")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sensor/ Probe'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"")]/@href').get()),
                                 callback=self.parse_item, meta={'category': ''})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gaskets/ Pipe Connectors/ ")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gaskets/ Pipe Connectors/ '})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Soot/Particulate Filter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Soot/Particulate Filter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gaskets/ Pipe Connectors/ Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gaskets/ Pipe Connectors/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Baffle")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Baffle'})

    #Filters
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Filter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Air Filter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Filter, passenger compartment")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Air Filter, passenger compartment'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Filter Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Filter Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Filter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Filter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Hydraulic Filter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Hydraulic Filter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Filter, driver cab")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Air Filter, driver cab'})
    #Fuel Mixture Formation
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Accelerator Pedal")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Accelerator Pedal'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Injector/Nozzle/Nozzle and Holder Assembly/UI")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Injector/Nozzle/Nozzle and Holder Assembly/UI'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sensor/ Probe")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sensor/ Probe'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Throttle/ Fuel Lines/ Vacuum Pipe")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Throttle/ Fuel Lines/ Vacuum Pipe'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"EGR Pressure Transducer")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'EGR Pressure Transducer'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Suction System, secondary air intake")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Suction System, secondary air intake'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Injection Pump/High Pressure Pump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Injection Pump/High Pressure Pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Line/- Distribution/-Allocation")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Line/- Distribution/-Allocation'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Gasket, water pump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Gasket, water pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"mass airflow sensor/airflow meter")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'mass airflow sensor/airflow meter'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Nozzle and Holder Assembly/Nozzle Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Nozzle and Holder Assembly/Nozzle Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Switch/ Relay")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Switch/ Relay'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Valves / Valve Unit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Valves / Valve Unit'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Control Linkage/ Damper/ Chambers")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Control Linkage/ Damper/ Chambers'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Cable/ Linkages")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Cable/ Linkages'})


    #Fuel Supply System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Delivery Unit, complete")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Delivery Unit, complete'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Filter/-housing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Filter/-housing'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Pressure Regulator / Switch")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Pressure Regulator / Switch'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Pump")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Fuel Pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Tank / Parts")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Fuel Tank / Parts'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Sender Unit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Sender Unit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Fuel Tank / Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Fuel Tank / Parts'})
    #Heater
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Air Filter, passenger compartment")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Air Filter, passenger compartment'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Blower/ Parts")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Blower/ Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Interior Heat Exchanger")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Interior Heat Exchanger'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Coolant Water Preheating")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Coolant Water Preheating'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Hoses/Pipes")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Hoses/Pipes'})
    #Hydraulic System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Filter, hydraulic system")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Filter, hydraulic system'})


    #Information/ Communication Systems
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Instruments")]/@href').get()),
                         callback=self.parse_item, meta={'category': 'Instruments'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Aerial")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Aerial'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Audio System")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Audio System'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Communication")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Communication'})



    #Interior Equipment
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Boot")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Boot'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Hand/ Foot Lever System")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Hand/ Foot Lever System'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Window Regulator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Window Regulator'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Handles")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Handles'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Sun Visor")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Sun Visor'})


    #Locking System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Handles")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Handles'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Lock Barrel/ Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Lock Barrel/ Set'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Locks, interior")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Locks, interior'})
    #Maintenance Service Parts
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Additional Repairs")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Additional Repairs'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Service Intervals")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Service Intervals'})

    #Spark/ Glow Ignition
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Control Unit/ Relay")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Control Unit/ Relay'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Ignition Coil/Ignition Coil Unit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Ignition Coil/Ignition Coil Unit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Ignition Module/ Control Unit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Ignition Module/ Control Unit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Pulse Generator")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Pulse Generator'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Spark Plug")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Spark Plug'})
    #Steerin- 9
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bellow/Seal")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bellow/Seal'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Filter, power steering")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Filter, power steering'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Steering Angle Sensor")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Steering Angle Sensor'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Steering Column")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Steering Column'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Steering Gear/ Pump")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Steering Gear/ Pump'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Steering Joints")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Steering Joints'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Parts, tie rod assy.")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Parts, tie rod assy.'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Repair Kit")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Repair Kit'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tie Rod Assembly")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tie Rod Assembly'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Filter, power steering")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Filter, power steering'})


    #Suspension
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Coil Spring Suspension")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Coil Spring Suspension'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Coil Springs")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Coil Springs'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Shock Absorber")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Shock Absorber'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Suspension Kit, complete")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Suspension Kit, complete'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Assembly Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Assembly Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Suspension Strut Bearing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Suspension Strut Bearing'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Pneumatic Suspension")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Pneumatic Suspension'})

    #Towbar/ Parts
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Electric Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Electric Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Parts")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Parts'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Towbar")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Towbar'})


    #Transmission
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Oil")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Oil'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Transmission")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Transmission'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Transmission Control")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Transmission Control'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Transmission Mounting")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Transmission Mounting'})

    #Wheel Drive
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Bellow")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Bellow'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Drive Shaft")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Drive Shaft'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Joint / Set")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Joint / Set'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tripod Hub")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Tripod Hub'})


    #Wheels/Tyres
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Accessories")]/@href')[1].get()),
                                callback = self.parse_item, meta = {'category': 'Accessories'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Tyre Pressure Control System")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Tyre Pressure Control System'})

    #Windscreen Cleaning System
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Motor, windscreen wipers")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Motor, windscreen wipers'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Water Pump, windscreen washing")]/@href').get()),
                                callback = self.parse_item, meta = {'category': 'Water Pump, windscreen washing'})
           

            yield scrapy.Request(url=response.urljoin(
                response.xpath('(//div[@class="container"])[2]//a[contains(text(),"Windscreen Cleaning System")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Windscreen Cleaning System'})

            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wiper Arm/ Bearing")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wiper Arm/ Bearing'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wiper Blade/-Rubber")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wiper Blade/-Rubber'})
            yield scrapy.Request(url=response.urljoin(response.xpath('//a[contains(text(),"Wiper Linkage/ Drive")]/@href').get()),
                                 callback=self.parse_item, meta={'category': 'Wiper Linkage/ Drive'})

            try:
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Axle Mounting'}) for
                            link in response.xpath('//a[contains(text(),"Axle Mounting")]/@href').getall()]

                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Wheel Hub'}) for
                            link in response.xpath('//a[contains(text(),"Wheel Hub")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Combination Rearlight'}) for
                            link in response.xpath('//a[contains(text(),"Combination Rearlight")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Indicator'}) for
                            link in response.xpath('//a[contains(text(),"Indicator")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Reverse Light'}) for
                            link in response.xpath('//a[contains(text(),"Reverse Light")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Mirrors'}) for
                            link in response.xpath('//a[contains(text(),"Mirrors")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Flanges'}) for
                                    link in response.xpath('//a[contains(text(),"Flanges")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Oil Cooler'}) for
                            link in response.xpath('//a[contains(text(),"Oil Cooler")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Thermostat'}) for
                            link in response.xpath('//a[contains(text(),"Thermostat")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Water Pump'}) for
                            link in response.xpath('//a[contains(text(),"Water Pump")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Alternator'}) for
                            link in response.xpath('//a[contains(text(),"Alternator")]/@href').getall()]

                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Starter'}) for
                            link in response.xpath('//a[contains(text(),"Starter")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Timing Belt Set'}) for
                            link in response.xpath('//a[contains(text(),"Timing Belt Set")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'V-Ribbed Belt Kit'}) for
                            link in response.xpath('//a[contains(text(),"V-Ribbed Belt Kit")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Complete Engine'}) for
                            link in response.xpath('//a[contains(text(),"Complete Engine")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Crankcase'}) for
                            link in response.xpath('//a[contains(text(),"Crankcase")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Oil Cooler'}) for
                            link in response.xpath('//a[contains(text(),"Oil Cooler")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Gasket'}) for
                            link in response.xpath('//a[contains(text(),"Gasket")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Charger'}) for
                            link in response.xpath('//a[contains(text(),"Charger")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Oil Filter'}) for
                            link in response.xpath('//a[contains(text(),"Oil Filter")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Lambda Control'}) for
                            link in response.xpath('//a[contains(text(),"Lambda Control")]/@href').getall()]

                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Fuel Pump'}) for
                            link in response.xpath('//a[contains(text(),"Fuel Pump")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Floor Mats'}) for
                            link in response.xpath('//a[contains(text(),"Floor Mats")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Assembly Parts'}) for
                            link in response.xpath('//a[contains(text(),"Assembly Parts")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Windscreen Cleaning System'}) for
                            link in response.xpath('//a[contains(text(),"Windscreen Cleaning System")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Axle Support / Chassis Sub-Frame'}) for
                            link in response.xpath('//a[contains(text(),"Axle Support / Chassis Sub-Frame")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Axle Beam'}) for
                            link in response.xpath('//a[contains(text(),"Axle Beam")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Repair Kit'}) for
                            link in response.xpath('//a[contains(text(),"Repair Kit")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Stub Axle'}) for
                            link in response.xpath('//a[contains(text(),"Stub Axle")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Windows'}) for
                            link in response.xpath('//a[contains(text(),"Windows")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Drum Brake Parts'}) for
                            link in response.xpath('//a[contains(text(),"Drum Brake Parts")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Tools'}) for
                            link in response.xpath('//a[contains(text(),"Tools")]/@href').getall()]
                yield from [scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Relay'}) for
                            link in response.xpath('//a[contains(text(),"Relay")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Starter Parts'}) for
                    link in response.xpath('//a[contains(text(),"Starter Parts")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Clamp'}) for
                    link in response.xpath('//a[contains(text(),"Clamp")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Air Bag System'}) for
                    link in response.xpath('//a[contains(text(),"Air Bag System")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Towbar'}) for
                    link in response.xpath('//a[contains(text(),"Towbar")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Radiator'}) for
                    link in response.xpath('//a[contains(text(),"Radiator")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Transmission Control / Hydraulics'}) for
                    link in response.xpath('//a[contains(text(),"Transmission Control / Hydraulics")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Transmission'}) for
                    link in response.xpath('//a[contains(text(),"Transmission")]/@href').getall()]

                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Air Filter, driver cab'}) for
                    link in response.xpath('//a[contains(text(),"Air Filter, driver cab")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': 'Cornering Light/-Parts'}) for
                    link in response.xpath('//a[contains(text(),"Cornering Light/-Parts")]/@href').getall()]
                yield from [
                    scrapy.Request(url=response.urljoin(link), callback=self.parse_item, meta={'category': ''}) for
                    link in response.xpath('//a[contains(text(),"")]/@href').getall()]
                

            except:
                 pass

    def parse_item(self, response):
        self.url_counter += 1
        company = 'CMC'
        category = response.meta['category']
        suppliers = response.xpath('//td[@class]/text()')

        if suppliers:
            for supplier in suppliers:
                supplier_name = supplier.extract().strip()
                if supplier_name:
                    yield {
                        'Car Brand': company,
                        'Sub Category Description': category,
                        'Supplier': supplier_name,
                    }

        def handle_spider_error(self, failure):
            self.logger.error(f"Spider failed: {failure}")

        self.logger.info(f"Extracted data from {self.url_counter} URLs")