from src.fetcher import get_race_results , save_raw_data

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

for year in years:
    print(f"Descargando {year}...")
    data = get_race_results(year)
    save_raw_data(data, year)
    print(f"{year} guardado.")

print("Todo listo!")