# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Write new code that responds to different url paths
# Write code to take in query parameters and use them
#    i.e.  youtube.com/?v=blahblah

import webapp2

# dict = {'cat':'',
# 'dog':'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13001000/Beagle-On-White-01-400x267.jpg',
# }
class MainPage(webapp2.RequestHandler):
    def get(self):
        # Change this to do some fizzbuzzing
        num = self.request.get('number')
        txt = self._fizzbuzz(int(num))
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<html><body><h1>Result: {txt}</h1></body></html>".format(
            txt=txt))

    def _fizzbuzz(self, num):
        txt = ""
        if num % 3 == 0:
            txt += "fizz"
        if num % 5 == 0:
            txt += "buzz"
        return txt

app = webapp2.WSGIApplication([
('/main', MainPage)
], debug=True)

