# Home Assistant Custom Sensor: USD/PLN

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Custom%20Component-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

## Description

This custom Home Assistant integration adds a sensor that fetches the **current USD/PLN exchange rate** from [Investing.com](https://www.investing.com/currencies/usd-pln-converter) by parsing the HTML page. The sensor updates its value at a configurable interval.
> [!IMPORTANT]
> Please be polite to investing.com and don't run this custom component with scan_interval less than 15min.


## Features

- Automatically fetches the USD/PLN rate at a set interval (`scan_interval`)
- Displays the exchange rate as a Home Assistant sensor
- Allows configuration of update interval

## Requirements

- Home Assistant 2022.0 or newer
- Python 3.10+
- Installed libraries: `requests`, `beautifulsoup4`

## Installation

1. Clone this repository or copy the `usd_pln` folder into your Home Assistant `custom_components` directory:

    ```
    custom_components/usd_pln/
        ├── __init__.py
        ├── manifest.json
        ├── sensor.py
    ```

2. Install the required libraries (if not already present, because HA probably is shipped with it):

    ```
    pip install requests beautifulsoup4
    ```

3. Add the following configuration to your `configuration.yaml`:

    ```
    sensor:
      - platform: usd_pln
        scan_interval: 900   # (optional, default is 15 minutes)
    ```

4. Restart Home Assistant.

5. The sensor will appear as `sensor.usd_to_pln`.

## Configuration Parameters

| Name            | Type | Default | Description                          |
|-----------------|------|---------|--------------------------------------|
| `scan_interval` | int  | `900`   | Sensor update interval               |
