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
import json
from google.appengine.api import urlfetch

imgflip_url = 'https://api.imgflip.com/get_memes'

class MainPage(webapp2.RequestHandler):
    def get(self):
        try:
            result = urlfetch.fetch(imgflip_url)
            json_result = json.loads(result.content)
            for meme in json_result.get('data').get('memes'):
                url = meme.get('url')
                caption = meme.get('name')
                if result.status_code == 200:
                    self.response.write("<img style='width: 250px' src='{img_url}'/>{caption}".format(
                        img_url=url, caption=caption))
                else:
                    self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
            # self.response.headers['Content-Type'] = 'text/html'


app = webapp2.WSGIApplication([
('/', MainPage)
], debug=True)
