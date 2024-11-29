import streamlit as st

def filter_data(df, date_range, selected_type_matches, selected_victory_values, selected_openings):
    # Verificar se duas datas foram selecionadas
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date, end_date = date_range
        if start_date > end_date:
            st.sidebar.warning('A data de início não pode ser posterior à data de fim.')
            st.stop()
    else:
        st.sidebar.warning('Por favor, selecione um intervalo de duas datas (início e fim).')
        st.stop()
    
    # Aplicar filtros ao DataFrame
    df_filtered = df[
        (df['Timestamp'].dt.date >= start_date) &
        (df['Timestamp'].dt.date <= end_date) &
        (df['Type Match'].isin(selected_type_matches)) &
        (df['Victory'].isin(selected_victory_values)) &
        (df['Opening'].isin(selected_openings))
    ]
    
    return df_filtered
