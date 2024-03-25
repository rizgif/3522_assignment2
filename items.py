# items.py

class Toy:
    def __init__(self, product_id, name, description, battery_operated, min_age):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.battery_operated = battery_operated
        self.min_age = min_age

class StuffedAnimal:
    def __init__(self, product_id, name, description, stuffing, size, fabric):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric

class Candy:
    def __init__(self, product_id, name, description, has_nuts, lactose_free):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.has_nuts = has_nuts
        self.lactose_free = lactose_free

# Specific Toys
class SantasWorkshopToy(Toy):
    def __init__(self, product_id, name, description, dimensions, num_rooms, **kwargs):
        super().__init__(product_id, name, description, False, **kwargs)
        self.dimensions = dimensions
        self.num_rooms = num_rooms

class RCSpiderToy(Toy):
    def __init__(self, product_id, name, description, speed, jump_height, glows_in_dark, type_spider, **kwargs):
        super().__init__(product_id, name, description, True, **kwargs)
        self.speed = speed
        self.jump_height = jump_height
        self.glows_in_dark = glows_in_dark
        self.type_spider = type_spider

class RobotBunnyToy(Toy):
    def __init__(self, product_id, name, description, num_sound_effects, color, **kwargs):
        super().__init__(product_id, name, description, True, **kwargs)
        self.num_sound_effects = num_sound_effects
        self.color = color

# Specific Stuffed Animals
class DancingSkeletonStuffedAnimal(StuffedAnimal):
    def __init__(self, product_id, name, description, **kwargs):
        super().__init__(product_id, name, description, "Polyester Fibrefill", "M", "Acrylic", **kwargs)
        self.glows_in_dark = True

class ReindeerStuffedAnimal(StuffedAnimal):
    def __init__(self, product_id, name, description, **kwargs):
        super().__init__(product_id, name, description, "Wool", "M", "Cotton", **kwargs)
        self.has_sleigh = True  # Example property, assumes all reindeers come with a mini sleigh

class EasterBunnyStuffedAnimal(StuffedAnimal):
    def __init__(self, product_id, name, description, color, **kwargs):
        super().__init__(product_id, name, description, "Polyester Fibrefill", "M", "Linen", **kwargs)
        self.color = color

# Specific Candies
class PumpkinCaramelToffeeCandy(Candy):
    def __init__(self, product_id, name, description, variety, **kwargs):
        super().__init__(product_id, name, description, True, False, **kwargs)
        self.variety = variety  # e.g., "Sea Salt" or "Regular"

class CandyCaneCandy(Candy):
    def __init__(self, product_id, name, description, color, **kwargs):
        super().__init__(product_id, name, description, False, True, **kwargs)
        self.color = color  # "Red" or "Green"

class CremeEggCandy(Candy):
    def __init__(self, product_id, name, description, pack_size, **kwargs):
        super().__init__(product_id, name, description, True, False, **kwargs)
        self.pack_size = pack_size  # e.g., number of eggs in a pack

# ... Add any additional item-specific classes as required for your assignment.
