import json
import pandas as pd
from datetime import datetime

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Remover a chave 'timestamp' se existir
    if 'timestamp' in data:
        del data['timestamp']
    
    # Converter dados JSON em uma lista de dicionários
    records = []
    for timestamp, match_info in data.items():
        match_record = match_info.copy()
        match_record['Timestamp'] = datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')
        
        # Achatar o dicionário 'Stats Match'
        stats_match = match_record.pop('Stats Match', {})
        for stat_key, stat_value in stats_match.items():
            match_record[stat_key] = stat_value
        
        records.append(match_record)
    
    # Criar DataFrame a partir dos registros
    df = pd.DataFrame(records)
    
    # Ordenar DataFrame por Timestamp
    df.sort_values('Timestamp', inplace=True)
    
    # Resetar o índice do DataFrame
    df.reset_index(drop=True, inplace=True)
    
    return df

def save_data(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
