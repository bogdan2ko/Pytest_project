class BuilderBassClass:
    def __init__(self):
        self.result={}


    def update_inner_value(self, keys, value):
        if not isinstance(keys,list):
            self.result[keys] = value
        else:
            temporary = self.result
            for items in keys[:-1]:
                if  items not in temporary.keys():
                    temporary[items] = {}
                temporary = temporary[items]
            temporary[keys[-1]] = value
        return self
    
    def build(self):
        return self.result
    