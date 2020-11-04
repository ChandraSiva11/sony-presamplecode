import socket
import time
import asyncio


async def send_n_recv_data(question):
    ip = '127.0.0.1'
    tcp_port = 5005
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd.connect((ip, tcp_port))
    sockfd.send(question.encode())
    data = sockfd.recv(1024)
    sockfd.close()
    return(data)


async def get_answer_by_question(question):
    print(f"Quesion: {question}")
    reply = send_n_recv_data(question)
    print(f"Asnwer : {reply}")
    print()
    await asyncio.sleep(1)


async def main():
    task1 = get_answer_by_question("One-page question")
    task2 = get_answer_by_question("One-line question")
    task3 = get_answer_by_question("Booleon question")
    await asyncio.wait([task1, task2, task3])
    # await asyncio.sleep(delay)


if __name__ == '__main__':
	main()