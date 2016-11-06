# libvmod-cacheadmission

## description

A Varnish VMOD for cache admission policies that shield Varnish from many unpopular (large) objects (aka. one-hit-wonders). This improves the cache hit ratio as these unpopular objects, if allowed into the cache, would push out more popular objects -- while not yielding any hits.

Early development stage.


## install

If you installed varnish to "/usr/local/varnish/" (like me), you first have to point to this path with:

    export PKG_CONFIG_PATH=/usr/local/varnish/lib/pkgconfig

Then (assuming the same path):

    ./autogen.sh --prefix=/usr/local/varnish/
    ./configure
    make
    make install