Name:           mydumpadmin
Version:        1
Release:        0
Summary:        An Advance Bash Script for MySQL Database Backup

Group:          TecAdmin
BuildArch:      noarch
License:        GPL
URL:            https://github.com/AshutoshJha786/mydumpadmin-1.git 
Source0:        mydumpadmin-1.0.tar.gz

%description
Write some description about your package here

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/mydumpadmin
install -m 0600 credentials.txt $RPM_BUILD_ROOT/etc/mydumpadmin/credentials.txt
install -m 0755 mysql-dump.sh $RPM_BUILD_ROOT/etc/mydumpadmin/mysql-dump.sh
install -m 0644 README.md $RPM_BUILD_ROOT/etc/mydumpadmin/README.md
install -m 0644 settings.conf $RPM_BUILD_ROOT/etc/mydumpadmin/settings.conf

%files
/etc/mydumpadmin
/etc/mydumpadmin/credentials.txt
/etc/mydumpadmin/mysql-dump.sh
/etc/mydumpadmin/README.md
/etc/mydumpadmin/settings.conf

%changelog
* Tue Oct 06 2020 Ashutosh Jha 1.0.0
  - Initial rpm release
