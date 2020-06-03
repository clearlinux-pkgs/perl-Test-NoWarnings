#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-NoWarnings
Version  : 1.04
Release  : 33
URL      : http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-NoWarnings-1.04.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-NoWarnings-1.04.tar.gz
Summary  : "Make sure you didn't emit any warnings while testing"
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Test-NoWarnings-license = %{version}-%{release}
Requires: perl-Test-NoWarnings-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::NoWarnings - Make sure you didn't emit any warnings while testing
SYNOPSIS
For scripts that have no plan

%package dev
Summary: dev components for the perl-Test-NoWarnings package.
Group: Development
Provides: perl-Test-NoWarnings-devel = %{version}-%{release}
Requires: perl-Test-NoWarnings = %{version}-%{release}

%description dev
dev components for the perl-Test-NoWarnings package.


%package license
Summary: license components for the perl-Test-NoWarnings package.
Group: Default

%description license
license components for the perl-Test-NoWarnings package.


%package perl
Summary: perl components for the perl-Test-NoWarnings package.
Group: Default
Requires: perl-Test-NoWarnings = %{version}-%{release}

%description perl
perl components for the perl-Test-NoWarnings package.


%prep
%setup -q -n Test-NoWarnings-1.04
cd %{_builddir}/Test-NoWarnings-1.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-NoWarnings
cp %{_builddir}/Test-NoWarnings-1.04/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-NoWarnings/cf756914ec51f52f9c121be247bfda232dc6afd2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::NoWarnings.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-NoWarnings/cf756914ec51f52f9c121be247bfda232dc6afd2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Test/NoWarnings.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/NoWarnings/Warning.pm
