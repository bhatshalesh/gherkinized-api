Feature: Task API

  Scenario: Get tasks when no tasks exist
    Given the task list is empty
    When I request the list of tasks
    Then I should receive an empty list

  Scenario: Create a new task
    Given the task list is empty
    When I create a task with title "Buy milk"
    Then the task list should contain a task with title "Buy milk"
