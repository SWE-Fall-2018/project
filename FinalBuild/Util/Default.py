from pyo import *
from Waves.Wave import Wave
from Filters.Filter import Filter
from Util.EnumerateData import UserInput

class Default:

    def __init__(self, _pitch, _amp, _userWaves):
        self.__pitch = _pitch
        self.__amp = _amp
        self.__userWaves = _userWaves
        self.__waves = [UserInput.NONE.value] * UserInput.THREE.value
        self.__filters1 = [UserInput.NONE.value] * UserInput.FIVE.value
        self.__filters2 = [UserInput.NONE.value] * UserInput.FIVE.value
        self.__filters3 = [UserInput.NONE.value] * UserInput.FIVE.value
        self.__filters = [self.__filters1, self.__filters2, self.__filters3]

        #sets self.__waves indices to Active Wave objects.
        for i in range(self.__userWaves.getLength()):
            newWave = Wave(self.__pitch, self.__amp)
            self.__waves[i] = newWave
            #Sets self.__filters indices to Active Filter objects.
            for j in range(self.__userWaves.getFilters(i).getLength()):
                newFilter = Filter()
                self.__filters[i][j] = newFilter
        #Sets the first voice to a default sine wave with no filters.
        self.__waves[UserInput.ZERO.value].setDefault()
        #Sets all voices and corresponding mutable filter slots to active Wave and Filter Object
        for i in range(self.__userWaves.getLength()):
            self.__userWaves.setWave(i, self.__waves[i])
            for j in range(self.__userWaves.getFilters(i).getLength()):
                self.__userWaves.setFilter(i, j, self.__filters[i][j])

    def getUserWaves(self):
        return self.__userWaves

    def getWaves(self):
        return self.__waves

    def getFilters(self):
        return self.__filters
