import os
import csv
import random
from django.conf import settings
from django.shortcuts import render
def analiyze_data(e, a, w, max_energy=10.42, max_air=0.139, max_water=3.47):
    status_energy = "Normal"
    status_air = "Normal"
    status_water = "Normal"
    if e > max_energy * 1.5:
        status_energy = "Severe"
    elif e > max_energy:
        status_energy = "High"
    if a > max_air * 1.5:
        status_air = "Severe"
    elif a > max_air:
        status_air = "High"
    if w > max_water * 1.5:
        status_water = "Severe"
    elif w > max_water:
        status_water = "High"
    return status_energy, status_air, status_water
def get_random_data_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = list(csv.DictReader(file))
        random_row = random.choice(reader)
        energy = float(random_row['Energy_Consumption_kWh_per_min'])
        air = float(random_row['Air_Pollution_CO2_kg_per_min'])
        water = float(random_row['Water_Usage_liters_per_min'])
        return energy, air, water
def dashboard(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'data.csv')
    energy, air, water = get_random_data_from_csv(csv_file_path)
    status_energy, status_air, status_water = analiyze_data(energy, air, water)
    context = {
        'status_energy_text': f"Energy is {status_energy}",
        'energy_value': energy,
        'status_air_text': f"Air pollution is {status_air}",
        'air_value': air,
        'status_water_text': f"Water usage is {status_water}",
        'water_value': water,
    }
    return render(request, 'core/dashboard.html', context)