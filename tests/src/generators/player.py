from tests.src.enums.user_enums import Status
from tests.src.generators.player_localization import PlayerLocalization

from tests.src.baseclasses.builder import BuilderBassClass

class Player(BuilderBassClass):

    def __init__(self):
        super().__init__()
        self.reset()
    
        
    def set_status(self, status=Status.ACTIVE.value):
        self.result['account_status'] = status
        return self
    
    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self
    
    def set_avatar(self, avatar="http://example.com/avatar.png"):
        self.result['avatar'] = avatar
        return self
    
    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result["localization"] = {
            'EN': PlayerLocalization("en_US").build(),
            'RU': PlayerLocalization("ru_RU").build(),
            }
        return self
    


    
# x = Player().set_status("ГОВНО").set_balance(20).build()
# print(x)
