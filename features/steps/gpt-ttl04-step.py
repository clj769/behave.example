from behave import given, when, then
from blender import Blender   # Please replace with your actual module

@given('I put "{thing}" in a blender')
def step_given_put_thing_in_blender(context, thing):
    context.blender = Blender()
    context.blender.add(thing)

@when('I switch the blender on')
def step_when_switch_blender_on(context):
    context.blender.switch_on()

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    assert context.blender.result == other_thing, \
        f'Expected "{other_thing}", but got "{context.blender.result}"'
