# Waybar Internet Status Widget

Real-time internet connection monitoring for Waybar
![Internet Status Widget Preview](./docs/swappy-20250425_124359.png "Widget display")

## Features
- Ping latency display (8.8.8.8)
- Color-coded status
- Hover tooltip information

## Installation
```bash
git clone https://github.com/yourusername/waybar-internet-widget.git
cp ./internet_status.py ~/.config/waybar/scripts/
```
## Configuration
```bash
#add the follwing to your Waybar config.jsonc
"modules-right": ["custom/internet", "clock", etc],  // Add to existing modules
"custom/internet": {
    "exec": "~/.config/waybar/scripts/internet_status.py",
    "return-type": "json"
}
