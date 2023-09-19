masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for  masina in masini:
    if masina in ['Trabant','Lăstun']:
        continue
    print(f'S-ar putea sa va placa masina {masina}')
