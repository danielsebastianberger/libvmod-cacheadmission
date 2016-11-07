Summary: Cache Admission VMOD for Varnish
Name: vmod-cacheadmission
Version: 0.01
Release: 1%{?dist}
License: BSD two-clause
Group: System Environment/Daemons
Source0: libvmod-cacheadmission.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.0.2
BuildRequires: make
BuildRequires: python-docutils
BuildRequires: varnish >= 4.0.2
BuildRequires: varnish-libs-devel >= 4.0.2

%description
Cache Admission VMOD

%prep
%setup -n libvmod-cacheadmission-trunk

%build
%configure --prefix=/usr/
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check

%install
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mv %{buildroot}/usr/share/doc/lib%{name} %{buildroot}/usr/share/doc/%{name}


%clean
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Thu Nov 03 2016 Daniel S. Berger <berger@cs.uni-kl.de> - 0.01
- Initial version.
