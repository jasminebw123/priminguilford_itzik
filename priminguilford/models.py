from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'The A Team'

doc = """
A Guilford Task (Alternate Uses Task) + priming - An operation of one's creativity
 by semantic priming of a distant/close to the object the player will be 
 asked to come up with uses to (A within subjects experiment).
"""


class Constants(BaseConstants):
    name_in_url = 'a_team_experiment'
    players_per_group = None
    tasks = ["OfficeClip", "SheetProtector"]
    num_rounds = len(tasks)
    num_uses = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
                p.participant.vars['task_name'] = Constants.tasks[self.round_number]
                

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics:
    gender = models.StringField(label="Gender", choices=["Male", "Female", "Other"], blank=True)
    yoe = models.IntegerField(label="Years of Education", min=1, max=50, blank=True)
    residence = models.StringField(label="Your current residence city", blank=True)
    age = models.IntegerField(label="Age", min=20, max=90, blank=True)
    youth_mov = models.IntegerField(label="How many years did you attend a youth movement?",
                                    min=0, max=30, blank=True)
    psychometric = models.IntegerField(label="Your psychometric grade (if you don't have one, please type 100",
                                       min=100, max=800, blank=True)
    #condition = label="condition"
    # other variables, for other uses:
    use1 = models.StringField(label="use1", blank=False)
    use2 = models.StringField(label="use2", blank=True)
    use3 = models.StringField(label="use3", blank=True)
    use4 = models.StringField(label="use4", blank=True)
    use5 = models.StringField(label="use5", blank=True)
    use6 = models.StringField(label="use6", blank=True)
    use7 = models.StringField(label="use7", blank=True)
    use8 = models.StringField(label="use8", blank=True)
    use9 = models.StringField(label="use9", blank=True)
    use10 = models.StringField(label="use10", blank=True)
  