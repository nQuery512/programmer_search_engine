#### Flask server ####
from bs4 import BeautifulSoup
import logging
from flask import Flask, request, render_template
import re
import requests
import time
from urllib.request import urlopen
from selenium import webdriver
import favicon
import json

import utility.stack_parser as stack_parser

html_link_regex = re.compile("(?<=/url\?q=)(htt.*://.*)")
api = stack_parser.init_stack_api()
# TODO
# Optimisation :
#     - Compilation des regex au lancemnt du serveur

# Librairie perso
#Parser stackvoerflow afin de trouver une réponse approprié lors d'un problème
#Parser différent site et en extraire du code source
    #Connection api stackoverflow

app = Flask(__name__) 
#driver = webdriver.ChromeOptions()
#driver.add_argument('headless')
#browser = webdriver.Chrome(options=driver)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

#Interaction backend -- StackAPI
@app.route('/snippets', methods=['GET', 'POST'])
def snippets():
    id = 48086812
    data = stack_parser.get_best_answers(api, id)
    print(data)

    json_response = {}
    json_response['code'] = data
    return render_template("snippets.html", json_response=json.dumps(json_response, ensure_ascii=False).encode('utf-8'))
    #return json.dumps(json_response, ensure_ascii=False).encode('utf-8')

@app.route('/skill-learn')
def ok():
    return render_template('search.html')

@app.route('/search')
def search_raw():
    #print("Bienvenue, ouverture des 5 meilleures page Web pour apprendre "+args.skill_to_learn)
    query = request.args.get('q')
    IT_learning_words = ["ressources", "documentation", "cheatsheet", "good practice", "code samples"]
    best_links = []
    best_thumbnails = []

    # Boucle des recherches
    for good_word in IT_learning_words:
        url = "https://www.google.fr/search?q=" +query+" "+good_word
        print("requesting: "+query+" "+good_word)
        page = requests.get(url)
        soup = BeautifulSoup(page.content,features="html.parser")
        links = soup.findAll("a")

        # Boucle des résultats
        for link in soup.find_all("a",href=html_link_regex):
            link = re.split(":(?=http)",link["href"].replace("/url?q=",""))
            link = str(link[0].split("&sa=")[0])
            
            # Si le lien nettoyé existe déjà, on passe a un autre mot clef
            if(link in best_links):
                pass

            # Sinon:
            else:
                # On entre l'url trouvé dans la liste des meilleurs liens
                best_links.append(link)
                
                # On crée la miniature
                #browser.get(link)
                #browser.save_screenshot(query+"_"+good_word+'.png')
                #if( ".pdf" in link[-4:]):
                 #   best_thumbnails.append("https://cdn4.iconfinder.com/data/icons/file-extensions-1/64/pdfs-512.png")
                  #  break

                # On cherche le lien du favicon
                #icons = favicon.get(link)
                #if(len(icons) != 0):
                 #   icon = icons[0]
                 #   print("Icon links: "+ icon.url)
                 #   best_thumbnails.append(icon.url)
                    # On entre l'url du favicon
                #else:
                 #   best_thumbnails.append(None)

                #print("link= ",link)
                #print("\n")
                break

    json_response = {}
    json_response["thumbnail_list"] = best_thumbnails
    json_response["url_list"] = best_links
    json_response["epoch_time"] = int(time.time())
    json_response["result_count"] = len(best_links)
    json_response["url_label"] = IT_learning_words
    json_response["query_text"] = query
        
    #Render template page des résultats
    #return json.dumps(json_response, ensure_ascii=False).encode('utf-8')
    return render_template('result.html', json_response=json.dumps(json_response, ensure_ascii=False).encode('utf-8'))
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    
    '''
    # Boucle d'ouverture des liens
    for best_link in best_links:
        print("Opening "+ str(best_link)+'\n')
        webbrowser.open(best_link)
    '''