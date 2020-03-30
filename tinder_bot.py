### Осталось научить переписываться более чем на одно сообщение

from selenium import webdriver
from time import sleep
import random
from secret import email_gmail,pass1,login_facebook,pass2

class TinderBot():
    def __init__(self,left_count,right_count,mas_right,mas_left):
        self.driver = webdriver.Chrome()
        self.left_count = left_count
        self.right_count = right_count
        self.mas_right = mas_right
        self.mas_left = mas_left

    def login(self):
        self.driver.get('http://tinder.com')
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div/button').click()
        try:
            self.login_google()
            self.notification()
        except Exception:
            self.login_fb()
            self.notification()

        sleep(4)
        # self.auto_swipe()

    def login_google(self):
        print("Actions in page 1...")
        try:
            self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div/div/button').click()
        except:
            try:
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button').click()
            except:
                self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/div[1]/div/span/div[1]/div/button').click()

        # switch to login popup page (переключение между основным и всплывающем окном)
        base_window = self.driver.window_handles[0]
        log_window = self.driver.window_handles[1]
        self.driver.switch_to.window(log_window) # переключение драйвера в окно
        print("Actions in page 2...")

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(email_gmail)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(2)

        password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys(pass1)
        login_bttn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        login_bttn.click()
        sleep(4)
        self.driver.switch_to.window(base_window)
        sleep(4)

    def login_fb(self):
        print("Actions in page 1...")
        try:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button').click()
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
        sleep(4)
        self.driver.switch_to.window(base_window)
        sleep(2)

    def notification(self):
        # popup 1
        geo = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        geo.click()
        sleep(4)

        # popup 2
        notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification.click()
        sleep(4)

        #popup 3
        location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button/span')
        location.click()
        sleep(4)

    def like(self):
        sleep(1)
        try:
            get_div = self.driver.find_element_by_css_selector('#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > main > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(10px\)--s.Pos\(r\) > div > div.Pos\(r\).Py\(16px\).Px\(4px\).Px\(8px\)--ml.D\(f\).Jc\(sb\).Ai\(c\).Maw\(375px\)--m.Mx\(a\).Pe\(n\).Mt\(-1px\) > div:nth-child(4) > button')
            get_div.click()
        except:
            try:
                get_div = self.driver.find_element_by_css_selector('#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(10px\)--s.Pos\(r\) > div > div.Pos\(r\).Py\(16px\).Px\(4px\).Px\(8px\)--ml.D\(f\).Jc\(sb\).Ai\(c\).Maw\(375px\)--m.Mx\(a\).Pe\(n\).Mt\(-1px\) > div:nth-child(4) > button')
                get_div.click()
                # self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
            except:
                self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div/div[2]/div/div/div[4]/button').click()

    def dislike(self):
        sleep(1)
        try:
            get_div = self.driver.find_element_by_css_selector('#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > main > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(10px\)--s.Pos\(r\) > div > div.Pos\(r\).Py\(16px\).Px\(4px\).Px\(8px\)--ml.D\(f\).Jc\(sb\).Ai\(c\).Maw\(375px\)--m.Mx\(a\).Pe\(n\).Mt\(-1px\) > div:nth-child(2) > button')
            get_div.click()
        except:
            try:
                self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]').click()
            except:
                try:
                    get_div = self.driver.find_element_by_css_selector(
                        '#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(10px\)--s.Pos\(r\) > div > div.Pos\(r\).Py\(16px\).Px\(4px\).Px\(8px\)--ml.D\(f\).Jc\(sb\).Ai\(c\).Maw\(375px\)--m.Mx\(a\).Pe\(n\).Mt\(-1px\) > div:nth-child(2) > button')
                    get_div.click()
                    # self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div/div[2]/div/div/div[2]/button').click()
                except:
                    self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button/span').click()

    def choose(self):
        r = random.randint(0,10)
        if r <= 8:
            self.like()
            self.right_count += 1
            self.mas_right.append(self.right_count)
            print(f'{len(self.mas_right)} лайков ')
        else:
            self.dislike()
            self.left_count += 1
            self.mas_left.append(self.left_count)
            print(f'{len(self.mas_left)} диз ')

    def auto_swipe(self):
        while True:
            for i in range(40):
                r = random.randint(1,3)
                sleep(r)
                try:
                    self.choose()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match() or self.close_tinder_plus() or self.close_tinder_on_header_window()
            bot.message_all()


    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/a')
        match_popup.click()

    def close_tinder_plus(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]/span')
        popup_4.click()

    def close_tinder_on_header_window(self):
        popup_5 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_5.click()


    def message_all(self):
        while 1:
            matches = self.driver.find_elements_by_class_name('matchListItem')[0:]

            if len(matches) <= 1:
                break

            matches[1].click()
            sleep(1)

            msg_box = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            msg_box.send_keys('Привет. Как дела?')

            send_message = self.driver.find_element_by_css_selector('#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > main > div > div:nth-child(4) > form > button > span')
            send_message.click()
            matches_tab = self.driver.find_element_by_css_selector('#match-tab')
            matches_tab.click()
            sleep(1)

if __name__ == '__main__':
    left_count, right_count = 0, 0
    mas_left = []
    mas_right = []

    bot = TinderBot(left_count,right_count,mas_left,mas_right)
    bot.login()
    bot.auto_swipe()
