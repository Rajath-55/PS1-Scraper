
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import getpass
import csv

url = 'http://psd.bits-pilani.ac.in/Login.aspx'


def login(username, password):
    driver = webdriver.Chrome()
    print("here")
    driver.get(url)

    driver.find_element(By.NAME, "TxtEmail").send_keys(username)

    driver.find_element(By.NAME, "txtPass").send_keys(password)
    driver.find_element(By.NAME, "Button1").click()

    WebDriverWait(driver, 5)
    driver.find_element(By.NAME, "PSI").click()
    wait = WebDriverWait(driver, 5)
    driver.find_element_by_link_text("Problem Bank").click()
    driver.find_element_by_link_text(
        "View Active Station Problem Banks").click()
    wait = WebDriverWait(driver, 10)
    table = driver.find_element(By.ID, "data-table-hrteam")
    # get all of the rows in the table
    rows = table.find_elements(By.TAG_NAME, "tr")
    data = []
    file = open('PS1.csv', 'a+', newline='')
    writer = csv.writer(file)
    reader = csv.reader(file)

    check = 0
    tags = {}
    for row in rows:
        if check == 0:
            print(row.text)

            heading = str(row.text).split(' ')
            headings = [heading[0], heading[1], str(
                heading[2]) + " " + str(heading[3]), str(heading[4]) + " " + str(heading[5]), "Batch", "Institute Scholarship (If any)", "No. of Projects", "Disciplines"]
            writer.writerow(headings)

        check += 1
        temp = []
        # for col in row.find_elements_by_tag_name('td'):
        #     if col.text == "View":
        #         WebDriverWait(driver,2)
        #         col.click()
        #         WebDriverWait(driver, 2)
        #         try:
        #             new_row = driver.find_elements(By.ID, "trapplylist4")
        #             for new_col in new_row.find_elements_by_tag_name("td"):
        #                 temp.append(new_col.text)
        #             WebDriverWait(driver,2)
        #             temp = 0
        #         except:
        #             pass

        splitted = str(row.text).split(' ')
        tags[splitted[0]] = 'aaa'
        station_type = splitted[len(splitted) - 2]
        loc = splitted[1]
        name = ''
        for i in range(2, len(splitted) - 2):
            name += splitted[i]
            name += " "
        if check != 0:
            data.append([loc, name, station_type, "Summer 2021", "None", "A3, A7"])

    for i in range(1, len(data)):
        new_data = [i] + data[i]
        writer.writerow(new_data)

    # print(data)
    file.close()
    print(check)
    if check > 504:
        return
    while True:
        pass


if __name__ == '__main__':
    print("Enter your BITSmail ID : ", end=" ")
    username = str(input())
    password = getpass.getpass("Enter your password : ")
    login(username, password)
