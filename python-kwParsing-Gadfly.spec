Summary: Parser generator
Name: python-kwParsing
Version: 1.0
Release: 1
Copyright: distributable
Packager: John Eikenberry (jae@dsinw.com)
Group: Development/Languages/Python
Source0: kwP.tar.gz
Source1: Gadfly.pth
Source2: kwParsing.pth
Source3: sqlwhere.py
Icon: linux-python-small.gif 
BuildRoot:	/tmp/%{name}-%{version}-root
Requires: python >= 1.5
Provides: python-kwParsing
BuildArchitectures: noarch

%changelog

%description
kwParser is a parser generator for Python. It transforms an abstract
specification of a language grammar (for example the CORBA Interface
Definition Language) together with "interpretation functions" that define
the semantics of the language into a compiler or translator or interpreter.
In the case of CORBA IDL a python program using kwParser could generate
stubs and support code (in Python or some other language) to talk to a CORBA
interface.

%package -n python-Gadfly
Summary: Python SQL Database Engine
Group: Development/Languages/Python
Icon: linux-python2-small.gif
Requires: python, python-kwParsing
BuildArchitectures: noarch

%description -n python-Gadfly
These are the core files to the Gadfly SQL database engine (beta). A
relational database query engine that supports the Structured Query
Language (SQL), implemented entirely in Python (with optional builtin
support from the kjbuckets builtin data structure accelerator). 

%prep
%setup -n kwP -c 
cp $RPM_SOURCE_DIR/kwParsing.pth ./
cp $RPM_SOURCE_DIR/Gadfly.pth ./

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly

install -m644 DLispShort.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 DumbLispGen.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 idl.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 pygram.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 kjpylint.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 kjParseBuild.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 kjParser.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install -m644 kjSet.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing

install -m644 gadfly.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gfserve.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gfclient.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gfsocket.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gfstest.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gfinstall.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gftest.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sqlbind.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sqlgen.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sqlgram.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sqlgtest.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sqlsem.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sqlmod.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 gfdb0.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 relalg.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 kjbuckets0.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install -m644 sql.mar $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly

cp $RPM_SOURCE_DIR/kwParsing.pth $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages
cp $RPM_SOURCE_DIR/Gadfly.pth $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages
cp $RPM_SOURCE_DIR/sqlwhere.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly

%postun
rm -rf %{_libdir}/python1.5/site-packages/kwParsing

%postun -n python-Gadfly
rm -rf %{_libdir}/python1.5/site-packages/Gadfly

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYRIGHT kwParsing.html server.html
%{_libdir}/python1.5/site-packages/kwParsing
%{_libdir}/python1.5/site-packages/kwParsing.pth

%files -n python-Gadfly
%doc gadfly.html gfSQL.html gfrecover.html index.html gffaq.html gadfly.JPG
%{_libdir}/python1.5/site-packages/Gadfly
%{_libdir}/python1.5/site-packages/Gadfly.pth
