import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Utilities import configreader
from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Profile(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)
    def OpenPage(self,url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)
    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")
    def Click_loginhomepage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINHOMEPAHEBUTTON_XPATH")
    def Enter_Username(self,username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH",username)
    def Enter_password(self,password):
        self.DynamicImplicitWait(20)
        self.TypeEditBox("PASSWORD_XPATH", password)
    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")
    # def Mouse_hover(self):
    #     self.DynamicImplicitWait(40)
    #     time.sleep(3)
    #     # self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/svg")
    #     # a = ActionChains(self.driver)
    #     # m = self.driver.find_element_by_link_text("shirisha")
    #     # a.move_to_element(m).perform()
    #     # element_to_hover_over =self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/svg")
    #     #
    #     # hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
    #     # hover.perform()
    #     acc=self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/svg")
    #     actions=ActionChains(self.driver)
    #     actions.move_to_element(acc).perform()

    def clickloginLink(self):
        time.sleep(5)
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until( EC.presence_of_element_located((By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div" )))
        e = self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
        a = ActionChains(self.driver)
        a.move_to_element(e)
        a.perform()
        time.sleep(5)

    def Click_profile(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("PROFILE_XPATH")
    def click_edit(self):
        self.DynamicImplicitWait(40)
        # self.driver.execute_script("window.scrollBy(0,400)")
        # self.ClickButton("EDIT_XPATH")
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div/span[2]").click()
    def Enter_name(self,First_name):
        self.DynamicImplicitWait(40)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[1]/form/div[1]/div[1]/div/input").clear()
        # self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[1]/form/div[1]/div[1]/div/input").send_keys("shirisha")
        self.TypeEditBox("FIRST_XPATH", First_name)
    def enterLast_name(self,Last_n):
        self.DynamicImplicitWait(40)
        self.driver.find_element(By.XPATH,"//input[contains(@name,'lastName')]").clear()
        # self.driver.find_element(By.XPATH,"//input[contains(@name,'lastName')]").send_keys(Last_n)
        #self.TypeEditBox("LAST_XPATH", Last_name)
    def gender_button(self):
        self.DynamicImplicitWait(40)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[1]/form/div[3]/label[2]/div[1]").click()
    def save_button(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("save_XPATH")
    # def clickedit(self):
    #     self.DynamicImplicitWait(40)
    #     # self.driver.execute_script("window.scrollBy(0,400)")
    #     # self.ClickButton("EDIT_XPATH")
    #     self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/a[1]").click()
    # def Email_box(self,email):
    #     self.DynamicImplicitWait(40)
    #     self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div/div/input").clear()
    #     # self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]/div[1]/form/div[1]/div[1]/div/input").send_keys("shirisha")
    #     self.TypeEditBoxEmail("email_XPATH", email)
    # def savebutton(self):
    #     self.DynamicImplicitWait(40)
    #     self.ClickButton("savebutton_XPATH")
    #     time.sleep(60)
    # # def otp(self):
    # #     self.DynamicImplicitWait(40)
    # #     self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/form/div[2]/div/input").click()
    # #     time.sleep(20)
    # #     # self.TypeEditBox(OTP)
    # def submit(self):
    #     self.DynamicImplicitWait(40)
    #     self.ClickButton("submit_XPATH")
    #
    # def username(self, uname):
    #     self.DynamicImplicitWait(40)
    #     self.TypeEditBox("user_XPATH", uname)
    #
    # def password(self, passw):
    #     self.DynamicImplicitWait(20)
    #     self.TypeEditBox("pass_XPATH", passw)
    #
    # def login(self):
    #     self.DynamicImplicitWait(40)
    #     self.ClickButton("login_XPATH")
    #     time.sleep(30)
    def manage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("manage_XPATH")
    def add_address(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("addadd_XPATH")
    def name(self,name):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("name_XPATH",name)
    def mobille_number(self,mobilenumber):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("mobile_XPATH",mobilenumber)
    def pincode_box(self,pincode):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("pincode_XPATH", pincode)
    def locality_box(self,locality):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("locality_XPATH", locality)
    def address_box(self,address):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("addres_XPATH",address)
    def save_butt(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SAVED_XPATH")















