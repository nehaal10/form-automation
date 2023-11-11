from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

def generate_dets():
    #opt -1 
    data_set = []

    numbers1 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers1.append(number)

    numbers2 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers2.append(number)

    numbers3 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers3.append(number)

    numbers4 = []
    for _ in range(100):
        number = random.randint(1, 2)
        numbers4.append(number)

    numbers5 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers5.append(number)

    numbers6 = []
    for _ in range(100):
        number = random.randint(1, 2)
        numbers6.append(number)

    numbers7 = []
    for _ in range(100):
        number = random.randint(1, 3)
        numbers7.append(number)

    numbers8 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers8.append(number)

    numbers9 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers9.append(number)

    numbers10 = []
    for _ in range(100):
        number = random.randint(1, 5)
        numbers10.append(number)


    for i in range(2):
        d = {"nums1":numbers1[i],
             "nums2":numbers2[i],
             "nums3":numbers3[i],
             "nums4":numbers4[i],
             "nums5":numbers5[i],
             "nums6":numbers6[i],
             "nums7":numbers7[i],
             "nums8":numbers8[i],
             "nums9":numbers9[i],
             "nums10":numbers10[i]
             }
        data_set.append(d)

    return data_set



web = webdriver.Chrome()

data = generate_dets()
#web.get('https://docs.google.com/forms/d/e/1FAIpQLSeeDm1TbIUlEPOsDUle_W71mKIuKIuZme4isHmu3uRouEyLIA/viewform')
time.sleep(3)

for i in data:

    web.get('https://docs.google.com/forms/d/e/1FAIpQLSeeDm1TbIUlEPOsDUle_W71mKIuKIuZme4isHmu3uRouEyLIA/viewform')

    if i['nums1'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
        num.click()

    elif i['nums1'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
        num.click()

    elif i['nums1'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
        num.click()

    elif i['nums1'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
        num.click()


    if i['nums2'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
        num.click()

    elif i['nums2'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
        num.click()

    elif i['nums2'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
        num.click()

    elif i['nums2'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
        num.click()


    if i['nums3'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
        num.click()

    elif i['nums3'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
        num.click()

    elif i['nums3'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
        num.click()

    elif i['nums3'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
        num.click()


    if i['nums4'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="i17"]')
        num.click()
    else:
        num = web.find_element(By.XPATH,'//*[@id="i20"]')
        num.click()

    if i['nums5'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
        num.click()

    elif i['nums5'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
        num.click()

    elif i['nums5'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
        num.click()

    elif i['nums5'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
        num.click()

    if i['nums6'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="i31"]')
        num.click()
    else:
        num = web.find_element(By.XPATH,'//*[@id="i34"]')
        num.click()

    if i['nums7'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="i41"]')
        num.click()

    elif i['nums7'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="i44"]')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="i47"]')
        num.click()

    if i['nums8'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="i54"]')
        num.click()

    elif i['nums8'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="i57"]')
        num.click()

    elif i['nums8'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="i60"]')
        num.click()

    elif i['nums8'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="i63"]')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="i66"]')
        num.click()


    if i['nums9'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div')
        num.click()

    elif i['nums9'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div')
        num.click()

    elif i['nums9'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div')
        num.click()

    elif i['nums9'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div')
        num.click()

    if i['nums10'] == 1:
        num = web.find_element(By.XPATH,'//*[@id="i77"]')
        num.click()

    elif i['nums10'] == 2:
        num = web.find_element(By.XPATH,'//*[@id="i80"]')
        num.click()

    elif i['nums10'] == 3:
        num = web.find_element(By.XPATH,'//*[@id="i83"]')
        num.click()

    elif i['nums10'] == 4:
        num = web.find_element(By.XPATH,'//*[@id="i86"]')
        num.click()

    else:
        num = web.find_element(By.XPATH,'//*[@id="i89"]')
        num.click()

    btn = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div')
    btn.click()


    time.sleep(5)


web.quit()