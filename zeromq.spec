Name:           zeromq
Version:        2.0.7
Release:        4%{?dist}
Summary:        Software library for fast, message-based applications

Group:          System Environment/Libraries
License:        LGPLv3+
URL:            http://www.zeromq.org
# VCS:          git:http://github.com/zeromq/zeromq2.git
Source0:        http://www.zeromq.org/local--files/area:download/zeromq-%{version}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  libuuid-devel


%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for 
developing applications that use %{name}.


%package utils
Summary:        Utility files for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}


%description utils
This package contains ZeroMQ related utility files,
e.g. zmq_forwarder, zmq_streamer and zmq_queue.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

# remove *.la
rm %{buildroot}%{_libdir}/libzmq.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS README
%{_libdir}/libzmq.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq.*
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*


%files utils
%defattr(-,root,root,-)
%{_bindir}/zmq_forwarder
%{_bindir}/zmq_queue
%{_bindir}/zmq_streamer
%{_mandir}/man1/zmq*


%changelog
* Fri Jul 23 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-4
- upstream VCS changed
- remove buildroot / %%clean
- change descriptions

* Tue Jul 20 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-3
- move binaries to seperate utils package

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-2
- remove BR: libstdc++-devel
- move man3 to the devel package
- change group to System Environment/Libraries

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.7-1
- initial package (based on upstreams example one)
