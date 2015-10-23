Summary: Utilities for managing filesystem extended attributes
Name: attr
Version: 2.4.44
Release: %{?release_prefix:%{release_prefix}.}7.11.%{?dist}%{!?dist:tizen}
VCS:     framework/base/attr#Z910F_PROTEX_0625-2-gf85ff3a6295796e796f7a57e540601bd2ca3bd86
Source: http://download.savannah.gnu.org/releases/attr/attr-%{version}.src.tar.gz
Source1001: attr.manifest
Patch0: 01-578386-Makefile.patch
Patch1: 02-fix_memory_leak_in_attr_copy_action.patch
Patch2: 03-pull_in_string.h.patch
Patch3: 05-eliminate_a_memory_leak.patch
Patch4: 06-eliminate_a_double_free.patch
Patch5: 07-fix_thinko_in_restore.patch
Patch6: attr-2.4.44-build.patch
Patch7: 08-getfattr_encode_NULs_properly_with_--encoding=text.patch

License: GPLv2+
URL: http://savannah.nongnu.org/projects/attr/
Group: System/Base
BuildRequires: autoconf
BuildRequires: libtool >= 1.5
BuildRequires: gettext-tools

%description
This package contains the libattr.so dynamic library which contains
the extended attribute system calls and library functions.

%package -n libattr
Summary: Utilities for managing filesystem extended attributes
Group: System/Libraries
License: LGPLv2+

%description -n libattr
Utilities for managing filesystem extended attributes

%package -n libattr-devel
Summary: Extended attribute static libraries and headers
Group: Development/Libraries
License: LGPLv2+
Requires: libattr = %{version}-%{release}

%description -n libattr-devel
This package contains the libraries and header files needed to
develop programs which make use of extended attributes.
For Linux programs, the documented system call API is the
recommended interface, but an SGI IRIX compatibility interface
is also provided.

Currently only ext2, ext3 and XFS support extended attributes.
The SGI IRIX compatibility API built above the Linux system calls is
used by programs such as xfsdump(8), xfsrestore(8) and xfs_fsr(8).

You should install libattr-devel if you want to develop programs
which make use of extended attributes.  If you install libattr-devel,
you'll also want to install attr.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cp %{SOURCE1001} .
#export DIST_ROOT=%{buildroot}
export INSTALL_USER="root"
export INSTALL_GROUP="root"
%configure \
 	--prefix=/ \
 	--exec-prefix=/ \
 	--sbindir=/bin \
 	--bindir=/usr/bin \
 	--libdir=/%{_lib} \
 	--libexecdir=/%{_libdir}
make configure
make default %{?_smp_mflags}
rm -f po/attr.pot
make -C po attr.pot

%install
rm -rf $RPM_BUILD_ROOT

DIST_ROOT=%{buildroot}; export DIST_ROOT; make -C . install
DIST_ROOT=%{buildroot}; export DIST_ROOT; make -C . install-dev
DIST_ROOT=%{buildroot}; export DIST_ROOT; make -C . install-lib

chmod +x %{buildroot}/%{_lib}/libattr.so.*
rm -f %{buildroot}/%{_lib}/libattr.{la,a}
rm -f %{buildroot}%{_libdir}/libattr.{la,a}

mkdir -p %{buildroot}/%{_datadir}/license
cp -f COPYING.GPLv2 %{buildroot}/%{_datadir}/license/%{name}
cp -f COPYING.LGPLv2.1 %{buildroot}/%{_datadir}/license/lib%{name}

%remove_docs

%post -n libattr -p /sbin/ldconfig

%postun -n libattr -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%manifest attr.manifest
%{_bindir}/*
%{_prefix}/share/locale/*/LC_MESSAGES/attr.mo
%{_datadir}/license/%{name}

%files -n libattr
%defattr(-,root,root,-)
/%{_lib}/libattr.so.*
%{_datadir}/license/lib%{name}

