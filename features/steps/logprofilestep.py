import time

from behave import *
from Utilities.configreader import ConfigReader
from features.pageobject.profile import Profile

@given(u'We are on flipkart website')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given We are on flipkart website')
    context.profile = Profile(context.driver)
    context.profile.OpenPage(ConfigReader("base info", "URL"))
    context.profile.clickclose()

@when(u'click login')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When click login')
    context.profile.Click_loginhomepage()

@then(u'Enter your "{username}" in the feild')
def step_impl(context,username):
    # raise NotImplementedError(u'STEP: Then Enter your "9182539988" in the feild')
    context.profile.Enter_Username(username)

@then(u'Enter your "{password}" in the box')
def step_impl(context,password):
    # raise NotImplementedError(u'STEP: Then Enter your "Shirisha@23" in the box')
    context.profile.Enter_password(password)

@then(u'click login')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then click login')
    context.profile.Click_login()

# @when(u'user mousehover on my account')
# def step_impl(context):
#     # raise NotImplementedError(u'STEP: When user mousehover on my account')
#     context.profile.Mouse_hover()
@when(u'we hover over Login Button')
def step_impl(context):
    context.reg = Profile(context.driver)
    context.reg.clickloginLink()
@when(u'user clicks on  My profile')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When user clicks on  My profile')
    context.profile.Click_profile()

@then(u'user clicks on edit button')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then user clicks on edit button')
    context.profile.click_edit()

@then(u'user enters the "{First_name}"')
def step_impl(context,First_name):
    # raise NotImplementedError(u'STEP: Then user enters "shirisha"')
    context.profile.Enter_name(First_name)

@then(u'user enters "{Last_n}"')
def step_impl(context,Last_n):
    # raise NotImplementedError(u'STEP: Then user enters "Banda"')
    context.profile.enterLast_name(Last_n)

@then(u'chooses the gender')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then chooses the gender')
    context.profile.gender_button()

@then(u'clicks on save button')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then clicks on save button')
    context.profile.save_button()
# @then(u'click the email edit')
# def step_impl(context):
#     context.profile.clickedit()
# @then(u'type the "{email}"')
# def step_impl(context,email):
#     context.profile.Email_box(email)
# @then(u'save button clicked')
# def step_impl(context):
#     context.profile.savebutton()
# # @then(u'"{OTP}" entered')
# # def step_impl(context):
# #     time.sleep(10)
# #     context.profile.otp()
# time.sleep(10)
# @then(u'click submit')
# def step_impl(context):
#     context.profile.submit()
#     time.sleep(30)
# @then(u'again "{uname}" entered')
# def step_impl(context,uname):
#     # raise NotImplementedError(u'STEP: Then Enter your "9182539988" in the feild')
#     context.profile.username(uname)
#
# @then(u'"{passw}" entered')
# def step_impl(context,passw):
#     # raise NotImplementedError(u'STEP: Then Enter your "Shirisha@23" in the box')
#     context.profile.password(passw)
#
# @then(u'login clicked')
# def step_impl(context):
#     # raise NotImplementedError(u'STEP: Then click login')
#     context.profile.login()
@when(u'user clicks on Manage Addresses')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When user clicks on Manage Addresses')
    context.profile.manage()
@then(u'user clicked add address')
def step_impl(context):
    context.profile.add_address()

@then(u'user entered "{name}"')
def step_impl(context,name):
    context.profile.name(name)

@then(u'user enters "{mobilenumber}" on number')
def step_impl(context,mobilenumber):
    # raise NotImplementedError(u'STEP: Then user enters "9182539988"')
    context.profile.mobille_number(mobilenumber)

@then(u'enter "{pincode}"')
def step_impl(context,pincode):
    #raise NotImplementedError(u'STEP: Then user enters "508278"')
    context.profile.pincode_box(pincode)

@then(u'user enter the "{locality}"')
def step_impl(context,locality):
    # raise NotImplementedError(u'STEP: Then user enters "marupaka"')
    context.profile.locality_box(locality)

@then(u'user types "{address}"')
def step_impl(context,address):
    # raise NotImplementedError(u'STEP: Then user enters "h.no:84,marupaka"')
    context.profile.address_box(address)

@then(u'click on save button')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then click on save button')
    context.profile.save_butt()