# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-20 23:20:36

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

        self.dfa35 = self.DFA35(
            self, 35,
            eot = self.DFA35_eot,
            eof = self.DFA35_eof,
            min = self.DFA35_min,
            max = self.DFA35_max,
            accept = self.DFA35_accept,
            special = self.DFA35_special,
            transition = self.DFA35_transition
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
    # lesscss.g:64:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) ;
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
                # lesscss.g:65:2: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) )
                # lesscss.g:65:4: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:65:4: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:65:4: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet130)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:66:4: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:66:4: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet136)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet142)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet147) 
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
                    # 69:3: -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    # lesscss.g:69:6: ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:69:21: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:69:30: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:69:39: ( bodylist )?
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
    # lesscss.g:75:1: charSet : CHARSET_SYM STRING SEMI ;
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
                # lesscss.g:76:2: ( CHARSET_SYM STRING SEMI )
                # lesscss.g:76:4: CHARSET_SYM STRING SEMI
                pass 
                root_0 = self._adaptor.nil()

                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet179)
                if self._state.backtracking == 0:

                    CHARSET_SYM5_tree = self._adaptor.createWithPayload(CHARSET_SYM5)
                    root_0 = self._adaptor.becomeRoot(CHARSET_SYM5_tree, root_0)

                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet182)
                if self._state.backtracking == 0:

                    STRING6_tree = self._adaptor.createWithPayload(STRING6)
                    self._adaptor.addChild(root_0, STRING6_tree)

                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet184)



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
    # lesscss.g:82:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI ;
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
                # lesscss.g:83:2: ( IMPORT_SYM importUrl ( media_query_list )? SEMI )
                # lesscss.g:83:4: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports200)
                if self._state.backtracking == 0:

                    IMPORT_SYM8_tree = self._adaptor.createWithPayload(IMPORT_SYM8)
                    root_0 = self._adaptor.becomeRoot(IMPORT_SYM8_tree, root_0)

                self._state.following.append(self.FOLLOW_importUrl_in_imports203)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, importUrl9.tree)
                # lesscss.g:83:26: ( media_query_list )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((IDENT <= LA3_0 <= LPAREN)) :
                    alt3 = 1
                if alt3 == 1:
                    # lesscss.g:83:26: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports205)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports208)



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
    # lesscss.g:86:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:87:2: ( STRING | URI )
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
    # lesscss.g:95:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset13 = None



        try:
            try:
                # lesscss.g:96:2: ( ( bodyset )* )
                # lesscss.g:96:4: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:96:4: ( bodyset )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == MEDIA_SYM or LA4_0 == IDENT or LA4_0 == COLON or (FONTFACE_SYM <= LA4_0 <= KEYFRAMES_SYM) or (HASH <= LA4_0 <= STAR)) :
                        alt4 = 1


                    if alt4 == 1:
                        # lesscss.g:96:4: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist240)
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
    # lesscss.g:99:1: bodyset : ( ruleSet | media | page | fontface | keyframes );
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
                # lesscss.g:100:2: ( ruleSet | media | page | fontface | keyframes )
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
                    # lesscss.g:100:4: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset252)
                    ruleSet14 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet14.tree)


                elif alt5 == 2:
                    # lesscss.g:101:4: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset257)
                    media15 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media15.tree)


                elif alt5 == 3:
                    # lesscss.g:102:4: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset262)
                    page16 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page16.tree)


                elif alt5 == 4:
                    # lesscss.g:103:4: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset267)
                    fontface17 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface17.tree)


                elif alt5 == 5:
                    # lesscss.g:104:4: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_bodyset272)
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
    # lesscss.g:112:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( bodyset )* RBRACE ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM19 = None
        LBRACE21 = None
        RBRACE23 = None
        media_query_list20 = None

        bodyset22 = None


        MEDIA_SYM19_tree = None
        LBRACE21_tree = None
        RBRACE23_tree = None

        try:
            try:
                # lesscss.g:113:2: ( MEDIA_SYM ( media_query_list )? LBRACE ( bodyset )* RBRACE )
                # lesscss.g:113:4: MEDIA_SYM ( media_query_list )? LBRACE ( bodyset )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                MEDIA_SYM19=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media291)
                if self._state.backtracking == 0:

                    MEDIA_SYM19_tree = self._adaptor.createWithPayload(MEDIA_SYM19)
                    root_0 = self._adaptor.becomeRoot(MEDIA_SYM19_tree, root_0)

                # lesscss.g:113:15: ( media_query_list )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((IDENT <= LA6_0 <= LPAREN)) :
                    alt6 = 1
                if alt6 == 1:
                    # lesscss.g:113:15: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media294)
                    media_query_list20 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_query_list20.tree)



                LBRACE21=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media299)
                # lesscss.g:115:4: ( bodyset )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == MEDIA_SYM or LA7_0 == IDENT or LA7_0 == COLON or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM) or (HASH <= LA7_0 <= STAR)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:115:4: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_media305)
                        bodyset22 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset22.tree)


                    else:
                        break #loop7
                RBRACE23=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media314)



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
    # lesscss.g:122:1: media_query_list : media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) ;
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
                # lesscss.g:123:2: ( media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) )
                # lesscss.g:123:4: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list329)
                media_query24 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query24.tree)
                # lesscss.g:123:16: ( COMMA media_query )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # lesscss.g:123:17: COMMA media_query
                        pass 
                        COMMA25=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list332) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA25)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list334)
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
                    # 124:3: -> ^( N_MediaQuery ( media_query )+ )
                    # lesscss.g:124:6: ^( N_MediaQuery ( media_query )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaQuery, "N_MediaQuery"), root_1)

                    # lesscss.g:124:21: ( media_query )+
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
    # lesscss.g:129:1: media_query : ( media_stmt | media_expr )+ ;
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        media_stmt27 = None

        media_expr28 = None



        try:
            try:
                # lesscss.g:130:2: ( ( media_stmt | media_expr )+ )
                # lesscss.g:130:4: ( media_stmt | media_expr )+
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:130:4: ( media_stmt | media_expr )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 3
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENT) :
                        alt9 = 1
                    elif (LA9_0 == LPAREN) :
                        alt9 = 2


                    if alt9 == 1:
                        # lesscss.g:130:6: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query362)
                        media_stmt27 = self.media_stmt()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_stmt27.tree)


                    elif alt9 == 2:
                        # lesscss.g:130:19: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query366)
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
    # lesscss.g:133:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT29 = None

        IDENT29_tree = None

        try:
            try:
                # lesscss.g:134:2: ( IDENT )
                # lesscss.g:134:4: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT29=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt380)
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
    # lesscss.g:137:1: media_expr : LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) ;
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
                # lesscss.g:138:2: ( LPAREN media_stmt ( COLON expr )? RPAREN -> ^( N_MediaExpr media_stmt ( expr )? ) )
                # lesscss.g:138:4: LPAREN media_stmt ( COLON expr )? RPAREN
                pass 
                LPAREN30=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr391) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN30)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr393)
                media_stmt31 = self.media_stmt()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_stmt.add(media_stmt31.tree)
                # lesscss.g:138:22: ( COLON expr )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == COLON) :
                    alt10 = 1
                if alt10 == 1:
                    # lesscss.g:138:24: COLON expr
                    pass 
                    COLON32=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr397) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON32)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr399)
                    expr33 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr33.tree)



                RPAREN34=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr404) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN34)

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
                    # 139:3: -> ^( N_MediaExpr media_stmt ( expr )? )
                    # lesscss.g:139:6: ^( N_MediaExpr media_stmt ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_stmt.nextTree())
                    # lesscss.g:139:31: ( expr )?
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
    # lesscss.g:146:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE ;
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
                # lesscss.g:147:2: ( FONTFACE_SYM LBRACE declarationset RBRACE )
                # lesscss.g:147:4: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                FONTFACE_SYM35=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface433)
                if self._state.backtracking == 0:

                    FONTFACE_SYM35_tree = self._adaptor.createWithPayload(FONTFACE_SYM35)
                    root_0 = self._adaptor.becomeRoot(FONTFACE_SYM35_tree, root_0)

                LBRACE36=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface436)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface439)
                declarationset37 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset37.tree)
                RBRACE38=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface441)



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
    # lesscss.g:153:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE ;
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
                # lesscss.g:154:2: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE )
                # lesscss.g:154:4: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                PAGE_SYM39=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page456)
                if self._state.backtracking == 0:

                    PAGE_SYM39_tree = self._adaptor.createWithPayload(PAGE_SYM39)
                    root_0 = self._adaptor.becomeRoot(PAGE_SYM39_tree, root_0)

                # lesscss.g:154:14: ( pseudoPage )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    alt11 = 1
                if alt11 == 1:
                    # lesscss.g:154:14: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page459)
                    pseudoPage40 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudoPage40.tree)



                LBRACE41=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page462)
                self._state.following.append(self.FOLLOW_declarationset_in_page465)
                declarationset42 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset42.tree)
                RBRACE43=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page467)



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
    # lesscss.g:157:1: pseudoPage : COLON a= IDENT -> IDENT ;
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
                # lesscss.g:158:2: ( COLON a= IDENT -> IDENT )
                # lesscss.g:158:4: COLON a= IDENT
                pass 
                COLON44=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage479) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON44)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage483) 
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
                    # 160:3: -> IDENT
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
    # lesscss.g:167:1: keyframes : KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE ;
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
                # lesscss.g:168:2: ( KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE )
                # lesscss.g:168:4: KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                KEYFRAMES_SYM45=self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes509)
                if self._state.backtracking == 0:

                    KEYFRAMES_SYM45_tree = self._adaptor.createWithPayload(KEYFRAMES_SYM45)
                    root_0 = self._adaptor.becomeRoot(KEYFRAMES_SYM45_tree, root_0)

                IDENT46=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes512)
                if self._state.backtracking == 0:

                    IDENT46_tree = self._adaptor.createWithPayload(IDENT46)
                    self._adaptor.addChild(root_0, IDENT46_tree)

                LBRACE47=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes514)
                # lesscss.g:168:33: ( keyframes_block )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == IDENT or LA12_0 == PERCENTAGE) :
                        alt12 = 1


                    if alt12 == 1:
                        # lesscss.g:168:33: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes517)
                        keyframes_block48 = self.keyframes_block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, keyframes_block48.tree)


                    else:
                        break #loop12
                RBRACE49=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes520)



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
    # lesscss.g:171:1: keyframes_block : keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) ;
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
                # lesscss.g:172:2: ( keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset ) )
                # lesscss.g:172:4: keyframe_selector ( COMMA keyframe_selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block532)
                keyframe_selector50 = self.keyframe_selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_keyframe_selector.add(keyframe_selector50.tree)
                # lesscss.g:172:22: ( COMMA keyframe_selector )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == COMMA) :
                        alt13 = 1


                    if alt13 == 1:
                        # lesscss.g:172:24: COMMA keyframe_selector
                        pass 
                        COMMA51=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keyframes_block536) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA51)
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block538)
                        keyframe_selector52 = self.keyframe_selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_keyframe_selector.add(keyframe_selector52.tree)


                    else:
                        break #loop13
                LBRACE53=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes_block543) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE53)
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block545)
                declarationset54 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset54.tree)
                RBRACE55=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes_block547) 
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
                    # 173:3: -> ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    # lesscss.g:173:6: ^( N_KeyframeBlock ( ^( M_KeyframeSelector keyframe_selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_KeyframeBlock, "N_KeyframeBlock"), root_1)

                    # lesscss.g:173:24: ( ^( M_KeyframeSelector keyframe_selector ) )+
                    if not (stream_keyframe_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_keyframe_selector.hasNext():
                        # lesscss.g:173:24: ^( M_KeyframeSelector keyframe_selector )
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
    # lesscss.g:177:1: keyframe_selector : ( IDENT | PERCENTAGE ) ;
    def keyframe_selector(self, ):

        retval = self.keyframe_selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set56 = None

        set56_tree = None

        try:
            try:
                # lesscss.g:178:2: ( ( IDENT | PERCENTAGE ) )
                # lesscss.g:178:4: ( IDENT | PERCENTAGE )
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

    class ruleSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.ruleSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleSet"
    # lesscss.g:185:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA58 = None
        LBRACE60 = None
        RBRACE62 = None
        selector57 = None

        selector59 = None

        declarationset61 = None


        COMMA58_tree = None
        LBRACE60_tree = None
        RBRACE62_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:186:2: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:186:4: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet600)
                selector57 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector57.tree)
                # lesscss.g:186:13: ( COMMA selector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1


                    if alt14 == 1:
                        # lesscss.g:186:14: COMMA selector
                        pass 
                        COMMA58=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet603) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA58)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet605)
                        selector59 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector59.tree)


                    else:
                        break #loop14
                LBRACE60=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet609) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE60)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet611)
                declarationset61 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset61.tree)
                RBRACE62=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet613) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE62)

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
                    # 187:3: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:187:6: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:187:18: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:187:18: ^( N_Selector selector )
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
    # lesscss.g:190:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector63 = None

        combinator64 = None

        simpleSelector65 = None



        try:
            try:
                # lesscss.g:191:2: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:191:4: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector641)
                simpleSelector63 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector63.tree)
                # lesscss.g:191:19: ( combinator simpleSelector )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == IDENT or LA15_0 == COLON or (PLUS <= LA15_0 <= STAR)) :
                        alt15 = 1


                    if alt15 == 1:
                        # lesscss.g:191:20: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector644)
                        combinator64 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator64.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector646)
                        simpleSelector65 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector65.tree)


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
    # lesscss.g:194:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS66 = None
        GREATER67 = None

        PLUS66_tree = None
        GREATER67_tree = None

        try:
            try:
                # lesscss.g:195:2: ( PLUS | GREATER | )
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
                    # lesscss.g:195:4: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS66=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator659)
                    if self._state.backtracking == 0:

                        PLUS66_tree = self._adaptor.createWithPayload(PLUS66)
                        self._adaptor.addChild(root_0, PLUS66_tree)



                elif alt16 == 2:
                    # lesscss.g:196:4: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER67=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator664)
                    if self._state.backtracking == 0:

                        GREATER67_tree = self._adaptor.createWithPayload(GREATER67)
                        self._adaptor.addChild(root_0, GREATER67_tree)



                elif alt16 == 3:
                    # lesscss.g:198:2: 
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
    # lesscss.g:200:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName68 = None

        elementSubsequent69 = None

        elementSubsequent70 = None



        try:
            try:
                # lesscss.g:201:2: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
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
                    # lesscss.g:201:4: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector678)
                    elementName68 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName68.tree)
                    # lesscss.g:201:16: ( ( esPred )=> elementSubsequent )*
                    while True: #loop17
                        alt17 = 2
                        alt17 = self.dfa17.predict(self.input)
                        if alt17 == 1:
                            # lesscss.g:201:17: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector685)
                            elementSubsequent69 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent69.tree)


                        else:
                            break #loop17


                elif alt19 == 2:
                    # lesscss.g:202:4: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:202:4: ( ( esPred )=> elementSubsequent )+
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
                            # lesscss.g:202:5: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector697)
                            elementSubsequent70 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent70.tree)


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
    # lesscss.g:205:1: esPred : ( HASH | DOT | COLON | LBRACKET );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set71 = None

        set71_tree = None

        try:
            try:
                # lesscss.g:206:2: ( HASH | DOT | COLON | LBRACKET )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set71 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
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

        set72 = None

        set72_tree = None

        try:
            try:
                # lesscss.g:213:2: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set72 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set72))
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
    # lesscss.g:217:1: elementSubsequent : ( HASH | cssClass | pseudo | attrib );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH73 = None
        cssClass74 = None

        pseudo75 = None

        attrib76 = None


        HASH73_tree = None

        try:
            try:
                # lesscss.g:218:2: ( HASH | cssClass | pseudo | attrib )
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
                    # lesscss.g:218:4: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH73=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent759)
                    if self._state.backtracking == 0:

                        HASH73_tree = self._adaptor.createWithPayload(HASH73)
                        self._adaptor.addChild(root_0, HASH73_tree)



                elif alt20 == 2:
                    # lesscss.g:219:4: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent764)
                    cssClass74 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass74.tree)


                elif alt20 == 3:
                    # lesscss.g:220:4: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent769)
                    pseudo75 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo75.tree)


                elif alt20 == 4:
                    # lesscss.g:221:4: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent774)
                    attrib76 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib76.tree)


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
        DOT77 = None

        a_tree = None
        DOT77_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:225:2: ( DOT a= IDENT -> IDENT )
                # lesscss.g:225:4: DOT a= IDENT
                pass 
                DOT77=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass785) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT77)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass789) 
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
                    # 227:3: -> IDENT
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
    # lesscss.g:230:1: pseudo : a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) ;
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        b = None
        IDENT78 = None
        pseudoFunction79 = None


        a_tree = None
        b_tree = None
        IDENT78_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_pseudoFunction = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoFunction")
        try:
            try:
                # lesscss.g:231:2: (a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) ) )
                # lesscss.g:231:4: a= COLON (b= COLON )? ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
                pass 
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo813) 
                if self._state.backtracking == 0:
                    stream_COLON.add(a)
                # lesscss.g:231:13: (b= COLON )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == COLON) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:231:13: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo817) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(b)



                # lesscss.g:232:2: ( IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | pseudoFunction -> ^( N_Pseudo $a ( $b)? pseudoFunction ) )
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
                    # lesscss.g:232:4: IDENT
                    pass 
                    IDENT78=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo823) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT78)

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
                        # 233:3: -> ^( N_Pseudo $a ( $b)? IDENT )
                        # lesscss.g:233:6: ^( N_Pseudo $a ( $b)? IDENT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:233:20: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 2:
                    # lesscss.g:234:4: pseudoFunction
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoFunction_in_pseudo845)
                    pseudoFunction79 = self.pseudoFunction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoFunction.add(pseudoFunction79.tree)

                    # AST Rewrite
                    # elements: b, a, pseudoFunction
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
                        # 235:3: -> ^( N_Pseudo $a ( $b)? pseudoFunction )
                        # lesscss.g:235:6: ^( N_Pseudo $a ( $b)? pseudoFunction )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:235:20: ( $b)?
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
    # lesscss.g:239:1: pseudoFunction : ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) );
    def pseudoFunction(self, ):

        retval = self.pseudoFunction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FUNCTION80 = None
        RPAREN82 = None
        FUNCTION83 = None
        LBRACKET84 = None
        RBRACKET86 = None
        RPAREN87 = None
        FUNCTION88 = None
        RPAREN90 = None
        expr81 = None

        attribBody85 = None

        pseudo89 = None


        FUNCTION80_tree = None
        RPAREN82_tree = None
        FUNCTION83_tree = None
        LBRACKET84_tree = None
        RBRACKET86_tree = None
        RPAREN87_tree = None
        FUNCTION88_tree = None
        RPAREN90_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        stream_pseudo = RewriteRuleSubtreeStream(self._adaptor, "rule pseudo")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:240:2: ( FUNCTION expr RPAREN -> ^( N_PseudoFunction FUNCTION expr ) | FUNCTION LBRACKET attribBody RBRACKET RPAREN -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET ) | FUNCTION pseudo RPAREN -> ^( N_PseudoFunction FUNCTION pseudo ) )
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
                    # lesscss.g:240:4: FUNCTION expr RPAREN
                    pass 
                    FUNCTION80=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction876) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION80)
                    self._state.following.append(self.FOLLOW_expr_in_pseudoFunction878)
                    expr81 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr81.tree)
                    RPAREN82=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction880) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN82)

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
                        # 241:3: -> ^( N_PseudoFunction FUNCTION expr )
                        # lesscss.g:241:6: ^( N_PseudoFunction FUNCTION expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 2:
                    # lesscss.g:243:4: FUNCTION LBRACKET attribBody RBRACKET RPAREN
                    pass 
                    FUNCTION83=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction899) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION83)
                    LBRACKET84=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudoFunction901) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET84)
                    self._state.following.append(self.FOLLOW_attribBody_in_pseudoFunction903)
                    attribBody85 = self.attribBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_attribBody.add(attribBody85.tree)
                    RBRACKET86=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudoFunction905) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET86)
                    RPAREN87=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction907) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN87)

                    # AST Rewrite
                    # elements: RBRACKET, FUNCTION, attribBody, LBRACKET
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
                        # 244:3: -> ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        # lesscss.g:244:6: ^( N_PseudoFunction FUNCTION LBRACKET attribBody RBRACKET )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_PseudoFunction, "N_PseudoFunction"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_LBRACKET.nextNode())
                        self._adaptor.addChild(root_1, stream_attribBody.nextTree())
                        self._adaptor.addChild(root_1, stream_RBRACKET.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 3:
                    # lesscss.g:246:4: FUNCTION pseudo RPAREN
                    pass 
                    FUNCTION88=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudoFunction930) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION88)
                    self._state.following.append(self.FOLLOW_pseudo_in_pseudoFunction932)
                    pseudo89 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudo.add(pseudo89.tree)
                    RPAREN90=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudoFunction934) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN90)

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
                        # 247:3: -> ^( N_PseudoFunction FUNCTION pseudo )
                        # lesscss.g:247:6: ^( N_PseudoFunction FUNCTION pseudo )
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
    # lesscss.g:251:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET91 = None
        RBRACKET93 = None
        attribBody92 = None


        LBRACKET91_tree = None
        RBRACKET93_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:252:2: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:252:4: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET91=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib959) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET91)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib961)
                attribBody92 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody92.tree)
                RBRACKET93=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib963) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET93)

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
                    # 253:3: -> ^( N_Attrib attribBody )
                    # lesscss.g:253:7: ^( N_Attrib attribBody )
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
    # lesscss.g:256:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT94 = None
        IDENT95 = None
        set96 = None
        term97 = None


        IDENT94_tree = None
        IDENT95_tree = None
        set96_tree = None

        try:
            try:
                # lesscss.g:257:2: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term )
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
                    # lesscss.g:257:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT94=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody986)
                    if self._state.backtracking == 0:

                        IDENT94_tree = self._adaptor.createWithPayload(IDENT94)
                        self._adaptor.addChild(root_0, IDENT94_tree)



                elif alt24 == 2:
                    # lesscss.g:258:4: IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) term
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT95=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody991)
                    if self._state.backtracking == 0:

                        IDENT95_tree = self._adaptor.createWithPayload(IDENT95)
                        self._adaptor.addChild(root_0, IDENT95_tree)

                    set96 = self.input.LT(1)
                    set96 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= SUBSTRINGMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set96), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_term_in_attribBody1040)
                    term97 = self.term()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, term97.tree)


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
    # lesscss.g:269:1: declarationset : ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ | -> N_Empty );
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI99 = None
        SEMI101 = None
        declaration98 = None

        declaration100 = None


        SEMI99_tree = None
        SEMI101_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:270:2: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ | -> N_Empty )
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
                    # lesscss.g:270:4: declaration ( SEMI declaration )* ( SEMI )?
                    pass 
                    self._state.following.append(self.FOLLOW_declaration_in_declarationset1051)
                    declaration98 = self.declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_declaration.add(declaration98.tree)
                    # lesscss.g:270:16: ( SEMI declaration )*
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == SEMI) :
                            LA25_1 = self.input.LA(2)

                            if (LA25_1 == IDENT or LA25_1 == STAR) :
                                alt25 = 1




                        if alt25 == 1:
                            # lesscss.g:270:17: SEMI declaration
                            pass 
                            SEMI99=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1054) 
                            if self._state.backtracking == 0:
                                stream_SEMI.add(SEMI99)
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset1056)
                            declaration100 = self.declaration()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_declaration.add(declaration100.tree)


                        else:
                            break #loop25
                    # lesscss.g:270:36: ( SEMI )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == SEMI) :
                        alt26 = 1
                    if alt26 == 1:
                        # lesscss.g:270:36: SEMI
                        pass 
                        SEMI101=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1060) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI101)




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
                        # 271:4: -> ( declaration )+
                        # lesscss.g:271:7: ( declaration )+
                        if not (stream_declaration.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_declaration.hasNext():
                            self._adaptor.addChild(root_0, stream_declaration.nextTree())


                        stream_declaration.reset()



                        retval.tree = root_0


                elif alt27 == 2:
                    # lesscss.g:274:3: 
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
                        # 274:3: -> N_Empty
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
    # lesscss.g:278:1: declaration : ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) );
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON103 = None
        COLON107 = None
        property102 = None

        expr104 = None

        prio105 = None

        property106 = None


        COLON103_tree = None
        COLON107_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:279:2: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) | property COLON -> ^( N_Declaration property ) )
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
                    # lesscss.g:279:4: property COLON expr ( prio )?
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1091)
                    property102 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property102.tree)
                    COLON103=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1093) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON103)
                    self._state.following.append(self.FOLLOW_expr_in_declaration1095)
                    expr104 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr104.tree)
                    # lesscss.g:279:24: ( prio )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == IMPORTANT_SYM) :
                        alt28 = 1
                    if alt28 == 1:
                        # lesscss.g:279:24: prio
                        pass 
                        self._state.following.append(self.FOLLOW_prio_in_declaration1097)
                        prio105 = self.prio()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_prio.add(prio105.tree)




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
                        # 280:3: -> ^( N_Declaration property expr ( prio )? )
                        # lesscss.g:280:6: ^( N_Declaration property expr ( prio )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                        self._adaptor.addChild(root_1, stream_property.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())
                        # lesscss.g:280:36: ( prio )?
                        if stream_prio.hasNext():
                            self._adaptor.addChild(root_1, stream_prio.nextTree())


                        stream_prio.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 2:
                    # lesscss.g:282:5: property COLON
                    pass 
                    self._state.following.append(self.FOLLOW_property_in_declaration1120)
                    property106 = self.property()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property.add(property106.tree)
                    COLON107=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1122) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON107)

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
                        # 283:3: -> ^( N_Declaration property )
                        # lesscss.g:283:6: ^( N_Declaration property )
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
    # lesscss.g:287:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT108 = None
        STAR109 = None

        a_tree = None
        IDENT108_tree = None
        STAR109_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:288:2: ( IDENT | STAR a= IDENT -> IDENT )
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
                    # lesscss.g:288:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT108=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1147)
                    if self._state.backtracking == 0:

                        IDENT108_tree = self._adaptor.createWithPayload(IDENT108)
                        self._adaptor.addChild(root_0, IDENT108_tree)



                elif alt30 == 2:
                    # lesscss.g:292:4: STAR a= IDENT
                    pass 
                    STAR109=self.match(self.input, STAR, self.FOLLOW_STAR_in_property1157) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR109)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1161) 
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
                        # 294:3: -> IDENT
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
    # lesscss.g:297:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM110 = None

        IMPORTANT_SYM110_tree = None

        try:
            try:
                # lesscss.g:298:2: ( IMPORTANT_SYM )
                # lesscss.g:298:4: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM110=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1183)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM110_tree = self._adaptor.createWithPayload(IMPORTANT_SYM110)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM110_tree)




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
    # lesscss.g:301:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term111 = None

        operator112 = None

        term113 = None



        try:
            try:
                # lesscss.g:302:2: ( term ( operator term )* )
                # lesscss.g:302:4: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1194)
                term111 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term111.tree)
                # lesscss.g:302:9: ( operator term )*
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
                        # lesscss.g:302:10: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1197)
                        operator112 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator112.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1200)
                        term113 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term113.tree)


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
    # lesscss.g:305:10: fragment operator : ( SOLIDUS | COMMA | -> N_Empty );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS114 = None
        COMMA115 = None

        SOLIDUS114_tree = None
        COMMA115_tree = None

        try:
            try:
                # lesscss.g:306:2: ( SOLIDUS | COMMA | -> N_Empty )
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
                    # lesscss.g:306:4: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS114=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1215)
                    if self._state.backtracking == 0:

                        SOLIDUS114_tree = self._adaptor.createWithPayload(SOLIDUS114)
                        self._adaptor.addChild(root_0, SOLIDUS114_tree)



                elif alt32 == 2:
                    # lesscss.g:307:4: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA115=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1220)
                    if self._state.backtracking == 0:

                        COMMA115_tree = self._adaptor.createWithPayload(COMMA115)
                        self._adaptor.addChild(root_0, COMMA115_tree)



                elif alt32 == 3:
                    # lesscss.g:308:4: 
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
                        # 308:4: -> N_Empty
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
    # lesscss.g:311:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH ) | STRING | IDENT | URI | function | hexColor | UNICODE_RANGE );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set117 = None
        STRING118 = None
        IDENT119 = None
        URI120 = None
        UNICODE_RANGE123 = None
        unaryOperator116 = None

        function121 = None

        hexColor122 = None


        set117_tree = None
        STRING118_tree = None
        IDENT119_tree = None
        URI120_tree = None
        UNICODE_RANGE123_tree = None

        try:
            try:
                # lesscss.g:312:2: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH ) | STRING | IDENT | URI | function | hexColor | UNICODE_RANGE )
                alt34 = 7
                LA34 = self.input.LA(1)
                if LA34 == PERCENTAGE or LA34 == PLUS or LA34 == NUMBER or LA34 == LENGTH or LA34 == EMS or LA34 == EXS or LA34 == REMS or LA34 == CHS or LA34 == ANGLE or LA34 == TIME or LA34 == FREQ or LA34 == RESOLUTION or LA34 == VPORTLEN or LA34 == NTH or LA34 == MINUS:
                    alt34 = 1
                elif LA34 == STRING:
                    alt34 = 2
                elif LA34 == IDENT:
                    LA34_3 = self.input.LA(2)

                    if ((STRING <= LA34_3 <= SEMI) or LA34_3 == URI or (RBRACE <= LA34_3 <= IDENT) or LA34_3 == RPAREN or (PERCENTAGE <= LA34_3 <= PLUS) or LA34_3 == HASH or (FUNCTION <= LA34_3 <= RBRACKET) or (IMPORTANT_SYM <= LA34_3 <= MINUS)) :
                        alt34 = 3
                    elif (LA34_3 == COLON or LA34_3 == DOT) :
                        alt34 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 34, 3, self.input)

                        raise nvae

                elif LA34 == URI:
                    alt34 = 4
                elif LA34 == FUNCTION:
                    alt34 = 5
                elif LA34 == HASH:
                    alt34 = 6
                elif LA34 == UNICODE_RANGE:
                    alt34 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # lesscss.g:312:4: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:312:17: ( unaryOperator )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == PLUS or LA33_0 == MINUS) :
                        alt33 = 1
                    if alt33 == 1:
                        # lesscss.g:312:17: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1239)
                        unaryOperator116 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator116.tree, root_0)



                    set117 = self.input.LT(1)
                    if self.input.LA(1) == PERCENTAGE or (NUMBER <= self.input.LA(1) <= NTH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set117))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt34 == 2:
                    # lesscss.g:328:4: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING118=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1345)
                    if self._state.backtracking == 0:

                        STRING118_tree = self._adaptor.createWithPayload(STRING118)
                        self._adaptor.addChild(root_0, STRING118_tree)



                elif alt34 == 3:
                    # lesscss.g:329:4: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT119=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1350)
                    if self._state.backtracking == 0:

                        IDENT119_tree = self._adaptor.createWithPayload(IDENT119)
                        self._adaptor.addChild(root_0, IDENT119_tree)



                elif alt34 == 4:
                    # lesscss.g:330:4: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI120=self.match(self.input, URI, self.FOLLOW_URI_in_term1355)
                    if self._state.backtracking == 0:

                        URI120_tree = self._adaptor.createWithPayload(URI120)
                        self._adaptor.addChild(root_0, URI120_tree)



                elif alt34 == 5:
                    # lesscss.g:331:4: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1360)
                    function121 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function121.tree)


                elif alt34 == 6:
                    # lesscss.g:332:4: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1365)
                    hexColor122 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor122.tree)


                elif alt34 == 7:
                    # lesscss.g:333:4: UNICODE_RANGE
                    pass 
                    root_0 = self._adaptor.nil()

                    UNICODE_RANGE123=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term1370)
                    if self._state.backtracking == 0:

                        UNICODE_RANGE123_tree = self._adaptor.createWithPayload(UNICODE_RANGE123)
                        self._adaptor.addChild(root_0, UNICODE_RANGE123_tree)



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
    # lesscss.g:336:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set124 = None

        set124_tree = None

        try:
            try:
                # lesscss.g:337:2: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set124 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set124))
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
    # lesscss.g:342:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN127 = None
        RPAREN130 = None
        fnct_name125 = None

        fnct_args126 = None

        fnct_name128 = None

        expr129 = None


        RPAREN127_tree = None
        RPAREN130_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:343:2: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt35 = 2
                alt35 = self.dfa35.predict(self.input)
                if alt35 == 1:
                    # lesscss.g:343:4: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1400)
                    fnct_name125 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name125.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1402)
                    fnct_args126 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args126.tree)
                    RPAREN127=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1404) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN127)

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
                        # 344:3: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:344:6: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt35 == 2:
                    # lesscss.g:346:4: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1422)
                    fnct_name128 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name128.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1424)
                    expr129 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr129.tree)
                    RPAREN130=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1426) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN130)

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
                        # 347:3: -> ^( N_Function fnct_name expr )
                        # lesscss.g:347:6: ^( N_Function fnct_name expr )
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
    # lesscss.g:351:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT131 = None
        set132 = None
        FUNCTION133 = None

        IDENT131_tree = None
        set132_tree = None
        FUNCTION133_tree = None

        try:
            try:
                # lesscss.g:352:2: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:352:4: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:352:4: ( IDENT ( COLON | DOT )+ )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == IDENT) :
                        alt37 = 1


                    if alt37 == 1:
                        # lesscss.g:352:5: IDENT ( COLON | DOT )+
                        pass 
                        IDENT131=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1451)
                        if self._state.backtracking == 0:

                            IDENT131_tree = self._adaptor.createWithPayload(IDENT131)
                            self._adaptor.addChild(root_0, IDENT131_tree)

                        # lesscss.g:352:11: ( COLON | DOT )+
                        cnt36 = 0
                        while True: #loop36
                            alt36 = 2
                            LA36_0 = self.input.LA(1)

                            if (LA36_0 == COLON or LA36_0 == DOT) :
                                alt36 = 1


                            if alt36 == 1:
                                # lesscss.g:
                                pass 
                                set132 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set132))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt36 >= 1:
                                    break #loop36

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(36, self.input)
                                raise eee

                            cnt36 += 1


                    else:
                        break #loop37
                FUNCTION133=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1463)
                if self._state.backtracking == 0:

                    FUNCTION133_tree = self._adaptor.createWithPayload(FUNCTION133)
                    root_0 = self._adaptor.becomeRoot(FUNCTION133_tree, root_0)




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
    # lesscss.g:355:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA135 = None
        fnct_arg134 = None

        fnct_arg136 = None


        COMMA135_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:356:2: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:356:4: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1477)
                fnct_arg134 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg134.tree)
                # lesscss.g:356:13: ( COMMA fnct_arg )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == COMMA) :
                        alt38 = 1


                    if alt38 == 1:
                        # lesscss.g:356:14: COMMA fnct_arg
                        pass 
                        COMMA135=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1480) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA135)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1482)
                        fnct_arg136 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg136.tree)


                    else:
                        break #loop38

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
                    # 357:3: -> ( fnct_arg )+
                    # lesscss.g:357:6: ( fnct_arg )+
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
    # lesscss.g:360:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT137 = None
        OPEQ138 = None
        expr139 = None


        IDENT137_tree = None
        OPEQ138_tree = None

        try:
            try:
                # lesscss.g:361:2: ( IDENT OPEQ expr )
                # lesscss.g:361:4: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT137=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1502)
                if self._state.backtracking == 0:

                    IDENT137_tree = self._adaptor.createWithPayload(IDENT137)
                    self._adaptor.addChild(root_0, IDENT137_tree)

                OPEQ138=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1504)
                if self._state.backtracking == 0:

                    OPEQ138_tree = self._adaptor.createWithPayload(OPEQ138)
                    root_0 = self._adaptor.becomeRoot(OPEQ138_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1507)
                expr139 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr139.tree)



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
    # lesscss.g:364:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH140 = None

        HASH140_tree = None

        try:
            try:
                # lesscss.g:365:2: ( HASH )
                # lesscss.g:365:4: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH140=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1518)
                if self._state.backtracking == 0:

                    HASH140_tree = self._adaptor.createWithPayload(HASH140)
                    self._adaptor.addChild(root_0, HASH140_tree)




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
        # lesscss.g:201:17: ( esPred )
        # lesscss.g:201:18: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss682)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:202:5: ( esPred )
        # lesscss.g:202:6: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss694)
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
        u"\1\27\3\uffff\4\0\3\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\1\47\3\uffff\4\0\3\uffff"
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
    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\1\32\1\34\1\22\1\32\1\22\2\uffff"
        )

    DFA35_max = DFA.unpack(
        u"\1\50\1\45\1\77\1\50\1\77\2\uffff"
        )

    DFA35_accept = DFA.unpack(
        u"\5\uffff\1\2\1\1"
        )

    DFA35_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA35_transition = [
        DFA.unpack(u"\1\1\15\uffff\1\2"),
        DFA.unpack(u"\1\3\10\uffff\1\3"),
        DFA.unpack(u"\1\5\2\uffff\1\5\4\uffff\1\4\6\uffff\2\5\1\uffff\1"
        u"\5\3\uffff\1\5\11\uffff\16\5"),
        DFA.unpack(u"\1\1\1\uffff\1\3\10\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\5\2\uffff\1\5\3\uffff\2\5\1\uffff\2\5\3\uffff\2"
        u"\5\1\uffff\2\5\2\uffff\1\5\1\uffff\1\6\6\uffff\17\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet130 = frozenset([20, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_imports_in_styleSheet136 = frozenset([20, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_bodylist_in_styleSheet142 = frozenset([])
    FOLLOW_EOF_in_styleSheet147 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet179 = frozenset([18])
    FOLLOW_STRING_in_charSet182 = frozenset([19])
    FOLLOW_SEMI_in_charSet184 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports200 = frozenset([18, 21])
    FOLLOW_importUrl_in_imports203 = frozenset([19, 26, 27])
    FOLLOW_media_query_list_in_imports205 = frozenset([19])
    FOLLOW_SEMI_in_imports208 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_bodyset_in_bodylist240 = frozenset([1, 22, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_ruleSet_in_bodyset252 = frozenset([1])
    FOLLOW_media_in_bodyset257 = frozenset([1])
    FOLLOW_page_in_bodyset262 = frozenset([1])
    FOLLOW_fontface_in_bodyset267 = frozenset([1])
    FOLLOW_keyframes_in_bodyset272 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media291 = frozenset([23, 26, 27])
    FOLLOW_media_query_list_in_media294 = frozenset([23])
    FOLLOW_LBRACE_in_media299 = frozenset([22, 24, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_bodyset_in_media305 = frozenset([22, 24, 26, 28, 30, 31, 32, 36, 37, 38, 39])
    FOLLOW_RBRACE_in_media314 = frozenset([1])
    FOLLOW_media_query_in_media_query_list329 = frozenset([1, 25])
    FOLLOW_COMMA_in_media_query_list332 = frozenset([26, 27])
    FOLLOW_media_query_in_media_query_list334 = frozenset([1, 25])
    FOLLOW_media_stmt_in_media_query362 = frozenset([1, 26, 27])
    FOLLOW_media_expr_in_media_query366 = frozenset([1, 26, 27])
    FOLLOW_IDENT_in_media_stmt380 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr391 = frozenset([26])
    FOLLOW_media_stmt_in_media_expr393 = frozenset([28, 29])
    FOLLOW_COLON_in_media_expr397 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_media_expr399 = frozenset([29])
    FOLLOW_RPAREN_in_media_expr404 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface433 = frozenset([23])
    FOLLOW_LBRACE_in_fontface436 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_fontface439 = frozenset([24])
    FOLLOW_RBRACE_in_fontface441 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page456 = frozenset([23, 28])
    FOLLOW_pseudoPage_in_page459 = frozenset([23])
    FOLLOW_LBRACE_in_page462 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_page465 = frozenset([24])
    FOLLOW_RBRACE_in_page467 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage479 = frozenset([26])
    FOLLOW_IDENT_in_pseudoPage483 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes509 = frozenset([26])
    FOLLOW_IDENT_in_keyframes512 = frozenset([23])
    FOLLOW_LBRACE_in_keyframes514 = frozenset([24, 26, 33])
    FOLLOW_keyframes_block_in_keyframes517 = frozenset([24, 26, 33])
    FOLLOW_RBRACE_in_keyframes520 = frozenset([1])
    FOLLOW_keyframe_selector_in_keyframes_block532 = frozenset([23, 25])
    FOLLOW_COMMA_in_keyframes_block536 = frozenset([26, 33])
    FOLLOW_keyframe_selector_in_keyframes_block538 = frozenset([23, 25])
    FOLLOW_LBRACE_in_keyframes_block543 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_keyframes_block545 = frozenset([24])
    FOLLOW_RBRACE_in_keyframes_block547 = frozenset([1])
    FOLLOW_set_in_keyframe_selector577 = frozenset([1])
    FOLLOW_selector_in_ruleSet600 = frozenset([23, 25])
    FOLLOW_COMMA_in_ruleSet603 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_selector_in_ruleSet605 = frozenset([23, 25])
    FOLLOW_LBRACE_in_ruleSet609 = frozenset([24, 26, 39])
    FOLLOW_declarationset_in_ruleSet611 = frozenset([24])
    FOLLOW_RBRACE_in_ruleSet613 = frozenset([1])
    FOLLOW_simpleSelector_in_selector641 = frozenset([1, 26, 28, 34, 35, 36, 37, 38, 39])
    FOLLOW_combinator_in_selector644 = frozenset([26, 28, 36, 37, 38, 39])
    FOLLOW_simpleSelector_in_selector646 = frozenset([1, 26, 28, 34, 35, 36, 37, 38, 39])
    FOLLOW_PLUS_in_combinator659 = frozenset([1])
    FOLLOW_GREATER_in_combinator664 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector678 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector685 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector697 = frozenset([1, 26, 28, 36, 37, 38, 39])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent759 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent764 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent769 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent774 = frozenset([1])
    FOLLOW_DOT_in_cssClass785 = frozenset([26])
    FOLLOW_IDENT_in_cssClass789 = frozenset([1])
    FOLLOW_COLON_in_pseudo813 = frozenset([26, 28, 40])
    FOLLOW_COLON_in_pseudo817 = frozenset([26, 28, 40])
    FOLLOW_IDENT_in_pseudo823 = frozenset([1])
    FOLLOW_pseudoFunction_in_pseudo845 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction876 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_pseudoFunction878 = frozenset([29])
    FOLLOW_RPAREN_in_pseudoFunction880 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction899 = frozenset([38])
    FOLLOW_LBRACKET_in_pseudoFunction901 = frozenset([26])
    FOLLOW_attribBody_in_pseudoFunction903 = frozenset([41])
    FOLLOW_RBRACKET_in_pseudoFunction905 = frozenset([29])
    FOLLOW_RPAREN_in_pseudoFunction907 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudoFunction930 = frozenset([28])
    FOLLOW_pseudo_in_pseudoFunction932 = frozenset([29])
    FOLLOW_RPAREN_in_pseudoFunction934 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib959 = frozenset([26])
    FOLLOW_attribBody_in_attrib961 = frozenset([41])
    FOLLOW_RBRACKET_in_attrib963 = frozenset([1])
    FOLLOW_IDENT_in_attribBody986 = frozenset([1])
    FOLLOW_IDENT_in_attribBody991 = frozenset([42, 43, 44, 45, 46, 47])
    FOLLOW_set_in_attribBody996 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_term_in_attribBody1040 = frozenset([1])
    FOLLOW_declaration_in_declarationset1051 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1054 = frozenset([26, 39])
    FOLLOW_declaration_in_declarationset1056 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1060 = frozenset([1])
    FOLLOW_property_in_declaration1091 = frozenset([28])
    FOLLOW_COLON_in_declaration1093 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_declaration1095 = frozenset([1, 48])
    FOLLOW_prio_in_declaration1097 = frozenset([1])
    FOLLOW_property_in_declaration1120 = frozenset([28])
    FOLLOW_COLON_in_declaration1122 = frozenset([1])
    FOLLOW_IDENT_in_property1147 = frozenset([1])
    FOLLOW_STAR_in_property1157 = frozenset([26])
    FOLLOW_IDENT_in_property1161 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1183 = frozenset([1])
    FOLLOW_term_in_expr1194 = frozenset([1, 18, 21, 25, 26, 33, 34, 36, 40, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_operator_in_expr1197 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_term_in_expr1200 = frozenset([1, 18, 21, 25, 26, 33, 34, 36, 40, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_SOLIDUS_in_operator1215 = frozenset([1])
    FOLLOW_COMMA_in_operator1220 = frozenset([1])
    FOLLOW_unaryOperator_in_term1239 = frozenset([33, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_set_in_term1245 = frozenset([1])
    FOLLOW_STRING_in_term1345 = frozenset([1])
    FOLLOW_IDENT_in_term1350 = frozenset([1])
    FOLLOW_URI_in_term1355 = frozenset([1])
    FOLLOW_function_in_term1360 = frozenset([1])
    FOLLOW_hexColor_in_term1365 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term1370 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1400 = frozenset([26])
    FOLLOW_fnct_args_in_function1402 = frozenset([29])
    FOLLOW_RPAREN_in_function1404 = frozenset([1])
    FOLLOW_fnct_name_in_function1422 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_function1424 = frozenset([29])
    FOLLOW_RPAREN_in_function1426 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1451 = frozenset([28, 37])
    FOLLOW_set_in_fnct_name1453 = frozenset([26, 28, 37, 40])
    FOLLOW_FUNCTION_in_fnct_name1463 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1477 = frozenset([1, 25])
    FOLLOW_COMMA_in_fnct_args1480 = frozenset([26])
    FOLLOW_fnct_arg_in_fnct_args1482 = frozenset([1, 25])
    FOLLOW_IDENT_in_fnct_arg1502 = frozenset([42])
    FOLLOW_OPEQ_in_fnct_arg1504 = frozenset([18, 21, 26, 33, 34, 36, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_expr_in_fnct_arg1507 = frozenset([1])
    FOLLOW_HASH_in_hexColor1518 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss682 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss694 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
