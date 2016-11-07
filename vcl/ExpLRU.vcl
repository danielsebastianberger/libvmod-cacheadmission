vcl 4.0;
import std;

C{
	#include <stdlib.h>
	#include <math.h>
}C

# Default backend definition. Set this to point to your content server.
backend default {
    .host = "127.0.0.1";
    .port = "8000";
}


sub vcl_backend_response {
    C{
	const struct gethdr_s hdr = { HDR_BERESP, "\017Content-Length:" };
	const int clen = atoi(VRT_GetHdr(ctx, &hdr));
	const double admissionprob = exp(-clen/ 32768);
	const double urand = drand48();
	// if admission test suceeds, mark as uncacheable (set ttl=0, so do not create hit-for-pass)
	if(admissionprob < urand) {
	   VRT_l_beresp_ttl(ctx,0);
	   VRT_l_beresp_uncacheable(ctx,1);
	}
    }C
    return (deliver);
}
