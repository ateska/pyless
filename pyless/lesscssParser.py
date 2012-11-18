# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-18 02:01:41

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=40
STAR=39
EOF=-1
MEDIA_SYM=22
INCLUDES=43
LBRACKET=38
RPAREN=29
NAME=66
GREATER=35
ESCAPE=63
DIMENSION=99
STRINGESC=97
NL=100
COMMENT=94
D=71
E=72
F=73
G=74
A=68
RBRACE=24
B=69
C=70
L=79
IMPORT_SYM=20
NMCHAR=65
M=80
SUBSTRINGMATCH=47
N=81
O=82
H=75
I=76
J=77
NUMBER=50
K=78
U=88
T=87
W=90
V=89
Q=84
P=83
S=86
CDO=95
R=85
CDC=96
Y=92
PERCENTAGE=33
URL=67
X=91
Z=93
URI=21
PAGE_SYM=31
WS=98
DASHMATCH=44
EMS=52
N_PseudoFunction=16
N_RuleSet=7
NONASCII=61
N_MediaQuery=5
N_Selector=10
LBRACE=23
LPAREN=27
LENGTH=51
IMPORTANT_SYM=48
N_Function=12
TIME=56
KEYFRAMES_SYM=32
COMMA=25
N_StyleSheet=4
IDENT=26
PLUS=34
FREQ=57
RBRACKET=41
DOT=37
CHARSET_SYM=17
ANGLE=55
REMS=54
HASH=36
HEXCHAR=60
RESOLUTION=58
PREFIXMATCH=45
MINUS=59
N_Pseudo=15
SOLIDUS=49
SEMI=19
UNICODE=62
COLON=28
NMSTART=64
N_Declaration=11
OPEQ=42
FONTFACE_SYM=30
EXS=53
M_KeyframeSelector=9
N_Space=14
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=46
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Space", "N_Pseudo", "N_PseudoFunction", "CHARSET_SYM", "STRING", 
    "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", "COMMA", 
    "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", "KEYFRAMES_SYM", 
    "PERCENTAGE", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "STAR", 
    "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", "PREFIXMATCH", 
    "SUFFIXMATCH", "SUBSTRINGMATCH", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "LENGTH", "EMS", "EXS", "REMS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
    "MINUS", "HEXCHAR", "NONASCII", "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", 
    "NAME", "URL", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", 
    "Z", "COMMENT", "CDO", "CDC", "STRINGESC", "WS", "DIMENSION", "NL"
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

        self.dfa21 = self.DFA21(
            self, 21,
            eot = self.DFA21_eot,
            eof = self.DFA21_eof,
            min = self.DFA21_min,
            max = self.DFA21_max,
            accept = self.DFA21_accept,
            special = self.DFA21_special,
            transition = self.DFA21_transition
            )

        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
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
    # lesscss.g:65:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) ;
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
                # lesscss.g:66:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) )
                # lesscss.g:66:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:66:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:66:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet184)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:67:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:67:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet195)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet206)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet216) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: bodylist, imports, charSet
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
                    # 70:13: -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    # lesscss.g:70:16: ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:70:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:70:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:70:49: ( bodylist )?
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
    # lesscss.g:76:1: charSet : CHARSET_SYM STRING SEMI ;
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
                # lesscss.g:77:5: ( CHARSET_SYM STRING SEMI )
                # lesscss.g:77:9: CHARSET_SYM STRING SEMI
                pass 
                root_0 = self._adaptor.nil()

                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet269)
                if self._state.backtracking == 0:

                    CHARSET_SYM5_tree = self._adaptor.createWithPayload(CHARSET_SYM5)
                    root_0 = self._adaptor.becomeRoot(CHARSET_SYM5_tree, root_0)

                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet272)
                if self._state.backtracking == 0:

                    STRING6_tree = self._adaptor.createWithPayload(STRING6)
                    self._adaptor.addChild(root_0, STRING6_tree)

                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet274)



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
    # lesscss.g:83:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI ;
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
                # lesscss.g:84:5: ( IMPORT_SYM importUrl ( media_query_list )? SEMI )
                # lesscss.g:84:9: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports298)
                if self._state.backtracking == 0:

                    IMPORT_SYM8_tree = self._adaptor.createWithPayload(IMPORT_SYM8)
                    root_0 = self._adaptor.becomeRoot(IMPORT_SYM8_tree, root_0)

                self._state.following.append(self.FOLLOW_importUrl_in_imports301)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, importUrl9.tree)
                # lesscss.g:84:31: ( media_query_list )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((IDENT <= LA3_0 <= LPAREN)) :
                    alt3 = 1
                if alt3 == 1:
                    # lesscss.g:84:31: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports303)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports306)



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
    # lesscss.g:87:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:88:5: ( STRING | URI )
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
    # lesscss.g:96:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset13 = None



        try:
            try:
                # lesscss.g:97:5: ( ( bodyset )* )
                # lesscss.g:97:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:97:7: ( bodyset )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == MEDIA_SYM or LA4_0 == IDENT or LA4_0 == COLON or (FONTFACE_SYM <= LA4_0 <= KEYFRAMES_SYM) or (HASH <= LA4_0 <= STAR)) :
                        alt4 = 1


                    if alt4 == 1:
                        # lesscss.g:97:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist353)
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
    # lesscss.g:100:1: bodyset : ( ruleSet | media | page | fontface | keyframes );
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
                # lesscss.g:101:5: ( ruleSet | media | page | fontface | keyframes )
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
                    # lesscss.g:101:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset371)
                    ruleSet14 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet14.tree)


                elif alt5 == 2:
                    # lesscss.g:102:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset379)
                    media15 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media15.tree)


                elif alt5 == 3:
                    # lesscss.g:103:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset387)
                    page16 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page16.tree)


                elif alt5 == 4:
                    # lesscss.g:104:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset395)
                    fontface17 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface17.tree)


                elif alt5 == 5:
                    # lesscss.g:105:7: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_bodyset403)
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
    # lesscss.g:113:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM19 = None
        LBRACE21 = None
        RBRACE23 = None
        media_query_list20 = None

        ruleSet22 = None


        MEDIA_SYM19_tree = None
        LBRACE21_tree = None
        RBRACE23_tree = None

        try:
            try:
                # lesscss.g:114:5: ( MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE )
                # lesscss.g:114:7: MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                MEDIA_SYM19=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media428)
                if self._state.backtracking == 0:

                    MEDIA_SYM19_tree = self._adaptor.createWithPayload(MEDIA_SYM19)
                    root_0 = self._adaptor.becomeRoot(MEDIA_SYM19_tree, root_0)

                # lesscss.g:114:18: ( media_query_list )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((IDENT <= LA6_0 <= LPAREN)) :
                    alt6 = 1
                if alt6 == 1:
                    # lesscss.g:114:18: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media431)
                    media_query_list20 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list20.tree)



                LBRACE21=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media442)
                # lesscss.g:116:13: ( ruleSet )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == IDENT or LA7_0 == COLON or (HASH <= LA7_0 <= STAR)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:116:13: ruleSet
                        pass 
                        self._state.following.append(self.FOLLOW_ruleSet_in_media457)
                        ruleSet22 = self.ruleSet()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, ruleSet22.tree)


                    else:
                        break #loop7
                RBRACE23=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media468)



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
    # lesscss.g:123:1: media_query_list : media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) ;
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
                # lesscss.g:124:5: ( media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) )
                # lesscss.g:124:7: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list489)
                media_query24 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query24.tree)
                # lesscss.g:124:19: ( COMMA media_query )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # lesscss.g:124:20: COMMA media_query
                        pass 
                        COMMA25=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list492) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA25)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list494)
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
                    # 125:9: -> ^( N_MediaQuery ( media_query )+ )
                    # lesscss.g:125:12: ^( N_MediaQuery ( media_query )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaQuery, "N_MediaQuery"), root_1)

                    # lesscss.g:125:27: ( media_query )+
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
    # lesscss.g:128:1: media_query : ( ( IDENT )? media_type ( IDENT media_expr )* | media_expr ( IDENT media_expr )* );
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT27 = None
        IDENT29 = None
        IDENT32 = None
        media_type28 = None

        media_expr30 = None

        media_expr31 = None

        media_expr33 = None


        IDENT27_tree = None
        IDENT29_tree = None
        IDENT32_tree = None

        try:
            try:
                # lesscss.g:129:5: ( ( IDENT )? media_type ( IDENT media_expr )* | media_expr ( IDENT media_expr )* )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == IDENT) :
                    alt12 = 1
                elif (LA12_0 == LPAREN) :
                    alt12 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # lesscss.g:129:7: ( IDENT )? media_type ( IDENT media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:129:7: ( IDENT )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENT) :
                        LA9_1 = self.input.LA(2)

                        if (LA9_1 == IDENT) :
                            LA9_2 = self.input.LA(3)

                            if (LA9_2 == SEMI or LA9_2 == LBRACE or (COMMA <= LA9_2 <= IDENT)) :
                                alt9 = 1
                    if alt9 == 1:
                        # lesscss.g:129:9: IDENT
                        pass 
                        IDENT27=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query532)
                        if self._state.backtracking == 0:

                            IDENT27_tree = self._adaptor.createWithPayload(IDENT27)
                            self._adaptor.addChild(root_0, IDENT27_tree)




                    self._state.following.append(self.FOLLOW_media_type_in_media_query537)
                    media_type28 = self.media_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_type28.tree)
                    # lesscss.g:129:29: ( IDENT media_expr )*
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == IDENT) :
                            alt10 = 1


                        if alt10 == 1:
                            # lesscss.g:129:31: IDENT media_expr
                            pass 
                            IDENT29=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query541)
                            if self._state.backtracking == 0:

                                IDENT29_tree = self._adaptor.createWithPayload(IDENT29)
                                root_0 = self._adaptor.becomeRoot(IDENT29_tree, root_0)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query544)
                            media_expr30 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr30.tree)


                        else:
                            break #loop10


                elif alt12 == 2:
                    # lesscss.g:130:7: media_expr ( IDENT media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_expr_in_media_query555)
                    media_expr31 = self.media_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_expr31.tree)
                    # lesscss.g:130:18: ( IDENT media_expr )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == IDENT) :
                            alt11 = 1


                        if alt11 == 1:
                            # lesscss.g:130:20: IDENT media_expr
                            pass 
                            IDENT32=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query559)
                            if self._state.backtracking == 0:

                                IDENT32_tree = self._adaptor.createWithPayload(IDENT32)
                                root_0 = self._adaptor.becomeRoot(IDENT32_tree, root_0)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query562)
                            media_expr33 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr33.tree)


                        else:
                            break #loop11


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

    class media_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_type"
    # lesscss.g:133:1: media_type : IDENT ;
    def media_type(self, ):

        retval = self.media_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT34 = None

        IDENT34_tree = None

        try:
            try:
                # lesscss.g:134:5: ( IDENT )
                # lesscss.g:134:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT34=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_type582)
                if self._state.backtracking == 0:

                    IDENT34_tree = self._adaptor.createWithPayload(IDENT34)
                    self._adaptor.addChild(root_0, IDENT34_tree)




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

    # $ANTLR end "media_type"

    class media_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_expr"
    # lesscss.g:137:1: media_expr : LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN -> ^( N_MediaExpr media_feature ( expr )? ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN35 = None
        COLON37 = None
        COLON39 = None
        RPAREN40 = None
        media_feature36 = None

        expr38 = None


        LPAREN35_tree = None
        COLON37_tree = None
        COLON39_tree = None
        RPAREN40_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_media_feature = RewriteRuleSubtreeStream(self._adaptor, "rule media_feature")
        try:
            try:
                # lesscss.g:138:5: ( LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN -> ^( N_MediaExpr media_feature ( expr )? ) )
                # lesscss.g:138:7: LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN
                pass 
                LPAREN35=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr599) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN35)
                self._state.following.append(self.FOLLOW_media_feature_in_media_expr601)
                media_feature36 = self.media_feature()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_feature.add(media_feature36.tree)
                # lesscss.g:138:28: ( COLON expr )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == COLON) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == STRING or LA13_1 == URI or LA13_1 == IDENT or (PERCENTAGE <= LA13_1 <= PLUS) or LA13_1 == HASH or LA13_1 == FUNCTION or (NUMBER <= LA13_1 <= MINUS)) :
                        alt13 = 1
                if alt13 == 1:
                    # lesscss.g:138:30: COLON expr
                    pass 
                    COLON37=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr605) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON37)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr607)
                    expr38 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr38.tree)



                # lesscss.g:138:44: ( COLON )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == COLON) :
                    alt14 = 1
                if alt14 == 1:
                    # lesscss.g:138:44: COLON
                    pass 
                    COLON39=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr612) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON39)



                RPAREN40=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr615) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN40)

                # AST Rewrite
                # elements: media_feature, expr
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
                    # 139:9: -> ^( N_MediaExpr media_feature ( expr )? )
                    # lesscss.g:139:12: ^( N_MediaExpr media_feature ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_feature.nextTree())
                    # lesscss.g:139:40: ( expr )?
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

    class media_feature_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_feature_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_feature"
    # lesscss.g:142:1: media_feature : IDENT ;
    def media_feature(self, ):

        retval = self.media_feature_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT41 = None

        IDENT41_tree = None

        try:
            try:
                # lesscss.g:143:5: ( IDENT )
                # lesscss.g:143:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT41=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_feature652)
                if self._state.backtracking == 0:

                    IDENT41_tree = self._adaptor.createWithPayload(IDENT41)
                    self._adaptor.addChild(root_0, IDENT41_tree)




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

    # $ANTLR end "media_feature"

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:149:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM42 = None
        LBRACE43 = None
        RBRACE45 = None
        declarationset44 = None


        FONTFACE_SYM42_tree = None
        LBRACE43_tree = None
        RBRACE45_tree = None

        try:
            try:
                # lesscss.g:150:5: ( FONTFACE_SYM LBRACE declarationset RBRACE )
                # lesscss.g:150:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                FONTFACE_SYM42=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface672)
                if self._state.backtracking == 0:

                    FONTFACE_SYM42_tree = self._adaptor.createWithPayload(FONTFACE_SYM42)
                    root_0 = self._adaptor.becomeRoot(FONTFACE_SYM42_tree, root_0)

                LBRACE43=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface675)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface678)
                declarationset44 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset44.tree)
                RBRACE45=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface680)



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
    # lesscss.g:156:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM46 = None
        LBRACE48 = None
        RBRACE50 = None
        pseudoPage47 = None

        declarationset49 = None


        PAGE_SYM46_tree = None
        LBRACE48_tree = None
        RBRACE50_tree = None

        try:
            try:
                # lesscss.g:157:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE )
                # lesscss.g:157:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                PAGE_SYM46=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page701)
                if self._state.backtracking == 0:

                    PAGE_SYM46_tree = self._adaptor.createWithPayload(PAGE_SYM46)
                    root_0 = self._adaptor.becomeRoot(PAGE_SYM46_tree, root_0)

                # lesscss.g:157:17: ( pseudoPage )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == COLON) :
                    alt15 = 1
                if alt15 == 1:
                    # lesscss.g:157:17: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page704)
                    pseudoPage47 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudoPage47.tree)



                LBRACE48=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page707)
                self._state.following.append(self.FOLLOW_declarationset_in_page710)
                declarationset49 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset49.tree)
                RBRACE50=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page712)



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
    # lesscss.g:160:1: pseudoPage : COLON a= IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON51 = None

        a_tree = None
        COLON51_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:161:5: ( COLON a= IDENT -> IDENT )
                # lesscss.g:161:7: COLON a= IDENT
                pass 
                COLON51=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage730) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON51)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage734) 
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
                    # 163:9: -> IDENT
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
    # lesscss.g:170:1: keyframes : KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE ;
    def keyframes(self, ):

        retval = self.keyframes_return()
        retval.start = self.input.LT(1)

        root_0 = None

        KEYFRAMES_SYM52 = None
        IDENT53 = None
        LBRACE54 = None
        RBRACE56 = None
        keyframes_block55 = None


        KEYFRAMES_SYM52_tree = None
        IDENT53_tree = None
        LBRACE54_tree = None
        RBRACE56_tree = None

        try:
            try:
                # lesscss.g:171:5: ( KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE )
                # lesscss.g:171:7: KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                KEYFRAMES_SYM52=self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes778)
                if self._state.backtracking == 0:

                    KEYFRAMES_SYM52_tree = self._adaptor.createWithPayload(KEYFRAMES_SYM52)
                    root_0 = self._adaptor.becomeRoot(KEYFRAMES_SYM52_tree, root_0)

                IDENT53=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes781)
                if self._state.backtracking == 0:

                    IDENT53_tree = self._adaptor.createWithPayload(IDENT53)
                    self._adaptor.addChild(root_0, IDENT53_tree)

                LBRACE54=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes783)
                # lesscss.g:171:36: ( keyframes_block )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == IDENT or LA16_0 == PERCENTAGE) :
                        alt16 = 1


                    if alt16 == 1:
                        # lesscss.g:171:36: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes786)
                        keyframes_block55 = self.keyframes_block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, keyframes_block55.tree)


                    else:
                        break #loop16
                RBRACE56=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes789)



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
    # lesscss.g:174:1: keyframes_block : keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) ;
    def keyframes_block(self, ):

        retval = self.keyframes_block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA58 = None
        LBRACE60 = None
        RBRACE62 = None
        keyframe_selector57 = None

        keyframe_selector59 = None

        declarationset61 = None


        COMMA58_tree = None
        LBRACE60_tree = None
        RBRACE62_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_keyframe_selector = RewriteRuleSubtreeStream(self._adaptor, "rule keyframe_selector")
        try:
            try:
                # lesscss.g:175:5: ( keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) )
                # lesscss.g:175:7: keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block807)
                keyframe_selector57 = self.keyframe_selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_keyframe_selector.add(keyframe_selector57.tree)
                # lesscss.g:175:25: ( COMMA keyframe_selector )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == COMMA) :
                        alt17 = 1


                    if alt17 == 1:
                        # lesscss.g:175:27: COMMA keyframe_selector
                        pass 
                        COMMA58=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keyframes_block811) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA58)
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block813)
                        keyframe_selector59 = self.keyframe_selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_keyframe_selector.add(keyframe_selector59.tree)


                    else:
                        break #loop17
                LBRACE60=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes_block818) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE60)
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block820)
                declarationset61 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset61.tree)
                RBRACE62=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes_block822) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE62)

                # AST Rewrite
                # elements: declarationset, keyframe_selector
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
                    # 176:9: -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    # lesscss.g:176:12: ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_KeyframeBlock, "N_KeyframeBlock"), root_1)

                    # lesscss.g:176:30: ( ^( M_KeyframeSelector keyframe_selector ) )+
                    if not (stream_keyframe_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_keyframe_selector.hasNext():
                        # lesscss.g:176:30: ^( M_KeyframeSelector keyframe_selector )
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
    # lesscss.g:180:1: keyframe_selector : ( IDENT | PERCENTAGE ) ;
    def keyframe_selector(self, ):

        retval = self.keyframe_selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set63 = None

        set63_tree = None

        try:
            try:
                # lesscss.g:181:5: ( ( IDENT | PERCENTAGE ) )
                # lesscss.g:181:7: ( IDENT | PERCENTAGE )
                pass 
                root_0 = self._adaptor.nil()

                set63 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == PERCENTAGE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set63))
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
    # lesscss.g:188:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA65 = None
        LBRACE67 = None
        RBRACE69 = None
        selector64 = None

        selector66 = None

        declarationset68 = None


        COMMA65_tree = None
        LBRACE67_tree = None
        RBRACE69_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:189:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:189:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet893)
                selector64 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector64.tree)
                # lesscss.g:189:16: ( COMMA selector )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == COMMA) :
                        alt18 = 1


                    if alt18 == 1:
                        # lesscss.g:189:17: COMMA selector
                        pass 
                        COMMA65=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet896) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA65)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet898)
                        selector66 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector66.tree)


                    else:
                        break #loop18
                LBRACE67=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet902) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE67)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet904)
                declarationset68 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset68.tree)
                RBRACE69=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet906) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE69)

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
                    # 190:9: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:190:12: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:190:24: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:190:24: ^( N_Selector selector )
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
    # lesscss.g:193:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector70 = None

        combinator71 = None

        simpleSelector72 = None



        try:
            try:
                # lesscss.g:194:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:194:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector946)
                simpleSelector70 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector70.tree)
                # lesscss.g:194:22: ( combinator simpleSelector )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == IDENT or LA19_0 == COLON or (PLUS <= LA19_0 <= STAR)) :
                        alt19 = 1


                    if alt19 == 1:
                        # lesscss.g:194:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector949)
                        combinator71 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator71.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector951)
                        simpleSelector72 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector72.tree)


                    else:
                        break #loop19



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
    # lesscss.g:197:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS73 = None
        GREATER74 = None

        PLUS73_tree = None
        GREATER74_tree = None

        try:
            try:
                # lesscss.g:198:5: ( PLUS | GREATER | )
                alt20 = 3
                LA20 = self.input.LA(1)
                if LA20 == PLUS:
                    alt20 = 1
                elif LA20 == GREATER:
                    alt20 = 2
                elif LA20 == IDENT or LA20 == COLON or LA20 == HASH or LA20 == DOT or LA20 == LBRACKET or LA20 == STAR:
                    alt20 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # lesscss.g:198:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS73=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator970)
                    if self._state.backtracking == 0:

                        PLUS73_tree = self._adaptor.createWithPayload(PLUS73)
                        self._adaptor.addChild(root_0, PLUS73_tree)



                elif alt20 == 2:
                    # lesscss.g:199:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER74=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator978)
                    if self._state.backtracking == 0:

                        GREATER74_tree = self._adaptor.createWithPayload(GREATER74)
                        self._adaptor.addChild(root_0, GREATER74_tree)



                elif alt20 == 3:
                    # lesscss.g:201:5: 
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
    # lesscss.g:203:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName75 = None

        elementSubsequent76 = None

        elementSubsequent77 = None



        try:
            try:
                # lesscss.g:204:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == IDENT or LA23_0 == STAR) :
                    alt23 = 1
                elif (LA23_0 == COLON or (HASH <= LA23_0 <= LBRACKET)) :
                    alt23 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # lesscss.g:204:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector1001)
                    elementName75 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName75.tree)
                    # lesscss.g:204:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop21
                        alt21 = 2
                        alt21 = self.dfa21.predict(self.input)
                        if alt21 == 1:
                            # lesscss.g:204:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1008)
                            elementSubsequent76 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent76.tree)


                        else:
                            break #loop21


                elif alt23 == 2:
                    # lesscss.g:205:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:205:7: ( ( esPred )=> elementSubsequent )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22 = self.input.LA(1)
                        if LA22 == HASH:
                            LA22_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt22 = 1


                        elif LA22 == DOT:
                            LA22_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt22 = 1


                        elif LA22 == LBRACKET:
                            LA22_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt22 = 1


                        elif LA22 == COLON:
                            LA22_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt22 = 1



                        if alt22 == 1:
                            # lesscss.g:205:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1023)
                            elementSubsequent77 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent77.tree)


                        else:
                            if cnt22 >= 1:
                                break #loop22

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


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
    # lesscss.g:208:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set78 = None

        set78_tree = None

        try:
            try:
                # lesscss.g:209:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set78 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set78))
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
    # lesscss.g:212:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set79 = None

        set79_tree = None

        try:
            try:
                # lesscss.g:213:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set79 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set79))
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
    # lesscss.g:217:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH80 = None
        cssClass81 = None

        attrib82 = None

        pseudo83 = None


        HASH80_tree = None

        try:
            try:
                # lesscss.g:218:5: ( HASH | cssClass | attrib | pseudo )
                alt24 = 4
                LA24 = self.input.LA(1)
                if LA24 == HASH:
                    alt24 = 1
                elif LA24 == DOT:
                    alt24 = 2
                elif LA24 == LBRACKET:
                    alt24 = 3
                elif LA24 == COLON:
                    alt24 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # lesscss.g:218:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH80=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent1096)
                    if self._state.backtracking == 0:

                        HASH80_tree = self._adaptor.createWithPayload(HASH80)
                        self._adaptor.addChild(root_0, HASH80_tree)



                elif alt24 == 2:
                    # lesscss.g:219:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent1104)
                    cssClass81 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass81.tree)


                elif alt24 == 3:
                    # lesscss.g:220:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent1112)
                    attrib82 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib82.tree)


                elif alt24 == 4:
                    # lesscss.g:221:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent1120)
                    pseudo83 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo83.tree)


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
    # lesscss.g:224:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT84 = None

        a_tree = None
        DOT84_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:225:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:225:7: DOT a= IDENT
                pass 
                DOT84=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass1137) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT84)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass1141) 
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
                    # 227:9: -> IDENT
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
    # lesscss.g:230:1: pseudo : (a= COLON (b= COLON )? IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | c= COLON (d= COLON )? FUNCTION expr RPAREN -> ^( N_Pseudo $c ( $d)? ^( N_PseudoFunction FUNCTION expr ) ) | e= COLON (f= COLON )? FUNCTION LBRACKET expr RBRACKET RPAREN -> ^( N_Pseudo $e ( $f)? ^( N_PseudoFunction FUNCTION LBRACKET expr RBRACKET ) ) | g= COLON (h= COLON )? FUNCTION pseudo RPAREN -> ^( N_Pseudo $g ( $h)? ^( N_PseudoFunction FUNCTION pseudo ) ) );
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        c = None
        d = None
        e = None
        f = None
        g = None
        h = None
        IDENT85 = None
        FUNCTION86 = None
        RPAREN88 = None
        FUNCTION89 = None
        LBRACKET90 = None
        RBRACKET92 = None
        RPAREN93 = None
        FUNCTION94 = None
        RPAREN96 = None
        expr87 = None

        expr91 = None

        pseudo95 = None


        a_tree = None
        b_tree = None
        c_tree = None
        d_tree = None
        e_tree = None
        f_tree = None
        g_tree = None
        h_tree = None
        IDENT85_tree = None
        FUNCTION86_tree = None
        RPAREN88_tree = None
        FUNCTION89_tree = None
        LBRACKET90_tree = None
        RBRACKET92_tree = None
        RPAREN93_tree = None
        FUNCTION94_tree = None
        RPAREN96_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_pseudo = RewriteRuleSubtreeStream(self._adaptor, "rule pseudo")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:231:5: (a= COLON (b= COLON )? IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | c= COLON (d= COLON )? FUNCTION expr RPAREN -> ^( N_Pseudo $c ( $d)? ^( N_PseudoFunction FUNCTION expr ) ) | e= COLON (f= COLON )? FUNCTION LBRACKET expr RBRACKET RPAREN -> ^( N_Pseudo $e ( $f)? ^( N_PseudoFunction FUNCTION LBRACKET expr RBRACKET ) ) | g= COLON (h= COLON )? FUNCTION pseudo RPAREN -> ^( N_Pseudo $g ( $h)? ^( N_PseudoFunction FUNCTION pseudo ) ) )
                alt29 = 4
                LA29_0 = self.input.LA(1)

                if (LA29_0 == COLON) :
                    LA29 = self.input.LA(2)
                    if LA29 == COLON:
                        LA29_2 = self.input.LA(3)

                        if (LA29_2 == FUNCTION) :
                            LA29 = self.input.LA(4)
                            if LA29 == LBRACKET:
                                alt29 = 3
                            elif LA29 == STRING or LA29 == URI or LA29 == IDENT or LA29 == PERCENTAGE or LA29 == PLUS or LA29 == HASH or LA29 == FUNCTION or LA29 == NUMBER or LA29 == LENGTH or LA29 == EMS or LA29 == EXS or LA29 == REMS or LA29 == ANGLE or LA29 == TIME or LA29 == FREQ or LA29 == RESOLUTION or LA29 == MINUS:
                                alt29 = 2
                            elif LA29 == COLON:
                                alt29 = 4
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 29, 4, self.input)

                                raise nvae

                        elif (LA29_2 == IDENT) :
                            alt29 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 29, 2, self.input)

                            raise nvae

                    elif LA29 == IDENT:
                        alt29 = 1
                    elif LA29 == FUNCTION:
                        LA29 = self.input.LA(3)
                        if LA29 == LBRACKET:
                            alt29 = 3
                        elif LA29 == STRING or LA29 == URI or LA29 == IDENT or LA29 == PERCENTAGE or LA29 == PLUS or LA29 == HASH or LA29 == FUNCTION or LA29 == NUMBER or LA29 == LENGTH or LA29 == EMS or LA29 == EXS or LA29 == REMS or LA29 == ANGLE or LA29 == TIME or LA29 == FREQ or LA29 == RESOLUTION or LA29 == MINUS:
                            alt29 = 2
                        elif LA29 == COLON:
                            alt29 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 29, 4, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 29, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # lesscss.g:231:7: a= COLON (b= COLON )? IDENT
                    pass 
                    a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1183) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(a)
                    # lesscss.g:231:16: (b= COLON )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == COLON) :
                        alt25 = 1
                    if alt25 == 1:
                        # lesscss.g:231:16: b= COLON
                        pass 
                        b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1187) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(b)



                    IDENT85=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1190) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT85)

                    # AST Rewrite
                    # elements: a, b, IDENT
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
                        # 232:9: -> ^( N_Pseudo $a ( $b)? IDENT )
                        # lesscss.g:232:12: ^( N_Pseudo $a ( $b)? IDENT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:232:26: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 2:
                    # lesscss.g:234:7: c= COLON (d= COLON )? FUNCTION expr RPAREN
                    pass 
                    c=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1228) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(c)
                    # lesscss.g:234:16: (d= COLON )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COLON) :
                        alt26 = 1
                    if alt26 == 1:
                        # lesscss.g:234:16: d= COLON
                        pass 
                        d=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1232) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(d)



                    FUNCTION86=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1235) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION86)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1237)
                    expr87 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr87.tree)
                    RPAREN88=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1239) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN88)

                    # AST Rewrite
                    # elements: d, expr, c, FUNCTION
                    # token labels: d, c
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0
                        stream_d = RewriteRuleTokenStream(self._adaptor, "token d", d)
                        stream_c = RewriteRuleTokenStream(self._adaptor, "token c", c)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 235:9: -> ^( N_Pseudo $c ( $d)? ^( N_PseudoFunction FUNCTION expr ) )
                        # lesscss.g:235:12: ^( N_Pseudo $c ( $d)? ^( N_PseudoFunction FUNCTION expr ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_c.nextNode())
                        # lesscss.g:235:26: ( $d)?
                        if stream_d.hasNext():
                            self._adaptor.addChild(root_1, stream_d.nextNode())


                        stream_d.reset();
                        # lesscss.g:235:30: ^( N_PseudoFunction FUNCTION expr )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_2)

                        self._adaptor.addChild(root_2, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_2, stream_expr.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 3:
                    # lesscss.g:237:7: e= COLON (f= COLON )? FUNCTION LBRACKET expr RBRACKET RPAREN
                    pass 
                    e=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1281) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(e)
                    # lesscss.g:237:16: (f= COLON )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == COLON) :
                        alt27 = 1
                    if alt27 == 1:
                        # lesscss.g:237:16: f= COLON
                        pass 
                        f=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1285) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(f)



                    FUNCTION89=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1288) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION89)
                    LBRACKET90=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudo1290) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET90)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1292)
                    expr91 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr91.tree)
                    RBRACKET92=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudo1294) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET92)
                    RPAREN93=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1296) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN93)

                    # AST Rewrite
                    # elements: e, RBRACKET, expr, FUNCTION, LBRACKET, f
                    # token labels: f, e
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0
                        stream_f = RewriteRuleTokenStream(self._adaptor, "token f", f)
                        stream_e = RewriteRuleTokenStream(self._adaptor, "token e", e)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 238:9: -> ^( N_Pseudo $e ( $f)? ^( N_PseudoFunction FUNCTION LBRACKET expr RBRACKET ) )
                        # lesscss.g:238:12: ^( N_Pseudo $e ( $f)? ^( N_PseudoFunction FUNCTION LBRACKET expr RBRACKET ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_e.nextNode())
                        # lesscss.g:238:26: ( $f)?
                        if stream_f.hasNext():
                            self._adaptor.addChild(root_1, stream_f.nextNode())


                        stream_f.reset();
                        # lesscss.g:238:30: ^( N_PseudoFunction FUNCTION LBRACKET expr RBRACKET )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_2)

                        self._adaptor.addChild(root_2, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_2, stream_LBRACKET.nextNode())
                        self._adaptor.addChild(root_2, stream_expr.nextTree())
                        self._adaptor.addChild(root_2, stream_RBRACKET.nextNode())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 4:
                    # lesscss.g:240:7: g= COLON (h= COLON )? FUNCTION pseudo RPAREN
                    pass 
                    g=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1342) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(g)
                    # lesscss.g:240:16: (h= COLON )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == COLON) :
                        alt28 = 1
                    if alt28 == 1:
                        # lesscss.g:240:16: h= COLON
                        pass 
                        h=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1346) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(h)



                    FUNCTION94=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1349) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION94)
                    self._state.following.append(self.FOLLOW_pseudo_in_pseudo1351)
                    pseudo95 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudo.add(pseudo95.tree)
                    RPAREN96=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1353) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN96)

                    # AST Rewrite
                    # elements: pseudo, h, g, FUNCTION
                    # token labels: g, h
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0
                        stream_g = RewriteRuleTokenStream(self._adaptor, "token g", g)
                        stream_h = RewriteRuleTokenStream(self._adaptor, "token h", h)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 241:9: -> ^( N_Pseudo $g ( $h)? ^( N_PseudoFunction FUNCTION pseudo ) )
                        # lesscss.g:241:12: ^( N_Pseudo $g ( $h)? ^( N_PseudoFunction FUNCTION pseudo ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_g.nextNode())
                        # lesscss.g:241:26: ( $h)?
                        if stream_h.hasNext():
                            self._adaptor.addChild(root_1, stream_h.nextNode())


                        stream_h.reset();
                        # lesscss.g:241:30: ^( N_PseudoFunction FUNCTION pseudo )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_2)

                        self._adaptor.addChild(root_2, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_2, stream_pseudo.nextTree())

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

    # $ANTLR end "pseudo"

    class attrib_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attrib_return, self).__init__()

            self.tree = None




    # $ANTLR start "attrib"
    # lesscss.g:245:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET97 = None
        RBRACKET99 = None
        attribBody98 = None


        LBRACKET97_tree = None
        RBRACKET99_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:246:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:246:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET97=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1402) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET97)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1404)
                attribBody98 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody98.tree)
                RBRACKET99=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1406) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET99)

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
                    # 247:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:247:13: ^( N_Attrib attribBody )
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
    # lesscss.g:250:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) ( IDENT | STRING ) );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT100 = None
        IDENT101 = None
        set102 = None
        set103 = None

        IDENT100_tree = None
        IDENT101_tree = None
        set102_tree = None
        set103_tree = None

        try:
            try:
                # lesscss.g:251:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) ( IDENT | STRING ) )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == IDENT) :
                    LA30_1 = self.input.LA(2)

                    if ((OPEQ <= LA30_1 <= SUBSTRINGMATCH)) :
                        alt30 = 2
                    elif (LA30_1 == RBRACKET) :
                        alt30 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 30, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # lesscss.g:251:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT100=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1441)
                    if self._state.backtracking == 0:

                        IDENT100_tree = self._adaptor.createWithPayload(IDENT100)
                        self._adaptor.addChild(root_0, IDENT100_tree)



                elif alt30 == 2:
                    # lesscss.g:252:7: IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) ( IDENT | STRING )
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT101=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1449)
                    if self._state.backtracking == 0:

                        IDENT101_tree = self._adaptor.createWithPayload(IDENT101)
                        self._adaptor.addChild(root_0, IDENT101_tree)

                    set102 = self.input.LT(1)
                    set102 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= SUBSTRINGMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set102), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set103 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set103))
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

    # $ANTLR end "attribBody"

    class declarationset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declarationset_return, self).__init__()

            self.tree = None




    # $ANTLR start "declarationset"
    # lesscss.g:265:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI105 = None
        SEMI107 = None
        declaration104 = None

        declaration106 = None


        SEMI105_tree = None
        SEMI107_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:266:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:266:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1590)
                declaration104 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration104.tree)
                # lesscss.g:266:19: ( SEMI declaration )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == SEMI) :
                        LA31_1 = self.input.LA(2)

                        if (LA31_1 == IDENT or LA31_1 == STAR) :
                            alt31 = 1




                    if alt31 == 1:
                        # lesscss.g:266:20: SEMI declaration
                        pass 
                        SEMI105=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1593) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI105)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1595)
                        declaration106 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration106.tree)


                    else:
                        break #loop31
                # lesscss.g:266:39: ( SEMI )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == SEMI) :
                    alt32 = 1
                if alt32 == 1:
                    # lesscss.g:266:39: SEMI
                    pass 
                    SEMI107=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1599) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI107)




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
                    # 267:10: -> ( declaration )+
                    # lesscss.g:267:13: ( declaration )+
                    if not (stream_declaration.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_declaration.hasNext():
                        self._adaptor.addChild(root_0, stream_declaration.nextTree())


                    stream_declaration.reset()



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
    # lesscss.g:270:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON109 = None
        property108 = None

        expr110 = None

        prio111 = None


        COLON109_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:271:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:271:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1631)
                property108 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property108.tree)
                COLON109=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1633) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON109)
                self._state.following.append(self.FOLLOW_expr_in_declaration1635)
                expr110 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr110.tree)
                # lesscss.g:271:27: ( prio )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == IMPORTANT_SYM) :
                    alt33 = 1
                if alt33 == 1:
                    # lesscss.g:271:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1637)
                    prio111 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prio.add(prio111.tree)




                # AST Rewrite
                # elements: expr, prio, property
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
                    # 272:9: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:272:12: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:272:42: ( prio )?
                    if stream_prio.hasNext():
                        self._adaptor.addChild(root_1, stream_prio.nextTree())


                    stream_prio.reset();

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
    # lesscss.g:275:1: property : ( IDENT | STAR a= IDENT -> IDENT );
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
                # lesscss.g:276:5: ( IDENT | STAR a= IDENT -> IDENT )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == IDENT) :
                    alt34 = 1
                elif (LA34_0 == STAR) :
                    alt34 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # lesscss.g:276:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT112=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1676)
                    if self._state.backtracking == 0:

                        IDENT112_tree = self._adaptor.createWithPayload(IDENT112)
                        self._adaptor.addChild(root_0, IDENT112_tree)



                elif alt34 == 2:
                    # lesscss.g:280:7: STAR a= IDENT
                    pass 
                    STAR113=self.match(self.input, STAR, self.FOLLOW_STAR_in_property1695) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR113)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1699) 
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
                        # 282:9: -> IDENT
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
    # lesscss.g:285:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM114 = None

        IMPORTANT_SYM114_tree = None

        try:
            try:
                # lesscss.g:286:5: ( IMPORTANT_SYM )
                # lesscss.g:286:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM114=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1739)
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
    # lesscss.g:289:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term115 = None

        operator116 = None

        term117 = None



        try:
            try:
                # lesscss.g:290:5: ( term ( operator term )* )
                # lesscss.g:290:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1756)
                term115 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term115.tree)
                # lesscss.g:290:12: ( operator term )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == COMMA) :
                        LA35_2 = self.input.LA(2)

                        if (LA35_2 == IDENT) :
                            LA35_4 = self.input.LA(3)

                            if ((STRING <= LA35_4 <= SEMI) or LA35_4 == URI or (RBRACE <= LA35_4 <= IDENT) or (COLON <= LA35_4 <= RPAREN) or (PERCENTAGE <= LA35_4 <= PLUS) or (HASH <= LA35_4 <= DOT) or (FUNCTION <= LA35_4 <= RBRACKET) or (IMPORTANT_SYM <= LA35_4 <= MINUS)) :
                                alt35 = 1


                        elif (LA35_2 == STRING or LA35_2 == URI or (PERCENTAGE <= LA35_2 <= PLUS) or LA35_2 == HASH or LA35_2 == FUNCTION or (NUMBER <= LA35_2 <= MINUS)) :
                            alt35 = 1


                    elif (LA35_0 == STRING or LA35_0 == URI or LA35_0 == IDENT or (PERCENTAGE <= LA35_0 <= PLUS) or LA35_0 == HASH or LA35_0 == FUNCTION or (SOLIDUS <= LA35_0 <= MINUS)) :
                        alt35 = 1


                    if alt35 == 1:
                        # lesscss.g:290:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1759)
                        operator116 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator116.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1762)
                        term117 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term117.tree)


                    else:
                        break #loop35



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
    # lesscss.g:293:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
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
                # lesscss.g:294:5: ( SOLIDUS | COMMA | -> N_Space )
                alt36 = 3
                LA36 = self.input.LA(1)
                if LA36 == SOLIDUS:
                    alt36 = 1
                elif LA36 == COMMA:
                    alt36 = 2
                elif LA36 == STRING or LA36 == URI or LA36 == IDENT or LA36 == PERCENTAGE or LA36 == PLUS or LA36 == HASH or LA36 == FUNCTION or LA36 == NUMBER or LA36 == LENGTH or LA36 == EMS or LA36 == EXS or LA36 == REMS or LA36 == ANGLE or LA36 == TIME or LA36 == FREQ or LA36 == RESOLUTION or LA36 == MINUS:
                    alt36 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # lesscss.g:294:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS118=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1783)
                    if self._state.backtracking == 0:

                        SOLIDUS118_tree = self._adaptor.createWithPayload(SOLIDUS118)
                        self._adaptor.addChild(root_0, SOLIDUS118_tree)



                elif alt36 == 2:
                    # lesscss.g:295:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA119=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1791)
                    if self._state.backtracking == 0:

                        COMMA119_tree = self._adaptor.createWithPayload(COMMA119)
                        self._adaptor.addChild(root_0, COMMA119_tree)



                elif alt36 == 3:
                    # lesscss.g:296:7: 
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
                        # 296:7: -> N_Space
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
    # lesscss.g:299:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set121 = None
        STRING122 = None
        IDENT123 = None
        URI124 = None
        unaryOperator120 = None

        function125 = None

        hexColor126 = None


        set121_tree = None
        STRING122_tree = None
        IDENT123_tree = None
        URI124_tree = None

        try:
            try:
                # lesscss.g:300:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | IDENT | URI | function | hexColor )
                alt38 = 6
                LA38 = self.input.LA(1)
                if LA38 == PERCENTAGE or LA38 == PLUS or LA38 == NUMBER or LA38 == LENGTH or LA38 == EMS or LA38 == EXS or LA38 == REMS or LA38 == ANGLE or LA38 == TIME or LA38 == FREQ or LA38 == RESOLUTION or LA38 == MINUS:
                    alt38 = 1
                elif LA38 == STRING:
                    alt38 = 2
                elif LA38 == IDENT:
                    LA38 = self.input.LA(2)
                    if LA38 == STRING or LA38 == SEMI or LA38 == URI or LA38 == RBRACE or LA38 == COMMA or LA38 == IDENT or LA38 == RPAREN or LA38 == PERCENTAGE or LA38 == PLUS or LA38 == HASH or LA38 == FUNCTION or LA38 == RBRACKET or LA38 == IMPORTANT_SYM or LA38 == SOLIDUS or LA38 == NUMBER or LA38 == LENGTH or LA38 == EMS or LA38 == EXS or LA38 == REMS or LA38 == ANGLE or LA38 == TIME or LA38 == FREQ or LA38 == RESOLUTION or LA38 == MINUS:
                        alt38 = 3
                    elif LA38 == COLON:
                        LA38_8 = self.input.LA(3)

                        if (LA38_8 == IDENT or LA38_8 == COLON or LA38_8 == DOT or LA38_8 == FUNCTION) :
                            alt38 = 5
                        elif (LA38_8 == RPAREN) :
                            alt38 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 38, 8, self.input)

                            raise nvae

                    elif LA38 == DOT:
                        alt38 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 38, 3, self.input)

                        raise nvae

                elif LA38 == URI:
                    alt38 = 4
                elif LA38 == FUNCTION:
                    alt38 = 5
                elif LA38 == HASH:
                    alt38 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae

                if alt38 == 1:
                    # lesscss.g:300:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | ANGLE | TIME | FREQ | RESOLUTION )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:300:20: ( unaryOperator )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == PLUS or LA37_0 == MINUS) :
                        alt37 = 1
                    if alt37 == 1:
                        # lesscss.g:300:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1819)
                        unaryOperator120 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator120.tree, root_0)



                    set121 = self.input.LT(1)
                    if self.input.LA(1) == PERCENTAGE or (NUMBER <= self.input.LA(1) <= RESOLUTION):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set121))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt38 == 2:
                    # lesscss.g:313:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING122=self.match(self.input, STRING, self.FOLLOW_STRING_in_term2009)
                    if self._state.backtracking == 0:

                        STRING122_tree = self._adaptor.createWithPayload(STRING122)
                        self._adaptor.addChild(root_0, STRING122_tree)



                elif alt38 == 3:
                    # lesscss.g:314:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT123=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term2017)
                    if self._state.backtracking == 0:

                        IDENT123_tree = self._adaptor.createWithPayload(IDENT123)
                        self._adaptor.addChild(root_0, IDENT123_tree)



                elif alt38 == 4:
                    # lesscss.g:315:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI124=self.match(self.input, URI, self.FOLLOW_URI_in_term2025)
                    if self._state.backtracking == 0:

                        URI124_tree = self._adaptor.createWithPayload(URI124)
                        self._adaptor.addChild(root_0, URI124_tree)



                elif alt38 == 5:
                    # lesscss.g:316:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term2033)
                    function125 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function125.tree)


                elif alt38 == 6:
                    # lesscss.g:317:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term2041)
                    hexColor126 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor126.tree)


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
    # lesscss.g:320:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set127 = None

        set127_tree = None

        try:
            try:
                # lesscss.g:321:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set127 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set127))
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
    # lesscss.g:326:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN130 = None
        RPAREN133 = None
        fnct_name128 = None

        fnct_args129 = None

        fnct_name131 = None

        expr132 = None


        RPAREN130_tree = None
        RPAREN133_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:327:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # lesscss.g:327:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function2086)
                    fnct_name128 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name128.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function2088)
                    fnct_args129 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args129.tree)
                    RPAREN130=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function2090) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN130)

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
                        # 328:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:328:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt39 == 2:
                    # lesscss.g:330:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function2117)
                    fnct_name131 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name131.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function2119)
                    expr132 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr132.tree)
                    RPAREN133=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function2121) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN133)

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
                        # 331:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:331:12: ^( N_Function fnct_name expr )
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
    # lesscss.g:335:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT134 = None
        set135 = None
        FUNCTION136 = None

        IDENT134_tree = None
        set135_tree = None
        FUNCTION136_tree = None

        try:
            try:
                # lesscss.g:336:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:336:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:336:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == IDENT) :
                        alt41 = 1


                    if alt41 == 1:
                        # lesscss.g:336:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT134=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name2158)
                        if self._state.backtracking == 0:

                            IDENT134_tree = self._adaptor.createWithPayload(IDENT134)
                            self._adaptor.addChild(root_0, IDENT134_tree)

                        # lesscss.g:336:14: ( COLON | DOT )+
                        cnt40 = 0
                        while True: #loop40
                            alt40 = 2
                            LA40_0 = self.input.LA(1)

                            if (LA40_0 == COLON or LA40_0 == DOT) :
                                alt40 = 1


                            if alt40 == 1:
                                # lesscss.g:
                                pass 
                                set135 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set135))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt40 >= 1:
                                    break #loop40

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(40, self.input)
                                raise eee

                            cnt40 += 1


                    else:
                        break #loop41
                FUNCTION136=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name2170)
                if self._state.backtracking == 0:

                    FUNCTION136_tree = self._adaptor.createWithPayload(FUNCTION136)
                    root_0 = self._adaptor.becomeRoot(FUNCTION136_tree, root_0)




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
    # lesscss.g:339:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA138 = None
        fnct_arg137 = None

        fnct_arg139 = None


        COMMA138_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:340:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:340:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args2190)
                fnct_arg137 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg137.tree)
                # lesscss.g:340:16: ( COMMA fnct_arg )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == COMMA) :
                        alt42 = 1


                    if alt42 == 1:
                        # lesscss.g:340:17: COMMA fnct_arg
                        pass 
                        COMMA138=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args2193) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA138)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args2195)
                        fnct_arg139 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg139.tree)


                    else:
                        break #loop42

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
                    # 341:9: -> ( fnct_arg )+
                    # lesscss.g:341:12: ( fnct_arg )+
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
    # lesscss.g:344:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT140 = None
        OPEQ141 = None
        expr142 = None


        IDENT140_tree = None
        OPEQ141_tree = None

        try:
            try:
                # lesscss.g:345:5: ( IDENT OPEQ expr )
                # lesscss.g:345:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT140=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg2227)
                if self._state.backtracking == 0:

                    IDENT140_tree = self._adaptor.createWithPayload(IDENT140)
                    self._adaptor.addChild(root_0, IDENT140_tree)

                OPEQ141=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg2229)
                if self._state.backtracking == 0:

                    OPEQ141_tree = self._adaptor.createWithPayload(OPEQ141)
                    root_0 = self._adaptor.becomeRoot(OPEQ141_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg2232)
                expr142 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr142.tree)



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
    # lesscss.g:348:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH143 = None

        HASH143_tree = None

        try:
            try:
                # lesscss.g:349:5: ( HASH )
                # lesscss.g:349:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH143=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor2249)
                if self._state.backtracking == 0:

                    HASH143_tree = self._adaptor.createWithPayload(HASH143)
                    self._adaptor.addChild(root_0, HASH143_tree)




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
        # lesscss.g:204:20: ( esPred )
        # lesscss.g:204:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss1005)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:205:8: ( esPred )
        # lesscss.g:205:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss1020)
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



    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\1\27\3\uffff\4\0\3\uffff"
        )

    DFA21_max = DFA.unpack(
        u"\1\47\3\uffff\4\0\3\uffff"
        )

    DFA21_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA21_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA21_transition = [
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

    # class definition for DFA #21

    class DFA21(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA21_4 = input.LA(1)

                 
                index21_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index21_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA21_5 = input.LA(1)

                 
                index21_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index21_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA21_6 = input.LA(1)

                 
                index21_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index21_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA21_7 = input.LA(1)

                 
                index21_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index21_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 21, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\1\32\1\34\1\22\1\32\1\22\2\uffff"
        )

    DFA39_max = DFA.unpack(
        u"\1\50\1\45\1\73\1\50\1\73\2\uffff"
        )

    DFA39_accept = DFA.unpack(
        u"\5\uffff\1\2\1\1"
        )

    DFA39_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA39_transition = [
        DFA.unpack(u"\1\1\15\uffff\1\2"),
        DFA.unpack(u"\1\3\10\uffff\1\3"),
        DFA.unpack(u"\1\5\2\uffff\1\5\4\uffff\1\4\6\uffff\2\5\1\uffff\1"
        u"\5\3\uffff\1\5\11\uffff\12\5"),
        DFA.unpack(u"\1\1\1\uffff\1\3\10\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\5\2\uffff\1\5\3\uffff\2\5\1\uffff\2\5\3\uffff\2"
        u"\5\1\uffff\2\5\2\uffff\1\5\1\uffff\1\6\6\uffff\13\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #39

    class DFA39(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet184 = frozenset([20, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_imports_in_styleSheet195 = frozenset([20, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_bodylist_in_styleSheet206 = frozenset([])
    FOLLOW_EOF_in_styleSheet216 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet269 = frozenset([18])
    FOLLOW_STRING_in_charSet272 = frozenset([19])
    FOLLOW_SEMI_in_charSet274 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports298 = frozenset([18, 21])
    FOLLOW_importUrl_in_imports301 = frozenset([19, 26, 27])
    FOLLOW_media_query_list_in_imports303 = frozenset([19])
    FOLLOW_SEMI_in_imports306 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_bodyset_in_bodylist353 = frozenset([1, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_ruleSet_in_bodyset371 = frozenset([1])
    FOLLOW_media_in_bodyset379 = frozenset([1])
    FOLLOW_page_in_bodyset387 = frozenset([1])
    FOLLOW_fontface_in_bodyset395 = frozenset([1])
    FOLLOW_keyframes_in_bodyset403 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media428 = frozenset([23, 26, 27])
    FOLLOW_media_query_list_in_media431 = frozenset([23])
    FOLLOW_LBRACE_in_media442 = frozenset([24, 26, 28, 36, 37, 38, 39])
    FOLLOW_ruleSet_in_media457 = frozenset([24, 26, 28, 36, 37, 38, 39])
    FOLLOW_RBRACE_in_media468 = frozenset([1])
    FOLLOW_media_query_in_media_query_list489 = frozenset([1, 25])
    FOLLOW_COMMA_in_media_query_list492 = frozenset([26, 27])
    FOLLOW_media_query_in_media_query_list494 = frozenset([1, 25])
    FOLLOW_IDENT_in_media_query532 = frozenset([26])
    FOLLOW_media_type_in_media_query537 = frozenset([1, 26])
    FOLLOW_IDENT_in_media_query541 = frozenset([26, 27])
    FOLLOW_media_expr_in_media_query544 = frozenset([1, 26])
    FOLLOW_media_expr_in_media_query555 = frozenset([1, 26])
    FOLLOW_IDENT_in_media_query559 = frozenset([26, 27])
    FOLLOW_media_expr_in_media_query562 = frozenset([1, 26])
    FOLLOW_IDENT_in_media_type582 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr599 = frozenset([26])
    FOLLOW_media_feature_in_media_expr601 = frozenset([28, 29])
    FOLLOW_COLON_in_media_expr605 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_expr_in_media_expr607 = frozenset([28, 29])
    FOLLOW_COLON_in_media_expr612 = frozenset([29])
    FOLLOW_RPAREN_in_media_expr615 = frozenset([1])
    FOLLOW_IDENT_in_media_feature652 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface672 = frozenset([23])
    FOLLOW_LBRACE_in_fontface675 = frozenset([26, 39])
    FOLLOW_declarationset_in_fontface678 = frozenset([24])
    FOLLOW_RBRACE_in_fontface680 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page701 = frozenset([23, 28])
    FOLLOW_pseudoPage_in_page704 = frozenset([23])
    FOLLOW_LBRACE_in_page707 = frozenset([26, 39])
    FOLLOW_declarationset_in_page710 = frozenset([24])
    FOLLOW_RBRACE_in_page712 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage730 = frozenset([26])
    FOLLOW_IDENT_in_pseudoPage734 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes778 = frozenset([26])
    FOLLOW_IDENT_in_keyframes781 = frozenset([23])
    FOLLOW_LBRACE_in_keyframes783 = frozenset([24, 26, 33])
    FOLLOW_keyframes_block_in_keyframes786 = frozenset([24, 26, 33])
    FOLLOW_RBRACE_in_keyframes789 = frozenset([1])
    FOLLOW_keyframe_selector_in_keyframes_block807 = frozenset([23, 25])
    FOLLOW_COMMA_in_keyframes_block811 = frozenset([26, 33])
    FOLLOW_keyframe_selector_in_keyframes_block813 = frozenset([23, 25])
    FOLLOW_LBRACE_in_keyframes_block818 = frozenset([26, 39])
    FOLLOW_declarationset_in_keyframes_block820 = frozenset([24])
    FOLLOW_RBRACE_in_keyframes_block822 = frozenset([1])
    FOLLOW_set_in_keyframe_selector864 = frozenset([1])
    FOLLOW_selector_in_ruleSet893 = frozenset([23, 25])
    FOLLOW_COMMA_in_ruleSet896 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_selector_in_ruleSet898 = frozenset([23, 25])
    FOLLOW_LBRACE_in_ruleSet902 = frozenset([26, 39])
    FOLLOW_declarationset_in_ruleSet904 = frozenset([24])
    FOLLOW_RBRACE_in_ruleSet906 = frozenset([1])
    FOLLOW_simpleSelector_in_selector946 = frozenset([1, 26, 28, 34, 35, 36, 37, 38, 39])
    FOLLOW_combinator_in_selector949 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_simpleSelector_in_selector951 = frozenset([1, 26, 28, 34, 35, 36, 37, 38, 39])
    FOLLOW_PLUS_in_combinator970 = frozenset([1])
    FOLLOW_GREATER_in_combinator978 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector1001 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector1008 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector1023 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent1096 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent1104 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent1112 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent1120 = frozenset([1])
    FOLLOW_DOT_in_cssClass1137 = frozenset([26])
    FOLLOW_IDENT_in_cssClass1141 = frozenset([1])
    FOLLOW_COLON_in_pseudo1183 = frozenset([26, 28])
    FOLLOW_COLON_in_pseudo1187 = frozenset([26])
    FOLLOW_IDENT_in_pseudo1190 = frozenset([1])
    FOLLOW_COLON_in_pseudo1228 = frozenset([28, 40])
    FOLLOW_COLON_in_pseudo1232 = frozenset([40])
    FOLLOW_FUNCTION_in_pseudo1235 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_expr_in_pseudo1237 = frozenset([29])
    FOLLOW_RPAREN_in_pseudo1239 = frozenset([1])
    FOLLOW_COLON_in_pseudo1281 = frozenset([28, 40])
    FOLLOW_COLON_in_pseudo1285 = frozenset([40])
    FOLLOW_FUNCTION_in_pseudo1288 = frozenset([38])
    FOLLOW_LBRACKET_in_pseudo1290 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_expr_in_pseudo1292 = frozenset([41])
    FOLLOW_RBRACKET_in_pseudo1294 = frozenset([29])
    FOLLOW_RPAREN_in_pseudo1296 = frozenset([1])
    FOLLOW_COLON_in_pseudo1342 = frozenset([28, 40])
    FOLLOW_COLON_in_pseudo1346 = frozenset([40])
    FOLLOW_FUNCTION_in_pseudo1349 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_pseudo_in_pseudo1351 = frozenset([29])
    FOLLOW_RPAREN_in_pseudo1353 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1402 = frozenset([26])
    FOLLOW_attribBody_in_attrib1404 = frozenset([41])
    FOLLOW_RBRACKET_in_attrib1406 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1441 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1449 = frozenset([42, 43, 44, 45, 46, 47])
    FOLLOW_set_in_attribBody1460 = frozenset([18, 26])
    FOLLOW_set_in_attribBody1546 = frozenset([1])
    FOLLOW_declaration_in_declarationset1590 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1593 = frozenset([26, 39])
    FOLLOW_declaration_in_declarationset1595 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1599 = frozenset([1])
    FOLLOW_property_in_declaration1631 = frozenset([28])
    FOLLOW_COLON_in_declaration1633 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_expr_in_declaration1635 = frozenset([1, 48])
    FOLLOW_prio_in_declaration1637 = frozenset([1])
    FOLLOW_IDENT_in_property1676 = frozenset([1])
    FOLLOW_STAR_in_property1695 = frozenset([26])
    FOLLOW_IDENT_in_property1699 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1739 = frozenset([1])
    FOLLOW_term_in_expr1756 = frozenset([1, 18, 21, 25, 26, 33, 34, 36, 40, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_operator_in_expr1759 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_term_in_expr1762 = frozenset([1, 18, 21, 25, 26, 33, 34, 36, 40, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_SOLIDUS_in_operator1783 = frozenset([1])
    FOLLOW_COMMA_in_operator1791 = frozenset([1])
    FOLLOW_unaryOperator_in_term1819 = frozenset([33, 50, 51, 52, 53, 54, 55, 56, 57, 58])
    FOLLOW_set_in_term1831 = frozenset([1])
    FOLLOW_STRING_in_term2009 = frozenset([1])
    FOLLOW_IDENT_in_term2017 = frozenset([1])
    FOLLOW_URI_in_term2025 = frozenset([1])
    FOLLOW_function_in_term2033 = frozenset([1])
    FOLLOW_hexColor_in_term2041 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function2086 = frozenset([26])
    FOLLOW_fnct_args_in_function2088 = frozenset([29])
    FOLLOW_RPAREN_in_function2090 = frozenset([1])
    FOLLOW_fnct_name_in_function2117 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_expr_in_function2119 = frozenset([29])
    FOLLOW_RPAREN_in_function2121 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name2158 = frozenset([28, 37])
    FOLLOW_set_in_fnct_name2160 = frozenset([26, 28, 37, 40])
    FOLLOW_FUNCTION_in_fnct_name2170 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args2190 = frozenset([1, 25])
    FOLLOW_COMMA_in_fnct_args2193 = frozenset([26])
    FOLLOW_fnct_arg_in_fnct_args2195 = frozenset([1, 25])
    FOLLOW_IDENT_in_fnct_arg2227 = frozenset([42])
    FOLLOW_OPEQ_in_fnct_arg2229 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_expr_in_fnct_arg2232 = frozenset([1])
    FOLLOW_HASH_in_hexColor2249 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss1005 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss1020 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
