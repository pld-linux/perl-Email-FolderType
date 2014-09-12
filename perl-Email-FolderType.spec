#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	FolderType
Summary:	Email::FolderType - return type of a mail folder
Summary(pl.UTF-8):	Email::FolderType - sprawdzenie rodzaju folderu pocztowego
Name:		perl-Email-FolderType
Version:	0.813
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d33367e38ec1548737c15ccd200f18c
URL:		http://search.cpan.org/dist/Email-FolderType/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.47
BuildRequires:	perl-Module-Pluggable
%endif
Conflicts:	perl-Email-FolderType-Net <= 0:1.02
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a utility module for detecting the type of a given mail box.

%description -l pl.UTF-8
Jest to moduł narzędziowy do wykrywania rodzaju podanej skrzynki
pocztowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
