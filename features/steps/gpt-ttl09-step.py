# from behave import given, when, then
#
# class Ninja:
#     def __init__(self, belt_level):
#         self.belt_level = belt_level
#
#     def encounter(self):
#         pass
#
#     def attack(self, opponent):
#         if opponent == "Chuck Norris" or self.belt_level < 3:
#             return "run for his life"
#         else:
#             return "engage the opponent"
#
# @given('the ninja encounters another opponent')
# def step_given_the_ninja_encounters_another_opponent(context):
#     pass
#
# @given('the ninja has a third level black-belt')
# def step_given_the_ninja_has_a_third_level_black_belt(context):
#     context.ninja = Ninja(3)
#
# @given('the ninja has a second level black-belt')
# def step_given_the_ninja_has_a_second_level_black_belt(context):
#     context.ninja = Ninja(2)
#
# @when('attacked by a samurai')
# def step_when_attacked_by_a_samurai(context):
#     context.ninja_action = context.ninja.attack("samurai")
#
# @when('attacked by Chuck Norris')
# def step_when_attacked_by_chuck_norris(context):
#     context.ninja_action = context.ninja.attack("Chuck Norris")
#
# @then('the ninja should engage the opponent')
# def step_then_the_ninja_should_engage_the_opponent(context):
#     assert context.ninja_action == "engage the opponent"
#
# @then('the ninja should run for his life')
# def step_then_the_ninja_should_run_for_his_life(context):
#     assert context.ninja_action == "run for his life"
