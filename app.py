from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

client = MongoClient('mongodb+srv://id:pw@product.a76xeom.mongodb.net/?retryWrites=true&w=majority')
db = client.Special_price_MOA

@app.route('/')
def main():
    return render_template("특가모아_main.html")

@app.route('/coopang')
def coopang():
    return render_template("특가모아_coopang.html")

@app.route('/street_11th')
def street():
    return render_template("특가모아_11th_street.html")

@app.route('/auction')
def auction():
    return render_template("특가모아_auction.html")

@app.route('/gmarket')
def gmarket():
    return render_template("특가모아_gmarket.html")

@app.route('/interpark')
def interpark():
    return render_template("특가모아_interpark.html")

@app.route('/tmon')
def tmon():
    return render_template("특가모아_tmon.html")

@app.route('/wemap')
def wemap():
    return render_template("특가모아_wemap.html")

@app.route('/search')
def search():
    return render_template("특가모아_search.html")

@app.route("/coopang_item", methods=["GET"])
def coopang_item_get():
    coopang_list = list(db.coopang.find({}, {'_id':False}))
    return jsonify({'coopangs': coopang_list})

@app.route("/street_11th_item", methods=["GET"])
def street_item_get():
    street_11th_list = list(db.street_11th.find({},{'_id':False}))
    return jsonify({'street_11ths':street_11th_list})

@app.route("/auction_item", methods=["GET"])
def auction_item_get():
    auction_list = list(db.auction.find({},{'_id':False}))
    return jsonify({'auctions':auction_list})

@app.route("/gmarket_item", methods=["GET"])
def gmarket_item_get():
    gmarket_list = list(db.gmarket.find({},{'_id':False}))
    return jsonify({'gmarkets':gmarket_list})

@app.route("/interpark_item", methods=["GET"])
def interpark_item_get():
    interpark_list = list(db.interpark.find({},{'_id':False}))
    return jsonify({'interparks':interpark_list})

@app.route("/tmon_item", methods=["GET"])
def tmon_item_get():
    tmon_list = list(db.tmon.find({},{'_id':False}))
    return jsonify({'tmons':tmon_list})

@app.route("/wemap_item", methods=["GET"])
def wemap_item_get():
    wemap_list = list(db.wemap.find({},{'_id':False}))
    return jsonify({'wemaps':wemap_list})

@app.route("/search_item", methods=["GET"])
def search_item_get():
    search_receive = request.args.get('query')
    search_list1 = list(db.coopang.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list2 = list(db.street_11th.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list3 = list(db.auction.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list4 = list(db.gmarket.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list5 = list(db.interpark.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list6 = list(db.tmon.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list7 = list(db.wemap.find({'Title': {'$regex': search_receive, '$options': 'i'}},{'_id':False}))
    search_list = search_list1 + search_list2 + search_list3 + search_list4 + search_list5 + search_list6 + search_list7
    
    return jsonify({'searchs':search_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
