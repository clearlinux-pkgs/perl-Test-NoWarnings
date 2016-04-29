#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-NoWarnings
Version  : 1.04
Release  : 7
URL      : http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-NoWarnings-1.04.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-NoWarnings-1.04.tar.gz
Summary  : "Make sure you didn't emit any warnings while testing"
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Test-NoWarnings-doc

%description
NAME
Test::NoWarnings - Make sure you didn't emit any warnings while testing
SYNOPSIS
For scripts that have no plan

%package doc
Summary: doc components for the perl-Test-NoWarnings package.
Group: Documentation

%description doc
doc components for the perl-Test-NoWarnings package.


%prep
%setup -q -n Test-NoWarnings-1.04

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Test/NoWarnings.pm
/usr/lib/perl5/site_perl/5.22.0/Test/NoWarnings/Warning.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
