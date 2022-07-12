# python3
import sys


def compute_min_refills(distance, tank, stops):
    tank_capacity = tank
    tank = tank
    stops_indeces_covered = -1
    refills = 0
    
    if distance <= tank: # where tank capacity is greater than distance
        return refills
    
    for idx, next_stop in enumerate(stops):
        if tank - next_stop < 0:
            return -1
        if stops_indeces_covered >= idx:
            continue            
        for future_stop_idx in range(idx+1, len(stops)):
            if tank - stops[future_stop_idx] < 0:
                refills +=1
                tank = tank_capacity + stops[future_stop_idx -1]
                stops_indeces_covered = future_stop_idx - 1
                break
            
            if future_stop_idx == len(stops)-1:
                if distance <= tank:
                    continue
                else:
                    refills +=1
                    tank = tank_capacity + stops[future_stop_idx]
                    if tank - distance > 0:
                        continue
                    else:
                        return -1
    if distance <= tank:
        pass
    else:
        refills +=1
        tank = tank_capacity + stops[-1]
        if distance <= tank:
            pass
        else:
            return -1
    return refills

            


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d = 500
    # m = 200
    # stops = [100, 300, 400]
    print(compute_min_refills(d, m, stops))
