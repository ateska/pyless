# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-12-02 20:15:29

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=43
UNICODE_RANGE=65
STAR=42
EOF=-1
MEDIA_SYM=25
LBRACKET=41
INCLUDES=46
RPAREN=32
NAME=73
GREATER=38
ESCAPE=70
DIMENSION=106
STRINGESC=104
NL=107
COMMENT=101
D=78
E=79
F=80
G=81
A=75
B=76
RBRACE=27
C=77
L=86
M=87
NMCHAR=72
IMPORT_SYM=23
N=88
SUBSTRINGMATCH=50
O=89
H=82
I=83
J=84
K=85
NUMBER=53
U=95
T=94
W=97
V=96
Q=91
P=90
S=93
CDO=102
R=92
CDC=103
Y=99
PERCENTAGE=36
URL=74
X=98
Z=100
URI=24
PAGE_SYM=34
WS=105
DASHMATCH=47
EMS=55
N_PseudoFunction=17
N_RuleSet=7
NONASCII=68
N_MediaQuery=5
N_Expr=19
N_Selector=10
LBRACE=26
LPAREN=30
LENGTH=54
IMPORTANT_SYM=51
N_Function=12
TIME=60
KEYFRAMES_SYM=35
COMMA=28
N_StyleSheet=4
IDENT=29
PLUS=37
FREQ=61
RBRACKET=44
DOT=40
VPORTLEN=63
CHARSET_SYM=20
ANGLE=59
REMS=57
HASH=39
HEXCHAR=67
RESOLUTION=62
PREFIXMATCH=48
MINUS=66
N_Pseudo=16
SOLIDUS=52
SEMI=22
N_Empty=14
UNICODE=69
CHS=58
COLON=31
NMSTART=71
N_Declaration=11
OPEQ=45
FONTFACE_SYM=33
N_Term=18
EXS=56
N_Space=15
M_KeyframeSelector=9
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=49
NTH=64
STRING=21

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Space", "N_Pseudo", "N_PseudoFunction", "N_Term", "N_Expr", 
    "CHARSET_SYM", "STRING", "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", 
    "RBRACE", "COMMA", "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", 
    "PAGE_SYM", "KEYFRAMES_SYM", "PERCENTAGE", "PLUS", "GREATER", "HASH", 
    "DOT", "LBRACKET", "STAR", "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", 
    "DASHMATCH", "PREFIXMATCH", "SUFFIXMATCH", "SUBSTRINGMATCH", "IMPORTANT_SYM", 
    "SOLIDUS", "NUMBER", "LENGTH", "EMS", "EXS", "REMS", "CHS", "ANGLE", 
    "TIME", "FREQ", "RESOLUTION", "VPORTLEN", "NTH", "UNICODE_RANGE", "MINUS", 
    "HEXCHAR", "NONASCII", "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", 
    "URL", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", 
    "CDO", "CDC", "STRINGESC", "WS", "DIMENSION", "NL"
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

        self.dfa30 = self.DFA30(
            self, 30,
            eot = self.DFA30_eot,
            eof = self.DFA30_eof,
            min = self.DFA30_min,
            max = self.DFA30_max,
            accept = self.DFA30_accept,
            special = self.DFA30_special,
            transition = self.DFA30_transition
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
                        # treelesscss.g:16:5: charSet
                        pass 
                        self._state.following.append(self.FOLLOW_charSet_in_styleSheet61)
                        charSet1 = self.charSet()

                        self._state.following.pop()
                        #action start
                        self.writeln(charSet1); 
                        #action end



                    # treelesscss.g:18:3: ( imports )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == IMPORT_SYM) :
                            alt2 = 1


                        if alt2 == 1:
                            # treelesscss.g:19:5: imports
                            pass 
                            self._state.following.append(self.FOLLOW_imports_in_styleSheet79)
                            imports2 = self.imports()

                            self._state.following.pop()
                            #action start
                            self.writeln(imports2); 
                            #action end


                        else:
                            break #loop2
                    # treelesscss.g:21:3: ( body )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == N_RuleSet or LA3_0 == MEDIA_SYM or (FONTFACE_SYM <= LA3_0 <= KEYFRAMES_SYM)) :
                            alt3 = 1


                        if alt3 == 1:
                            # treelesscss.g:21:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_styleSheet91)
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
    # treelesscss.g:27:1: charSet returns [gencode] : ^( CHARSET_SYM STRING ) ;
    def charSet(self, ):

        gencode = None

        STRING3 = None

        try:
            try:
                # treelesscss.g:28:4: ( ^( CHARSET_SYM STRING ) )
                # treelesscss.g:28:6: ^( CHARSET_SYM STRING )
                pass 
                self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet115)

                self.match(self.input, DOWN, None)
                STRING3=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet117)

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
    # treelesscss.g:35:1: imports returns [gencode] : ^( IMPORT_SYM importUrl ( media_query )* ) ;
    def imports(self, ):

        gencode = None

        importUrl4 = None

        media_query5 = None


        try:
            try:
                # treelesscss.g:36:2: ( ^( IMPORT_SYM importUrl ( media_query )* ) )
                # treelesscss.g:36:4: ^( IMPORT_SYM importUrl ( media_query )* )
                pass 
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports144)

                #action start
                                   
                gencode =  '@import '
                mqs = list(); 
                				
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_importUrl_in_imports152)
                importUrl4 = self.importUrl()

                self._state.following.pop()
                #action start
                gencode += ((importUrl4 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(importUrl4.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(importUrl4.start)
                    )] or [None])[0]; 
                #action end
                # treelesscss.g:41:3: ( media_query )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == N_MediaQuery) :
                        alt4 = 1


                    if alt4 == 1:
                        # treelesscss.g:42:5: media_query
                        pass 
                        self._state.following.append(self.FOLLOW_media_query_in_imports164)
                        media_query5 = self.media_query()

                        self._state.following.pop()
                        #action start
                        mqs.append(media_query5); 
                        #action end


                    else:
                        break #loop4
                #action start
                     
                if len(mqs) > 0: gencode += ' ' + self.LISTCOMA.join(mqs);
                gencode += self.EOLSEMI ; 
                				
                #action end

                self.match(self.input, UP, None)




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
    # treelesscss.g:59:1: body : ( ruleSet | media | page | fontface | keyframes );
    def body(self, ):

        try:
            try:
                # treelesscss.g:60:2: ( ruleSet | media | page | fontface | keyframes )
                alt5 = 5
                LA5 = self.input.LA(1)
                if LA5 == N_RuleSet:
                    alt5 = 1
                elif LA5 == MEDIA_SYM:
                    alt5 = 2
                elif LA5 == PAGE_SYM:
                    alt5 = 3
                elif LA5 == FONTFACE_SYM:
                    alt5 = 4
                elif LA5 == KEYFRAMES_SYM:
                    alt5 = 5
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # treelesscss.g:60:4: ruleSet
                    pass 
                    self._state.following.append(self.FOLLOW_ruleSet_in_body210)
                    self.ruleSet()

                    self._state.following.pop()


                elif alt5 == 2:
                    # treelesscss.g:61:4: media
                    pass 
                    self._state.following.append(self.FOLLOW_media_in_body216)
                    self.media()

                    self._state.following.pop()


                elif alt5 == 3:
                    # treelesscss.g:62:4: page
                    pass 
                    self._state.following.append(self.FOLLOW_page_in_body223)
                    self.page()

                    self._state.following.pop()


                elif alt5 == 4:
                    # treelesscss.g:63:4: fontface
                    pass 
                    self._state.following.append(self.FOLLOW_fontface_in_body230)
                    self.fontface()

                    self._state.following.pop()


                elif alt5 == 5:
                    # treelesscss.g:64:4: keyframes
                    pass 
                    self._state.following.append(self.FOLLOW_keyframes_in_body236)
                    self.keyframes()

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


        try:
            try:
                # treelesscss.g:73:2: ( ^( MEDIA_SYM ( media_query )* ( body )* ) )
                # treelesscss.g:73:4: ^( MEDIA_SYM ( media_query )* ( body )* )
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media254)

                #action start
                mqs = list(); 
                #action end

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:74:3: ( media_query )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == N_MediaQuery) :
                            alt6 = 1


                        if alt6 == 1:
                            # treelesscss.g:75:5: media_query
                            pass 
                            self._state.following.append(self.FOLLOW_media_query_in_media267)
                            media_query6 = self.media_query()

                            self._state.following.pop()
                            #action start
                            mqs.append(media_query6); 
                            #action end


                        else:
                            break #loop6
                    #action start
                         
                    mediahead = '@media';
                    if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
                    mediahead += self.EOLLBRACKET;
                    self.writeln(mediahead);
                    self.indent_level += 1
                    				
                    #action end
                    # treelesscss.g:84:3: ( body )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == N_RuleSet or LA7_0 == MEDIA_SYM or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM)) :
                            alt7 = 1


                        if alt7 == 1:
                            # treelesscss.g:84:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_media286)
                            self.body()

                            self._state.following.pop()


                        else:
                            break #loop7
                    #action start
                         
                    self.indent_level -= 1
                    self.writeln(self.EOLRBRACKET);
                    				
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
    # treelesscss.g:95:1: media_query returns [gencode] : ^( N_MediaQuery ( media_stmt | media_expr )+ ) ;
    def media_query(self, ):

        gencode = None

        media_stmt7 = None

        media_expr8 = None


        try:
            try:
                # treelesscss.g:96:2: ( ^( N_MediaQuery ( media_stmt | media_expr )+ ) )
                # treelesscss.g:96:4: ^( N_MediaQuery ( media_stmt | media_expr )+ )
                pass 
                self.match(self.input, N_MediaQuery, self.FOLLOW_N_MediaQuery_in_media_query314)

                #action start
                mq = list(); 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:97:3: ( media_stmt | media_expr )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 3
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IDENT) :
                        alt8 = 1
                    elif (LA8_0 == N_MediaExpr) :
                        alt8 = 2


                    if alt8 == 1:
                        # treelesscss.g:98:5: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query326)
                        media_stmt7 = self.media_stmt()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_stmt7 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_stmt7.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_stmt7.start)
                            )] or [None])[0]); 
                        #action end


                    elif alt8 == 2:
                        # treelesscss.g:99:5: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query334)
                        media_expr8 = self.media_expr()

                        self._state.following.pop()
                        #action start
                        mq.append(media_expr8); 
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
    # treelesscss.g:104:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:105:2: ( IDENT )
                # treelesscss.g:105:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt360)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "media_stmt"


    # $ANTLR start "media_expr"
    # treelesscss.g:108:1: media_expr returns [gencode] : ^( N_MediaExpr media_stmt ( expr )? ) ;
    def media_expr(self, ):

        gencode = None

        media_stmt9 = None

        expr10 = None


        try:
            try:
                # treelesscss.g:109:2: ( ^( N_MediaExpr media_stmt ( expr )? ) )
                # treelesscss.g:109:4: ^( N_MediaExpr media_stmt ( expr )? )
                pass 
                self.match(self.input, N_MediaExpr, self.FOLLOW_N_MediaExpr_in_media_expr376)

                #action start
                gencode =  '(' 
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr383)
                media_stmt9 = self.media_stmt()

                self._state.following.pop()
                #action start
                gencode += ((media_stmt9 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(media_stmt9.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(media_stmt9.start)
                    )] or [None])[0]; 
                #action end
                # treelesscss.g:111:3: ( expr )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == N_Space or LA9_0 == N_Term or LA9_0 == STRING or LA9_0 == URI or (COMMA <= LA9_0 <= IDENT) or LA9_0 == HASH or LA9_0 == SOLIDUS or LA9_0 == UNICODE_RANGE) :
                    alt9 = 1
                if alt9 == 1:
                    # treelesscss.g:112:5: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_media_expr396)
                    expr10 = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode += ':' + expr10; 
                    #action end




                self.match(self.input, UP, None)
                #action start
                gencode += ')'; 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "media_expr"


    # $ANTLR start "fontface"
    # treelesscss.g:121:1: fontface : ^( FONTFACE_SYM declarationset ) ;
    def fontface(self, ):

        try:
            try:
                # treelesscss.g:122:2: ( ^( FONTFACE_SYM declarationset ) )
                # treelesscss.g:122:4: ^( FONTFACE_SYM declarationset )
                pass 
                self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface428)

                #action start
                     
                self.writeln('@fontface' + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface438)
                self.declarationset()

                self._state.following.pop()
                #action start
                     
                self.indent_level -= 1
                self.writeln(self.EOLRBRACKET);
                				
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "fontface"


    # $ANTLR start "page"
    # treelesscss.g:137:1: page : ^( PAGE_SYM ( pseudoPage )? declarationset ) ;
    def page(self, ):

        pseudoPage11 = None


        try:
            try:
                # treelesscss.g:138:2: ( ^( PAGE_SYM ( pseudoPage )? declarationset ) )
                # treelesscss.g:138:4: ^( PAGE_SYM ( pseudoPage )? declarationset )
                pass 
                self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page460)

                #action start
                out = '@page'; 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:139:3: ( pseudoPage )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IDENT) :
                    alt10 = 1
                if alt10 == 1:
                    # treelesscss.g:140:5: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page474)
                    pseudoPage11 = self.pseudoPage()

                    self._state.following.pop()
                    #action start
                    out += ' ' + pseudoPage11; 
                    #action end



                #action start
                     
                self.writeln(out + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_page491)
                self.declarationset()

                self._state.following.pop()
                #action start
                     
                self.indent_level -= 1
                self.writeln(self.EOLRBRACKET);
                				
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "page"


    # $ANTLR start "pseudoPage"
    # treelesscss.g:153:10: fragment pseudoPage returns [gencode] : IDENT ;
    def pseudoPage(self, ):

        gencode = None

        IDENT12 = None

        try:
            try:
                # treelesscss.g:154:2: ( IDENT )
                # treelesscss.g:154:4: IDENT
                pass 
                IDENT12=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage515)
                #action start
                gencode =  IDENT12.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudoPage"


    # $ANTLR start "keyframes"
    # treelesscss.g:161:1: keyframes : ^( KEYFRAMES_SYM IDENT ( keyframes_block )* ) ;
    def keyframes(self, ):

        IDENT13 = None

        try:
            try:
                # treelesscss.g:162:2: ( ^( KEYFRAMES_SYM IDENT ( keyframes_block )* ) )
                # treelesscss.g:162:4: ^( KEYFRAMES_SYM IDENT ( keyframes_block )* )
                pass 
                self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes535)

                self.match(self.input, DOWN, None)
                IDENT13=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes537)
                #action start
                     
                self.writeln('@keyframes ' + IDENT13.text + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                # treelesscss.g:167:3: ( keyframes_block )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == N_KeyframeBlock) :
                        alt11 = 1


                    if alt11 == 1:
                        # treelesscss.g:167:3: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes547)
                        self.keyframes_block()

                        self._state.following.pop()


                    else:
                        break #loop11
                #action start
                     
                self.indent_level -= 1
                self.writeln(self.EOLRBRACKET);
                				
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "keyframes"


    # $ANTLR start "keyframes_block"
    # treelesscss.g:174:1: keyframes_block : ^( N_KeyframeBlock ( keyframe_selector )+ declarationset ) ;
    def keyframes_block(self, ):

        keyframe_selector14 = None


        try:
            try:
                # treelesscss.g:175:2: ( ^( N_KeyframeBlock ( keyframe_selector )+ declarationset ) )
                # treelesscss.g:175:4: ^( N_KeyframeBlock ( keyframe_selector )+ declarationset )
                pass 
                self.match(self.input, N_KeyframeBlock, self.FOLLOW_N_KeyframeBlock_in_keyframes_block567)

                #action start
                ks = list(); 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:176:3: ( keyframe_selector )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == M_KeyframeSelector) :
                        alt12 = 1


                    if alt12 == 1:
                        # treelesscss.g:176:5: keyframe_selector
                        pass 
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block576)
                        keyframe_selector14 = self.keyframe_selector()

                        self._state.following.pop()
                        #action start
                        ks.append(keyframe_selector14); 
                        #action end


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                #action start
                     
                self.writeln(self.LISTCOMA.join(ks) + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block599)
                self.declarationset()

                self._state.following.pop()
                #action start
                     
                self.indent_level -= 1
                self.writeln(self.EOLRBRACKET);
                				
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "keyframes_block"


    # $ANTLR start "keyframe_selector"
    # treelesscss.g:190:1: keyframe_selector returns [gencode] : ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) ) ;
    def keyframe_selector(self, ):

        gencode = None

        IDENT15 = None
        PERCENTAGE16 = None

        try:
            try:
                # treelesscss.g:191:2: ( ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) ) )
                # treelesscss.g:191:4: ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) )
                pass 
                self.match(self.input, M_KeyframeSelector, self.FOLLOW_M_KeyframeSelector_in_keyframe_selector622)

                self.match(self.input, DOWN, None)
                # treelesscss.g:192:3: ( IDENT | PERCENTAGE )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == IDENT) :
                    alt13 = 1
                elif (LA13_0 == PERCENTAGE) :
                    alt13 = 2
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # treelesscss.g:192:5: IDENT
                    pass 
                    IDENT15=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframe_selector628)
                    #action start
                    gencode =  IDENT15.text 
                    #action end


                elif alt13 == 2:
                    # treelesscss.g:193:5: PERCENTAGE
                    pass 
                    PERCENTAGE16=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_keyframe_selector637)
                    #action start
                    gencode =  PERCENTAGE16.text 
                    #action end




                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "keyframe_selector"


    # $ANTLR start "ruleSet"
    # treelesscss.g:201:1: ruleSet : ^( N_RuleSet ( selector_list )+ declarationset ) ;
    def ruleSet(self, ):

        selector_list17 = None


        try:
            try:
                # treelesscss.g:202:2: ( ^( N_RuleSet ( selector_list )+ declarationset ) )
                # treelesscss.g:202:4: ^( N_RuleSet ( selector_list )+ declarationset )
                pass 
                self.match(self.input, N_RuleSet, self.FOLLOW_N_RuleSet_in_ruleSet661)

                #action start
                sellist = list(); 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:203:3: ( selector_list )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == N_Selector) :
                        alt14 = 1


                    if alt14 == 1:
                        # treelesscss.g:204:4: selector_list
                        pass 
                        self._state.following.append(self.FOLLOW_selector_list_in_ruleSet673)
                        selector_list17 = self.selector_list()

                        self._state.following.pop()
                        #action start
                        sellist.append(selector_list17); 
                        #action end


                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1
                #action start
                     
                self.writeln(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet691)
                self.declarationset()

                self._state.following.pop()
                #action start
                     
                self.indent_level -= 1
                self.writeln(self.EOLRBRACKET);
                				
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
    # treelesscss.g:217:1: selector_list returns [gencode] : ^( N_Selector selector ) ;
    def selector_list(self, ):

        gencode = None

        selector18 = None


        try:
            try:
                # treelesscss.g:217:32: ( ^( N_Selector selector ) )
                # treelesscss.g:218:2: ^( N_Selector selector )
                pass 
                self.match(self.input, N_Selector, self.FOLLOW_N_Selector_in_selector_list713)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_selector_in_selector_list717)
                selector18 = self.selector()

                self._state.following.pop()
                #action start
                gencode =  selector18 
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
    # treelesscss.g:222:1: selector returns [gencode] : a= simpleSelector ( combinator b= simpleSelector )* ;
    def selector(self, ):

        gencode = None

        a = None

        b = None

        combinator19 = None


        try:
            try:
                # treelesscss.g:223:2: (a= simpleSelector ( combinator b= simpleSelector )* )
                # treelesscss.g:223:4: a= simpleSelector ( combinator b= simpleSelector )*
                pass 
                self._state.following.append(self.FOLLOW_simpleSelector_in_selector737)
                a = self.simpleSelector()

                self._state.following.pop()
                #action start
                gencode =  a 
                #action end
                # treelesscss.g:224:2: ( combinator b= simpleSelector )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == N_Attrib or LA15_0 == N_Pseudo or LA15_0 == IDENT or (PLUS <= LA15_0 <= HASH) or LA15_0 == STAR) :
                        alt15 = 1


                    if alt15 == 1:
                        # treelesscss.g:225:3: combinator b= simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector746)
                        combinator19 = self.combinator()

                        self._state.following.pop()
                        #action start
                        gencode += combinator19; 
                        #action end
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector754)
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
                        break #loop15




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector"


    # $ANTLR start "combinator"
    # treelesscss.g:238:1: combinator returns [gencode] : ( PLUS | GREATER | );
    def combinator(self, ):

        gencode = None

        PLUS20 = None
        GREATER21 = None

        try:
            try:
                # treelesscss.g:239:2: ( PLUS | GREATER | )
                alt16 = 3
                LA16 = self.input.LA(1)
                if LA16 == PLUS:
                    alt16 = 1
                elif LA16 == GREATER:
                    alt16 = 2
                elif LA16 == N_Attrib or LA16 == N_Pseudo or LA16 == IDENT or LA16 == HASH or LA16 == STAR:
                    alt16 = 3
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # treelesscss.g:239:4: PLUS
                    pass 
                    PLUS20=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator779)
                    #action start
                    gencode =  PLUS20.text 
                    #action end


                elif alt16 == 2:
                    # treelesscss.g:240:4: GREATER
                    pass 
                    GREATER21=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator788)
                    #action start
                    gencode =  GREATER21.text 
                    #action end


                elif alt16 == 3:
                    # treelesscss.g:241:6: 
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
    # treelesscss.g:244:1: simpleSelector returns [gencode] : ( IDENT | STAR | HASH | pseudo | attrib );
    def simpleSelector(self, ):

        gencode = None

        IDENT22 = None
        STAR23 = None
        HASH24 = None
        pseudo25 = None

        attrib26 = None


        try:
            try:
                # treelesscss.g:245:2: ( IDENT | STAR | HASH | pseudo | attrib )
                alt17 = 5
                LA17 = self.input.LA(1)
                if LA17 == IDENT:
                    alt17 = 1
                elif LA17 == STAR:
                    alt17 = 2
                elif LA17 == HASH:
                    alt17 = 3
                elif LA17 == N_Pseudo:
                    alt17 = 4
                elif LA17 == N_Attrib:
                    alt17 = 5
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # treelesscss.g:245:4: IDENT
                    pass 
                    IDENT22=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_simpleSelector813)
                    #action start
                    gencode =  IDENT22.text 
                    #action end


                elif alt17 == 2:
                    # treelesscss.g:246:4: STAR
                    pass 
                    STAR23=self.match(self.input, STAR, self.FOLLOW_STAR_in_simpleSelector822)
                    #action start
                    gencode =  STAR23.text 
                    #action end


                elif alt17 == 3:
                    # treelesscss.g:247:4: HASH
                    pass 
                    HASH24=self.match(self.input, HASH, self.FOLLOW_HASH_in_simpleSelector831)
                    #action start
                    gencode =  HASH24.text 
                    #action end


                elif alt17 == 4:
                    # treelesscss.g:248:4: pseudo
                    pass 
                    self._state.following.append(self.FOLLOW_pseudo_in_simpleSelector840)
                    pseudo25 = self.pseudo()

                    self._state.following.pop()
                    #action start
                    gencode =  pseudo25 
                    #action end


                elif alt17 == 5:
                    # treelesscss.g:249:4: attrib
                    pass 
                    self._state.following.append(self.FOLLOW_attrib_in_simpleSelector848)
                    attrib26 = self.attrib()

                    self._state.following.pop()
                    #action start
                    gencode =  attrib26 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "simpleSelector"


    # $ANTLR start "pseudo"
    # treelesscss.g:252:1: pseudo returns [gencode] : ( ^( N_Pseudo a= COLON (b= COLON )? IDENT ) | ^( N_Pseudo a= COLON (b= COLON )? pseudoFunction ) );
    def pseudo(self, ):

        gencode = None

        a = None
        b = None
        IDENT27 = None
        pseudoFunction28 = None


        try:
            try:
                # treelesscss.g:253:2: ( ^( N_Pseudo a= COLON (b= COLON )? IDENT ) | ^( N_Pseudo a= COLON (b= COLON )? pseudoFunction ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == N_Pseudo) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == 2) :
                        LA20_2 = self.input.LA(3)

                        if (LA20_2 == COLON) :
                            LA20 = self.input.LA(4)
                            if LA20 == COLON:
                                LA20_4 = self.input.LA(5)

                                if (LA20_4 == N_PseudoFunction) :
                                    alt20 = 2
                                elif (LA20_4 == IDENT) :
                                    alt20 = 1
                                else:
                                    nvae = NoViableAltException("", 20, 4, self.input)

                                    raise nvae

                            elif LA20 == N_PseudoFunction:
                                alt20 = 2
                            elif LA20 == IDENT:
                                alt20 = 1
                            else:
                                nvae = NoViableAltException("", 20, 3, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 20, 2, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # treelesscss.g:253:4: ^( N_Pseudo a= COLON (b= COLON )? IDENT )
                    pass 
                    self.match(self.input, N_Pseudo, self.FOLLOW_N_Pseudo_in_pseudo867)

                    self.match(self.input, DOWN, None)
                    a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo873)
                    #action start
                    gencode =  a.text 
                    #action end
                    # treelesscss.g:255:3: (b= COLON )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == COLON) :
                        alt18 = 1
                    if alt18 == 1:
                        # treelesscss.g:256:5: b= COLON
                        pass 
                        b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo888)
                        #action start
                        gencode += b.text; 
                        #action end



                    IDENT27=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo900)
                    #action start
                    gencode += IDENT27.text; 
                    #action end

                    self.match(self.input, UP, None)


                elif alt20 == 2:
                    # treelesscss.g:260:4: ^( N_Pseudo a= COLON (b= COLON )? pseudoFunction )
                    pass 
                    self.match(self.input, N_Pseudo, self.FOLLOW_N_Pseudo_in_pseudo912)

                    self.match(self.input, DOWN, None)
                    a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo918)
                    #action start
                    gencode =  a.text 
                    #action end
                    # treelesscss.g:262:3: (b= COLON )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == COLON) :
                        alt19 = 1
                    if alt19 == 1:
                        # treelesscss.g:263:5: b= COLON
                        pass 
                        b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo933)
                        #action start
                        gencode += b.text; 
                        #action end



                    self._state.following.append(self.FOLLOW_pseudoFunction_in_pseudo945)
                    pseudoFunction28 = self.pseudoFunction()

                    self._state.following.pop()
                    #action start
                    gencode += pseudoFunction28; 
                    #action end

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudo"


    # $ANTLR start "pseudoFunction"
    # treelesscss.g:268:1: pseudoFunction returns [gencode] : ( ^( N_PseudoFunction FUNCTION expr ) | ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | ^( N_PseudoFunction FUNCTION pseudo ) );
    def pseudoFunction(self, ):

        gencode = None

        FUNCTION29 = None
        FUNCTION31 = None
        FUNCTION33 = None
        expr30 = None

        attribBody32 = None

        pseudo34 = None


        try:
            try:
                # treelesscss.g:269:2: ( ^( N_PseudoFunction FUNCTION expr ) | ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | ^( N_PseudoFunction FUNCTION pseudo ) )
                alt21 = 3
                LA21_0 = self.input.LA(1)

                if (LA21_0 == N_PseudoFunction) :
                    LA21_1 = self.input.LA(2)

                    if (LA21_1 == 2) :
                        LA21_2 = self.input.LA(3)

                        if (LA21_2 == FUNCTION) :
                            LA21 = self.input.LA(4)
                            if LA21 == LBRACKET:
                                alt21 = 2
                            elif LA21 == N_Pseudo:
                                alt21 = 3
                            elif LA21 == N_Space or LA21 == N_Term or LA21 == STRING or LA21 == URI or LA21 == COMMA or LA21 == IDENT or LA21 == HASH or LA21 == SOLIDUS or LA21 == UNICODE_RANGE:
                                alt21 = 1
                            else:
                                nvae = NoViableAltException("", 21, 3, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 21, 2, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 21, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # treelesscss.g:269:4: ^( N_PseudoFunction FUNCTION expr )
                    pass 
                    self.match(self.input, N_PseudoFunction, self.FOLLOW_N_PseudoFunction_in_pseudoFunction964)

                    self.match(self.input, DOWN, None)
                    FUNCTION29=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction968)
                    self._state.following.append(self.FOLLOW_expr_in_pseudoFunction972)
                    expr30 = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode =  FUNCTION29.text + expr30 + ')' 
                    #action end

                    self.match(self.input, UP, None)


                elif alt21 == 2:
                    # treelesscss.g:273:4: ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                    pass 
                    self.match(self.input, N_PseudoFunction, self.FOLLOW_N_PseudoFunction_in_pseudoFunction985)

                    self.match(self.input, DOWN, None)
                    FUNCTION31=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction989)
                    self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudoFunction991)
                    self._state.following.append(self.FOLLOW_attribBody_in_pseudoFunction995)
                    attribBody32 = self.attribBody()

                    self._state.following.pop()
                    self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudoFunction999)
                    #action start
                    gencode =  FUNCTION31.text + '[' + attribBody32 + '])' 
                    #action end

                    self.match(self.input, UP, None)


                elif alt21 == 3:
                    # treelesscss.g:278:4: ^( N_PseudoFunction FUNCTION pseudo )
                    pass 
                    self.match(self.input, N_PseudoFunction, self.FOLLOW_N_PseudoFunction_in_pseudoFunction1010)

                    self.match(self.input, DOWN, None)
                    FUNCTION33=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction1014)
                    self._state.following.append(self.FOLLOW_pseudo_in_pseudoFunction1018)
                    pseudo34 = self.pseudo()

                    self._state.following.pop()
                    #action start
                    gencode =  FUNCTION33.text + pseudo34 + ')' 
                    #action end

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudoFunction"


    # $ANTLR start "attrib"
    # treelesscss.g:283:1: attrib returns [gencode] : ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        gencode = None

        attribBody35 = None


        try:
            try:
                # treelesscss.g:284:2: ( ^( N_Attrib attribBody ) )
                # treelesscss.g:284:4: ^( N_Attrib attribBody )
                pass 
                self.match(self.input, N_Attrib, self.FOLLOW_N_Attrib_in_attrib1038)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1042)
                attribBody35 = self.attribBody()

                self._state.following.pop()
                #action start
                gencode =  '[' + attribBody35 + ']' 
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attrib"


    # $ANTLR start "attribBody"
    # treelesscss.g:288:1: attribBody returns [gencode] : ( IDENT | ^( attribOper IDENT term ) );
    def attribBody(self, ):

        gencode = None

        IDENT36 = None
        IDENT37 = None
        attribOper38 = None

        term39 = None


        try:
            try:
                # treelesscss.g:289:2: ( IDENT | ^( attribOper IDENT term ) )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IDENT) :
                    alt22 = 1
                elif ((OPEQ <= LA22_0 <= SUBSTRINGMATCH)) :
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # treelesscss.g:289:4: IDENT
                    pass 
                    IDENT36=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1060)
                    #action start
                    gencode =  IDENT36.text 
                    #action end


                elif alt22 == 2:
                    # treelesscss.g:290:4: ^( attribOper IDENT term )
                    pass 
                    self._state.following.append(self.FOLLOW_attribOper_in_attribBody1070)
                    attribOper38 = self.attribOper()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    IDENT37=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1074)
                    self._state.following.append(self.FOLLOW_term_in_attribBody1078)
                    term39 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  IDENT37.text + attribOper38 + term39 
                    #action end

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attribBody"


    # $ANTLR start "attribOper"
    # treelesscss.g:295:10: fragment attribOper returns [gencode] : ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH );
    def attribOper(self, ):

        gencode = None

        OPEQ40 = None
        INCLUDES41 = None
        DASHMATCH42 = None
        PREFIXMATCH43 = None
        SUFFIXMATCH44 = None
        SUBSTRINGMATCH45 = None

        try:
            try:
                # treelesscss.g:296:2: ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH )
                alt23 = 6
                LA23 = self.input.LA(1)
                if LA23 == OPEQ:
                    alt23 = 1
                elif LA23 == INCLUDES:
                    alt23 = 2
                elif LA23 == DASHMATCH:
                    alt23 = 3
                elif LA23 == PREFIXMATCH:
                    alt23 = 4
                elif LA23 == SUFFIXMATCH:
                    alt23 = 5
                elif LA23 == SUBSTRINGMATCH:
                    alt23 = 6
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # treelesscss.g:296:4: OPEQ
                    pass 
                    OPEQ40=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_attribOper1100)
                    #action start
                    gencode =  OPEQ40.text 
                    #action end


                elif alt23 == 2:
                    # treelesscss.g:297:4: INCLUDES
                    pass 
                    INCLUDES41=self.match(self.input, INCLUDES, self.FOLLOW_INCLUDES_in_attribOper1109)
                    #action start
                    gencode =  INCLUDES41.text 
                    #action end


                elif alt23 == 3:
                    # treelesscss.g:298:4: DASHMATCH
                    pass 
                    DASHMATCH42=self.match(self.input, DASHMATCH, self.FOLLOW_DASHMATCH_in_attribOper1117)
                    #action start
                    gencode =  DASHMATCH42.text 
                    #action end


                elif alt23 == 4:
                    # treelesscss.g:299:4: PREFIXMATCH
                    pass 
                    PREFIXMATCH43=self.match(self.input, PREFIXMATCH, self.FOLLOW_PREFIXMATCH_in_attribOper1125)
                    #action start
                    gencode =  PREFIXMATCH43.text 
                    #action end


                elif alt23 == 5:
                    # treelesscss.g:300:4: SUFFIXMATCH
                    pass 
                    SUFFIXMATCH44=self.match(self.input, SUFFIXMATCH, self.FOLLOW_SUFFIXMATCH_in_attribOper1133)
                    #action start
                    gencode =  SUFFIXMATCH44.text 
                    #action end


                elif alt23 == 6:
                    # treelesscss.g:301:4: SUBSTRINGMATCH
                    pass 
                    SUBSTRINGMATCH45=self.match(self.input, SUBSTRINGMATCH, self.FOLLOW_SUBSTRINGMATCH_in_attribOper1141)
                    #action start
                    gencode =  SUBSTRINGMATCH45.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attribOper"


    # $ANTLR start "declarationset"
    # treelesscss.g:307:1: declarationset : ( N_Empty | ( declaration )+ );
    def declarationset(self, ):

        try:
            try:
                # treelesscss.g:308:2: ( N_Empty | ( declaration )+ )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == N_Empty) :
                    alt25 = 1
                elif (LA25_0 == N_Declaration) :
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # treelesscss.g:308:4: N_Empty
                    pass 
                    self.match(self.input, N_Empty, self.FOLLOW_N_Empty_in_declarationset1157)


                elif alt25 == 2:
                    # treelesscss.g:309:4: ( declaration )+
                    pass 
                    # treelesscss.g:309:4: ( declaration )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == N_Declaration) :
                            alt24 = 1


                        if alt24 == 1:
                            # treelesscss.g:309:4: declaration
                            pass 
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset1162)
                            self.declaration()

                            self._state.following.pop()


                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declarationset"


    # $ANTLR start "declaration"
    # treelesscss.g:313:1: declaration : ^( N_Declaration property ( expr )? ( prio )? ) ;
    def declaration(self, ):

        property46 = None

        expr47 = None


        try:
            try:
                # treelesscss.g:314:2: ( ^( N_Declaration property ( expr )? ( prio )? ) )
                # treelesscss.g:314:4: ^( N_Declaration property ( expr )? ( prio )? )
                pass 
                self.match(self.input, N_Declaration, self.FOLLOW_N_Declaration_in_declaration1176)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_property_in_declaration1180)
                property46 = self.property()

                self._state.following.pop()
                #action start
                propout = property46 +  ":";  
                #action end
                # treelesscss.g:316:3: ( expr )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == N_Space or LA26_0 == N_Term or LA26_0 == STRING or LA26_0 == URI or (COMMA <= LA26_0 <= IDENT) or LA26_0 == HASH or LA26_0 == SOLIDUS or LA26_0 == UNICODE_RANGE) :
                    alt26 = 1
                if alt26 == 1:
                    # treelesscss.g:317:5: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_declaration1193)
                    expr47 = self.expr()

                    self._state.following.pop()
                    #action start
                    propout += expr47
                    #action end



                # treelesscss.g:319:3: ( prio )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == IMPORTANT_SYM) :
                    alt27 = 1
                if alt27 == 1:
                    # treelesscss.g:320:5: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1211)
                    self.prio()

                    self._state.following.pop()
                    #action start
                    propout += ' !important'
                    #action end



                #action start
                     
                #TODO: Remove last semicolon in the declarationset (how?) ...
                self.writeln(propout + self.EOLSEMI);
                				
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
    # treelesscss.g:328:1: property returns [gencode] : IDENT ;
    def property(self, ):

        gencode = None

        IDENT48 = None

        try:
            try:
                # treelesscss.g:329:2: ( IDENT )
                # treelesscss.g:329:4: IDENT
                pass 
                IDENT48=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1241)
                #action start
                gencode =  IDENT48.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "property"


    # $ANTLR start "prio"
    # treelesscss.g:332:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        try:
            try:
                # treelesscss.g:333:2: ( IMPORTANT_SYM )
                # treelesscss.g:333:4: IMPORTANT_SYM
                pass 
                self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1256)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "prio"


    # $ANTLR start "expr"
    # treelesscss.g:337:1: expr returns [gencode] : ( ^( operator a= expr b= expr ) | term );
    def expr(self, ):

        gencode = None

        a = None

        b = None

        operator49 = None

        term50 = None


        try:
            try:
                # treelesscss.g:338:2: ( ^( operator a= expr b= expr ) | term )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == N_Space or LA28_0 == COMMA or LA28_0 == SOLIDUS) :
                    alt28 = 1
                elif (LA28_0 == N_Term or LA28_0 == STRING or LA28_0 == URI or LA28_0 == IDENT or LA28_0 == HASH or LA28_0 == UNICODE_RANGE) :
                    alt28 = 2
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # treelesscss.g:338:4: ^( operator a= expr b= expr )
                    pass 
                    self._state.following.append(self.FOLLOW_operator_in_expr1274)
                    operator49 = self.operator()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr1280)
                    a = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr1286)
                    b = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode =  a + operator49 + b 
                    #action end

                    self.match(self.input, UP, None)


                elif alt28 == 2:
                    # treelesscss.g:342:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_expr1298)
                    term50 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term50 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "expr"


    # $ANTLR start "operator"
    # treelesscss.g:345:10: fragment operator returns [gencode] : ( SOLIDUS | COMMA | N_Space );
    def operator(self, ):

        gencode = None

        SOLIDUS51 = None
        COMMA52 = None

        try:
            try:
                # treelesscss.g:346:2: ( SOLIDUS | COMMA | N_Space )
                alt29 = 3
                LA29 = self.input.LA(1)
                if LA29 == SOLIDUS:
                    alt29 = 1
                elif LA29 == COMMA:
                    alt29 = 2
                elif LA29 == N_Space:
                    alt29 = 3
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # treelesscss.g:346:4: SOLIDUS
                    pass 
                    SOLIDUS51=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1319)
                    #action start
                    gencode =  SOLIDUS51.text 
                    #action end


                elif alt29 == 2:
                    # treelesscss.g:347:4: COMMA
                    pass 
                    COMMA52=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1328)
                    #action start
                    gencode =  COMMA52.text 
                    #action end


                elif alt29 == 3:
                    # treelesscss.g:348:4: N_Space
                    pass 
                    self.match(self.input, N_Space, self.FOLLOW_N_Space_in_operator1337)
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
    # treelesscss.g:351:1: term returns [gencode] : ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE );
    def term(self, ):

        gencode = None

        STRING56 = None
        IDENT57 = None
        URI58 = None
        UNICODE_RANGE60 = None
        unaryOperator53 = None

        termnum54 = None

        termnum55 = None

        hexColor59 = None


        try:
            try:
                # treelesscss.g:352:2: ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE )
                alt30 = 7
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # treelesscss.g:352:4: ^( N_Term unaryOperator termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term1356)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_unaryOperator_in_term1360)
                    unaryOperator53 = self.unaryOperator()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_termnum_in_term1364)
                    termnum54 = self.termnum()

                    self._state.following.pop()
                    #action start
                    gencode =  ((unaryOperator53 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(unaryOperator53.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(unaryOperator53.start)
                        )] or [None])[0] + termnum54 
                    #action end

                    self.match(self.input, UP, None)


                elif alt30 == 2:
                    # treelesscss.g:356:4: ^( N_Term termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term1378)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_termnum_in_term1382)
                    termnum55 = self.termnum()

                    self._state.following.pop()
                    #action start
                    gencode =  termnum55 
                    #action end

                    self.match(self.input, UP, None)


                elif alt30 == 3:
                    # treelesscss.g:359:4: STRING
                    pass 
                    STRING56=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1396)
                    #action start
                    gencode =  STRING56.text 
                    #action end


                elif alt30 == 4:
                    # treelesscss.g:360:4: IDENT
                    pass 
                    IDENT57=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1404)
                    #action start
                    gencode =  IDENT57.text 
                    #action end


                elif alt30 == 5:
                    # treelesscss.g:361:4: URI
                    pass 
                    URI58=self.match(self.input, URI, self.FOLLOW_URI_in_term1413)
                    #action start
                    gencode =  URI58.text 
                    #action end


                elif alt30 == 6:
                    # treelesscss.g:362:4: hexColor
                    pass 
                    self._state.following.append(self.FOLLOW_hexColor_in_term1422)
                    hexColor59 = self.hexColor()

                    self._state.following.pop()
                    #action start
                    gencode =  ((hexColor59 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(hexColor59.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(hexColor59.start)
                        )] or [None])[0] 
                    #action end


                elif alt30 == 7:
                    # treelesscss.g:363:4: UNICODE_RANGE
                    pass 
                    UNICODE_RANGE60=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term1430)
                    #action start
                    gencode =  UNICODE_RANGE60.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "term"


    # $ANTLR start "termnum"
    # treelesscss.g:366:10: fragment termnum returns [gencode] : ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function );
    def termnum(self, ):

        gencode = None

        NUMBER61 = None
        PERCENTAGE62 = None
        LENGTH63 = None
        EMS64 = None
        EXS65 = None
        REMS66 = None
        CHS67 = None
        ANGLE68 = None
        TIME69 = None
        FREQ70 = None
        RESOLUTION71 = None
        VPORTLEN72 = None
        NTH73 = None
        function74 = None


        try:
            try:
                # treelesscss.g:367:2: ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function )
                alt31 = 14
                LA31 = self.input.LA(1)
                if LA31 == NUMBER:
                    alt31 = 1
                elif LA31 == PERCENTAGE:
                    alt31 = 2
                elif LA31 == LENGTH:
                    alt31 = 3
                elif LA31 == EMS:
                    alt31 = 4
                elif LA31 == EXS:
                    alt31 = 5
                elif LA31 == REMS:
                    alt31 = 6
                elif LA31 == CHS:
                    alt31 = 7
                elif LA31 == ANGLE:
                    alt31 = 8
                elif LA31 == TIME:
                    alt31 = 9
                elif LA31 == FREQ:
                    alt31 = 10
                elif LA31 == RESOLUTION:
                    alt31 = 11
                elif LA31 == VPORTLEN:
                    alt31 = 12
                elif LA31 == NTH:
                    alt31 = 13
                elif LA31 == N_Function:
                    alt31 = 14
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # treelesscss.g:367:4: NUMBER
                    pass 
                    NUMBER61=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_termnum1450)
                    #action start
                    gencode =  NUMBER61.text.strip() 
                    #action end


                elif alt31 == 2:
                    # treelesscss.g:368:4: PERCENTAGE
                    pass 
                    PERCENTAGE62=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_termnum1458)
                    #action start
                    gencode =  PERCENTAGE62.text.strip() 
                    #action end


                elif alt31 == 3:
                    # treelesscss.g:369:4: LENGTH
                    pass 
                    LENGTH63=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_termnum1466)
                    #action start
                    gencode =  LENGTH63.text.strip() 
                    #action end


                elif alt31 == 4:
                    # treelesscss.g:370:4: EMS
                    pass 
                    EMS64=self.match(self.input, EMS, self.FOLLOW_EMS_in_termnum1474)
                    #action start
                    gencode =  EMS64.text.strip() 
                    #action end


                elif alt31 == 5:
                    # treelesscss.g:371:4: EXS
                    pass 
                    EXS65=self.match(self.input, EXS, self.FOLLOW_EXS_in_termnum1483)
                    #action start
                    gencode =  EXS65.text.strip() 
                    #action end


                elif alt31 == 6:
                    # treelesscss.g:372:4: REMS
                    pass 
                    REMS66=self.match(self.input, REMS, self.FOLLOW_REMS_in_termnum1492)
                    #action start
                    gencode =  REMS66.text.strip() 
                    #action end


                elif alt31 == 7:
                    # treelesscss.g:373:4: CHS
                    pass 
                    CHS67=self.match(self.input, CHS, self.FOLLOW_CHS_in_termnum1501)
                    #action start
                    gencode =  CHS67.text.strip() 
                    #action end


                elif alt31 == 8:
                    # treelesscss.g:374:4: ANGLE
                    pass 
                    ANGLE68=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_termnum1510)
                    #action start
                    gencode =  ANGLE68.text.strip() 
                    #action end


                elif alt31 == 9:
                    # treelesscss.g:375:4: TIME
                    pass 
                    TIME69=self.match(self.input, TIME, self.FOLLOW_TIME_in_termnum1519)
                    #action start
                    gencode =  TIME69.text.strip() 
                    #action end


                elif alt31 == 10:
                    # treelesscss.g:376:4: FREQ
                    pass 
                    FREQ70=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_termnum1528)
                    #action start
                    gencode =  FREQ70.text.strip() 
                    #action end


                elif alt31 == 11:
                    # treelesscss.g:377:4: RESOLUTION
                    pass 
                    RESOLUTION71=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_termnum1537)
                    #action start
                    gencode =  RESOLUTION71.text.strip() 
                    #action end


                elif alt31 == 12:
                    # treelesscss.g:378:4: VPORTLEN
                    pass 
                    VPORTLEN72=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_termnum1545)
                    #action start
                    gencode =  VPORTLEN72.text.strip() 
                    #action end


                elif alt31 == 13:
                    # treelesscss.g:379:4: NTH
                    pass 
                    NTH73=self.match(self.input, NTH, self.FOLLOW_NTH_in_termnum1553)
                    #action start
                    gencode =  NTH73.text.strip() 
                    #action end


                elif alt31 == 14:
                    # treelesscss.g:380:4: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_termnum1562)
                    function74 = self.function()

                    self._state.following.pop()
                    #action start
                    gencode =  function74 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "termnum"

    class unaryOperator_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.unaryOperator_return, self).__init__()





    # $ANTLR start "unaryOperator"
    # treelesscss.g:384:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:385:2: ( MINUS | PLUS )
                # treelesscss.g:
                pass 
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
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

    # $ANTLR end "unaryOperator"


    # $ANTLR start "function"
    # treelesscss.g:390:1: function returns [gencode] : ^( N_Function fnct_name fnct_args ) ;
    def function(self, ):

        gencode = None

        fnct_name75 = None

        fnct_args76 = None


        try:
            try:
                # treelesscss.g:391:2: ( ^( N_Function fnct_name fnct_args ) )
                # treelesscss.g:391:4: ^( N_Function fnct_name fnct_args )
                pass 
                self.match(self.input, N_Function, self.FOLLOW_N_Function_in_function1600)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_fnct_name_in_function1604)
                fnct_name75 = self.fnct_name()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_fnct_args_in_function1608)
                fnct_args76 = self.fnct_args()

                self._state.following.pop()
                #action start
                gencode =  fnct_name75 + fnct_args76 + ')' 
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "function"


    # $ANTLR start "fnct_name"
    # treelesscss.g:397:1: fnct_name returns [gencode] : ^( FUNCTION ( IDENT | COLON | DOT )* ) ;
    def fnct_name(self, ):

        gencode = None

        IDENT77 = None
        COLON78 = None
        DOT79 = None
        FUNCTION80 = None

        try:
            try:
                # treelesscss.g:398:2: ( ^( FUNCTION ( IDENT | COLON | DOT )* ) )
                # treelesscss.g:398:4: ^( FUNCTION ( IDENT | COLON | DOT )* )
                pass 
                FUNCTION80=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1629)

                #action start
                prefix = list(); 
                #action end

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:399:3: ( IDENT | COLON | DOT )*
                    while True: #loop32
                        alt32 = 4
                        LA32 = self.input.LA(1)
                        if LA32 == IDENT:
                            alt32 = 1
                        elif LA32 == COLON:
                            alt32 = 2
                        elif LA32 == DOT:
                            alt32 = 3

                        if alt32 == 1:
                            # treelesscss.g:399:5: IDENT
                            pass 
                            IDENT77=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1638)
                            #action start
                            prefix.append(IDENT77.text); 
                            #action end


                        elif alt32 == 2:
                            # treelesscss.g:400:5: COLON
                            pass 
                            COLON78=self.match(self.input, COLON, self.FOLLOW_COLON_in_fnct_name1647)
                            #action start
                            prefix.append(COLON78.text); 
                            #action end


                        elif alt32 == 3:
                            # treelesscss.g:401:5: DOT
                            pass 
                            DOT79=self.match(self.input, DOT, self.FOLLOW_DOT_in_fnct_name1656)
                            #action start
                            prefix.append(DOT79.text); 
                            #action end


                        else:
                            break #loop32

                    self.match(self.input, UP, None)

                #action start
                gencode =  ''.join(prefix) + FUNCTION80.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "fnct_name"


    # $ANTLR start "fnct_args"
    # treelesscss.g:406:10: fragment fnct_args returns [gencode] : ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | ^( N_Expr expr ) );
    def fnct_args(self, ):

        gencode = None

        COMMA81 = None
        IDENT82 = None
        OPEQ83 = None
        a = None

        b = None

        expr84 = None

        expr85 = None


        try:
            try:
                # treelesscss.g:407:2: ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | ^( N_Expr expr ) )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 == COMMA:
                    alt33 = 1
                elif LA33 == OPEQ:
                    alt33 = 2
                elif LA33 == N_Expr:
                    alt33 = 3
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # treelesscss.g:407:4: ^( COMMA a= fnct_args b= fnct_args )
                    pass 
                    COMMA81=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1690)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1696)
                    a = self.fnct_args()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1702)
                    b = self.fnct_args()

                    self._state.following.pop()
                    #action start
                    gencode =  a + COMMA81.text + b 
                    #action end

                    self.match(self.input, UP, None)


                elif alt33 == 2:
                    # treelesscss.g:411:4: ^( OPEQ IDENT expr )
                    pass 
                    OPEQ83=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_args1713)

                    self.match(self.input, DOWN, None)
                    IDENT82=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_args1717)
                    self._state.following.append(self.FOLLOW_expr_in_fnct_args1721)
                    expr84 = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode =  IDENT82.text + OPEQ83.text + expr84 
                    #action end

                    self.match(self.input, UP, None)


                elif alt33 == 3:
                    # treelesscss.g:415:4: ^( N_Expr expr )
                    pass 
                    self.match(self.input, N_Expr, self.FOLLOW_N_Expr_in_fnct_args1734)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_fnct_args1738)
                    expr85 = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode =  expr85 
                    #action end

                    self.match(self.input, UP, None)



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





    # $ANTLR start "hexColor"
    # treelesscss.g:420:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:421:2: ( HASH )
                # treelesscss.g:421:4: HASH
                pass 
                self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1755)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"


    # Delegated rules


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\22\1\2\5\uffff\1\14\2\uffff"
        )

    DFA30_max = DFA.unpack(
        u"\1\101\1\2\5\uffff\1\102\2\uffff"
        )

    DFA30_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\1\7\1\uffff\1\1\1\2"
        )

    DFA30_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA30_transition = [
        DFA.unpack(u"\1\1\2\uffff\1\2\2\uffff\1\4\4\uffff\1\3\11\uffff\1"
        u"\5\31\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\27\uffff\1\11\1\10\17\uffff\14\11\1\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet61 = frozenset([3, 7, 23, 25, 33, 34, 35])
    FOLLOW_imports_in_styleSheet79 = frozenset([3, 7, 23, 25, 33, 34, 35])
    FOLLOW_body_in_styleSheet91 = frozenset([3, 7, 25, 33, 34, 35])
    FOLLOW_CHARSET_SYM_in_charSet115 = frozenset([2])
    FOLLOW_STRING_in_charSet117 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports144 = frozenset([2])
    FOLLOW_importUrl_in_imports152 = frozenset([3, 5])
    FOLLOW_media_query_in_imports164 = frozenset([3, 5])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body210 = frozenset([1])
    FOLLOW_media_in_body216 = frozenset([1])
    FOLLOW_page_in_body223 = frozenset([1])
    FOLLOW_fontface_in_body230 = frozenset([1])
    FOLLOW_keyframes_in_body236 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media254 = frozenset([2])
    FOLLOW_media_query_in_media267 = frozenset([3, 5, 7, 25, 33, 34, 35])
    FOLLOW_body_in_media286 = frozenset([3, 7, 25, 33, 34, 35])
    FOLLOW_N_MediaQuery_in_media_query314 = frozenset([2])
    FOLLOW_media_stmt_in_media_query326 = frozenset([3, 6, 29])
    FOLLOW_media_expr_in_media_query334 = frozenset([3, 6, 29])
    FOLLOW_IDENT_in_media_stmt360 = frozenset([1])
    FOLLOW_N_MediaExpr_in_media_expr376 = frozenset([2])
    FOLLOW_media_stmt_in_media_expr383 = frozenset([3, 15, 18, 21, 24, 28, 29, 39, 52, 65])
    FOLLOW_expr_in_media_expr396 = frozenset([3])
    FOLLOW_FONTFACE_SYM_in_fontface428 = frozenset([2])
    FOLLOW_declarationset_in_fontface438 = frozenset([3])
    FOLLOW_PAGE_SYM_in_page460 = frozenset([2])
    FOLLOW_pseudoPage_in_page474 = frozenset([11, 14])
    FOLLOW_declarationset_in_page491 = frozenset([3])
    FOLLOW_IDENT_in_pseudoPage515 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes535 = frozenset([2])
    FOLLOW_IDENT_in_keyframes537 = frozenset([3, 8])
    FOLLOW_keyframes_block_in_keyframes547 = frozenset([3, 8])
    FOLLOW_N_KeyframeBlock_in_keyframes_block567 = frozenset([2])
    FOLLOW_keyframe_selector_in_keyframes_block576 = frozenset([9, 11, 14])
    FOLLOW_declarationset_in_keyframes_block599 = frozenset([3])
    FOLLOW_M_KeyframeSelector_in_keyframe_selector622 = frozenset([2])
    FOLLOW_IDENT_in_keyframe_selector628 = frozenset([3])
    FOLLOW_PERCENTAGE_in_keyframe_selector637 = frozenset([3])
    FOLLOW_N_RuleSet_in_ruleSet661 = frozenset([2])
    FOLLOW_selector_list_in_ruleSet673 = frozenset([10, 11, 14])
    FOLLOW_declarationset_in_ruleSet691 = frozenset([3])
    FOLLOW_N_Selector_in_selector_list713 = frozenset([2])
    FOLLOW_selector_in_selector_list717 = frozenset([3])
    FOLLOW_simpleSelector_in_selector737 = frozenset([1, 13, 16, 29, 37, 38, 39, 42])
    FOLLOW_combinator_in_selector746 = frozenset([13, 16, 29, 37, 38, 39, 42])
    FOLLOW_simpleSelector_in_selector754 = frozenset([1, 13, 16, 29, 37, 38, 39, 42])
    FOLLOW_PLUS_in_combinator779 = frozenset([1])
    FOLLOW_GREATER_in_combinator788 = frozenset([1])
    FOLLOW_IDENT_in_simpleSelector813 = frozenset([1])
    FOLLOW_STAR_in_simpleSelector822 = frozenset([1])
    FOLLOW_HASH_in_simpleSelector831 = frozenset([1])
    FOLLOW_pseudo_in_simpleSelector840 = frozenset([1])
    FOLLOW_attrib_in_simpleSelector848 = frozenset([1])
    FOLLOW_N_Pseudo_in_pseudo867 = frozenset([2])
    FOLLOW_COLON_in_pseudo873 = frozenset([29, 31])
    FOLLOW_COLON_in_pseudo888 = frozenset([29])
    FOLLOW_IDENT_in_pseudo900 = frozenset([3])
    FOLLOW_N_Pseudo_in_pseudo912 = frozenset([2])
    FOLLOW_COLON_in_pseudo918 = frozenset([17, 31])
    FOLLOW_COLON_in_pseudo933 = frozenset([17, 31])
    FOLLOW_pseudoFunction_in_pseudo945 = frozenset([3])
    FOLLOW_N_PseudoFunction_in_pseudoFunction964 = frozenset([2])
    FOLLOW_FUNCTION_in_pseudoFunction968 = frozenset([15, 18, 21, 24, 28, 29, 39, 52, 65])
    FOLLOW_expr_in_pseudoFunction972 = frozenset([3])
    FOLLOW_N_PseudoFunction_in_pseudoFunction985 = frozenset([2])
    FOLLOW_FUNCTION_in_pseudoFunction989 = frozenset([41])
    FOLLOW_LBRACKET_in_pseudoFunction991 = frozenset([29, 45, 46, 47, 48, 49, 50])
    FOLLOW_attribBody_in_pseudoFunction995 = frozenset([44])
    FOLLOW_RBRACKET_in_pseudoFunction999 = frozenset([3])
    FOLLOW_N_PseudoFunction_in_pseudoFunction1010 = frozenset([2])
    FOLLOW_FUNCTION_in_pseudoFunction1014 = frozenset([16])
    FOLLOW_pseudo_in_pseudoFunction1018 = frozenset([3])
    FOLLOW_N_Attrib_in_attrib1038 = frozenset([2])
    FOLLOW_attribBody_in_attrib1042 = frozenset([3])
    FOLLOW_IDENT_in_attribBody1060 = frozenset([1])
    FOLLOW_attribOper_in_attribBody1070 = frozenset([2])
    FOLLOW_IDENT_in_attribBody1074 = frozenset([15, 18, 21, 24, 28, 29, 39, 52, 65])
    FOLLOW_term_in_attribBody1078 = frozenset([3])
    FOLLOW_OPEQ_in_attribOper1100 = frozenset([1])
    FOLLOW_INCLUDES_in_attribOper1109 = frozenset([1])
    FOLLOW_DASHMATCH_in_attribOper1117 = frozenset([1])
    FOLLOW_PREFIXMATCH_in_attribOper1125 = frozenset([1])
    FOLLOW_SUFFIXMATCH_in_attribOper1133 = frozenset([1])
    FOLLOW_SUBSTRINGMATCH_in_attribOper1141 = frozenset([1])
    FOLLOW_N_Empty_in_declarationset1157 = frozenset([1])
    FOLLOW_declaration_in_declarationset1162 = frozenset([1, 11, 14])
    FOLLOW_N_Declaration_in_declaration1176 = frozenset([2])
    FOLLOW_property_in_declaration1180 = frozenset([3, 15, 18, 21, 24, 28, 29, 39, 51, 52, 65])
    FOLLOW_expr_in_declaration1193 = frozenset([3, 51])
    FOLLOW_prio_in_declaration1211 = frozenset([3])
    FOLLOW_IDENT_in_property1241 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1256 = frozenset([1])
    FOLLOW_operator_in_expr1274 = frozenset([2])
    FOLLOW_expr_in_expr1280 = frozenset([15, 18, 21, 24, 28, 29, 39, 52, 65])
    FOLLOW_expr_in_expr1286 = frozenset([3])
    FOLLOW_term_in_expr1298 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator1319 = frozenset([1])
    FOLLOW_COMMA_in_operator1328 = frozenset([1])
    FOLLOW_N_Space_in_operator1337 = frozenset([1])
    FOLLOW_N_Term_in_term1356 = frozenset([2])
    FOLLOW_unaryOperator_in_term1360 = frozenset([12, 36, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])
    FOLLOW_termnum_in_term1364 = frozenset([3])
    FOLLOW_N_Term_in_term1378 = frozenset([2])
    FOLLOW_termnum_in_term1382 = frozenset([3])
    FOLLOW_STRING_in_term1396 = frozenset([1])
    FOLLOW_IDENT_in_term1404 = frozenset([1])
    FOLLOW_URI_in_term1413 = frozenset([1])
    FOLLOW_hexColor_in_term1422 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term1430 = frozenset([1])
    FOLLOW_NUMBER_in_termnum1450 = frozenset([1])
    FOLLOW_PERCENTAGE_in_termnum1458 = frozenset([1])
    FOLLOW_LENGTH_in_termnum1466 = frozenset([1])
    FOLLOW_EMS_in_termnum1474 = frozenset([1])
    FOLLOW_EXS_in_termnum1483 = frozenset([1])
    FOLLOW_REMS_in_termnum1492 = frozenset([1])
    FOLLOW_CHS_in_termnum1501 = frozenset([1])
    FOLLOW_ANGLE_in_termnum1510 = frozenset([1])
    FOLLOW_TIME_in_termnum1519 = frozenset([1])
    FOLLOW_FREQ_in_termnum1528 = frozenset([1])
    FOLLOW_RESOLUTION_in_termnum1537 = frozenset([1])
    FOLLOW_VPORTLEN_in_termnum1545 = frozenset([1])
    FOLLOW_NTH_in_termnum1553 = frozenset([1])
    FOLLOW_function_in_termnum1562 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_N_Function_in_function1600 = frozenset([2])
    FOLLOW_fnct_name_in_function1604 = frozenset([19, 28, 45])
    FOLLOW_fnct_args_in_function1608 = frozenset([3])
    FOLLOW_FUNCTION_in_fnct_name1629 = frozenset([2])
    FOLLOW_IDENT_in_fnct_name1638 = frozenset([3, 29, 31, 40])
    FOLLOW_COLON_in_fnct_name1647 = frozenset([3, 29, 31, 40])
    FOLLOW_DOT_in_fnct_name1656 = frozenset([3, 29, 31, 40])
    FOLLOW_COMMA_in_fnct_args1690 = frozenset([2])
    FOLLOW_fnct_args_in_fnct_args1696 = frozenset([19, 28, 45])
    FOLLOW_fnct_args_in_fnct_args1702 = frozenset([3])
    FOLLOW_OPEQ_in_fnct_args1713 = frozenset([2])
    FOLLOW_IDENT_in_fnct_args1717 = frozenset([15, 18, 21, 24, 28, 29, 39, 52, 65])
    FOLLOW_expr_in_fnct_args1721 = frozenset([3])
    FOLLOW_N_Expr_in_fnct_args1734 = frozenset([2])
    FOLLOW_expr_in_fnct_args1738 = frozenset([3])
    FOLLOW_HASH_in_hexColor1755 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
