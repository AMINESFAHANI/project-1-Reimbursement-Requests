Feature: logging

  Background: logging Home Page
    Given The Guest is on the logging Home Page


  Scenario: cenario: logging as an employee
    When The Guest types abc into the username bar
    When The Guest types 123 into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say welcome to employee
    When The guest clicks ok on  alert prompt
    Then The guest should be on employee page

  Scenario: logging as a manager
    When The Guest types abc into the username bar
    When The Guest types xyz into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say welcome to manager
    When The guest clicks ok on  alert prompt
    Then The guest should be on manager page

  Scenario: logging with wrong credential
    When The Guest types abcd into the username bar
    When The Guest types xyz into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say username or password is not correct
    When The guest clicks ok on  alert prompt


