from selenium import webdriver
from time import sleep
from secret import email, password

frnc_list = []
pol_list = []


class Quizlebot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(1)

    def login(self):
        self.driver.get('https://quizlet.com/')
        log_btn = self.driver.find_element_by_xpath('//*[@id="SiteHeaderReactTarget"]/header/div[1]/div/div[2]/span[2]/div/div[3]/div/button[1]')
        log_btn.click()

        email_input = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_input.send_keys(email)

        pw_input = bot.driver.find_element_by_xpath('//*[@id="password"]')
        pw_input.send_keys(password)

        login_btn = self.driver.find_element_by_css_selector('body > div.UIModal.UIModal-container.is-white.is-open > div > div.UIModalBody > form > button')
        sleep(3)
        login_btn.click()


    def words(self,m):
        for n in range (1, m+10):
            try:
                frnc_word = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[1]/div[3]/div[2]/div/div/section/div/section/div[' + str(n) + ']/div/div/div[1]/div/div[1]/div').text
                print(frnc_word)
                frnc_list.append(frnc_word)
            except Exception:
                print('----null----')

        for n in range (1, m+10):
            try:
                pol_word = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[1]/div[3]/div[2]/div/div/section/div/section/div[' + str(n) + ']/div/div/div[1]/div/div[2]/div/a/span').text
                print(pol_word)
                pol_list.append(pol_word)
            except Exception:
                print('----null----')
            
    def show_array(self):
        print(pol_list)
        print(frnc_list)

    def writting(self):
        while True:
            try:
                pl_check_word = self.driver.find_element_by_xpath('//*[@id="js-learnModeInner"]/div/div/div[1]/div/div/div/div/span').text 
                if pl_check_word in pol_list:
                    index_word = pol_list.index(pl_check_word)
                    print(index_word)
            
                    answer_fild = self.driver.find_element_by_xpath('//*[@id="user-answer"]')
                    frnc_answer = frnc_list[index_word]
                    answer_fild.send_keys(frnc_answer)
                    sleep(1)

                    confirm_btn = self.driver.find_element_by_xpath('//*[@id="js-learnModeAnswerButton"]')
                    confirm_btn.click()

                    sleep(1)

                    self.driver.find_element_by_xpath('//*[@id="js-learnModeInner"]/div[2]/button').click()
            except Exception:
                print('---end---')
                break


    def web(address):
        pass
    
    def save(self):
        
        all_list = []
        for n in range (0,len(pol_list)):
            all_list.append(pol_list[n] + ' - ' + frnc_list[n]) 

        with open('plik.txt', 'w') as f:
            for item in all_list:
                f.write(item + '\n')                    

    def door(self):
        self.driver.close()

bot = Quizlebot()
bot.login()