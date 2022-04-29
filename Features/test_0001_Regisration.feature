Feature: Login
Different channels are provided for user to login/sign-up

    @regression
    Scenario: User is trying to Login using the username and password textbox
        Given User opens login in page
        When User enters username and password and clicks sign-in button
        And User is in Home page
        Then User is logged-in

    @regression @sse-4332
    Scenario Outline: Login functionality with Negative emailid  and valid password
        Given User opens login in page
        When the User enters "<invalid_email>" into username and valid credential on the other textbox
        Then verify wrong_email will display a "<warning_message>" under the textbox
        Examples:
        |  invalid_email     |    warning_message                 |
        |  abc@jjj.com       |    Email not found                 |
        |  null              |    Invalid Email address           |

    @regression  @sse-4332
    Scenario Outline: Login functionality with Negative password  and valid email
        Given User opens login in page
        When the User enters "<invalid_password>" into password and valid credential on the other textbox
        Then verify wrong_password will display a "<warning_message>" under the textbox
        Examples:
        |  invalid_password     |    warning_message                  |
        |  test1                |    Password does not match          |
        |                       |    Password cannot be empty         |
        |  tt                   |    Login failed due to some reason. |
