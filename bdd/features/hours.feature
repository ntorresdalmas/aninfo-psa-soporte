Feature: Hour Load System
  # Internal hour load system


  Scenario: Authenticate with credentials
    Given An hour system
    When A worker tries to authenticate with valid credentials
    Then Grant access

  Scenario: Authenticate with credentials
    Given An hour system
    When A worker tries to authenticate with invalid credentials
    Then Offer retry

  Scenario: Access to menu
    Given An hour system
    When A worker selects menu option
    Then Show menu

  Scenario: Select a project
    Given An hour system
    When A worker chooses a project
    Then Show project options

  Scenario: Load Hours
    Given An hour system
    When A worker enters the number_of_hours worked
    Then Link the number of hours to his/her profile