'''
Import Flask and create an to serve the functionality of DecisionTreeClassifier model
'''
from flask import Flask, jsonify
from flask_cors import CORS
import ExpertSystem


app = Flask(__name__)
CORS(app)


@app.route('/api/options/<node_index>', methods=['GET'])
def get_node_options_from_index(node_index=0):
    node_index = int(node_index)

    # If is leaf_node return the associated class label
    if ExpertSystem.is_leaf(model.tree_, node_index):
        node_class = ExpertSystem.get_class(model.tree_, node_index)
        label = model.classes_[node_class]

        return jsonify({
            'node_index': node_index,
            'feature': '',
            'question': '',
            'options': [],
            'label': label
        })
    
    # If it is not a leaf_node
    feature, question, options = ExpertSystem.get_feature_options_from_node(model.tree_, label_encoders, node_index)
    # if type(options[0]) == list:
    #     options = [option[0] for option in options]
    return jsonify({
        'node_index': node_index,
        'feature': feature,
        'question': question,
        'options': options,
        'label': ''
    })


# Get node_index for left child
@app.route('/api/left/<node_index>', methods=['GET'])
def get_left_node_index(node_index=0):
    node_index = int(node_index)

    left_node_index = ExpertSystem.get_left_child(model.tree_, node_index)
    return jsonify({
        'node_index': int(left_node_index)
    })


# Get node_index for right child
@app.route('/api/right/<node_index>', methods=['GET'])
def get_right_node_index(node_index=0):
    node_index = int(node_index)

    right_node_index = ExpertSystem.get_right_child(model.tree_, node_index)
    return jsonify({
        'node_index': int(right_node_index)
    })


if __name__ == '__main__':
    model, label_encoders = ExpertSystem.import_model()

    # leaf_nodes = ExpertSystem.find_leaf_nodes(model.tree_, 0)
    # print(leaf_nodes)

    app.run()