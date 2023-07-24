# from behave import given, when, then
#
# class Frobulator(object):
#     def __init__(self, text=None):
#         self.text = None
#         self.activated = False
#
#     def activate(self):
#         self.activated = True
#
#     def seems_like_language(self):
#         """
#         Business logic how frobulator should react/oracle on text data.
#         """
#         assert self.text is not None
#         assert self.activated
#         if self.text.startswith("Lorem ipsum"):
#             return "English"
#         else:
#             return "UNKNOWN"
#
# @given('a sample text loaded into the frobulator')
# def step_given_load_text_into_frobulator(context):
#     context.frobulator = Frobulator()
#     context.frobulator.text = context.text
#
# @when('we activate the frobulator')
# def step_when_activate_frobulator(context):
#     context.frobulator.activate()
#
# @then('we will find it similar to English')
# def step_then_find_it_similar_to_english(context):
#     result = context.frobulator.seems_like_language()
#     assert result == "English", f'Expected "English", but got "{result}"'
