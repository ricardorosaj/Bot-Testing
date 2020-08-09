from selenium import webdriver
from time import sleep

class InstaBot:
    "A bot that checks which people that you follow doesn't follow you back"
    def __init__(self, user, pw):
        self.driver = webdriver.Chrome()
        self.username = user
        #opens insta
        self.driver.get("https://instagram.com")
        sleep(2)
        #logins
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        #closes dumb stuff
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(2)
        #goes to profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
        sleep(2)
        #closes dumb stuff
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div").click()
    def _get_names(self):
        "Seleciona os nomes dentro das caixas de seguidores e seguindo e os salva numa lista"
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names

    def get_unfollowers(self):
        "Seleciona os seguidores e quem segue e compara pra checar que você segue que não te segue"
        #following
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        following = self._get_names()
        #followers
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        followers = self._get_names()
        #check if following individual follows back
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        print(len(not_following_back))

bot = InstaBot('user', 'pw') #change to your user and password
bot.get_unfollowers()        