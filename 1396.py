class UndergroundSystem:

    def __init__(self):
        # {id: (stationName, time)}
        self.checkIns = {}
        # {route: (numTrips, totalTime)}
        self.checkOuts = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns.pop(id)
        route = (startStation, stationName)
        self.checkOuts[route][0] += 1
        self.checkOuts[route][1] += t - startTime

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        numTrips, totalTime = self.checkOuts[(startStation, endStation)]
        return totalTime / numTrips
        
## 1396. Design Underground System


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)