# from behave import given, when, then
#
# class Ninja:
#     def __init__(self, level):
#         self.level = level
#
#     def react_to_attack(self, opponent):
#         if opponent == 'samurai':
#             return 'engage'
#         elif opponent == 'Chuck Norris':
#             return 'run for his life'
#
# @given('the ninja has a third level black-belt')
# def step_given_the_ninja_has_third_level_black_belt(context):
#     context.ninja = Ninja('third level black-belt')
#
# @when('attacked by a samurai')
# def step_when_attacked_by_a_samurai(context):
#     context.ninja_reaction = context.ninja.react_to_attack('samurai')
#
# @then('the ninja should engage the opponent')
# def step_then_ninja_should_engage_opponent(context):
#     assert context.ninja_reaction == 'engage'
#
# @when('attacked by Chuck Norris')
# def step_when_attacked_by_chuck_norris(context):
#     context.ninja_reaction = context.ninja.react_to_attack('Chuck Norris')
#
# @then('the ninja should run for his life')
# def step_then_ninja_should_run_for_his_life(context):
#     assert context.ninja_reaction == 'run for his life'
