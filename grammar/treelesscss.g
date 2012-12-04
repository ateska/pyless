tree grammar treelesscss;

options {
    tokenVocab=lesscss;
    ASTLabelType=CommonTree;
    language=Python;
}

// -------------
// Main rule.
//
//
styleSheet
	: ^( N_StyleSheet
		(
		  charSet	{ self.writeln($charSet.gencode); } 
		)?
		(
		  imports	{ self.writeln($imports.gencode); }
		 )*
		body*	// Body is 'direct' output function
	);

// -----------------
// Character set.   Picks up the user specified character set, should it be present.
//
charSet returns [gencode]
  	: ^(CHARSET_SYM STRING)	{ $gencode = '@charset {0}{1}'.format($STRING.text, self.EOLSEMI); }
    	;


// ---------
// Import.  Location of an external style sheet to include in the ruleset.
//
imports returns [gencode]
	: ^(IMPORT_SYM 		{
				  $gencode = '@import ';
				  mqs = list(); 
				}
		importUrl	{ $gencode += $importUrl.text; }
		(
		  media_query	{ mqs.append($media_query.gencode); }
		) *
				{
				  if len(mqs) > 0: $gencode += ' ' + self.LISTCOMA.join(mqs);
				  $gencode += self.EOLSEMI ; 
				}
	);

importUrl
	: STRING
	| URI
	;


// ---------
// Body
//
body
	: ruleSet	// ruleSet is 'direct' output function
	| media		// media is 'direct' output function
	| page		// page is 'direct' output function
	| fontface	// fontface is 'direct' output function
	| keyframes	// keyframes is 'direct' output function
	;


// ---------
// Media.   Introduce a set of rules that are to be used if the consumer indicates
//          it belongs to the signified medium.
//
media
	: ^(MEDIA_SYM		{ mqs = list(); }
		(
		  media_query	{ mqs.append($media_query.gencode); } 
		) *
				{
				  mediahead = '@media';
				  if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
				  mediahead += self.EOLLBRACKET;
				  self.writeln(mediahead);
				  self.indent_level += 1
				}
		body*
				{
				  self.indent_level -= 1
				  self.writeln(self.EOLRBRACKET);
				}
	);


// ---------    
// Media queries
//
media_query returns [gencode]
	: ^(N_MediaQuery	{ mq = list(); }
		(
		  media_stmt	{ mq.append($media_stmt.text); }
		| media_expr	{ mq.append($media_expr.gencode); }
		)+ 
	)			{ $gencode = ' '.join(mq); }
	;

media_stmt
	: IDENT
	;

media_expr returns [gencode]
	: ^(N_MediaExpr		{ $gencode  = '('; }
		media_stmt 	{ $gencode += $media_stmt.text; }
		(
		  expr		{ $gencode += ':' + $expr.gencode; }
		)? 
	)			{ $gencode += ')'; }
	;


// ---------
// Font face
//
fontface
	: ^(FONTFACE_SYM
				{
				  self.writeln('@font-face' + self.EOLLBRACKET);
				  self.indent_level += 1;
				}
		declarationset
				{
				  self.indent_level -= 1
				  self.writeln(self.EOLRBRACKET);
				}
	);

// ---------
// Page
//
page
	: ^(PAGE_SYM 		{ out = '@page'; }
		(
		  pseudoPage	{ out += ' ' + $pseudoPage.gencode; }
		)?
				{
				  self.writeln(out + self.EOLLBRACKET);
				  self.indent_level += 1;
				}
		declarationset
				{
				  self.indent_level -= 1
				  self.writeln(self.EOLRBRACKET);
				}
	);

fragment pseudoPage returns [gencode]
	: IDENT 		{ $gencode = $IDENT.text; }
	;


// ---------
// Keyframes.   From CSS3 Animation
//
keyframes
	: ^(KEYFRAMES_SYM IDENT
				{
				  self.writeln('@keyframes ' + $IDENT.text + self.EOLLBRACKET);
				  self.indent_level += 1;
				}
		keyframes_block*
				{
				  self.indent_level -= 1
				  self.writeln(self.EOLRBRACKET);
				}
	);

