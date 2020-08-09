from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https:\\google.com')
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('cheiro de pneu queimado')
searchbox.send_keys(Keys.ENTER)
video = driver.find_element_by_xpath('//*[@id="wp-tabs-container"]/div[1]/div[2]/div/div/div/div/div/div[2]/h3/a/h3')
video.click()
play = driver.find_element_by_xpath('//*[@id="movie_player"]/div[25]/div[2]/div[1]/button')
play.click()