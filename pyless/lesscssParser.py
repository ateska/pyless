# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-12-04 00:36:14

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=45
UNICODE_RANGE=67
STAR=44
EOF=-1
MEDIA_SYM=26
LBRACKET=43
INCLUDES=48
RPAREN=33
NAME=75
GREATER=40
ESCAPE=72
DIMENSION=108
STRINGESC=106
NL=109
COMMENT=103
D=80
E=81
F=82
G=83
A=77
RBRACE=28
B=78
C=79
L=88
IMPORT_SYM=24
NMCHAR=74
M=89
SUBSTRINGMATCH=52
N=90
O=91
H=84
I=85
J=86
NUMBER=55
K=87
U=97
T=96
W=99
V=98
Q=93
P=92
S=95
CDO=104
R=94
CDC=105
Y=101
PERCENTAGE=37
URL=76
X=100
Z=102
URI=25
PAGE_SYM=35
WS=107
DASHMATCH=49
EMS=57
N_Less_VarDef=20
N_PseudoFunction=17
N_RuleSet=7
NONASCII=70
N_MediaQuery=5
N_Expr=19
N_Selector=10
LBRACE=27
LPAREN=31
LENGTH=56
IMPORTANT_SYM=53
N_Function=12
TIME=62
KEYFRAMES_SYM=36
COMMA=29
N_StyleSheet=4
IDENT=30
PLUS=39
FREQ=63
RBRACKET=46
DOT=42
VPORTLEN=65
CHARSET_SYM=21
ANGLE=61
REMS=59
HASH=41
HEXCHAR=69
RESOLUTION=64
PREFIXMATCH=50
MINUS=68
N_Pseudo=16
SOLIDUS=54
SEMI=23
N_Empty=14
UNICODE=71
CHS=60
COLON=32
NMSTART=73
N_Declaration=11
FONTFACE_SYM=34
OPEQ=47
N_Term=18
EXS=58
M_KeyframeSelector=9
N_Space=15
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=51
LESS_VARNAME=38
NTH=66
STRING=22

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Space", "N_Pseudo", "N_PseudoFunction", "N_Term", "N_Expr", 
    "N_Less_VarDef", "CHARSET_SYM", "STRING", "SEMI", "IMPORT_SYM", "URI", 
    "MEDIA_SYM", "LBRACE", "RBRACE", "COMMA", "IDENT", "LPAREN", "COLON", 
    "RPAREN", "FONTFACE_SYM", "PAGE_SYM", "KEYFRAMES_SYM", "PERCENTAGE", 
    "LESS_VARNAME", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "STAR", 
    "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", "PREFIXMATCH", 
    "SUFFIXMATCH", "SUBSTRINGMATCH", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "LENGTH", "EMS", "EXS", "REMS", "CHS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
    "VPORTLEN", "NTH", "UNICODE_RANGE", "MINUS", "HEXCHAR", "NONASCII", 
    "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", "URL", "A", "B", "C", 
    "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", "CDO", "CDC", 
    "STRINGESC", "WS", "DIMENSION", "NL"
]




