# from enum import Enum
# class User(Enum):
#     Twowater = 98
#     Hang = 30
#     Tom = 12
# Twowater = User.Twowater
# Hang = User.Hang
# print(Twowater == Hang, Twowater == User.Twowater)
# print(Twowater is Hang, Twowater is User.Twowater)
# try:
#     print('\n'.join('  ' + s.name for s in sorted(User)))
# except TypeError as err:
#     print(' Error : {}'.format(err))

import enum
class User(enum.IntEnum):
    Twowater = 98
    Hang = 30
    Tom = 12


try:
    print('\n'.join(s.name for s in sorted(User)))
except TypeError as err:
    print(' Error : {}'.format(err))