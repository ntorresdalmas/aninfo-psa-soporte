from behave import *


@given("An hour system")
def step_impl(context, amount):
    pass

@when("A {worker} enters the {number_of_hours} worked")
def step_impl(context, worker, number_of_hours):
    assert(number_of_hours >= 0)
    if context.number_of_hours >= 0:
        context.worker = number_of_hours
        context.valid_hours = True

@then("Link the number of hours to his/her profile")
def step_impl(context):
    assert context.failed is False
    assert context.valid_hours is True
    assert context.worker is not None