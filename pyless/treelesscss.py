# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-12-01 00:56:45

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=42
UNICODE_RANGE=64
STAR=41
EOF=-1
MEDIA_SYM=24
LBRACKET=40
INCLUDES=45
RPAREN=31
NAME=72
GREATER=37
ESCAPE=69
DIMENSION=105
STRINGESC=103
NL=106
COMMENT=100
D=77
E=78
F=79
G=80
A=74
B=75
RBRACE=26
C=76
L=85
M=86
NMCHAR=71
IMPORT_SYM=22
N=87
SUBSTRINGMATCH=49
O=88
H=81
I=82
J=83
K=84
NUMBER=52
U=94
T=93
W=96
V=95
Q=90
P=89
S=92
CDO=101
R=91
CDC=102
Y=98
PERCENTAGE=35
URL=73
X=97
Z=99
URI=23
PAGE_SYM=33
WS=104
DASHMATCH=46
EMS=54
N_PseudoFunction=17
N_RuleSet=7
NONASCII=67
N_MediaQuery=5
N_Selector=10
LBRACE=25
LPAREN=29
LENGTH=53
IMPORTANT_SYM=50
N_Function=12
TIME=59
KEYFRAMES_SYM=34
COMMA=27
N_StyleSheet=4
IDENT=28
PLUS=36
FREQ=60
RBRACKET=43
DOT=39
VPORTLEN=62
CHARSET_SYM=19
ANGLE=58
REMS=56
HASH=38
HEXCHAR=66
RESOLUTION=61
PREFIXMATCH=47
MINUS=65
N_Pseudo=16
SOLIDUS=51
SEMI=21
N_Empty=14
UNICODE=68
CHS=57
COLON=30
NMSTART=70
N_Declaration=11
OPEQ=44
FONTFACE_SYM=32
N_Term=18
EXS=55
N_Space=15
M_KeyframeSelector=9
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=48
NTH=63
STRING=20

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Space", "N_Pseudo", "N_PseudoFunction", "N_Term", "CHARSET_SYM", 
    "STRING", "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", 
    "COMMA", "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", 
    "KEYFRAMES_SYM", "PERCENTAGE", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", 
    "STAR", "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", "PREFIXMATCH", 
    "SUFFIXMATCH", "SUBSTRINGMATCH", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "LENGTH", "EMS", "EXS", "REMS", "CHS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
    "VPORTLEN", "NTH", "UNICODE_RANGE", "MINUS", "HEXCHAR", "NONASCII", 
    "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", "URL", "A", "B", "C", 
    "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", "CDO", "CDC", 
    "STRINGESC", "WS", "DIMENSION", "NL"
]




