import asyncio
import time
import json
import aiohttp
from statistics import mean


# BASE_URL = "http://127.0.0.1:8080"
BASE_URL = " http://172.17.0.2:5000/"

# Função assíncrona para enviar requisições HTTP
async def fetch(session, url, method="GET", data=None):
    try:
        if method == "POST":
            async with session.post(url, json=data) as response:
                return await response.text()
        elif method == "DELETE":
            async with session.delete(url, json=data) as response:
                return await response.text()
        else:
            async with session.get(url) as response:
                return await response.text()
    except Exception as e:
        return str(e)

# Função principal para executar o teste de estresse
async def run_test(total_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        start_time = time.time()

        requests_per_endpoint = total_requests // 5

        for i in range(requests_per_endpoint):
            tasks.append(fetch(session, f"{BASE_URL}/convert?from=USD&to=BRL&amount=10"))
            tasks.append(fetch(session, f"{BASE_URL}/convert?from=BTC&to=EUR&amount=0.1"))
            tasks.append(fetch(session, f"{BASE_URL}/convert?from=ETH&to=USD&amount=1"))
            tasks.append(fetch(session, f"{BASE_URL}/currencies", method="POST", data={"currency": "TEST", "rate": 1.23}))
            tasks.append(fetch(session, f"{BASE_URL}/currencies", method="DELETE", data={"currency": "TEST"}))

            if (i + 1) % 10 == 0:
                print(f"Enviadas {i + 1} requisições para cada endpoint...")

        responses = await asyncio.gather(*tasks)
        end_time = time.time()

        total_time = end_time - start_time
        successful_requests = sum(1 for r in responses if r)
        failed_requests = len(responses) - successful_requests

        print(f"Total de requisições: {len(responses)}")
        print(f"Requisições bem-sucedidas: {successful_requests}")
        print(f"Requisições falhadas: {failed_requests}")
        print(f"Tempo total: {total_time:.2f} segundos")
        print(f"Requisições por segundo: {len(responses) / total_time:.2f}")

        return responses, total_time

# Função para analisar as respostas do teste de estresse
def analyze_responses(responses, total_time):
    success_times = []
    fail_times = []

    for response in responses:
        if response:
            try:
                response_time = float(response)
                success_times.append(response_time)
            except ValueError:
                continue
        else:
            fail_times.append(response)

    if success_times:
        print(f"Tempo médio de resposta (sucesso): {mean(success_times):.2f} ms")
    if fail_times:
        print(f"Tempo médio de resposta (falha): {len(fail_times) / total_time:.2f} requisições por segundo")

# Função para gerar gráficos dos resultados do teste
# def plot_results(success_times, fail_times, total_requests, total_time):
#     plt.figure(figsize=(12, 6))

#     plt.subplot(1, 2, 1)
#     plt.plot(success_times, label="Sucesso")
#     plt.xlabel("Requisições")
#     plt.ylabel("Tempo de resposta (ms)")
#     plt.title("Tempo de Resposta por Requisição")
#     plt.legend()

#     plt.subplot(1, 2, 2)
#     labels = ['Sucesso', 'Falha']
#     sizes = [len(success_times), len(fail_times)]
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#     plt.title("Distribuição de Requisições")

#     plt.tight_layout()
#     plt.show()

# Função principal que executa o teste e analisa os resultados
def main():
    total_requests = 1000
    responses, total_time = asyncio.run(run_test(total_requests))
    analyze_responses(responses, total_time)

    success_times = [float(r) for r in responses if r and r.replace('.', '', 1).isdigit()]
    fail_times = [r for r in responses if not (r and r.replace('.', '', 1).isdigit())]

    # plot_results(success_times, fail_times, total_requests, total_time)

# Execução da função principal
if __name__ == '__main__':
    main()