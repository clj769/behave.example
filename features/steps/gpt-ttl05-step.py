# from behave import given, when, then
#
# class Frobulator:
#     def __init__(self, text):
#         self.text = text
#
#     def activate(self):
#         return "English"
#
# @given('a sample text loaded into the frobulator')
# def step_given_a_sample_text_loaded_into_the_frobulator(context):
#     context.frobulator = Frobulator(context.text)
#
# @when('we activate the frobulator')
# def step_when_we_activate_the_frobulator(context):
#     context.frobulator_result = context.frobulator.activate()
#
# @then('we will find it similar to English')
# def step_then_we_will_find_it_similar_to_english(context):
#     assert context.frobulator_result == "English"
