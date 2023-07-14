# from behave import given, when, then
#
# class Blender:
#     def __init__(self):
#         self.contents = ""
#
#     def add(self, item):
#         self.contents = item
#
#     def switch_on(self):
#         if self.contents == "Red Tree Frog":
#             self.contents = "mush"
#         elif self.contents == "apples":
#             self.contents = "apple juice"
#         elif self.contents in ["iPhone", "Galaxy Nexus"]:
#             self.contents = "toxic waste"
#
# @given('I put "{thing}" in a blender')
# def step_given_i_put_thing_in_blender(context, thing):
#     context.blender = Blender()
#     context.blender.add(thing)
#
# @when('I switch the blender on')
# def step_when_i_switch_the_blender_on(context):
#     context.blender.switch_on()
#
# @then('it should transform into "{other_thing}"')
# def step_then_it_should_transform_into_other_thing(context, other_thing):
#     assert context.blender.contents == other_thing
