# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-17 14:57:27

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=41
STAR=35
NOT=27
EOF=-1
MEDIA_SYM=22
LBRACKET=40
INCLUDES=44
RPAREN=32
NAME=64
GREATER=37
ESCAPE=61
DIMENSION=97
STRINGESC=95
NL=98
COMMENT=92
N_Media=9
D=69
E=70
F=71
G=72
A=66
RBRACE=24
B=67
C=68
L=77
IMPORT_SYM=20
NMCHAR=63
M=78
N=79
O=80
H=73
I=74
J=75
NUMBER=48
K=76
U=86
T=85
W=88
V=87
Q=82
P=81
S=84
CDO=93
R=83
CDC=94
PERCENTAGE=49
URL=65
Y=90
X=89
URI=21
Z=91
PAGE_SYM=34
WS=96
DASHMATCH=45
EMS=51
N_RuleSet=10
NONASCII=59
N_Page=8
N_Declarations=12
ONLY=26
N_Selector=11
LBRACE=23
AND=28
N_Import=6
LPAREN=30
LENGTH=50
IMPORTANT_SYM=46
N_Function=14
TIME=54
COMMA=25
N_StyleSheet=4
IDENT=29
PLUS=36
FREQ=55
RBRACKET=42
DOT=39
CHARSET_SYM=17
ANGLE=53
HASH=38
HEXCHAR=58
N_CharSet=5
RESOLUTION=56
MINUS=57
SOLIDUS=47
SEMI=19
UNICODE=60
COLON=31
NMSTART=62
N_Declaration=13
OPEQ=43
FONTFACE_SYM=33
EXS=52
N_Space=16
N_Attrib=15
N_FontFace=7
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_CharSet", "N_Import", "N_FontFace", "N_Page", "N_Media", 
    "N_RuleSet", "N_Selector", "N_Declarations", "N_Declaration", "N_Function", 
    "N_Attrib", "N_Space", "CHARSET_SYM", "STRING", "SEMI", "IMPORT_SYM", 
    "URI", "MEDIA_SYM", "LBRACE", "RBRACE", "COMMA", "ONLY", "NOT", "AND", 
    "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", "STAR", 
    "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "FUNCTION", "RBRACKET", 
    "OPEQ", "INCLUDES", "DASHMATCH", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "PERCENTAGE", "LENGTH", "EMS", "EXS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
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

        self.dfa19 = self.DFA19(
            self, 19,
            eot = self.DFA19_eot,
            eof = self.DFA19_eof,
            min = self.DFA19_min,
            max = self.DFA19_max,
            accept = self.DFA19_accept,
            special = self.DFA19_special,
            transition = self.DFA19_transition
            )

        self.dfa31 = self.DFA31(
            self, 31,
            eot = self.DFA31_eot,
            eof = self.DFA31_eof,
            min = self.DFA31_min,
            max = self.DFA31_max,
            accept = self.DFA31_accept,
            special = self.DFA31_special,
            transition = self.DFA31_transition
            )

        self.dfa32 = self.DFA32(
            self, 32,
            eot = self.DFA32_eot,
            eof = self.DFA32_eof,
            min = self.DFA32_min,
            max = self.DFA32_max,
            accept = self.DFA32_accept,
            special = self.DFA32_special,
            transition = self.DFA32_transition
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
    # lesscss.g:50:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) ;
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
                # lesscss.g:51:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) )
                # lesscss.g:51:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:51:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:51:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet169)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:52:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:52:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet180)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet191)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet201) 
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
                    # 55:13: -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    # lesscss.g:55:16: ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:55:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:55:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:55:49: ( bodylist )?
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
    # lesscss.g:61:1: charSet : CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) ;
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
        stream_CHARSET_SYM = RewriteRuleTokenStream(self._adaptor, "token CHARSET_SYM")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # lesscss.g:62:5: ( CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) )
                # lesscss.g:62:9: CHARSET_SYM STRING SEMI
                pass 
                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet254) 
                if self._state.backtracking == 0:
                    stream_CHARSET_SYM.add(CHARSET_SYM5)
                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet256) 
                if self._state.backtracking == 0:
                    stream_STRING.add(STRING6)
                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet258) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI7)

                # AST Rewrite
                # elements: STRING
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
                    # 63:9: -> ^( N_CharSet STRING )
                    # lesscss.g:63:12: ^( N_CharSet STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_CharSet, "N_CharSet"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

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

    # $ANTLR end "charSet"

    class imports_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.imports_return, self).__init__()

            self.tree = None




    # $ANTLR start "imports"
    # lesscss.g:69:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI -> ^( N_Import importUrl ) ;
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
        stream_IMPORT_SYM = RewriteRuleTokenStream(self._adaptor, "token IMPORT_SYM")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_media_query_list = RewriteRuleSubtreeStream(self._adaptor, "rule media_query_list")
        stream_importUrl = RewriteRuleSubtreeStream(self._adaptor, "rule importUrl")
        try:
            try:
                # lesscss.g:70:5: ( IMPORT_SYM importUrl ( media_query_list )? SEMI -> ^( N_Import importUrl ) )
                # lesscss.g:70:9: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports296) 
                if self._state.backtracking == 0:
                    stream_IMPORT_SYM.add(IMPORT_SYM8)
                self._state.following.append(self.FOLLOW_importUrl_in_imports298)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_importUrl.add(importUrl9.tree)
                # lesscss.g:70:30: ( media_query_list )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((ONLY <= LA3_0 <= NOT) or (IDENT <= LA3_0 <= LPAREN)) :
                    alt3 = 1
                if alt3 == 1:
                    # lesscss.g:70:30: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports300)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_media_query_list.add(media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports303) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI11)

                # AST Rewrite
                # elements: importUrl
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
                    # 71:9: -> ^( N_Import importUrl )
                    # lesscss.g:71:12: ^( N_Import importUrl )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Import, "N_Import"), root_1)

                    self._adaptor.addChild(root_1, stream_importUrl.nextTree())

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

    # $ANTLR end "imports"

    class importUrl_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.importUrl_return, self).__init__()

            self.tree = None




    # $ANTLR start "importUrl"
    # lesscss.g:74:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:75:5: ( STRING | URI )
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

    class media_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_return, self).__init__()

            self.tree = None




    # $ANTLR start "media"
    # lesscss.g:83:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( media_query_list )? ( ruleSet )* ) ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM13 = None
        LBRACE15 = None
        RBRACE17 = None
        media_query_list14 = None

        ruleSet16 = None


        MEDIA_SYM13_tree = None
        LBRACE15_tree = None
        RBRACE17_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_MEDIA_SYM = RewriteRuleTokenStream(self._adaptor, "token MEDIA_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_media_query_list = RewriteRuleSubtreeStream(self._adaptor, "rule media_query_list")
        stream_ruleSet = RewriteRuleSubtreeStream(self._adaptor, "rule ruleSet")
        try:
            try:
                # lesscss.g:84:5: ( MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( media_query_list )? ( ruleSet )* ) )
                # lesscss.g:84:7: MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE
                pass 
                MEDIA_SYM13=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media365) 
                if self._state.backtracking == 0:
                    stream_MEDIA_SYM.add(MEDIA_SYM13)
                # lesscss.g:84:17: ( media_query_list )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((ONLY <= LA4_0 <= NOT) or (IDENT <= LA4_0 <= LPAREN)) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:84:17: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media367)
                    media_query_list14 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_media_query_list.add(media_query_list14.tree)



                LBRACE15=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media378) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE15)
                # lesscss.g:86:13: ( ruleSet )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == IDENT or LA5_0 == COLON or LA5_0 == STAR or (HASH <= LA5_0 <= LBRACKET)) :
                        alt5 = 1


                    if alt5 == 1:
                        # lesscss.g:86:13: ruleSet
                        pass 
                        self._state.following.append(self.FOLLOW_ruleSet_in_media392)
                        ruleSet16 = self.ruleSet()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ruleSet.add(ruleSet16.tree)


                    else:
                        break #loop5
                RBRACE17=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media403) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE17)

                # AST Rewrite
                # elements: ruleSet, media_query_list
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
                    # 88:9: -> ^( N_Media ( media_query_list )? ( ruleSet )* )
                    # lesscss.g:88:12: ^( N_Media ( media_query_list )? ( ruleSet )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Media, "N_Media"), root_1)

                    # lesscss.g:88:22: ( media_query_list )?
                    if stream_media_query_list.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query_list.nextTree())


                    stream_media_query_list.reset();
                    # lesscss.g:88:40: ( ruleSet )*
                    while stream_ruleSet.hasNext():
                        self._adaptor.addChild(root_1, stream_ruleSet.nextTree())


                    stream_ruleSet.reset();

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

    # $ANTLR end "media"

    class media_query_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query_list"
    # lesscss.g:94:1: media_query_list : media_query ( COMMA media_query )* ;
    def media_query_list(self, ):

        retval = self.media_query_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA19 = None
        media_query18 = None

        media_query20 = None


        COMMA19_tree = None

        try:
            try:
                # lesscss.g:95:5: ( media_query ( COMMA media_query )* )
                # lesscss.g:95:7: media_query ( COMMA media_query )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_media_query_in_media_query_list443)
                media_query18 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, media_query18.tree)
                # lesscss.g:95:19: ( COMMA media_query )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # lesscss.g:95:20: COMMA media_query
                        pass 
                        COMMA19=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list446)
                        if self._state.backtracking == 0:

                            COMMA19_tree = self._adaptor.createWithPayload(COMMA19)
                            self._adaptor.addChild(root_0, COMMA19_tree)

                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list448)
                        media_query20 = self.media_query()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, media_query20.tree)


                    else:
                        break #loop6



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
    # lesscss.g:98:1: media_query : ( ( ONLY | NOT )? media_type ( AND media_expr )* | media_expr ( AND media_expr )* );
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set21 = None
        AND23 = None
        AND26 = None
        media_type22 = None

        media_expr24 = None

        media_expr25 = None

        media_expr27 = None


        set21_tree = None
        AND23_tree = None
        AND26_tree = None

        try:
            try:
                # lesscss.g:99:5: ( ( ONLY | NOT )? media_type ( AND media_expr )* | media_expr ( AND media_expr )* )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((ONLY <= LA10_0 <= NOT) or LA10_0 == IDENT) :
                    alt10 = 1
                elif (LA10_0 == LPAREN) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # lesscss.g:99:7: ( ONLY | NOT )? media_type ( AND media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:99:7: ( ONLY | NOT )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((ONLY <= LA7_0 <= NOT)) :
                        alt7 = 1
                    if alt7 == 1:
                        # lesscss.g:
                        pass 
                        set21 = self.input.LT(1)
                        if (ONLY <= self.input.LA(1) <= NOT):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set21))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse





                    self._state.following.append(self.FOLLOW_media_type_in_media_query478)
                    media_type22 = self.media_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_type22.tree)
                    # lesscss.g:99:34: ( AND media_expr )*
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == AND) :
                            alt8 = 1


                        if alt8 == 1:
                            # lesscss.g:99:36: AND media_expr
                            pass 
                            AND23=self.match(self.input, AND, self.FOLLOW_AND_in_media_query482)
                            if self._state.backtracking == 0:

                                AND23_tree = self._adaptor.createWithPayload(AND23)
                                self._adaptor.addChild(root_0, AND23_tree)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query484)
                            media_expr24 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr24.tree)


                        else:
                            break #loop8


                elif alt10 == 2:
                    # lesscss.g:100:7: media_expr ( AND media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_expr_in_media_query495)
                    media_expr25 = self.media_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_expr25.tree)
                    # lesscss.g:100:18: ( AND media_expr )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == AND) :
                            alt9 = 1


                        if alt9 == 1:
                            # lesscss.g:100:20: AND media_expr
                            pass 
                            AND26=self.match(self.input, AND, self.FOLLOW_AND_in_media_query499)
                            if self._state.backtracking == 0:

                                AND26_tree = self._adaptor.createWithPayload(AND26)
                                self._adaptor.addChild(root_0, AND26_tree)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query501)
                            media_expr27 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr27.tree)


                        else:
                            break #loop9


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
    # lesscss.g:103:1: media_type : IDENT ;
    def media_type(self, ):

        retval = self.media_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT28 = None

        IDENT28_tree = None

        try:
            try:
                # lesscss.g:104:5: ( IDENT )
                # lesscss.g:104:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT28=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_type521)
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

    # $ANTLR end "media_type"

    class media_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_expr"
    # lesscss.g:107:1: media_expr : LPAREN media_feature ( COLON expr )? RPAREN ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN29 = None
        COLON31 = None
        RPAREN33 = None
        media_feature30 = None

        expr32 = None


        LPAREN29_tree = None
        COLON31_tree = None
        RPAREN33_tree = None

        try:
            try:
                # lesscss.g:108:5: ( LPAREN media_feature ( COLON expr )? RPAREN )
                # lesscss.g:108:7: LPAREN media_feature ( COLON expr )? RPAREN
                pass 
                root_0 = self._adaptor.nil()

                LPAREN29=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr538)
                if self._state.backtracking == 0:

                    LPAREN29_tree = self._adaptor.createWithPayload(LPAREN29)
                    self._adaptor.addChild(root_0, LPAREN29_tree)

                self._state.following.append(self.FOLLOW_media_feature_in_media_expr540)
                media_feature30 = self.media_feature()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, media_feature30.tree)
                # lesscss.g:108:28: ( COLON expr )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    alt11 = 1
                if alt11 == 1:
                    # lesscss.g:108:30: COLON expr
                    pass 
                    COLON31=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr544)
                    if self._state.backtracking == 0:

                        COLON31_tree = self._adaptor.createWithPayload(COLON31)
                        self._adaptor.addChild(root_0, COLON31_tree)

                    self._state.following.append(self.FOLLOW_expr_in_media_expr546)
                    expr32 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr32.tree)



                RPAREN33=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr551)
                if self._state.backtracking == 0:

                    RPAREN33_tree = self._adaptor.createWithPayload(RPAREN33)
                    self._adaptor.addChild(root_0, RPAREN33_tree)




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
    # lesscss.g:111:1: media_feature : IDENT ;
    def media_feature(self, ):

        retval = self.media_feature_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT34 = None

        IDENT34_tree = None

        try:
            try:
                # lesscss.g:112:5: ( IDENT )
                # lesscss.g:112:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT34=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_feature568)
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

    # $ANTLR end "media_feature"

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:118:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) ;
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
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_FONTFACE_SYM = RewriteRuleTokenStream(self._adaptor, "token FONTFACE_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:119:5: ( FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) )
                # lesscss.g:119:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                FONTFACE_SYM35=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface588) 
                if self._state.backtracking == 0:
                    stream_FONTFACE_SYM.add(FONTFACE_SYM35)
                LBRACE36=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface590) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE36)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface592)
                declarationset37 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset37.tree)
                RBRACE38=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface594) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE38)

                # AST Rewrite
                # elements: declarationset
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
                    # 120:9: -> ^( N_FontFace declarationset )
                    # lesscss.g:120:12: ^( N_FontFace declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_FontFace, "N_FontFace"), root_1)

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

    # $ANTLR end "fontface"

    class bodylist_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodylist_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodylist"
    # lesscss.g:123:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset39 = None



        try:
            try:
                # lesscss.g:124:5: ( ( bodyset )* )
                # lesscss.g:124:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:124:7: ( bodyset )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == MEDIA_SYM or LA12_0 == IDENT or LA12_0 == COLON or (FONTFACE_SYM <= LA12_0 <= STAR) or (HASH <= LA12_0 <= LBRACKET)) :
                        alt12 = 1


                    if alt12 == 1:
                        # lesscss.g:124:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist631)
                        bodyset39 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset39.tree)


                    else:
                        break #loop12



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
    # lesscss.g:127:1: bodyset : ( ruleSet | media | page | fontface );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet40 = None

        media41 = None

        page42 = None

        fontface43 = None



        try:
            try:
                # lesscss.g:128:5: ( ruleSet | media | page | fontface )
                alt13 = 4
                LA13 = self.input.LA(1)
                if LA13 == IDENT or LA13 == COLON or LA13 == STAR or LA13 == HASH or LA13 == DOT or LA13 == LBRACKET:
                    alt13 = 1
                elif LA13 == MEDIA_SYM:
                    alt13 = 2
                elif LA13 == PAGE_SYM:
                    alt13 = 3
                elif LA13 == FONTFACE_SYM:
                    alt13 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # lesscss.g:128:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset649)
                    ruleSet40 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet40.tree)


                elif alt13 == 2:
                    # lesscss.g:129:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset657)
                    media41 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media41.tree)


                elif alt13 == 3:
                    # lesscss.g:130:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset665)
                    page42 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page42.tree)


                elif alt13 == 4:
                    # lesscss.g:131:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset673)
                    fontface43 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface43.tree)


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

    class page_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.page_return, self).__init__()

            self.tree = None




    # $ANTLR start "page"
    # lesscss.g:134:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM44 = None
        LBRACE46 = None
        RBRACE48 = None
        pseudoPage45 = None

        declarationset47 = None


        PAGE_SYM44_tree = None
        LBRACE46_tree = None
        RBRACE48_tree = None
        stream_PAGE_SYM = RewriteRuleTokenStream(self._adaptor, "token PAGE_SYM")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_pseudoPage = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoPage")
        try:
            try:
                # lesscss.g:135:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) )
                # lesscss.g:135:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                PAGE_SYM44=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page693) 
                if self._state.backtracking == 0:
                    stream_PAGE_SYM.add(PAGE_SYM44)
                # lesscss.g:135:16: ( pseudoPage )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == COLON) :
                    alt14 = 1
                if alt14 == 1:
                    # lesscss.g:135:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page695)
                    pseudoPage45 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoPage.add(pseudoPage45.tree)



                LBRACE46=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page698) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE46)
                self._state.following.append(self.FOLLOW_declarationset_in_page700)
                declarationset47 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset47.tree)
                RBRACE48=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page702) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE48)

                # AST Rewrite
                # elements: pseudoPage, declarationset
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
                    # 136:9: -> ^( N_Page ( pseudoPage )? declarationset )
                    # lesscss.g:136:12: ^( N_Page ( pseudoPage )? declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Page, "N_Page"), root_1)

                    # lesscss.g:136:21: ( pseudoPage )?
                    if stream_pseudoPage.hasNext():
                        self._adaptor.addChild(root_1, stream_pseudoPage.nextTree())


                    stream_pseudoPage.reset();
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

    # $ANTLR end "page"

    class pseudoPage_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudoPage_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudoPage"
    # lesscss.g:139:1: pseudoPage : COLON IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON49 = None
        IDENT50 = None

        COLON49_tree = None
        IDENT50_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:140:5: ( COLON IDENT -> IDENT )
                # lesscss.g:140:7: COLON IDENT
                pass 
                COLON49=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage738) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON49)
                IDENT50=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage740) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT50)

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
                    # 140:19: -> IDENT
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

    class property_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.property_return, self).__init__()

            self.tree = None




    # $ANTLR start "property"
    # lesscss.g:143:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT51 = None
        STAR52 = None

        a_tree = None
        IDENT51_tree = None
        STAR52_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:144:5: ( IDENT | STAR a= IDENT -> IDENT )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IDENT) :
                    alt15 = 1
                elif (LA15_0 == STAR) :
                    alt15 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # lesscss.g:144:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT51=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property765)
                    if self._state.backtracking == 0:

                        IDENT51_tree = self._adaptor.createWithPayload(IDENT51)
                        self._adaptor.addChild(root_0, IDENT51_tree)



                elif alt15 == 2:
                    # lesscss.g:148:7: STAR a= IDENT
                    pass 
                    STAR52=self.match(self.input, STAR, self.FOLLOW_STAR_in_property784) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR52)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property788) 
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
                        # 150:9: -> IDENT
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

    class ruleSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.ruleSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleSet"
    # lesscss.g:154:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA54 = None
        LBRACE56 = None
        RBRACE58 = None
        selector53 = None

        selector55 = None

        declarationset57 = None


        COMMA54_tree = None
        LBRACE56_tree = None
        RBRACE58_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:155:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:155:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet829)
                selector53 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector53.tree)
                # lesscss.g:155:16: ( COMMA selector )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == COMMA) :
                        alt16 = 1


                    if alt16 == 1:
                        # lesscss.g:155:17: COMMA selector
                        pass 
                        COMMA54=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet832) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA54)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet834)
                        selector55 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector55.tree)


                    else:
                        break #loop16
                LBRACE56=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet838) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE56)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet840)
                declarationset57 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset57.tree)
                RBRACE58=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet842) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE58)

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
                    # 156:9: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:156:12: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:156:24: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:156:24: ^( N_Selector selector )
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
    # lesscss.g:159:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector59 = None

        combinator60 = None

        simpleSelector61 = None



        try:
            try:
                # lesscss.g:160:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:160:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector882)
                simpleSelector59 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector59.tree)
                # lesscss.g:160:22: ( combinator simpleSelector )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == IDENT or LA17_0 == COLON or (STAR <= LA17_0 <= LBRACKET)) :
                        alt17 = 1


                    if alt17 == 1:
                        # lesscss.g:160:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector885)
                        combinator60 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator60.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector887)
                        simpleSelector61 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector61.tree)


                    else:
                        break #loop17



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
    # lesscss.g:163:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS62 = None
        GREATER63 = None

        PLUS62_tree = None
        GREATER63_tree = None

        try:
            try:
                # lesscss.g:164:5: ( PLUS | GREATER | )
                alt18 = 3
                LA18 = self.input.LA(1)
                if LA18 == PLUS:
                    alt18 = 1
                elif LA18 == GREATER:
                    alt18 = 2
                elif LA18 == IDENT or LA18 == COLON or LA18 == STAR or LA18 == HASH or LA18 == DOT or LA18 == LBRACKET:
                    alt18 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # lesscss.g:164:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS62=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator906)
                    if self._state.backtracking == 0:

                        PLUS62_tree = self._adaptor.createWithPayload(PLUS62)
                        self._adaptor.addChild(root_0, PLUS62_tree)



                elif alt18 == 2:
                    # lesscss.g:165:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER63=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator914)
                    if self._state.backtracking == 0:

                        GREATER63_tree = self._adaptor.createWithPayload(GREATER63)
                        self._adaptor.addChild(root_0, GREATER63_tree)



                elif alt18 == 3:
                    # lesscss.g:167:5: 
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
    # lesscss.g:169:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName64 = None

        elementSubsequent65 = None

        elementSubsequent66 = None



        try:
            try:
                # lesscss.g:170:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == IDENT or LA21_0 == STAR) :
                    alt21 = 1
                elif (LA21_0 == COLON or (HASH <= LA21_0 <= LBRACKET)) :
                    alt21 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # lesscss.g:170:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector937)
                    elementName64 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName64.tree)
                    # lesscss.g:170:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop19
                        alt19 = 2
                        alt19 = self.dfa19.predict(self.input)
                        if alt19 == 1:
                            # lesscss.g:170:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector944)
                            elementSubsequent65 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent65.tree)


                        else:
                            break #loop19


                elif alt21 == 2:
                    # lesscss.g:171:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:171:7: ( ( esPred )=> elementSubsequent )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20 = self.input.LA(1)
                        if LA20 == HASH:
                            LA20_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt20 = 1


                        elif LA20 == DOT:
                            LA20_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt20 = 1


                        elif LA20 == LBRACKET:
                            LA20_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt20 = 1


                        elif LA20 == COLON:
                            LA20_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt20 = 1



                        if alt20 == 1:
                            # lesscss.g:171:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector959)
                            elementSubsequent66 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent66.tree)


                        else:
                            if cnt20 >= 1:
                                break #loop20

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


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
    # lesscss.g:174:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set67 = None

        set67_tree = None

        try:
            try:
                # lesscss.g:175:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set67 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set67))
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
    # lesscss.g:178:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set68 = None

        set68_tree = None

        try:
            try:
                # lesscss.g:179:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set68 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set68))
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
    # lesscss.g:183:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH69 = None
        cssClass70 = None

        attrib71 = None

        pseudo72 = None


        HASH69_tree = None

        try:
            try:
                # lesscss.g:184:5: ( HASH | cssClass | attrib | pseudo )
                alt22 = 4
                LA22 = self.input.LA(1)
                if LA22 == HASH:
                    alt22 = 1
                elif LA22 == DOT:
                    alt22 = 2
                elif LA22 == LBRACKET:
                    alt22 = 3
                elif LA22 == COLON:
                    alt22 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # lesscss.g:184:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH69=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent1032)
                    if self._state.backtracking == 0:

                        HASH69_tree = self._adaptor.createWithPayload(HASH69)
                        self._adaptor.addChild(root_0, HASH69_tree)



                elif alt22 == 2:
                    # lesscss.g:185:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent1040)
                    cssClass70 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass70.tree)


                elif alt22 == 3:
                    # lesscss.g:186:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent1048)
                    attrib71 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib71.tree)


                elif alt22 == 4:
                    # lesscss.g:187:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent1056)
                    pseudo72 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo72.tree)


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
    # lesscss.g:190:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT73 = None

        a_tree = None
        DOT73_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:191:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:191:7: DOT a= IDENT
                pass 
                DOT73=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass1073) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT73)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass1077) 
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
                    # 193:9: -> IDENT
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
    # lesscss.g:196:1: pseudo : ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) );
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON74 = None
        COLON75 = None
        FUNCTION76 = None
        RPAREN78 = None
        expr77 = None


        a_tree = None
        COLON74_tree = None
        COLON75_tree = None
        FUNCTION76_tree = None
        RPAREN78_tree = None
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:197:5: ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == COLON) :
                    LA23_1 = self.input.LA(2)

                    if (LA23_1 == IDENT) :
                        alt23 = 1
                    elif (LA23_1 == FUNCTION) :
                        alt23 = 2
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
                    # lesscss.g:197:7: COLON a= IDENT
                    pass 
                    COLON74=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1117) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON74)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1121) 
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
                        # 199:9: -> IDENT
                        self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                        retval.tree = root_0


                elif alt23 == 2:
                    # lesscss.g:200:7: COLON FUNCTION expr RPAREN
                    pass 
                    COLON75=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1152) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON75)
                    FUNCTION76=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1154) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION76)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1156)
                    expr77 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr77.tree)
                    RPAREN78=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1158) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN78)

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
                        # 201:9: -> ^( N_Function FUNCTION expr )
                        # lesscss.g:201:12: ^( N_Function FUNCTION expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
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

    # $ANTLR end "pseudo"

    class attrib_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attrib_return, self).__init__()

            self.tree = None




    # $ANTLR start "attrib"
    # lesscss.g:204:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET79 = None
        RBRACKET81 = None
        attribBody80 = None


        LBRACKET79_tree = None
        RBRACKET81_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:205:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:205:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET79=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1193) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET79)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1195)
                attribBody80 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody80.tree)
                RBRACKET81=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1197) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET81)

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
                    # 206:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:206:13: ^( N_Attrib attribBody )
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
    # lesscss.g:209:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT82 = None
        IDENT83 = None
        set84 = None
        set85 = None

        IDENT82_tree = None
        IDENT83_tree = None
        set84_tree = None
        set85_tree = None

        try:
            try:
                # lesscss.g:210:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == IDENT) :
                    LA24_1 = self.input.LA(2)

                    if ((OPEQ <= LA24_1 <= DASHMATCH)) :
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
                    # lesscss.g:210:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT82=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1232)
                    if self._state.backtracking == 0:

                        IDENT82_tree = self._adaptor.createWithPayload(IDENT82)
                        self._adaptor.addChild(root_0, IDENT82_tree)



                elif alt24 == 2:
                    # lesscss.g:211:7: IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT83=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1240)
                    if self._state.backtracking == 0:

                        IDENT83_tree = self._adaptor.createWithPayload(IDENT83)
                        self._adaptor.addChild(root_0, IDENT83_tree)

                    set84 = self.input.LT(1)
                    set84 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set84), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set85 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set85))
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
    # lesscss.g:214:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI87 = None
        SEMI89 = None
        declaration86 = None

        declaration88 = None


        SEMI87_tree = None
        SEMI89_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:215:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:215:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1280)
                declaration86 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration86.tree)
                # lesscss.g:215:19: ( SEMI declaration )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == SEMI) :
                        LA25_1 = self.input.LA(2)

                        if (LA25_1 == IDENT or LA25_1 == STAR) :
                            alt25 = 1




                    if alt25 == 1:
                        # lesscss.g:215:20: SEMI declaration
                        pass 
                        SEMI87=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1283) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI87)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1285)
                        declaration88 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration88.tree)


                    else:
                        break #loop25
                # lesscss.g:215:39: ( SEMI )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == SEMI) :
                    alt26 = 1
                if alt26 == 1:
                    # lesscss.g:215:39: SEMI
                    pass 
                    SEMI89=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1289) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI89)




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
                    # 215:45: -> ( declaration )+
                    # lesscss.g:215:48: ( declaration )+
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
    # lesscss.g:218:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON91 = None
        property90 = None

        expr92 = None

        prio93 = None


        COLON91_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:219:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:219:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1312)
                property90 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property90.tree)
                COLON91=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1314) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON91)
                self._state.following.append(self.FOLLOW_expr_in_declaration1316)
                expr92 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr92.tree)
                # lesscss.g:219:27: ( prio )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == IMPORTANT_SYM) :
                    alt27 = 1
                if alt27 == 1:
                    # lesscss.g:219:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1318)
                    prio93 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prio.add(prio93.tree)




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
                    # 219:33: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:219:36: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:219:66: ( prio )?
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

    class prio_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.prio_return, self).__init__()

            self.tree = None




    # $ANTLR start "prio"
    # lesscss.g:222:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM94 = None

        IMPORTANT_SYM94_tree = None

        try:
            try:
                # lesscss.g:223:5: ( IMPORTANT_SYM )
                # lesscss.g:223:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM94=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1349)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM94_tree = self._adaptor.createWithPayload(IMPORTANT_SYM94)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM94_tree)




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
    # lesscss.g:226:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term95 = None

        operator96 = None

        term97 = None



        try:
            try:
                # lesscss.g:227:5: ( term ( operator term )* )
                # lesscss.g:227:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1366)
                term95 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term95.tree)
                # lesscss.g:227:12: ( operator term )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == COMMA) :
                        LA28_2 = self.input.LA(2)

                        if (LA28_2 == IDENT) :
                            LA28_4 = self.input.LA(3)

                            if ((STRING <= LA28_4 <= SEMI) or LA28_4 == URI or (RBRACE <= LA28_4 <= IDENT) or (COLON <= LA28_4 <= RPAREN) or LA28_4 == PLUS or (HASH <= LA28_4 <= DOT) or LA28_4 == FUNCTION or (IMPORTANT_SYM <= LA28_4 <= MINUS)) :
                                alt28 = 1


                        elif (LA28_2 == STRING or LA28_2 == URI or (ONLY <= LA28_2 <= AND) or LA28_2 == PLUS or LA28_2 == HASH or LA28_2 == FUNCTION or (NUMBER <= LA28_2 <= MINUS)) :
                            alt28 = 1


                    elif (LA28_0 == STRING or LA28_0 == URI or (ONLY <= LA28_0 <= IDENT) or LA28_0 == PLUS or LA28_0 == HASH or LA28_0 == FUNCTION or (SOLIDUS <= LA28_0 <= MINUS)) :
                        alt28 = 1


                    if alt28 == 1:
                        # lesscss.g:227:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1369)
                        operator96 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator96.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1372)
                        term97 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term97.tree)


                    else:
                        break #loop28



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
    # lesscss.g:230:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS98 = None
        COMMA99 = None

        SOLIDUS98_tree = None
        COMMA99_tree = None

        try:
            try:
                # lesscss.g:231:5: ( SOLIDUS | COMMA | -> N_Space )
                alt29 = 3
                LA29 = self.input.LA(1)
                if LA29 == SOLIDUS:
                    alt29 = 1
                elif LA29 == COMMA:
                    alt29 = 2
                elif LA29 == STRING or LA29 == URI or LA29 == ONLY or LA29 == NOT or LA29 == AND or LA29 == IDENT or LA29 == PLUS or LA29 == HASH or LA29 == FUNCTION or LA29 == NUMBER or LA29 == PERCENTAGE or LA29 == LENGTH or LA29 == EMS or LA29 == EXS or LA29 == ANGLE or LA29 == TIME or LA29 == FREQ or LA29 == RESOLUTION or LA29 == MINUS:
                    alt29 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # lesscss.g:231:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS98=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1393)
                    if self._state.backtracking == 0:

                        SOLIDUS98_tree = self._adaptor.createWithPayload(SOLIDUS98)
                        self._adaptor.addChild(root_0, SOLIDUS98_tree)



                elif alt29 == 2:
                    # lesscss.g:232:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA99=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1401)
                    if self._state.backtracking == 0:

                        COMMA99_tree = self._adaptor.createWithPayload(COMMA99)
                        self._adaptor.addChild(root_0, COMMA99_tree)



                elif alt29 == 3:
                    # lesscss.g:233:7: 
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
                        # 233:7: -> N_Space
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
    # lesscss.g:236:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | NOT | AND | ONLY | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set101 = None
        STRING102 = None
        NOT103 = None
        AND104 = None
        ONLY105 = None
        IDENT106 = None
        URI107 = None
        unaryOperator100 = None

        function108 = None

        hexColor109 = None


        set101_tree = None
        STRING102_tree = None
        NOT103_tree = None
        AND104_tree = None
        ONLY105_tree = None
        IDENT106_tree = None
        URI107_tree = None

        try:
            try:
                # lesscss.g:237:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | NOT | AND | ONLY | IDENT | URI | function | hexColor )
                alt31 = 9
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # lesscss.g:237:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:237:20: ( unaryOperator )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == PLUS or LA30_0 == MINUS) :
                        alt30 = 1
                    if alt30 == 1:
                        # lesscss.g:237:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1429)
                        unaryOperator100 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator100.tree, root_0)



                    set101 = self.input.LT(1)
                    if (NUMBER <= self.input.LA(1) <= RESOLUTION):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set101))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt31 == 2:
                    # lesscss.g:249:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING102=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1603)
                    if self._state.backtracking == 0:

                        STRING102_tree = self._adaptor.createWithPayload(STRING102)
                        self._adaptor.addChild(root_0, STRING102_tree)



                elif alt31 == 3:
                    # lesscss.g:250:7: NOT
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT103=self.match(self.input, NOT, self.FOLLOW_NOT_in_term1611)
                    if self._state.backtracking == 0:

                        NOT103_tree = self._adaptor.createWithPayload(NOT103)
                        self._adaptor.addChild(root_0, NOT103_tree)



                elif alt31 == 4:
                    # lesscss.g:251:7: AND
                    pass 
                    root_0 = self._adaptor.nil()

                    AND104=self.match(self.input, AND, self.FOLLOW_AND_in_term1619)
                    if self._state.backtracking == 0:

                        AND104_tree = self._adaptor.createWithPayload(AND104)
                        self._adaptor.addChild(root_0, AND104_tree)



                elif alt31 == 5:
                    # lesscss.g:252:7: ONLY
                    pass 
                    root_0 = self._adaptor.nil()

                    ONLY105=self.match(self.input, ONLY, self.FOLLOW_ONLY_in_term1627)
                    if self._state.backtracking == 0:

                        ONLY105_tree = self._adaptor.createWithPayload(ONLY105)
                        self._adaptor.addChild(root_0, ONLY105_tree)



                elif alt31 == 6:
                    # lesscss.g:253:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT106=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1635)
                    if self._state.backtracking == 0:

                        IDENT106_tree = self._adaptor.createWithPayload(IDENT106)
                        self._adaptor.addChild(root_0, IDENT106_tree)



                elif alt31 == 7:
                    # lesscss.g:254:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI107=self.match(self.input, URI, self.FOLLOW_URI_in_term1643)
                    if self._state.backtracking == 0:

                        URI107_tree = self._adaptor.createWithPayload(URI107)
                        self._adaptor.addChild(root_0, URI107_tree)



                elif alt31 == 8:
                    # lesscss.g:255:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1651)
                    function108 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function108.tree)


                elif alt31 == 9:
                    # lesscss.g:256:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1659)
                    hexColor109 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor109.tree)


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
    # lesscss.g:259:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set110 = None

        set110_tree = None

        try:
            try:
                # lesscss.g:260:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set110 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set110))
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
    # lesscss.g:265:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN113 = None
        RPAREN116 = None
        fnct_name111 = None

        fnct_args112 = None

        fnct_name114 = None

        expr115 = None


        RPAREN113_tree = None
        RPAREN116_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:266:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt32 = 2
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # lesscss.g:266:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1704)
                    fnct_name111 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name111.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1706)
                    fnct_args112 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args112.tree)
                    RPAREN113=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1708) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN113)

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
                        # 267:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:267:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt32 == 2:
                    # lesscss.g:269:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1735)
                    fnct_name114 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name114.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1737)
                    expr115 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr115.tree)
                    RPAREN116=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1739) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN116)

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
                        # 270:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:270:12: ^( N_Function fnct_name expr )
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
    # lesscss.g:274:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT117 = None
        set118 = None
        FUNCTION119 = None

        IDENT117_tree = None
        set118_tree = None
        FUNCTION119_tree = None

        try:
            try:
                # lesscss.g:275:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:275:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:275:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == IDENT) :
                        alt34 = 1


                    if alt34 == 1:
                        # lesscss.g:275:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT117=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1776)
                        if self._state.backtracking == 0:

                            IDENT117_tree = self._adaptor.createWithPayload(IDENT117)
                            self._adaptor.addChild(root_0, IDENT117_tree)

                        # lesscss.g:275:14: ( COLON | DOT )+
                        cnt33 = 0
                        while True: #loop33
                            alt33 = 2
                            LA33_0 = self.input.LA(1)

                            if (LA33_0 == COLON or LA33_0 == DOT) :
                                alt33 = 1


                            if alt33 == 1:
                                # lesscss.g:
                                pass 
                                set118 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set118))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt33 >= 1:
                                    break #loop33

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(33, self.input)
                                raise eee

                            cnt33 += 1


                    else:
                        break #loop34
                FUNCTION119=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1788)
                if self._state.backtracking == 0:

                    FUNCTION119_tree = self._adaptor.createWithPayload(FUNCTION119)
                    self._adaptor.addChild(root_0, FUNCTION119_tree)




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
    # lesscss.g:278:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA121 = None
        fnct_arg120 = None

        fnct_arg122 = None


        COMMA121_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:279:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:279:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1807)
                fnct_arg120 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg120.tree)
                # lesscss.g:279:16: ( COMMA fnct_arg )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == COMMA) :
                        alt35 = 1


                    if alt35 == 1:
                        # lesscss.g:279:17: COMMA fnct_arg
                        pass 
                        COMMA121=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1810) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA121)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1812)
                        fnct_arg122 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg122.tree)


                    else:
                        break #loop35

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
                    # 280:9: -> ( fnct_arg )+
                    # lesscss.g:280:12: ( fnct_arg )+
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
    # lesscss.g:283:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT123 = None
        OPEQ124 = None
        expr125 = None


        IDENT123_tree = None
        OPEQ124_tree = None

        try:
            try:
                # lesscss.g:284:5: ( IDENT OPEQ expr )
                # lesscss.g:284:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT123=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1844)
                if self._state.backtracking == 0:

                    IDENT123_tree = self._adaptor.createWithPayload(IDENT123)
                    self._adaptor.addChild(root_0, IDENT123_tree)

                OPEQ124=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1846)
                if self._state.backtracking == 0:

                    OPEQ124_tree = self._adaptor.createWithPayload(OPEQ124)
                    root_0 = self._adaptor.becomeRoot(OPEQ124_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1849)
                expr125 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr125.tree)



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
    # lesscss.g:287:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH126 = None

        HASH126_tree = None

        try:
            try:
                # lesscss.g:288:5: ( HASH )
                # lesscss.g:288:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH126=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1866)
                if self._state.backtracking == 0:

                    HASH126_tree = self._adaptor.createWithPayload(HASH126)
                    self._adaptor.addChild(root_0, HASH126_tree)




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
        # lesscss.g:170:20: ( esPred )
        # lesscss.g:170:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss941)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:171:8: ( esPred )
        # lesscss.g:171:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss956)
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



    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\1\27\3\uffff\4\0\3\uffff"
        )

    DFA19_max = DFA.unpack(
        u"\1\50\3\uffff\4\0\3\uffff"
        )

    DFA19_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA19_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA19_transition = [
        DFA.unpack(u"\1\1\1\uffff\1\1\3\uffff\1\1\1\uffff\1\7\3\uffff\3\1"
        u"\1\4\1\5\1\6"),
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

    # class definition for DFA #19

    class DFA19(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA19_4 = input.LA(1)

                 
                index19_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index19_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA19_5 = input.LA(1)

                 
                index19_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index19_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA19_6 = input.LA(1)

                 
                index19_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index19_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA19_7 = input.LA(1)

                 
                index19_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index19_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 19, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\1\22\5\uffff\1\22\4\uffff"
        )

    DFA31_max = DFA.unpack(
        u"\1\71\5\uffff\1\71\4\uffff"
        )

    DFA31_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\uffff\1\7\1\10\1\11\1\6"
        )

    DFA31_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA31_transition = [
        DFA.unpack(u"\1\2\2\uffff\1\7\4\uffff\1\5\1\3\1\4\1\6\6\uffff\1\1"
        u"\1\uffff\1\11\2\uffff\1\10\6\uffff\12\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\12\1\uffff\1\12\2\uffff\6\12\1\uffff\1\10\1\12\3"
        u"\uffff\1\12\1\uffff\1\12\1\10\1\uffff\1\12\4\uffff\14\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #31

    class DFA31(DFA):
        pass


    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\1\35\1\37\1\22\1\35\1\22\2\uffff"
        )

    DFA32_max = DFA.unpack(
        u"\1\51\1\47\1\71\1\51\1\71\2\uffff"
        )

    DFA32_accept = DFA.unpack(
        u"\5\uffff\1\2\1\1"
        )

    DFA32_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA32_transition = [
        DFA.unpack(u"\1\1\13\uffff\1\2"),
        DFA.unpack(u"\1\3\7\uffff\1\3"),
        DFA.unpack(u"\1\5\2\uffff\1\5\4\uffff\3\5\1\4\6\uffff\1\5\1\uffff"
        u"\1\5\2\uffff\1\5\6\uffff\12\5"),
        DFA.unpack(u"\1\1\1\uffff\1\3\7\uffff\1\3\1\uffff\1\2"),
        DFA.unpack(u"\1\5\2\uffff\1\5\3\uffff\5\5\1\uffff\2\5\3\uffff\1"
        u"\5\1\uffff\2\5\1\uffff\1\5\1\uffff\1\6\3\uffff\13\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #32

    class DFA32(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet169 = frozenset([20, 22, 29, 31, 33, 34, 35, 38, 39, 40])
    FOLLOW_imports_in_styleSheet180 = frozenset([20, 22, 29, 31, 33, 34, 35, 38, 39, 40])
    FOLLOW_bodylist_in_styleSheet191 = frozenset([])
    FOLLOW_EOF_in_styleSheet201 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet254 = frozenset([18])
    FOLLOW_STRING_in_charSet256 = frozenset([19])
    FOLLOW_SEMI_in_charSet258 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports296 = frozenset([18, 21])
    FOLLOW_importUrl_in_imports298 = frozenset([19, 26, 27, 29, 30])
    FOLLOW_media_query_list_in_imports300 = frozenset([19])
    FOLLOW_SEMI_in_imports303 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media365 = frozenset([23, 26, 27, 29, 30])
    FOLLOW_media_query_list_in_media367 = frozenset([23])
    FOLLOW_LBRACE_in_media378 = frozenset([24, 29, 31, 35, 38, 39, 40])
    FOLLOW_ruleSet_in_media392 = frozenset([24, 29, 31, 35, 38, 39, 40])
    FOLLOW_RBRACE_in_media403 = frozenset([1])
    FOLLOW_media_query_in_media_query_list443 = frozenset([1, 25])
    FOLLOW_COMMA_in_media_query_list446 = frozenset([26, 27, 29, 30])
    FOLLOW_media_query_in_media_query_list448 = frozenset([1, 25])
    FOLLOW_set_in_media_query467 = frozenset([26, 27, 29])
    FOLLOW_media_type_in_media_query478 = frozenset([1, 28])
    FOLLOW_AND_in_media_query482 = frozenset([26, 27, 29, 30])
    FOLLOW_media_expr_in_media_query484 = frozenset([1, 28])
    FOLLOW_media_expr_in_media_query495 = frozenset([1, 28])
    FOLLOW_AND_in_media_query499 = frozenset([26, 27, 29, 30])
    FOLLOW_media_expr_in_media_query501 = frozenset([1, 28])
    FOLLOW_IDENT_in_media_type521 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr538 = frozenset([29])
    FOLLOW_media_feature_in_media_expr540 = frozenset([31, 32])
    FOLLOW_COLON_in_media_expr544 = frozenset([18, 21, 26, 27, 28, 29, 36, 38, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_expr_in_media_expr546 = frozenset([32])
    FOLLOW_RPAREN_in_media_expr551 = frozenset([1])
    FOLLOW_IDENT_in_media_feature568 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface588 = frozenset([23])
    FOLLOW_LBRACE_in_fontface590 = frozenset([29, 35])
    FOLLOW_declarationset_in_fontface592 = frozenset([24])
    FOLLOW_RBRACE_in_fontface594 = frozenset([1])
    FOLLOW_bodyset_in_bodylist631 = frozenset([1, 22, 29, 31, 33, 34, 35, 38, 39, 40])
    FOLLOW_ruleSet_in_bodyset649 = frozenset([1])
    FOLLOW_media_in_bodyset657 = frozenset([1])
    FOLLOW_page_in_bodyset665 = frozenset([1])
    FOLLOW_fontface_in_bodyset673 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page693 = frozenset([23, 31])
    FOLLOW_pseudoPage_in_page695 = frozenset([23])
    FOLLOW_LBRACE_in_page698 = frozenset([29, 35])
    FOLLOW_declarationset_in_page700 = frozenset([24])
    FOLLOW_RBRACE_in_page702 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage738 = frozenset([29])
    FOLLOW_IDENT_in_pseudoPage740 = frozenset([1])
    FOLLOW_IDENT_in_property765 = frozenset([1])
    FOLLOW_STAR_in_property784 = frozenset([29])
    FOLLOW_IDENT_in_property788 = frozenset([1])
    FOLLOW_selector_in_ruleSet829 = frozenset([23, 25])
    FOLLOW_COMMA_in_ruleSet832 = frozenset([29, 31, 35, 38, 39, 40])
    FOLLOW_selector_in_ruleSet834 = frozenset([23, 25])
    FOLLOW_LBRACE_in_ruleSet838 = frozenset([29, 35])
    FOLLOW_declarationset_in_ruleSet840 = frozenset([24])
    FOLLOW_RBRACE_in_ruleSet842 = frozenset([1])
    FOLLOW_simpleSelector_in_selector882 = frozenset([1, 29, 31, 35, 36, 37, 38, 39, 40])
    FOLLOW_combinator_in_selector885 = frozenset([29, 31, 35, 38, 39, 40])
    FOLLOW_simpleSelector_in_selector887 = frozenset([1, 29, 31, 35, 36, 37, 38, 39, 40])
    FOLLOW_PLUS_in_combinator906 = frozenset([1])
    FOLLOW_GREATER_in_combinator914 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector937 = frozenset([1, 29, 31, 35, 38, 39, 40])
    FOLLOW_elementSubsequent_in_simpleSelector944 = frozenset([1, 29, 31, 35, 38, 39, 40])
    FOLLOW_elementSubsequent_in_simpleSelector959 = frozenset([1, 29, 31, 35, 38, 39, 40])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent1032 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent1040 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent1048 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent1056 = frozenset([1])
    FOLLOW_DOT_in_cssClass1073 = frozenset([29])
    FOLLOW_IDENT_in_cssClass1077 = frozenset([1])
    FOLLOW_COLON_in_pseudo1117 = frozenset([29])
    FOLLOW_IDENT_in_pseudo1121 = frozenset([1])
    FOLLOW_COLON_in_pseudo1152 = frozenset([41])
    FOLLOW_FUNCTION_in_pseudo1154 = frozenset([18, 21, 26, 27, 28, 29, 36, 38, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_expr_in_pseudo1156 = frozenset([32])
    FOLLOW_RPAREN_in_pseudo1158 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1193 = frozenset([29])
    FOLLOW_attribBody_in_attrib1195 = frozenset([42])
    FOLLOW_RBRACKET_in_attrib1197 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1232 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1240 = frozenset([43, 44, 45])
    FOLLOW_set_in_attribBody1242 = frozenset([18, 29])
    FOLLOW_set_in_attribBody1255 = frozenset([1])
    FOLLOW_declaration_in_declarationset1280 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1283 = frozenset([29, 35])
    FOLLOW_declaration_in_declarationset1285 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1289 = frozenset([1])
    FOLLOW_property_in_declaration1312 = frozenset([31])
    FOLLOW_COLON_in_declaration1314 = frozenset([18, 21, 26, 27, 28, 29, 36, 38, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_expr_in_declaration1316 = frozenset([1, 46])
    FOLLOW_prio_in_declaration1318 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1349 = frozenset([1])
    FOLLOW_term_in_expr1366 = frozenset([1, 18, 21, 25, 26, 27, 28, 29, 36, 38, 41, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_operator_in_expr1369 = frozenset([18, 21, 26, 27, 28, 29, 36, 38, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_term_in_expr1372 = frozenset([1, 18, 21, 25, 26, 27, 28, 29, 36, 38, 41, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_SOLIDUS_in_operator1393 = frozenset([1])
    FOLLOW_COMMA_in_operator1401 = frozenset([1])
    FOLLOW_unaryOperator_in_term1429 = frozenset([48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_set_in_term1441 = frozenset([1])
    FOLLOW_STRING_in_term1603 = frozenset([1])
    FOLLOW_NOT_in_term1611 = frozenset([1])
    FOLLOW_AND_in_term1619 = frozenset([1])
    FOLLOW_ONLY_in_term1627 = frozenset([1])
    FOLLOW_IDENT_in_term1635 = frozenset([1])
    FOLLOW_URI_in_term1643 = frozenset([1])
    FOLLOW_function_in_term1651 = frozenset([1])
    FOLLOW_hexColor_in_term1659 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1704 = frozenset([29])
    FOLLOW_fnct_args_in_function1706 = frozenset([32])
    FOLLOW_RPAREN_in_function1708 = frozenset([1])
    FOLLOW_fnct_name_in_function1735 = frozenset([18, 21, 26, 27, 28, 29, 36, 38, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_expr_in_function1737 = frozenset([32])
    FOLLOW_RPAREN_in_function1739 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1776 = frozenset([31, 39])
    FOLLOW_set_in_fnct_name1778 = frozenset([29, 31, 39, 41])
    FOLLOW_FUNCTION_in_fnct_name1788 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1807 = frozenset([1, 25])
    FOLLOW_COMMA_in_fnct_args1810 = frozenset([29])
    FOLLOW_fnct_arg_in_fnct_args1812 = frozenset([1, 25])
    FOLLOW_IDENT_in_fnct_arg1844 = frozenset([43])
    FOLLOW_OPEQ_in_fnct_arg1846 = frozenset([18, 21, 26, 27, 28, 29, 36, 38, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_expr_in_fnct_arg1849 = frozenset([1])
    FOLLOW_HASH_in_hexColor1866 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss941 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss956 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
