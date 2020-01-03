# coding:utf-8
from selenium import webdriver
from multiprocessing import Pool
import time
from functools import partial

# 配置浏览器信息（引入默认浏览器数据路径）
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\于泽川\AppData\Local\Google\Chrome\User Data")

# 主运行函数
#
def get_url(url):
    browser = webdriver.Chrome(options = options)
    browser.get(url)
    time.sleep(3)
    # sign_in(browser)
    # time.sleep(1)
    for i in range(1,13):
        parse(browser,i)

def parse(browser,i):
    browser.switch_to_window(browser.window_handles[0])
    click_one = browser.find_element_by_css_selector('#classify-list > dl > dd:nth-child(' + str(i) + ') > a > cite')
    click_one.click()
    # time.sleep(1)
    browser.switch_to_window(browser.window_handles[1])
    click_names(browser)
    browser.close()

# 登录
# def sign_in(browser):
#     time.sleep(3)
#     click_in = browser.find_element_by_css_selector('#login-btn')
#     click_in.click()
#     time.sleep(10)
#     browser.switch_to_alert().dismiss()
    # alert = browser.switch_to_alert().accept()
    # time.sleep(2)
    # input_name = browser.find_element_by_css_selector('#username')
    # # input_name = alert.find_element_by_css_selector('#username')
    # input_name.send_keys('18730297218')
    # time.sleep(1)
    # input_pwd = browser.find_element_by_css_selector('#password')
    # # input_pwd = alert.find_element_by_css_selector('#password')
    # input_pwd.send_keys('1031833yy')
    # time.sleep(1)
    # click_init = browser.find_element_by_css_selector('#password')
    # # click_init = alert.find_element_by_css_selector('#j-inputMode > div.login-common-wrap > a')
    # click_init.click()

# 点击书名
def click_names(browser):
    # browser = webdriver.Chrome(options=options)
    for i in range(1,11):
        browser.switch_to_window(browser.window_handles[1])
        time.sleep(1)
        click_name = browser.find_element_by_css_selector('body > div.wrap > div.box-center > div.focus-wrap.mb40.cf > div.week-rec-wrap.fl > div > ul > li:nth-child('+str(i)+') > em > a')
        click_name.click()
        # time.sleep(1)
        browser.switch_to_window(browser.window_handles[2])
        click_read(browser)
        browser.close()
    browser.switch_to_window(browser.window_handles[1])

# 点击阅读
def click_read(browser):
    # browser = webdriver.Chrome(options=options)
    click_read = browser.find_element_by_css_selector('#readBtn')
    click_read.click()

if __name__ == '__main__':
    get_url('https://www.qidian.com/')