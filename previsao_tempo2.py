# Implementa uma interface usando Tkinter para previsão do tempo

import requests
import tkinter as tk

# Janela principal
root = tk.Tk()

# Título da janela
root.title("Previsão do Tempo")

# Largura e altura da janela
# root.geometry("400x600")

# Label da caixa de entrada de texto
label = tk.Label(root, text="Digite a cidade", font=("Helvetica", 16), width=30)

# Posiciona o label na janela
label.grid(row=0, column=0, padx=10, pady=10)

# Entrada de texto para digitar a cidade
city = tk.Entry(root, font=("Helvetica", 16), justify="center", width=30)

# Posiciona a entrada de texto na janela
city.grid(row=1, column=0, padx=10, pady=10)

# Função para pegar o geocode da cidade
def get_geocode(city):
    # URL da API
    url = 'https://geocode.maps.co/search?q={nome_do_lugar}&api_key={api_key}'

    # Chave da API
    api_key = '65c416d7670a5986487780dyldad80c'

    # Faz a chamada da API
    response = requests.get(url.format(nome_do_lugar=city, api_key=api_key))

    # Verifica se a chamada foi bem sucedida
    if response.status_code == 200:
        # Pega o JSON retornado pela API
        data = response.json()

        # Pega o geocode da cidade
        latitude = data[0]['lat']
        longitude = data[0]['lon']

        # Retorna o geocode
        return {"latitude": latitude, "longitude": longitude}
    else:
        # Retorna None se a chamada não foi bem sucedida
        return None

# Função para chamar a API de previsão do tempo
def call_weather_api(city):

    # Pega o geocode da cidade
    geocode = get_geocode(city)

    # Verifica se o geocode foi retornado
    if geocode:
        # URL da API
        url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'

        # Chave da API
        api_key = '492485aff3ea4b06013a377a9fec8002'

        # Faz a chamada da API
        response = requests.get(url.format(lat=geocode['latitude'], lon=geocode['longitude'], api_key=api_key))

        # Verifica se a chamada foi bem sucedida
        if response.status_code == 200:
            # Pega o JSON retornado pela API
            data = response.json()

            # Retorna o JSON
            return data
        else:
            # Retorna None se a chamada não foi bem sucedida
            return None
    else:
        # Retorna None se o geocode não foi retornado
        return None


# Função para buscar a previsão do tempo
def get_weather(city):
    # Limpa o frame da previsão do tempo
    for widget in weather_frame.winfo_children():
        widget.destroy()

    # Limpa o label da cidade
    city_label.config(text="")

    # Chama a API de previsão do tempo
    data = call_weather_api(city)

    # Verifica se a chamada foi bem sucedida
    if data:
        # Importa a biblioteca datetime
        from datetime import datetime
        # Importa a biblioteca PIL
        from PIL import Image, ImageTk

        # Pega a lista de previsões do tempo
        weather_list = data["list"]

        # Captura o nome da cidade
        city_name = data["city"]["name"]

        # Coloca o nome da cidade no label
        city_label.config(text=city_name)

        # Itera sobre a lista de previsões do tempo
        for row, weather in enumerate(weather_list[:5]):
            # Converte a data e hora "dt_txt" para o formato D/M/A H:M:S
            date = datetime.strptime(weather["dt_txt"], "%Y-%m-%d %H:%M:%S")
            date = date.strftime("%d/%m/%Y %H:%M:%S")

            # Pega a temperatura mínima
            min_temp = weather["main"]["temp_min"]

            # Pega a temperatura máxima
            max_temp = weather["main"]["temp_max"]

            # Pega a descrição do tempo
            description = weather["weather"][0]["description"]

            # Pega o icone do tempo
            icon_id = weather["weather"][0]["icon"]

            # Cria a URL do icone do tempo
            icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"

            # Faz o download do icone do tempo
            icon_response = requests.get(icon_url)

            # Verifica se o download foi bem sucedido
            if icon_response.status_code == 200:
                # Salva o icone do tempo em um arquivo
                with open(f"{icon_id}.png", "wb") as f:
                    f.write(icon_response.content)

            # Cria um objeto Image do icone do tempo
            image = Image.open(f"{icon_id}.png")

            # Cria um Label para mostrar o icone do tempo
            icon = ImageTk.PhotoImage(image)

            # Posiciona o label no frame da previsão do tempo
            icon_label = tk.Label(weather_frame, image=icon, bg="darkgray")
            icon_label.image = icon

            # Cria um Label para mostrar a data e hora, temperatura mínima, temperatura máxima e descrição do tempo no frame da previsão do tempo
            weather_label = tk.Label(weather_frame, text=f"{date} - Mínima: {min_temp}°C - Máxima: {max_temp}°C - {description}", font=("Helvetica", 12), justify="left")
            
            # Posiciona o label no frame da previsão do tempo
            icon_label.grid(row=row, column=0, padx=10, pady=5)
            
            # Posiciona o label no frame da previsão do tempo
            weather_label.grid(row=row, column=1, padx=10, pady=5)

            # Imprime a data e hora, temperatura mínima, temperatura máxima e descrição do tempo
            # print(date, min_temp, max_temp, description)


# Botão para buscar a previsão do tempo
get_weather_btn = tk.Button(root, text="Buscar Previsão do Tempo", command=lambda: get_weather(city.get()))

# Posiciona o botão na janela
get_weather_btn.grid(row=2, column=0, padx=10, pady=10)

# Label para mostrar a previsão do tempo
weather_label = tk.Label(root, text="Previsão do Tempo")

# Posiciona o label na janela
weather_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label para mostrar o nome da cidade
city_label = tk.Label(root, text="", font=("Helvetica", 16))

# Posiciona o label na janela
city_label.grid(row=4, column=0, padx=10, pady=10)

# Cria um frame para mostrar a previsão do tempo
weather_frame = tk.Frame(root)

# Posiciona o frame na janela
weather_frame.grid(row=5, column=0, padx=10, pady=10)


root.bind('<Escape>', lambda event: root.quit())

# Finaliza a janela
root.mainloop()