# libvmod-cacheadmission

A Varnish VMOD for cache admission policies that shield Varnish from many unpopular (large) objects (aka. one-hit-wonders). This improves the cache hit ratio as these unpopular objects, if allowed into the cache, would push out more popular objects -- while not yielding any hits.

Early development stage.