class lesscssParser(Parser):
    grammarFileName = "lesscss.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(lesscssParser, self).__init__(input, state, *args, **kwargs)

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class styleSheet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.styleSheet_return, self).__init__()

            self.tree = None




    # $ANTLR start "styleSheet"
    # lesscss.g:69:1: styleSheet : ( charSet )? ( imports )* ( body )* EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) ;
    def styleSheet(self, ):

        retval = self.styleSheet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF4 = None
        charSet1 = None

        imports2 = None

        body3 = None


        EOF4_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_body = RewriteRuleSubtreeStream(self._adaptor, "rule body")
        stream_charSet = RewriteRuleSubtreeStream(self._adaptor, "rule charSet")
        stream_imports = RewriteRuleSubtreeStream(self._adaptor, "rule imports")
        try:
            try:
                # lesscss.g:70:2: ( ( charSet )? ( imports )* ( body )* EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) )
                # lesscss.g:70:4: ( charSet )? ( imports )* ( body )* EOF
                pass 
                # lesscss.g:70:4: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:70:4: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet147)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:71:4: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:71:4: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet153)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                # lesscss.g:72:4: ( body )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MEDIA_SYM or LA3_0 == IDENT or LA3_0 == COLON or (FONTFACE_SYM <= LA3_0 <= KEYFRAMES_SYM) or LA3_0 == LESS_VARNAME or (HASH <= LA3_0 <= STAR)) :
                        alt3 = 1


                    if alt3 == 1:
                        # lesscss.g:72:4: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_styleSheet159)
                        body3 = self.body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_body.add(body3.tree)


                    else:
                        break #loop3
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet165) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: body, charSet, imports
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 74:3: -> ^( N_StyleSheet ( charSet )? ( imports )* ( body )* )
                    # lesscss.g:74:6: ^( N_StyleSheet ( charSet )? ( imports )* ( body )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:74:21: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:74:30: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:74:39: ( body )*
                    while stream_body.hasNext():
                        self._adaptor.addChild(root_1, stream_body.nextTree())


                    stream_body.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "styleSheet"

    class charSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.charSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "charSet"
    # lesscss.g:80:1: charSet : CHARSET_SYM STRING SEMI ;
    def charSet(self, ):

        retval = self.charSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHARSET_SYM5 = None
        STRING6 = None
        SEMI7 = None

        CHARSET_SYM5_tree = None
        STRING6_tree = None
        SEMI7_tree = None

        try:
            try:
                # lesscss.g:81:2: ( CHARSET_SYM STRING SEMI )
                # lesscss.g:81:4: CHARSET_SYM STRING SEMI
                pass 
                root_0 = self._adaptor.nil()

                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet197)
                if self._state.backtracking == 0:

                    CHARSET_SYM5_tree = self._adaptor.createWithPayload(CHARSET_SYM5)
                    root_0 = self._adaptor.becomeRoot(CHARSET_SYM5_tree, root_0)

                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet200)
                if self._state.backtracking == 0:

                    STRING6_tree = self._adaptor.createWithPayload(STRING6)
                    self._adaptor.addChild(root_0, STRING6_tree)

                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet202)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "charSet"

    class imports_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.imports_return, self).__init__()

            self.tree = None




    # $ANTLR start "imports"
    # lesscss.g:87:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI ;
    def imports(self, ):

        retval = self.imports_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT_SYM8 = None
        SEMI11 = None
        importUrl9 = None

        media_query_list10 = None


        IMPORT_SYM8_tree = None
        SEMI11_tree = None

        try:
            try:
                # lesscss.g:88:2: ( IMPORT_SYM importUrl ( media_query_list )? SEMI )
                # lesscss.g:88:4: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports217)
                if self._state.backtracking == 0:

                    IMPORT_SYM8_tree = self._adaptor.createWithPayload(IMPORT_SYM8)
                    root_0 = self._adaptor.becomeRoot(IMPORT_SYM8_tree, root_0)

                self._state.following.append(self.FOLLOW_importUrl_in_imports220)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, importUrl9.tree)
                # lesscss.g:88:26: ( media_query_list )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((IDENT <= LA4_0 <= LPAREN)) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:88:26: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports222)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports225)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "imports"

    class importUrl_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.importUrl_return, self).__init__()

            self.tree = None




    # $ANTLR start "importUrl"
    # lesscss.g:91:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:92:2: ( STRING | URI )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set12 = self.input.LT(1)
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set12))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importUrl"

    class body_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.body_return, self).__init__()

            self.tree = None




    # $ANTLR start "body"
    # lesscss.g:100:1: body : ( ruleSet | media | page | fontface | keyframes | less_variable_def );
    def body(self, ):

        retval = self.body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet13 = None

        media14 = None

        page15 = None

        fontface16 = None

        keyframes17 = None

        less_variable_def18 = None



        try:
            try:
                # lesscss.g:101:2: ( ruleSet | media | page | fontface | keyframes | less_variable_def )
                alt5 = 6
                LA5 = self.input.LA(1)
                if LA5 == IDENT or LA5 == COLON or LA5 == HASH or LA5 == DOT or LA5 == LBRACKET or LA5 == STAR:
                    alt5 = 1
                elif LA5 == MEDIA_SYM:
                    alt5 = 2
                elif LA5 == PAGE_SYM:
                    alt5 = 3
                elif LA5 == FONTFACE_SYM:
                    alt5 = 4
                elif LA5 == KEYFRAMES_SYM:
                    alt5 = 5
                elif LA5 == LESS_VARNAME:
                    alt5 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # lesscss.g:101:4: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_body257)
                    ruleSet13 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet13.tree)


                elif alt5 == 2:
                    # lesscss.g:102:4: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_body262)
                    media14 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media14.tree)


                elif alt5 == 3:
                    # lesscss.g:103:4: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_body267)
                    page15 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page15.tree)


                elif alt5 == 4:
                    # lesscss.g:104:4: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_body272)
                    fontface16 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface16.tree)


                elif alt5 == 5:
                    # lesscss.g:105:4: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_body277)
                    keyframes17 = self.keyframes()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, keyframes17.tree)


                elif alt5 == 6:
                    # lesscss.g:106:4: less_variable_def
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_less_variable_def_in_body282)
                    less_variable_def18 = self.less_variable_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, less_variable_def18.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "body"

    class media_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_return, self).__init__()

            self.tree = None




    # $ANTLR start "media"
    # lesscss.g:114:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( body )* RBRACE ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM19 = None
        LBRACE21 = None
        RBRACE23 = None
        media_query_list20 = None

        body22 = None


        MEDIA_SYM19_tree = None
        LBRACE21_tree = None
        RBRACE23_tree = None

        try:
            try:
                # lesscss.g:115:2: ( MEDIA_SYM ( media_query_list )? LBRACE ( body )* RBRACE )
                # lesscss.g:115:4: MEDIA_SYM ( media_query_list )? LBRACE ( body )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                MEDIA_SYM19=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media301)
                if self._state.backtracking == 0:

                    MEDIA_SYM19_tree = self._adaptor.createWithPayload(MEDIA_SYM19)
                    root_0 = self._adaptor.becomeRoot(MEDIA_SYM19_tree, root_0)

                # lesscss.g:115:15: ( media_query_list )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((IDENT <= LA6_0 <= LPAREN)) :
                    alt6 = 1
                if alt6 == 1:
                    # lesscss.g:115:15: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media304)
                    media_query_list20 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list20.tree)



                LBRACE21=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media309)
                # lesscss.g:117:4: ( body )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == MEDIA_SYM or LA7_0 == IDENT or LA7_0 == COLON or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM) or LA7_0 == LESS_VARNAME or (HASH <= LA7_0 <= STAR)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:117:4: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_media315)
                        body22 = self.body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, body22.tree)


                    else:
                        break #loop7
                RBRACE23=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media324)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media"

    class media_query_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query_list"
    # lesscss.g:124:1: media_query_list : media_query ( COMMA media_query )* -> ( ^( N_MediaQuery media_query ) )+ ;
    def media_query_list(self, ):

        retval = self.media_query_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA25 = None
        media_query24 = None

        media_query26 = None


        COMMA25_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_media_query = RewriteRuleSubtreeStream(self._adaptor, "rule media_query")
        try:
            try:
                # lesscss.g:125:2: ( media_query ( COMMA media_query )* -> ( ^( N_MediaQuery media_query ) )+ )
                # lesscss.g:125:4: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list339)
                media_query24 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query24.tree)
                # lesscss.g:125:16: ( COMMA media_query )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # lesscss.g:125:17: COMMA media_query
                        pass 
                        COMMA25=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list342) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA25)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list344)
                        media_query26 = self.media_query()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_media_query.add(media_query26.tree)


                    else:
                        break #loop8

                # AST Rewrite
                # elements: media_query
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 126:3: -> ( ^( N_MediaQuery media_query ) )+
                    # lesscss.g:126:6: ( ^( N_MediaQuery media_query ) )+
                    if not (stream_media_query.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_media_query.hasNext():
                        # lesscss.g:126:6: ^( N_MediaQuery media_query )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaQuery, "N_MediaQuery"), root_1)

                        self._adaptor.addChild(root_1, stream_media_query.nextTree())

                        self._adaptor.addChild(root_0, root_1)


                    stream_media_query.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media_query_list"

    class media_query_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query"
    # lesscss.g:131:1: media_query : ( media_stmt | media_expr )+ ;
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        media_stmt27 = None

        media_expr28 = None



        try:
            try:
                # lesscss.g:132:2: ( ( media_stmt | media_expr )+ )
                # lesscss.g:132:4: ( media_stmt | media_expr )+
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:132:4: ( media_stmt | media_expr )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 3
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENT) :
                        alt9 = 1
                    elif (LA9_0 == LPAREN) :
                        alt9 = 2


                    if alt9 == 1:
                        # lesscss.g:132:6: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query373)
                        media_stmt27 = self.media_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_stmt27.tree)


                    elif alt9 == 2:
                        # lesscss.g:132:19: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query377)
                        media_expr28 = self.media_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_expr28.tree)


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media_query"

    class media_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_stmt"
    # lesscss.g:135:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT29 = None

        IDENT29_tree = None

        try:
            try:
                # lesscss.g:136:2: ( IDENT )
                # lesscss.g:136:4: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT29=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt391)
                if self._state.backtracking == 0:

                    IDENT29_tree = self._adaptor.createWithPayload(IDENT29)
                    self._adaptor.addChild(root_0, IDENT29_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media_stmt"

    class media_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_expr"
    # lesscss.g:139:1: media_expr : LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN30 = None
        COLON32 = None
        RPAREN34 = None
        media_stmt31 = None

        expr33 = None


        LPAREN30_tree = None
        COLON32_tree = None
        RPAREN34_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_media_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule media_stmt")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:140:2: ( LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) )
                # lesscss.g:140:4: LPAREN media_stmt ( COLON expr )? RPAREN
                pass 
                LPAREN30=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr402) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN30)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr404)
                media_stmt31 = self.media_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_stmt.add(media_stmt31.tree)
                # lesscss.g:140:22: ( COLON expr )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == COLON) :
                    alt10 = 1
                if alt10 == 1:
                    # lesscss.g:140:24: COLON expr
                    pass 
                    COLON32=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr408) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON32)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr410)
                    expr33 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr33.tree)



                RPAREN34=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr415) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN34)

                # AST Rewrite
                # elements: expr, media_stmt
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 141:3: -> ^( N_MediaExpr media_stmt ( expr )? )
                    # lesscss.g:141:6: ^( N_MediaExpr media_stmt ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_stmt.nextTree())
                    # lesscss.g:141:31: ( expr )?
                    if stream_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_expr.nextTree())


                    stream_expr.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media_expr"

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:148:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM35 = None
        LBRACE36 = None
        RBRACE38 = None
        declarationset37 = None


        FONTFACE_SYM35_tree = None
        LBRACE36_tree = None
        RBRACE38_tree = None

        try:
            try:
                # lesscss.g:149:2: ( FONTFACE_SYM LBRACE declarationset RBRACE )
                # lesscss.g:149:4: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                FONTFACE_SYM35=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface444)
                if self._state.backtracking == 0:

                    FONTFACE_SYM35_tree = self._adaptor.createWithPayload(FONTFACE_SYM35)
                    root_0 = self._adaptor.becomeRoot(FONTFACE_SYM35_tree, root_0)

                LBRACE36=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface447)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface450)
                declarationset37 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset37.tree)
                RBRACE38=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface452)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fontface"

    class page_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.page_return, self).__init__()

            self.tree = None




    # $ANTLR start "page"
    # lesscss.g:155:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM39 = None
        LBRACE41 = None
        RBRACE43 = None
        pseudoPage40 = None

        declarationset42 = None


        PAGE_SYM39_tree = None
        LBRACE41_tree = None
        RBRACE43_tree = None

        try:
            try:
                # lesscss.g:156:2: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE )
                # lesscss.g:156:4: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                PAGE_SYM39=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page467)
                if self._state.backtracking == 0:

                    PAGE_SYM39_tree = self._adaptor.createWithPayload(PAGE_SYM39)
                    root_0 = self._adaptor.becomeRoot(PAGE_SYM39_tree, root_0)

                # lesscss.g:156:14: ( pseudoPage )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    alt11 = 1
                if alt11 == 1:
                    # lesscss.g:156:14: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page470)
                    pseudoPage40 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudoPage40.tree)



                LBRACE41=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page473)
                self._state.following.append(self.FOLLOW_declarationset_in_page476)
                declarationset42 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset42.tree)
                RBRACE43=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page478)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "page"

    class pseudoPage_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudoPage_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudoPage"
    # lesscss.g:159:1: pseudoPage : COLON a= IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON44 = None

        a_tree = None
        COLON44_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:160:2: ( COLON a= IDENT -> IDENT )
                # lesscss.g:160:4: COLON a= IDENT
                pass 
                COLON44=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage490) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON44)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage494) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(a)
                if self._state.backtracking == 0:
                    a.setText(':' + a.getText()); 


                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 162:3: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudoPage"

    class keyframes_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.keyframes_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyframes"
    # lesscss.g:169:1: keyframes : KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE ;
    def keyframes(self, ):

        retval = self.keyframes_return()
        retval.start = self.input.LT(1)

        root_0 = None

        KEYFRAMES_SYM45 = None
        IDENT46 = None
        LBRACE47 = None
        RBRACE49 = None
        keyframes_block48 = None


        KEYFRAMES_SYM45_tree = None
        IDENT46_tree = None
        LBRACE47_tree = None
        RBRACE49_tree = None

        try:
            try:
                # lesscss.g:170:2: ( KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE )
                # lesscss.g:170:4: KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                KEYFRAMES_SYM45=self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes520)
                if self._state.backtracking == 0:

                    KEYFRAMES_SYM45_tree = self._adaptor.createWithPayload(KEYFRAMES_SYM45)
                    root_0 = self._adaptor.becomeRoot(KEYFRAMES_SYM45_tree, root_0)

                IDENT46=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes523)
                if self._state.backtracking == 0:

                    IDENT46_tree = self._adaptor.createWithPayload(IDENT46)
                    self._adaptor.addChild(root_0, IDENT46_tree)

                LBRACE47=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes525)
                # lesscss.g:170:33: ( keyframes_block )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == IDENT or LA12_0 == PERCENTAGE) :
                        alt12 = 1


                    if alt12 == 1:
                        # lesscss.g:170:33: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes528)
                        keyframes_block48 = self.keyframes_block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, keyframes_block48.tree)


                    else:
                        break #loop12
                RBRACE49=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes531)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "keyframes"

    class keyframes_block_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.keyframes_block_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyframes_block"
    # lesscss.g:173:1: keyframes_block : keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) ;
    def keyframes_block(self, ):

        retval = self.keyframes_block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA51 = None
        LBRACE53 = None
        RBRACE55 = None
        keyframe_selector50 = None

        keyframe_selector52 = None

        declarationset54 = None


        COMMA51_tree = None
        LBRACE53_tree = None
        RBRACE55_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_keyframe_selector = RewriteRuleSubtreeStream(self._adaptor, "rule keyframe_selector")
        try:
            try:
                # lesscss.g:174:2: ( keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) )
                # lesscss.g:174:4: keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block543)
                keyframe_selector50 = self.keyframe_selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_keyframe_selector.add(keyframe_selector50.tree)
                # lesscss.g:174:22: ( COMMA keyframe_selector )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == COMMA) :
                        alt13 = 1


                    if alt13 == 1:
                        # lesscss.g:174:24: COMMA keyframe_selector
                        pass 
                        COMMA51=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keyframes_block547) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA51)
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block549)
                        keyframe_selector52 = self.keyframe_selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_keyframe_selector.add(keyframe_selector52.tree)


                    else:
                        break #loop13
                LBRACE53=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes_block554) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE53)
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block556)
                declarationset54 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset54.tree)
                RBRACE55=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes_block558) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE55)

                # AST Rewrite
                # elements: keyframe_selector, declarationset
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 175:3: -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    # lesscss.g:175:6: ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_KeyframeBlock, "N_KeyframeBlock"), root_1)

                    # lesscss.g:175:24: ( ^( M_KeyframeSelector keyframe_selector ) )+
                    if not (stream_keyframe_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_keyframe_selector.hasNext():
                        # lesscss.g:175:24: ^( M_KeyframeSelector keyframe_selector )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(M_KeyframeSelector, "M_KeyframeSelector"), root_2)

                        self._adaptor.addChild(root_2, stream_keyframe_selector.nextTree())

                        self._adaptor.addChild(root_1, root_2)


                    stream_keyframe_selector.reset()
                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "keyframes_block"

    class keyframe_selector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.keyframe_selector_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyframe_selector"
    # lesscss.g:179:1: keyframe_selector : ( IDENT | PERCENTAGE ) ;
    def keyframe_selector(self, ):

        retval = self.keyframe_selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set56 = None

        set56_tree = None

        try:
            try:
                # lesscss.g:180:2: ( ( IDENT | PERCENTAGE ) )
                # lesscss.g:180:4: ( IDENT | PERCENTAGE )
                pass 
                root_0 = self._adaptor.nil()

                set56 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == PERCENTAGE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set56))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "keyframe_selector"

    class less_variable_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.less_variable_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "less_variable_def"
    # lesscss.g:187:1: less_variable_def : LESS_VARNAME COLON term SEMI -> ^( N_Less_VarDef LESS_VARNAME term ) ;
    def less_variable_def(self, ):

        retval = self.less_variable_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LESS_VARNAME57 = None
        COLON58 = None
        SEMI60 = None
        term59 = None


        LESS_VARNAME57_tree = None
        COLON58_tree = None
        SEMI60_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_LESS_VARNAME = RewriteRuleTokenStream(self._adaptor, "token LESS_VARNAME")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_term = RewriteRuleSubtreeStream(self._adaptor, "rule term")
        try:
            try:
                # lesscss.g:188:2: ( LESS_VARNAME COLON term SEMI -> ^( N_Less_VarDef LESS_VARNAME term ) )
                # lesscss.g:188:4: LESS_VARNAME COLON term SEMI
                pass 
                LESS_VARNAME57=self.match(self.input, LESS_VARNAME, self.FOLLOW_LESS_VARNAME_in_less_variable_def611) 
                if self._state.backtracking == 0:
                    stream_LESS_VARNAME.add(LESS_VARNAME57)
                COLON58=self.match(self.input, COLON, self.FOLLOW_COLON_in_less_variable_def613) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON58)
                self._state.following.append(self.FOLLOW_term_in_less_variable_def615)
                term59 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_term.add(term59.tree)
                SEMI60=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_less_variable_def617) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI60)

                # AST Rewrite
                # elements: term, LESS_VARNAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 189:3: -> ^( N_Less_VarDef LESS_VARNAME term )
                    # lesscss.g:189:6: ^( N_Less_VarDef LESS_VARNAME term )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Less_VarDef, "N_Less_VarDef"), root_1)

                    self._adaptor.addChild(root_1, stream_LESS_VARNAME.nextNode())
                    self._adaptor.addChild(root_1, stream_term.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "less_variable_def"

    class ruleSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.ruleSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleSet"
    # lesscss.g:198:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA62 = None
        LBRACE64 = None
        RBRACE66 = None
        selector61 = None

        selector63 = None

        declarationset65 = None


        COMMA62_tree = None
        LBRACE64_tree = None
        RBRACE66_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:199:2: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:199:4: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet646)
                selector61 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector61.tree)
                # lesscss.g:199:13: ( COMMA selector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1


                    if alt14 == 1:
                        # lesscss.g:199:14: COMMA selector
                        pass 
                        COMMA62=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet649) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA62)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet651)
                        selector63 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector63.tree)


                    else:
                        break #loop14
                LBRACE64=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet655) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE64)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet657)
                declarationset65 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset65.tree)
                RBRACE66=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet659) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE66)

                # AST Rewrite
                # elements: declarationset, selector
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 200:3: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:200:6: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:200:18: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:200:18: ^( N_Selector selector )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Selector, "N_Selector"), root_2)

                        self._adaptor.addChild(root_2, stream_selector.nextTree())

                        self._adaptor.addChild(root_1, root_2)


                    stream_selector.reset()
                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ruleSet"

    class selector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.selector_return, self).__init__()

            self.tree = None




    # $ANTLR start "selector"
    # lesscss.g:203:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector67 = None

        combinator68 = None

        simpleSelector69 = None



        try:
            try:
                # lesscss.g:204:2: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:204:4: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector687)
                simpleSelector67 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector67.tree)
                # lesscss.g:204:19: ( combinator simpleSelector )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == IDENT or LA15_0 == COLON or (PLUS <= LA15_0 <= STAR)) :
                        alt15 = 1


                    if alt15 == 1:
                        # lesscss.g:204:20: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector690)
                        combinator68 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator68.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector692)
                        simpleSelector69 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector69.tree)


                    else:
                        break #loop15



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "selector"

    class combinator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.combinator_return, self).__init__()

            self.tree = None




    # $ANTLR start "combinator"
    # lesscss.g:207:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS70 = None
        GREATER71 = None

        PLUS70_tree = None
        GREATER71_tree = None

        try:
            try:
                # lesscss.g:208:2: ( PLUS | GREATER | )
                alt16 = 3
                LA16 = self.input.LA(1)
                if LA16 == PLUS:
                    alt16 = 1
                elif LA16 == GREATER:
                    alt16 = 2
                elif LA16 == IDENT or LA16 == COLON or LA16 == HASH or LA16 == DOT or LA16 == LBRACKET or LA16 == STAR:
                    alt16 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # lesscss.g:208:4: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS70=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator705)
                    if self._state.backtracking == 0:

                        PLUS70_tree = self._adaptor.createWithPayload(PLUS70)
                        self._adaptor.addChild(root_0, PLUS70_tree)



                elif alt16 == 2:
                    # lesscss.g:209:4: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER71=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator710)
                    if self._state.backtracking == 0:

                        GREATER71_tree = self._adaptor.createWithPayload(GREATER71)
                        self._adaptor.addChild(root_0, GREATER71_tree)



                elif alt16 == 3:
                    # lesscss.g:211:2: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "combinator"

    class simpleSelector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.simpleSelector_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleSelector"
    # lesscss.g:213:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName72 = None

        elementSubsequent73 = None

        elementSubsequent74 = None



        try:
            try:
                # lesscss.g:214:2: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == IDENT or LA19_0 == STAR) :
                    alt19 = 1
                elif (LA19_0 == COLON or (HASH <= LA19_0 <= LBRACKET)) :
                    alt19 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # lesscss.g:214:4: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector724)
                    elementName72 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName72.tree)
                    # lesscss.g:214:16: ( ( esPred )=> elementSubsequent )*
                    while True: #loop17
                        alt17 = 2
                        alt17 = self.dfa17.predict(self.input)
                        if alt17 == 1:
                            # lesscss.g:214:17: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector731)
                            elementSubsequent73 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent73.tree)


                        else:
                            break #loop17


                elif alt19 == 2:
                    # lesscss.g:215:4: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:215:4: ( ( esPred )=> elementSubsequent )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18 = self.input.LA(1)
                        if LA18 == HASH:
                            LA18_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt18 = 1


                        elif LA18 == DOT:
                            LA18_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt18 = 1


                        elif LA18 == COLON:
                            LA18_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt18 = 1


                        elif LA18 == LBRACKET:
                            LA18_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt18 = 1



                        if alt18 == 1:
                            # lesscss.g:215:5: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector743)
                            elementSubsequent74 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent74.tree)


                        else:
                            if cnt18 >= 1:
                                break #loop18

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simpleSelector"

    class esPred_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.esPred_return, self).__init__()

            self.tree = None




    # $ANTLR start "esPred"
    # lesscss.g:218:1: esPred : ( HASH | DOT | COLON | LBRACKET );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set75 = None

        set75_tree = None

        try:
            try:
                # lesscss.g:219:2: ( HASH | DOT | COLON | LBRACKET )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set75 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set75))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "esPred"

    class elementName_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementName_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementName"
    # lesscss.g:225:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set76 = None

        set76_tree = None

        try:
            try:
                # lesscss.g:226:2: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set76 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set76))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elementName"

    class elementSubsequent_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementSubsequent_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementSubsequent"
    # lesscss.g:230:1: elementSubsequent : ( HASH | cssClass | pseudo | attrib );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH77 = None
        cssClass78 = None

        pseudo79 = None

        attrib80 = None


        HASH77_tree = None

        try:
            try:
                # lesscss.g:231:2: ( HASH | cssClass | pseudo | attrib )
                alt20 = 4
                LA20 = self.input.LA(1)
                if LA20 == HASH:
                    alt20 = 1
                elif LA20 == DOT:
                    alt20 = 2
                elif LA20 == COLON:
                    alt20 = 3
                elif LA20 == LBRACKET:
                    alt20 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # lesscss.g:231:4: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH77=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent805)
                    if self._state.backtracking == 0:

                        HASH77_tree = self._adaptor.createWithPayload(HASH77)
                        self._adaptor.addChild(root_0, HASH77_tree)



                elif alt20 == 2:
                    # lesscss.g:232:4: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent810)
                    cssClass78 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass78.tree)


                elif alt20 == 3:
                    # lesscss.g:233:4: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent815)
                    pseudo79 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo79.tree)


                elif alt20 == 4:
                    # lesscss.g:234:4: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent820)
                    attrib80 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib80.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elementSubsequent"

    class cssClass_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.cssClass_return, self).__init__()

            self.tree = None




    # $ANTLR start "cssClass"
    # lesscss.g:237:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT81 = None

        a_tree = None
        DOT81_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:238:2: ( DOT a= IDENT -> IDENT )
                # lesscss.g:238:4: DOT a= IDENT
                pass 
                DOT81=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass832) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT81)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass836) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(a)
                if self._state.backtracking == 0:
                    a.setText('.' + a.getText()); 


                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 240:3: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "cssClass"

    class pseudo_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudo_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudo"
    # lesscss.g:243:1: pseudo : a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) ;
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        IDENT82 = None
        pseudoFunction83 = None


        a_tree = None
        b_tree = None
        IDENT82_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_pseudoFunction = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoFunction")
        try:
            try:
                # lesscss.g:244:2: (a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) )
                # lesscss.g:244:4: a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
                pass 
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo860) 
                if self._state.backtracking == 0:
                    stream_COLON.add(a)
                # lesscss.g:244:13: (b= COLON )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == COLON) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:244:13: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo864) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(b)



                # lesscss.g:245:2: ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IDENT) :
                    alt22 = 1
                elif (LA22_0 == FUNCTION) :
                    alt22 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # lesscss.g:245:4: IDENT
                    pass 
                    IDENT82=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo870) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT82)

                    # AST Rewrite
                    # elements: a, IDENT, b
                    # token labels: b, a
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0
                        stream_b = RewriteRuleTokenStream(self._adaptor, "token b", b)
                        stream_a = RewriteRuleTokenStream(self._adaptor, "token a", a)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 246:3: -> ^( N_Pseudo $a ( $b)? IDENT )
                        # lesscss.g:246:6: ^( N_Pseudo $a ( $b)? IDENT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:246:20: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 2:
                    # lesscss.g:247:4: pseudoFunction
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoFunction_in_pseudo892)
                    pseudoFunction83 = self.pseudoFunction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoFunction.add(pseudoFunction83.tree)

                    # AST Rewrite
                    # elements: pseudoFunction, a, b
                    # token labels: b, a
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0
                        stream_b = RewriteRuleTokenStream(self._adaptor, "token b", b)
                        stream_a = RewriteRuleTokenStream(self._adaptor, "token a", a)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 248:3: -> ^( N_Pseudo $a ( $b)? pseudoFunction )
                        # lesscss.g:248:6: ^( N_Pseudo $a ( $b)? pseudoFunction )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:248:20: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_pseudoFunction.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudo"

    class pseudoFunction_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudoFunction_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudoFunction"
    # lesscss.g:252:1: pseudoFunction : ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) );
    def pseudoFunction(self, ):

        retval = self.pseudoFunction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FUNCTION84 = None
        RPAREN86 = None
        FUNCTION87 = None
        LBRACKET88 = None
        RBRACKET90 = None
        RPAREN91 = None
        FUNCTION92 = None
        RPAREN94 = None
        expr85 = None

        attribBody89 = None

        pseudo93 = None


        FUNCTION84_tree = None
        RPAREN86_tree = None
        FUNCTION87_tree = None
        LBRACKET88_tree = None
        RBRACKET90_tree = None
        RPAREN91_tree = None
        FUNCTION92_tree = None
        RPAREN94_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        stream_pseudo = RewriteRuleSubtreeStream(self._adaptor, "rule pseudo")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:253:2: ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) )
                alt23 = 3
                LA23_0 = self.input.LA(1)

                if (LA23_0 == FUNCTION) :
                    LA23 = self.input.LA(2)
                    if LA23 == LBRACKET:
                        alt23 = 2
                    elif LA23 == COLON:
                        alt23 = 3
                    elif LA23 == STRING or LA23 == URI or LA23 == IDENT or LA23 == PERCENTAGE or LA23 == LESS_VARNAME or LA23 == PLUS or LA23 == HASH or LA23 == FUNCTION or LA23 == NUMBER or LA23 == LENGTH or LA23 == EMS or LA23 == EXS or LA23 == REMS or LA23 == CHS or LA23 == ANGLE or LA23 == TIME or LA23 == FREQ or LA23 == RESOLUTION or LA23 == VPORTLEN or LA23 == NTH or LA23 == UNICODE_RANGE or LA23 == MINUS:
                        alt23 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 23, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # lesscss.g:253:4: FUNCTION expr RPAREN
                    pass 
                    FUNCTION84=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction923) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION84)
                    self._state.following.append(self.FOLLOW_expr_in_pseudoFunction925)
                    expr85 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr85.tree)
                    RPAREN86=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction927) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN86)

                    # AST Rewrite
                    # elements: FUNCTION, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 254:3: -> ^( N_PseudoFunction FUNCTION expr )
                        # lesscss.g:254:6: ^( N_PseudoFunction FUNCTION expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 2:
                    # lesscss.g:256:4: FUNCTION LBRACKET attribBody RBRACKET RPAREN
                    pass 
                    FUNCTION87=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction946) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION87)
                    LBRACKET88=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudoFunction948) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET88)
                    self._state.following.append(self.FOLLOW_attribBody_in_pseudoFunction950)
                    attribBody89 = self.attribBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_attribBody.add(attribBody89.tree)
                    RBRACKET90=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudoFunction952) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET90)
                    RPAREN91=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction954) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN91)

                    # AST Rewrite
                    # elements: LBRACKET, RBRACKET, attribBody, FUNCTION
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 257:3: -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        # lesscss.g:257:6: ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_LBRACKET.nextNode())
                        self._adaptor.addChild(root_1, stream_attribBody.nextTree())
                        self._adaptor.addChild(root_1, stream_RBRACKET.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 3:
                    # lesscss.g:259:4: FUNCTION pseudo RPAREN
                    pass 
                    FUNCTION92=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction977) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION92)
                    self._state.following.append(self.FOLLOW_pseudo_in_pseudoFunction979)
                    pseudo93 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudo.add(pseudo93.tree)
                    RPAREN94=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction981) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN94)

                    # AST Rewrite
                    # elements: FUNCTION, pseudo
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 260:3: -> ^( N_PseudoFunction FUNCTION pseudo )
                        # lesscss.g:260:6: ^( N_PseudoFunction FUNCTION pseudo )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_pseudo.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudoFunction"

    class attrib_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attrib_return, self).__init__()

            self.tree = None




    # $ANTLR start "attrib"
    # lesscss.g:264:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET95 = None
        RBRACKET97 = None
        attribBody96 = None


        LBRACKET95_tree = None
        RBRACKET97_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:265:2: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:265:4: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET95=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1006) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET95)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1008)
                attribBody96 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody96.tree)
                RBRACKET97=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1010) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET97)

                # AST Rewrite
                # elements: attribBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 266:3: -> ^( N_Attrib attribBody )
                    # lesscss.g:266:7: ^( N_Attrib attribBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Attrib, "N_Attrib"), root_1)

                    self._adaptor.addChild(root_1, stream_attribBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "attrib"

    class attribBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attribBody_return, self).__init__()

            self.tree = None




    # $ANTLR start "attribBody"
    # lesscss.g:269:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT98 = None
        IDENT99 = None
        set100 = None
        term101 = None


        IDENT98_tree = None
        IDENT99_tree = None
        set100_tree = None

        try:
            try:
                # lesscss.g:270:2: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == IDENT) :
                    LA24_1 = self.input.LA(2)

                    if ((OPEQ <= LA24_1 <= SUBSTRINGMATCH)) :
                        alt24 = 2
                    elif (LA24_1 == RBRACKET) :
                        alt24 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # lesscss.g:270:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT98=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1033)
                    if self._state.backtracking == 0:

                        IDENT98_tree = self._adaptor.createWithPayload(IDENT98)
                        self._adaptor.addChild(root_0, IDENT98_tree)



                elif alt24 == 2:
                    # lesscss.g:271:4: IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT99=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1038)
                    if self._state.backtracking == 0:

                        IDENT99_tree = self._adaptor.createWithPayload(IDENT99)
                        self._adaptor.addChild(root_0, IDENT99_tree)

                    set100 = self.input.LT(1)
                    set100 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= SUBSTRINGMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set100), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_term_in_attribBody1087)
                    term101 = self.term()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, term101.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "attribBody"

    class declarationset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declarationset_return, self).__init__()

            self.tree = None




    # $ANTLR start "declarationset"
    # lesscss.g:286:1: declarationset : ( declaration ( SEMI declaration )* ( SEMI )? | -> N_Empty );
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI103 = None
        SEMI105 = None
        declaration102 = None

        declaration104 = None


        SEMI103_tree = None
        SEMI105_tree = None

        try:
            try:
                # lesscss.g:287:2: ( declaration ( SEMI declaration )* ( SEMI )? | -> N_Empty )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == IDENT or LA27_0 == STAR) :
                    alt27 = 1
                elif (LA27_0 == RBRACE) :
                    alt27 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # lesscss.g:287:4: declaration ( SEMI declaration )* ( SEMI )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_declaration_in_declarationset1102)
                    declaration102 = self.declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, declaration102.tree)
                    # lesscss.g:287:16: ( SEMI declaration )*
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == SEMI) :
                            LA25_1 = self.input.LA(2)

                            if (LA25_1 == IDENT or LA25_1 == STAR) :
                                alt25 = 1




                        if alt25 == 1:
                            # lesscss.g:287:17: SEMI declaration
                            pass 
                            SEMI103=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1105)
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset1108)
                            declaration104 = self.declaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, declaration104.tree)


                        else:
                            break #loop25
                    # lesscss.g:287:41: ( SEMI )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == SEMI) :
                        alt26 = 1
                    if alt26 == 1:
                        # lesscss.g:287:41: SEMI
                        pass 
                        SEMI105=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1112)





                elif alt27 == 2:
                    # lesscss.g:288:4: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 288:4: -> N_Empty
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(N_Empty, "N_Empty"))



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declarationset"

    class declaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "declaration"
    # lesscss.g:291:1: declaration : ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) );
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON107 = None
        COLON111 = None
        property106 = None

        expr108 = None

        prio109 = None

        property110 = None


        COLON107_tree = None
        COLON111_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:292:2: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == IDENT) :
                    LA29_1 = self.input.LA(2)

                    if (LA29_1 == COLON) :
                        LA29_3 = self.input.LA(3)

                        if (LA29_3 == STRING or LA29_3 == URI or LA29_3 == IDENT or (PERCENTAGE <= LA29_3 <= PLUS) or LA29_3 == HASH or LA29_3 == FUNCTION or (NUMBER <= LA29_3 <= MINUS)) :
                            alt29 = 1
                        elif (LA29_3 == SEMI or LA29_3 == RBRACE) :
                            alt29 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 29, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 29, 1, self.input)

                        raise nvae

                elif (LA29_0 == STAR) :
                    LA29_2 = self.input.LA(2)

                    if (LA29_2 == IDENT) :
                        LA29_4 = self.input.LA(3)

                        if (LA29_4 == COLON) :
                            LA29_3 = self.input.LA(4)

                            if (LA29_3 == STRING or LA29_3 == URI or LA29_3 == IDENT or (PERCENTAGE <= LA29_3 <= PLUS) or LA29_3 == HASH or LA29_3 == FUNCTION or (NUMBER <= LA29_3 <= MINUS)) :
                                alt29 = 1
                            elif (LA29_3 == SEMI or LA29_3 == RBRACE) :
                                alt29 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 29, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 29, 4, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 29, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # lesscss.g:292:4: property COLON expr ( prio )?
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1132)
                    property106 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property106.tree)
                    COLON107=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1134) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON107)
                    self._state.following.append(self.FOLLOW_expr_in_declaration1136)
                    expr108 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr108.tree)
                    # lesscss.g:292:24: ( prio )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == IMPORTANT_SYM) :
                        alt28 = 1
                    if alt28 == 1:
                        # lesscss.g:292:24: prio
                        pass 
                        self._state.following.append(self.FOLLOW_prio_in_declaration1138)
                        prio109 = self.prio()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_prio.add(prio109.tree)




                    # AST Rewrite
                    # elements: prio, property, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 293:3: -> ^( N_Declaration property expr ( prio )? )
                        # lesscss.g:293:6: ^( N_Declaration property expr ( prio )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                        self._adaptor.addChild(root_1, stream_property.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())
                        # lesscss.g:293:36: ( prio )?
                        if stream_prio.hasNext():
                            self._adaptor.addChild(root_1, stream_prio.nextTree())


                        stream_prio.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 2:
                    # lesscss.g:295:5: property COLON
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1161)
                    property110 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property110.tree)
                    COLON111=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1163) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON111)

                    # AST Rewrite
                    # elements: property
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 296:3: -> ^( N_Declaration property )
                        # lesscss.g:296:6: ^( N_Declaration property )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                        self._adaptor.addChild(root_1, stream_property.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declaration"

    class property_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.property_return, self).__init__()

            self.tree = None




    # $ANTLR start "property"
    # lesscss.g:300:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT112 = None
        STAR113 = None

        a_tree = None
        IDENT112_tree = None
        STAR113_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:301:2: ( IDENT | STAR a= IDENT -> IDENT )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == IDENT) :
                    alt30 = 1
                elif (LA30_0 == STAR) :
                    alt30 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # lesscss.g:301:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT112=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1188)
                    if self._state.backtracking == 0:

                        IDENT112_tree = self._adaptor.createWithPayload(IDENT112)
                        self._adaptor.addChild(root_0, IDENT112_tree)



                elif alt30 == 2:
                    # lesscss.g:305:4: STAR a= IDENT
                    pass 
                    STAR113=self.match(self.input, STAR, self.FOLLOW_STAR_in_property1198) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR113)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1202) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(a)
                    if self._state.backtracking == 0:
                        a.setText('*' + a.getText()); 


                    # AST Rewrite
                    # elements: IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 307:3: -> IDENT
                        self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "property"

    class prio_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.prio_return, self).__init__()

            self.tree = None




    # $ANTLR start "prio"
    # lesscss.g:311:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM114 = None

        IMPORTANT_SYM114_tree = None

        try:
            try:
                # lesscss.g:312:2: ( IMPORTANT_SYM )
                # lesscss.g:312:4: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM114=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1225)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM114_tree = self._adaptor.createWithPayload(IMPORTANT_SYM114)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM114_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prio"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # lesscss.g:315:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term115 = None

        operator116 = None

        term117 = None



        try:
            try:
                # lesscss.g:316:2: ( term ( operator term )* )
                # lesscss.g:316:4: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1236)
                term115 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term115.tree)
                # lesscss.g:316:9: ( operator term )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == COMMA) :
                        LA31_2 = self.input.LA(2)

                        if (LA31_2 == STRING or LA31_2 == URI or (PERCENTAGE <= LA31_2 <= PLUS) or LA31_2 == HASH or LA31_2 == FUNCTION or (NUMBER <= LA31_2 <= MINUS)) :
                            alt31 = 1
                        elif (LA31_2 == IDENT) :
                            LA31_4 = self.input.LA(3)

                            if ((STRING <= LA31_4 <= SEMI) or LA31_4 == URI or (RBRACE <= LA31_4 <= IDENT) or (COLON <= LA31_4 <= RPAREN) or (PERCENTAGE <= LA31_4 <= PLUS) or (HASH <= LA31_4 <= DOT) or LA31_4 == FUNCTION or (IMPORTANT_SYM <= LA31_4 <= MINUS)) :
                                alt31 = 1




                    elif (LA31_0 == STRING or LA31_0 == URI or LA31_0 == IDENT or (PERCENTAGE <= LA31_0 <= PLUS) or LA31_0 == HASH or LA31_0 == FUNCTION or (SOLIDUS <= LA31_0 <= MINUS)) :
                        alt31 = 1


                    if alt31 == 1:
                        # lesscss.g:316:10: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1239)
                        operator116 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator116.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1242)
                        term117 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term117.tree)


                    else:
                        break #loop31



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.operator_return, self).__init__()

            self.tree = None




    # $ANTLR start "operator"
    # lesscss.g:319:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS118 = None
        COMMA119 = None

        SOLIDUS118_tree = None
        COMMA119_tree = None

        try:
            try:
                # lesscss.g:320:2: ( SOLIDUS | COMMA | -> N_Space )
                alt32 = 3
                LA32 = self.input.LA(1)
                if LA32 == SOLIDUS:
                    alt32 = 1
                elif LA32 == COMMA:
                    alt32 = 2
                elif LA32 == STRING or LA32 == URI or LA32 == IDENT or LA32 == PERCENTAGE or LA32 == LESS_VARNAME or LA32 == PLUS or LA32 == HASH or LA32 == FUNCTION or LA32 == NUMBER or LA32 == LENGTH or LA32 == EMS or LA32 == EXS or LA32 == REMS or LA32 == CHS or LA32 == ANGLE or LA32 == TIME or LA32 == FREQ or LA32 == RESOLUTION or LA32 == VPORTLEN or LA32 == NTH or LA32 == UNICODE_RANGE or LA32 == MINUS:
                    alt32 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # lesscss.g:320:4: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS118=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1257)
                    if self._state.backtracking == 0:

                        SOLIDUS118_tree = self._adaptor.createWithPayload(SOLIDUS118)
                        self._adaptor.addChild(root_0, SOLIDUS118_tree)



                elif alt32 == 2:
                    # lesscss.g:321:4: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA119=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1262)
                    if self._state.backtracking == 0:

                        COMMA119_tree = self._adaptor.createWithPayload(COMMA119)
                        self._adaptor.addChild(root_0, COMMA119_tree)



                elif alt32 == 3:
                    # lesscss.g:322:4: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 322:4: -> N_Space
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(N_Space, "N_Space"))



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "operator"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # lesscss.g:325:1: term : ( ( unaryOperator )? ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) ) | STRING | IDENT | URI | hexColor -> ^( N_Term hexColor ) | UNICODE_RANGE | LESS_VARNAME );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NUMBER121 = None
        PERCENTAGE122 = None
        LENGTH123 = None
        EMS124 = None
        EXS125 = None
        REMS126 = None
        CHS127 = None
        ANGLE128 = None
        TIME129 = None
        FREQ130 = None
        RESOLUTION131 = None
        VPORTLEN132 = None
        NTH133 = None
        STRING135 = None
        IDENT136 = None
        URI137 = None
        UNICODE_RANGE139 = None
        LESS_VARNAME140 = None
        unaryOperator120 = None

        function134 = None

        hexColor138 = None


        NUMBER121_tree = None
        PERCENTAGE122_tree = None
        LENGTH123_tree = None
        EMS124_tree = None
        EXS125_tree = None
        REMS126_tree = None
        CHS127_tree = None
        ANGLE128_tree = None
        TIME129_tree = None
        FREQ130_tree = None
        RESOLUTION131_tree = None
        VPORTLEN132_tree = None
        NTH133_tree = None
        STRING135_tree = None
        IDENT136_tree = None
        URI137_tree = None
        UNICODE_RANGE139_tree = None
        LESS_VARNAME140_tree = None
        stream_TIME = RewriteRuleTokenStream(self._adaptor, "token TIME")
        stream_ANGLE = RewriteRuleTokenStream(self._adaptor, "token ANGLE")
        stream_EMS = RewriteRuleTokenStream(self._adaptor, "token EMS")
        stream_REMS = RewriteRuleTokenStream(self._adaptor, "token REMS")
        stream_EXS = RewriteRuleTokenStream(self._adaptor, "token EXS")
        stream_NUMBER = RewriteRuleTokenStream(self._adaptor, "token NUMBER")
        stream_RESOLUTION = RewriteRuleTokenStream(self._adaptor, "token RESOLUTION")
        stream_FREQ = RewriteRuleTokenStream(self._adaptor, "token FREQ")
        stream_NTH = RewriteRuleTokenStream(self._adaptor, "token NTH")
        stream_PERCENTAGE = RewriteRuleTokenStream(self._adaptor, "token PERCENTAGE")
        stream_VPORTLEN = RewriteRuleTokenStream(self._adaptor, "token VPORTLEN")
        stream_LENGTH = RewriteRuleTokenStream(self._adaptor, "token LENGTH")
        stream_CHS = RewriteRuleTokenStream(self._adaptor, "token CHS")
        stream_unaryOperator = RewriteRuleSubtreeStream(self._adaptor, "rule unaryOperator")
        stream_hexColor = RewriteRuleSubtreeStream(self._adaptor, "rule hexColor")
        stream_function = RewriteRuleSubtreeStream(self._adaptor, "rule function")
        try:
            try:
                # lesscss.g:326:2: ( ( unaryOperator )? ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) ) | STRING | IDENT | URI | hexColor -> ^( N_Term hexColor ) | UNICODE_RANGE | LESS_VARNAME )
                alt35 = 7
                LA35 = self.input.LA(1)
                if LA35 == PERCENTAGE or LA35 == PLUS or LA35 == FUNCTION or LA35 == NUMBER or LA35 == LENGTH or LA35 == EMS or LA35 == EXS or LA35 == REMS or LA35 == CHS or LA35 == ANGLE or LA35 == TIME or LA35 == FREQ or LA35 == RESOLUTION or LA35 == VPORTLEN or LA35 == NTH or LA35 == MINUS:
                    alt35 = 1
                elif LA35 == IDENT:
                    LA35_2 = self.input.LA(2)

                    if (LA35_2 == COLON or LA35_2 == DOT) :
                        alt35 = 1
                    elif ((STRING <= LA35_2 <= SEMI) or LA35_2 == URI or (RBRACE <= LA35_2 <= IDENT) or LA35_2 == RPAREN or (PERCENTAGE <= LA35_2 <= PLUS) or LA35_2 == HASH or (FUNCTION <= LA35_2 <= RBRACKET) or (IMPORTANT_SYM <= LA35_2 <= MINUS)) :
                        alt35 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 35, 2, self.input)

                        raise nvae

                elif LA35 == STRING:
                    alt35 = 2
                elif LA35 == URI:
                    alt35 = 4
                elif LA35 == HASH:
                    alt35 = 5
                elif LA35 == UNICODE_RANGE:
                    alt35 = 6
                elif LA35 == LESS_VARNAME:
                    alt35 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # lesscss.g:326:4: ( unaryOperator )? ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) )
                    pass 
                    # lesscss.g:326:4: ( unaryOperator )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == PLUS or LA33_0 == MINUS) :
                        alt33 = 1
                    if alt33 == 1:
                        # lesscss.g:326:4: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1281)
                        unaryOperator120 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_unaryOperator.add(unaryOperator120.tree)



                    # lesscss.g:326:19: ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) )
                    alt34 = 14
                    LA34 = self.input.LA(1)
                    if LA34 == NUMBER:
                        alt34 = 1
                    elif LA34 == PERCENTAGE:
                        alt34 = 2
                    elif LA34 == LENGTH:
                        alt34 = 3
                    elif LA34 == EMS:
                        alt34 = 4
                    elif LA34 == EXS:
                        alt34 = 5
                    elif LA34 == REMS:
                        alt34 = 6
                    elif LA34 == CHS:
                        alt34 = 7
                    elif LA34 == ANGLE:
                        alt34 = 8
                    elif LA34 == TIME:
                        alt34 = 9
                    elif LA34 == FREQ:
                        alt34 = 10
                    elif LA34 == RESOLUTION:
                        alt34 = 11
                    elif LA34 == VPORTLEN:
                        alt34 = 12
                    elif LA34 == NTH:
                        alt34 = 13
                    elif LA34 == IDENT or LA34 == FUNCTION:
                        alt34 = 14
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 34, 0, self.input)

                        raise nvae

                    if alt34 == 1:
                        # lesscss.g:327:5: NUMBER
                        pass 
                        NUMBER121=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_term1290) 
                        if self._state.backtracking == 0:
                            stream_NUMBER.add(NUMBER121)

                        # AST Rewrite
                        # elements: unaryOperator, NUMBER
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 327:12: -> ^( N_Term ( unaryOperator )? NUMBER )
                            # lesscss.g:327:15: ^( N_Term ( unaryOperator )? NUMBER )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:327:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_NUMBER.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 2:
                        # lesscss.g:328:5: PERCENTAGE
                        pass 
                        PERCENTAGE122=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_term1307) 
                        if self._state.backtracking == 0:
                            stream_PERCENTAGE.add(PERCENTAGE122)

                        # AST Rewrite
                        # elements: unaryOperator, PERCENTAGE
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 328:16: -> ^( N_Term ( unaryOperator )? PERCENTAGE )
                            # lesscss.g:328:19: ^( N_Term ( unaryOperator )? PERCENTAGE )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:328:28: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_PERCENTAGE.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 3:
                        # lesscss.g:329:5: LENGTH
                        pass 
                        LENGTH123=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_term1324) 
                        if self._state.backtracking == 0:
                            stream_LENGTH.add(LENGTH123)

                        # AST Rewrite
                        # elements: LENGTH, unaryOperator
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 329:12: -> ^( N_Term ( unaryOperator )? LENGTH )
                            # lesscss.g:329:15: ^( N_Term ( unaryOperator )? LENGTH )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:329:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_LENGTH.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 4:
                        # lesscss.g:330:5: EMS
                        pass 
                        EMS124=self.match(self.input, EMS, self.FOLLOW_EMS_in_term1341) 
                        if self._state.backtracking == 0:
                            stream_EMS.add(EMS124)

                        # AST Rewrite
                        # elements: unaryOperator, EMS
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 330:11: -> ^( N_Term ( unaryOperator )? EMS )
                            # lesscss.g:330:14: ^( N_Term ( unaryOperator )? EMS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:330:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_EMS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 5:
                        # lesscss.g:331:5: EXS
                        pass 
                        EXS125=self.match(self.input, EXS, self.FOLLOW_EXS_in_term1360) 
                        if self._state.backtracking == 0:
                            stream_EXS.add(EXS125)

                        # AST Rewrite
                        # elements: EXS, unaryOperator
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 331:11: -> ^( N_Term ( unaryOperator )? EXS )
                            # lesscss.g:331:14: ^( N_Term ( unaryOperator )? EXS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:331:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_EXS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 6:
                        # lesscss.g:332:5: REMS
                        pass 
                        REMS126=self.match(self.input, REMS, self.FOLLOW_REMS_in_term1379) 
                        if self._state.backtracking == 0:
                            stream_REMS.add(REMS126)

                        # AST Rewrite
                        # elements: unaryOperator, REMS
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 332:12: -> ^( N_Term ( unaryOperator )? REMS )
                            # lesscss.g:332:15: ^( N_Term ( unaryOperator )? REMS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:332:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_REMS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 7:
                        # lesscss.g:333:5: CHS
                        pass 
                        CHS127=self.match(self.input, CHS, self.FOLLOW_CHS_in_term1398) 
                        if self._state.backtracking == 0:
                            stream_CHS.add(CHS127)

                        # AST Rewrite
                        # elements: unaryOperator, CHS
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 333:11: -> ^( N_Term ( unaryOperator )? CHS )
                            # lesscss.g:333:14: ^( N_Term ( unaryOperator )? CHS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:333:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_CHS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 8:
                        # lesscss.g:334:5: ANGLE
                        pass 
                        ANGLE128=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_term1417) 
                        if self._state.backtracking == 0:
                            stream_ANGLE.add(ANGLE128)

                        # AST Rewrite
                        # elements: unaryOperator, ANGLE
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 334:13: -> ^( N_Term ( unaryOperator )? ANGLE )
                            # lesscss.g:334:16: ^( N_Term ( unaryOperator )? ANGLE )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:334:25: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_ANGLE.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 9:
                        # lesscss.g:335:5: TIME
                        pass 
                        TIME129=self.match(self.input, TIME, self.FOLLOW_TIME_in_term1436) 
                        if self._state.backtracking == 0:
                            stream_TIME.add(TIME129)

                        # AST Rewrite
                        # elements: unaryOperator, TIME
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 335:12: -> ^( N_Term ( unaryOperator )? TIME )
                            # lesscss.g:335:15: ^( N_Term ( unaryOperator )? TIME )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:335:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_TIME.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 10:
                        # lesscss.g:336:5: FREQ
                        pass 
                        FREQ130=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_term1455) 
                        if self._state.backtracking == 0:
                            stream_FREQ.add(FREQ130)

                        # AST Rewrite
                        # elements: unaryOperator, FREQ
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 336:12: -> ^( N_Term ( unaryOperator )? FREQ )
                            # lesscss.g:336:15: ^( N_Term ( unaryOperator )? FREQ )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:336:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_FREQ.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 11:
                        # lesscss.g:337:5: RESOLUTION
                        pass 
                        RESOLUTION131=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_term1474) 
                        if self._state.backtracking == 0:
                            stream_RESOLUTION.add(RESOLUTION131)

                        # AST Rewrite
                        # elements: unaryOperator, RESOLUTION
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 337:16: -> ^( N_Term ( unaryOperator )? RESOLUTION )
                            # lesscss.g:337:19: ^( N_Term ( unaryOperator )? RESOLUTION )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:337:28: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_RESOLUTION.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 12:
                        # lesscss.g:338:5: VPORTLEN
                        pass 
                        VPORTLEN132=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_term1491) 
                        if self._state.backtracking == 0:
                            stream_VPORTLEN.add(VPORTLEN132)

                        # AST Rewrite
                        # elements: VPORTLEN, unaryOperator
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 338:14: -> ^( N_Term ( unaryOperator )? VPORTLEN )
                            # lesscss.g:338:17: ^( N_Term ( unaryOperator )? VPORTLEN )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:338:26: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_VPORTLEN.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 13:
                        # lesscss.g:339:5: NTH
                        pass 
                        NTH133=self.match(self.input, NTH, self.FOLLOW_NTH_in_term1508) 
                        if self._state.backtracking == 0:
                            stream_NTH.add(NTH133)

                        # AST Rewrite
                        # elements: NTH, unaryOperator
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 339:11: -> ^( N_Term ( unaryOperator )? NTH )
                            # lesscss.g:339:14: ^( N_Term ( unaryOperator )? NTH )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:339:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_NTH.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 14:
                        # lesscss.g:340:5: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_term1527)
                        function134 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_function.add(function134.tree)

                        # AST Rewrite
                        # elements: function, unaryOperator
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:

                            retval.tree = root_0

                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 340:14: -> ^( N_Term ( unaryOperator )? function )
                            # lesscss.g:340:17: ^( N_Term ( unaryOperator )? function )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:340:26: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_function.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt35 == 2:
                    # lesscss.g:342:4: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING135=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1546)
                    if self._state.backtracking == 0:

                        STRING135_tree = self._adaptor.createWithPayload(STRING135)
                        self._adaptor.addChild(root_0, STRING135_tree)



                elif alt35 == 3:
                    # lesscss.g:343:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT136=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1551)
                    if self._state.backtracking == 0:

                        IDENT136_tree = self._adaptor.createWithPayload(IDENT136)
                        self._adaptor.addChild(root_0, IDENT136_tree)



                elif alt35 == 4:
                    # lesscss.g:344:4: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI137=self.match(self.input, URI, self.FOLLOW_URI_in_term1556)
                    if self._state.backtracking == 0:

                        URI137_tree = self._adaptor.createWithPayload(URI137)
                        self._adaptor.addChild(root_0, URI137_tree)



                elif alt35 == 5:
                    # lesscss.g:345:4: hexColor
                    pass 
                    self._state.following.append(self.FOLLOW_hexColor_in_term1561)
                    hexColor138 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_hexColor.add(hexColor138.tree)

                    # AST Rewrite
                    # elements: hexColor
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 345:14: -> ^( N_Term hexColor )
                        # lesscss.g:345:17: ^( N_Term hexColor )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                        self._adaptor.addChild(root_1, stream_hexColor.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt35 == 6:
                    # lesscss.g:346:4: UNICODE_RANGE
                    pass 
                    root_0 = self._adaptor.nil()

                    UNICODE_RANGE139=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term1575)
                    if self._state.backtracking == 0:

                        UNICODE_RANGE139_tree = self._adaptor.createWithPayload(UNICODE_RANGE139)
                        self._adaptor.addChild(root_0, UNICODE_RANGE139_tree)



                elif alt35 == 7:
                    # lesscss.g:347:4: LESS_VARNAME
                    pass 
                    root_0 = self._adaptor.nil()

                    LESS_VARNAME140=self.match(self.input, LESS_VARNAME, self.FOLLOW_LESS_VARNAME_in_term1580)
                    if self._state.backtracking == 0:

                        LESS_VARNAME140_tree = self._adaptor.createWithPayload(LESS_VARNAME140)
                        self._adaptor.addChild(root_0, LESS_VARNAME140_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "term"

    class unaryOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.unaryOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "unaryOperator"
    # lesscss.g:350:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set141 = None

        set141_tree = None

        try:
            try:
                # lesscss.g:351:2: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set141 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set141))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unaryOperator"

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.function_return, self).__init__()

            self.tree = None




    # $ANTLR start "function"
    # lesscss.g:356:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name ^( N_Expr expr ) ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN144 = None
        RPAREN147 = None
        fnct_name142 = None

        fnct_args143 = None

        fnct_name145 = None

        expr146 = None


        RPAREN144_tree = None
        RPAREN147_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:357:2: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name ^( N_Expr expr ) ) )
                alt36 = 2
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # lesscss.g:357:4: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1608)
                    fnct_name142 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name142.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1610)
                    fnct_args143 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args143.tree)
                    RPAREN144=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1612) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN144)

                    # AST Rewrite
                    # elements: fnct_args, fnct_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 358:3: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:358:6: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 2:
                    # lesscss.g:360:4: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1630)
                    fnct_name145 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name145.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1632)
                    expr146 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr146.tree)
                    RPAREN147=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1634) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN147)

                    # AST Rewrite
                    # elements: expr, fnct_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 361:3: -> ^( N_Function fnct_name ^( N_Expr expr ) )
                        # lesscss.g:361:6: ^( N_Function fnct_name ^( N_Expr expr ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        # lesscss.g:361:29: ^( N_Expr expr )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Expr, "N_Expr"), root_2)

                        self._adaptor.addChild(root_2, stream_expr.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "function"

    class fnct_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_name"
    # lesscss.g:365:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT148 = None
        set149 = None
        FUNCTION150 = None

        IDENT148_tree = None
        set149_tree = None
        FUNCTION150_tree = None

        try:
            try:
                # lesscss.g:366:2: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:366:4: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:366:4: ( IDENT ( COLON | DOT )+ )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == IDENT) :
                        alt38 = 1


                    if alt38 == 1:
                        # lesscss.g:366:5: IDENT ( COLON | DOT )+
                        pass 
                        IDENT148=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1664)
                        if self._state.backtracking == 0:

                            IDENT148_tree = self._adaptor.createWithPayload(IDENT148)
                            self._adaptor.addChild(root_0, IDENT148_tree)

                        # lesscss.g:366:11: ( COLON | DOT )+
                        cnt37 = 0
                        while True: #loop37
                            alt37 = 2
                            LA37_0 = self.input.LA(1)

                            if (LA37_0 == COLON or LA37_0 == DOT) :
                                alt37 = 1


                            if alt37 == 1:
                                # lesscss.g:
                                pass 
                                set149 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set149))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt37 >= 1:
                                    break #loop37

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(37, self.input)
                                raise eee

                            cnt37 += 1


                    else:
                        break #loop38
                FUNCTION150=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1676)
                if self._state.backtracking == 0:

                    FUNCTION150_tree = self._adaptor.createWithPayload(FUNCTION150)
                    root_0 = self._adaptor.becomeRoot(FUNCTION150_tree, root_0)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_name"

    class fnct_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_args_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_args"
    # lesscss.g:369:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA152 = None
        fnct_arg151 = None

        fnct_arg153 = None


        COMMA152_tree = None

        try:
            try:
                # lesscss.g:370:2: ( fnct_arg ( COMMA fnct_arg )* )
                # lesscss.g:370:4: fnct_arg ( COMMA fnct_arg )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1690)
                fnct_arg151 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fnct_arg151.tree)
                # lesscss.g:370:13: ( COMMA fnct_arg )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == COMMA) :
                        alt39 = 1


                    if alt39 == 1:
                        # lesscss.g:370:14: COMMA fnct_arg
                        pass 
                        COMMA152=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1693)
                        if self._state.backtracking == 0:

                            COMMA152_tree = self._adaptor.createWithPayload(COMMA152)
                            root_0 = self._adaptor.becomeRoot(COMMA152_tree, root_0)

                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1696)
                        fnct_arg153 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fnct_arg153.tree)


                    else:
                        break #loop39



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_args"

    class fnct_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_arg"
    # lesscss.g:373:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT154 = None
        OPEQ155 = None
        expr156 = None


        IDENT154_tree = None
        OPEQ155_tree = None

        try:
            try:
                # lesscss.g:374:2: ( IDENT OPEQ expr )
                # lesscss.g:374:4: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT154=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1709)
                if self._state.backtracking == 0:

                    IDENT154_tree = self._adaptor.createWithPayload(IDENT154)
                    self._adaptor.addChild(root_0, IDENT154_tree)

                OPEQ155=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1711)
                if self._state.backtracking == 0:

                    OPEQ155_tree = self._adaptor.createWithPayload(OPEQ155)
                    root_0 = self._adaptor.becomeRoot(OPEQ155_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1714)
                expr156 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr156.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_arg"

    class hexColor_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.hexColor_return, self).__init__()

            self.tree = None




    # $ANTLR start "hexColor"
    # lesscss.g:377:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH157 = None

        HASH157_tree = None

        try:
            try:
                # lesscss.g:378:2: ( HASH )
                # lesscss.g:378:4: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH157=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1725)
                if self._state.backtracking == 0:

                    HASH157_tree = self._adaptor.createWithPayload(HASH157)
                    self._adaptor.addChild(root_0, HASH157_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"

    # $ANTLR start "synpred1_lesscss"
    def synpred1_lesscss_fragment(self, ):
        # lesscss.g:214:17: ( esPred )
        # lesscss.g:214:18: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss728)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:215:5: ( esPred )
        # lesscss.g:215:6: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss740)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred2_lesscss"




    # Delegated rules

    def synpred2_lesscss(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_lesscss_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_lesscss(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_lesscss_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\33\3\uffff\4\0\3\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\1\54\3\uffff\4\0\3\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA17_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\1\1\uffff\2\1\1\uffff\1\6\6\uffff\2\1\1\4\1\5\1\7"
        u"\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA17_4 = input.LA(1)

                 
                index17_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index17_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA17_5 = input.LA(1)

                 
                index17_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index17_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA17_6 = input.LA(1)

                 
                index17_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index17_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA17_7 = input.LA(1)

                 
                index17_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index17_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 17, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\1\36\1\40\1\26\1\36\1\26\2\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\1\55\1\52\1\104\1\55\1\104\2\uffff"
        )

    DFA36_accept = DFA.unpack(
        u"\5\uffff\1\2\1\1"
        )

    DFA36_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\1\1\16\uffff\1\2"),
        DFA.unpack(u"\1\3\11\uffff\1\3"),
        DFA.unpack(u"\1\5\2\uffff\1\5\4\uffff\1\4\6\uffff\3\5\1\uffff\1"
        u"\5\3\uffff\1\5\11\uffff\16\5"),
        DFA.unpack(u"\1\1\1\uffff\1\3\11\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\5\2\uffff\1\5\3\uffff\2\5\1\uffff\2\5\3\uffff\3"
        u"\5\1\uffff\2\5\2\uffff\1\5\1\uffff\1\6\6\uffff\17\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #36

    class DFA36(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet147 = frozenset([24, 26, 30, 32, 34, 35, 36, 38, 41, 42, 43, 44])
    FOLLOW_imports_in_styleSheet153 = frozenset([24, 26, 30, 32, 34, 35, 36, 38, 41, 42, 43, 44])
    FOLLOW_body_in_styleSheet159 = frozenset([26, 30, 32, 34, 35, 36, 38, 41, 42, 43, 44])
    FOLLOW_EOF_in_styleSheet165 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet197 = frozenset([22])
    FOLLOW_STRING_in_charSet200 = frozenset([23])
    FOLLOW_SEMI_in_charSet202 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports217 = frozenset([22, 25])
    FOLLOW_importUrl_in_imports220 = frozenset([23, 30, 31])
    FOLLOW_media_query_list_in_imports222 = frozenset([23])
    FOLLOW_SEMI_in_imports225 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body257 = frozenset([1])
    FOLLOW_media_in_body262 = frozenset([1])
    FOLLOW_page_in_body267 = frozenset([1])
    FOLLOW_fontface_in_body272 = frozenset([1])
    FOLLOW_keyframes_in_body277 = frozenset([1])
    FOLLOW_less_variable_def_in_body282 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media301 = frozenset([27, 30, 31])
    FOLLOW_media_query_list_in_media304 = frozenset([27])
    FOLLOW_LBRACE_in_media309 = frozenset([26, 28, 30, 32, 34, 35, 36, 38, 41, 42, 43, 44])
    FOLLOW_body_in_media315 = frozenset([26, 28, 30, 32, 34, 35, 36, 38, 41, 42, 43, 44])
    FOLLOW_RBRACE_in_media324 = frozenset([1])
    FOLLOW_media_query_in_media_query_list339 = frozenset([1, 29])
    FOLLOW_COMMA_in_media_query_list342 = frozenset([30, 31])
    FOLLOW_media_query_in_media_query_list344 = frozenset([1, 29])
    FOLLOW_media_stmt_in_media_query373 = frozenset([1, 30, 31])
    FOLLOW_media_expr_in_media_query377 = frozenset([1, 30, 31])
    FOLLOW_IDENT_in_media_stmt391 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr402 = frozenset([30])
    FOLLOW_media_stmt_in_media_expr404 = frozenset([32, 33])
    FOLLOW_COLON_in_media_expr408 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_expr_in_media_expr410 = frozenset([33])
    FOLLOW_RPAREN_in_media_expr415 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface444 = frozenset([27])
    FOLLOW_LBRACE_in_fontface447 = frozenset([28, 30, 44])
    FOLLOW_declarationset_in_fontface450 = frozenset([28])
    FOLLOW_RBRACE_in_fontface452 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page467 = frozenset([27, 32])
    FOLLOW_pseudoPage_in_page470 = frozenset([27])
    FOLLOW_LBRACE_in_page473 = frozenset([28, 30, 44])
    FOLLOW_declarationset_in_page476 = frozenset([28])
    FOLLOW_RBRACE_in_page478 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage490 = frozenset([30])
    FOLLOW_IDENT_in_pseudoPage494 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes520 = frozenset([30])
    FOLLOW_IDENT_in_keyframes523 = frozenset([27])
    FOLLOW_LBRACE_in_keyframes525 = frozenset([28, 30, 37])
    FOLLOW_keyframes_block_in_keyframes528 = frozenset([28, 30, 37])
    FOLLOW_RBRACE_in_keyframes531 = frozenset([1])
    FOLLOW_keyframe_selector_in_keyframes_block543 = frozenset([27, 29])
    FOLLOW_COMMA_in_keyframes_block547 = frozenset([30, 37])
    FOLLOW_keyframe_selector_in_keyframes_block549 = frozenset([27, 29])
    FOLLOW_LBRACE_in_keyframes_block554 = frozenset([28, 30, 44])
    FOLLOW_declarationset_in_keyframes_block556 = frozenset([28])
    FOLLOW_RBRACE_in_keyframes_block558 = frozenset([1])
    FOLLOW_set_in_keyframe_selector588 = frozenset([1])
    FOLLOW_LESS_VARNAME_in_less_variable_def611 = frozenset([32])
    FOLLOW_COLON_in_less_variable_def613 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_term_in_less_variable_def615 = frozenset([23])
    FOLLOW_SEMI_in_less_variable_def617 = frozenset([1])
    FOLLOW_selector_in_ruleSet646 = frozenset([27, 29])
    FOLLOW_COMMA_in_ruleSet649 = frozenset([30, 32, 41, 42, 43, 44])
    FOLLOW_selector_in_ruleSet651 = frozenset([27, 29])
    FOLLOW_LBRACE_in_ruleSet655 = frozenset([28, 30, 44])
    FOLLOW_declarationset_in_ruleSet657 = frozenset([28])
    FOLLOW_RBRACE_in_ruleSet659 = frozenset([1])
    FOLLOW_simpleSelector_in_selector687 = frozenset([1, 30, 32, 39, 40, 41, 42, 43, 44])
    FOLLOW_combinator_in_selector690 = frozenset([30, 32, 41, 42, 43, 44])
    FOLLOW_simpleSelector_in_selector692 = frozenset([1, 30, 32, 39, 40, 41, 42, 43, 44])
    FOLLOW_PLUS_in_combinator705 = frozenset([1])
    FOLLOW_GREATER_in_combinator710 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector724 = frozenset([1, 30, 32, 41, 42, 43, 44])
    FOLLOW_elementSubsequent_in_simpleSelector731 = frozenset([1, 30, 32, 41, 42, 43, 44])
    FOLLOW_elementSubsequent_in_simpleSelector743 = frozenset([1, 30, 32, 41, 42, 43, 44])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent805 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent810 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent815 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent820 = frozenset([1])
    FOLLOW_DOT_in_cssClass832 = frozenset([30])
    FOLLOW_IDENT_in_cssClass836 = frozenset([1])
    FOLLOW_COLON_in_pseudo860 = frozenset([30, 32, 45])
    FOLLOW_COLON_in_pseudo864 = frozenset([30, 32, 45])
    FOLLOW_IDENT_in_pseudo870 = frozenset([1])
    FOLLOW_pseudoFunction_in_pseudo892 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction923 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_expr_in_pseudoFunction925 = frozenset([33])
    FOLLOW_RPAREN_in_pseudoFunction927 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction946 = frozenset([43])
    FOLLOW_LBRACKET_in_pseudoFunction948 = frozenset([30])
    FOLLOW_attribBody_in_pseudoFunction950 = frozenset([46])
    FOLLOW_RBRACKET_in_pseudoFunction952 = frozenset([33])
    FOLLOW_RPAREN_in_pseudoFunction954 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction977 = frozenset([32])
    FOLLOW_pseudo_in_pseudoFunction979 = frozenset([33])
    FOLLOW_RPAREN_in_pseudoFunction981 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1006 = frozenset([30])
    FOLLOW_attribBody_in_attrib1008 = frozenset([46])
    FOLLOW_RBRACKET_in_attrib1010 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1033 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1038 = frozenset([47, 48, 49, 50, 51, 52])
    FOLLOW_set_in_attribBody1043 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_term_in_attribBody1087 = frozenset([1])
    FOLLOW_declaration_in_declarationset1102 = frozenset([1, 23])
    FOLLOW_SEMI_in_declarationset1105 = frozenset([30, 44])
    FOLLOW_declaration_in_declarationset1108 = frozenset([1, 23])
    FOLLOW_SEMI_in_declarationset1112 = frozenset([1])
    FOLLOW_property_in_declaration1132 = frozenset([32])
    FOLLOW_COLON_in_declaration1134 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_expr_in_declaration1136 = frozenset([1, 53])
    FOLLOW_prio_in_declaration1138 = frozenset([1])
    FOLLOW_property_in_declaration1161 = frozenset([32])
    FOLLOW_COLON_in_declaration1163 = frozenset([1])
    FOLLOW_IDENT_in_property1188 = frozenset([1])
    FOLLOW_STAR_in_property1198 = frozenset([30])
    FOLLOW_IDENT_in_property1202 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1225 = frozenset([1])
    FOLLOW_term_in_expr1236 = frozenset([1, 22, 25, 29, 30, 37, 38, 39, 41, 45, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_operator_in_expr1239 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_term_in_expr1242 = frozenset([1, 22, 25, 29, 30, 37, 38, 39, 41, 45, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_SOLIDUS_in_operator1257 = frozenset([1])
    FOLLOW_COMMA_in_operator1262 = frozenset([1])
    FOLLOW_unaryOperator_in_term1281 = frozenset([30, 37, 39, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68])
    FOLLOW_NUMBER_in_term1290 = frozenset([1])
    FOLLOW_PERCENTAGE_in_term1307 = frozenset([1])
    FOLLOW_LENGTH_in_term1324 = frozenset([1])
    FOLLOW_EMS_in_term1341 = frozenset([1])
    FOLLOW_EXS_in_term1360 = frozenset([1])
    FOLLOW_REMS_in_term1379 = frozenset([1])
    FOLLOW_CHS_in_term1398 = frozenset([1])
    FOLLOW_ANGLE_in_term1417 = frozenset([1])
    FOLLOW_TIME_in_term1436 = frozenset([1])
    FOLLOW_FREQ_in_term1455 = frozenset([1])
    FOLLOW_RESOLUTION_in_term1474 = frozenset([1])
    FOLLOW_VPORTLEN_in_term1491 = frozenset([1])
    FOLLOW_NTH_in_term1508 = frozenset([1])
    FOLLOW_function_in_term1527 = frozenset([1])
    FOLLOW_STRING_in_term1546 = frozenset([1])
    FOLLOW_IDENT_in_term1551 = frozenset([1])
    FOLLOW_URI_in_term1556 = frozenset([1])
    FOLLOW_hexColor_in_term1561 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term1575 = frozenset([1])
    FOLLOW_LESS_VARNAME_in_term1580 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1608 = frozenset([30])
    FOLLOW_fnct_args_in_function1610 = frozenset([33])
    FOLLOW_RPAREN_in_function1612 = frozenset([1])
    FOLLOW_fnct_name_in_function1630 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_expr_in_function1632 = frozenset([33])
    FOLLOW_RPAREN_in_function1634 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1664 = frozenset([32, 42])
    FOLLOW_set_in_fnct_name1666 = frozenset([30, 32, 42, 45])
    FOLLOW_FUNCTION_in_fnct_name1676 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1690 = frozenset([1, 29])
    FOLLOW_COMMA_in_fnct_args1693 = frozenset([30])
    FOLLOW_fnct_arg_in_fnct_args1696 = frozenset([1, 29])
    FOLLOW_IDENT_in_fnct_arg1709 = frozenset([47])
    FOLLOW_OPEQ_in_fnct_arg1711 = frozenset([22, 25, 30, 37, 38, 39, 41, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68])
    FOLLOW_expr_in_fnct_arg1714 = frozenset([1])
    FOLLOW_HASH_in_hexColor1725 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss728 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss740 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
