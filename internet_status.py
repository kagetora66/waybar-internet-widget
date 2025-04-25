#!/usr/bin/env python3
import json
import subprocess
import re
import sys
import time

def get_latency():
    try:
        result = subprocess.run(
            ['ping', '-c1', '-W1', '8.8.8.8'],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        if result.returncode == 0:
            match = re.search(r'time=(\d+\.?\d*)', result.stdout)
            return float(match.group(1)) if match else None
        return None
    except Exception:
        return None

while True:
    latency = get_latency()
    
    status = {
        "color":"#FF0000",
	"tooltip":"Pinging 8.8.8.8",
	"separator": False
    }
    
    if latency is not None:
        status["text"] = f"🌐 {int(latency)}ms" if latency <= 130 else f"⚠️  {int(latency)}ms" 
        status["color"] = "#00FF00" if latency <= 130 else "#FFFF00"
    else:       
        status["text"] = "no connection"
        status["color"] = "#FF0000"	
    
    sys.stdout.write(f'{json.dumps(status)}\n')
    sys.stdout.flush()
    
    time.sleep(5)
