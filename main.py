from src.cleaner import load_raw_data, extract_results

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
all_records = []

for year in years:
    data = load_raw_data(year)
    records = extract_results(data, year)
    all_records.extend(records)
    print(f"{year}: {len(records)} registros")

print(f"\nTotal general: {len(all_records)} registros")