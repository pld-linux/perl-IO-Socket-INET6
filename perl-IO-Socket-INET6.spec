%include	/usr/lib/rpm/macros.perl
Summary:	IO-Socket-INET6 perl module
Summary(pl):	Modu³ perla IO-Socket-INET6
Name:		perl-IO-Socket-INET6
Version:	0.01a
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.pld.org.pl/people/agaran/IO-Socket-INET6-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Socket-INET6 - uses socket6.

%description -l pl
IO-Socket-INET6 - nazwa tlumaczy wszystko ;)

%prep
%setup -q -n IO-Socket-INET6-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/IO/Socket/INET6.pm
