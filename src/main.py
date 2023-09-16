import time
import pygame
import os


def main():

# Initialize pygame
  pygame.init()

# Create a sound object
pygame.mixer.init()
sound = pygame.mixer.Sound("bell.wav")  # Replace "bell.wav" with your sound file

# Pomodoro session duration (seconds)
pomodoro_duration = 25 * 60  # 25 minutes

# Break session duration (seconds)
break_duration = 5 * 60  # 5 minutes

# Pomodoro and break session counters
pomodoro_count = 0

while True:
    # Pomodoro session
    print(f'Pomodoro {pomodoro_count + 1}')
    for remaining in range(pomodoro_duration, 0, -1):
        mins, secs = divmod(remaining, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timeformat}', end='', flush=True)
        time.sleep(1)
    
    # Break session
    print("\nBreak Time")
    sound.play()  # Play the sound (bell.wav)
    for remaining in range(break_duration, 0, -1):
        mins, secs = divmod(remaining, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timeformat}', end='', flush=True)
        time.sleep(1)
    
    pomodoro_count += 1

    # Insert a long break every 4 Pomodoro sessions
    if pomodoro_count % 4 == 0:
        long_break_duration = 15 * 60  # 15 minutes
        print("\nLong Break Time")
        sound.play()  # Play the sound (bell.wav) for long break
        for remaining in range(long_break_duration, 0, -1):
            mins, secs = divmod(remaining, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(f'\r{timeformat}', end='', flush=True)
            time.sleep(1)
    
    print("\n\n")


if __name__ == "__main__":
  pass
