class BaseModel:
    _id_counter = 1

    def __init__(self):
        self.id = BaseModel._id_counter
        BaseModel._id_counter += 1

    def to_dict(self):
        return {"id": self.id}