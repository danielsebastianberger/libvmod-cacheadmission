# libvmod-cacheadmission

## description

Cache admission policies for memory web cache based on Varnish. These policies seek to prevent admitting objects that are large but unpopular (aka. "one-hit-wonders"), and thus would not contribute to the hit ratio.

The most simple cache admission policy are a) admitting after N requests, and b) admitting an object if its size is below a threshold. Unfortunately, a) has significant overhead (counting the number of requests per object), and b) only helps for outliers (really large objects).

These policies can be combined by using an admission probability that is decreasing with the object size. For example, small objects are admitted (in expectation) after two requests, and large objects after 100 requests. A natural probability function is the class of exponential functions (with parameter c):

    admission_probability(size) = exp(-size/c)

This repo implements such an admission probability for Varnish, either as implemented in VCL with inline c, or as a VMOD (currently the VMOD is outdated and incomplete).

## VCL

Checkout ExpLRU.vcl from the "vcl" folder. Set your backend, and start varnish with

    varnishd ... -f ExpLRU.vcl -n -p vcc_allow_inline_c=on ...

The default parameter is c=32KB. Feel free to experiment.

## VMOD

See folder "vmod".

If you installed varnish to "/usr/local/varnish/" (like me), you first have to point to this path with:

    export PKG_CONFIG_PATH=/usr/local/varnish/lib/pkgconfig

Then (assuming the same path):

    ./autogen.sh --prefix=/usr/local/varnish/
    ./configure
    make
    make install
