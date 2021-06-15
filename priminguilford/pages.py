from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from PIL import Image
import random


class Instructions(Page):
    form_model = "player"
    def is_displayed(self):
        return self.round_number == 1

class Primming(Page):
    timeout_seconds = 1
    form_model = "player"
    def is_displayed(self):
        return self.round_number < Constants.num_rounds +1
    def vars_for_template(self):
        return dict(image_path='{}.png'.format(self.round_number+1))
    
    
class Task(Page):
    timeout_seconds = 120.00
    form_model = "player"
    form_fields = [ "use1", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10"]
    def is_displayed(self):
        return self.round_number < Constants.num_rounds +1
    #passing the number of the image to the page
    def vars_for_template(self):
        return dict(image_path='{}.png'.format(self.round_number))


class Demographics(Page):
    form_model = "player"
    form_fields = ["age", "residence", "gender", "yoe", "psychometric", "youth_mov"]
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [Instructions, Primming, Task, Demographics]






# randomized_order = list(range(1, 7))
# random_order = random.shuffle(randomized_order)