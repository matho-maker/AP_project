from acceleration import accel_x, accel_y
from numpy import sqrt

# A more elaborated try, this time assuming that the skiers always look downwards once they passed a square(in that case the above new_coord function doesn't need to be defined)
position = (0, 0)
# initial position, just a placeholder
speed = 0


# initial speed placeholder

def get_position():
    get
    coord(x), get
    coord(y)


distance = 1
# it can be whatever we choose for the distance of the grid, but it has to be in meters.

terrain_type = ['snow', 'wet snow', 'grass', 'ice', 'packed snow', 'tree']
terrain_type_penalty = [1, 1.2, 1.5, 2, 0.7, 99999]
terrain_type_mu = [0.1, 0.14, 0.2, 0.03, 0.1, 0]
# I don't remember the values for this and I also do not have all of the friction coefficients (mu) between the terrain and skis(waxed wood)

# as a ditionnary:
tt_penalty = {'snow': 1, 'wet snow': 1.1, 'grass': 1.5, 'ice': 2, 'packed snow': 0.7, 'tree': 99999}
tt_mu = {'snow': 0.1, 'wet snow': 0.14, 'grass': 0.2, 'ice': 0.03, 'packed snow': 0.1, 'tree': 0}


# also needs something for the target terrain type

##This uses the array index
def get_terrain_type(position):
    get terrain(x, y)


def get_slope(position):
    get_slope()
    # This gets the rad argument for our acceleration function, os the angle has to be in radians


def get_mass(skier):
    get_mass()


def get_speed(position):
    get speed(y)


# not sure if the positional argument is required here

#accel_y(m, rad, 9.81, mu, 0.92, 0.916, 0.61, v)
#accel_x(m, 9.81, mu, 0.92, 0.916, 0.61, v)
# area replaced by 0.61, C replaced by 0.92, g replaced by 9.81, rho replaced by 0.916, these are the equations to get acceleration

# The acceleration functions to be used should look like this:

##Needs a reference to skier
accel_y(get_mass(skier), get_slope(position), 9.81, tt_mu.get(get_terrain_type(position)), 0.92, 0.916, 0.61, get_speed(position))
accel_x(get_mass(skier), get_slope(position), 9.81, tt_mu.get(get_terrain_type(position)), 0.92, 0.916, 0.61, get_speed(position))
# I only implemented the y acceleration for now


# we are only interested in the speed on the y axis (going down), the speed depends on the position (x,y)

time = 0
# This is the initial time, before the optimisation has begun
path = []


# This will keep track of the coordinates

# The following function compares the strategies of going right, left or down depending on whether the skier can go diagonally or not.
# It solves the constraint of the skier only seeing one row in front(limiting them even more, as they only have 3 choices of where they can go, os idk if it's good enough)
# Maybe it would be best to have an optimization program for time that does it while seeing the whole row in front (thus we'd need more points of comparison when it comes to time)
# Or maybe we should do it assuming that the map is known instead (I'm against that idea)
# The arguments that go in the function might also have to be changed (f.e. to (x,y, speed))
def optimisation(position, speed):
    if diagonal_movement = 1:
        # diagonal_movement is the characteristic that allows the skier to go diagonally, either 1 or 0, they are to be encoded depending on probability, or we can change the conditons.
        time_dl = (np.sqrt(2) * distance / speed(y)) * tt_penalty.get(get_terrain_type(x - 1, y - 1))
        ##should there be a speed(y)/sqrt(2) instead of just speed(y) in order to take the proper acceleration decomposition into account? and only to look at y acceleration?
        time_dr = (np.sqrt(2) * distance / speed(y)) * tt_penalty.get(get_terrain_type(x + 1, y - 1))
        ##same question as above
        time_d = (distance / speed(y)) * tt_penalty.get(get_terrain_type(x, y - 1))
        lowest_time = min(time_dl, time_dr, time_d)
        if lowest_time = time_dl:
            target_coord = ((x - 1), (y - 1))
        elif lowest_time = time_dr:
            target_coord = ((x + 1), (y - 1))
        else:
            target_coord = ((x), (y - 1))
    elif diagonal_movement = 0:
        time_ld = (distance / speed(y)) * tt_penalty.get(get_terrain_type(x - 1, y)) + (distance / speed(y)) * tt_penalty.get(get_terrain_type(x - 1, y - 1))
        ##sideways there is no acceleration or deceleration for now
        time_lr = (distance / speed(y)) * tt_penalty.get(get_terrain_type(x + 1, y)) + (distance / speed(y)) * tt_penalty.get(get_terrain_type(x + 1, y - 1))
        ##same as above
        time_d = (distance / speed(y)) * tt_penalty.get(get_terrain_type(x, y - 1))
        lowest_time = min(time_ld, time_rd, time_d)
        if lowest_time = time_ld:
            target_coord = ((x - 1), (y - 1))
        elif lowest_time = time_rd:
            target_coord = ((x + 1), (y - 1))
        else:
            target_coord = ((x), (y - 1))
    return lowest_time
    # we return the lowest time and then we switch the position to the new coordinate dictated by that lowest time
    path.append(target_coord)
    position = target_coord
    time += lowest_time


position = (np.random(0, l), h)
# for a randomly generated position

# The loop that applies the optimisation function to the whole map, going from the starting position (ikd if that's defined at random or not)
# The dimensions of the map should be defined elsewhere, I'm taking h(height - y axis) and w(width - x axis) as ranges for now. Mabye we'll involve x and y instead.
for i in range(0, h):
    position = get_position()

    if speed <= 0:
        speed = 2
        time += 1
        # This takes into account the possibility of starting at speed 0 or of pushing oneself after a fall to get speed (I put 2m/s arbitrarily for now, not sure what's best, and a time penalty of 1s)
        # I also put the less than sign to make sure our speed is never negative
    if speed > 0:
        speed = speed  # I wanted to put something else here, but I will actually account for increments at the end, because I require the time for each passage ot get new speeds form acceleration.

    if i == h:
        break
        # not sure about the syntax here, but it's just to have the skier stop as he reaches the lsat part, maybe the best would be to just run in a range (0, h-1)?
    else:
        optimisation(position, speed)
        speed = speed + accel_y(get_mass(skier), get_slope(position), 9.81, tt_mu.get(get_terrain_type(position)), 0.92, 0.916, 0.61, speed) * lowest_time
        # this last line replaces the speed for our square by a new speed based on the acceleration variables and the time.

        # FOR NOW THERE IS A PROBLEM HERE, BECAUSE THE SKIER DOES NOT CHANGE HIS SPEED IF HE GOES SIDEWAYS AND GOING DIAGONALLY, HE DOESN'T PROPERLY DECOMPOSE HIS ACCELERATION EITHER.
        # Actually, I think that it's ok that the skier doesn't gain speed when going sideways, as there is no (y) acceleration there, there could only be deceleration (not implemented)

print("The total time was: ", time)
print("The path chosen was: ", path)

# I think the next step is to calculate a max speed for the given characteristics, or just take them from the .csv I made previously, but maybe it doens't matter in the end.



