# factories.py
from items import (SantasWorkshopToy, RCSpiderToy, RobotBunnyToy, 
                   DancingSkeletonStuffedAnimal, ReindeerStuffedAnimal, 
                   EasterBunnyStuffedAnimal, PumpkinCaramelToffeeCandy, 
                   CandyCaneCandy, CremeEggCandy)

class AbstractFactory:
    def create_toy(self, details):
        pass

    def create_stuffed_animal(self, details):
        pass

    def create_candy(self, details):
        pass

class EasterFactory(AbstractFactory):
    def create_toy(self, details):
        return RobotBunnyToy(**details)

    def create_stuffed_animal(self, details):
        return EasterBunnyStuffedAnimal(**details)

    def create_candy(self, details):
        return CremeEggCandy(**details)

class ChristmasFactory(AbstractFactory):
    def create_toy(self, details):
        return SantasWorkshopToy(**details)

    def create_stuffed_animal(self, details):
        return ReindeerStuffedAnimal(**details)

    def create_candy(self, details):
        return CandyCaneCandy(**details)

class HalloweenFactory(AbstractFactory):
    def create_toy(self, details):
        return RCSpiderToy(**details)

    def create_stuffed_animal(self, details):
        return DancingSkeletonStuffedAnimal(**details)

    def create_candy(self, details):
        return PumpkinCaramelToffeeCandy(**details)
