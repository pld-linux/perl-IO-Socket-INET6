%include	/usr/lib/rpm/macros.perl
Summary:	IO::Socket::INET6 perl module
Summary(pl):	Modu³ perla IO::Socket::INET6
Name:		perl-IO-Socket-INET6
Version:	0.01a
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.pld.org.pl/people/agaran/IO-Socket-INET6-%{version}.tar.gz
# Source0-md5:	852c28f33fa678b029860219543bc6a1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Socket::INET6 - uses socket6.

%description -l pl
IO::Socket::INET6 - nazwa tlumaczy wszystko ;)

%prep
%setup -q -n IO-Socket-INET6

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/IO/Socket/INET6.pm
