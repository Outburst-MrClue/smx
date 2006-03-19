%define name smx
%define ver 1.1.3
%define rel 1

Summary: 	Server Macro eXpansion Language
Name: 		%{name}
Version: 	%{ver}
Release: 	%{rel}
Source: 	%{name}-%{ver}.tar.gz
Vendor: 	Erik Aronesty <erik@smxlang.org>
Packager: 	Erik Aronesty <erik@smxlang.org>
URL: 		http://www.smxlang.org/
License: 	GPL
Group: 		Development/Languages
Prefix: 	%{_prefix}
BuildRoot: 	%{_tmppath}/%{name}-%{ver}-root
BuildPrereq:	unixODBC-devel >= 2.0
BuildPrereq:	httpd-devel >= 2.0
BuildPrereq:	openssl-devel >= 0.9
%if "%{enable_sqlite}" == "yes"
BuildPrereq:	sqlite-devel >= 3.0
%endif

%description
SMX is a simple macro language that can be used to parse text files
and replace inline macros. Contains the smx command-line and cgi 
tool, as well as the modsmx apache module.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Development/Libraries
Requires: %{name} = %{ver}

%description devel
The %{name}-devel package contains the header files and static libraries for
building applications which use %{name}.

%prep
%setup -q

%build
if [ -x ./configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir}
else
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%{_prefix} --mandir=%{_mandir}
fi
make

%install
rm -rf ${buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_prefix}/bin/smx
%{_prefix}/lib/lib*smx.*
%{_prefix}/share/man/man3/%*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_prefix}/lib/libsmx*.so.*

%changelog
* Mon Feb 27 2006 Erik Aronesty <erik@q32.com>
- First draft of the spec file

