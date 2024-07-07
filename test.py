from flask import Flask, send_file, request, jsonify
import os
variables = {}
app = Flask(__name__)

@app.route('/')
def app_route():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html')), 200

import time
# Define a dictionary to store dynamic variables
variables = {}

import os
# Function to handle application termination
def ExitApp():
    os._exit(1)

import time
import threading
# Dictionary to store active timers
active_timers = {}
# Function to start, stop, or adjust a timer
def SetTimer(func, timeOrOnOff):
    def timer_wrapper(name, interval_ms):
        def run_timer():
            func()
            if active_timers[name]['running']:
                active_timers[name]['timer'] = threading.Timer(interval_ms / 1000.0, run_timer)
                active_timers[name]['timer'].start()
                
        if timeOrOnOff == "On" and not active_timers[name]['running']:
            active_timers[name]['timer'] = threading.Timer(active_timers[name]['interval_ms'] / 1000.0, run_timer)
            active_timers[name]['timer'].start()
            active_timers[name]['running'] = True
            #print(f"Timer '{name}' started with interval {active_timers[name]['interval_ms']} ms.")
        elif timeOrOnOff == "Off" and active_timers[name]['running']:
            active_timers[name]['timer'].cancel()
            active_timers[name]['running'] = False
            #print(f"Timer '{name}' stopped.")
        elif isinstance(timeOrOnOff, int):
            active_timers[name]['interval_ms'] = timeOrOnOff  # Update the stored interval
            if active_timers[name]['running']:
                active_timers[name]['timer'].cancel()
                active_timers[name]['timer'] = threading.Timer(timeOrOnOff / 1000.0, run_timer)
                active_timers[name]['timer'].start()
                #print(f"Timer '{name}' adjusted to interval {timeOrOnOff} ms.")
            else:
                active_timers[name]['timer'] = threading.Timer(timeOrOnOff / 1000.0, run_timer)
                active_timers[name]['timer'].start()
                active_timers[name]['running'] = True
                #print(f"Timer '{name}' started with adjusted interval {timeOrOnOff} ms.")
        else:
            print("Invalid arguments. Please provide a valid function and time/On/Off state.")
    # Ensure func is callable
    if not callable(func):
        print("Invalid function provided.")
        return
    name = func.__name__  # Use function name as timer identifier
    # Initialize timer if not already active
    if name not in active_timers:
        active_timers[name] = {
            'timer': None,
            'running': False,
            'interval_ms': 1000  # Default interval
        }
    # Determine the interval_ms value
    if isinstance(timeOrOnOff, int):
        interval_ms = timeOrOnOff
    else:
        interval_ms = active_timers[name]['interval_ms']  # Use stored interval
    # Call timer_wrapper to manage timer based on timeOrOnOff
    timer_wrapper(name, interval_ms)

def timer1():
    print("timer1 msg\n")
variables['wert'] = 5555
variables['port'] = variables['wert']
@app.route('/waesdrf', methods=['POST'])
def waesdrf():
    variables['as'] = request.get_json()
    print("j")
def timer2():
    print("timer2 msg\n")
SetTimer(timer1, 300)
SetTimer(timer2, 69)
for A_Index1 in range(1, 20 + 1):
    variables['A_Index1'] = A_Index1
    time.sleep(300 / 1000)
    print("this is Index "  +  str(variables['A_Index1']) +  "\n")
    if (variables['A_Index1'] == 4):
        print("STOP the timer2\n")
        SetTimer(timer2, "Off")
    if (variables['A_Index1'] == 17):
        print("bye bye\n")
        ExitApp()
    if (variables['A_Index1'] == 10):
        print("Start back the timer2\n")
        SetTimer(timer2, "On")


@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=variables['port'], debug=True)
