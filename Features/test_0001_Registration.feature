Feature: Login
This feature file is designed to test the Registration for Automation Practice website

    Scenario: To test the Registration process
        Given User opens the Automation Practice website
        When User clicks Sign-in Page
        And User clicks create account
        And User enters the mandatory details in the form
        Then New Account is created
        And Name is appearing in the page
        And User logs out
