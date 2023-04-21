# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 設定 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="/Users/liaohanlin/training/chromedriver"
# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
# 連線到 PTT 股票版
# 取得股票版中的文章標題
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
print(driver.page_source) # 取得網頁的原始碼
tags=driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)
# 取得上一頁的文章標題
nextPage=driver.find_element(By.LINK_TEXT,"‹ 上頁")
nextPage.click() # 模擬使用者的點擊
tags=driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)

driver.close()

i=0
while i < 4:
  tags=driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 屬性是 title 的所有標籤
  for tag in tags:
    print(tag.text)
  i+=1
  nextPage=driver.find_element(By.LINK_TEXT,"‹ 上頁")
  nextPage.click()
driver.close()