import argparse
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from service.motors import MotorsService
from service.base import Priority

def test_motors_service():
    parser = argparse.ArgumentParser(description="Test Motors Service")
    parser.add_argument('--id', type=str, required=True, help='ID of the lamp')
    parser.add_argument('--port', type=str, required=True, help='Serial port for the lamp')
    args = parser.parse_args()
    
    print("Testing Motors Service...")
    
    motors_service = MotorsService(port=args.port, lamp_id=args.id)
    motors_service.start()
    
    try:
        print("Getting available recordings...")
        recordings = motors_service.get_available_recordings()
        print(f"Available recordings: {recordings}")
        
        if recordings:
            print(f"Playing first recording: {recordings[0]}")
            motors_service.dispatch("play", recordings[0])
            
            # Wait for playback to complete
            motors_service.wait_until_idle(timeout=30)
            print("Playback completed!")
        else:
            print("No recordings found. Create some recordings first.")
        
    finally:
        motors_service.stop()
        print("Motors Service test completed!")

if __name__ == "__main__":
    test_motors_service()