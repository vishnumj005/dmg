Feature: Login
Different channels are provided for user to login/sign-up

    @regression
    Scenario: User is trying to Login using the username and password textbox
        Given User opens the Automation Practice website
        When User clicks Sign-in Page
        And User enters username and password and clicks sign-in button
        Then Verify the name is appearing in home page