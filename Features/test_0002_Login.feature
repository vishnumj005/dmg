Feature: Login
This feature file is designed to test the Login for Automation Practice website

    Scenario: User is trying to Login using the username and password textbox
        Given User opens the Automation Practice website
        When User clicks Sign-in Page
        And User enters username and password and clicks sign-in button
        Then Verify the name is appearing in home page
        Then User logs out

    Scenario Outline: Login functionality with wrong emailid and valid password
        Given User opens the Automation Practice website
        When User clicks Sign-in Page
        And User enters "<invalid_username>" into username and valid password on the other textbox
        Then Verify the "<warning_message>"
        Examples:
        |  invalid_username     |    warning_message                 |
        |  abc@jjj.com          |    Authentication failed.          |
        |  null                 |    Invalid email address.          |

    Scenario Outline: Login functionality with wrong password and valid emai
        Given User opens the Automation Practice website
        When User clicks Sign-in Page
        And User enters valid username into username and "<invalid_password>" into the other textbox
        Then Verify the "<warning_message>"
        Examples:
        |  invalid_password     |    warning_message                 |
        |  automationtest       |    Authentication failed.          |
        |  null                 |    Invalid password.               |