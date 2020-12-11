# Created by ntowers at 11/12/20
Feature: Ticket System
  # Internal ticket system

  Scenario: Create Ticket
    Given A ticket system
    When A customer claim
    Then Create a ticket with the customer issue

  Scenario: Link Ticket to Project
    Given A created ticket
    When A customer claim
    Then Link ticket to corresponding project

  Scenario: Add project resources to Ticket
    Given A created ticket
    When A customer claim
    Then Add determined project resources to the ticket

  Scenario: Change Ticket description
    Given A created ticket
    When A customer issue changes
    Then Change description in a created ticket

  Scenario: Close ticket
    Given A created ticket
    When A customer issue is solved
    Then Close the created ticket