class treelesscss(TreeParser):
    grammarFileName = "treelesscss.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(treelesscss, self).__init__(input, state, *args, **kwargs)

        self.dfa22 = self.DFA22(
            self, 22,
            eot = self.DFA22_eot,
            eof = self.DFA22_eof,
            min = self.DFA22_min,
            max = self.DFA22_max,
            accept = self.DFA22_accept,
            special = self.DFA22_special,
            transition = self.DFA22_transition
            )






                


        



    # $ANTLR start "styleSheet"
    # treelesscss.g:13:1: styleSheet : ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) ;
    def styleSheet(self, ):

        charSet1 = None

        imports2 = None


        try:
            try:
                # treelesscss.g:14:2: ( ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) )
                # treelesscss.g:14:4: ^( N_StyleSheet ( charSet )? ( imports )* ( body )* )
                pass 
                self.match(self.input, N_StyleSheet, self.FOLLOW_N_StyleSheet_in_styleSheet51)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:15:3: ( charSet )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CHARSET_SYM) :
                        alt1 = 1
                    if alt1 == 1:
                        # treelesscss.g:15:4: charSet
                        pass 
                        self._state.following.append(self.FOLLOW_charSet_in_styleSheet56)
                        charSet1 = self.charSet()

                        self._state.following.pop()
                        #action start
                        self.output(charSet1); 
                        #action end



                    # treelesscss.g:16:3: ( imports )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == IMPORT_SYM) :
                            alt2 = 1


                        if alt2 == 1:
                            # treelesscss.g:16:4: imports
                            pass 
                            self._state.following.append(self.FOLLOW_imports_in_styleSheet66)
                            imports2 = self.imports()

                            self._state.following.pop()
                            #action start
                            self.output(imports2); 
                            #action end


                        else:
                            break #loop2
                    # treelesscss.g:17:3: ( body )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == N_RuleSet or LA3_0 == MEDIA_SYM) :
                            alt3 = 1


                        if alt3 == 1:
                            # treelesscss.g:17:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_styleSheet75)
                            self.body()

                            self._state.following.pop()


                        else:
                            break #loop3

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "styleSheet"


    # $ANTLR start "charSet"
    # treelesscss.g:24:1: charSet returns [gencode] : ^( CHARSET_SYM STRING ) ;
    def charSet(self, ):

        gencode = None

        STRING3 = None

        try:
            try:
                # treelesscss.g:25:4: ( ^( CHARSET_SYM STRING ) )
                # treelesscss.g:25:6: ^( CHARSET_SYM STRING )
                pass 
                self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet101)

                self.match(self.input, DOWN, None)
                STRING3=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet103)

                self.match(self.input, UP, None)
                #action start
                gencode =  '@charset {0}{1}'.format(STRING3.text, self.EOLSEMI) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "charSet"


    # $ANTLR start "imports"
    # treelesscss.g:33:1: imports returns [gencode] : ^( IMPORT_SYM importUrl ( media_query )* ) ;
    def imports(self, ):

        gencode = None

        importUrl4 = None

        media_query5 = None


          
        gencode =  '@import '
        mqs = []
        	
        try:
            try:
                # treelesscss.g:39:2: ( ^( IMPORT_SYM importUrl ( media_query )* ) )
                # treelesscss.g:39:4: ^( IMPORT_SYM importUrl ( media_query )* )
                pass 
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports141)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_importUrl_in_imports145)
                importUrl4 = self.importUrl()

                self._state.following.pop()
                #action start
                gencode += ((importUrl4 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(importUrl4.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(importUrl4.start)
                    )] or [None])[0] ; 
                #action end
                # treelesscss.g:41:3: ( media_query )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == N_MediaQuery) :
                        alt4 = 1


                    if alt4 == 1:
                        # treelesscss.g:41:5: media_query
                        pass 
                        self._state.following.append(self.FOLLOW_media_query_in_imports153)
                        media_query5 = self.media_query()

                        self._state.following.pop()
                        #action start
                        mqs.append(media_query5) ; 
                        #action end


                    else:
                        break #loop4

                self.match(self.input, UP, None)
                #action start
                   
                if len(mqs) > 0: gencode += ' ' + self.LISTCOMA.join(mqs);
                gencode += self.EOLSEMI ; 
                		
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "imports"

    class importUrl_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.importUrl_return, self).__init__()





    # $ANTLR start "importUrl"
    # treelesscss.g:50:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:51:2: ( STRING | URI )
                # treelesscss.g:
                pass 
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "importUrl"


    # $ANTLR start "body"
    # treelesscss.g:59:1: body : ( ruleSet | media );
    def body(self, ):

        try:
            try:
                # treelesscss.g:60:2: ( ruleSet | media )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == N_RuleSet) :
                    alt5 = 1
                elif (LA5_0 == MEDIA_SYM) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # treelesscss.g:60:4: ruleSet
                    pass 
                    self._state.following.append(self.FOLLOW_ruleSet_in_body204)
                    self.ruleSet()

                    self._state.following.pop()


                elif alt5 == 2:
                    # treelesscss.g:61:4: media
                    pass 
                    self._state.following.append(self.FOLLOW_media_in_body211)
                    self.media()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "body"


    # $ANTLR start "media"
    # treelesscss.g:72:1: media : ^( MEDIA_SYM ( media_query )* ( body )* ) ;
    def media(self, ):

        media_query6 = None


          
        mqs = []
        	
        try:
            try:
                # treelesscss.g:77:2: ( ^( MEDIA_SYM ( media_query )* ( body )* ) )
                # treelesscss.g:77:4: ^( MEDIA_SYM ( media_query )* ( body )* )
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media240)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:78:3: ( media_query )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == N_MediaQuery) :
                            alt6 = 1


                        if alt6 == 1:
                            # treelesscss.g:78:5: media_query
                            pass 
                            self._state.following.append(self.FOLLOW_media_query_in_media246)
                            media_query6 = self.media_query()

                            self._state.following.pop()
                            #action start
                            mqs.append(media_query6) ; 
                            #action end


                        else:
                            break #loop6
                    #action start
                       
                    mediahead = '@media';
                    if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
                    mediahead += self.EOLLBRACKET;
                    self.output(mediahead);
                    self.indent_level += 1
                    		
                    #action end
                    # treelesscss.g:86:3: ( body )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == N_RuleSet or LA7_0 == MEDIA_SYM) :
                            alt7 = 1


                        if alt7 == 1:
                            # treelesscss.g:86:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_media260)
                            self.body()

                            self._state.following.pop()


                        else:
                            break #loop7
                    #action start
                       
                    self.indent_level -= 1
                    self.output(self.EOLRBRACKET);
                    		
                    #action end

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "media"


    # $ANTLR start "media_query"
    # treelesscss.g:98:1: media_query returns [gencode] : ^( N_MediaQuery ( media_stmt | media_expr )+ ) ;
    def media_query(self, ):

        gencode = None

        media_stmt7 = None

        media_expr8 = None


          
        mq = list()
        	
        try:
            try:
                # treelesscss.g:103:2: ( ^( N_MediaQuery ( media_stmt | media_expr )+ ) )
                # treelesscss.g:103:4: ^( N_MediaQuery ( media_stmt | media_expr )+ )
                pass 
                self.match(self.input, N_MediaQuery, self.FOLLOW_N_MediaQuery_in_media_query295)

                self.match(self.input, DOWN, None)
                # treelesscss.g:104:3: ( media_stmt | media_expr )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 3
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IDENT) :
                        alt8 = 1
                    elif (LA8_0 == N_MediaExpr) :
                        alt8 = 2


                    if alt8 == 1:
                        # treelesscss.g:104:5: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query301)
                        media_stmt7 = self.media_stmt()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_stmt7 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_stmt7.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_stmt7.start)
                            )] or [None])[0]); 
                        #action end


                    elif alt8 == 2:
                        # treelesscss.g:105:5: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query309)
                        media_expr8 = self.media_expr()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_expr8 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_expr8.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_expr8.start)
                            )] or [None])[0]); 
                        #action end


                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1

                self.match(self.input, UP, None)
                #action start
                gencode =  ' '.join(mq) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "media_query"

    class media_stmt_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.media_stmt_return, self).__init__()





    # $ANTLR start "media_stmt"
    # treelesscss.g:111:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:112:2: ( IDENT )
                # treelesscss.g:112:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt335)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "media_stmt"

    class media_expr_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.media_expr_return, self).__init__()





    # $ANTLR start "media_expr"
    # treelesscss.g:115:1: media_expr : ^( N_MediaExpr media_stmt ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:116:2: ( ^( N_MediaExpr media_stmt ) )
                # treelesscss.g:116:4: ^( N_MediaExpr media_stmt )
                pass 
                self.match(self.input, N_MediaExpr, self.FOLLOW_N_MediaExpr_in_media_expr347)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr349)
                self.media_stmt()

                self._state.following.pop()

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "media_expr"


    # $ANTLR start "ruleSet"
    # treelesscss.g:124:1: ruleSet : ^( N_RuleSet ( selector_list )+ declarationset ) ;
    def ruleSet(self, ):

        selector_list9 = None


          
        sellist = [];
        	
        try:
            try:
                # treelesscss.g:129:2: ( ^( N_RuleSet ( selector_list )+ declarationset ) )
                # treelesscss.g:129:4: ^( N_RuleSet ( selector_list )+ declarationset )
                pass 
                self.match(self.input, N_RuleSet, self.FOLLOW_N_RuleSet_in_ruleSet376)

                self.match(self.input, DOWN, None)
                # treelesscss.g:130:3: ( selector_list )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == N_Selector) :
                        alt9 = 1


                    if alt9 == 1:
                        # treelesscss.g:130:4: selector_list
                        pass 
                        self._state.following.append(self.FOLLOW_selector_list_in_ruleSet381)
                        selector_list9 = self.selector_list()

                        self._state.following.pop()
                        #action start
                        sellist.append(selector_list9); 
                        #action end


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                #action start
                   
                self.output(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet394)
                self.declarationset()

                self._state.following.pop()
                #action start
                   
                self.indent_level -= 1
                self.output(self.EOLRBRACKET);
                		
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "ruleSet"


    # $ANTLR start "selector_list"
    # treelesscss.g:143:1: selector_list returns [gencode] : ^( N_Selector selector ) ;
    def selector_list(self, ):

        gencode = None

        selector10 = None


        try:
            try:
                # treelesscss.g:143:32: ( ^( N_Selector selector ) )
                # treelesscss.g:144:2: ^( N_Selector selector )
                pass 
                self.match(self.input, N_Selector, self.FOLLOW_N_Selector_in_selector_list417)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_selector_in_selector_list421)
                selector10 = self.selector()

                self._state.following.pop()
                #action start
                gencode =  selector10 
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector_list"


    # $ANTLR start "selector"
    # treelesscss.g:149:1: selector returns [gencode] : a= simpleSelector ( combinator b= simpleSelector )* ;
    def selector(self, ):

        gencode = None

        a = None

        b = None

        combinator11 = None


        try:
            try:
                # treelesscss.g:150:2: (a= simpleSelector ( combinator b= simpleSelector )* )
                # treelesscss.g:150:4: a= simpleSelector ( combinator b= simpleSelector )*
                pass 
                self._state.following.append(self.FOLLOW_simpleSelector_in_selector444)
                a = self.simpleSelector()

                self._state.following.pop()
                #action start
                gencode =  a 
                #action end
                # treelesscss.g:151:2: ( combinator b= simpleSelector )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == N_Attrib or LA10_0 == N_Pseudo or LA10_0 == IDENT or (PLUS <= LA10_0 <= HASH) or LA10_0 == STAR) :
                        alt10 = 1


                    if alt10 == 1:
                        # treelesscss.g:152:3: combinator b= simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector453)
                        combinator11 = self.combinator()

                        self._state.following.pop()
                        #action start
                        gencode += combinator11; 
                        #action end
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector461)
                        b = self.simpleSelector()

                        self._state.following.pop()
                        #action start
                                            
                        # This code decides if there will be whitespace between selectors or not
                        #TODO: Refactor this (to remove this 'strange construct')
                        if b[:1] == ':':
                        	gencode =  gencode.rstrip() + b
                        else:
                        	gencode += b;
                        		
                        #action end


                    else:
                        break #loop10




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector"


    # $ANTLR start "combinator"
    # treelesscss.g:164:1: combinator returns [gencode] : ( PLUS | GREATER | );
    def combinator(self, ):

        gencode = None

        PLUS12 = None
        GREATER13 = None

        try:
            try:
                # treelesscss.g:165:2: ( PLUS | GREATER | )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == PLUS:
                    alt11 = 1
                elif LA11 == GREATER:
                    alt11 = 2
                elif LA11 == N_Attrib or LA11 == N_Pseudo or LA11 == IDENT or LA11 == HASH or LA11 == STAR:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # treelesscss.g:165:4: PLUS
                    pass 
                    PLUS12=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator482)
                    #action start
                    gencode =  PLUS12.text 
                    #action end


                elif alt11 == 2:
                    # treelesscss.g:166:4: GREATER
                    pass 
                    GREATER13=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator491)
                    #action start
                    gencode =  GREATER13.text 
                    #action end


                elif alt11 == 3:
                    # treelesscss.g:167:5: 
                    pass 
                    #action start
                    gencode =  ' ' 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "combinator"


    # $ANTLR start "simpleSelector"
    # treelesscss.g:170:1: simpleSelector returns [gencode] : ( IDENT | STAR | HASH | pseudo | attrib );
    def simpleSelector(self, ):

        gencode = None

        IDENT14 = None
        STAR15 = None
        HASH16 = None
        pseudo17 = None

        attrib18 = None


        try:
            try:
                # treelesscss.g:171:2: ( IDENT | STAR | HASH | pseudo | attrib )
                alt12 = 5
                LA12 = self.input.LA(1)
                if LA12 == IDENT:
                    alt12 = 1
                elif LA12 == STAR:
                    alt12 = 2
                elif LA12 == HASH:
                    alt12 = 3
                elif LA12 == N_Pseudo:
                    alt12 = 4
                elif LA12 == N_Attrib:
                    alt12 = 5
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # treelesscss.g:171:4: IDENT
                    pass 
                    IDENT14=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_simpleSelector514)
                    #action start
                    gencode =  IDENT14.text 
                    #action end


                elif alt12 == 2:
                    # treelesscss.g:172:4: STAR
                    pass 
                    STAR15=self.match(self.input, STAR, self.FOLLOW_STAR_in_simpleSelector522)
                    #action start
                    gencode =  STAR15.text 
                    #action end


                elif alt12 == 3:
                    # treelesscss.g:173:4: HASH
                    pass 
                    HASH16=self.match(self.input, HASH, self.FOLLOW_HASH_in_simpleSelector530)
                    #action start
                    gencode =  HASH16.text 
                    #action end


                elif alt12 == 4:
                    # treelesscss.g:174:4: pseudo
                    pass 
                    self._state.following.append(self.FOLLOW_pseudo_in_simpleSelector538)
                    pseudo17 = self.pseudo()

                    self._state.following.pop()
                    #action start
                    gencode =  pseudo17 
                    #action end


                elif alt12 == 5:
                    # treelesscss.g:175:4: attrib
                    pass 
                    self._state.following.append(self.FOLLOW_attrib_in_simpleSelector545)
                    attrib18 = self.attrib()

                    self._state.following.pop()
                    #action start
                    gencode =  attrib18 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "simpleSelector"


    # $ANTLR start "pseudo"
    # treelesscss.g:178:1: pseudo returns [gencode] : ^( N_Pseudo a= COLON (b= COLON )? IDENT ) ;
    def pseudo(self, ):

        gencode = None

        a = None
        b = None
        IDENT19 = None

        try:
            try:
                # treelesscss.g:179:2: ( ^( N_Pseudo a= COLON (b= COLON )? IDENT ) )
                # treelesscss.g:179:4: ^( N_Pseudo a= COLON (b= COLON )? IDENT )
                pass 
                self.match(self.input, N_Pseudo, self.FOLLOW_N_Pseudo_in_pseudo563)

                self.match(self.input, DOWN, None)
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo567)
                # treelesscss.g:179:24: (b= COLON )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == COLON) :
                    alt13 = 1
                if alt13 == 1:
                    # treelesscss.g:179:24: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo571)



                IDENT19=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo574)

                self.match(self.input, UP, None)
                #action start
                gencode =  a.text + (b.text if b is not None else '') + IDENT19.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudo"


    # $ANTLR start "attrib"
    # treelesscss.g:185:1: attrib returns [gencode] : ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        gencode = None

        attribBody20 = None


        try:
            try:
                # treelesscss.g:186:2: ( ^( N_Attrib attribBody ) )
                # treelesscss.g:186:4: ^( N_Attrib attribBody )
                pass 
                self.match(self.input, N_Attrib, self.FOLLOW_N_Attrib_in_attrib597)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib599)
                attribBody20 = self.attribBody()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                gencode =  '[' + attribBody20 + ']'  
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attrib"


    # $ANTLR start "attribBody"
    # treelesscss.g:190:1: attribBody returns [gencode] : ( IDENT | ^( attribOper IDENT term ) );
    def attribBody(self, ):

        gencode = None

        IDENT21 = None
        IDENT22 = None
        attribOper23 = None

        term24 = None


        try:
            try:
                # treelesscss.g:191:2: ( IDENT | ^( attribOper IDENT term ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == IDENT) :
                    alt14 = 1
                elif ((OPEQ <= LA14_0 <= SUBSTRINGMATCH)) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # treelesscss.g:191:4: IDENT
                    pass 
                    IDENT21=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody621)
                    #action start
                    gencode =  IDENT21.text 
                    #action end


                elif alt14 == 2:
                    # treelesscss.g:192:4: ^( attribOper IDENT term )
                    pass 
                    self._state.following.append(self.FOLLOW_attribOper_in_attribBody630)
                    attribOper23 = self.attribOper()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    IDENT22=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody632)
                    self._state.following.append(self.FOLLOW_term_in_attribBody634)
                    term24 = self.term()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  IDENT22.text + attribOper23 + term24 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attribBody"


    # $ANTLR start "attribOper"
    # treelesscss.g:196:10: fragment attribOper returns [gencode] : ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH );
    def attribOper(self, ):

        gencode = None

        OPEQ25 = None
        INCLUDES26 = None
        DASHMATCH27 = None
        PREFIXMATCH28 = None
        SUFFIXMATCH29 = None
        SUBSTRINGMATCH30 = None

        try:
            try:
                # treelesscss.g:197:2: ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH )
                alt15 = 6
                LA15 = self.input.LA(1)
                if LA15 == OPEQ:
                    alt15 = 1
                elif LA15 == INCLUDES:
                    alt15 = 2
                elif LA15 == DASHMATCH:
                    alt15 = 3
                elif LA15 == PREFIXMATCH:
                    alt15 = 4
                elif LA15 == SUFFIXMATCH:
                    alt15 = 5
                elif LA15 == SUBSTRINGMATCH:
                    alt15 = 6
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # treelesscss.g:197:4: OPEQ
                    pass 
                    OPEQ25=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_attribOper658)
                    #action start
                    gencode =  OPEQ25.text 
                    #action end


                elif alt15 == 2:
                    # treelesscss.g:198:4: INCLUDES
                    pass 
                    INCLUDES26=self.match(self.input, INCLUDES, self.FOLLOW_INCLUDES_in_attribOper668)
                    #action start
                    gencode =  INCLUDES26.text 
                    #action end


                elif alt15 == 3:
                    # treelesscss.g:199:4: DASHMATCH
                    pass 
                    DASHMATCH27=self.match(self.input, DASHMATCH, self.FOLLOW_DASHMATCH_in_attribOper676)
                    #action start
                    gencode =  DASHMATCH27.text 
                    #action end


                elif alt15 == 4:
                    # treelesscss.g:200:4: PREFIXMATCH
                    pass 
                    PREFIXMATCH28=self.match(self.input, PREFIXMATCH, self.FOLLOW_PREFIXMATCH_in_attribOper684)
                    #action start
                    gencode =  PREFIXMATCH28.text 
                    #action end


                elif alt15 == 5:
                    # treelesscss.g:201:4: SUFFIXMATCH
                    pass 
                    SUFFIXMATCH29=self.match(self.input, SUFFIXMATCH, self.FOLLOW_SUFFIXMATCH_in_attribOper692)
                    #action start
                    gencode =  SUFFIXMATCH29.text 
                    #action end


                elif alt15 == 6:
                    # treelesscss.g:202:4: SUBSTRINGMATCH
                    pass 
                    SUBSTRINGMATCH30=self.match(self.input, SUBSTRINGMATCH, self.FOLLOW_SUBSTRINGMATCH_in_attribOper700)
                    #action start
                    gencode =  SUBSTRINGMATCH30.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attribOper"


    # $ANTLR start "declarationset"
    # treelesscss.g:208:1: declarationset : ( N_Empty | ( declaration )+ );
    def declarationset(self, ):

        try:
            try:
                # treelesscss.g:209:2: ( N_Empty | ( declaration )+ )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == N_Empty) :
                    alt17 = 1
                elif (LA17_0 == N_Declaration) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # treelesscss.g:209:4: N_Empty
                    pass 
                    self.match(self.input, N_Empty, self.FOLLOW_N_Empty_in_declarationset716)


                elif alt17 == 2:
                    # treelesscss.g:210:4: ( declaration )+
                    pass 
                    # treelesscss.g:210:4: ( declaration )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == N_Declaration) :
                            alt16 = 1


                        if alt16 == 1:
                            # treelesscss.g:210:4: declaration
                            pass 
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset721)
                            self.declaration()

                            self._state.following.pop()


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declarationset"


    # $ANTLR start "declaration"
    # treelesscss.g:214:1: declaration : ^( N_Declaration property ( expr )? ( prio )? ) ;
    def declaration(self, ):

        property31 = None

        expr32 = None


        try:
            try:
                # treelesscss.g:215:2: ( ^( N_Declaration property ( expr )? ( prio )? ) )
                # treelesscss.g:215:4: ^( N_Declaration property ( expr )? ( prio )? )
                pass 
                self.match(self.input, N_Declaration, self.FOLLOW_N_Declaration_in_declaration735)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_property_in_declaration739)
                property31 = self.property()

                self._state.following.pop()
                #action start
                propout = property31 +  ":"; 
                #action end
                # treelesscss.g:217:3: ( expr )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == N_Space or LA18_0 == N_Term or LA18_0 == STRING or LA18_0 == URI or (COMMA <= LA18_0 <= IDENT) or LA18_0 == HASH or LA18_0 == SOLIDUS or LA18_0 == UNICODE_RANGE) :
                    alt18 = 1
                if alt18 == 1:
                    # treelesscss.g:217:4: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_declaration746)
                    expr32 = self.expr()

                    self._state.following.pop()
                    #action start
                    propout += expr32
                    #action end



                # treelesscss.g:218:3: ( prio )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == IMPORTANT_SYM) :
                    alt19 = 1
                if alt19 == 1:
                    # treelesscss.g:218:4: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration756)
                    self.prio()

                    self._state.following.pop()
                    #action start
                    propout += ' !important'
                    #action end



                #action start
                   
                #TODO: Remove last semicolon in the declarationset (how?) ...
                self.output(propout + self.EOLSEMI);
                		
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declaration"


    # $ANTLR start "property"
    # treelesscss.g:226:1: property returns [gencode] : IDENT ;
    def property(self, ):

        gencode = None

        IDENT33 = None

        try:
            try:
                # treelesscss.g:227:2: ( IDENT )
                # treelesscss.g:227:4: IDENT
                pass 
                IDENT33=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property783)
                #action start
                gencode =  IDENT33.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "property"


    # $ANTLR start "prio"
    # treelesscss.g:230:1: prio returns [gencode] : IMPORTANT_SYM ;
    def prio(self, ):

        gencode = None

        IMPORTANT_SYM34 = None

        try:
            try:
                # treelesscss.g:231:2: ( IMPORTANT_SYM )
                # treelesscss.g:231:4: IMPORTANT_SYM
                pass 
                IMPORTANT_SYM34=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio802)
                #action start
                gencode =  IMPORTANT_SYM34.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "prio"


    # $ANTLR start "expr"
    # treelesscss.g:235:1: expr returns [gencode] : ( ^( operator a= expr b= expr ) | term );
    def expr(self, ):

        gencode = None

        a = None

        b = None

        operator35 = None

        term36 = None


        try:
            try:
                # treelesscss.g:236:2: ( ^( operator a= expr b= expr ) | term )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == N_Space or LA20_0 == COMMA or LA20_0 == SOLIDUS) :
                    alt20 = 1
                elif (LA20_0 == N_Term or LA20_0 == STRING or LA20_0 == URI or LA20_0 == IDENT or LA20_0 == HASH or LA20_0 == UNICODE_RANGE) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # treelesscss.g:236:4: ^( operator a= expr b= expr )
                    pass 
                    self._state.following.append(self.FOLLOW_operator_in_expr823)
                    operator35 = self.operator()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr829)
                    a = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr833)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  a + operator35 + b 
                    #action end


                elif alt20 == 2:
                    # treelesscss.g:239:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_expr846)
                    term36 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term36 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "expr"


    # $ANTLR start "operator"
    # treelesscss.g:242:10: fragment operator returns [gencode] : ( SOLIDUS | COMMA | N_Space );
    def operator(self, ):

        gencode = None

        SOLIDUS37 = None
        COMMA38 = None

        try:
            try:
                # treelesscss.g:243:2: ( SOLIDUS | COMMA | N_Space )
                alt21 = 3
                LA21 = self.input.LA(1)
                if LA21 == SOLIDUS:
                    alt21 = 1
                elif LA21 == COMMA:
                    alt21 = 2
                elif LA21 == N_Space:
                    alt21 = 3
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # treelesscss.g:243:4: SOLIDUS
                    pass 
                    SOLIDUS37=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator867)
                    #action start
                    gencode =  SOLIDUS37.text 
                    #action end


                elif alt21 == 2:
                    # treelesscss.g:244:4: COMMA
                    pass 
                    COMMA38=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator876)
                    #action start
                    gencode =  COMMA38.text 
                    #action end


                elif alt21 == 3:
                    # treelesscss.g:245:4: N_Space
                    pass 
                    self.match(self.input, N_Space, self.FOLLOW_N_Space_in_operator885)
                    #action start
                    gencode =  ' ' 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "operator"


    # $ANTLR start "term"
    # treelesscss.g:248:1: term returns [gencode] : ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE );
    def term(self, ):

        gencode = None

        STRING42 = None
        IDENT43 = None
        URI44 = None
        UNICODE_RANGE46 = None
        unaryOperator39 = None

        termnum40 = None

        termnum41 = None

        hexColor45 = None


        try:
            try:
                # treelesscss.g:249:2: ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE )
                alt22 = 7
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # treelesscss.g:249:4: ^( N_Term unaryOperator termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term904)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_unaryOperator_in_term906)
                    unaryOperator39 = self.unaryOperator()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_termnum_in_term908)
                    termnum40 = self.termnum()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  unaryOperator39 + termnum40 
                    #action end


                elif alt22 == 2:
                    # treelesscss.g:250:4: ^( N_Term termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term918)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_termnum_in_term920)
                    termnum41 = self.termnum()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  termnum41 
                    #action end


                elif alt22 == 3:
                    # treelesscss.g:251:4: STRING
                    pass 
                    STRING42=self.match(self.input, STRING, self.FOLLOW_STRING_in_term930)
                    #action start
                    gencode =  STRING42.text 
                    #action end


                elif alt22 == 4:
                    # treelesscss.g:252:4: IDENT
                    pass 
                    IDENT43=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term938)
                    #action start
                    gencode =  IDENT43.text 
                    #action end


                elif alt22 == 5:
                    # treelesscss.g:253:4: URI
                    pass 
                    URI44=self.match(self.input, URI, self.FOLLOW_URI_in_term947)
                    #action start
                    gencode =  URI44.text 
                    #action end


                elif alt22 == 6:
                    # treelesscss.g:254:4: hexColor
                    pass 
                    self._state.following.append(self.FOLLOW_hexColor_in_term956)
                    hexColor45 = self.hexColor()

                    self._state.following.pop()
                    #action start
                    gencode =  ((hexColor45 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(hexColor45.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(hexColor45.start)
                        )] or [None])[0] 
                    #action end


                elif alt22 == 7:
                    # treelesscss.g:255:4: UNICODE_RANGE
                    pass 
                    UNICODE_RANGE46=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term964)
                    #action start
                    gencode =  UNICODE_RANGE46.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "term"


    # $ANTLR start "termnum"
    # treelesscss.g:258:10: fragment termnum returns [gencode] : ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function );
    def termnum(self, ):

        gencode = None

        NUMBER47 = None
        PERCENTAGE48 = None
        LENGTH49 = None
        EMS50 = None
        EXS51 = None
        REMS52 = None
        CHS53 = None
        ANGLE54 = None
        TIME55 = None
        FREQ56 = None
        RESOLUTION57 = None
        VPORTLEN58 = None
        NTH59 = None
        function60 = None


        try:
            try:
                # treelesscss.g:259:2: ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function )
                alt23 = 14
                LA23 = self.input.LA(1)
                if LA23 == NUMBER:
                    alt23 = 1
                elif LA23 == PERCENTAGE:
                    alt23 = 2
                elif LA23 == LENGTH:
                    alt23 = 3
                elif LA23 == EMS:
                    alt23 = 4
                elif LA23 == EXS:
                    alt23 = 5
                elif LA23 == REMS:
                    alt23 = 6
                elif LA23 == CHS:
                    alt23 = 7
                elif LA23 == ANGLE:
                    alt23 = 8
                elif LA23 == TIME:
                    alt23 = 9
                elif LA23 == FREQ:
                    alt23 = 10
                elif LA23 == RESOLUTION:
                    alt23 = 11
                elif LA23 == VPORTLEN:
                    alt23 = 12
                elif LA23 == NTH:
                    alt23 = 13
                elif LA23 == N_Function:
                    alt23 = 14
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # treelesscss.g:259:4: NUMBER
                    pass 
                    NUMBER47=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_termnum984)
                    #action start
                    gencode =  NUMBER47.text.strip() 
                    #action end


                elif alt23 == 2:
                    # treelesscss.g:260:4: PERCENTAGE
                    pass 
                    PERCENTAGE48=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_termnum992)
                    #action start
                    gencode =  PERCENTAGE48.text.strip() 
                    #action end


                elif alt23 == 3:
                    # treelesscss.g:261:4: LENGTH
                    pass 
                    LENGTH49=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_termnum1000)
                    #action start
                    gencode =  LENGTH49.text.strip() 
                    #action end


                elif alt23 == 4:
                    # treelesscss.g:262:4: EMS
                    pass 
                    EMS50=self.match(self.input, EMS, self.FOLLOW_EMS_in_termnum1008)
                    #action start
                    gencode =  EMS50.text.strip() 
                    #action end


                elif alt23 == 5:
                    # treelesscss.g:263:4: EXS
                    pass 
                    EXS51=self.match(self.input, EXS, self.FOLLOW_EXS_in_termnum1017)
                    #action start
                    gencode =  EXS51.text.strip() 
                    #action end


                elif alt23 == 6:
                    # treelesscss.g:264:4: REMS
                    pass 
                    REMS52=self.match(self.input, REMS, self.FOLLOW_REMS_in_termnum1026)
                    #action start
                    gencode =  REMS52.text.strip() 
                    #action end


                elif alt23 == 7:
                    # treelesscss.g:265:4: CHS
                    pass 
                    CHS53=self.match(self.input, CHS, self.FOLLOW_CHS_in_termnum1035)
                    #action start
                    gencode =  CHS53.text.strip() 
                    #action end


                elif alt23 == 8:
                    # treelesscss.g:266:4: ANGLE
                    pass 
                    ANGLE54=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_termnum1044)
                    #action start
                    gencode =  ANGLE54.text.strip() 
                    #action end


                elif alt23 == 9:
                    # treelesscss.g:267:4: TIME
                    pass 
                    TIME55=self.match(self.input, TIME, self.FOLLOW_TIME_in_termnum1053)
                    #action start
                    gencode =  TIME55.text.strip() 
                    #action end


                elif alt23 == 10:
                    # treelesscss.g:268:4: FREQ
                    pass 
                    FREQ56=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_termnum1062)
                    #action start
                    gencode =  FREQ56.text.strip() 
                    #action end


                elif alt23 == 11:
                    # treelesscss.g:269:4: RESOLUTION
                    pass 
                    RESOLUTION57=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_termnum1071)
                    #action start
                    gencode =  RESOLUTION57.text.strip() 
                    #action end


                elif alt23 == 12:
                    # treelesscss.g:270:4: VPORTLEN
                    pass 
                    VPORTLEN58=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_termnum1079)
                    #action start
                    gencode =  VPORTLEN58.text.strip() 
                    #action end


                elif alt23 == 13:
                    # treelesscss.g:271:4: NTH
                    pass 
                    NTH59=self.match(self.input, NTH, self.FOLLOW_NTH_in_termnum1087)
                    #action start
                    gencode =  NTH59.text.strip() 
                    #action end


                elif alt23 == 14:
                    # treelesscss.g:272:4: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_termnum1096)
                    function60 = self.function()

                    self._state.following.pop()
                    #action start
                    gencode =  function60 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "termnum"


    # $ANTLR start "unaryOperator"
    # treelesscss.g:276:1: unaryOperator returns [gencode] : ( MINUS | PLUS );
    def unaryOperator(self, ):

        gencode = None

        MINUS61 = None
        PLUS62 = None

        try:
            try:
                # treelesscss.g:277:2: ( MINUS | PLUS )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == MINUS) :
                    alt24 = 1
                elif (LA24_0 == PLUS) :
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # treelesscss.g:277:4: MINUS
                    pass 
                    MINUS61=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_unaryOperator1116)
                    #action start
                    gencode =  MINUS61.text 
                    #action end


                elif alt24 == 2:
                    # treelesscss.g:278:4: PLUS
                    pass 
                    PLUS62=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_unaryOperator1124)
                    #action start
                    gencode =  PLUS62.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "unaryOperator"


    # $ANTLR start "function"
    # treelesscss.g:282:1: function returns [gencode] : ^( N_Function fnct_name fnct_args ) ;
    def function(self, ):

        gencode = None

        fnct_name63 = None

        fnct_args64 = None


        try:
            try:
                # treelesscss.g:283:2: ( ^( N_Function fnct_name fnct_args ) )
                # treelesscss.g:283:4: ^( N_Function fnct_name fnct_args )
                pass 
                self.match(self.input, N_Function, self.FOLLOW_N_Function_in_function1144)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_fnct_name_in_function1146)
                fnct_name63 = self.fnct_name()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_fnct_args_in_function1148)
                fnct_args64 = self.fnct_args()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                gencode =  fnct_name63 + fnct_args64 + ')' 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "function"


    # $ANTLR start "fnct_name"
    # treelesscss.g:287:1: fnct_name returns [gencode] : ^( FUNCTION ( IDENT ( COLON | DOT )+ )* ) ;
    def fnct_name(self, ):

        gencode = None

        IDENT65 = None
        COLON66 = None
        DOT67 = None
        FUNCTION68 = None

        try:
            try:
                # treelesscss.g:288:2: ( ^( FUNCTION ( IDENT ( COLON | DOT )+ )* ) )
                # treelesscss.g:288:4: ^( FUNCTION ( IDENT ( COLON | DOT )+ )* )
                pass 
                FUNCTION68=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1170)

                #action start
                gencode =  '' 
                #action end

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:290:4: ( IDENT ( COLON | DOT )+ )*
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == IDENT) :
                            alt26 = 1


                        if alt26 == 1:
                            # treelesscss.g:290:5: IDENT ( COLON | DOT )+
                            pass 
                            IDENT65=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1181)
                            #action start
                            gencode += IDENT65.text; 
                            #action end
                            # treelesscss.g:291:5: ( COLON | DOT )+
                            cnt25 = 0
                            while True: #loop25
                                alt25 = 3
                                LA25_0 = self.input.LA(1)

                                if (LA25_0 == COLON) :
                                    alt25 = 1
                                elif (LA25_0 == DOT) :
                                    alt25 = 2


                                if alt25 == 1:
                                    # treelesscss.g:291:6: COLON
                                    pass 
                                    COLON66=self.match(self.input, COLON, self.FOLLOW_COLON_in_fnct_name1190)
                                    #action start
                                    gencode += COLON66.text; 
                                    #action end


                                elif alt25 == 2:
                                    # treelesscss.g:292:6: DOT
                                    pass 
                                    DOT67=self.match(self.input, DOT, self.FOLLOW_DOT_in_fnct_name1199)
                                    #action start
                                    gencode += DOT67.text; 
                                    #action end


                                else:
                                    if cnt25 >= 1:
                                        break #loop25

                                    eee = EarlyExitException(25, self.input)
                                    raise eee

                                cnt25 += 1


                        else:
                            break #loop26
                    #action start
                    gencode += FUNCTION68.text; 
                    #action end

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "fnct_name"


    # $ANTLR start "fnct_args"
    # treelesscss.g:299:10: fragment fnct_args returns [gencode] : ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | term );
    def fnct_args(self, ):

        gencode = None

        COMMA69 = None
        IDENT70 = None
        OPEQ71 = None
        a = None

        b = None

        expr72 = None

        term73 = None


        try:
            try:
                # treelesscss.g:300:2: ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | term )
                alt27 = 3
                LA27 = self.input.LA(1)
                if LA27 == COMMA:
                    alt27 = 1
                elif LA27 == OPEQ:
                    alt27 = 2
                elif LA27 == N_Term or LA27 == STRING or LA27 == URI or LA27 == IDENT or LA27 == HASH or LA27 == UNICODE_RANGE:
                    alt27 = 3
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # treelesscss.g:300:4: ^( COMMA a= fnct_args b= fnct_args )
                    pass 
                    COMMA69=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1244)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1248)
                    a = self.fnct_args()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1252)
                    b = self.fnct_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  a + COMMA69.text + b  
                    #action end


                elif alt27 == 2:
                    # treelesscss.g:303:4: ^( OPEQ IDENT expr )
                    pass 
                    OPEQ71=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_args1265)

                    self.match(self.input, DOWN, None)
                    IDENT70=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_args1267)
                    self._state.following.append(self.FOLLOW_expr_in_fnct_args1269)
                    expr72 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  IDENT70.text + OPEQ71.text + expr72  
                    #action end


                elif alt27 == 3:
                    # treelesscss.g:305:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_fnct_args1280)
                    term73 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term73  
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "fnct_args"

    class hexColor_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.hexColor_return, self).__init__()

            self.gencode = None




    # $ANTLR start "hexColor"
    # treelesscss.g:310:1: hexColor returns [gencode] : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        HASH74 = None

        try:
            try:
                # treelesscss.g:311:2: ( HASH )
                # treelesscss.g:311:4: HASH
                pass 
                HASH74=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1301)
                #action start
                retval.gencode =  HASH74.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"


    # Delegated rules


    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\22\1\2\5\uffff\1\14\2\uffff"
        )

    DFA22_max = DFA.unpack(
        u"\1\100\1\2\5\uffff\1\101\2\uffff"
        )

    DFA22_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\1\7\1\uffff\1\1\1\2"
        )

    DFA22_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA22_transition = [
        DFA.unpack(u"\1\1\1\uffff\1\2\2\uffff\1\4\4\uffff\1\3\11\uffff\1"
        u"\5\31\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\26\uffff\1\11\1\10\17\uffff\14\11\1\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #22

    class DFA22(DFA):
        pass


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet56 = frozenset([3, 7, 22, 24])
    FOLLOW_imports_in_styleSheet66 = frozenset([3, 7, 22, 24])
    FOLLOW_body_in_styleSheet75 = frozenset([3, 7, 24])
    FOLLOW_CHARSET_SYM_in_charSet101 = frozenset([2])
    FOLLOW_STRING_in_charSet103 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports141 = frozenset([2])
    FOLLOW_importUrl_in_imports145 = frozenset([3, 5])
    FOLLOW_media_query_in_imports153 = frozenset([3, 5])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body204 = frozenset([1])
    FOLLOW_media_in_body211 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media240 = frozenset([2])
    FOLLOW_media_query_in_media246 = frozenset([3, 5, 7, 24])
    FOLLOW_body_in_media260 = frozenset([3, 7, 24])
    FOLLOW_N_MediaQuery_in_media_query295 = frozenset([2])
    FOLLOW_media_stmt_in_media_query301 = frozenset([3, 6, 28])
    FOLLOW_media_expr_in_media_query309 = frozenset([3, 6, 28])
    FOLLOW_IDENT_in_media_stmt335 = frozenset([1])
    FOLLOW_N_MediaExpr_in_media_expr347 = frozenset([2])
    FOLLOW_media_stmt_in_media_expr349 = frozenset([3])
    FOLLOW_N_RuleSet_in_ruleSet376 = frozenset([2])
    FOLLOW_selector_list_in_ruleSet381 = frozenset([10, 11, 14])
    FOLLOW_declarationset_in_ruleSet394 = frozenset([3])
    FOLLOW_N_Selector_in_selector_list417 = frozenset([2])
    FOLLOW_selector_in_selector_list421 = frozenset([3])
    FOLLOW_simpleSelector_in_selector444 = frozenset([1, 13, 16, 28, 36, 37, 38, 41])
    FOLLOW_combinator_in_selector453 = frozenset([13, 16, 28, 36, 37, 38, 41])
    FOLLOW_simpleSelector_in_selector461 = frozenset([1, 13, 16, 28, 36, 37, 38, 41])
    FOLLOW_PLUS_in_combinator482 = frozenset([1])
    FOLLOW_GREATER_in_combinator491 = frozenset([1])
    FOLLOW_IDENT_in_simpleSelector514 = frozenset([1])
    FOLLOW_STAR_in_simpleSelector522 = frozenset([1])
    FOLLOW_HASH_in_simpleSelector530 = frozenset([1])
    FOLLOW_pseudo_in_simpleSelector538 = frozenset([1])
    FOLLOW_attrib_in_simpleSelector545 = frozenset([1])
    FOLLOW_N_Pseudo_in_pseudo563 = frozenset([2])
    FOLLOW_COLON_in_pseudo567 = frozenset([28, 30])
    FOLLOW_COLON_in_pseudo571 = frozenset([28])
    FOLLOW_IDENT_in_pseudo574 = frozenset([3])
    FOLLOW_N_Attrib_in_attrib597 = frozenset([2])
    FOLLOW_attribBody_in_attrib599 = frozenset([3])
    FOLLOW_IDENT_in_attribBody621 = frozenset([1])
    FOLLOW_attribOper_in_attribBody630 = frozenset([2])
    FOLLOW_IDENT_in_attribBody632 = frozenset([18, 20, 23, 28, 38, 64])
    FOLLOW_term_in_attribBody634 = frozenset([3])
    FOLLOW_OPEQ_in_attribOper658 = frozenset([1])
    FOLLOW_INCLUDES_in_attribOper668 = frozenset([1])
    FOLLOW_DASHMATCH_in_attribOper676 = frozenset([1])
    FOLLOW_PREFIXMATCH_in_attribOper684 = frozenset([1])
    FOLLOW_SUFFIXMATCH_in_attribOper692 = frozenset([1])
    FOLLOW_SUBSTRINGMATCH_in_attribOper700 = frozenset([1])
    FOLLOW_N_Empty_in_declarationset716 = frozenset([1])
    FOLLOW_declaration_in_declarationset721 = frozenset([1, 11, 14])
    FOLLOW_N_Declaration_in_declaration735 = frozenset([2])
    FOLLOW_property_in_declaration739 = frozenset([3, 15, 18, 20, 23, 27, 28, 38, 50, 51, 64])
    FOLLOW_expr_in_declaration746 = frozenset([3, 50])
    FOLLOW_prio_in_declaration756 = frozenset([3])
    FOLLOW_IDENT_in_property783 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio802 = frozenset([1])
    FOLLOW_operator_in_expr823 = frozenset([2])
    FOLLOW_expr_in_expr829 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_expr833 = frozenset([3])
    FOLLOW_term_in_expr846 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator867 = frozenset([1])
    FOLLOW_COMMA_in_operator876 = frozenset([1])
    FOLLOW_N_Space_in_operator885 = frozenset([1])
    FOLLOW_N_Term_in_term904 = frozenset([2])
    FOLLOW_unaryOperator_in_term906 = frozenset([12, 35, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_termnum_in_term908 = frozenset([3])
    FOLLOW_N_Term_in_term918 = frozenset([2])
    FOLLOW_termnum_in_term920 = frozenset([3])
    FOLLOW_STRING_in_term930 = frozenset([1])
    FOLLOW_IDENT_in_term938 = frozenset([1])
    FOLLOW_URI_in_term947 = frozenset([1])
    FOLLOW_hexColor_in_term956 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term964 = frozenset([1])
    FOLLOW_NUMBER_in_termnum984 = frozenset([1])
    FOLLOW_PERCENTAGE_in_termnum992 = frozenset([1])
    FOLLOW_LENGTH_in_termnum1000 = frozenset([1])
    FOLLOW_EMS_in_termnum1008 = frozenset([1])
    FOLLOW_EXS_in_termnum1017 = frozenset([1])
    FOLLOW_REMS_in_termnum1026 = frozenset([1])
    FOLLOW_CHS_in_termnum1035 = frozenset([1])
    FOLLOW_ANGLE_in_termnum1044 = frozenset([1])
    FOLLOW_TIME_in_termnum1053 = frozenset([1])
    FOLLOW_FREQ_in_termnum1062 = frozenset([1])
    FOLLOW_RESOLUTION_in_termnum1071 = frozenset([1])
    FOLLOW_VPORTLEN_in_termnum1079 = frozenset([1])
    FOLLOW_NTH_in_termnum1087 = frozenset([1])
    FOLLOW_function_in_termnum1096 = frozenset([1])
    FOLLOW_MINUS_in_unaryOperator1116 = frozenset([1])
    FOLLOW_PLUS_in_unaryOperator1124 = frozenset([1])
    FOLLOW_N_Function_in_function1144 = frozenset([2])
    FOLLOW_fnct_name_in_function1146 = frozenset([18, 20, 23, 27, 28, 38, 44, 64])
    FOLLOW_fnct_args_in_function1148 = frozenset([3])
    FOLLOW_FUNCTION_in_fnct_name1170 = frozenset([2])
    FOLLOW_IDENT_in_fnct_name1181 = frozenset([30, 39])
    FOLLOW_COLON_in_fnct_name1190 = frozenset([3, 28, 30, 39])
    FOLLOW_DOT_in_fnct_name1199 = frozenset([3, 28, 30, 39])
    FOLLOW_COMMA_in_fnct_args1244 = frozenset([2])
    FOLLOW_fnct_args_in_fnct_args1248 = frozenset([18, 20, 23, 27, 28, 38, 44, 64])
    FOLLOW_fnct_args_in_fnct_args1252 = frozenset([3])
    FOLLOW_OPEQ_in_fnct_args1265 = frozenset([2])
    FOLLOW_IDENT_in_fnct_args1267 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_fnct_args1269 = frozenset([3])
    FOLLOW_term_in_fnct_args1280 = frozenset([1])
    FOLLOW_HASH_in_hexColor1301 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
