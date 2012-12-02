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
		(charSet { self.output($charSet.gencode); } )?
		(imports { self.output($imports.gencode); } )*
		body*	// Body is 'direct' output function
	)
	;

// -----------------
// Character set.   Picks up the user specified character set, should it be present.
//
charSet returns [gencode]
  	: ^(CHARSET_SYM STRING)
  		{ $gencode = '@charset {0}{1}'.format($STRING.text, self.EOLSEMI); }
    	;


// ---------
// Import.  Location of an external style sheet to include in the ruleset.
//
imports returns [gencode]
	@init
	{
		$gencode = '@import ';
		mqs = []
	}
	: ^(IMPORT_SYM
		importUrl { $gencode += $importUrl.text ; }
		( media_query { mqs.append($media_query.gencode) ; } ) *
	)
		{
			if len(mqs) > 0: $gencode += ' ' + self.LISTCOMA.join(mqs);
			$gencode += self.EOLSEMI ; 
		}
    		
	;

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
	@init
	{
		mqs = []
	}
	: ^(MEDIA_SYM
		( media_query { mqs.append($media_query.gencode) ; } ) *
		{
			mediahead = '@media';
			if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
			mediahead += self.EOLLBRACKET;
			self.output(mediahead);
			self.indent_level += 1
		}
		body*
		{
			self.indent_level -= 1
			self.output(self.EOLRBRACKET);
		}
	)
	;


// ---------    
// Media queries
//
media_query returns [gencode]
	@init
	{
		mq = list()
	}
	: ^(N_MediaQuery
		( media_stmt { mq.append($media_stmt.text); }
		| media_expr { mq.append($media_expr.text); }
		)+ 
	)
		{ $gencode = ' '.join(mq); }
	;

media_stmt
	: IDENT
	;

media_expr
	: ^(N_MediaExpr media_stmt )
//TODO: : ^(N_MediaExpr media_stmt expr? )
	;



// ---------
// Font face
//
fontface
	: ^(FONTFACE_SYM
		{
			self.output('@fontface' + self.EOLLBRACKET);
			self.indent_level += 1;
		}
		declarationset
		{
			self.indent_level -= 1
			self.output(self.EOLRBRACKET);
		}
	)
	;

// ---------
// Page
//
page
	: ^(PAGE_SYM
		{	out = '@page'}
		(
			pseudoPage
			{ out += ' ' + $pseudoPage.text}
		)?
		{
			self.output(out + self.EOLLBRACKET);
			self.indent_level += 1;
		}
		declarationset
		{
			self.indent_level -= 1
			self.output(self.EOLRBRACKET);
		}
	)
	;

pseudoPage
	: IDENT
	;


// ---------
// Keyframes.   From CSS3 Animation
//
keyframes
	: ^(KEYFRAMES_SYM IDENT
		{
			self.output('@keyframes ' + $IDENT.text + self.EOLLBRACKET);
			self.indent_level += 1;
		}
		keyframes_block*
		{
			self.indent_level -= 1
			self.output(self.EOLRBRACKET);
		}
	)
	;

keyframes_block
	: ^(N_KeyframeBlock
		{ ks = []; }
		(
			keyframe_selector
				{ ks.append($keyframe_selector.gencode); }
		)+
		{
			self.output(' '.join(ks) + self.EOLLBRACKET);
			self.indent_level += 1;
		}
		declarationset
		{
			self.indent_level -= 1
			self.output(self.EOLRBRACKET);
		}
	)
	;


keyframe_selector returns [gencode]
	: ^(M_KeyframeSelector ( 
		  IDENT 	{ $gencode = $IDENT.text; }
		| PERCENTAGE 	{ $gencode = $PERCENTAGE.text; }
		) 
	)
	;


