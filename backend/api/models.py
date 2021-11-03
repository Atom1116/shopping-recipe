class MaterialPostModel(object):
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit


class ProcedurePostModel(object):
    def __init__(self, order, contents,):
        self.order = order
        self.contents = contents


class RecipePost(object):
    def __init__(self, title, materials,):
        self.title = title
        self.materials = materials
        # self.procedure = procedure
