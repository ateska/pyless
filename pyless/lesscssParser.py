# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-18 03:40:47

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=40
UNICODE_RANGE=62
STAR=39
EOF=-1
MEDIA_SYM=22
INCLUDES=43
LBRACKET=38
RPAREN=29
NAME=70
GREATER=35
ESCAPE=67
DIMENSION=103
STRINGESC=101
NL=104
COMMENT=98
D=75
E=76
F=77
G=78
A=72
RBRACE=24
B=73
C=74
L=83
IMPORT_SYM=20
NMCHAR=69
M=84
SUBSTRINGMATCH=47
N=85
O=86
H=79
I=80
J=81
NUMBER=50
K=82
U=92
T=91
W=94
V=93
Q=88
P=87
S=90
CDO=99
R=89
CDC=100
Y=96
PERCENTAGE=33
URL=71
X=95
Z=97
URI=21
PAGE_SYM=31
WS=102
DASHMATCH=44
EMS=52
N_PseudoFunction=16
N_RuleSet=7
NONASCII=65
N_MediaQuery=5
N_Selector=10
LBRACE=23
LPAREN=27
LENGTH=51
IMPORTANT_SYM=48
N_Function=12
TIME=57
KEYFRAMES_SYM=32
COMMA=25
N_StyleSheet=4
IDENT=26
PLUS=34
FREQ=58
RBRACKET=41
DOT=37
VPORTLEN=60
CHARSET_SYM=17
ANGLE=56
REMS=54
HASH=36
HEXCHAR=64
RESOLUTION=59
PREFIXMATCH=45
MINUS=63
N_Pseudo=15
SOLIDUS=49
N_Empty=14
SEMI=19
UNICODE=66
CHS=55
COLON=28
NMSTART=68
N_Declaration=11
OPEQ=42
FONTFACE_SYM=30
EXS=53
M_KeyframeSelector=9
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=46
NTH=61
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Pseudo", "N_PseudoFunction", "CHARSET_SYM", "STRING", 
    "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", "COMMA", 
    "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", "KEYFRAMES_SYM", 
    "PERCENTAGE", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "STAR", 
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

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
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
    # lesscss.g:67:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) ;
    def styleSheet(self, ):

        retval = self.styleSheet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF4 = None
        charSet1 = None

        imports2 = None

        bodylist3 = None


        EOF4_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_bodylist = RewriteRuleSubtreeStream(self._adaptor, "rule bodylist")
        stream_charSet = RewriteRuleSubtreeStream(self._adaptor, "rule charSet")
        stream_imports = RewriteRuleSubtreeStream(self._adaptor, "rule imports")
        try:
            try:
                # lesscss.g:68:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) )
                # lesscss.g:68:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:68:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:68:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet186)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:69:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:69:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet197)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet208)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet218) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: imports, charSet, bodylist
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
                    # 72:13: -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    # lesscss.g:72:16: ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:72:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:72:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:72:49: ( bodylist )?
                    if stream_bodylist.hasNext():
                        self._adaptor.addChild(root_1, stream_bodylist.nextTree())


                    stream_bodylist.reset();

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
                # lesscss.g:79:5: ( CHARSET_SYM STRING SEMI )
                # lesscss.g:79:9: CHARSET_SYM STRING SEMI
                pass 
                root_0 = self._adaptor.nil()

                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet271)
                if self._state.backtracking == 0:

                    CHARSET_SYM5_tree = self._adaptor.createWithPayload(CHARSET_SYM5)
                    root_0 = self._adaptor.becomeRoot(CHARSET_SYM5_tree, root_0)

                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet274)
                if self._state.backtracking == 0:

                    STRING6_tree = self._adaptor.createWithPayload(STRING6)
                    self._adaptor.addChild(root_0, STRING6_tree)

                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet276)



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
                # lesscss.g:86:5: ( IMPORT_SYM importUrl ( media_query_list )? SEMI )
                # lesscss.g:86:9: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports300)
                if self._state.backtracking == 0:

                    IMPORT_SYM8_tree = self._adaptor.createWithPayload(IMPORT_SYM8)
                    root_0 = self._adaptor.becomeRoot(IMPORT_SYM8_tree, root_0)

                self._state.following.append(self.FOLLOW_importUrl_in_imports303)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, importUrl9.tree)
                # lesscss.g:86:31: ( media_query_list )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((IDENT <= LA3_0 <= LPAREN)) :
                    alt3 = 1
                if alt3 == 1:
                    # lesscss.g:86:31: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports305)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports308)



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
                # lesscss.g:90:5: ( STRING | URI )
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

    class bodylist_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodylist_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodylist"
    # lesscss.g:98:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset13 = None



        try:
            try:
                # lesscss.g:99:5: ( ( bodyset )* )
                # lesscss.g:99:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:99:7: ( bodyset )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == MEDIA_SYM or LA4_0 == IDENT or LA4_0 == COLON or (FONTFACE_SYM <= LA4_0 <= KEYFRAMES_SYM) or (HASH <= LA4_0 <= STAR)) :
                        alt4 = 1


                    if alt4 == 1:
                        # lesscss.g:99:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist355)
                        bodyset13 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset13.tree)


                    else:
                        break #loop4



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

    # $ANTLR end "bodylist"

    class bodyset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodyset_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodyset"
    # lesscss.g:102:1: bodyset : ( ruleSet | media | page | fontface | keyframes );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet14 = None

        media15 = None

        page16 = None

        fontface17 = None

        keyframes18 = None



        try:
            try:
                # lesscss.g:103:5: ( ruleSet | media | page | fontface | keyframes )
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
                    # lesscss.g:103:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset373)
                    ruleSet14 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet14.tree)


                elif alt5 == 2:
                    # lesscss.g:104:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset381)
                    media15 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media15.tree)


                elif alt5 == 3:
                    # lesscss.g:105:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset389)
                    page16 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page16.tree)


                elif alt5 == 4:
                    # lesscss.g:106:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset397)
                    fontface17 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface17.tree)


                elif alt5 == 5:
                    # lesscss.g:107:7: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_bodyset405)
                    keyframes18 = self.keyframes()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, keyframes18.tree)


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

    # $ANTLR end "bodyset"

    class media_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_return, self).__init__()

            self.tree = None




    # $ANTLR start "media"
    # lesscss.g:115:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( media_bodyset )* RBRACE ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM19 = None
        LBRACE21 = None
        RBRACE23 = None
        media_query_list20 = None

        media_bodyset22 = None


        MEDIA_SYM19_tree = None
        LBRACE21_tree = None
        RBRACE23_tree = None

        try:
            try:
                # lesscss.g:116:5: ( MEDIA_SYM ( media_query_list )? LBRACE ( media_bodyset )* RBRACE )
                # lesscss.g:116:7: MEDIA_SYM ( media_query_list )? LBRACE ( media_bodyset )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                MEDIA_SYM19=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media430)
                if self._state.backtracking == 0:

                    MEDIA_SYM19_tree = self._adaptor.createWithPayload(MEDIA_SYM19)
                    root_0 = self._adaptor.becomeRoot(MEDIA_SYM19_tree, root_0)

                # lesscss.g:116:18: ( media_query_list )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((IDENT <= LA6_0 <= LPAREN)) :
                    alt6 = 1
                if alt6 == 1:
                    # lesscss.g:116:18: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media433)
                    media_query_list20 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list20.tree)



                LBRACE21=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media444)
                # lesscss.g:118:13: ( media_bodyset )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == IDENT or LA7_0 == COLON or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM) or (HASH <= LA7_0 <= STAR)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:118:13: media_bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_media_bodyset_in_media459)
                        media_bodyset22 = self.media_bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_bodyset22.tree)


                    else:
                        break #loop7
                RBRACE23=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media470)



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

    class media_bodyset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_bodyset_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_bodyset"
    # lesscss.g:122:1: media_bodyset : ( ruleSet | page | fontface | keyframes );
    def media_bodyset(self, ):

        retval = self.media_bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet24 = None

        page25 = None

        fontface26 = None

        keyframes27 = None



        try:
            try:
                # lesscss.g:123:5: ( ruleSet | page | fontface | keyframes )
                alt8 = 4
                LA8 = self.input.LA(1)
                if LA8 == IDENT or LA8 == COLON or LA8 == HASH or LA8 == DOT or LA8 == LBRACKET or LA8 == STAR:
                    alt8 = 1
                elif LA8 == PAGE_SYM:
                    alt8 = 2
                elif LA8 == FONTFACE_SYM:
                    alt8 = 3
                elif LA8 == KEYFRAMES_SYM:
                    alt8 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # lesscss.g:123:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_media_bodyset488)
                    ruleSet24 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet24.tree)


                elif alt8 == 2:
                    # lesscss.g:124:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_media_bodyset496)
                    page25 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page25.tree)


                elif alt8 == 3:
                    # lesscss.g:125:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_media_bodyset504)
                    fontface26 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface26.tree)


                elif alt8 == 4:
                    # lesscss.g:126:7: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_media_bodyset512)
                    keyframes27 = self.keyframes()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, keyframes27.tree)


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

    # $ANTLR end "media_bodyset"

    class media_query_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query_list"
    # lesscss.g:133:1: media_query_list : media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) ;
    def media_query_list(self, ):

        retval = self.media_query_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA29 = None
        media_query28 = None

        media_query30 = None


        COMMA29_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_media_query = RewriteRuleSubtreeStream(self._adaptor, "rule media_query")
        try:
            try:
                # lesscss.g:134:5: ( media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) )
                # lesscss.g:134:7: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list536)
                media_query28 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query28.tree)
                # lesscss.g:134:19: ( COMMA media_query )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == COMMA) :
                        alt9 = 1


                    if alt9 == 1:
                        # lesscss.g:134:20: COMMA media_query
                        pass 
                        COMMA29=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list539) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA29)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list541)
                        media_query30 = self.media_query()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_media_query.add(media_query30.tree)


                    else:
                        break #loop9

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
                    # 135:9: -> ^( N_MediaQuery ( media_query )+ )
                    # lesscss.g:135:12: ^( N_MediaQuery ( media_query )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaQuery, "N_MediaQuery"), root_1)

                    # lesscss.g:135:27: ( media_query )+
                    if not (stream_media_query.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_media_query.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query.nextTree())


                    stream_media_query.reset()

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

    # $ANTLR end "media_query_list"

    class media_query_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query"
    # lesscss.g:140:1: media_query : ( media_stmt | media_expr )+ ;
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        media_stmt31 = None

        media_expr32 = None



        try:
            try:
                # lesscss.g:141:5: ( ( media_stmt | media_expr )+ )
                # lesscss.g:141:7: ( media_stmt | media_expr )+
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:141:7: ( media_stmt | media_expr )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 3
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == IDENT) :
                        alt10 = 1
                    elif (LA10_0 == LPAREN) :
                        alt10 = 2


                    if alt10 == 1:
                        # lesscss.g:141:9: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query581)
                        media_stmt31 = self.media_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_stmt31.tree)


                    elif alt10 == 2:
                        # lesscss.g:141:22: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query585)
                        media_expr32 = self.media_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_expr32.tree)


                    else:
                        if cnt10 >= 1:
                            break #loop10

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1



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
    # lesscss.g:144:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT33 = None

        IDENT33_tree = None

        try:
            try:
                # lesscss.g:145:5: ( IDENT )
                # lesscss.g:145:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT33=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt605)
                if self._state.backtracking == 0:

                    IDENT33_tree = self._adaptor.createWithPayload(IDENT33)
                    self._adaptor.addChild(root_0, IDENT33_tree)




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
    # lesscss.g:148:1: media_expr : LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN34 = None
        COLON36 = None
        RPAREN38 = None
        media_stmt35 = None

        expr37 = None


        LPAREN34_tree = None
        COLON36_tree = None
        RPAREN38_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_media_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule media_stmt")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:149:5: ( LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) )
                # lesscss.g:149:7: LPAREN media_stmt ( COLON expr )? RPAREN
                pass 
                LPAREN34=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr622) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN34)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr624)
                media_stmt35 = self.media_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_stmt.add(media_stmt35.tree)
                # lesscss.g:149:25: ( COLON expr )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    alt11 = 1
                if alt11 == 1:
                    # lesscss.g:149:27: COLON expr
                    pass 
                    COLON36=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr628) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON36)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr630)
                    expr37 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr37.tree)



                RPAREN38=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr635) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN38)

                # AST Rewrite
                # elements: media_stmt, expr
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
                    # 150:9: -> ^( N_MediaExpr media_stmt ( expr )? )
                    # lesscss.g:150:12: ^( N_MediaExpr media_stmt ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_stmt.nextTree())
                    # lesscss.g:150:37: ( expr )?
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
    # lesscss.g:157:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM39 = None
        LBRACE40 = None
        RBRACE42 = None
        declarationset41 = None


        FONTFACE_SYM39_tree = None
        LBRACE40_tree = None
        RBRACE42_tree = None

        try:
            try:
                # lesscss.g:158:5: ( FONTFACE_SYM LBRACE declarationset RBRACE )
                # lesscss.g:158:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                FONTFACE_SYM39=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface676)
                if self._state.backtracking == 0:

                    FONTFACE_SYM39_tree = self._adaptor.createWithPayload(FONTFACE_SYM39)
                    root_0 = self._adaptor.becomeRoot(FONTFACE_SYM39_tree, root_0)

                LBRACE40=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface679)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface682)
                declarationset41 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset41.tree)
                RBRACE42=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface684)



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
    # lesscss.g:164:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM43 = None
        LBRACE45 = None
        RBRACE47 = None
        pseudoPage44 = None

        declarationset46 = None


        PAGE_SYM43_tree = None
        LBRACE45_tree = None
        RBRACE47_tree = None

        try:
            try:
                # lesscss.g:165:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE )
                # lesscss.g:165:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                PAGE_SYM43=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page705)
                if self._state.backtracking == 0:

                    PAGE_SYM43_tree = self._adaptor.createWithPayload(PAGE_SYM43)
                    root_0 = self._adaptor.becomeRoot(PAGE_SYM43_tree, root_0)

                # lesscss.g:165:17: ( pseudoPage )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == COLON) :
                    alt12 = 1
                if alt12 == 1:
                    # lesscss.g:165:17: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page708)
                    pseudoPage44 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudoPage44.tree)



                LBRACE45=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page711)
                self._state.following.append(self.FOLLOW_declarationset_in_page714)
                declarationset46 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset46.tree)
                RBRACE47=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page716)



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
    # lesscss.g:168:1: pseudoPage : COLON a= IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON48 = None

        a_tree = None
        COLON48_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:169:5: ( COLON a= IDENT -> IDENT )
                # lesscss.g:169:7: COLON a= IDENT
                pass 
                COLON48=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage734) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON48)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage738) 
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
                    # 171:9: -> IDENT
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
    # lesscss.g:178:1: keyframes : KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE ;
    def keyframes(self, ):

        retval = self.keyframes_return()
        retval.start = self.input.LT(1)

        root_0 = None

        KEYFRAMES_SYM49 = None
        IDENT50 = None
        LBRACE51 = None
        RBRACE53 = None
        keyframes_block52 = None


        KEYFRAMES_SYM49_tree = None
        IDENT50_tree = None
        LBRACE51_tree = None
        RBRACE53_tree = None

        try:
            try:
                # lesscss.g:179:5: ( KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE )
                # lesscss.g:179:7: KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                KEYFRAMES_SYM49=self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes782)
                if self._state.backtracking == 0:

                    KEYFRAMES_SYM49_tree = self._adaptor.createWithPayload(KEYFRAMES_SYM49)
                    root_0 = self._adaptor.becomeRoot(KEYFRAMES_SYM49_tree, root_0)

                IDENT50=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes785)
                if self._state.backtracking == 0:

                    IDENT50_tree = self._adaptor.createWithPayload(IDENT50)
                    self._adaptor.addChild(root_0, IDENT50_tree)

                LBRACE51=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes787)
                # lesscss.g:179:36: ( keyframes_block )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == IDENT or LA13_0 == PERCENTAGE) :
                        alt13 = 1


                    if alt13 == 1:
                        # lesscss.g:179:36: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes790)
                        keyframes_block52 = self.keyframes_block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, keyframes_block52.tree)


                    else:
                        break #loop13
                RBRACE53=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes793)



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
    # lesscss.g:182:1: keyframes_block : keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) ;
    def keyframes_block(self, ):

        retval = self.keyframes_block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA55 = None
        LBRACE57 = None
        RBRACE59 = None
        keyframe_selector54 = None

        keyframe_selector56 = None

        declarationset58 = None


        COMMA55_tree = None
        LBRACE57_tree = None
        RBRACE59_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_keyframe_selector = RewriteRuleSubtreeStream(self._adaptor, "rule keyframe_selector")
        try:
            try:
                # lesscss.g:183:5: ( keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) )
                # lesscss.g:183:7: keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block811)
                keyframe_selector54 = self.keyframe_selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_keyframe_selector.add(keyframe_selector54.tree)
                # lesscss.g:183:25: ( COMMA keyframe_selector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1


                    if alt14 == 1:
                        # lesscss.g:183:27: COMMA keyframe_selector
                        pass 
                        COMMA55=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keyframes_block815) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA55)
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block817)
                        keyframe_selector56 = self.keyframe_selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_keyframe_selector.add(keyframe_selector56.tree)


                    else:
                        break #loop14
                LBRACE57=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes_block822) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE57)
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block824)
                declarationset58 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset58.tree)
                RBRACE59=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes_block826) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE59)

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
                    # 184:9: -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    # lesscss.g:184:12: ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_KeyframeBlock, "N_KeyframeBlock"), root_1)

                    # lesscss.g:184:30: ( ^( M_KeyframeSelector keyframe_selector ) )+
                    if not (stream_keyframe_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_keyframe_selector.hasNext():
                        # lesscss.g:184:30: ^( M_KeyframeSelector keyframe_selector )
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
    # lesscss.g:188:1: keyframe_selector : ( IDENT | PERCENTAGE ) ;
    def keyframe_selector(self, ):

        retval = self.keyframe_selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set60 = None

        set60_tree = None

        try:
            try:
                # lesscss.g:189:5: ( ( IDENT | PERCENTAGE ) )
                # lesscss.g:189:7: ( IDENT | PERCENTAGE )
                pass 
                root_0 = self._adaptor.nil()

                set60 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == PERCENTAGE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set60))
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
    # lesscss.g:196:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
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
                # lesscss.g:197:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:197:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet897)
                selector61 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector61.tree)
                # lesscss.g:197:16: ( COMMA selector )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == COMMA) :
                        alt15 = 1


                    if alt15 == 1:
                        # lesscss.g:197:17: COMMA selector
                        pass 
                        COMMA62=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet900) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA62)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet902)
                        selector63 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector63.tree)


                    else:
                        break #loop15
                LBRACE64=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet906) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE64)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet908)
                declarationset65 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset65.tree)
                RBRACE66=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet910) 
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
                    # 198:9: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:198:12: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:198:24: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:198:24: ^( N_Selector selector )
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
    # lesscss.g:201:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector67 = None

        combinator68 = None

        simpleSelector69 = None



        try:
            try:
                # lesscss.g:202:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:202:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector950)
                simpleSelector67 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector67.tree)
                # lesscss.g:202:22: ( combinator simpleSelector )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == IDENT or LA16_0 == COLON or (PLUS <= LA16_0 <= STAR)) :
                        alt16 = 1


                    if alt16 == 1:
                        # lesscss.g:202:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector953)
                        combinator68 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator68.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector955)
                        simpleSelector69 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector69.tree)


                    else:
                        break #loop16



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
    # lesscss.g:205:1: combinator : ( PLUS | GREATER | );
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
                # lesscss.g:206:5: ( PLUS | GREATER | )
                alt17 = 3
                LA17 = self.input.LA(1)
                if LA17 == PLUS:
                    alt17 = 1
                elif LA17 == GREATER:
                    alt17 = 2
                elif LA17 == IDENT or LA17 == COLON or LA17 == HASH or LA17 == DOT or LA17 == LBRACKET or LA17 == STAR:
                    alt17 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # lesscss.g:206:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS70=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator974)
                    if self._state.backtracking == 0:

                        PLUS70_tree = self._adaptor.createWithPayload(PLUS70)
                        self._adaptor.addChild(root_0, PLUS70_tree)



                elif alt17 == 2:
                    # lesscss.g:207:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER71=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator982)
                    if self._state.backtracking == 0:

                        GREATER71_tree = self._adaptor.createWithPayload(GREATER71)
                        self._adaptor.addChild(root_0, GREATER71_tree)



                elif alt17 == 3:
                    # lesscss.g:209:5: 
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
    # lesscss.g:211:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName72 = None

        elementSubsequent73 = None

        elementSubsequent74 = None



        try:
            try:
                # lesscss.g:212:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == IDENT or LA20_0 == STAR) :
                    alt20 = 1
                elif (LA20_0 == COLON or (HASH <= LA20_0 <= LBRACKET)) :
                    alt20 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # lesscss.g:212:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector1005)
                    elementName72 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName72.tree)
                    # lesscss.g:212:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop18
                        alt18 = 2
                        alt18 = self.dfa18.predict(self.input)
                        if alt18 == 1:
                            # lesscss.g:212:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1012)
                            elementSubsequent73 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent73.tree)


                        else:
                            break #loop18


                elif alt20 == 2:
                    # lesscss.g:213:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:213:7: ( ( esPred )=> elementSubsequent )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19 = self.input.LA(1)
                        if LA19 == HASH:
                            LA19_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt19 = 1


                        elif LA19 == DOT:
                            LA19_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt19 = 1


                        elif LA19 == LBRACKET:
                            LA19_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt19 = 1


                        elif LA19 == COLON:
                            LA19_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt19 = 1



                        if alt19 == 1:
                            # lesscss.g:213:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1027)
                            elementSubsequent74 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent74.tree)


                        else:
                            if cnt19 >= 1:
                                break #loop19

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


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
    # lesscss.g:216:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set75 = None

        set75_tree = None

        try:
            try:
                # lesscss.g:217:5: ( HASH | DOT | LBRACKET | COLON )
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
    # lesscss.g:220:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set76 = None

        set76_tree = None

        try:
            try:
                # lesscss.g:221:5: ( IDENT | STAR )
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
    # lesscss.g:225:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH77 = None
        cssClass78 = None

        attrib79 = None

        pseudo80 = None


        HASH77_tree = None

        try:
            try:
                # lesscss.g:226:5: ( HASH | cssClass | attrib | pseudo )
                alt21 = 4
                LA21 = self.input.LA(1)
                if LA21 == HASH:
                    alt21 = 1
                elif LA21 == DOT:
                    alt21 = 2
                elif LA21 == LBRACKET:
                    alt21 = 3
                elif LA21 == COLON:
                    alt21 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # lesscss.g:226:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH77=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent1100)
                    if self._state.backtracking == 0:

                        HASH77_tree = self._adaptor.createWithPayload(HASH77)
                        self._adaptor.addChild(root_0, HASH77_tree)



                elif alt21 == 2:
                    # lesscss.g:227:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent1108)
                    cssClass78 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass78.tree)


                elif alt21 == 3:
                    # lesscss.g:228:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent1116)
                    attrib79 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib79.tree)


                elif alt21 == 4:
                    # lesscss.g:229:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent1124)
                    pseudo80 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo80.tree)


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
    # lesscss.g:232:1: cssClass : DOT a= IDENT -> IDENT ;
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
                # lesscss.g:233:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:233:7: DOT a= IDENT
                pass 
                DOT81=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass1141) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT81)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass1145) 
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
                    # 235:9: -> IDENT
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
    # lesscss.g:238:1: pseudo : a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) ;
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
                # lesscss.g:239:5: (a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) )
                # lesscss.g:239:7: a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
                pass 
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1187) 
                if self._state.backtracking == 0:
                    stream_COLON.add(a)
                # lesscss.g:239:16: (b= COLON )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == COLON) :
                    alt22 = 1
                if alt22 == 1:
                    # lesscss.g:239:16: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1191) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(b)



                # lesscss.g:240:5: ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == IDENT) :
                    alt23 = 1
                elif (LA23_0 == FUNCTION) :
                    alt23 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # lesscss.g:240:7: IDENT
                    pass 
                    IDENT82=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1200) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT82)

                    # AST Rewrite
                    # elements: IDENT, b, a
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
                        # 241:9: -> ^( N_Pseudo $a ( $b)? IDENT )
                        # lesscss.g:241:12: ^( N_Pseudo $a ( $b)? IDENT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:241:26: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 2:
                    # lesscss.g:242:7: pseudoFunction
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoFunction_in_pseudo1231)
                    pseudoFunction83 = self.pseudoFunction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoFunction.add(pseudoFunction83.tree)

                    # AST Rewrite
                    # elements: b, pseudoFunction, a
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
                        # 243:9: -> ^( N_Pseudo $a ( $b)? pseudoFunction )
                        # lesscss.g:243:12: ^( N_Pseudo $a ( $b)? pseudoFunction )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:243:26: ( $b)?
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
    # lesscss.g:247:1: pseudoFunction : ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) );
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
                # lesscss.g:248:5: ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) )
                alt24 = 3
                LA24_0 = self.input.LA(1)

                if (LA24_0 == FUNCTION) :
                    LA24 = self.input.LA(2)
                    if LA24 == LBRACKET:
                        alt24 = 2
                    elif LA24 == COLON:
                        alt24 = 3
                    elif LA24 == STRING or LA24 == URI or LA24 == IDENT or LA24 == PERCENTAGE or LA24 == PLUS or LA24 == HASH or LA24 == FUNCTION or LA24 == NUMBER or LA24 == LENGTH or LA24 == EMS or LA24 == EXS or LA24 == REMS or LA24 == CHS or LA24 == ANGLE or LA24 == TIME or LA24 == FREQ or LA24 == RESOLUTION or LA24 == VPORTLEN or LA24 == NTH or LA24 == UNICODE_RANGE or LA24 == MINUS:
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
                    # lesscss.g:248:7: FUNCTION expr RPAREN
                    pass 
                    FUNCTION84=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction1277) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION84)
                    self._state.following.append(self.FOLLOW_expr_in_pseudoFunction1279)
                    expr85 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr85.tree)
                    RPAREN86=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction1281) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN86)

                    # AST Rewrite
                    # elements: expr, FUNCTION
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
                        # 249:9: -> ^( N_PseudoFunction FUNCTION expr )
                        # lesscss.g:249:12: ^( N_PseudoFunction FUNCTION expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt24 == 2:
                    # lesscss.g:251:7: FUNCTION LBRACKET attribBody RBRACKET RPAREN
                    pass 
                    FUNCTION87=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction1309) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION87)
                    LBRACKET88=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudoFunction1311) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET88)
                    self._state.following.append(self.FOLLOW_attribBody_in_pseudoFunction1313)
                    attribBody89 = self.attribBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_attribBody.add(attribBody89.tree)
                    RBRACKET90=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudoFunction1315) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET90)
                    RPAREN91=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction1317) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN91)

                    # AST Rewrite
                    # elements: FUNCTION, attribBody, LBRACKET, RBRACKET
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
                        # 252:9: -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        # lesscss.g:252:12: ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_LBRACKET.nextNode())
                        self._adaptor.addChild(root_1, stream_attribBody.nextTree())
                        self._adaptor.addChild(root_1, stream_RBRACKET.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt24 == 3:
                    # lesscss.g:254:7: FUNCTION pseudo RPAREN
                    pass 
                    FUNCTION92=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction1349) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION92)
                    self._state.following.append(self.FOLLOW_pseudo_in_pseudoFunction1351)
                    pseudo93 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudo.add(pseudo93.tree)
                    RPAREN94=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction1353) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN94)

                    # AST Rewrite
                    # elements: pseudo, FUNCTION
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
                        # 255:9: -> ^( N_PseudoFunction FUNCTION pseudo )
                        # lesscss.g:255:12: ^( N_PseudoFunction FUNCTION pseudo )
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
    # lesscss.g:260:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
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
                # lesscss.g:261:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:261:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET95=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1391) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET95)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1393)
                attribBody96 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody96.tree)
                RBRACKET97=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1395) 
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
                    # 262:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:262:13: ^( N_Attrib attribBody )
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
    # lesscss.g:265:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term );
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
                # lesscss.g:266:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == IDENT) :
                    LA25_1 = self.input.LA(2)

                    if ((OPEQ <= LA25_1 <= SUBSTRINGMATCH)) :
                        alt25 = 2
                    elif (LA25_1 == RBRACKET) :
                        alt25 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # lesscss.g:266:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT98=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1430)
                    if self._state.backtracking == 0:

                        IDENT98_tree = self._adaptor.createWithPayload(IDENT98)
                        self._adaptor.addChild(root_0, IDENT98_tree)



                elif alt25 == 2:
                    # lesscss.g:267:7: IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT99=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1438)
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


                    self._state.following.append(self.FOLLOW_term_in_attribBody1535)
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
    # lesscss.g:278:1: declarationset : ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ | -> N_Empty );
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
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:279:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ | -> N_Empty )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == IDENT or LA28_0 == STAR) :
                    alt28 = 1
                elif (LA28_0 == RBRACE) :
                    alt28 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # lesscss.g:279:7: declaration ( SEMI declaration )* ( SEMI )?
                    pass 
                    self._state.following.append(self.FOLLOW_declaration_in_declarationset1552)
                    declaration102 = self.declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_declaration.add(declaration102.tree)
                    # lesscss.g:279:19: ( SEMI declaration )*
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == SEMI) :
                            LA26_1 = self.input.LA(2)

                            if (LA26_1 == IDENT or LA26_1 == STAR) :
                                alt26 = 1




                        if alt26 == 1:
                            # lesscss.g:279:20: SEMI declaration
                            pass 
                            SEMI103=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1555) 
                            if self._state.backtracking == 0:
                                stream_SEMI.add(SEMI103)
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset1557)
                            declaration104 = self.declaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_declaration.add(declaration104.tree)


                        else:
                            break #loop26
                    # lesscss.g:279:39: ( SEMI )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == SEMI) :
                        alt27 = 1
                    if alt27 == 1:
                        # lesscss.g:279:39: SEMI
                        pass 
                        SEMI105=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1561) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI105)




                    # AST Rewrite
                    # elements: declaration
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
                        # 280:10: -> ( declaration )+
                        # lesscss.g:280:13: ( declaration )+
                        if not (stream_declaration.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_declaration.hasNext():
                            self._adaptor.addChild(root_0, stream_declaration.nextTree())


                        stream_declaration.reset()



                        retval.tree = root_0


                elif alt28 == 2:
                    # lesscss.g:281:7: 
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
                        # 281:7: -> N_Empty
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
    # lesscss.g:284:1: declaration : ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) );
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
                # lesscss.g:285:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == IDENT) :
                    LA30_1 = self.input.LA(2)

                    if (LA30_1 == COLON) :
                        LA30_3 = self.input.LA(3)

                        if (LA30_3 == STRING or LA30_3 == URI or LA30_3 == IDENT or (PERCENTAGE <= LA30_3 <= PLUS) or LA30_3 == HASH or LA30_3 == FUNCTION or (NUMBER <= LA30_3 <= MINUS)) :
                            alt30 = 1
                        elif (LA30_3 == SEMI or LA30_3 == RBRACE) :
                            alt30 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 30, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 30, 1, self.input)

                        raise nvae

                elif (LA30_0 == STAR) :
                    LA30_2 = self.input.LA(2)

                    if (LA30_2 == IDENT) :
                        LA30_4 = self.input.LA(3)

                        if (LA30_4 == COLON) :
                            LA30_3 = self.input.LA(4)

                            if (LA30_3 == STRING or LA30_3 == URI or LA30_3 == IDENT or (PERCENTAGE <= LA30_3 <= PLUS) or LA30_3 == HASH or LA30_3 == FUNCTION or (NUMBER <= LA30_3 <= MINUS)) :
                                alt30 = 1
                            elif (LA30_3 == SEMI or LA30_3 == RBRACE) :
                                alt30 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 30, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 30, 4, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 30, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # lesscss.g:285:7: property COLON expr ( prio )?
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1603)
                    property106 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property106.tree)
                    COLON107=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1605) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON107)
                    self._state.following.append(self.FOLLOW_expr_in_declaration1607)
                    expr108 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr108.tree)
                    # lesscss.g:285:27: ( prio )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == IMPORTANT_SYM) :
                        alt29 = 1
                    if alt29 == 1:
                        # lesscss.g:285:27: prio
                        pass 
                        self._state.following.append(self.FOLLOW_prio_in_declaration1609)
                        prio109 = self.prio()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_prio.add(prio109.tree)




                    # AST Rewrite
                    # elements: prio, expr, property
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
                        # 286:9: -> ^( N_Declaration property expr ( prio )? )
                        # lesscss.g:286:12: ^( N_Declaration property expr ( prio )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                        self._adaptor.addChild(root_1, stream_property.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())
                        # lesscss.g:286:42: ( prio )?
                        if stream_prio.hasNext():
                            self._adaptor.addChild(root_1, stream_prio.nextTree())


                        stream_prio.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt30 == 2:
                    # lesscss.g:287:8: property COLON
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1640)
                    property110 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property110.tree)
                    COLON111=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1642) 
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
                        # 288:9: -> ^( N_Declaration property )
                        # lesscss.g:288:12: ^( N_Declaration property )
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
    # lesscss.g:291:1: property : ( IDENT | STAR a= IDENT -> IDENT );
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
                # lesscss.g:292:5: ( IDENT | STAR a= IDENT -> IDENT )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == IDENT) :
                    alt31 = 1
                elif (LA31_0 == STAR) :
                    alt31 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # lesscss.g:292:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT112=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1678)
                    if self._state.backtracking == 0:

                        IDENT112_tree = self._adaptor.createWithPayload(IDENT112)
                        self._adaptor.addChild(root_0, IDENT112_tree)



                elif alt31 == 2:
                    # lesscss.g:296:7: STAR a= IDENT
                    pass 
                    STAR113=self.match(self.input, STAR, self.FOLLOW_STAR_in_property1697) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR113)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1701) 
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
                        # 298:9: -> IDENT
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
    # lesscss.g:301:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM114 = None

        IMPORTANT_SYM114_tree = None

        try:
            try:
                # lesscss.g:302:5: ( IMPORTANT_SYM )
                # lesscss.g:302:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM114=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1741)
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
    # lesscss.g:305:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term115 = None

        operator116 = None

        term117 = None



        try:
            try:
                # lesscss.g:306:5: ( term ( operator term )* )
                # lesscss.g:306:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1758)
                term115 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term115.tree)
                # lesscss.g:306:12: ( operator term )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == COMMA) :
                        LA32_2 = self.input.LA(2)

                        if (LA32_2 == STRING or LA32_2 == URI or (PERCENTAGE <= LA32_2 <= PLUS) or LA32_2 == HASH or LA32_2 == FUNCTION or (NUMBER <= LA32_2 <= MINUS)) :
                            alt32 = 1
                        elif (LA32_2 == IDENT) :
                            LA32_4 = self.input.LA(3)

                            if ((STRING <= LA32_4 <= SEMI) or LA32_4 == URI or (RBRACE <= LA32_4 <= IDENT) or (COLON <= LA32_4 <= RPAREN) or (PERCENTAGE <= LA32_4 <= PLUS) or (HASH <= LA32_4 <= DOT) or LA32_4 == FUNCTION or (IMPORTANT_SYM <= LA32_4 <= MINUS)) :
                                alt32 = 1




                    elif (LA32_0 == STRING or LA32_0 == URI or LA32_0 == IDENT or (PERCENTAGE <= LA32_0 <= PLUS) or LA32_0 == HASH or LA32_0 == FUNCTION or (SOLIDUS <= LA32_0 <= MINUS)) :
                        alt32 = 1


                    if alt32 == 1:
                        # lesscss.g:306:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1761)
                        operator116 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator116.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1764)
                        term117 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term117.tree)


                    else:
                        break #loop32



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
    # lesscss.g:309:10: fragment operator : ( SOLIDUS | COMMA | -> N_Empty );
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
                # lesscss.g:310:5: ( SOLIDUS | COMMA | -> N_Empty )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 == SOLIDUS:
                    alt33 = 1
                elif LA33 == COMMA:
                    alt33 = 2
                elif LA33 == STRING or LA33 == URI or LA33 == IDENT or LA33 == PERCENTAGE or LA33 == PLUS or LA33 == HASH or LA33 == FUNCTION or LA33 == NUMBER or LA33 == LENGTH or LA33 == EMS or LA33 == EXS or LA33 == REMS or LA33 == CHS or LA33 == ANGLE or LA33 == TIME or LA33 == FREQ or LA33 == RESOLUTION or LA33 == VPORTLEN or LA33 == NTH or LA33 == UNICODE_RANGE or LA33 == MINUS:
                    alt33 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # lesscss.g:310:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS118=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1785)
                    if self._state.backtracking == 0:

                        SOLIDUS118_tree = self._adaptor.createWithPayload(SOLIDUS118)
                        self._adaptor.addChild(root_0, SOLIDUS118_tree)



                elif alt33 == 2:
                    # lesscss.g:311:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA119=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1793)
                    if self._state.backtracking == 0:

                        COMMA119_tree = self._adaptor.createWithPayload(COMMA119)
                        self._adaptor.addChild(root_0, COMMA119_tree)



                elif alt33 == 3:
                    # lesscss.g:312:7: 
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
                        # 312:7: -> N_Empty
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

    # $ANTLR end "operator"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # lesscss.g:315:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH ) | STRING | IDENT | URI | function | hexColor | UNICODE_RANGE );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set121 = None
        STRING122 = None
        IDENT123 = None
        URI124 = None
        UNICODE_RANGE127 = None
        unaryOperator120 = None

        function125 = None

        hexColor126 = None


        set121_tree = None
        STRING122_tree = None
        IDENT123_tree = None
        URI124_tree = None
        UNICODE_RANGE127_tree = None

        try:
            try:
                # lesscss.g:316:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH ) | STRING | IDENT | URI | function | hexColor | UNICODE_RANGE )
                alt35 = 7
                LA35 = self.input.LA(1)
                if LA35 == PERCENTAGE or LA35 == PLUS or LA35 == NUMBER or LA35 == LENGTH or LA35 == EMS or LA35 == EXS or LA35 == REMS or LA35 == CHS or LA35 == ANGLE or LA35 == TIME or LA35 == FREQ or LA35 == RESOLUTION or LA35 == VPORTLEN or LA35 == NTH or LA35 == MINUS:
                    alt35 = 1
                elif LA35 == STRING:
                    alt35 = 2
                elif LA35 == IDENT:
                    LA35_3 = self.input.LA(2)

                    if (LA35_3 == COLON or LA35_3 == DOT) :
                        alt35 = 5
                    elif ((STRING <= LA35_3 <= SEMI) or LA35_3 == URI or (RBRACE <= LA35_3 <= IDENT) or LA35_3 == RPAREN or (PERCENTAGE <= LA35_3 <= PLUS) or LA35_3 == HASH or (FUNCTION <= LA35_3 <= RBRACKET) or (IMPORTANT_SYM <= LA35_3 <= MINUS)) :
                        alt35 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 35, 3, self.input)

                        raise nvae

                elif LA35 == URI:
                    alt35 = 4
                elif LA35 == FUNCTION:
                    alt35 = 5
                elif LA35 == HASH:
                    alt35 = 6
                elif LA35 == UNICODE_RANGE:
                    alt35 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # lesscss.g:316:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:316:20: ( unaryOperator )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == PLUS or LA34_0 == MINUS) :
                        alt34 = 1
                    if alt34 == 1:
                        # lesscss.g:316:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1821)
                        unaryOperator120 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator120.tree, root_0)



                    set121 = self.input.LT(1)
                    if self.input.LA(1) == PERCENTAGE or (NUMBER <= self.input.LA(1) <= NTH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set121))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt35 == 2:
                    # lesscss.g:332:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING122=self.match(self.input, STRING, self.FOLLOW_STRING_in_term2059)
                    if self._state.backtracking == 0:

                        STRING122_tree = self._adaptor.createWithPayload(STRING122)
                        self._adaptor.addChild(root_0, STRING122_tree)



                elif alt35 == 3:
                    # lesscss.g:333:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT123=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term2067)
                    if self._state.backtracking == 0:

                        IDENT123_tree = self._adaptor.createWithPayload(IDENT123)
                        self._adaptor.addChild(root_0, IDENT123_tree)



                elif alt35 == 4:
                    # lesscss.g:334:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI124=self.match(self.input, URI, self.FOLLOW_URI_in_term2075)
                    if self._state.backtracking == 0:

                        URI124_tree = self._adaptor.createWithPayload(URI124)
                        self._adaptor.addChild(root_0, URI124_tree)



                elif alt35 == 5:
                    # lesscss.g:335:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term2083)
                    function125 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function125.tree)


                elif alt35 == 6:
                    # lesscss.g:336:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term2091)
                    hexColor126 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor126.tree)


                elif alt35 == 7:
                    # lesscss.g:337:7: UNICODE_RANGE
                    pass 
                    root_0 = self._adaptor.nil()

                    UNICODE_RANGE127=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term2099)
                    if self._state.backtracking == 0:

                        UNICODE_RANGE127_tree = self._adaptor.createWithPayload(UNICODE_RANGE127)
                        self._adaptor.addChild(root_0, UNICODE_RANGE127_tree)



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
    # lesscss.g:340:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set128 = None

        set128_tree = None

        try:
            try:
                # lesscss.g:341:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set128 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set128))
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
    # lesscss.g:346:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN131 = None
        RPAREN134 = None
        fnct_name129 = None

        fnct_args130 = None

        fnct_name132 = None

        expr133 = None


        RPAREN131_tree = None
        RPAREN134_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:347:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt36 = 2
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # lesscss.g:347:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function2144)
                    fnct_name129 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name129.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function2146)
                    fnct_args130 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args130.tree)
                    RPAREN131=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function2148) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN131)

                    # AST Rewrite
                    # elements: fnct_name, fnct_args
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
                        # 348:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:348:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 2:
                    # lesscss.g:350:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function2175)
                    fnct_name132 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name132.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function2177)
                    expr133 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr133.tree)
                    RPAREN134=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function2179) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN134)

                    # AST Rewrite
                    # elements: fnct_name, expr
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
                        # 351:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:351:12: ^( N_Function fnct_name expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

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
    # lesscss.g:355:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT135 = None
        set136 = None
        FUNCTION137 = None

        IDENT135_tree = None
        set136_tree = None
        FUNCTION137_tree = None

        try:
            try:
                # lesscss.g:356:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:356:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:356:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == IDENT) :
                        alt38 = 1


                    if alt38 == 1:
                        # lesscss.g:356:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT135=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name2216)
                        if self._state.backtracking == 0:

                            IDENT135_tree = self._adaptor.createWithPayload(IDENT135)
                            self._adaptor.addChild(root_0, IDENT135_tree)

                        # lesscss.g:356:14: ( COLON | DOT )+
                        cnt37 = 0
                        while True: #loop37
                            alt37 = 2
                            LA37_0 = self.input.LA(1)

                            if (LA37_0 == COLON or LA37_0 == DOT) :
                                alt37 = 1


                            if alt37 == 1:
                                # lesscss.g:
                                pass 
                                set136 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set136))
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
                FUNCTION137=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name2228)
                if self._state.backtracking == 0:

                    FUNCTION137_tree = self._adaptor.createWithPayload(FUNCTION137)
                    root_0 = self._adaptor.becomeRoot(FUNCTION137_tree, root_0)




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
    # lesscss.g:359:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA139 = None
        fnct_arg138 = None

        fnct_arg140 = None


        COMMA139_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:360:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:360:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args2248)
                fnct_arg138 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg138.tree)
                # lesscss.g:360:16: ( COMMA fnct_arg )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == COMMA) :
                        alt39 = 1


                    if alt39 == 1:
                        # lesscss.g:360:17: COMMA fnct_arg
                        pass 
                        COMMA139=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args2251) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA139)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args2253)
                        fnct_arg140 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg140.tree)


                    else:
                        break #loop39

                # AST Rewrite
                # elements: fnct_arg
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
                    # 361:9: -> ( fnct_arg )+
                    # lesscss.g:361:12: ( fnct_arg )+
                    if not (stream_fnct_arg.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_fnct_arg.hasNext():
                        self._adaptor.addChild(root_0, stream_fnct_arg.nextTree())


                    stream_fnct_arg.reset()



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

    # $ANTLR end "fnct_args"

    class fnct_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_arg"
    # lesscss.g:364:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT141 = None
        OPEQ142 = None
        expr143 = None


        IDENT141_tree = None
        OPEQ142_tree = None

        try:
            try:
                # lesscss.g:365:5: ( IDENT OPEQ expr )
                # lesscss.g:365:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT141=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg2285)
                if self._state.backtracking == 0:

                    IDENT141_tree = self._adaptor.createWithPayload(IDENT141)
                    self._adaptor.addChild(root_0, IDENT141_tree)

                OPEQ142=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg2287)
                if self._state.backtracking == 0:

                    OPEQ142_tree = self._adaptor.createWithPayload(OPEQ142)
                    root_0 = self._adaptor.becomeRoot(OPEQ142_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg2290)
                expr143 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr143.tree)



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
    # lesscss.g:368:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH144 = None

        HASH144_tree = None

        try:
            try:
                # lesscss.g:369:5: ( HASH )
                # lesscss.g:369:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH144=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor2307)
                if self._state.backtracking == 0:

                    HASH144_tree = self._adaptor.createWithPayload(HASH144)
                    self._adaptor.addChild(root_0, HASH144_tree)




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
        # lesscss.g:212:20: ( esPred )
        # lesscss.g:212:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss1009)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:213:8: ( esPred )
        # lesscss.g:213:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss1024)
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



    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\27\3\uffff\4\0\3\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\1\47\3\uffff\4\0\3\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA18_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\1\1\uffff\2\1\1\uffff\1\7\5\uffff\2\1\1\4\1\5\1\6"
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

    # class definition for DFA #18

    class DFA18(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA18_4 = input.LA(1)

                 
                index18_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index18_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA18_5 = input.LA(1)

                 
                index18_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index18_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA18_6 = input.LA(1)

                 
                index18_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index18_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA18_7 = input.LA(1)

                 
                index18_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index18_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 18, _s, input)
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
        u"\1\32\1\34\1\22\1\32\1\uffff\1\22\1\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\1\50\1\45\1\77\1\50\1\uffff\1\77\1\uffff"
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


 

    FOLLOW_charSet_in_styleSheet186 = frozenset([20, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_imports_in_styleSheet197 = frozenset([20, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_bodylist_in_styleSheet208 = frozenset([])
    FOLLOW_EOF_in_styleSheet218 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet271 = frozenset([18])
    FOLLOW_STRING_in_charSet274 = frozenset([19])
    FOLLOW_SEMI_in_charSet276 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports300 = frozenset([18, 21])
    FOLLOW_importUrl_in_imports303 = frozenset([19, 26, 27])
    FOLLOW_media_query_list_in_imports305 = frozenset([19])
    FOLLOW_SEMI_in_imports308 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_bodyset_in_bodylist355 = frozenset([1, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_ruleSet_in_bodyset373 = frozenset([1])
    FOLLOW_media_in_bodyset381 = frozenset([1])
    FOLLOW_page_in_bodyset389 = frozenset([1])
    FOLLOW_fontface_in_bodyset397 = frozenset([1])
    FOLLOW_keyframes_in_bodyset405 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media430 = frozenset([23, 26, 27])
    FOLLOW_media_query_list_in_media433 = frozenset([23])
    FOLLOW_LBRACE_in_media444 = frozenset([22, 24, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_media_bodyset_in_media459 = frozenset([22, 24, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_RBRACE_in_media470 = frozenset([1])
    FOLLOW_ruleSet_in_media_bodyset488 = frozenset([1])
    FOLLOW_page_in_media_bodyset496 = frozenset([1])
    FOLLOW_fontface_in_media_bodyset504 = frozenset([1])
    FOLLOW_keyframes_in_media_bodyset512 = frozenset([1])
    FOLLOW_media_query_in_media_query_list536 = frozenset([1, 25])
    FOLLOW_COMMA_in_media_query_list539 = frozenset([26, 27])
    FOLLOW_media_query_in_media_query_list541 = frozenset([1, 25])
    FOLLOW_media_stmt_in_media_query581 = frozenset([1, 26, 27])
    FOLLOW_media_expr_in_media_query585 = frozenset([1, 26, 27])
    FOLLOW_IDENT_in_media_stmt605 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr622 = frozenset([26])
    FOLLOW_media_stmt_in_media_expr624 = frozenset([28, 29])
    FOLLOW_COLON_in_media_expr628 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_media_expr630 = frozenset([29])
    FOLLOW_RPAREN_in_media_expr635 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface676 = frozenset([23])
    FOLLOW_LBRACE_in_fontface679 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_fontface682 = frozenset([24])
    FOLLOW_RBRACE_in_fontface684 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page705 = frozenset([23, 28])
    FOLLOW_pseudoPage_in_page708 = frozenset([23])
    FOLLOW_LBRACE_in_page711 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_page714 = frozenset([24])
    FOLLOW_RBRACE_in_page716 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage734 = frozenset([26])
    FOLLOW_IDENT_in_pseudoPage738 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes782 = frozenset([26])
    FOLLOW_IDENT_in_keyframes785 = frozenset([23])
    FOLLOW_LBRACE_in_keyframes787 = frozenset([24, 26, 33])
    FOLLOW_keyframes_block_in_keyframes790 = frozenset([24, 26, 33])
    FOLLOW_RBRACE_in_keyframes793 = frozenset([1])
    FOLLOW_keyframe_selector_in_keyframes_block811 = frozenset([23, 25])
    FOLLOW_COMMA_in_keyframes_block815 = frozenset([26, 33])
    FOLLOW_keyframe_selector_in_keyframes_block817 = frozenset([23, 25])
    FOLLOW_LBRACE_in_keyframes_block822 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_keyframes_block824 = frozenset([24])
    FOLLOW_RBRACE_in_keyframes_block826 = frozenset([1])
    FOLLOW_set_in_keyframe_selector868 = frozenset([1])
    FOLLOW_selector_in_ruleSet897 = frozenset([23, 25])
    FOLLOW_COMMA_in_ruleSet900 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_selector_in_ruleSet902 = frozenset([23, 25])
    FOLLOW_LBRACE_in_ruleSet906 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_ruleSet908 = frozenset([24])
    FOLLOW_RBRACE_in_ruleSet910 = frozenset([1])
    FOLLOW_simpleSelector_in_selector950 = frozenset([1, 26, 28, 34, 35, 36, 37, 38, 39])
    FOLLOW_combinator_in_selector953 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_simpleSelector_in_selector955 = frozenset([1, 26, 28, 34, 35, 36, 37, 38, 39])
    FOLLOW_PLUS_in_combinator974 = frozenset([1])
    FOLLOW_GREATER_in_combinator982 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector1005 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector1012 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector1027 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent1100 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent1108 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent1116 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent1124 = frozenset([1])
    FOLLOW_DOT_in_cssClass1141 = frozenset([26])
    FOLLOW_IDENT_in_cssClass1145 = frozenset([1])
    FOLLOW_COLON_in_pseudo1187 = frozenset([26, 28, 40])
    FOLLOW_COLON_in_pseudo1191 = frozenset([26, 28, 40])
    FOLLOW_IDENT_in_pseudo1200 = frozenset([1])
    FOLLOW_pseudoFunction_in_pseudo1231 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction1277 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_pseudoFunction1279 = frozenset([29])
    FOLLOW_RPAREN_in_pseudoFunction1281 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction1309 = frozenset([38])
    FOLLOW_LBRACKET_in_pseudoFunction1311 = frozenset([26])
    FOLLOW_attribBody_in_pseudoFunction1313 = frozenset([41])
    FOLLOW_RBRACKET_in_pseudoFunction1315 = frozenset([29])
    FOLLOW_RPAREN_in_pseudoFunction1317 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction1349 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_pseudo_in_pseudoFunction1351 = frozenset([29])
    FOLLOW_RPAREN_in_pseudoFunction1353 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1391 = frozenset([26])
    FOLLOW_attribBody_in_attrib1393 = frozenset([41])
    FOLLOW_RBRACKET_in_attrib1395 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1430 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1438 = frozenset([42, 43, 44, 45, 46, 47])
    FOLLOW_set_in_attribBody1449 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_term_in_attribBody1535 = frozenset([1])
    FOLLOW_declaration_in_declarationset1552 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1555 = frozenset([26, 39])
    FOLLOW_declaration_in_declarationset1557 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1561 = frozenset([1])
    FOLLOW_property_in_declaration1603 = frozenset([28])
    FOLLOW_COLON_in_declaration1605 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_declaration1607 = frozenset([1, 48])
    FOLLOW_prio_in_declaration1609 = frozenset([1])
    FOLLOW_property_in_declaration1640 = frozenset([28])
    FOLLOW_COLON_in_declaration1642 = frozenset([1])
    FOLLOW_IDENT_in_property1678 = frozenset([1])
    FOLLOW_STAR_in_property1697 = frozenset([26])
    FOLLOW_IDENT_in_property1701 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1741 = frozenset([1])
    FOLLOW_term_in_expr1758 = frozenset([1, 18, 21, 25, 26, 33, 34, 36, 40, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_operator_in_expr1761 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_term_in_expr1764 = frozenset([1, 18, 21, 25, 26, 33, 34, 36, 40, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_SOLIDUS_in_operator1785 = frozenset([1])
    FOLLOW_COMMA_in_operator1793 = frozenset([1])
    FOLLOW_unaryOperator_in_term1821 = frozenset([33, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_set_in_term1833 = frozenset([1])
    FOLLOW_STRING_in_term2059 = frozenset([1])
    FOLLOW_IDENT_in_term2067 = frozenset([1])
    FOLLOW_URI_in_term2075 = frozenset([1])
    FOLLOW_function_in_term2083 = frozenset([1])
    FOLLOW_hexColor_in_term2091 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term2099 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function2144 = frozenset([26])
    FOLLOW_fnct_args_in_function2146 = frozenset([29])
    FOLLOW_RPAREN_in_function2148 = frozenset([1])
    FOLLOW_fnct_name_in_function2175 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_function2177 = frozenset([29])
    FOLLOW_RPAREN_in_function2179 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name2216 = frozenset([28, 37])
    FOLLOW_set_in_fnct_name2218 = frozenset([26, 28, 37, 40])
    FOLLOW_FUNCTION_in_fnct_name2228 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args2248 = frozenset([1, 25])
    FOLLOW_COMMA_in_fnct_args2251 = frozenset([26])
    FOLLOW_fnct_arg_in_fnct_args2253 = frozenset([1, 25])
    FOLLOW_IDENT_in_fnct_arg2285 = frozenset([42])
    FOLLOW_OPEQ_in_fnct_arg2287 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_fnct_arg2290 = frozenset([1])
    FOLLOW_HASH_in_hexColor2307 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss1009 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss1024 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
