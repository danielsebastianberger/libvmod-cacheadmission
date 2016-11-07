AM_CPPFLAGS = @VMOD_INCLUDES@ -Wall -Werror

vmoddir = @VMOD_DIR@
vmod_LTLIBRARIES = libvmod_cacheadmission.la

libvmod_cacheadmission_la_LDFLAGS = -module -export-dynamic -avoid-version -shared

libvmod_cacheadmission_la_SOURCES = \
	vmod_cacheadmission.c

nodist_libvmod_cacheadmission_la_SOURCES = \
	vcc_if.c \
	vcc_if.h

vmod_cacheadmission.lo: vcc_if.c vcc_if.h

vcc_if.c: vcc_if.h

vcc_if.h: @VMODTOOL@ $(top_srcdir)/src/vmod_cacheadmission.vcc
	@VMODTOOL@ $(top_srcdir)/src/vmod_cacheadmission.vcc

VMOD_TESTS = $(top_srcdir)/src/tests/*.vtc
.PHONY: $(VMOD_TESTS)

$(top_srcdir)/src/tests/*.vtc: libvmod_cacheadmission.la
	@VARNISHTEST@ -Dvarnishd=@VARNISHD@ -Dvmod_topbuild=$(abs_top_builddir) $@

check: $(VMOD_TESTS)

EXTRA_DIST = \
	vmod_cacheadmission.vcc \
	$(VMOD_TESTS)

CLEANFILES = \
	$(builddir)/vcc_if.c \
	$(builddir)/vcc_if.h \
	$(builddir)/vmod_cacheadmission.rst \
	$(builddir)/vmod_cacheadmission.man.rst
