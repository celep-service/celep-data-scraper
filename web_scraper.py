
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# 무신사 의류 스크래핑

# 브라우저 실행
browser = webdriver.Edge() # 괄호안에 드라이버 경로를 넣어준다.(같은 폴더에 있으면 안넣어도 됨)
browser.maximize_window() # 창 최대화



# 무신사 의류 페이지 접속
url = "https://www.musinsa.com/ranking/best?period=week&age=ALL&mainCategory=005&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=true&exclusive=false&discount=false&soldOut=false&page=1&viewType=small&priceMin=&priceMax=#pol3487878"
file_name = "musinsa_shoes"
browser.get(url)

# 이미지 로딩을 위해 스크롤을 내린다
# 스크롤 내리기
for i in range(1, 11):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/10*"+str(i)+")")
    time.sleep(0.5)
# 3초간 대기
time.sleep(1)

# 의류 정보 가져오기
goods_rank_list = browser.find_elements(By.XPATH, '//ul[@id="goodsRankList"]/li')
print(len(goods_rank_list))

filename = file_name+'.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
# newline 옵션을 주지 않으면 한줄씩 띄어지는 현상이 발생한다.
writer = csv.writer(f)

# 의류정보 하나씩 찢기
# csv 파일로 저장
time.sleep(1)

for idx, good in enumerate(goods_rank_list):
    
    # 의류 브랜드
    good_brand = good.find_element(By.XPATH, './/p[@class="item_title"]/a')
    #print(good_brand.text)
    # 의류 이름
    good_name = good.find_element(By.XPATH, './/p[@class="list_info"]/a')
    #print(good_name.text)
    # 의류 가격
    good_price = good.find_element(By.XPATH, './/p[@class="price"]')
    # 내부에 있는 del 태그를 제거
    if good_price.find_elements(By.XPATH, './/del'):
        del_tag = good_price.find_element(By.XPATH, './/del')
        browser.execute_script('arguments[0].remove()', del_tag)
    #print(good_price.text)
    # 의류 이미지
    good_img = good.find_element(By.XPATH, './/img')
    #print(good_img.get_attribute('src'))
    # 의류 링크
    good_link = good.find_element(By.XPATH, './/p[@class="list_info"]/a')
    #print(good_link.get_attribute('href'))
    #print('-' * 50)
    
    # csv 파일로 저장
    writer.writerow([good_brand.text, good_name.text.strip(), good_img.get_attribute('src'), good_link.get_attribute('href'), good_price.text])


time.sleep(1)
browser.quit()


