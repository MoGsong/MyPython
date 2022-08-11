from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.maltego.com/ce-registration/')
bro.switch_to.frame('login_frame')
# 快捷登录
# user = bro.find_element_by_id('img_out_1986523538')
# user.click()
table = bro.find_elements_by_id('register-community__form')
reg_FN = bro.find_elements_by_class_name('license_firstname')  # copy--bold copy--grey copy-high label  "
reg_LN = bro.find_elements_by_class_name('license_lastname')
reg_phone = bro.find_elements_by_class_name('phone')
reg_email = bro.find_elements_by_class_name('license_email')
reg_password = bro.find_elements_by_class_name('password')
reg_FN.insert()
reg_password_confirm = bro.find_elements_by_class_name('password_confirm')
check = bro.find_elements_by_class_name('recaptcha-anchor-label')
check_message = bro.find_element_by_xpath('//*[@id="recaptcha-anchor"]')
while(True):
    if 'Ture' not in check_message:
        check.click()


# 账号密码登录
# log_page = bro.find_element_by_id('switcher_plogin')
# log_page.click()
# user = bro.find_element_by_id('u')
# password =bro.find_element_by_id('p')
# user.send_keys('1070962214')
# sleep(2)
# password.send_keys('SHEisWDS1399')
# sleep(1)
# login_btn = bro.find_element_by_id('login_button')
# login_btn.click()