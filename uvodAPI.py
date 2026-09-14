slovar = {"ključ":"vrednost"}

print(slovar)
print(slovar["ključ"])

razno = {"število": 6,
        "ime": "Jon",
        "seznam": [1,2,3,4],
        "slovar": {"firma": "Dacia", "moč": "120kw"}}

print(razno["število"] + 10)

print(max(razno["seznam"]))

print(razno["slovar"])
print(razno["slovar"]["firma"])


# API: Open-Meteo (https://open-meteo.com/en/docs)
# Odgovor API-ja je JSON, ki ga Python prebere kot slovar.

import requests

NASLOV = "https://api.open-meteo.com/v1/forecast"

parametri = {
    "latitude": 46.0569,            # Ljubljana
    "longitude": 14.5058,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Ljubljana",
    "forecast_days": 3,
}

odgovor = requests.get(NASLOV, params=parametri, timeout=10)
odgovor.raise_for_status()      # javi napako, ce strezniku kaj ne uspe

vreme = odgovor.json()          # <- to je navaden slovar

print()
print("Kraj:", vreme["latitude"], vreme["longitude"], "|", vreme["timezone"])

# Trenutno vreme -> gnezden slovar, enako kot razno["slovar"]["firma"]
trenutno = vreme["current"]
enote = vreme["current_units"]

print("Cas meritve:", trenutno["time"])
print("Temperatura:", trenutno["temperature_2m"], enote["temperature_2m"])
print("Vlaga:", trenutno["relative_humidity_2m"], enote["relative_humidity_2m"])
print("Veter:", trenutno["wind_speed_10m"], enote["wind_speed_10m"])

# Napoved -> slovar seznamov, zato jih zdruzimo z zip()
dnevi = vreme["daily"]

print()
print("Napoved po dnevih:")
for datum, najvec, najmanj in zip(dnevi["time"],
                                  dnevi["temperature_2m_max"],
                                  dnevi["temperature_2m_min"]):
    print(f"  {datum}: od {najmanj} do {najvec} {enote['temperature_2m']}")

print()
print("Najvisja temperatura v napovedi:", max(dnevi["temperature_2m_max"]))
