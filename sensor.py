import requests
from bs4 import BeautifulSoup
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_SCAN_INTERVAL, CONF_URL
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA

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
        """Definiuje jednostkę miary."""
        return "PLN"

    @property
    def device_class(self):
        """Ustawia klasę urządzenia dla encji."""
        return "monetary"

    @property
    def state_class(self):
        """Definiuje typ danych encji (pomiar)."""
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
            print(f"Data retriving error: {e}")
