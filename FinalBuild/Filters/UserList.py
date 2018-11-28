from pyo import *
from Util.EnumerateData import UserInput

class UserList:

    def __init__(self):
        self.__userList = [UserInput.NONE.value] * UserInput.FIVE.value
        self.activeFilters = [UserInput.TBOOL.value] * UserInput.FIVE.value

    def __dir__(self):
        return ['userList']

    #Assigns selected filter type to selected filter associated with selected waveform.
    def setFilter(self, _input, _newFilter):
        self.__userList[_input] = _newFilter

    def getLength(self):
        return len(self.__userList)

    def readIndex(self, _input):
        return self.__userList[_input]

    #Returns the isActive state for a selected filter.
    def getIsActive(self, _input):
        return self.activeFilters[_input]

    #Toggles the isActive state for a selected filter.
    def setIsActive(self, _input):
        if (self.activeFilters[_input] == UserInput.TBOOL.value):
            self.activeFilters[_input] = UserInput.FBOOL.value
        else:
            self.activeFilters[_input] = UserInput.TBOOL.value
