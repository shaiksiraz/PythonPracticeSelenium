from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

rows=driver.find_elements_by_xpath("//body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")
print(" No.of rows are : ", len(rows))
for row in range(1,len(rows)+1):
    cols = driver.find_elements_by_xpath("//body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr["+str(row)+"]/td")
    print()
    for col in range(1,len(cols)+1):
        columnobject=driver.find_element_by_xpath("//body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr["+str(row)+"]/td["+str(col)+"]")
        print(columnobject.text, end="     ")
# //body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]
# //body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]
driver.quit()