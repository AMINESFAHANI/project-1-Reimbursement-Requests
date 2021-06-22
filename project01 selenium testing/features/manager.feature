Feature: manager update a request



  Background: : : : logging as a manager
    Given The Guest is on the logging Home Page
    When The Guest types abc into the username bar
    When The Guest types xyz into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say welcome to manager
    When The guest clicks ok on  alert prompt
    Then The guest should be on manager page



  Scenario Outline: updating a request

    When The Guest types <id> into the id bar
    When The Guest types <status> into the request status bar
    When The Guest clicks on the update button
    Then The prompt alert text should be <text>
    When The guest clicks ok on  alert prompt


    Examples:
      | id | status | text |
      | 10 | pending | The request was successfully updated |
      | 12255 | accepted | The resource was not found |
      | 7 | rejected | The request was successfully updated |
      | 0 | pending | The resource was not found |

        Scenario Outline: updating a request with an empty field

    When The Guest types <id> into the id bar
    When The Guest clicks on the update button
    Then The prompt alert text should be <text>
    When The guest clicks ok on  alert prompt


    Examples:
      | id | text |

      | 32 | Some filels are still empty |
      | 10 | Some filels are still empty |