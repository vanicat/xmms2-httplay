#!/usr/bin/env python
# Copyright 2012 Remi Vanicat
# Copyright 2009 Simon Poirier
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

import BaseHTTPServer
import service, reqs

def main():
    handler = service.Service
    httpd = BaseHTTPServer.HTTPServer(('', 8000), handler)
    reqs.cli.connect(lambda : httpd.shutdown())
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
