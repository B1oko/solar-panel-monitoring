from prometheus_client import start_http_server, Gauge
import requests
import xml.etree.ElementTree as ET
import time

# Configuration
ENDPOINT = "http://192.168.1.128/measurements.xml"
SCRAPE_INTERVAL = 30

# Create Prometheus Metrics
AC_VOLTAGE = Gauge('ac_voltage', 'AC Voltage')
AC_CURRENT = Gauge('ac_current', 'AC Current')
AC_POWER = Gauge('ac_power', 'AC Power')
AC_POWER_FAST = Gauge('ac_power_fast', 'AC Power Fast')
AC_FRECUENCY = Gauge('ac_frecuency', 'AC Frecuency')
DC_VOLTAGE = Gauge('dc_voltage', 'DC Voltage')
DC_CURRENT = Gauge('dc_current', 'DC Current')
LINK_VOLTAGE = Gauge('LINK_Voltage', 'LINK Voltage')
GRID_POWER = Gauge('grid_power', 'Grid Power')
GRID_CONSUMED_POWER = Gauge('grid_consumed_power', 'Grid Consumed Power')
GRID_INJECTED_POWER = Gauge('grid_injected_power', 'Grid Injected Power')
OWN_CONSUMED_PROJECT = Gauge('own_consumed_power', 'Own Consumed Power')
DERATING = Gauge('derating', 'Derating')

# Función para recolectar datos del endpoint y actualizar métricas
def fetch_and_update_metrics():
    response = requests.get(ENDPOINT)
    root = ET.fromstring(response.content)

    measurements = root.find('.//Measurements')

    for measurement in measurements:
        type_ = measurement.attrib['Type']
        value = float(measurement.attrib.get('Value', 0.0))

        if type_ == 'AC_Voltage':
            AC_VOLTAGE.set(value)
        elif type_ == 'AC_Current':
            AC_CURRENT.set(value)
        elif type_ == 'AC_Power':
            AC_POWER.set(value)
        elif type_ == 'AC_Power_fast':
            AC_POWER_FAST.set(value)
        elif type_ == 'AC_Frequency':
            AC_FRECUENCY.set(value)
        elif type_ == 'DC_Voltage':
            DC_VOLTAGE.set(value)
        elif type_ == 'DC_Current':
            DC_CURRENT.set(value)
        elif type_ == 'LINK_Voltage':
            LINK_VOLTAGE.set(value)
        elif type_ == 'GridPower':
            GRID_POWER.set(value)
        elif type_ == 'GridConsumedPower':
            GRID_CONSUMED_POWER.set(value)
        elif type_ == 'GridInjectedPower':
            GRID_INJECTED_POWER.set(value)
        elif type_ == 'OwnConsumedPower':
            OWN_CONSUMED_PROJECT.set(value)
        elif type_ == 'Derating':
            DERATING.set(value)

if __name__ == '__main__':
    start_http_server(8000)  # Exponer métricas en http://localhost:8000
    while True:
        fetch_and_update_metrics()
        time.sleep(SCRAPE_INTERVAL)
