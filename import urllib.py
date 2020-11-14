# Importação da biblioteca necessária
import urllib.request

# Método que fará a ação de encurtar
# (Recebe a url de parâmetro)
def tiny_url(url):
    # Aqui é a api do tinyurl
    apiurl = "http://tinyurl.com/api-create.php?url="
    # Abrimos a api concatenando com a url desejada
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    # Retorna o link encurtado
    return tinyurl.decode("utf-8")

# Chama e printa na tela o método tiny_url passando como parâmetro a
# url desejada
print(tiny_url('https://www.programadoruniversitario.com.br/'))