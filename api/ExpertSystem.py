'''
Import DecisionTreeClassifier model from 'decision_tree.joblib' file, and label encoders from 'label_encoders.joblib' file.
'''
import joblib
import math
# import numpy


# Global variables
decision_tree = None
label_encoders = None
columns = ['Titlu', 'Angajator', 'Tip job', 'Nivel job', 'Remote', 'Paulesti', 'Blaj', 'Ramnicu Valcea', 'Baicoi', 'Husi', 'Clinceni', 'Sinaia', 'Ramnicu Sarat', 'Targu Secuiesc', 'Busteni', 'Pitesti', 'Chisinau', 'Targu Mures', 'Stefanestii de Jos', 'BUCHAREST', 'Sfantu Gheorghe', 'Titu', 'Bals', 'Timisoara', 'Moreni', 'Hunedoara', 'Lugoj', 'Victoria', 'Campina', 'Baia Mare', 'Vatra Dornei', 'Harsova', 'Alt oras', 'Strainatate', 'Fetesti', 'Focsani', 'Ploiesti', 'Orastie', 'Otopeni', 'Sebes', 'Falticeni', 'Targu Jiu', 'Iasi', 'Gaesti', 'Buftea', 'Voluntari', 'Resita', 'Urziceni', 'Navodari', 'Babadag', 'Floresti', 'Drobeta Turnu-Severin', 'Zalau', 'Radauti', 'Codlea', 'Brazi', 'Constanta', 'Mioveni', 'Craiova', 'Oradea', 'Miercurea-Ciuc', 'Medgidia', 'Ilfov', 'Calarasi', 'Braila', 'Chitila', 'Mihail Kogalniceanu', 'Sibiu', 'Campulung Muscel', 'Sighetu Marmatiei', 'Abroad', 'Brasov', 'Targoviste', 'BUCURESTI', 'Salonta', 'Buzau', 'Suceava', 'Giurgiu', 'Bacau', 'Sacele', 'Slobozia', 'Arad', 'Tecuci', 'Barlad', 'Slatina', 'Alexandria', 'Turnu Magurele', 'Boldesti-Scaieni', 'Botosani', 'Vaslui', 'Bistrita', 'Satu-Mare', 'Cluj Napoca', 'Dej', 'Baia', 'Piatra Neamt', 'Adjud', 'Afumati', 'Covasna', 'Balotesti', 'Deva', 'Mizil', 'Lipova', 'Targu Neamt', 'Mangalia', 'Galati', 'Bocsa', 'Pascani', 'Alba Iulia', 'Ghimbav', 'Aiud', 'Pucioasa', 'Tulcea', 'Ineu', 'Popesti Leordeni', 'Publicitate - Agentii publicitate', 'Agricultura', 'Juridic', 'Asistent Manager', 'Educatie - Training', 'Productie', 'Arhitectura - Design - Proiectare', 'Import - Export', 'Telecomunicatii', 'Achizitii - Logistica - Aprovizionare', 'Fundatii - Voluntariat - ONG', 'Resurse Umane - Psihologie', 'Marketing', 'Secretariat - Administrativ', 'Asigurari - Intermedieri financiare', 'Transporturi', 'IT Hardware', 'Suport clienti', 'Altele', 'Banci', 'Radio-Televiziune', 'Management - Consultanta', 'Internship', 'Media - Jurnalism', 'Turism', 'Internet - eCommerce', 'Inginerie', 'IT Software', 'Hoteluri - Restaurante - Cafenele', 'Vanzari', 'Constructii', 'Farmacie - Medicina', 'Imobiliare - Real Estate', 'Relatii Publice', 'Controlul calitatii', 'Administratie - Stiinte politice', 'Chimie - Petrochimie', 'Contabilitate - Finante', 'Contabilitate Finante', 'Retail - Comert']


# Import model from file
def import_model():
    decision_tree = joblib.load('decision_tree.joblib')
    label_encoders = joblib.load('label_encoders.joblib')
    return decision_tree, label_encoders


# Get feature and options values from a node
def get_feature_options_from_node(tree, label_encoders, node_index):
    feature_index = tree.feature[node_index]
    feature = columns[feature_index + 1]
    

    if(feature_index > 3): # Columns with boolean values
        options = ["Nu", "Da"]
    else:
        label_encoder = label_encoders[feature]
        options = [
            label_encoder.inverse_transform([math.floor(tree.threshold[node_index])])[0],
            label_encoder.inverse_transform([math.ceil(tree.threshold[node_index])])[0]
        ]
    
    if feature_index == 0:
        question = "La care dintre angajatori doriti sa aplicati?"
    elif feature_index == 1:
        question = "Ce tip de job doriti?"
    elif feature_index == 2:
        question = "Care este nivelul jobului dorit?"
    elif feature_index == 3:
        question = "Doriti un job remote?"
    elif feature_index < 114:
        question = f"Doriti sa activati in orasul {feature}?"
    else:
        question = f"Doriti sa activati in domeniul {feature}?"

    return feature, question, options


# Check if a node is a leaf
def is_leaf(tree, node_index):
    return tree.children_left[node_index] == tree.children_right[node_index] == -1


# Return the class of a leaf node
def get_class(tree, node_index):
    class_counts = tree.value[node_index][0]
    return class_counts.argmax()


# Get index of left child node
def get_left_child(tree, node_index):
    return tree.children_left[node_index]


# Get index of right child node
def get_right_child(tree, node_index):
    return tree.children_right[node_index]


# Find all leaf nodes; for debugging purposes
def find_leaf_nodes(tree, node_index):
    if is_leaf(tree, node_index):
        return [node_index]
    else:
        return find_leaf_nodes(tree, get_left_child(tree, node_index)) + find_leaf_nodes(tree, get_right_child(tree, node_index))


# if __name__ == '__main__':
#     decision_tree, label_encoders = import_model()

#     current_node = 0
#     while(not is_leaf(decision_tree.tree_, current_node)):
#         feature, options = get_feature_options_from_node(decision_tree.tree_, label_encoders, current_node)
#         print(f'Feature: {feature}, Options: {options}')

#         # Choose a path
#         option = input('Choose an option: (l/r)')
#         if option == 'l':
#             current_node = get_left_child(decision_tree.tree_, current_node)
#         else:
#             current_node = get_right_child(decision_tree.tree_, current_node)
    
#     print(current_node)
#     node_class = get_class(decision_tree.tree_, current_node)
#     print(f'Class: {node_class}')
#     print(f'Job: {decision_tree.classes_[node_class]}')
