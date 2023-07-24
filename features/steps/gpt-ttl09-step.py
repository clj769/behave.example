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

# from behave import given, when, then
#
# class NinjaFight(object):
#     """
#     Domain model for ninja fights.
#     """
#     # pylint: disable=R0903
#
#     def __init__(self, with_ninja_level=None):
#         self.with_ninja_level = with_ninja_level
#         self.opponent = None
#
#     def decision(self):
#         """
#         Business logic how a Ninja should react to increase his survival rate.
#         """
#         assert self.with_ninja_level is not None
#         assert self.opponent is not None
#         if self.opponent == "Chuck Norris":
#             return "run for his life"
#         if "black-belt" in self.with_ninja_level:
#             return "engage the opponent"
#         else:
#             return "run for his life"
#
# @given('the ninja encounters another opponent')
# def step_the_ninja_encounters_another_opponent(context):
#     pass
#
# @given('the ninja has a {level} level black-belt')
# def step_given_ninja_has_belt(context, level):
#     level_mapping = {"third": "3rd", "second": "2nd"}  # Mapping English words to belt levels
#     context.fight.with_ninja_level = level_mapping[level]
#
# @when('attacked by {opponent}')
# def step_when_attacked_by(context, opponent):
#     context.fight.opponent = opponent
#
# @then('the ninja should {decision}')
# def step_then_ninja_should(context, decision):
#     assert context.fight.decision() == decision, \
#         f'Expected decision: "{decision}", but got: "{context.fight.decision()}"'
