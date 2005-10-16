%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Socket-INET6
Summary:	IO::Socket::INET6 - Object interface for AF_INET|AF_INET6 domain sockets
Summary(pl):	Modu³ perla IO::Socket::INET6
Name:		perl-IO-Socket-INET6
Version:	2.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4ef8b7944fa036cda19dc3e1cc688a6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Socket::INET6 provides an object interface to creating and using
sockets in either AF_INET or AF_INET6 domains. It is built upon the
IO::Socket interface and inherits all the methods defined by
IO::Socket.

%description -l pl
IO::Socket::INET6 - nazwa t³umaczy wszystko ;)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/IO/Socket/INET6.pm
%{_mandir}/man3/*
