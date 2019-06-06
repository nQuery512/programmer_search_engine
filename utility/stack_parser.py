from stackapi import StackAPI
import re

#Compilation de la regex
code_pattern = re.compile("<code>(.*?)</code>", re.DOTALL)

# Pas de token requis, retourne une instance de l'API, prète à être requêter
def init_stack_api():
    try:
        api = StackAPI("stackoverflow")
    except StackAPIError as e:
        print(e.message)

    return api

def get_best_answers(api, question_id):
    # Requêtage de l'API
    res = api.fetch("questions/"+str(question_id)+"/answers", sort='votes', filter='withbody')
    # On selectionne les données de réponses
    test= res['items']

    # Capture de la réponse accepté
    for item in test:
        if item['is_accepted'] == True:
            best_answer = item['body']
            #print("\nACCEPTED: ",item['is_accepted'])

    #print(res,'\n\n')
    ret=[]

    # Capture du code écrit dans les réponses
    for match in re.finditer(code_pattern, best_answer):
        ret.append(match.group(1))
    return ret

'''
#Initalisation de l'API
api = init_stack_api()

if __name__ == "__main__":

    # ID aléatoire pour les tests
    id = 48086812
    print(get_best_answers(id))
'''
