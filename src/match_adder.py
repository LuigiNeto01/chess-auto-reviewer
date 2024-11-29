import streamlit as st
import json
from datetime import datetime
from src.data_loader import save_data

def adicionar_partida(url):
# Codigo teorico com uma base para judar e tbm com algumas tratativas de exemplo
    nova_partida = extrair_dados_partida(url)
    
    if nova_partida:
        # Carregar o arquivo JSON existente
        with open('data/matchs.json', 'r') as f:
            data = json.load(f)
        
        # Adicionar a nova partida
        timestamp = nova_partida['Timestamp']
        data[timestamp] = nova_partida
        
        # Salvar o arquivo JSON atualizado
        save_data(data, 'data/matchs.json')
        
        st.success('Partida adicionada com sucesso!')
    else:
        st.error('Não foi possível adicionar a partida. Verifique a URL e tente novamente.')

def extrair_dados_partida(url):
# Codigo teorico mas ja com o json no formato que ele vai retornar!
    try:
        # Supondo que extraímos os seguintes dados
        partida = {
            'Timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'Type Match': 'Blitz',
            'Victory': 1,
            'User Rating': 1500,
            'Precision': 85.0,
            'Opening': 'Defesa Siciliana',
            'Stats Match': {
                'Brilliant': 0,
                'Excellent': 5,
                'Better': 3,
                'Great': 2,
                'Good': 4,
                'Book': 1,
                'Inaccuracy': 1,
                'Error': 0,
                'Missed Chance': 0,
                'Capybara': 0
            }
        }
        return partida
    except Exception as e:
        return None
