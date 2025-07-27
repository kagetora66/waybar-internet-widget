# Waybar Internet Status Widget

Real-time internet connection monitoring for Waybar
![Internet Status Widget Preview](./docs/swappy-20250425_124359.png "Widget display")
![Internet Status Widget Preview](./docs/swappy-20250426_082808.png "Widget display")
![Internet Status Widget Preview](./docs/swappy-20250426_133241.png "Widget display")
![Internet Status Widget Preview](./docs/swappy-20250503_082207.png "Widget display")
## Features
- Ping latency display (8.8.8.8)
- Color-coded status
- Hover tooltip information

## Installation
```bash
git clone https://github.com/kagetora66/waybar-internet-widget.git
sudo chmod +x waybar-internet-widget/internet_status.py
cp waybar-internet-widget/internet_status.py ~/.config/waybar/scripts/ (create scripts folder if doesnt exist)
```
## Configuration
```bash
#add the follwing to your Waybar config.jsonc
"modules-right": ["custom/internet", "clock", etc],  // Add to existing modules
"custom/internet": {
    "exec": "~/.config/waybar/scripts/internet_status.py",
    "return-type": "json"
} #Make sure of validity of the json file!!!
