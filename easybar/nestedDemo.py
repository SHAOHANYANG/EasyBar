

from api import NestedBar
import time as _time
# nestedDemo
if __name__ == "__main__":
     nb = NestedBar(100, 3, colour='blue')
     for i in range(101):
         nb.update(0, i)  # Update progress for first bar
         nb.update(1, i*2)  # Update progress for second bar at twice the speed
         nb.update(2, i*3)  # Update progress for third bar at half the speed
         nb.print_bars()  # Print all bars
         _time.sleep(0.1)



