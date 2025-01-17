from duckduckgo_search import DDGS
import wget

out_dir = "salida"

def loadResults(text):
    results = DDGS().text(text, region='es-es', safesearch='off', timelimit='n', max_results=500)
    return results

data = loadResults('site:juntadeandalucia.es inurl:educacion/portals/galion filetype:pdf')

for resultado in data:
    print ("\nDescargando... " + resultado['href']+"\n")
    try: 
        wget.download(resultado['href'], out_dir)
    except:
        print("**** Error al descargar el archivo: "+resultado['href']+" **** \n")
