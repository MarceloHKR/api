# Implementa uma interface usando Tkinter para previsão do tempo

import requests
import tkinter as tk

# Janela principal
root = tk.Tk()

# Título da janela
root.title("Previsão do Tempo")

# Largura e altura da janela
root.geometry("400x600")

# Label da caixa de entrada de texto
label = tk.Label(root, text="Digite a cidade", font=("Helvetica", 16), width=30)

# Posiciona o label na janela
label.grid(row=0, column=0, padx=10, pady=10)

# Entrada de texto para digitar a cidade
city = tk.Entry(root, font=("Helvetica", 16), justify="center", width=30)

# Posiciona a entrada de texto na janela
city.grid(row=1, column=0, padx=10, pady=10)

#Função que transforma um nome de cidade ou local em coordenadas geográficas
def get_geocode(city: str):
    #URL da API geocode
    url = 'https://geocode.maps.co/search?q={nome_do_lugar}&api_key={api_key}'

    #chave da API
    api_key = '65c416d7670a5986487780dyldad80c'

    #chamando a API de geocode
    response = requests.get(url=url.format(nome_do_lugar=city, api_key=api_key))

    latitude = response.json()[0]['lat']
    longitude = response.json()[0]['lon']

    return {'latitude': latitude, 'longitude': longitude}

#Função para buscar a previsão do tempo
def call_weatger_api(city: str):
    #Chama a api do geocode para buscar a coordenada
    geocode = get_geocode(city)

    #chave da API de previsão do tempo
    api_key = '492485aff3ea4b06013a377a9fec8002'

    #URL da API de previsão do tempo
    url_forecast = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'

    #chamando a API de previsão do tempo
    response = requests.get(url=url_forecast.format(lat=geocode['latitude'], lon=geocode['longitude'], api_key=api_key))

    #extraindo a lista de previsões do tempo
    forecast_list = response.json()['list']

    #extraindo e guardando o nome da cidade da previsão retornada
    nome_da_cidade = response.json()['city']['name']

    #lista com as informações relevantes a serem exibidas na tela
    forecast_data = []

    #Iterar sobre a lista de previsões somente nos 5 primeiros resultados
    for forecast in forecast_list[:5]:
        #data e hora do periodo da previsão
        datahora = forecast['dt_txt']

        #temperatuda mínima do período
        temp_min = forecast['main']['temp_min']

        #temperatura máxima do período
        temp_max = forecast['main']['temp_max']

        #Descrição do período
        description = forecast['weather'][0]['description']

        forecast_data.append(
            {
                'nome_da_cidade': nome_da_cidade,
                'datahora': datahora,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'description': description
            }
        )
    return forecast_data
    

# Função para buscar a previsão do tempo
def get_weather(city):
    forecast_data = call_weatger_api(city)

    #limpa o frame da previsão do tempo
    for widget in weather_frame.winfo_children:
        widget.destroy()

    #limpa o label da cidade
        city_label.config(text=forecast_data[0]['nome_da_cidade'])

    #itera sobre os dados de previsão e adiciona no frame
    for forecast in forecast_data:
        label_text = forecast['datahora']
        label_text += ' ' + str(forecast['tenp_min'])
        label_text += ' ' + str(forecast['temp_max'])
        label_text += ' ' + forecast['description']
        #cria um label para mostrar a data e hora, temperatura mínima, temperatura máxima e descrição do tempo no frame da previsão do tempo
        weather_label = tk.Label(
            weather_frame,
            text=label_text,
            font = ("Helvetica", 12),
            justify="left"
        )

        weather_label.pack(pady=10)


# Botão para buscar a previsão do tempo
get_weather_btn = tk.Button(root, text="Buscar Previsão do Tempo", command=lambda: get_weather(city.get()))

# Posiciona o botão na janela
get_weather_btn.grid(row=2, column=0, padx=10, pady=10)

# Label para mostrar a previsão do tempo
weather_label = tk.Label(root, text="Previsão do Tempo")

# Posiciona o label na janela
weather_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#label para mostrar o nome da cidade
city_label = tk.Label(root, text="", font=("Helvetica",  16))

#posiciona o label na janela
city_label.grid(row=4, column=0, padx=10, pady=10)

#cria um frame para mostrar a previsão do tempo
weather_frame = tk.Frame(root)

#posiciona o frame na janela
weather_frame.grid(row=5, column=0, padx=10, pady=10)


# Finaliza a janela
root.mainloop()

'''fazer em casa, buscar e mostrar estado, país etc'''