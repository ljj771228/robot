import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from service.rgb import RGBService
from service.base import Priority

def test_rgb_service():
    print("Testing RGB Service...")
    
    rgb_service = RGBService()
    rgb_service.start()
    
    try:
        print("Testing solid red...")
        rgb_service.dispatch("solid", (255, 0, 0))
        time.sleep(2)
        
        print("Testing solid green...")
        rgb_service.dispatch("solid", (0, 255, 0))
        time.sleep(2)
        
        print("Testing solid blue...")
        rgb_service.dispatch("solid", (0, 0, 255))
        time.sleep(2)
        
        print("Testing paint pattern...")
        colors = [
            (255, 0, 0),    # Red
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (255, 255, 0),  # Yellow
            (255, 0, 255),  # Magenta
        ] * 8  # Repeat pattern
        
        rgb_service.dispatch("paint", colors)
        time.sleep(3)
        
        print("Testing priority - high priority solid should override paint...")
        rgb_service.dispatch("paint", [(255, 255, 255)] * 40)  # White
        rgb_service.dispatch("solid", (255, 0, 0), Priority.HIGH)  # High priority red
        time.sleep(2)
        
        print("Clearing...")
        rgb_service.clear()
        time.sleep(1)
        
    finally:
        rgb_service.stop()
        print("RGB Service test completed!")

if __name__ == "__main__":
    test_rgb_service()