// ---------
// Rules
//
ruleSet
	@init
	{
		sellist = [];
	}
	: ^(N_RuleSet
		(selector_list { sellist.append($selector_list.gencode); } )+
		{
			self.output(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
			self.indent_level += 1;
		}
		declarationset
		{
			self.indent_level -= 1
			self.output(self.EOLRBRACKET);
		}
	)	
	;

selector_list returns [gencode]:
	^(N_Selector
		selector { $gencode = $selector.gencode; }
	)	
	;

selector returns [gencode]
	: a=simpleSelector { $gencode = $a.gencode; }
	(
		combinator { $gencode += $combinator.gencode; }
		b=simpleSelector {
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
	: PLUS 		{ $gencode = $PLUS.text; }
	| GREATER	{ $gencode = $GREATER.text; }
	|		{ $gencode = ' '; }
	;

simpleSelector returns [gencode]
	: IDENT 	{ $gencode = $IDENT.text; }
	| STAR		{ $gencode = $STAR.text; }
	| HASH		{ $gencode = $HASH.text; }
	| pseudo	{ $gencode = $pseudo.gencode; }
	| attrib	{ $gencode = $attrib.gencode; }
	;

pseudo returns [gencode]
	: ^(N_Pseudo a=COLON b=COLON? IDENT)
		{ $gencode = $a.text + ($b.text if $b is not None else '') + $IDENT.text; }

//	| ^(N_Pseudo a=COLON b=COLON? pseudoFunction)
	;

attrib returns [gencode]
	: ^(N_Attrib attribBody )
			{ $gencode = '[' + $attribBody.gencode + ']' ; }
	;

attribBody returns [gencode]
	: IDENT		{ $gencode = $IDENT.text; }
	| ^(attribOper IDENT term )
			{ $gencode = $IDENT.text + $attribOper.text + $term.gencode; }
	;

fragment attribOper
	: OPEQ
	| INCLUDES
	| DASHMATCH
	| PREFIXMATCH
	| SUFFIXMATCH
	| SUBSTRINGMATCH
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
		property { propout = $property.text +  ":"; }
		(expr { propout += $expr.gencode} )?
		(prio { propout += ' !important'} )?
		{
			#TODO: Remove last semicolon in the declarationset (how?) ...
			self.output(propout + self.EOLSEMI);
		}
	)
	;

property
	: IDENT
	;

prio
	: IMPORTANT_SYM
	;


expr returns [gencode]
	: ^( operator
		a=expr b=expr 
	)			{ $gencode = $a.gencode + $operator.gencode + $b.gencode; }
	| term			{ $gencode = $term.gencode; }
	;

fragment operator returns [gencode]
	: SOLIDUS 		{ $gencode = $SOLIDUS.text; }
	| COMMA 		{ $gencode = $COMMA.text; }
	| N_Space		{ $gencode = ' '; }
	;

term returns [gencode]
	: ^(N_Term unaryOperator termnum) 	{ $gencode = $unaryOperator.text + $termnum.gencode; }
	| ^(N_Term termnum)			{ $gencode = $termnum.gencode; }
	| STRING		{ $gencode = $STRING.text; }
	| IDENT			{ $gencode = $IDENT.text; }
	| URI			{ $gencode = $URI.text; }
	| hexColor		{ $gencode = $hexColor.text; }
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
	: ^(N_Function fnct_name fnct_args)
			{ $gencode = $fnct_name.gencode + $fnct_args.gencode + ')'; }
	;

fnct_name returns [gencode]
	: ^(FUNCTION
				{ prefix = []; }
		( IDENT 	{ prefix.append($IDENT.text); }
		| COLON 	{ prefix.append($COLON.text); }
		| DOT		{ prefix.append($DOT.text); }
		)* 
	) { $gencode = ''.join(prefix) + $FUNCTION.text; }
	;

fragment fnct_args returns [gencode]
	: ^(COMMA a=fnct_args b=fnct_args)
			{ $gencode = $a.gencode + $COMMA.text + $b.gencode ; }

	| ^(OPEQ IDENT expr)
			{ $gencode = $IDENT.text + $OPEQ.text + $expr.gencode ; }
	| term
			{ $gencode = $term.gencode ; }
	;


hexColor
	: HASH
	;
