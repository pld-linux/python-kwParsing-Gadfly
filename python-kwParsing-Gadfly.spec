Summary:	Parser generator
Summary(pl):	Generator parser�w
Name:		python-kwParsing
Version:	1.0
Release:	1
License:	distributable
Group:		Development/Languages/Python
Source0:	http://www.chordate.com/kwParsing/kwP.tar.gz
Source1:	Gadfly.pth
Source2:	kwParsing.pth
Source3:	sqlwhere.py
URL:		http://www.chordate.com/kwParsing/
Icon:		linux-python-small.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python >= 1.5
BuildArch:	noarch

%description
kwParser is a parser generator for Python. It transforms an abstract
specification of a language grammar (for example the CORBA Interface
Definition Language) together with "interpretation functions" that
define the semantics of the language into a compiler or translator or
interpreter. In the case of CORBA IDL a python program using kwParser
could generate stubs and support code (in Python or some other
language) to talk to a CORBA interface.

%description -l pl
kwParser to generator parser�w dla Pythona. Przerabia abstrakcyjn�
specyfikacj� gramatyki j�zyka (np. w CORBA Interface Definition
Language) wraz z "funkcjami interpretacji" definiuj�cymi semantyk�
j�zyka na kompilator, translator lub interpreter. W przypadku CORBA
IDL program w Pythonie u�ywaj�cy modu�u kwParser mo�e generowa� kod
wspieraj�cy (w Pythonie lub innym j�zyku) do porozumiewania z
interfejsem CORBA.

%package -n python-Gadfly
Summary:	Python SQL Database Engine
Summary(pl):	Silnik baz danych SQL w Pythonie
Group:		Development/Languages/Python
Icon:		linux-python2-small.gif
Requires:	python
Requires:	python-kwParsing
BuildArch:	noarch

%description -n python-Gadfly
These are the core files to the Gadfly SQL database engine (beta). A
relational database query engine that supports the Structured Query
Language (SQL), implemented entirely in Python (with optional builtin
support from the kjbuckets builtin data structure accelerator).

%description -n python-Gadfly -l pl
To podstawowe pliki silnika bazodanowego SQL o nazwie Gadfly. Jest to
silnik relacyjnych baz danych obs�uguj�cy SQL, zaimplementowany
ca�kowicie w Pythonie (z opcjonalnie wbudowan� obs�ug� kjbuckets).

%prep
%setup -q -n kwP -c
cp -f %{SOURCE2} .
cp -f %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/{kwParsing,Gadfly}

install DLispShort.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install DumbLispGen.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install idl.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install pygram.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install kjpylint.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install kjParseBuild.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install kjParser.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing
install kjSet.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/kwParsing

install gadfly.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gfserve.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gfclient.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gfsocket.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gfstest.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gfinstall.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gftest.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sqlbind.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sqlgen.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sqlgram.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sqlgtest.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sqlsem.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sqlmod.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install gfdb0.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install relalg.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install kjbuckets0.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly
install sql.mar $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly

install %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages
install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages
install %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Gadfly

%clean
rm -rf $RPM_BUILD_ROOT

%postun
rm -rf %{_libdir}/python1.5/site-packages/kwParsing

%postun -n python-Gadfly
rm -rf %{_libdir}/python1.5/site-packages/Gadfly

%files
%defattr(644,root,root,755)
%doc COPYRIGHT kwParsing.html server.html
%{_libdir}/python1.5/site-packages/kwParsing
%{_libdir}/python1.5/site-packages/kwParsing.pth

%files -n python-Gadfly
%defattr(644,root,root,755)
%doc gadfly.html gfSQL.html gfrecover.html index.html gffaq.html gadfly.JPG
%{_libdir}/python1.5/site-packages/Gadfly
%{_libdir}/python1.5/site-packages/Gadfly.pth
