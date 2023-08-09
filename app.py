from flask import Flask, request ,render_template
from autoscraper import AutoScraper

scraper=AutoScraper()
scraper.load('flipkart_search')

app=Flask(__name__)

def get_flipkart_result(query):
    url="https://www.flipkart.com/search?q=%s" % query
    print(url)
    result = scraper.get_result_similar(url,group_by_alias=True)
    return aggregat_result(result)

def aggregat_result(result):
    f=[]
    for i in range(len(list(result.values())[0])):
        try:
            f.append({alias: result[alias][i] for alias in result})
        except:
            pass
    return f

@app.route('/')
def find():
    return render_template('index.html')

@app.route('/items',methods=['POST','GET'])
def scrap():
    query=request.form.get('search')
    print(query)
    result=get_flipkart_result(query)
    print(result)
    return render_template('after.html',data=result)

if __name__ == "__main__":
    app.run(debug=True)