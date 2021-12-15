\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{developercv}[2019/01/28 Developer CV class v1.0]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}}
\ProcessOptions\relax

\LoadClass{extarticle}

%----------------------n------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\setlength{\parindent}{0mm} 

\usepackage[hidelinks]{hyperref}

\pagestyle{empty} 

\usepackage{moresize} 

\usepackage{xcolor}

\definecolor{t4v_white}{HTML}{ECECEC}
\definecolor{t4v_purple}{HTML}{533BC8}
\definecolor{teal}{HTML}{008080}

%----------------------------------------------------------------------------------------
%	PAGE LAYOUT
%----------------------------------------------------------------------------------------

\usepackage{geometry}

\geometry{
	paper=a4paper,
	top=1.75cm,
	bottom=1.75cm,
	left=2cm,
	right=2cm,
	headheight=0.75cm,
	footskip=1cm,
	headsep=0.5cm, 
	%showframe,
}

%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

\usepackage[utf8]{inputenc} 
\usepackage[T1]{fontenc}

\usepackage[default]{raleway}
%\usepackage[defaultsans]{droidsans}
%\usepackage{cmbright}
%\usepackage{fetamont}
%\usepackage[default]{gillius}
%\usepackage{roboto}

\renewcommand*\familydefault{\sfdefault} 

%------------------------------------------------

\usepackage{fontawesome} 


\newcommand{\icon}[3]{
	\vcenteredhbox{\colorbox{teal}{\makebox(#2, #2){\textcolor{white}{\large\csname fa#1\endcsname}}}}
	\hspace{0.2cm}
	\vcenteredhbox{\textcolor{t4v_white}{#3}}
}

%----------------------------------------------------------------------------------------
%	GRAPHICS DEFINITIONS
%---------------------------------------------------------------------------------------- 

\usepackage{tikz} 
\usetikzlibrary{shapes, backgrounds}
\tikzset{x=1cm, y=1cm} 


\newcommand{\vcenteredhbox}[1]{
	\begingroup%
		\setbox0=\hbox{#1}\parbox{\wd0}{\box0}%
	\endgroup%
}

%----------------------------------------------------------------------------------------
%	CHARTS
%---------------------------------------------------------------------------------------- 

\newcounter{barcount}


\newenvironment{barchart}[1]{ 
	\newcommand{\barwidth}{0.35}
	\newcommand{\barsep}{0.2}
	

	\newcommand{\baritem}[2]{ 
		\pgfmathparse{##2}
		\let\perc\pgfmathresult
		
		\pgfmathparse{#1}
		\let\barsize\pgfmathresult
		
		\pgfmathparse{\barsize*##2/100}
		\let\barone\pgfmathresult
		
		\pgfmathparse{(\barwidth*\thebarcount)+(\barsep*\thebarcount)}
		\let\barx\pgfmathresult
		
		\filldraw[fill=teal, draw=none] (0,-\barx) rectangle (\barone,-\barx-\barwidth);
		
		\node [label=180:\colorbox{teal}{\textcolor{t4v_white}{##1}}] at (0,-\barx-0.175) {};
		\addtocounter{barcount}{1}
	}
	\begin{tikzpicture}
		\setcounter{barcount}{0}
}{
	\end{tikzpicture}
}

%------------------------------------------------

\newcounter{a}
\newcounter{b}
\newcounter{c}

\newcommand{\bubbles}[1]{
	
	\setcounter{a}{0}
	\setcounter{c}{150}
	
	\begin{tikzpicture}[scale=3]
		\foreach \p/\t in {#1} {
			\addtocounter{a}{1}
			\bubble{\thea/2}{\theb}{\p/25}{\t}{1\p0}
		}
	\end{tikzpicture}
}


\newcommand{\bubble}[5]{
	\filldraw[fill=black, draw=none] (#1,0.5) circle (#3); 
	\node[label=\textcolor{black}{#4}] at (#1,0.7) {};
}

%----------------------------------------------------------------------------------------
%	CUSTOM SECTIONS
%----------------------------------------------------------------------------------------


\newcommand{\cvsect}[1]{
	\vspace{\baselineskip} 
	\colorbox{teal}{\textcolor{t4v_white}{\MakeUppercase{\textbf{#1}}}}\\
}

%----------------------------------------------------------------------------------------
%	ENTRY LIST
%----------------------------------------------------------------------------------------

\usepackage{longtable} 
\setlength{\LTpre}{0pt} 
\setlength{\LTpost}{0pt} 

\setlength{\tabcolsep}{0pt} 


\newenvironment{entrylist}{
	\begin{longtable}[H]{l l}
}{
	\end{longtable}
}

\newcommand{\entry}[4]{
	\parbox[t]{0.175\textwidth}{
		#1 % Leftmost entry date(s) text
	}%
	&\parbox[t]{0.825\textwidth}{
		\textbf{#2}% Entry heading text
		\hfill% Horizontal whitespace
		{\footnotesize \textbf{\textcolor{t4v_white}{#3}}}\\% Right-aligned entry qualifier text
		#4 % Entry description text
	}\\\\}


\newcommand{\slashsep}{\hspace{3mm}/\hspace{3mm}}
