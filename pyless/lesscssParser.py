# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-12-02 23:11:58

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



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
RBRACE=27
B=76
C=77
L=86
IMPORT_SYM=23
NMCHAR=72
M=87
SUBSTRINGMATCH=50
N=88
O=89
H=82
I=83
J=84
NUMBER=53
K=85
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
FONTFACE_SYM=33
OPEQ=45
N_Term=18
EXS=56
M_KeyframeSelector=9
N_Space=15
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
    # lesscss.g:67:1: styleSheet : ( charSet )? ( imports )* ( body )* EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) ;
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
                # lesscss.g:68:2: ( ( charSet )? ( imports )* ( body )* EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) )
                # lesscss.g:68:4: ( charSet )? ( imports )* ( body )* EOF
                pass 
                # lesscss.g:68:4: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:68:4: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet142)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:69:4: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:69:4: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet148)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                # lesscss.g:70:4: ( body )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MEDIA_SYM or LA3_0 == IDENT or LA3_0 == COLON or (FONTFACE_SYM <= LA3_0 <= KEYFRAMES_SYM) or (HASH <= LA3_0 <= STAR)) :
                        alt3 = 1


                    if alt3 == 1:
                        # lesscss.g:70:4: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_styleSheet154)
                        body3 = self.body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_body.add(body3.tree)


                    else:
                        break #loop3
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet160) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: body, imports, charSet
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
                    # 72:3: -> ^( N_StyleSheet ( charSet )? ( imports )* ( body )* )
                    # lesscss.g:72:6: ^( N_StyleSheet ( charSet )? ( imports )* ( body )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:72:21: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:72:30: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:72:39: ( body )*
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
    # lesscss.g:78:1: charSet : CHARSET_SYM STRING SEMI ;
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
                # lesscss.g:79:2: ( CHARSET_SYM STRING SEMI )
                # lesscss.g:79:4: CHARSET_SYM STRING SEMI
                pass 
                root_0 = self._adaptor.nil()

                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet192)
                if self._state.backtracking == 0:

                    CHARSET_SYM5_tree = self._adaptor.createWithPayload(CHARSET_SYM5)
                    root_0 = self._adaptor.becomeRoot(CHARSET_SYM5_tree, root_0)

                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet195)
                if self._state.backtracking == 0:

                    STRING6_tree = self._adaptor.createWithPayload(STRING6)
                    self._adaptor.addChild(root_0, STRING6_tree)

                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet197)



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
    # lesscss.g:85:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI ;
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
                # lesscss.g:86:2: ( IMPORT_SYM importUrl ( media_query_list )? SEMI )
                # lesscss.g:86:4: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports213)
                if self._state.backtracking == 0:

                    IMPORT_SYM8_tree = self._adaptor.createWithPayload(IMPORT_SYM8)
                    root_0 = self._adaptor.becomeRoot(IMPORT_SYM8_tree, root_0)

                self._state.following.append(self.FOLLOW_importUrl_in_imports216)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, importUrl9.tree)
                # lesscss.g:86:26: ( media_query_list )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((IDENT <= LA4_0 <= LPAREN)) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:86:26: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports218)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports221)



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
    # lesscss.g:89:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:90:2: ( STRING | URI )
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
    # lesscss.g:98:1: body : ( ruleSet | media | page | fontface | keyframes );
    def body(self, ):

        retval = self.body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet13 = None

        media14 = None

        page15 = None

        fontface16 = None

        keyframes17 = None



        try:
            try:
                # lesscss.g:99:2: ( ruleSet | media | page | fontface | keyframes )
                alt5 = 5
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
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # lesscss.g:99:4: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_body253)
                    ruleSet13 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet13.tree)


                elif alt5 == 2:
                    # lesscss.g:100:4: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_body258)
                    media14 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media14.tree)


                elif alt5 == 3:
                    # lesscss.g:101:4: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_body263)
                    page15 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page15.tree)


                elif alt5 == 4:
                    # lesscss.g:102:4: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_body268)
                    fontface16 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface16.tree)


                elif alt5 == 5:
                    # lesscss.g:103:4: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_body273)
                    keyframes17 = self.keyframes()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, keyframes17.tree)


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
    # lesscss.g:111:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( body )* RBRACE ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM18 = None
        LBRACE20 = None
        RBRACE22 = None
        media_query_list19 = None

        body21 = None


        MEDIA_SYM18_tree = None
        LBRACE20_tree = None
        RBRACE22_tree = None

        try:
            try:
                # lesscss.g:112:2: ( MEDIA_SYM ( media_query_list )? LBRACE ( body )* RBRACE )
                # lesscss.g:112:4: MEDIA_SYM ( media_query_list )? LBRACE ( body )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                MEDIA_SYM18=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media292)
                if self._state.backtracking == 0:

                    MEDIA_SYM18_tree = self._adaptor.createWithPayload(MEDIA_SYM18)
                    root_0 = self._adaptor.becomeRoot(MEDIA_SYM18_tree, root_0)

                # lesscss.g:112:15: ( media_query_list )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((IDENT <= LA6_0 <= LPAREN)) :
                    alt6 = 1
                if alt6 == 1:
                    # lesscss.g:112:15: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media295)
                    media_query_list19 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list19.tree)



                LBRACE20=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media300)
                # lesscss.g:114:4: ( body )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == MEDIA_SYM or LA7_0 == IDENT or LA7_0 == COLON or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM) or (HASH <= LA7_0 <= STAR)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:114:4: body
                        pass 
                        self._state.following.append(self.FOLLOW_body_in_media306)
                        body21 = self.body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, body21.tree)


                    else:
                        break #loop7
                RBRACE22=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media315)



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
    # lesscss.g:121:1: media_query_list : media_query ( COMMA media_query )* -> ( ^( N_MediaQuery media_query ) )+ ;
    def media_query_list(self, ):

        retval = self.media_query_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA24 = None
        media_query23 = None

        media_query25 = None


        COMMA24_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_media_query = RewriteRuleSubtreeStream(self._adaptor, "rule media_query")
        try:
            try:
                # lesscss.g:122:2: ( media_query ( COMMA media_query )* -> ( ^( N_MediaQuery media_query ) )+ )
                # lesscss.g:122:4: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list330)
                media_query23 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query23.tree)
                # lesscss.g:122:16: ( COMMA media_query )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # lesscss.g:122:17: COMMA media_query
                        pass 
                        COMMA24=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list333) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA24)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list335)
                        media_query25 = self.media_query()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_media_query.add(media_query25.tree)


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
                    # 123:3: -> ( ^( N_MediaQuery media_query ) )+
                    # lesscss.g:123:6: ( ^( N_MediaQuery media_query ) )+
                    if not (stream_media_query.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_media_query.hasNext():
                        # lesscss.g:123:6: ^( N_MediaQuery media_query )
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
    # lesscss.g:128:1: media_query : ( media_stmt | media_expr )+ ;
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        media_stmt26 = None

        media_expr27 = None



        try:
            try:
                # lesscss.g:129:2: ( ( media_stmt | media_expr )+ )
                # lesscss.g:129:4: ( media_stmt | media_expr )+
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:129:4: ( media_stmt | media_expr )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 3
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENT) :
                        alt9 = 1
                    elif (LA9_0 == LPAREN) :
                        alt9 = 2


                    if alt9 == 1:
                        # lesscss.g:129:6: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query364)
                        media_stmt26 = self.media_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_stmt26.tree)


                    elif alt9 == 2:
                        # lesscss.g:129:19: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query368)
                        media_expr27 = self.media_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_expr27.tree)


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
    # lesscss.g:132:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT28 = None

        IDENT28_tree = None

        try:
            try:
                # lesscss.g:133:2: ( IDENT )
                # lesscss.g:133:4: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT28=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt382)
                if self._state.backtracking == 0:

                    IDENT28_tree = self._adaptor.createWithPayload(IDENT28)
                    self._adaptor.addChild(root_0, IDENT28_tree)




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
    # lesscss.g:136:1: media_expr : LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN29 = None
        COLON31 = None
        RPAREN33 = None
        media_stmt30 = None

        expr32 = None


        LPAREN29_tree = None
        COLON31_tree = None
        RPAREN33_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_media_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule media_stmt")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:137:2: ( LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) )
                # lesscss.g:137:4: LPAREN media_stmt ( COLON expr )? RPAREN
                pass 
                LPAREN29=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr393) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN29)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr395)
                media_stmt30 = self.media_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_stmt.add(media_stmt30.tree)
                # lesscss.g:137:22: ( COLON expr )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == COLON) :
                    alt10 = 1
                if alt10 == 1:
                    # lesscss.g:137:24: COLON expr
                    pass 
                    COLON31=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr399) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON31)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr401)
                    expr32 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr32.tree)



                RPAREN33=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr406) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN33)

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
                    # 138:3: -> ^( N_MediaExpr media_stmt ( expr )? )
                    # lesscss.g:138:6: ^( N_MediaExpr media_stmt ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_stmt.nextTree())
                    # lesscss.g:138:31: ( expr )?
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
    # lesscss.g:145:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM34 = None
        LBRACE35 = None
        RBRACE37 = None
        declarationset36 = None


        FONTFACE_SYM34_tree = None
        LBRACE35_tree = None
        RBRACE37_tree = None

        try:
            try:
                # lesscss.g:146:2: ( FONTFACE_SYM LBRACE declarationset RBRACE )
                # lesscss.g:146:4: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                FONTFACE_SYM34=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface435)
                if self._state.backtracking == 0:

                    FONTFACE_SYM34_tree = self._adaptor.createWithPayload(FONTFACE_SYM34)
                    root_0 = self._adaptor.becomeRoot(FONTFACE_SYM34_tree, root_0)

                LBRACE35=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface438)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface441)
                declarationset36 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset36.tree)
                RBRACE37=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface443)



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
    # lesscss.g:152:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM38 = None
        LBRACE40 = None
        RBRACE42 = None
        pseudoPage39 = None

        declarationset41 = None


        PAGE_SYM38_tree = None
        LBRACE40_tree = None
        RBRACE42_tree = None

        try:
            try:
                # lesscss.g:153:2: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE )
                # lesscss.g:153:4: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                PAGE_SYM38=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page458)
                if self._state.backtracking == 0:

                    PAGE_SYM38_tree = self._adaptor.createWithPayload(PAGE_SYM38)
                    root_0 = self._adaptor.becomeRoot(PAGE_SYM38_tree, root_0)

                # lesscss.g:153:14: ( pseudoPage )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    alt11 = 1
                if alt11 == 1:
                    # lesscss.g:153:14: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page461)
                    pseudoPage39 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudoPage39.tree)



                LBRACE40=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page464)
                self._state.following.append(self.FOLLOW_declarationset_in_page467)
                declarationset41 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset41.tree)
                RBRACE42=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page469)



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
    # lesscss.g:156:1: pseudoPage : COLON a= IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON43 = None

        a_tree = None
        COLON43_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:157:2: ( COLON a= IDENT -> IDENT )
                # lesscss.g:157:4: COLON a= IDENT
                pass 
                COLON43=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage481) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON43)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage485) 
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
                    # 159:3: -> IDENT
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
    # lesscss.g:166:1: keyframes : KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE ;
    def keyframes(self, ):

        retval = self.keyframes_return()
        retval.start = self.input.LT(1)

        root_0 = None

        KEYFRAMES_SYM44 = None
        IDENT45 = None
        LBRACE46 = None
        RBRACE48 = None
        keyframes_block47 = None


        KEYFRAMES_SYM44_tree = None
        IDENT45_tree = None
        LBRACE46_tree = None
        RBRACE48_tree = None

        try:
            try:
                # lesscss.g:167:2: ( KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE )
                # lesscss.g:167:4: KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                KEYFRAMES_SYM44=self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes511)
                if self._state.backtracking == 0:

                    KEYFRAMES_SYM44_tree = self._adaptor.createWithPayload(KEYFRAMES_SYM44)
                    root_0 = self._adaptor.becomeRoot(KEYFRAMES_SYM44_tree, root_0)

                IDENT45=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes514)
                if self._state.backtracking == 0:

                    IDENT45_tree = self._adaptor.createWithPayload(IDENT45)
                    self._adaptor.addChild(root_0, IDENT45_tree)

                LBRACE46=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes516)
                # lesscss.g:167:33: ( keyframes_block )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == IDENT or LA12_0 == PERCENTAGE) :
                        alt12 = 1


                    if alt12 == 1:
                        # lesscss.g:167:33: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes519)
                        keyframes_block47 = self.keyframes_block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, keyframes_block47.tree)


                    else:
                        break #loop12
                RBRACE48=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes522)



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
    # lesscss.g:170:1: keyframes_block : keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) ;
    def keyframes_block(self, ):

        retval = self.keyframes_block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA50 = None
        LBRACE52 = None
        RBRACE54 = None
        keyframe_selector49 = None

        keyframe_selector51 = None

        declarationset53 = None


        COMMA50_tree = None
        LBRACE52_tree = None
        RBRACE54_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_keyframe_selector = RewriteRuleSubtreeStream(self._adaptor, "rule keyframe_selector")
        try:
            try:
                # lesscss.g:171:2: ( keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) )
                # lesscss.g:171:4: keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block534)
                keyframe_selector49 = self.keyframe_selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_keyframe_selector.add(keyframe_selector49.tree)
                # lesscss.g:171:22: ( COMMA keyframe_selector )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == COMMA) :
                        alt13 = 1


                    if alt13 == 1:
                        # lesscss.g:171:24: COMMA keyframe_selector
                        pass 
                        COMMA50=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keyframes_block538) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA50)
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block540)
                        keyframe_selector51 = self.keyframe_selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_keyframe_selector.add(keyframe_selector51.tree)


                    else:
                        break #loop13
                LBRACE52=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes_block545) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE52)
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block547)
                declarationset53 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset53.tree)
                RBRACE54=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes_block549) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE54)

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
                    # 172:3: -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    # lesscss.g:172:6: ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_KeyframeBlock, "N_KeyframeBlock"), root_1)

                    # lesscss.g:172:24: ( ^( M_KeyframeSelector keyframe_selector ) )+
                    if not (stream_keyframe_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_keyframe_selector.hasNext():
                        # lesscss.g:172:24: ^( M_KeyframeSelector keyframe_selector )
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
    # lesscss.g:176:1: keyframe_selector : ( IDENT | PERCENTAGE ) ;
    def keyframe_selector(self, ):

        retval = self.keyframe_selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # lesscss.g:177:2: ( ( IDENT | PERCENTAGE ) )
                # lesscss.g:177:4: ( IDENT | PERCENTAGE )
                pass 
                root_0 = self._adaptor.nil()

                set55 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == PERCENTAGE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set55))
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

    class ruleSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.ruleSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleSet"
    # lesscss.g:184:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA57 = None
        LBRACE59 = None
        RBRACE61 = None
        selector56 = None

        selector58 = None

        declarationset60 = None


        COMMA57_tree = None
        LBRACE59_tree = None
        RBRACE61_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:185:2: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:185:4: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet602)
                selector56 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector56.tree)
                # lesscss.g:185:13: ( COMMA selector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1


                    if alt14 == 1:
                        # lesscss.g:185:14: COMMA selector
                        pass 
                        COMMA57=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet605) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA57)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet607)
                        selector58 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector58.tree)


                    else:
                        break #loop14
                LBRACE59=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet611) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE59)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet613)
                declarationset60 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset60.tree)
                RBRACE61=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet615) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE61)

                # AST Rewrite
                # elements: selector, declarationset
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
                    # 186:3: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:186:6: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:186:18: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:186:18: ^( N_Selector selector )
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
    # lesscss.g:189:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector62 = None

        combinator63 = None

        simpleSelector64 = None



        try:
            try:
                # lesscss.g:190:2: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:190:4: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector643)
                simpleSelector62 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector62.tree)
                # lesscss.g:190:19: ( combinator simpleSelector )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == IDENT or LA15_0 == COLON or (PLUS <= LA15_0 <= STAR)) :
                        alt15 = 1


                    if alt15 == 1:
                        # lesscss.g:190:20: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector646)
                        combinator63 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator63.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector648)
                        simpleSelector64 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector64.tree)


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
    # lesscss.g:193:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS65 = None
        GREATER66 = None

        PLUS65_tree = None
        GREATER66_tree = None

        try:
            try:
                # lesscss.g:194:2: ( PLUS | GREATER | )
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
                    # lesscss.g:194:4: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS65=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator661)
                    if self._state.backtracking == 0:

                        PLUS65_tree = self._adaptor.createWithPayload(PLUS65)
                        self._adaptor.addChild(root_0, PLUS65_tree)



                elif alt16 == 2:
                    # lesscss.g:195:4: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER66=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator666)
                    if self._state.backtracking == 0:

                        GREATER66_tree = self._adaptor.createWithPayload(GREATER66)
                        self._adaptor.addChild(root_0, GREATER66_tree)



                elif alt16 == 3:
                    # lesscss.g:197:2: 
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
    # lesscss.g:199:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName67 = None

        elementSubsequent68 = None

        elementSubsequent69 = None



        try:
            try:
                # lesscss.g:200:2: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
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
                    # lesscss.g:200:4: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector680)
                    elementName67 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName67.tree)
                    # lesscss.g:200:16: ( ( esPred )=> elementSubsequent )*
                    while True: #loop17
                        alt17 = 2
                        alt17 = self.dfa17.predict(self.input)
                        if alt17 == 1:
                            # lesscss.g:200:17: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector687)
                            elementSubsequent68 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent68.tree)


                        else:
                            break #loop17


                elif alt19 == 2:
                    # lesscss.g:201:4: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:201:4: ( ( esPred )=> elementSubsequent )+
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
                            # lesscss.g:201:5: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector699)
                            elementSubsequent69 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent69.tree)


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
    # lesscss.g:204:1: esPred : ( HASH | DOT | COLON | LBRACKET );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set70 = None

        set70_tree = None

        try:
            try:
                # lesscss.g:205:2: ( HASH | DOT | COLON | LBRACKET )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set70 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set70))
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
    # lesscss.g:211:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set71 = None

        set71_tree = None

        try:
            try:
                # lesscss.g:212:2: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set71 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set71))
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
    # lesscss.g:216:1: elementSubsequent : ( HASH | cssClass | pseudo | attrib );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH72 = None
        cssClass73 = None

        pseudo74 = None

        attrib75 = None


        HASH72_tree = None

        try:
            try:
                # lesscss.g:217:2: ( HASH | cssClass | pseudo | attrib )
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
                    # lesscss.g:217:4: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH72=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent761)
                    if self._state.backtracking == 0:

                        HASH72_tree = self._adaptor.createWithPayload(HASH72)
                        self._adaptor.addChild(root_0, HASH72_tree)



                elif alt20 == 2:
                    # lesscss.g:218:4: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent766)
                    cssClass73 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass73.tree)


                elif alt20 == 3:
                    # lesscss.g:219:4: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent771)
                    pseudo74 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo74.tree)


                elif alt20 == 4:
                    # lesscss.g:220:4: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent776)
                    attrib75 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib75.tree)


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
    # lesscss.g:223:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT76 = None

        a_tree = None
        DOT76_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:224:2: ( DOT a= IDENT -> IDENT )
                # lesscss.g:224:4: DOT a= IDENT
                pass 
                DOT76=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass787) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT76)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass791) 
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
                    # 226:3: -> IDENT
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
    # lesscss.g:229:1: pseudo : a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) ;
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        IDENT77 = None
        pseudoFunction78 = None


        a_tree = None
        b_tree = None
        IDENT77_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_pseudoFunction = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoFunction")
        try:
            try:
                # lesscss.g:230:2: (a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) )
                # lesscss.g:230:4: a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
                pass 
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo815) 
                if self._state.backtracking == 0:
                    stream_COLON.add(a)
                # lesscss.g:230:13: (b= COLON )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == COLON) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:230:13: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo819) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(b)



                # lesscss.g:231:2: ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
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
                    # lesscss.g:231:4: IDENT
                    pass 
                    IDENT77=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo825) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT77)

                    # AST Rewrite
                    # elements: IDENT, a, b
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
                        # 232:3: -> ^( N_Pseudo $a ( $b)? IDENT )
                        # lesscss.g:232:6: ^( N_Pseudo $a ( $b)? IDENT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:232:20: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 2:
                    # lesscss.g:233:4: pseudoFunction
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoFunction_in_pseudo847)
                    pseudoFunction78 = self.pseudoFunction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoFunction.add(pseudoFunction78.tree)

                    # AST Rewrite
                    # elements: pseudoFunction, b, a
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
                        # 234:3: -> ^( N_Pseudo $a ( $b)? pseudoFunction )
                        # lesscss.g:234:6: ^( N_Pseudo $a ( $b)? pseudoFunction )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:234:20: ( $b)?
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
    # lesscss.g:238:1: pseudoFunction : ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) );
    def pseudoFunction(self, ):

        retval = self.pseudoFunction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FUNCTION79 = None
        RPAREN81 = None
        FUNCTION82 = None
        LBRACKET83 = None
        RBRACKET85 = None
        RPAREN86 = None
        FUNCTION87 = None
        RPAREN89 = None
        expr80 = None

        attribBody84 = None

        pseudo88 = None


        FUNCTION79_tree = None
        RPAREN81_tree = None
        FUNCTION82_tree = None
        LBRACKET83_tree = None
        RBRACKET85_tree = None
        RPAREN86_tree = None
        FUNCTION87_tree = None
        RPAREN89_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        stream_pseudo = RewriteRuleSubtreeStream(self._adaptor, "rule pseudo")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:239:2: ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) )
                alt23 = 3
                LA23_0 = self.input.LA(1)

                if (LA23_0 == FUNCTION) :
                    LA23 = self.input.LA(2)
                    if LA23 == LBRACKET:
                        alt23 = 2
                    elif LA23 == COLON:
                        alt23 = 3
                    elif LA23 == STRING or LA23 == URI or LA23 == IDENT or LA23 == PERCENTAGE or LA23 == PLUS or LA23 == HASH or LA23 == FUNCTION or LA23 == NUMBER or LA23 == LENGTH or LA23 == EMS or LA23 == EXS or LA23 == REMS or LA23 == CHS or LA23 == ANGLE or LA23 == TIME or LA23 == FREQ or LA23 == RESOLUTION or LA23 == VPORTLEN or LA23 == NTH or LA23 == UNICODE_RANGE or LA23 == MINUS:
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
                    # lesscss.g:239:4: FUNCTION expr RPAREN
                    pass 
                    FUNCTION79=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction878) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION79)
                    self._state.following.append(self.FOLLOW_expr_in_pseudoFunction880)
                    expr80 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr80.tree)
                    RPAREN81=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction882) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN81)

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
                        # 240:3: -> ^( N_PseudoFunction FUNCTION expr )
                        # lesscss.g:240:6: ^( N_PseudoFunction FUNCTION expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 2:
                    # lesscss.g:242:4: FUNCTION LBRACKET attribBody RBRACKET RPAREN
                    pass 
                    FUNCTION82=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction901) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION82)
                    LBRACKET83=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudoFunction903) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET83)
                    self._state.following.append(self.FOLLOW_attribBody_in_pseudoFunction905)
                    attribBody84 = self.attribBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_attribBody.add(attribBody84.tree)
                    RBRACKET85=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudoFunction907) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET85)
                    RPAREN86=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction909) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN86)

                    # AST Rewrite
                    # elements: LBRACKET, RBRACKET, FUNCTION, attribBody
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
                        # 243:3: -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        # lesscss.g:243:6: ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_LBRACKET.nextNode())
                        self._adaptor.addChild(root_1, stream_attribBody.nextTree())
                        self._adaptor.addChild(root_1, stream_RBRACKET.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 3:
                    # lesscss.g:245:4: FUNCTION pseudo RPAREN
                    pass 
                    FUNCTION87=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction932) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION87)
                    self._state.following.append(self.FOLLOW_pseudo_in_pseudoFunction934)
                    pseudo88 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudo.add(pseudo88.tree)
                    RPAREN89=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction936) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN89)

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
                        # 246:3: -> ^( N_PseudoFunction FUNCTION pseudo )
                        # lesscss.g:246:6: ^( N_PseudoFunction FUNCTION pseudo )
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
    # lesscss.g:250:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET90 = None
        RBRACKET92 = None
        attribBody91 = None


        LBRACKET90_tree = None
        RBRACKET92_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:251:2: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:251:4: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET90=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib961) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET90)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib963)
                attribBody91 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody91.tree)
                RBRACKET92=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib965) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET92)

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
                    # 252:3: -> ^( N_Attrib attribBody )
                    # lesscss.g:252:7: ^( N_Attrib attribBody )
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
    # lesscss.g:255:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT93 = None
        IDENT94 = None
        set95 = None
        term96 = None


        IDENT93_tree = None
        IDENT94_tree = None
        set95_tree = None

        try:
            try:
                # lesscss.g:256:2: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term )
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
                    # lesscss.g:256:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT93=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody988)
                    if self._state.backtracking == 0:

                        IDENT93_tree = self._adaptor.createWithPayload(IDENT93)
                        self._adaptor.addChild(root_0, IDENT93_tree)



                elif alt24 == 2:
                    # lesscss.g:257:4: IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT94=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody993)
                    if self._state.backtracking == 0:

                        IDENT94_tree = self._adaptor.createWithPayload(IDENT94)
                        self._adaptor.addChild(root_0, IDENT94_tree)

                    set95 = self.input.LT(1)
                    set95 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= SUBSTRINGMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set95), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_term_in_attribBody1042)
                    term96 = self.term()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, term96.tree)


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
    # lesscss.g:272:1: declarationset : ( declaration ( SEMI declaration )* ( SEMI )? | -> N_Empty );
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI98 = None
        SEMI100 = None
        declaration97 = None

        declaration99 = None


        SEMI98_tree = None
        SEMI100_tree = None

        try:
            try:
                # lesscss.g:273:2: ( declaration ( SEMI declaration )* ( SEMI )? | -> N_Empty )
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
                    # lesscss.g:273:4: declaration ( SEMI declaration )* ( SEMI )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_declaration_in_declarationset1057)
                    declaration97 = self.declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, declaration97.tree)
                    # lesscss.g:273:16: ( SEMI declaration )*
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == SEMI) :
                            LA25_1 = self.input.LA(2)

                            if (LA25_1 == IDENT or LA25_1 == STAR) :
                                alt25 = 1




                        if alt25 == 1:
                            # lesscss.g:273:17: SEMI declaration
                            pass 
                            SEMI98=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1060)
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset1063)
                            declaration99 = self.declaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, declaration99.tree)


                        else:
                            break #loop25
                    # lesscss.g:273:41: ( SEMI )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == SEMI) :
                        alt26 = 1
                    if alt26 == 1:
                        # lesscss.g:273:41: SEMI
                        pass 
                        SEMI100=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1067)





                elif alt27 == 2:
                    # lesscss.g:274:4: 
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
                        # 274:4: -> N_Empty
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
    # lesscss.g:277:1: declaration : ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) );
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON102 = None
        COLON106 = None
        property101 = None

        expr103 = None

        prio104 = None

        property105 = None


        COLON102_tree = None
        COLON106_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:278:2: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == IDENT) :
                    LA29_1 = self.input.LA(2)

                    if (LA29_1 == COLON) :
                        LA29_3 = self.input.LA(3)

                        if (LA29_3 == SEMI or LA29_3 == RBRACE) :
                            alt29 = 2
                        elif (LA29_3 == STRING or LA29_3 == URI or LA29_3 == IDENT or (PERCENTAGE <= LA29_3 <= PLUS) or LA29_3 == HASH or LA29_3 == FUNCTION or (NUMBER <= LA29_3 <= MINUS)) :
                            alt29 = 1
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

                            if (LA29_3 == SEMI or LA29_3 == RBRACE) :
                                alt29 = 2
                            elif (LA29_3 == STRING or LA29_3 == URI or LA29_3 == IDENT or (PERCENTAGE <= LA29_3 <= PLUS) or LA29_3 == HASH or LA29_3 == FUNCTION or (NUMBER <= LA29_3 <= MINUS)) :
                                alt29 = 1
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
                    # lesscss.g:278:4: property COLON expr ( prio )?
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1087)
                    property101 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property101.tree)
                    COLON102=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1089) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON102)
                    self._state.following.append(self.FOLLOW_expr_in_declaration1091)
                    expr103 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr103.tree)
                    # lesscss.g:278:24: ( prio )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == IMPORTANT_SYM) :
                        alt28 = 1
                    if alt28 == 1:
                        # lesscss.g:278:24: prio
                        pass 
                        self._state.following.append(self.FOLLOW_prio_in_declaration1093)
                        prio104 = self.prio()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_prio.add(prio104.tree)




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
                        # 279:3: -> ^( N_Declaration property expr ( prio )? )
                        # lesscss.g:279:6: ^( N_Declaration property expr ( prio )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                        self._adaptor.addChild(root_1, stream_property.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())
                        # lesscss.g:279:36: ( prio )?
                        if stream_prio.hasNext():
                            self._adaptor.addChild(root_1, stream_prio.nextTree())


                        stream_prio.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 2:
                    # lesscss.g:281:5: property COLON
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1116)
                    property105 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property105.tree)
                    COLON106=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1118) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON106)

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
                        # 282:3: -> ^( N_Declaration property )
                        # lesscss.g:282:6: ^( N_Declaration property )
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
    # lesscss.g:286:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT107 = None
        STAR108 = None

        a_tree = None
        IDENT107_tree = None
        STAR108_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:287:2: ( IDENT | STAR a= IDENT -> IDENT )
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
                    # lesscss.g:287:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT107=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1143)
                    if self._state.backtracking == 0:

                        IDENT107_tree = self._adaptor.createWithPayload(IDENT107)
                        self._adaptor.addChild(root_0, IDENT107_tree)



                elif alt30 == 2:
                    # lesscss.g:291:4: STAR a= IDENT
                    pass 
                    STAR108=self.match(self.input, STAR, self.FOLLOW_STAR_in_property1153) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR108)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1157) 
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
                        # 293:3: -> IDENT
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
    # lesscss.g:296:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM109 = None

        IMPORTANT_SYM109_tree = None

        try:
            try:
                # lesscss.g:297:2: ( IMPORTANT_SYM )
                # lesscss.g:297:4: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM109=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1179)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM109_tree = self._adaptor.createWithPayload(IMPORTANT_SYM109)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM109_tree)




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
    # lesscss.g:300:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term110 = None

        operator111 = None

        term112 = None



        try:
            try:
                # lesscss.g:301:2: ( term ( operator term )* )
                # lesscss.g:301:4: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1190)
                term110 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term110.tree)
                # lesscss.g:301:9: ( operator term )*
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
                        # lesscss.g:301:10: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1193)
                        operator111 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator111.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1196)
                        term112 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term112.tree)


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
    # lesscss.g:304:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS113 = None
        COMMA114 = None

        SOLIDUS113_tree = None
        COMMA114_tree = None

        try:
            try:
                # lesscss.g:305:2: ( SOLIDUS | COMMA | -> N_Space )
                alt32 = 3
                LA32 = self.input.LA(1)
                if LA32 == SOLIDUS:
                    alt32 = 1
                elif LA32 == COMMA:
                    alt32 = 2
                elif LA32 == STRING or LA32 == URI or LA32 == IDENT or LA32 == PERCENTAGE or LA32 == PLUS or LA32 == HASH or LA32 == FUNCTION or LA32 == NUMBER or LA32 == LENGTH or LA32 == EMS or LA32 == EXS or LA32 == REMS or LA32 == CHS or LA32 == ANGLE or LA32 == TIME or LA32 == FREQ or LA32 == RESOLUTION or LA32 == VPORTLEN or LA32 == NTH or LA32 == UNICODE_RANGE or LA32 == MINUS:
                    alt32 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # lesscss.g:305:4: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS113=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1211)
                    if self._state.backtracking == 0:

                        SOLIDUS113_tree = self._adaptor.createWithPayload(SOLIDUS113)
                        self._adaptor.addChild(root_0, SOLIDUS113_tree)



                elif alt32 == 2:
                    # lesscss.g:306:4: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA114=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1216)
                    if self._state.backtracking == 0:

                        COMMA114_tree = self._adaptor.createWithPayload(COMMA114)
                        self._adaptor.addChild(root_0, COMMA114_tree)



                elif alt32 == 3:
                    # lesscss.g:307:4: 
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
                        # 307:4: -> N_Space
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
    # lesscss.g:310:1: term : ( ( unaryOperator )? ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NUMBER116 = None
        PERCENTAGE117 = None
        LENGTH118 = None
        EMS119 = None
        EXS120 = None
        REMS121 = None
        CHS122 = None
        ANGLE123 = None
        TIME124 = None
        FREQ125 = None
        RESOLUTION126 = None
        VPORTLEN127 = None
        NTH128 = None
        STRING130 = None
        IDENT131 = None
        URI132 = None
        UNICODE_RANGE134 = None
        unaryOperator115 = None

        function129 = None

        hexColor133 = None


        NUMBER116_tree = None
        PERCENTAGE117_tree = None
        LENGTH118_tree = None
        EMS119_tree = None
        EXS120_tree = None
        REMS121_tree = None
        CHS122_tree = None
        ANGLE123_tree = None
        TIME124_tree = None
        FREQ125_tree = None
        RESOLUTION126_tree = None
        VPORTLEN127_tree = None
        NTH128_tree = None
        STRING130_tree = None
        IDENT131_tree = None
        URI132_tree = None
        UNICODE_RANGE134_tree = None
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
        stream_function = RewriteRuleSubtreeStream(self._adaptor, "rule function")
        try:
            try:
                # lesscss.g:311:2: ( ( unaryOperator )? ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE )
                alt35 = 6
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
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # lesscss.g:311:4: ( unaryOperator )? ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) )
                    pass 
                    # lesscss.g:311:4: ( unaryOperator )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == PLUS or LA33_0 == MINUS) :
                        alt33 = 1
                    if alt33 == 1:
                        # lesscss.g:311:4: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1235)
                        unaryOperator115 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_unaryOperator.add(unaryOperator115.tree)



                    # lesscss.g:311:19: ( NUMBER -> ^( N_Term ( unaryOperator )? NUMBER ) | PERCENTAGE -> ^( N_Term ( unaryOperator )? PERCENTAGE ) | LENGTH -> ^( N_Term ( unaryOperator )? LENGTH ) | EMS -> ^( N_Term ( unaryOperator )? EMS ) | EXS -> ^( N_Term ( unaryOperator )? EXS ) | REMS -> ^( N_Term ( unaryOperator )? REMS ) | CHS -> ^( N_Term ( unaryOperator )? CHS ) | ANGLE -> ^( N_Term ( unaryOperator )? ANGLE ) | TIME -> ^( N_Term ( unaryOperator )? TIME ) | FREQ -> ^( N_Term ( unaryOperator )? FREQ ) | RESOLUTION -> ^( N_Term ( unaryOperator )? RESOLUTION ) | VPORTLEN -> ^( N_Term ( unaryOperator )? VPORTLEN ) | NTH -> ^( N_Term ( unaryOperator )? NTH ) | function -> ^( N_Term ( unaryOperator )? function ) )
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
                        # lesscss.g:312:5: NUMBER
                        pass 
                        NUMBER116=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_term1244) 
                        if self._state.backtracking == 0:
                            stream_NUMBER.add(NUMBER116)

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
                            # 312:12: -> ^( N_Term ( unaryOperator )? NUMBER )
                            # lesscss.g:312:15: ^( N_Term ( unaryOperator )? NUMBER )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:312:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_NUMBER.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 2:
                        # lesscss.g:313:5: PERCENTAGE
                        pass 
                        PERCENTAGE117=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_term1261) 
                        if self._state.backtracking == 0:
                            stream_PERCENTAGE.add(PERCENTAGE117)

                        # AST Rewrite
                        # elements: PERCENTAGE, unaryOperator
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
                            # 313:16: -> ^( N_Term ( unaryOperator )? PERCENTAGE )
                            # lesscss.g:313:19: ^( N_Term ( unaryOperator )? PERCENTAGE )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:313:28: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_PERCENTAGE.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 3:
                        # lesscss.g:314:5: LENGTH
                        pass 
                        LENGTH118=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_term1278) 
                        if self._state.backtracking == 0:
                            stream_LENGTH.add(LENGTH118)

                        # AST Rewrite
                        # elements: unaryOperator, LENGTH
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
                            # 314:12: -> ^( N_Term ( unaryOperator )? LENGTH )
                            # lesscss.g:314:15: ^( N_Term ( unaryOperator )? LENGTH )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:314:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_LENGTH.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 4:
                        # lesscss.g:315:5: EMS
                        pass 
                        EMS119=self.match(self.input, EMS, self.FOLLOW_EMS_in_term1295) 
                        if self._state.backtracking == 0:
                            stream_EMS.add(EMS119)

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
                            # 315:11: -> ^( N_Term ( unaryOperator )? EMS )
                            # lesscss.g:315:14: ^( N_Term ( unaryOperator )? EMS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:315:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_EMS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 5:
                        # lesscss.g:316:5: EXS
                        pass 
                        EXS120=self.match(self.input, EXS, self.FOLLOW_EXS_in_term1314) 
                        if self._state.backtracking == 0:
                            stream_EXS.add(EXS120)

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
                            # 316:11: -> ^( N_Term ( unaryOperator )? EXS )
                            # lesscss.g:316:14: ^( N_Term ( unaryOperator )? EXS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:316:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_EXS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 6:
                        # lesscss.g:317:5: REMS
                        pass 
                        REMS121=self.match(self.input, REMS, self.FOLLOW_REMS_in_term1333) 
                        if self._state.backtracking == 0:
                            stream_REMS.add(REMS121)

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
                            # 317:12: -> ^( N_Term ( unaryOperator )? REMS )
                            # lesscss.g:317:15: ^( N_Term ( unaryOperator )? REMS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:317:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_REMS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 7:
                        # lesscss.g:318:5: CHS
                        pass 
                        CHS122=self.match(self.input, CHS, self.FOLLOW_CHS_in_term1352) 
                        if self._state.backtracking == 0:
                            stream_CHS.add(CHS122)

                        # AST Rewrite
                        # elements: CHS, unaryOperator
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
                            # 318:11: -> ^( N_Term ( unaryOperator )? CHS )
                            # lesscss.g:318:14: ^( N_Term ( unaryOperator )? CHS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:318:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_CHS.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 8:
                        # lesscss.g:319:5: ANGLE
                        pass 
                        ANGLE123=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_term1371) 
                        if self._state.backtracking == 0:
                            stream_ANGLE.add(ANGLE123)

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
                            # 319:13: -> ^( N_Term ( unaryOperator )? ANGLE )
                            # lesscss.g:319:16: ^( N_Term ( unaryOperator )? ANGLE )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:319:25: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_ANGLE.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 9:
                        # lesscss.g:320:5: TIME
                        pass 
                        TIME124=self.match(self.input, TIME, self.FOLLOW_TIME_in_term1390) 
                        if self._state.backtracking == 0:
                            stream_TIME.add(TIME124)

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
                            # 320:12: -> ^( N_Term ( unaryOperator )? TIME )
                            # lesscss.g:320:15: ^( N_Term ( unaryOperator )? TIME )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:320:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_TIME.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 10:
                        # lesscss.g:321:5: FREQ
                        pass 
                        FREQ125=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_term1409) 
                        if self._state.backtracking == 0:
                            stream_FREQ.add(FREQ125)

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
                            # 321:12: -> ^( N_Term ( unaryOperator )? FREQ )
                            # lesscss.g:321:15: ^( N_Term ( unaryOperator )? FREQ )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:321:24: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_FREQ.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 11:
                        # lesscss.g:322:5: RESOLUTION
                        pass 
                        RESOLUTION126=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_term1428) 
                        if self._state.backtracking == 0:
                            stream_RESOLUTION.add(RESOLUTION126)

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
                            # 322:16: -> ^( N_Term ( unaryOperator )? RESOLUTION )
                            # lesscss.g:322:19: ^( N_Term ( unaryOperator )? RESOLUTION )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:322:28: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_RESOLUTION.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 12:
                        # lesscss.g:323:5: VPORTLEN
                        pass 
                        VPORTLEN127=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_term1445) 
                        if self._state.backtracking == 0:
                            stream_VPORTLEN.add(VPORTLEN127)

                        # AST Rewrite
                        # elements: unaryOperator, VPORTLEN
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
                            # 323:14: -> ^( N_Term ( unaryOperator )? VPORTLEN )
                            # lesscss.g:323:17: ^( N_Term ( unaryOperator )? VPORTLEN )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:323:26: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_VPORTLEN.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 13:
                        # lesscss.g:324:5: NTH
                        pass 
                        NTH128=self.match(self.input, NTH, self.FOLLOW_NTH_in_term1462) 
                        if self._state.backtracking == 0:
                            stream_NTH.add(NTH128)

                        # AST Rewrite
                        # elements: unaryOperator, NTH
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
                            # 324:11: -> ^( N_Term ( unaryOperator )? NTH )
                            # lesscss.g:324:14: ^( N_Term ( unaryOperator )? NTH )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:324:23: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_NTH.nextNode())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0


                    elif alt34 == 14:
                        # lesscss.g:325:5: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_term1481)
                        function129 = self.function()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_function.add(function129.tree)

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
                            # 325:14: -> ^( N_Term ( unaryOperator )? function )
                            # lesscss.g:325:17: ^( N_Term ( unaryOperator )? function )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Term, "N_Term"), root_1)

                            # lesscss.g:325:26: ( unaryOperator )?
                            if stream_unaryOperator.hasNext():
                                self._adaptor.addChild(root_1, stream_unaryOperator.nextTree())


                            stream_unaryOperator.reset();
                            self._adaptor.addChild(root_1, stream_function.nextTree())

                            self._adaptor.addChild(root_0, root_1)



                            retval.tree = root_0





                elif alt35 == 2:
                    # lesscss.g:327:4: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING130=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1500)
                    if self._state.backtracking == 0:

                        STRING130_tree = self._adaptor.createWithPayload(STRING130)
                        self._adaptor.addChild(root_0, STRING130_tree)



                elif alt35 == 3:
                    # lesscss.g:328:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT131=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1505)
                    if self._state.backtracking == 0:

                        IDENT131_tree = self._adaptor.createWithPayload(IDENT131)
                        self._adaptor.addChild(root_0, IDENT131_tree)



                elif alt35 == 4:
                    # lesscss.g:329:4: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI132=self.match(self.input, URI, self.FOLLOW_URI_in_term1510)
                    if self._state.backtracking == 0:

                        URI132_tree = self._adaptor.createWithPayload(URI132)
                        self._adaptor.addChild(root_0, URI132_tree)



                elif alt35 == 5:
                    # lesscss.g:330:4: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1515)
                    hexColor133 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor133.tree)


                elif alt35 == 6:
                    # lesscss.g:331:4: UNICODE_RANGE
                    pass 
                    root_0 = self._adaptor.nil()

                    UNICODE_RANGE134=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term1520)
                    if self._state.backtracking == 0:

                        UNICODE_RANGE134_tree = self._adaptor.createWithPayload(UNICODE_RANGE134)
                        self._adaptor.addChild(root_0, UNICODE_RANGE134_tree)



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
    # lesscss.g:334:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set135 = None

        set135_tree = None

        try:
            try:
                # lesscss.g:335:2: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set135 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set135))
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
    # lesscss.g:340:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name ^( N_Expr expr ) ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN138 = None
        RPAREN141 = None
        fnct_name136 = None

        fnct_args137 = None

        fnct_name139 = None

        expr140 = None


        RPAREN138_tree = None
        RPAREN141_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:341:2: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name ^( N_Expr expr ) ) )
                alt36 = 2
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # lesscss.g:341:4: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1548)
                    fnct_name136 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name136.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1550)
                    fnct_args137 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args137.tree)
                    RPAREN138=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1552) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN138)

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
                        # 342:3: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:342:6: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 2:
                    # lesscss.g:344:4: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1570)
                    fnct_name139 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name139.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1572)
                    expr140 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr140.tree)
                    RPAREN141=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1574) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN141)

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
                        # 345:3: -> ^( N_Function fnct_name ^( N_Expr expr ) )
                        # lesscss.g:345:6: ^( N_Function fnct_name ^( N_Expr expr ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        # lesscss.g:345:29: ^( N_Expr expr )
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
    # lesscss.g:349:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT142 = None
        set143 = None
        FUNCTION144 = None

        IDENT142_tree = None
        set143_tree = None
        FUNCTION144_tree = None

        try:
            try:
                # lesscss.g:350:2: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:350:4: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:350:4: ( IDENT ( COLON | DOT )+ )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == IDENT) :
                        alt38 = 1


                    if alt38 == 1:
                        # lesscss.g:350:5: IDENT ( COLON | DOT )+
                        pass 
                        IDENT142=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1604)
                        if self._state.backtracking == 0:

                            IDENT142_tree = self._adaptor.createWithPayload(IDENT142)
                            self._adaptor.addChild(root_0, IDENT142_tree)

                        # lesscss.g:350:11: ( COLON | DOT )+
                        cnt37 = 0
                        while True: #loop37
                            alt37 = 2
                            LA37_0 = self.input.LA(1)

                            if (LA37_0 == COLON or LA37_0 == DOT) :
                                alt37 = 1


                            if alt37 == 1:
                                # lesscss.g:
                                pass 
                                set143 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set143))
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
                FUNCTION144=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1616)
                if self._state.backtracking == 0:

                    FUNCTION144_tree = self._adaptor.createWithPayload(FUNCTION144)
                    root_0 = self._adaptor.becomeRoot(FUNCTION144_tree, root_0)




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
    # lesscss.g:353:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA146 = None
        fnct_arg145 = None

        fnct_arg147 = None


        COMMA146_tree = None

        try:
            try:
                # lesscss.g:354:2: ( fnct_arg ( COMMA fnct_arg )* )
                # lesscss.g:354:4: fnct_arg ( COMMA fnct_arg )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1630)
                fnct_arg145 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fnct_arg145.tree)
                # lesscss.g:354:13: ( COMMA fnct_arg )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == COMMA) :
                        alt39 = 1


                    if alt39 == 1:
                        # lesscss.g:354:14: COMMA fnct_arg
                        pass 
                        COMMA146=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1633)
                        if self._state.backtracking == 0:

                            COMMA146_tree = self._adaptor.createWithPayload(COMMA146)
                            root_0 = self._adaptor.becomeRoot(COMMA146_tree, root_0)

                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1636)
                        fnct_arg147 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fnct_arg147.tree)


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
    # lesscss.g:357:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT148 = None
        OPEQ149 = None
        expr150 = None


        IDENT148_tree = None
        OPEQ149_tree = None

        try:
            try:
                # lesscss.g:358:2: ( IDENT OPEQ expr )
                # lesscss.g:358:4: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT148=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1649)
                if self._state.backtracking == 0:

                    IDENT148_tree = self._adaptor.createWithPayload(IDENT148)
                    self._adaptor.addChild(root_0, IDENT148_tree)

                OPEQ149=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1651)
                if self._state.backtracking == 0:

                    OPEQ149_tree = self._adaptor.createWithPayload(OPEQ149)
                    root_0 = self._adaptor.becomeRoot(OPEQ149_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1654)
                expr150 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr150.tree)



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
    # lesscss.g:361:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH151 = None

        HASH151_tree = None

        try:
            try:
                # lesscss.g:362:2: ( HASH )
                # lesscss.g:362:4: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH151=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1665)
                if self._state.backtracking == 0:

                    HASH151_tree = self._adaptor.createWithPayload(HASH151)
                    self._adaptor.addChild(root_0, HASH151_tree)




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
        # lesscss.g:200:17: ( esPred )
        # lesscss.g:200:18: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss684)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:201:5: ( esPred )
        # lesscss.g:201:6: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss696)
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
        u"\1\32\3\uffff\4\0\3\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\1\52\3\uffff\4\0\3\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA17_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\1\1\uffff\2\1\1\uffff\1\6\5\uffff\2\1\1\4\1\5\1\7"
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
        u"\1\35\1\37\1\25\1\35\1\uffff\1\25\1\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\1\53\1\50\1\102\1\53\1\uffff\1\102\1\uffff"
        )

    DFA36_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA36_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\1\1\15\uffff\1\2"),
        DFA.unpack(u"\1\3\10\uffff\1\3"),
        DFA.unpack(u"\1\4\2\uffff\1\4\4\uffff\1\5\6\uffff\2\4\1\uffff\1"
        u"\4\3\uffff\1\4\11\uffff\16\4"),
        DFA.unpack(u"\1\1\1\uffff\1\3\10\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\1\4\3\uffff\2\4\1\uffff\2\4\3\uffff\2"
        u"\4\1\uffff\2\4\2\uffff\1\4\1\uffff\1\6\6\uffff\17\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #36

    class DFA36(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet142 = frozenset([23, 25, 29, 31, 33, 34, 35, 39, 40, 41, 42])
    FOLLOW_imports_in_styleSheet148 = frozenset([23, 25, 29, 31, 33, 34, 35, 39, 40, 41, 42])
    FOLLOW_body_in_styleSheet154 = frozenset([25, 29, 31, 33, 34, 35, 39, 40, 41, 42])
    FOLLOW_EOF_in_styleSheet160 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet192 = frozenset([21])
    FOLLOW_STRING_in_charSet195 = frozenset([22])
    FOLLOW_SEMI_in_charSet197 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports213 = frozenset([21, 24])
    FOLLOW_importUrl_in_imports216 = frozenset([22, 29, 30])
    FOLLOW_media_query_list_in_imports218 = frozenset([22])
    FOLLOW_SEMI_in_imports221 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body253 = frozenset([1])
    FOLLOW_media_in_body258 = frozenset([1])
    FOLLOW_page_in_body263 = frozenset([1])
    FOLLOW_fontface_in_body268 = frozenset([1])
    FOLLOW_keyframes_in_body273 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media292 = frozenset([26, 29, 30])
    FOLLOW_media_query_list_in_media295 = frozenset([26])
    FOLLOW_LBRACE_in_media300 = frozenset([25, 27, 29, 31, 33, 34, 35, 39, 40, 41, 42])
    FOLLOW_body_in_media306 = frozenset([25, 27, 29, 31, 33, 34, 35, 39, 40, 41, 42])
    FOLLOW_RBRACE_in_media315 = frozenset([1])
    FOLLOW_media_query_in_media_query_list330 = frozenset([1, 28])
    FOLLOW_COMMA_in_media_query_list333 = frozenset([29, 30])
    FOLLOW_media_query_in_media_query_list335 = frozenset([1, 28])
    FOLLOW_media_stmt_in_media_query364 = frozenset([1, 29, 30])
    FOLLOW_media_expr_in_media_query368 = frozenset([1, 29, 30])
    FOLLOW_IDENT_in_media_stmt382 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr393 = frozenset([29])
    FOLLOW_media_stmt_in_media_expr395 = frozenset([31, 32])
    FOLLOW_COLON_in_media_expr399 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_expr_in_media_expr401 = frozenset([32])
    FOLLOW_RPAREN_in_media_expr406 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface435 = frozenset([26])
    FOLLOW_LBRACE_in_fontface438 = frozenset([27, 29, 42])
    FOLLOW_declarationset_in_fontface441 = frozenset([27])
    FOLLOW_RBRACE_in_fontface443 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page458 = frozenset([26, 31])
    FOLLOW_pseudoPage_in_page461 = frozenset([26])
    FOLLOW_LBRACE_in_page464 = frozenset([27, 29, 42])
    FOLLOW_declarationset_in_page467 = frozenset([27])
    FOLLOW_RBRACE_in_page469 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage481 = frozenset([29])
    FOLLOW_IDENT_in_pseudoPage485 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes511 = frozenset([29])
    FOLLOW_IDENT_in_keyframes514 = frozenset([26])
    FOLLOW_LBRACE_in_keyframes516 = frozenset([27, 29, 36])
    FOLLOW_keyframes_block_in_keyframes519 = frozenset([27, 29, 36])
    FOLLOW_RBRACE_in_keyframes522 = frozenset([1])
    FOLLOW_keyframe_selector_in_keyframes_block534 = frozenset([26, 28])
    FOLLOW_COMMA_in_keyframes_block538 = frozenset([29, 36])
    FOLLOW_keyframe_selector_in_keyframes_block540 = frozenset([26, 28])
    FOLLOW_LBRACE_in_keyframes_block545 = frozenset([27, 29, 42])
    FOLLOW_declarationset_in_keyframes_block547 = frozenset([27])
    FOLLOW_RBRACE_in_keyframes_block549 = frozenset([1])
    FOLLOW_set_in_keyframe_selector579 = frozenset([1])
    FOLLOW_selector_in_ruleSet602 = frozenset([26, 28])
    FOLLOW_COMMA_in_ruleSet605 = frozenset([29, 31, 39, 40, 41, 42])
    FOLLOW_selector_in_ruleSet607 = frozenset([26, 28])
    FOLLOW_LBRACE_in_ruleSet611 = frozenset([27, 29, 42])
    FOLLOW_declarationset_in_ruleSet613 = frozenset([27])
    FOLLOW_RBRACE_in_ruleSet615 = frozenset([1])
    FOLLOW_simpleSelector_in_selector643 = frozenset([1, 29, 31, 37, 38, 39, 40, 41, 42])
    FOLLOW_combinator_in_selector646 = frozenset([29, 31, 39, 40, 41, 42])
    FOLLOW_simpleSelector_in_selector648 = frozenset([1, 29, 31, 37, 38, 39, 40, 41, 42])
    FOLLOW_PLUS_in_combinator661 = frozenset([1])
    FOLLOW_GREATER_in_combinator666 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector680 = frozenset([1, 29, 31, 39, 40, 41, 42])
    FOLLOW_elementSubsequent_in_simpleSelector687 = frozenset([1, 29, 31, 39, 40, 41, 42])
    FOLLOW_elementSubsequent_in_simpleSelector699 = frozenset([1, 29, 31, 39, 40, 41, 42])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent761 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent766 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent771 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent776 = frozenset([1])
    FOLLOW_DOT_in_cssClass787 = frozenset([29])
    FOLLOW_IDENT_in_cssClass791 = frozenset([1])
    FOLLOW_COLON_in_pseudo815 = frozenset([29, 31, 43])
    FOLLOW_COLON_in_pseudo819 = frozenset([29, 31, 43])
    FOLLOW_IDENT_in_pseudo825 = frozenset([1])
    FOLLOW_pseudoFunction_in_pseudo847 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction878 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_expr_in_pseudoFunction880 = frozenset([32])
    FOLLOW_RPAREN_in_pseudoFunction882 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction901 = frozenset([41])
    FOLLOW_LBRACKET_in_pseudoFunction903 = frozenset([29])
    FOLLOW_attribBody_in_pseudoFunction905 = frozenset([44])
    FOLLOW_RBRACKET_in_pseudoFunction907 = frozenset([32])
    FOLLOW_RPAREN_in_pseudoFunction909 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction932 = frozenset([31])
    FOLLOW_pseudo_in_pseudoFunction934 = frozenset([32])
    FOLLOW_RPAREN_in_pseudoFunction936 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib961 = frozenset([29])
    FOLLOW_attribBody_in_attrib963 = frozenset([44])
    FOLLOW_RBRACKET_in_attrib965 = frozenset([1])
    FOLLOW_IDENT_in_attribBody988 = frozenset([1])
    FOLLOW_IDENT_in_attribBody993 = frozenset([45, 46, 47, 48, 49, 50])
    FOLLOW_set_in_attribBody998 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_term_in_attribBody1042 = frozenset([1])
    FOLLOW_declaration_in_declarationset1057 = frozenset([1, 22])
    FOLLOW_SEMI_in_declarationset1060 = frozenset([29, 42])
    FOLLOW_declaration_in_declarationset1063 = frozenset([1, 22])
    FOLLOW_SEMI_in_declarationset1067 = frozenset([1])
    FOLLOW_property_in_declaration1087 = frozenset([31])
    FOLLOW_COLON_in_declaration1089 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_expr_in_declaration1091 = frozenset([1, 51])
    FOLLOW_prio_in_declaration1093 = frozenset([1])
    FOLLOW_property_in_declaration1116 = frozenset([31])
    FOLLOW_COLON_in_declaration1118 = frozenset([1])
    FOLLOW_IDENT_in_property1143 = frozenset([1])
    FOLLOW_STAR_in_property1153 = frozenset([29])
    FOLLOW_IDENT_in_property1157 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1179 = frozenset([1])
    FOLLOW_term_in_expr1190 = frozenset([1, 21, 24, 28, 29, 36, 37, 39, 43, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_operator_in_expr1193 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_term_in_expr1196 = frozenset([1, 21, 24, 28, 29, 36, 37, 39, 43, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_SOLIDUS_in_operator1211 = frozenset([1])
    FOLLOW_COMMA_in_operator1216 = frozenset([1])
    FOLLOW_unaryOperator_in_term1235 = frozenset([29, 36, 37, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66])
    FOLLOW_NUMBER_in_term1244 = frozenset([1])
    FOLLOW_PERCENTAGE_in_term1261 = frozenset([1])
    FOLLOW_LENGTH_in_term1278 = frozenset([1])
    FOLLOW_EMS_in_term1295 = frozenset([1])
    FOLLOW_EXS_in_term1314 = frozenset([1])
    FOLLOW_REMS_in_term1333 = frozenset([1])
    FOLLOW_CHS_in_term1352 = frozenset([1])
    FOLLOW_ANGLE_in_term1371 = frozenset([1])
    FOLLOW_TIME_in_term1390 = frozenset([1])
    FOLLOW_FREQ_in_term1409 = frozenset([1])
    FOLLOW_RESOLUTION_in_term1428 = frozenset([1])
    FOLLOW_VPORTLEN_in_term1445 = frozenset([1])
    FOLLOW_NTH_in_term1462 = frozenset([1])
    FOLLOW_function_in_term1481 = frozenset([1])
    FOLLOW_STRING_in_term1500 = frozenset([1])
    FOLLOW_IDENT_in_term1505 = frozenset([1])
    FOLLOW_URI_in_term1510 = frozenset([1])
    FOLLOW_hexColor_in_term1515 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term1520 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1548 = frozenset([29])
    FOLLOW_fnct_args_in_function1550 = frozenset([32])
    FOLLOW_RPAREN_in_function1552 = frozenset([1])
    FOLLOW_fnct_name_in_function1570 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_expr_in_function1572 = frozenset([32])
    FOLLOW_RPAREN_in_function1574 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1604 = frozenset([31, 40])
    FOLLOW_set_in_fnct_name1606 = frozenset([29, 31, 40, 43])
    FOLLOW_FUNCTION_in_fnct_name1616 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1630 = frozenset([1, 28])
    FOLLOW_COMMA_in_fnct_args1633 = frozenset([29])
    FOLLOW_fnct_arg_in_fnct_args1636 = frozenset([1, 28])
    FOLLOW_IDENT_in_fnct_arg1649 = frozenset([45])
    FOLLOW_OPEQ_in_fnct_arg1651 = frozenset([21, 24, 29, 36, 37, 39, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_expr_in_fnct_arg1654 = frozenset([1])
    FOLLOW_HASH_in_hexColor1665 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss684 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss696 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
