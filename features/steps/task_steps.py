import requests
from behave import given, when, then

BASE_URL = "http://127.0.0.1:5000"

@given("the task list is empty")
def step_impl(context):
    # Assuming task list is in-memory, just a placeholder
    context.expected_tasks = []

@when("I request the list of tasks")
def step_impl(context):
    response = requests.get(f"{BASE_URL}/tasks")
    context.response = response

@then("I should receive an empty list")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json() == context.expected_tasks

@when('I create a task with title "{title}"')
def step_impl(context, title):
    response = requests.post(f"{BASE_URL}/tasks", json={"title": title})
    context.response = response
    context.created_title = title

@then('the task list should contain a task with title "{title}"')
def step_impl(context, title):
    response = requests.get(f"{BASE_URL}/tasks")
    tasks = response.json()
    titles = [task["title"] for task in tasks]
    assert title in titles

