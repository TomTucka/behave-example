Feature: Behave Selenium Showcase

    Scenario: Google is available
        When I am on 'Google'
        Then The page title should be Google

    Scenario: GOV.UK is available
        When I am on 'GOV UK'
        Then The page title should be Welcome to GOV.UK

    Scenario: Make a lasting power of attorney online
        When I am on 'LPA Online'
        Then The page title should be Blah