import homeassistant.helpers.config_validation as cv
import requests
import voluptuous as vol
from bs4 import BeautifulSoup
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.components.sensor import SensorEntity

MIN_15 = 60 * 15
URL = "https://www.investing.com/currencies/usd-pln-converter"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional("scan_interval", default=MIN_15): cv.time_period,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    scan_interval = config.get("scan_interval")
    add_entities([UsdPlnSensor(URL, scan_interval)])


class UsdPlnSensor(SensorEntity):
    def __init__(self, url, scan_interval):
        self._state = None
        self._name = "USD to PLN"
        self._url = url
        self._scan_interval = scan_interval
        self._attr_should_poll = True

    @property
    def name(self):
        return self._name

    @property
    def unit_of_measurement(self):
        return "PLN"

    @property
    def device_class(self):
        return "monetary"

    @property
    def state_class(self):
        return "measurement"

    @property
    def state(self):
        return self._state

    def update(self):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(self._url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            rate_element = soup.find("span", {"id": "last_last"}).text
            self._state = round(float(rate_element), 4)
        except Exception as e:
            self._state = None
            print(f"Data downloading error: {e}")
