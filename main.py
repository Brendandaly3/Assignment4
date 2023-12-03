import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer =  "{:02d}:{:02d}".format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time completed!')

# Check if stdin is available before prompting for input
try:
    t = input('Enter the time in seconds: ')
except EOFError:
    t = 0

# If user provided input, proceed with the countdown
if t:
    try:
        countdown(int(t))
    except KeyboardInterrupt:
        print("\nCountdown interrupted. Exiting...")
else:
    print("No input provided. Exiting...")