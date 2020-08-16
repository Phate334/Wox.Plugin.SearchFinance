import webbrowser
from wox import Wox, WoxAPI


class HelloWorld(Wox):

    def query(self, query):
        fugle_url = 'https://www.fugle.tw/ai/' + query
        results = []
        results.append({
            "Title": "Search in Fugle",
            "SubTitle": "Query: {}".format(query),
            "IcoPath": "Images/up.png",
            "JsonRPCAction": {
                "method": "openUrl",
                "parameters": [fugle_url]
            }
        })
        return results

    def openUrl(self, url):
        webbrowser.open(url)
        WoxAPI.change_query(url)


if __name__ == "__main__":
    HelloWorld()