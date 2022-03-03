# Python and CGI

## Additional Notes

- static pages are making a comeback for thigns like blogs and documentation
  - use templating to generate; was that a thing back then?

## Terminology

- cgi
- cgi application

## Outline

- introduce to web 1.0
  - nothing was dynamic, everything had to be loaded from the server
  - "trip down memory lane" to a simplier time... when [big event], [big event], [small event]
  - google maps which was the first AJAX website I interacted with; before we had [company]

- easter egg
  - [marquee tag on google](https://www.google.com/search?q=marquee+tag)
    - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee
  - [blink tag](https://www.google.com/search?q=blink+tag)
  - midi ...?
  - geocities asthetic

- CGI
  - https://en.wikipedia.org/wiki/Common_Gateway_Interface
  - if you wanted to have a dynamic webpage, you had no choice but to use CGI
  - dive into what CGI is and how it's used
  - http://savage.net.au/Ron/html/cgi-scripting.html
    - 2 types of CGI scripts...
      - those which output HTML pages
        - counter
      - those which process input from forms
        - save information from a website into database and load all data from database
        - guestbook
  - if we want to start combining our dynamic website, our backend is gonna start getting complicated
  - fortunately our web developer ancestors from the early days of the internet foresaw this problem and found a solution

- server side inclues
  - what is it? and how to use it
  - https://en.wikipedia.org/wiki/Server_Side_Includes
  - https://www.whoishostingthis.com/resources/ssi/
  - Server Side Includes are an “old-fashioned” way to write dynamic web pages. It is generally recognized as a templating system instead of a full featured language.
    - https://uwsgi-docs.readthedocs.io/en/latest/SSI.html
  - https://github.com/danvk/ssi-server
    - if talk gets accepted, make this into a pip installable library that we can upload to PyPI
    - ask creator if it is okay
    - say "built on top of http.server"

- styling app
  - get jonathan to design something very 90s geocities

- deploying
  - so right now we're using http.server for local development, but this is not fit for production
  - talk about how to deploy using nginx
  - deploy to Ec2 with terraform and have it up for presentation
  - if time: docker and kubernets
  - [Python CGI on nginx](https://techexpert.tips/nginx/python-cgi-nginx/)
  - [SSI on nginx](http://nginx.org/en/docs/http/ngx_http_ssi_module.html)

- scaling
  - right now using CGI which has these problems
  - there is a fix, fastcgi which has been around since the 90s
  - leave this as an exercise to the reader
  - [What is CGI, FastCGI?](https://help.superhosting.bg/en/cgi-common-gateway-interface-fastcgi.html)
  - [python library -- fastcgi](https://github.com/fastai/fastcgi/tree/master/)
  - [nginx -- fastcgi](https://www.nginx.com/resources/wiki/start/topics/examples/fastcgiexample/)

## To Read

- https://docs.python.org/3/library/http.server.html
- https://docs.python.org/3/library/http.server.html#http.server.CGIHTTPRequestHandler
- [Introduction to CGI Programming](http://homepages.math.uic.edu/~jan/mcs275/mcs275notes/lec21.html)
- https://docs.python.org/3/library/cgi.html

## Additional Resources

- [Simple POST webserver](https://gist.github.com/MFry/90382082f9a65eceabd007ee7182af92)
  -- example of how to set up handlers for the server
- [4.4. CGI - Dynamic Web Pages](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/dynamic.html)
  -- lots of Python CGI examples

## Hello World

From [StackOverflow](https://stackoverflow.com/questions/30516414/how-to-run-cgi-hello-world-with-python-http-server):

```bash
# create hello.py
# update permissions
chmod -x cgi-bin/hello.py

# start server
python3 -m http.server --bind localhost --cgi 8000

# go to http://0.0.0.0:8000/cgi-bin/hello.py
```
