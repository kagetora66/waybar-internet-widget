# Waybar Internet Status Widget

Real-time internet connection monitoring for Waybar

## Features
- Ping latency display (8.8.8.8)
- Color-coded status
- Hover tooltip information

## Installation
```bash
git clone https://github.com/yourusername/waybar-internet-widget.git
cp src/internet_status.py ~/.config/waybar/scripts/

## Config
add the follwing to your Waybar's config.jsonc
```bash
"custom/internet": {
    "exec": "~/.config/waybar/scripts/internet_status.py",
    "return-type": "json"
}
