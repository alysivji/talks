ssi-server
==========

Server Side Includes in Python's SimpleHTTPServer

Use this in the same way as Python's SimpleHTTPServer:

    ./ssi_server.py [port]

The only difference is that, for files ending in '.html', ssi_server will
inline SSI (Server Side Includes) of the form:

    <!-- #include virtual="fragment.html" -->

Quick start:

    git clone https://github.com/danvk/ssi-server.git
    cd ssi-server
    ./ssi_server
    (visit localhost:8000) in your browser.
