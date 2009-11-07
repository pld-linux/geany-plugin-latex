Summary:	Geany LaTeX plugin
Summary(pl.UTF-8):	wtyczka Geany dla LaTeXa
Name:		geany-plugin-latex
Version:	0.4
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://frank.uvena.de/files/geany/geanylatex-%{version}.tar.gz
# Source0-md5:	cbcb2022372683830932d2b4e271d790
URL:		http://frank.uvena.de/en/Geany/geanylatex/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	geany-devel >= 0.16
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	geany >= 0.16
Requires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Geany LaTeX is a little plugin to improve support of LaTeX on Geany.
It implements a couple of mayby useful functions:
    - Wizard to create new LaTeX documents in a fast and easy way with a
      bunch of templates available
    - A front end for add labels \label and references \ref and \pageref
      with getting suggestion from aux file of document
    - Inserting special characters through menu
    - Help entering the right fields for BibTeX entries by providing
      templates
    - Easy inserting format patterns like \texttt through menu
    - Support on inserting environments by offering an dialog and
      recognising selections
    - Shortcuts for inserting \item and \newline
    - Toolbar with often used format options

%description -l pl.UTF-8
Geany LaTeX jest małą wtyczką, która udostępnia wsparcie LaTeXa w
Geany. Implementuje wiele być może przydatnych funkcji:
    - czarodziej pozwala stworzyć nowy dokument LaTeXa szybko i w łatwy
      sposób, dzięki wielu dostępnym szablonom
    - interfejs użytkownika dodaje etykiety \label i referencje \ref oraz
      \pageref, dzięki sugestiom z pliku aux
    - wstawianie znaków specjalnych z menu
    - pomaga poprawnie wypełniać pola BibTeX dzięki szablonom
    - proste wstawianie formatowania, jak na przykład \texttt, przez menu
    - wsparcie środowiska przy pisaniu dzięki wyświetlaniu opcji wyboru
      oraz jego zatwierdzeniu
    - skróty dla wstawiania \item i \newline
    - pasek narzędzi z często używanymi opcjami formatowania

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -q -n geanylatex-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang geanylatex

%files -f geanylatex.lang
%defattr(644,root,root,755)
%{_libdir}/geany/*
%doc AUTHORS COPYING ChangeLog NEWS README
