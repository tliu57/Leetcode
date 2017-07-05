def pour_water(terrains, location, water):
    waters = [0] * len(terrains)
    while water > 0:
        left = location - 1
        while left >= 0:
            if terrains[left] + waters[left] > terrains[left + 1] + waters[left + 1]:
                break
            left -= 1

        if terrains[left + 1] + waters[left + 1] < terrains[location] + waters[location]:
            location_to_pour = left + 1
        else:
            right = location + 1
            while right < len(terrains):
                if terrains[right] + waters[right] > terrains[right - 1] + waters[right - 1]:
                    break
                right += 1

            if terrains[right - 1] + waters[right - 1] < terrains[location] + waters[right - 1]:
                location_to_pour = right - 1
            else:
                location_to_pour = location

        waters[location_to_pour] += 1

        print "location_to_pour:", location_to_pour
        water -= 1 

    return waters


terrains = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]
water = 8
location = 0
pour_water(terrains, location, water)
