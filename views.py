from flask import Flask
from flask import request
import requests

app = Flask(__name__)

APP_CONFIG = {
        'url': "http://localhost:9494/test",
    "api_key": "5ff4679f6dae9f72ce96d1e30be75f333c135c0517a9f9b078bf5a7a34c75f9f"
}


@app.route("/test")
def test():
    html = "<html style=background:white;font-size:24px><div>HELLO WORLD</div></html>"
    return html

#def get_posts(access_token):
def get_posts():
    access_token = "bc944872f6210c7ed8abf75556d644469c6440d35ce60f7fa1a158daa4b92152"
#    responses = self.make_request("GET", "posts", {"day": day}, context)
    args = {
    'authorization': 'Bearer ' + access_token,
    }
    date = {
    'days_ago' : 1
            }
    try:
        r = requests.get("https://api.producthunt.com/v1/posts?%7B%7D=20", headers=args, data=date)
        print r
        posts = r.json()['posts']
        print posts[0]
        return posts
    except Exception, ex:
        print "Something horribly wrong happened..."

def render_user(me):
    html = "<html style=background:white;font-size:24px><div>%(displayname)s</div><div>%(email)s</div></html>" %  me
    html += "<br/>DICT BELOW <br/>"
    for k,v in me.items():
        html += "key: %s  value: %s<br/>" % (k,v)
    return html


def render_posts(posts):
    html = "<html style=background:white;font-size:24px><div>rendering posts</div></html>"
    html += "<br/>DICT BELOW <br/>"
    for post in posts:
        print post
        #        for k,v in post.items():
#            html += "key: %s  value: %s<br/>" % (k,v)
#        print "<a href=\"{}\">name = {} : votes {}.</a>".format(post['redirect_url'].encode('utf-8'),post['name'].encode('utf-8'), post['votes_count'])


        html += "<a href=\"{}\">name = {} : votes {}.</a>".format(post['redirect_url'],post['name'].encode('utf-8'), post['votes_count'])
        html += "<br/>"
    return html


@app.route("/")
def print_posts():
    print "trying to access posts"
#    args = {
#        "client_id": APP_CONFIG['url'],
#        "client_secret": APP_CONFIG['api_key'],
#        "scope": "https://chalkable.com",
#        "redirect_uri": APP_CONFIG['url'],
#        "grant_type": "authorization_code",
#        "code": request.args.get("code", '')
#    }
#    r = requests.post("https://chalkable-access-control.accesscontrol.windows.net/v2/OAuth2-13", data=args)
#    result = r.json()
#    access_token = result['access_token']
#    me = get_current_user(access_token)
    posts = get_posts()
    return render_posts(posts)

if __name__ == "__main__":
    app.run(debug=True)

