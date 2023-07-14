# from behave import given, when, then
#
# class Game:
#     def __init__(self):
#         self.level = 0
#
#     def start(self):
#         self.level = 1
#
#     def press_big_red_button(self):
#         self.level += 1
#
#     def duck(self):
#         self.level += 1
#
# @given('I start a new game')
# def step_given_i_start_a_new_game(context):
#     context.game = Game()
#     context.game.start()
#
# @when('I press the big red button')
# def step_when_i_press_the_big_red_button(context):
#     context.game.press_big_red_button()
#
# @when('I duck')
# def step_when_i_duck(context):
#     context.game.duck()
#
# @when('I do the same thing as before')
# def step_when_i_do_the_same_thing_as_before(context):
#     context.execute_steps("""
#         When I press the big red button
#          And I duck
#     """)
#
# @then('I reach the next level')
# def step_then_i_reach_the_next_level(context):
#     assert context.game.level == 3
