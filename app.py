import psutil
import platform
import time
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_detailed_stats():
    try:
        boot_time_timestamp = psutil.boot_time()
        uptime = str(datetime.now() - datetime.fromtimestamp(boot_time_timestamp)).split('.')[0]
    except Exception:
        uptime = "N/A"
    
    try:
        net_io = psutil.net_io_counters()
        net_sent = f"{net_io.bytes_sent / (1024**2):.2f} MB"
        net_recv = f"{net_io.bytes_recv / (1024**2):.2f} MB"
    except Exception:
        net_sent, net_recv = "0 MB", "0 MB"

    sensors = {"temperatures": [], "fans": [], "battery": "N/A"}
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                for entry in entries:
                    sensors["temperatures"].append({
                        "label": entry.label or name,
                        "current": f"{entry.current}°C"
                    })
        
        fans = psutil.sensors_fans()
        if fans:
            for name, entries in fans.items():
                for entry in entries:
                    sensors["fans"].append({
                        "label": entry.label or name,
                        "current": f"{entry.current} RPM"
                    })
        
        batt = psutil.sensors_battery()
        if batt:
            sensors["battery"] = f"%{batt.percent} ({'Takılı' if batt.power_plugged else 'Değil'})"
    except Exception:
        pass

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pinfo = proc.info
            pinfo['cpu_percent'] = pinfo['cpu_percent'] or 0
            pinfo['memory_percent'] = pinfo['memory_percent'] or 0
            processes.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:10]

    return {
        "uptime": uptime,
        "cpu_usage": psutil.cpu_percent(interval=None),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "net_sent": net_sent,
        "net_recv": net_recv,
        "tasks": processes,
        "sensors": sensors,
        "os_info": f"macOS {platform.mac_ver()[0]} ({platform.machine()})"
    }

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/stats")
async def stats():
    return get_detailed_stats()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")