%files -n libattr-devel
%defattr(-,root,root,-)
/%{_lib}/libattr.so
%{_libdir}/libattr.so
%{_includedir}/attr/*.h

%changelog
* Sat Jun 28 2014 SLP SCM <slpsystem.m@samsung.com> - None 
- PROJECT: framework/base/attr
- COMMIT_ID: f85ff3a6295796e796f7a57e540601bd2ca3bd86
- BRANCH: master
- PATCHSET_REVISION: f85ff3a6295796e796f7a57e540601bd2ca3bd86
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/534362
- PATCHSET_REVISION: f85ff3a6295796e796f7a57e540601bd2ca3bd86
- TAGGER: SLP SCM <slpsystem.m@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code-Review : 2
- Newton Lee <newton.lee@samsung.com> Verified : 1
- CHANGE_SUBJECT: Merged x86_64 support to master
- Merged x86_64 support to master
* Sat Feb 22 2014 Seongho Jeong <sh33.jeong@samsung.com> - None 
- PROJECT: framework/base/attr
- COMMIT_ID: 13d9d50e83d4d20dae9547f19f7bf3b1c86b3513
- PATCHSET_REVISION: 13d9d50e83d4d20dae9547f19f7bf3b1c86b3513
- CHANGE_OWNER: \"Seongho Jeong\" <sh33.jeong@samsung.com>
- PATCHSET_UPLOADER: \"Seongho Jeong\" <sh33.jeong@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/428510
- PATCHSET_REVISION: 13d9d50e83d4d20dae9547f19f7bf3b1c86b3513
- TAGGER: Seongho Jeong <sh33.jeong@samsung.com>
- Gerrit patchset approval info:
- Newton Lee <newton.lee@samsung.com> Code-Review : 2
- Seongho Jeong <sh33.jeong@samsung.com> Verified : 1
- CHANGE_SUBJECT: Add correct license document
- Add correct license document
* Mon Dec  9 2013 Yang YongHyun <alex.yang@samsung.com> - None 
- PROJECT: framework/base/attr
- COMMIT_ID: de5388ef886248d249cd3d489a61b36dfbee2029
- PATCHSET_REVISION: de5388ef886248d249cd3d489a61b36dfbee2029
- CHANGE_OWNER: \"Yang YongHyun\" <alex.yang@samsung.com>
- PATCHSET_UPLOADER: \"Yang YongHyun\" <alex.yang@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/362406
- PATCHSET_REVISION: de5388ef886248d249cd3d489a61b36dfbee2029
- TAGGER: Yang YongHyun <alex.yang@samsung.com>
- Gerrit patchset approval info:
- Jinwoo Nam <jwoo.nam@samsung.com> Code Review : 2
- Kidong Kim <kd0228.kim@samsung.com> Code Review : 1
- Kidong Kim <kd0228.kim@samsung.com> Verified : 1
- CHANGE_SUBJECT: Merge branch 'devel/arch/master'
- Merge branch 'devel/arch/master'
* Fri Nov 29 2013 Jinwoo nam <jwoo.nam@samsung.com> - None 
- PROJECT: framework/base/attr
- COMMIT_ID: 72250257133c201fc77fcca39c552900f4cf75aa
- PATCHSET_REVISION: 72250257133c201fc77fcca39c552900f4cf75aa
- CHANGE_OWNER: \"Jinwoo Nam\" <jwoo.nam@samsung.com>
- PATCHSET_UPLOADER: \"Jinwoo Nam\" <jwoo.nam@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/351680
- PATCHSET_REVISION: 72250257133c201fc77fcca39c552900f4cf75aa
- TAGGER: Jinwoo nam <jwoo.nam@samsung.com>
- Gerrit patchset approval info:
- Kidong Kim <kd0228.kim@samsung.com> Code Review : 2
- Kidong Kim <kd0228.kim@samsung.com> Verified : 1
- CHANGE_SUBJECT: Merge branch 'devel/arch/master' add Smack manifest
- Merge branch 'devel/arch/master' add Smack manifest
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121022.040552 
- PROJECT: framework/base/attr
- COMMIT_ID: 35dd84ba1b1f0701fe76589585894a569c308171
- PATCHSET_REVISION: 35dd84ba1b1f0701fe76589585894a569c308171
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103767
- PATCHSET_REVISION: 35dd84ba1b1f0701fe76589585894a569c308171
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Git OBS Sync
- [Version] 2.4.44
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