keyframes_block
	: ^(N_KeyframeBlock 	{ ks = list(); }
		( keyframe_selector
		  		{ ks.append($keyframe_selector.gencode); }
		)+
				{
				  self.writeln(self.LISTCOMA.join(ks) + self.EOLLBRACKET);
				  self.indent_level += 1;
				}
		declarationset
				{
				  self.indent_level -= 1
				  self.writeln(self.EOLRBRACKET);
				}
	);

keyframe_selector returns [gencode]
	: ^(M_KeyframeSelector
		( IDENT 	{ $gencode = $IDENT.text; }
		| PERCENTAGE 	{ $gencode = $PERCENTAGE.text; }
		)
	);


// ---------
// Rules
//
ruleSet
	: ^(N_RuleSet		{ sellist = list(); }
		(
		 selector_list	{ sellist.append($selector_list.gencode); } 
		)+
				{
				  self.writeln(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
				  self.indent_level += 1;
				}
		declarationset
				{
				  self.indent_level -= 1
				  self.writeln(self.EOLRBRACKET);
				}
	);

selector_list returns [gencode]:
	^(N_Selector
		selector	{ $gencode = $selector.gencode; }
	);

selector returns [gencode]
	: a=simpleSelector	{ $gencode = $a.gencode; }
	(
		combinator	{ $gencode += $combinator.gencode; }
		b=simpleSelector
				{
				  # This code decides if there will be whitespace between selectors or not
				  #TODO: Refactor this (to remove this 'strange construct')
				  if $b.gencode[:1] == ':':
					$gencode = $gencode.rstrip() + $b.gencode;
				  else:
					$gencode += $b.gencode;
				}
	)*
	;

combinator returns [gencode]
	: PLUS			{ $gencode = $PLUS.text; }
	| GREATER		{ $gencode = $GREATER.text; }
	|			{ $gencode = ' '; }
	;

simpleSelector returns [gencode]
	: IDENT			{ $gencode = $IDENT.text; }
	| STAR			{ $gencode = $STAR.text; }
	| HASH			{ $gencode = $HASH.text; }
	| pseudo		{ $gencode = $pseudo.gencode; }
	| attrib		{ $gencode = $attrib.gencode; }
	;

pseudo returns [gencode]
	: ^(N_Pseudo
		a=COLON		{ $gencode = $a.text; }
		(
		  b=COLON 	{ $gencode += $b.text; }
		)?
		IDENT		{ $gencode += $IDENT.text; }
	)
	| ^(N_Pseudo
		a=COLON		{ $gencode = $a.text; }
		(
		  b=COLON 	{ $gencode += $b.text; }
		)?
		pseudoFunction	{ $gencode += $pseudoFunction.gencode; }
	);

pseudoFunction returns [gencode]
	: ^(N_PseudoFunction
		FUNCTION
		expr 		{ $gencode = $FUNCTION.text + $expr.gencode + ')'; }
	)
	| ^(N_PseudoFunction
		FUNCTION LBRACKET
		attribBody
		RBRACKET	{ $gencode = $FUNCTION.text + '[' + $attribBody.gencode + '])'; }
	)
	| ^(N_PseudoFunction
		FUNCTION
		pseudo		{ $gencode = $FUNCTION.text + $pseudo.gencode + ')'; }
	);

attrib returns [gencode]
	: ^(N_Attrib
		attribBody	{ $gencode = '[' + $attribBody.gencode + ']'; }
	);

attribBody returns [gencode]
	: IDENT			{ $gencode = $IDENT.text; }
	| ^(attribOper
		IDENT
		term 		{ $gencode = $IDENT.text + $attribOper.gencode + $term.gencode; }
	);

fragment attribOper returns [gencode]
	: OPEQ			{ $gencode = $OPEQ.text; }
	| INCLUDES		{ $gencode = $INCLUDES.text; }
	| DASHMATCH		{ $gencode = $DASHMATCH.text; }
	| PREFIXMATCH		{ $gencode = $PREFIXMATCH.text; }
	| SUFFIXMATCH		{ $gencode = $SUFFIXMATCH.text; }
	| SUBSTRINGMATCH	{ $gencode = $SUBSTRINGMATCH.text; }
	;

// ---------
// Declarations
//
declarationset
	: N_Empty
	| declaration+
	;


declaration
	: ^(N_Declaration
		property 	{ propout = $property.gencode +  ":";  }
		(
		  expr		{ propout += $expr.gencode}
		)?
		(
		  prio		{ propout += ' !important'}
		)?
				{
				  #TODO: Remove last semicolon in the declarationset (how?) ...
				  self.writeln(propout + self.EOLSEMI);
				}
	);

property returns [gencode]
	: IDENT 		{ $gencode = $IDENT.text; }
	;

prio
	: IMPORTANT_SYM
	;


expr returns [gencode]
	: ^( operator
		a=expr
		b=expr 		{ $gencode = $a.gencode + $operator.gencode + $b.gencode; }
	)
	| term			{ $gencode = $term.gencode; }
	;

fragment operator returns [gencode]
	: SOLIDUS 		{ $gencode = $SOLIDUS.text; }
	| COMMA 		{ $gencode = $COMMA.text; }
	| N_Space		{ $gencode = ' '; }
	;

term returns [gencode]
	: ^(N_Term
		unaryOperator
		termnum		{ $gencode = $unaryOperator.text + $termnum.gencode; }
	) 	
	| ^(N_Term
		termnum		{ $gencode = $termnum.gencode; }
	)			
	| STRING		{ $gencode = $STRING.text; }
	| IDENT			{ $gencode = $IDENT.text; }
	| URI			{ $gencode = $URI.text; }
	| ^(N_Term
		hexColor	{ $gencode = $hexColor.text; }
	)
	| UNICODE_RANGE		{ $gencode = $UNICODE_RANGE.text; }
	;

fragment termnum returns [gencode]
	: NUMBER		{ $gencode = $NUMBER.text.strip(); }
	| PERCENTAGE		{ $gencode = $PERCENTAGE.text.strip(); }
	| LENGTH		{ $gencode = $LENGTH.text.strip(); }
	| EMS			{ $gencode = $EMS.text.strip(); }
	| EXS			{ $gencode = $EXS.text.strip(); }
	| REMS			{ $gencode = $REMS.text.strip(); }
	| CHS			{ $gencode = $CHS.text.strip(); }
	| ANGLE			{ $gencode = $ANGLE.text.strip(); }
	| TIME			{ $gencode = $TIME.text.strip(); }
	| FREQ			{ $gencode = $FREQ.text.strip(); }
	| RESOLUTION		{ $gencode = $RESOLUTION.text.strip(); }
	| VPORTLEN		{ $gencode = $VPORTLEN.text.strip(); }
	| NTH			{ $gencode = $NTH.text.strip(); }
	| function 		{ $gencode = $function.gencode; }
	;


unaryOperator
	: MINUS
	| PLUS
	;


function returns [gencode]
	: ^(N_Function
		fnct_name
		fnct_args	{ $gencode = $fnct_name.gencode + $fnct_args.gencode + ')'; }
	)
	;

fnct_name returns [gencode]
	: ^(FUNCTION		{ prefix = list(); }
		( IDENT 	{ prefix.append($IDENT.text); }
		| COLON 	{ prefix.append($COLON.text); }
		| DOT		{ prefix.append($DOT.text); }
		)* 
	)			{ $gencode = ''.join(prefix) + $FUNCTION.text; }
	;

fragment fnct_args returns [gencode]
	: ^(COMMA
		a=fnct_args
		b=fnct_args	{ $gencode = $a.gencode + $COMMA.text + $b.gencode; }
	)
	| ^(OPEQ
		IDENT
		expr 		{ $gencode = $IDENT.text + $OPEQ.text + $expr.gencode; }
	)
	| ^(N_Expr
		expr 		{ $gencode = $expr.gencode; }
	);


hexColor
	: HASH
	;
