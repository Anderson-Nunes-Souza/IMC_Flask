from flask import Flask

app = Flask(__name__)

@app.route("/calculate/")
#Função que  calcula o IMC recebido do input e do Teste de cenários
def CalculaIMC():
    altura: float = 1.80
    peso: float = 70
    #IMC = Peso / Altura²
    imc = float(peso / (altura * altura))
    imc_formatado = round(imc, 2)
    
    #Magreza, quando o resultado é menor que 18,5 kg/m2;
    if imc_formatado < 18.5:
        return(f"Imc de: {imc_formatado} = Magreza")
    # Normal, quando o resultado está entre 18,5 e 24,9 kg/m2;
    if imc_formatado >=18.5 and imc_formatado <=24.9:
        return(f"Imc de: {imc_formatado} = Normal")

    # Sobrepeso, quando o resultado está entre 24,9 e 30 kg/m2;
    if imc_formatado >24.9 and imc_formatado <= 30:
        return(f"Imc de: {imc_formatado} = Sobrepeso")

    # Obesidade, quando o resultado é maior que 30 kg/m2;
    if imc_formatado >30:
        return(f"Imc de: {imc_formatado} = Obeso")


app.run(host='localhost', port=3000, debug=True)