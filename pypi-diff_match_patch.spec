#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-diff_match_patch
Version  : 20200713
Release  : 30
URL      : https://files.pythonhosted.org/packages/f0/1e/48ba888757d3f63ff35536e3e73e05c8a20d701e2b4fcbe4b17c29a2408d/diff-match-patch-20200713.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/1e/48ba888757d3f63ff35536e3e73e05c8a20d701e2b4fcbe4b17c29a2408d/diff-match-patch-20200713.tar.gz
Summary  : Repackaging of Google's Diff Match and Patch libraries. Offers robust algorithms to perform the operations required for synchronizing plain text.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-diff_match_patch-license = %{version}-%{release}
Requires: pypi-diff_match_patch-python = %{version}-%{release}
Requires: pypi-diff_match_patch-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

%description
Google's [Diff Match and Patch][DMP] library, packaged for modern Python.

%package license
Summary: license components for the pypi-diff_match_patch package.
Group: Default

%description license
license components for the pypi-diff_match_patch package.


%package python
Summary: python components for the pypi-diff_match_patch package.
Group: Default
Requires: pypi-diff_match_patch-python3 = %{version}-%{release}

%description python
python components for the pypi-diff_match_patch package.


%package python3
Summary: python3 components for the pypi-diff_match_patch package.
Group: Default
Requires: python3-core
Provides: pypi(diff_match_patch)

%description python3
python3 components for the pypi-diff_match_patch package.


%prep
%setup -q -n diff-match-patch-20200713
cd %{_builddir}/diff-match-patch-20200713
pushd ..
cp -a diff-match-patch-20200713 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408065
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-diff_match_patch
cp %{_builddir}/diff-match-patch-20200713/LICENSE %{buildroot}/usr/share/package-licenses/pypi-diff_match_patch/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-diff_match_patch/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
