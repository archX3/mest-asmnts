from itertools import count

class Mest:
    fellows_added = 0

    def __init__(self) :
        Mest.fellows_added += 1


    def hire(self, name, nationality):
        print(Mest.fellows_added)
        if(Mest.fellows_added < 4):
            print("{} has been employed from {}".format(name, nationality))
        else:
            Exception("Can't accept any more employees atm")



# class Fellow:
    # _ids = count(1)

    # def __init__(self) :
    #     self.id = next(self._ids)
        # if (self.id > 3) :
        #     return

    # def get_count(self) :
    #     return self.id

mest = Mest()
# print(fellow1.get_count())
mest.hire("ama", "GH")
mest.hire("andrew", "USA")
mest.hire("zee", "ab's")
mest.hire("0-9", "nums")
mest.hire("eeiiii", "jnsldks")
# Fellow()
# Fellow()
# Fellow()
# Fellow()
# Fellow()
# Fellow()
# Fellow()
# mest.hire(Fellow())
#
# print(fellow2.get_count())
# fellow3 = Mest()
#
# fellow4 = Mest()
# fellow5 = Mest()
# print(fellow5.get_count())
# print(MestFellows.count)
# class MestFellow:
#     __count = 0
#
#     def __init__(self) :
#         if (self.__count >= 4) :
#             return
#         self.__count += 1
#
#     def get_count(self) :
#         return self.__count