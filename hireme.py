from itertools import count

class MestFellows:
    _ids = count(1)

    def __init__(self) :
        self.id = next(self._ids)
        if  (self.id > 3):
            return

    def get_count(self):
        return self.id


fellow1 = MestFellows()
# print(fellow1.get_count())
fellow2 = MestFellows()

print(fellow2.get_count())
fellow3 = MestFellows()

fellow4 = MestFellows()
fellow5 = MestFellows()
print(fellow5.get_count())
# print(MestFellows.count)