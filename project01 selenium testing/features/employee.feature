Feature: employee add a requst

  Background: : logging as an employee
    Given The Guest is on the logging Home Page
    When The Guest types abc into the username bar
    When The Guest types 123 into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say welcome to employee
    When The guest clicks ok on  alert prompt
    Then The guest should be on employee page



  Scenario Outline: adding a request

    When The Guest types <amount> into the amount bar
    When The Guest types <reason> into the reason bar
    When The Guest types <status> into the status bar
    When The Guest clicks on the add button
    Then The prompt alert text should be <text>
    When The guest clicks ok on  alert prompt


    Examples:
      | amount | reason | status | text |
      | 1000 | travel | pending | The request was successfully added |
      | 20000 | cost | accepted | The request was successfully added |



   Scenario Outline: adding a request with an empty filed

     When The Guest types <amount> into the amount bar
     When The Guest types <reason> into the reason bar
     When The Guest clicks on the add button
     Then The prompt alert text should be <text>
     When The guest clicks ok on  alert prompt


    Examples:
      | amount | reason | text |
      | 90000 | accepted | Some filels are still empty |


    Scenario Outline: adding a request with wrong value type for amount

          When The Guest types <amount> into the amount bar
    When The Guest types <reason> into the reason bar
    When The Guest types <status> into the status bar
    When The Guest clicks on the add button
    Then The prompt alert text should be <text>
    When The guest clicks ok on  alert prompt


    Examples:
      | amount | reason | status | text |
      | abc | travel | pending | Some filels are still empty |
      | akkk | cost | accepted | Some filels are still empty |

