Summary:	GTK+ Sudoku Game
Name:		sudoku-savant
Version:	1.3
Release:	1
License:	GPLv3
Group:		Games/Other
Url:		http://sourceforge.net/projects/sudoku-savant/
Source0:	http://downloads.sourceforge.net/project/sudoku-savant/sudoku-savant/sudoku-savant-1.3/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(gtk+-2.0)

%description
A simple GUI-driven application to solve and generate sudoku puzzles through 
logical means. Also supports manual solving, with pencil marks and cell 
colouring. Should be able to solve any standard sudoku from a newspaper or 
magazine.

%prep
%setup -q

%build
%configure2_5x

%make

%install
mkdir -p %{buildroot}%{_datadir}/pixmaps
%makeinstall

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png



%changelog
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.3-1
+ Revision: 800442
- imported package sudoku-savant

