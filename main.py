from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        self.response.out.write('Hello,<br>')

        if user:
            greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>) <br>" %
                        (user.nickname(), users.create_logout_url("/")))
            self.response.out.write("<html><body>%s</body></html>" % greeting)
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write('Nick: ' + user.nickname() + '<br>')
            self.response.out.write('Auth Dom: ' + user.auth_domain() + '<br>')
            self.response.out.write('UID: ' + user.user_id() + '<br>')
            self.response.out.write('Email: ' + user.email() + '<br>')
        else:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write('URL: ' + users.create_login_url('http://www.google.com') + '<br>')
            self.response.out.write('URI: ' + self.request.uri + '<br>')
            #self.redirect(users.create_login_url(self.request.uri))
            greeting = ("You can login here: <a href=\"%s\">Login</a> <br>" %
                        (users.create_login_url(self.request.uri)))
            self.response.out.write("<html><body>%s</body></html>" % greeting)


app = webapp2.WSGIApplication([
                ('/', MainPage)
                ], debug=True)

def main():
    app.run()


if __name__ == "__main__":
    main()