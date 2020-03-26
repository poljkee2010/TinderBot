
from selenium import webdriver
from time import sleep
import random
from secrets import email_gmail,pass1,login_facebook,pass2


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://tinder.com')
        sleep(3)
        try:
            self.login_google()
        except Exception:
            self.login_fb()

        sleep(5)
        self.auto_swipe()

    def login_google(self):
        print("Actions in page 1...")
        self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button').click()

        # switch to login popup page (переключение между основным и всплывающем окном)
        base_window = self.driver.window_handles[0]
        log_window = self.driver.window_handles[1]
        self.driver.switch_to.window(log_window) # переключение драйвера в окно
        print("Actions in page 2...")

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(email_gmail)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(5)

        password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys(pass1)
        login_bttn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        login_bttn.click()
        sleep(7)

        self.driver.switch_to.window(base_window)

        # popup 1
        geo = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        geo.click()

        # popup 2
        notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification.click()

    def login_fb(self):
        print("Actions in page 1...")
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()

        # switch to login popup page (переключение между основным и всплывающем окном)
        base_window = self.driver.window_handles[0]
        log_window = self.driver.window_handles[1]
        self.driver.switch_to.window(log_window) # переключение драйвера в окно
        print("Actions in page 2...")

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(login_facebook)
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(pass2)
        login_bttn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_bttn.click()
        sleep(7)

        self.driver.switch_to.window(base_window)
        # popup 1
        geo = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        geo.click()

        # popup 2
        notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification.click()

    def like(self):
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    def dislike(self):
        sleep(1)
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def choose(self):
        left_count, right_count = 0, 0
        r = random.randint(0,10)
        if r <= 8:
            self.like()
            right_count += 1
            print(f'{right_count} лайков ')
        else:
            self.dislike()
            left_count += 1
            print(f'{left_count} дизлайков ')

    def auto_swipe(self):
        i = 0
        while i<=45:
            i += 1
            r = random.randint(1,3)
            sleep(r)
            try:
                self.choose()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match() or self.close_tinder_plus()


    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_tinder_plus(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]/span')
        popup_4.click()


    def message_all(self):
        while 1:
            matches = self.driver.find_elements_by_class_name('matchListItem')[1:] # срез для листа
            print("matches = self.driver.find_elements_by_class_name('matchListItem') = ", self.driver.find_elements_by_class_name('matchListItem'))

            if len(matches) < 2: # одна не нужная вкладка, все остальные использованы для сообщений
                break

            matches[0].click()
            sleep(1)

            msg_box = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            msg_box.send_keys('Привет. Как дела?')

            send_message = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button/span')
            send_message.click()
            sleep(1)

            matches_tab = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            matches_tab.click()
            sleep(1)


bot = TinderBot()
bot.login()
# bot.auto_swipe()
bot.message_all()

