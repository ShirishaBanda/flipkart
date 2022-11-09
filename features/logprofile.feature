Feature: profile flipkart
  Scenario Outline: profile  data
    Given We are on flipkart website
    When click login
    Then Enter your "<username>" in the feild
    And Enter your "<password>" in the box
    And click login
    When we hover over Login Button
    When user clicks on  My profile
    Then user clicks on edit button
    Then user enters the "<First_name>"
    Then user enters "<Last_n>"
    Then chooses the gender
    Then clicks on save button
#    Then click the email edit
#    Then type the "<email>"
#    Then save button clicked
##    Then "<OTP>" entered
#    Then click submit
#    Then again "<uname>" entered
#    Then "<passw>" entered
#    Then login clicked
    When user clicks on Manage Addresses
    Then user clicked add address
    Then user entered "<name>"
    And user enters "<mobilenumber>" on number
    And enter "<pincode>"
    And user enter the "<locality>"
    And user types "<address>"
    Then click on save button
    Examples:
      | username | password | First_name | Last_n | email | uname | passw |name | mobilenumber | pincode | locality | address |
      | 9182539988 | Shirisha@23 | shirisha | banda | shirishabanda67@gmail.com | 9182539988 | Shirisha@23 | shirisha | 9182539988 | 508278 |  marupaka | h.no:84,marupaka |

