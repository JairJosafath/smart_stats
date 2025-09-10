from ollama import Client

print(Client(host="http://host.docker.internal:11434").list())
