from pages.base_page import Page
from support.logger import logger
from time import sleep

class MainPage(Page):



    def open_main(self):
        logger.info('Opening https://www.amazon.com/ ')
        self.driver.get('https://www.amazon.com/')
        sleep(3)
        self.driver.refresh()


