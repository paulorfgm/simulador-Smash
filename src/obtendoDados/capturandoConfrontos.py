import subprocess
import os
import csv
import ast

# Caminho para o subprocesso de requisição dos confrontos, e sua execução
file_path = os.path.join('F:', 'Final Project Smash', 'src', 'obtendoDados', 'requisicaoConfrontos.py')
result = subprocess.run(['python', file_path], capture_output=True, text=True)
data = result.stdout
data = ast.literal_eval(data)

# Caminho e nome do arquivo de saída
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_filename = 'matchups.csv'
csv_file_path = os.path.join(current_directory, csv_filename)

vector = []

# Processa cada entrada retornada pelo subprocesso
for entry in data:
    
    # Pega o nome dos personagens separados por 'vs'
    characters = entry['matchup'].split(' vs ')
    
    # Pega as porcentagens, separadas por '-', e tiramos o símbolo %
    percentages = entry['percentages'].split(' - ')
    percentages = [float(p.replace('%', '')) for p in percentages]
    
    # Adicionamos essas entradas ao vetor
    vector.append([characters[0], characters[1], percentages[0], percentages[1]])


# Escrevemos cada entrada do vetor para um csv, colocando também suas colunas
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Personagem1', 'Personagem2', 'taxaVitoria1', 'taxaVitoria2'])
    writer.writerows(vector)
