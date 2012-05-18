Summary: php library
Name: phplib
Version: 1.0
Release: 7
License: GNU Library or Lesser General Public License (LGPL)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root
Group: System Environment/Daemons
Source: %{name}-%{version}.tar.gz
Packager: David Beveridge <david@beveridge.id.au>

%description
A library that provides session managent, authentication, permission
control, tables, forms, form elements, templating and sql query builder.
Compatible with a wide range of databases including MySQL, ODBC, Oracle,
Postgres, MSSQL etc.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/phplib/local
mkdir -p $RPM_BUILD_ROOT/usr/share/phplib/examples
install -m 750 setup $RPM_BUILD_ROOT/usr/share/phplib/
install -m 644 setup.py $RPM_BUILD_ROOT/usr/share/phplib/
install -m 644 README $RPM_BUILD_ROOT/usr/share/phplib/
install -m 644 inc/* $RPM_BUILD_ROOT/usr/share/phplib/
install -m 644 examples/* $RPM_BUILD_ROOT/usr/share/phplib/examples/
mv local $RPM_BUILD_ROOT/usr/share/phplib/
#mv fckeditor $RPM_BUILD_ROOT/usr/share/phplib/
#mv ckeditor $RPM_BUILD_ROOT/usr/share/phplib/
#mv ckfinder $RPM_BUILD_ROOT/usr/share/phplib/

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/phplib/*

%changelog
* Fri May 18 2012 dave
- version 0.7
- Added BACB changes

* Mon Jun 28 2010 dave
- version 0.6
- Changed to work with register_globals = off and E_NOTICE on.
- allow switching of editors by _ENV variable
- showChildRecords() added to tpl_form.inc
- next_row() added to db_mysql.inc
- select() added to table.inc allowing OUTER JOINs to other sql tables in query results
- changed add_extra to use images for function links

* Wed Feb 6 2010 dave
- version 0.5
- versatile date input format using ajax_update_field function
- error handler that writes php error and backtrace to EventLog
- menu page function that creates place holder pages for menus
- edit function for help text on menu placeholder pages.
- Python Setup to create virtual web host configurations etc
- included CKeditor/CKfinder as alternative for FCKeditor

* Sat Jan 16 2010 David Beveridge <david@beveridge.id.au>
- version 0.4
- find_values moved from local.inc to tpl_form.inc
- image blobs can be stored in sql db instead of on disk
- new autogen with cPanel support
- new MenuEditor
- easier permission control integrated into menus
- have_perm function now available in session class.

* Fri Jun 26 2009 David Beveridge <david@beveridge.id.au>
- Added /js /css to local folder

* Fri Jun 12 2009 David Beveridge <david@beveridge.id.au>
- Added phplib.sql

* Mon Jun 01 2009 David Beveridge <david@beveridge.id.au>
- initial build

