from flask import Flask , render_template , request , jsonify

app =Flask(__name__)

items=[
        {"id":1,"Name":"Item1"},
        {"id":2,"Name":"Item2"}
]

@app.route('/',methods=['GET'])
def home():
    return "Welcome to the website"
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

#get items by id
@app.route('/items/<int:id>',methods=['GET'])
def get_item(id):
    item=next((item for item in items if item['id'] == id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)
# create a task if id not found
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]


    }
    items.append(new_item)
    return jsonify(new_item)

# cehcking the put method here
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    # item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

#delete
app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    item=next((item for item in items if item['id'] == item_id),None)
    return jsonify({"result":"Item deleted" })
if __name__=="__main__":
    app.run(debug=True)