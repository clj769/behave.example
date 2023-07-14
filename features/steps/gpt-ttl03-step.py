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
#         if self.contents == "apples":
#             self.contents = "apple juice"
#
# @given('I put "{item}" in a blender')
# def step_given_i_put_item_in_blender(context, item):
#     context.blender = Blender()
#     context.blender.add(item)
#
# @when('I switch the blender on')
# def step_when_i_switch_the_blender_on(context):
#     context.blender.switch_on()
#
# @then('it should transform into "{result}"')
# def step_then_it_should_transform_into_result(context, result):
#     assert context.blender.contents == result
