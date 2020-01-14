#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcmdrMisc
Version  : 2.5.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/RcmdrMisc_2.5-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcmdrMisc_2.5-1.tar.gz
Summary  : R Commander Miscellaneous Functions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Hmisc
Requires: R-abind
Requires: R-car
Requires: R-colorspace
Requires: R-e1071
Requires: R-haven
Requires: R-nortest
Requires: R-readstata13
Requires: R-readxl
Requires: R-sandwich
BuildRequires : R-Hmisc
BuildRequires : R-abind
BuildRequires : R-car
BuildRequires : R-colorspace
BuildRequires : R-e1071
BuildRequires : R-haven
BuildRequires : R-nortest
BuildRequires : R-readstata13
BuildRequires : R-readxl
BuildRequires : R-sandwich
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
Various statistical, graphics, and data-management functions used by the Rcmdr package in the R Commander GUI for R.

%prep
%setup -q -c -n RcmdrMisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579029023

%install
export SOURCE_DATE_EPOCH=1579029023
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcmdrMisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcmdrMisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcmdrMisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RcmdrMisc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcmdrMisc/DESCRIPTION
/usr/lib64/R/library/RcmdrMisc/INDEX
/usr/lib64/R/library/RcmdrMisc/Meta/Rd.rds
/usr/lib64/R/library/RcmdrMisc/Meta/features.rds
/usr/lib64/R/library/RcmdrMisc/Meta/hsearch.rds
/usr/lib64/R/library/RcmdrMisc/Meta/links.rds
/usr/lib64/R/library/RcmdrMisc/Meta/nsInfo.rds
/usr/lib64/R/library/RcmdrMisc/Meta/package.rds
/usr/lib64/R/library/RcmdrMisc/NAMESPACE
/usr/lib64/R/library/RcmdrMisc/NEWS
/usr/lib64/R/library/RcmdrMisc/R/RcmdrMisc
/usr/lib64/R/library/RcmdrMisc/R/RcmdrMisc.rdb
/usr/lib64/R/library/RcmdrMisc/R/RcmdrMisc.rdx
/usr/lib64/R/library/RcmdrMisc/help/AnIndex
/usr/lib64/R/library/RcmdrMisc/help/RcmdrMisc.rdb
/usr/lib64/R/library/RcmdrMisc/help/RcmdrMisc.rdx
/usr/lib64/R/library/RcmdrMisc/help/aliases.rds
/usr/lib64/R/library/RcmdrMisc/help/paths.rds
/usr/lib64/R/library/RcmdrMisc/html/00Index.html
/usr/lib64/R/library/RcmdrMisc/html/R.css
