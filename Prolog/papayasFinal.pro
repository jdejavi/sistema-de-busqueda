/*****************************************************************************

		Copyright (c) My Company

 Project:  PAPAYASFINAL
 FileName: PAPAYASFINAL.PRO
 Purpose: No description
 Written by: Visual Prolog
 Comments:
******************************************************************************/

include "papayasfinal.inc"

domains

	/*Componentes de una pieza*/
	peso=real
	id=integer
	coste=real
	dias=real
	
	fruta=p(peso,id,dias)
	bandeja=fruta*
	
	bandejaFull=b(bandeja,peso,coste)
predicates

	estaLlena(bandejaFull,bandeja)
	noLlena(peso)
	annadir(fruta, bandeja, bandejaFull) /*b([A|B],P,C)*/
	
	/*Escribe el contenido de las bandejas*/
	escribe(bandejaFull)
	escribeId(bandeja)
	backtrack(bandeja, bandeja, peso, coste)
  papayasfinal(bandeja)

clauses

  	escribeId([]).

	escribeId([p(_,Id,_)|T]):-
		write('\t'),
		write(Id,'\n'),
		escribeId(T),
		write('\n').
		
	escribe(b(Bandeja,Pt,Ct)):-
		write('\t'),
		write(Pt,'\t'),
		write(Ct,'\t'),
		write('\n'),
		escribeId(Bandeja).
	
	noLlena(Pt):-
		Pt<=2.0.
	
	estaLlena(b([H|T],Pt,Ct),B):-
		Pt>2.0,
		escribe(b([H|T],Pt,Ct)),
		backtrack(B,[],0.0,0.3).
	
	annadir(p(PeF,Id,D), Band, b(Bandeja,Pt,Ct)):-
		/*No llena*/
		noLlena(Pt),
		
		/*Calculamos el peso nuevo*/
		Pnew=PeF+Pt,
		Ctnew=Ct+0.1+2.0*PeF+0.05*D,
		NuevaBandeja=[p(PeF,Id,D)|Bandeja],
		not(estaLlena(b(NuevaBandeja,Pnew,Ctnew),Band)),
		backtrack(Band,NuevaBandeja,Pnew,Ctnew).
	
	backtrack([H|T],B,Pt,Ct):-
		
		annadir(H,T,b(B,Pt,Ct)).
		
	papayasfinal(Almacen):-
		backtrack(Almacen,[],0.0,0.3).
goal

  papayasfinal([
p(0.273, 1400001, 1.1),
p(0.405, 1400002, 1.0),
p(0.517, 1400003, 1.1),
p(0.533, 1400004, 1.7),
p(0.358, 1400005, 1.5),
p(0.562, 1400006, 1.9),
p(0.322, 1400007, 2.4),
p(0.494, 1400008, 1.8),
p(0.39, 1400009, 1.6),
p(0.281, 1400010, 2.2),
p(0.395, 1400011, 2.0),
p(0.407, 1400012, 2.0),
p(0.329, 1400013, 3.0),
p(0.629, 1400014, 2.7),
p(0.417, 1400015, 1.2),
p(0.278, 1400016, 1.4),
p(0.583, 1400017, 2.2),
p(0.598, 1400018, 1.9),
p(0.271, 1400019, 1.6),
p(0.265, 1400020, 2.1)
]).
