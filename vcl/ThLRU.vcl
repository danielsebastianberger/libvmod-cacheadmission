vcl 4.0;
import std;

# Default backend definition. Set this to point to your content server.
backend default {
    .host = "127.0.0.1";
    .port = "8000";
}

sub vcl_backend_response {
  if (std.integer(beresp.http.Content-Length, 0) > 65536) {
     set beresp.uncacheable = true;
     return (deliver);
  }
}
