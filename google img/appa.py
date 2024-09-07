from selenium import webdriver
import time
#import urllib.request

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=%EA%B0%95%EC%95%84%EC%A7%80&sca_esv=17147adff2573a58&hl=ko&udm=2&sxsrf=ADLYWILuFj-uEUIYavetdqo94FbdnsUdWw:1718785741552&source=lnt&tbs=sur:ol&sa=X&ved=2ahUKEwjnwMfsn-eGAxWQh1YBHUzZA3UQpwV6BAgCECE&biw=1536&bih=695&dpr=1.25')
firstImage = driver.find_element("xpath",'//*[@id="dimg_19"]')
firstImage.click()

#image = driver.find_element('#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div.AQyBn > div.BIB1wf.EIehLd.fHE6De > c-wiz > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.pT0Scc.iPVvYb')
#imageSrc = image.get_attribute('src')
#urllib.request.urlretrieve(imageSrc, 'dog_image.jpg')

time.sleep(10)
driver.quit()
