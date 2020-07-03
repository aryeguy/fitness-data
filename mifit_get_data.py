from selenium import webdriver
import time
import os


def main():
    password = os.environ.get('GOOGLE_PASSWORD', '')
    browser = webdriver.Chrome()
    browser.get('https://api-mifit.huami.com/t/account_mifit')
    export_data_button = browser.find_element_by_xpath('//*[@id="chooseOpt"]/div/div[4]')
    export_data_button.click()
    time.sleep(2)
    ok_button = browser.find_element_by_xpath('//*[@id="step1"]')
    ok_button.click()
    time.sleep(2)
    google_auth_button = browser.find_element_by_xpath('//*[@id="login3Link"]/li[4]/form/button')
    google_auth_button.click()
    time.sleep(2)
    google_email_input = browser.find_element_by_xpath('//*[@id="identifierId"]')
    google_email_input.send_keys('arye.guy@gmail.com')
    google_email_input.send_keys('\n')
    time.sleep(2)
    google_password_input = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    google_password_input.send_keys(password)
    google_password_input.send_keys('\n')
    time.sleep(20)
    body_data_checkbox = browser.find_element_by_xpath('//*[@id="clearData"]/li[5]')
    body_data_checkbox.click()
    time.sleep(2)
    from_selector_input = browser.find_element_by_xpath('//*[@id="startTime"]')
    from_selector_input.click()
    time.sleep(2)
    continue_button = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/span[2]')
    continue_button.click()
    time.sleep(2)
    to_selector_input = browser.find_element_by_xpath('//*[@id="endTime"]')
    to_selector_input.click()
    time.sleep(2)
    for i in range(6):
        year_wheel_down = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[1]/ul/li[2]')
        year_wheel_down.click()
        time.sleep(2)
    for i in range(11):
        month_wheel_down = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/ul/li[2]')
        month_wheel_down.click()
        time.sleep(2)
    for i in range(30):
        day_wheel_down = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/ul/li[31]')
        day_wheel_down.click()
        time.sleep(2)
    continue_button = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/span[2]')
    continue_button.click()
    time.sleep(2)
    # TODO
    time.sleep(2)
    time.sleep(2)

    time.sleep(100)


if __name__ == '__main__':
    main()
