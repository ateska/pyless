# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-17 23:35:04

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=43
STAR=37
EOF=-1
MEDIA_SYM=25
LBRACKET=42
INCLUDES=46
RPAREN=32
NAME=68
GREATER=39
ESCAPE=65
DIMENSION=101
STRINGESC=99
NL=102
COMMENT=96
N_Media=9
D=73
E=74
F=75
G=76
A=70
RBRACE=27
B=71
C=72
L=81
IMPORT_SYM=23
NMCHAR=67
M=82
SUBSTRINGMATCH=50
N=83
O=84
H=77
I=78
J=79
NUMBER=53
K=80
U=90
T=89
W=92
V=91
Q=86
P=85
S=88
CDO=97
R=87
CDC=98
Y=94
PERCENTAGE=35
URL=69
X=93
Z=95
URI=24
PAGE_SYM=36
WS=100
DASHMATCH=47
EMS=55
N_RuleSet=12
NONASCII=63
N_Page=8
N_MediaQuery=10
N_Declarations=14
N_Selector=13
LBRACE=26
N_Import=6
LPAREN=30
LENGTH=54
IMPORTANT_SYM=51
N_Function=16
TIME=58
KEYFRAMES_SYM=34
COMMA=28
N_StyleSheet=4
IDENT=29
PLUS=38
FREQ=59
RBRACKET=44
DOT=41
CHARSET_SYM=20
ANGLE=57
HASH=40
HEXCHAR=62
N_CharSet=5
RESOLUTION=60
PREFIXMATCH=48
MINUS=61
N_Pseudo=19
SOLIDUS=52
SEMI=22
UNICODE=64
COLON=31
NMSTART=66
N_Declaration=15
FONTFACE_SYM=33
OPEQ=45
EXS=56
N_Space=18
N_MediaExpr=11
N_Attrib=17
SUFFIXMATCH=49
STRING=21
N_FontFace=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_CharSet", "N_Import", "N_FontFace", "N_Page", "N_Media", 
    "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_Selector", "N_Declarations", 
    "N_Declaration", "N_Function", "N_Attrib", "N_Space", "N_Pseudo", "CHARSET_SYM", 
    "STRING", "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", 
    "COMMA", "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "KEYFRAMES_SYM", 
    "PERCENTAGE", "PAGE_SYM", "STAR", "PLUS", "GREATER", "HASH", "DOT", 
    "LBRACKET", "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", 
    "PREFIXMATCH", "SUFFIXMATCH", "SUBSTRINGMATCH", "IMPORTANT_SYM", "SOLIDUS", 
    "NUMBER", "LENGTH", "EMS", "EXS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
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

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
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
    # lesscss.g:68:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) ;
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
                # lesscss.g:69:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) )
                # lesscss.g:69:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:69:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:69:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet205)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:70:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:70:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet216)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet227)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet237) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: charSet, bodylist, imports
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
                    # 73:13: -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    # lesscss.g:73:16: ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:73:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:73:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:73:49: ( bodylist )?
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
    # lesscss.g:79:1: charSet : CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) ;
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
                # lesscss.g:80:5: ( CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) )
                # lesscss.g:80:9: CHARSET_SYM STRING SEMI
                pass 
                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet290) 
                if self._state.backtracking == 0:
                    stream_CHARSET_SYM.add(CHARSET_SYM5)
                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet292) 
                if self._state.backtracking == 0:
                    stream_STRING.add(STRING6)
                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet294) 
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
                    # 81:9: -> ^( N_CharSet STRING )
                    # lesscss.g:81:12: ^( N_CharSet STRING )
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
    # lesscss.g:87:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI -> ^( N_Import importUrl ( media_query_list )? ) ;
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
                # lesscss.g:88:5: ( IMPORT_SYM importUrl ( media_query_list )? SEMI -> ^( N_Import importUrl ( media_query_list )? ) )
                # lesscss.g:88:9: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports332) 
                if self._state.backtracking == 0:
                    stream_IMPORT_SYM.add(IMPORT_SYM8)
                self._state.following.append(self.FOLLOW_importUrl_in_imports334)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_importUrl.add(importUrl9.tree)
                # lesscss.g:88:30: ( media_query_list )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((IDENT <= LA3_0 <= LPAREN)) :
                    alt3 = 1
                if alt3 == 1:
                    # lesscss.g:88:30: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports336)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_media_query_list.add(media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports339) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI11)

                # AST Rewrite
                # elements: importUrl, media_query_list
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
                    # 89:9: -> ^( N_Import importUrl ( media_query_list )? )
                    # lesscss.g:89:12: ^( N_Import importUrl ( media_query_list )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Import, "N_Import"), root_1)

                    self._adaptor.addChild(root_1, stream_importUrl.nextTree())
                    # lesscss.g:89:33: ( media_query_list )?
                    if stream_media_query_list.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query_list.nextTree())


                    stream_media_query_list.reset();

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
    # lesscss.g:92:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:93:5: ( STRING | URI )
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
    # lesscss.g:101:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( media_query_list )? ( ruleSet )* ) ;
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
                # lesscss.g:102:5: ( MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( media_query_list )? ( ruleSet )* ) )
                # lesscss.g:102:7: MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE
                pass 
                MEDIA_SYM13=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media404) 
                if self._state.backtracking == 0:
                    stream_MEDIA_SYM.add(MEDIA_SYM13)
                # lesscss.g:102:17: ( media_query_list )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((IDENT <= LA4_0 <= LPAREN)) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:102:17: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media406)
                    media_query_list14 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_media_query_list.add(media_query_list14.tree)



                LBRACE15=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media417) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE15)
                # lesscss.g:104:13: ( ruleSet )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == IDENT or LA5_0 == COLON or LA5_0 == STAR or (HASH <= LA5_0 <= LBRACKET)) :
                        alt5 = 1


                    if alt5 == 1:
                        # lesscss.g:104:13: ruleSet
                        pass 
                        self._state.following.append(self.FOLLOW_ruleSet_in_media431)
                        ruleSet16 = self.ruleSet()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ruleSet.add(ruleSet16.tree)


                    else:
                        break #loop5
                RBRACE17=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media442) 
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
                    # 106:9: -> ^( N_Media ( media_query_list )? ( ruleSet )* )
                    # lesscss.g:106:12: ^( N_Media ( media_query_list )? ( ruleSet )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Media, "N_Media"), root_1)

                    # lesscss.g:106:22: ( media_query_list )?
                    if stream_media_query_list.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query_list.nextTree())


                    stream_media_query_list.reset();
                    # lesscss.g:106:40: ( ruleSet )*
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
    # lesscss.g:112:1: media_query_list : media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) ;
    def media_query_list(self, ):

        retval = self.media_query_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA19 = None
        media_query18 = None

        media_query20 = None


        COMMA19_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_media_query = RewriteRuleSubtreeStream(self._adaptor, "rule media_query")
        try:
            try:
                # lesscss.g:113:5: ( media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) )
                # lesscss.g:113:7: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list482)
                media_query18 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query18.tree)
                # lesscss.g:113:19: ( COMMA media_query )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # lesscss.g:113:20: COMMA media_query
                        pass 
                        COMMA19=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list485) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA19)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list487)
                        media_query20 = self.media_query()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_media_query.add(media_query20.tree)


                    else:
                        break #loop6

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
                    # 114:9: -> ^( N_MediaQuery ( media_query )+ )
                    # lesscss.g:114:12: ^( N_MediaQuery ( media_query )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaQuery, "N_MediaQuery"), root_1)

                    # lesscss.g:114:27: ( media_query )+
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
    # lesscss.g:117:1: media_query : ( ( IDENT )? media_type ( IDENT media_expr )* | media_expr ( IDENT media_expr )* );
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT21 = None
        IDENT23 = None
        IDENT26 = None
        media_type22 = None

        media_expr24 = None

        media_expr25 = None

        media_expr27 = None


        IDENT21_tree = None
        IDENT23_tree = None
        IDENT26_tree = None

        try:
            try:
                # lesscss.g:118:5: ( ( IDENT )? media_type ( IDENT media_expr )* | media_expr ( IDENT media_expr )* )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IDENT) :
                    alt10 = 1
                elif (LA10_0 == LPAREN) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # lesscss.g:118:7: ( IDENT )? media_type ( IDENT media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:118:7: ( IDENT )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == IDENT) :
                        LA7_1 = self.input.LA(2)

                        if (LA7_1 == IDENT) :
                            LA7_2 = self.input.LA(3)

                            if (LA7_2 == SEMI or LA7_2 == LBRACE or (COMMA <= LA7_2 <= IDENT)) :
                                alt7 = 1
                    if alt7 == 1:
                        # lesscss.g:118:9: IDENT
                        pass 
                        IDENT21=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query525)
                        if self._state.backtracking == 0:

                            IDENT21_tree = self._adaptor.createWithPayload(IDENT21)
                            self._adaptor.addChild(root_0, IDENT21_tree)




                    self._state.following.append(self.FOLLOW_media_type_in_media_query530)
                    media_type22 = self.media_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_type22.tree)
                    # lesscss.g:118:29: ( IDENT media_expr )*
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == IDENT) :
                            alt8 = 1


                        if alt8 == 1:
                            # lesscss.g:118:31: IDENT media_expr
                            pass 
                            IDENT23=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query534)
                            if self._state.backtracking == 0:

                                IDENT23_tree = self._adaptor.createWithPayload(IDENT23)
                                root_0 = self._adaptor.becomeRoot(IDENT23_tree, root_0)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query537)
                            media_expr24 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr24.tree)


                        else:
                            break #loop8


                elif alt10 == 2:
                    # lesscss.g:119:7: media_expr ( IDENT media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_expr_in_media_query548)
                    media_expr25 = self.media_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_expr25.tree)
                    # lesscss.g:119:18: ( IDENT media_expr )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == IDENT) :
                            alt9 = 1


                        if alt9 == 1:
                            # lesscss.g:119:20: IDENT media_expr
                            pass 
                            IDENT26=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query552)
                            if self._state.backtracking == 0:

                                IDENT26_tree = self._adaptor.createWithPayload(IDENT26)
                                root_0 = self._adaptor.becomeRoot(IDENT26_tree, root_0)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query555)
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
    # lesscss.g:122:1: media_type : IDENT ;
    def media_type(self, ):

        retval = self.media_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT28 = None

        IDENT28_tree = None

        try:
            try:
                # lesscss.g:123:5: ( IDENT )
                # lesscss.g:123:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT28=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_type575)
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
    # lesscss.g:126:1: media_expr : LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN -> ^( N_MediaExpr media_feature ( expr )? ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN29 = None
        COLON31 = None
        COLON33 = None
        RPAREN34 = None
        media_feature30 = None

        expr32 = None


        LPAREN29_tree = None
        COLON31_tree = None
        COLON33_tree = None
        RPAREN34_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_media_feature = RewriteRuleSubtreeStream(self._adaptor, "rule media_feature")
        try:
            try:
                # lesscss.g:127:5: ( LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN -> ^( N_MediaExpr media_feature ( expr )? ) )
                # lesscss.g:127:7: LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN
                pass 
                LPAREN29=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr592) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN29)
                self._state.following.append(self.FOLLOW_media_feature_in_media_expr594)
                media_feature30 = self.media_feature()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_feature.add(media_feature30.tree)
                # lesscss.g:127:28: ( COLON expr )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == STRING or LA11_1 == URI or LA11_1 == IDENT or LA11_1 == PERCENTAGE or LA11_1 == PLUS or LA11_1 == HASH or LA11_1 == FUNCTION or (NUMBER <= LA11_1 <= MINUS)) :
                        alt11 = 1
                if alt11 == 1:
                    # lesscss.g:127:30: COLON expr
                    pass 
                    COLON31=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr598) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON31)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr600)
                    expr32 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr32.tree)



                # lesscss.g:127:44: ( COLON )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == COLON) :
                    alt12 = 1
                if alt12 == 1:
                    # lesscss.g:127:44: COLON
                    pass 
                    COLON33=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr605) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON33)



                RPAREN34=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr608) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN34)

                # AST Rewrite
                # elements: expr, media_feature
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
                    # 128:9: -> ^( N_MediaExpr media_feature ( expr )? )
                    # lesscss.g:128:12: ^( N_MediaExpr media_feature ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_feature.nextTree())
                    # lesscss.g:128:40: ( expr )?
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
    # lesscss.g:131:1: media_feature : IDENT ;
    def media_feature(self, ):

        retval = self.media_feature_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT35 = None

        IDENT35_tree = None

        try:
            try:
                # lesscss.g:132:5: ( IDENT )
                # lesscss.g:132:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT35=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_feature645)
                if self._state.backtracking == 0:

                    IDENT35_tree = self._adaptor.createWithPayload(IDENT35)
                    self._adaptor.addChild(root_0, IDENT35_tree)




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
    # lesscss.g:138:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM36 = None
        LBRACE37 = None
        RBRACE39 = None
        declarationset38 = None


        FONTFACE_SYM36_tree = None
        LBRACE37_tree = None
        RBRACE39_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_FONTFACE_SYM = RewriteRuleTokenStream(self._adaptor, "token FONTFACE_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:139:5: ( FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) )
                # lesscss.g:139:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                FONTFACE_SYM36=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface665) 
                if self._state.backtracking == 0:
                    stream_FONTFACE_SYM.add(FONTFACE_SYM36)
                LBRACE37=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface667) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE37)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface669)
                declarationset38 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset38.tree)
                RBRACE39=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface671) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE39)

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
                    # 140:9: -> ^( N_FontFace declarationset )
                    # lesscss.g:140:12: ^( N_FontFace declarationset )
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

    class keyframes_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.keyframes_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyframes"
    # lesscss.g:148:2: keyframes : KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE ;
    def keyframes(self, ):

        retval = self.keyframes_return()
        retval.start = self.input.LT(1)

        root_0 = None

        KEYFRAMES_SYM40 = None
        IDENT41 = None
        LBRACE42 = None
        RBRACE44 = None
        keyframes_block43 = None


        KEYFRAMES_SYM40_tree = None
        IDENT41_tree = None
        LBRACE42_tree = None
        RBRACE44_tree = None

        try:
            try:
                # lesscss.g:149:5: ( KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE )
                # lesscss.g:149:7: KEYFRAMES_SYM IDENT LBRACE ( keyframes_block )* RBRACE
                pass 
                root_0 = self._adaptor.nil()

                KEYFRAMES_SYM40=self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes711)
                if self._state.backtracking == 0:

                    KEYFRAMES_SYM40_tree = self._adaptor.createWithPayload(KEYFRAMES_SYM40)
                    self._adaptor.addChild(root_0, KEYFRAMES_SYM40_tree)

                IDENT41=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes713)
                if self._state.backtracking == 0:

                    IDENT41_tree = self._adaptor.createWithPayload(IDENT41)
                    self._adaptor.addChild(root_0, IDENT41_tree)

                LBRACE42=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes715)
                if self._state.backtracking == 0:

                    LBRACE42_tree = self._adaptor.createWithPayload(LBRACE42)
                    self._adaptor.addChild(root_0, LBRACE42_tree)

                # lesscss.g:149:34: ( keyframes_block )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == IDENT or LA13_0 == PERCENTAGE) :
                        alt13 = 1


                    if alt13 == 1:
                        # lesscss.g:149:34: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes717)
                        keyframes_block43 = self.keyframes_block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, keyframes_block43.tree)


                    else:
                        break #loop13
                RBRACE44=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes720)
                if self._state.backtracking == 0:

                    RBRACE44_tree = self._adaptor.createWithPayload(RBRACE44)
                    self._adaptor.addChild(root_0, RBRACE44_tree)




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
    # lesscss.g:152:1: keyframes_block : keyframe_selector LBRACE declarationset RBRACE ;
    def keyframes_block(self, ):

        retval = self.keyframes_block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACE46 = None
        RBRACE48 = None
        keyframe_selector45 = None

        declarationset47 = None


        LBRACE46_tree = None
        RBRACE48_tree = None

        try:
            try:
                # lesscss.g:153:5: ( keyframe_selector LBRACE declarationset RBRACE )
                # lesscss.g:153:7: keyframe_selector LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block737)
                keyframe_selector45 = self.keyframe_selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, keyframe_selector45.tree)
                LBRACE46=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_keyframes_block739)
                if self._state.backtracking == 0:

                    LBRACE46_tree = self._adaptor.createWithPayload(LBRACE46)
                    self._adaptor.addChild(root_0, LBRACE46_tree)

                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block741)
                declarationset47 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset47.tree)
                RBRACE48=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_keyframes_block743)
                if self._state.backtracking == 0:

                    RBRACE48_tree = self._adaptor.createWithPayload(RBRACE48)
                    self._adaptor.addChild(root_0, RBRACE48_tree)




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
    # lesscss.g:157:1: keyframe_selector : ( IDENT | PERCENTAGE ) ( COMMA ( IDENT | PERCENTAGE ) )* ;
    def keyframe_selector(self, ):

        retval = self.keyframe_selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set49 = None
        COMMA50 = None
        set51 = None

        set49_tree = None
        COMMA50_tree = None
        set51_tree = None

        try:
            try:
                # lesscss.g:158:5: ( ( IDENT | PERCENTAGE ) ( COMMA ( IDENT | PERCENTAGE ) )* )
                # lesscss.g:158:7: ( IDENT | PERCENTAGE ) ( COMMA ( IDENT | PERCENTAGE ) )*
                pass 
                root_0 = self._adaptor.nil()

                set49 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == PERCENTAGE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set49))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # lesscss.g:158:30: ( COMMA ( IDENT | PERCENTAGE ) )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1


                    if alt14 == 1:
                        # lesscss.g:158:32: COMMA ( IDENT | PERCENTAGE )
                        pass 
                        COMMA50=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keyframe_selector773)
                        if self._state.backtracking == 0:

                            COMMA50_tree = self._adaptor.createWithPayload(COMMA50)
                            self._adaptor.addChild(root_0, COMMA50_tree)

                        set51 = self.input.LT(1)
                        if self.input.LA(1) == IDENT or self.input.LA(1) == PERCENTAGE:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set51))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop14



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

    class bodylist_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodylist_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodylist"
    # lesscss.g:164:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset52 = None



        try:
            try:
                # lesscss.g:165:5: ( ( bodyset )* )
                # lesscss.g:165:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:165:7: ( bodyset )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == MEDIA_SYM or LA15_0 == IDENT or LA15_0 == COLON or (FONTFACE_SYM <= LA15_0 <= KEYFRAMES_SYM) or (PAGE_SYM <= LA15_0 <= STAR) or (HASH <= LA15_0 <= LBRACKET)) :
                        alt15 = 1


                    if alt15 == 1:
                        # lesscss.g:165:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist806)
                        bodyset52 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset52.tree)


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

    # $ANTLR end "bodylist"

    class bodyset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodyset_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodyset"
    # lesscss.g:168:1: bodyset : ( ruleSet | media | page | fontface | keyframes );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet53 = None

        media54 = None

        page55 = None

        fontface56 = None

        keyframes57 = None



        try:
            try:
                # lesscss.g:169:5: ( ruleSet | media | page | fontface | keyframes )
                alt16 = 5
                LA16 = self.input.LA(1)
                if LA16 == IDENT or LA16 == COLON or LA16 == STAR or LA16 == HASH or LA16 == DOT or LA16 == LBRACKET:
                    alt16 = 1
                elif LA16 == MEDIA_SYM:
                    alt16 = 2
                elif LA16 == PAGE_SYM:
                    alt16 = 3
                elif LA16 == FONTFACE_SYM:
                    alt16 = 4
                elif LA16 == KEYFRAMES_SYM:
                    alt16 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # lesscss.g:169:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset824)
                    ruleSet53 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet53.tree)


                elif alt16 == 2:
                    # lesscss.g:170:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset832)
                    media54 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media54.tree)


                elif alt16 == 3:
                    # lesscss.g:171:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset840)
                    page55 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page55.tree)


                elif alt16 == 4:
                    # lesscss.g:172:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset848)
                    fontface56 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface56.tree)


                elif alt16 == 5:
                    # lesscss.g:173:7: keyframes
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_keyframes_in_bodyset856)
                    keyframes57 = self.keyframes()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, keyframes57.tree)


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
    # lesscss.g:176:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM58 = None
        LBRACE60 = None
        RBRACE62 = None
        pseudoPage59 = None

        declarationset61 = None


        PAGE_SYM58_tree = None
        LBRACE60_tree = None
        RBRACE62_tree = None
        stream_PAGE_SYM = RewriteRuleTokenStream(self._adaptor, "token PAGE_SYM")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_pseudoPage = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoPage")
        try:
            try:
                # lesscss.g:177:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) )
                # lesscss.g:177:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                PAGE_SYM58=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page876) 
                if self._state.backtracking == 0:
                    stream_PAGE_SYM.add(PAGE_SYM58)
                # lesscss.g:177:16: ( pseudoPage )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == COLON) :
                    alt17 = 1
                if alt17 == 1:
                    # lesscss.g:177:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page878)
                    pseudoPage59 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoPage.add(pseudoPage59.tree)



                LBRACE60=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page881) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE60)
                self._state.following.append(self.FOLLOW_declarationset_in_page883)
                declarationset61 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset61.tree)
                RBRACE62=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page885) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE62)

                # AST Rewrite
                # elements: declarationset, pseudoPage
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
                    # 178:9: -> ^( N_Page ( pseudoPage )? declarationset )
                    # lesscss.g:178:12: ^( N_Page ( pseudoPage )? declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Page, "N_Page"), root_1)

                    # lesscss.g:178:21: ( pseudoPage )?
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
    # lesscss.g:181:1: pseudoPage : COLON IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON63 = None
        IDENT64 = None

        COLON63_tree = None
        IDENT64_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:182:5: ( COLON IDENT -> IDENT )
                # lesscss.g:182:7: COLON IDENT
                pass 
                COLON63=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage921) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON63)
                IDENT64=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage923) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT64)

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
                    # 182:19: -> IDENT
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
    # lesscss.g:185:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT65 = None
        STAR66 = None

        a_tree = None
        IDENT65_tree = None
        STAR66_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:186:5: ( IDENT | STAR a= IDENT -> IDENT )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == IDENT) :
                    alt18 = 1
                elif (LA18_0 == STAR) :
                    alt18 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # lesscss.g:186:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT65=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property948)
                    if self._state.backtracking == 0:

                        IDENT65_tree = self._adaptor.createWithPayload(IDENT65)
                        self._adaptor.addChild(root_0, IDENT65_tree)



                elif alt18 == 2:
                    # lesscss.g:190:7: STAR a= IDENT
                    pass 
                    STAR66=self.match(self.input, STAR, self.FOLLOW_STAR_in_property967) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR66)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property971) 
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
                        # 192:9: -> IDENT
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
    # lesscss.g:196:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA68 = None
        LBRACE70 = None
        RBRACE72 = None
        selector67 = None

        selector69 = None

        declarationset71 = None


        COMMA68_tree = None
        LBRACE70_tree = None
        RBRACE72_tree = None
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
                self._state.following.append(self.FOLLOW_selector_in_ruleSet1012)
                selector67 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector67.tree)
                # lesscss.g:197:16: ( COMMA selector )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == COMMA) :
                        alt19 = 1


                    if alt19 == 1:
                        # lesscss.g:197:17: COMMA selector
                        pass 
                        COMMA68=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet1015) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA68)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet1017)
                        selector69 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector69.tree)


                    else:
                        break #loop19
                LBRACE70=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet1021) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE70)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet1023)
                declarationset71 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset71.tree)
                RBRACE72=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet1025) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE72)

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

        simpleSelector73 = None

        combinator74 = None

        simpleSelector75 = None



        try:
            try:
                # lesscss.g:202:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:202:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector1065)
                simpleSelector73 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector73.tree)
                # lesscss.g:202:22: ( combinator simpleSelector )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == IDENT or LA20_0 == COLON or (STAR <= LA20_0 <= LBRACKET)) :
                        alt20 = 1


                    if alt20 == 1:
                        # lesscss.g:202:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector1068)
                        combinator74 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator74.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector1070)
                        simpleSelector75 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector75.tree)


                    else:
                        break #loop20



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

        PLUS76 = None
        GREATER77 = None

        PLUS76_tree = None
        GREATER77_tree = None

        try:
            try:
                # lesscss.g:206:5: ( PLUS | GREATER | )
                alt21 = 3
                LA21 = self.input.LA(1)
                if LA21 == PLUS:
                    alt21 = 1
                elif LA21 == GREATER:
                    alt21 = 2
                elif LA21 == IDENT or LA21 == COLON or LA21 == STAR or LA21 == HASH or LA21 == DOT or LA21 == LBRACKET:
                    alt21 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # lesscss.g:206:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS76=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator1089)
                    if self._state.backtracking == 0:

                        PLUS76_tree = self._adaptor.createWithPayload(PLUS76)
                        self._adaptor.addChild(root_0, PLUS76_tree)



                elif alt21 == 2:
                    # lesscss.g:207:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER77=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator1097)
                    if self._state.backtracking == 0:

                        GREATER77_tree = self._adaptor.createWithPayload(GREATER77)
                        self._adaptor.addChild(root_0, GREATER77_tree)



                elif alt21 == 3:
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

        elementName78 = None

        elementSubsequent79 = None

        elementSubsequent80 = None



        try:
            try:
                # lesscss.g:212:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == IDENT or LA24_0 == STAR) :
                    alt24 = 1
                elif (LA24_0 == COLON or (HASH <= LA24_0 <= LBRACKET)) :
                    alt24 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # lesscss.g:212:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector1120)
                    elementName78 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName78.tree)
                    # lesscss.g:212:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop22
                        alt22 = 2
                        alt22 = self.dfa22.predict(self.input)
                        if alt22 == 1:
                            # lesscss.g:212:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1127)
                            elementSubsequent79 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent79.tree)


                        else:
                            break #loop22


                elif alt24 == 2:
                    # lesscss.g:213:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:213:7: ( ( esPred )=> elementSubsequent )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23 = self.input.LA(1)
                        if LA23 == HASH:
                            LA23_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt23 = 1


                        elif LA23 == DOT:
                            LA23_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt23 = 1


                        elif LA23 == LBRACKET:
                            LA23_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt23 = 1


                        elif LA23 == COLON:
                            LA23_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt23 = 1



                        if alt23 == 1:
                            # lesscss.g:213:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1142)
                            elementSubsequent80 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent80.tree)


                        else:
                            if cnt23 >= 1:
                                break #loop23

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


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

        set81 = None

        set81_tree = None

        try:
            try:
                # lesscss.g:217:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set81 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set81))
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

        set82 = None

        set82_tree = None

        try:
            try:
                # lesscss.g:221:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set82 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set82))
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

        HASH83 = None
        cssClass84 = None

        attrib85 = None

        pseudo86 = None


        HASH83_tree = None

        try:
            try:
                # lesscss.g:226:5: ( HASH | cssClass | attrib | pseudo )
                alt25 = 4
                LA25 = self.input.LA(1)
                if LA25 == HASH:
                    alt25 = 1
                elif LA25 == DOT:
                    alt25 = 2
                elif LA25 == LBRACKET:
                    alt25 = 3
                elif LA25 == COLON:
                    alt25 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # lesscss.g:226:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH83=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent1215)
                    if self._state.backtracking == 0:

                        HASH83_tree = self._adaptor.createWithPayload(HASH83)
                        self._adaptor.addChild(root_0, HASH83_tree)



                elif alt25 == 2:
                    # lesscss.g:227:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent1223)
                    cssClass84 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass84.tree)


                elif alt25 == 3:
                    # lesscss.g:228:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent1231)
                    attrib85 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib85.tree)


                elif alt25 == 4:
                    # lesscss.g:229:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent1239)
                    pseudo86 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo86.tree)


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
        DOT87 = None

        a_tree = None
        DOT87_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:233:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:233:7: DOT a= IDENT
                pass 
                DOT87=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass1256) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT87)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass1260) 
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
    # lesscss.g:238:1: pseudo : (a= COLON (b= COLON )? IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | c= COLON (d= COLON )? FUNCTION expr RPAREN -> ^( N_Pseudo $c ( $d)? ^( N_Function FUNCTION expr ) ) | e= COLON (f= COLON )? FUNCTION LBRACKET expr RBRACKET RPAREN -> ^( N_Pseudo $e ( $f)? ^( N_Function FUNCTION LBRACKET expr RBRACKET ) ) );
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
        IDENT88 = None
        FUNCTION89 = None
        RPAREN91 = None
        FUNCTION92 = None
        LBRACKET93 = None
        RBRACKET95 = None
        RPAREN96 = None
        expr90 = None

        expr94 = None


        a_tree = None
        b_tree = None
        c_tree = None
        d_tree = None
        e_tree = None
        f_tree = None
        IDENT88_tree = None
        FUNCTION89_tree = None
        RPAREN91_tree = None
        FUNCTION92_tree = None
        LBRACKET93_tree = None
        RBRACKET95_tree = None
        RPAREN96_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:239:5: (a= COLON (b= COLON )? IDENT -> ^( N_Pseudo $a ( $b)? IDENT ) | c= COLON (d= COLON )? FUNCTION expr RPAREN -> ^( N_Pseudo $c ( $d)? ^( N_Function FUNCTION expr ) ) | e= COLON (f= COLON )? FUNCTION LBRACKET expr RBRACKET RPAREN -> ^( N_Pseudo $e ( $f)? ^( N_Function FUNCTION LBRACKET expr RBRACKET ) ) )
                alt29 = 3
                LA29_0 = self.input.LA(1)

                if (LA29_0 == COLON) :
                    LA29 = self.input.LA(2)
                    if LA29 == COLON:
                        LA29_2 = self.input.LA(3)

                        if (LA29_2 == FUNCTION) :
                            LA29_3 = self.input.LA(4)

                            if (LA29_3 == LBRACKET) :
                                alt29 = 3
                            elif (LA29_3 == STRING or LA29_3 == URI or LA29_3 == IDENT or LA29_3 == PERCENTAGE or LA29_3 == PLUS or LA29_3 == HASH or LA29_3 == FUNCTION or (NUMBER <= LA29_3 <= MINUS)) :
                                alt29 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 29, 3, self.input)

                                raise nvae

                        elif (LA29_2 == IDENT) :
                            alt29 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 29, 2, self.input)

                            raise nvae

                    elif LA29 == FUNCTION:
                        LA29_3 = self.input.LA(3)

                        if (LA29_3 == LBRACKET) :
                            alt29 = 3
                        elif (LA29_3 == STRING or LA29_3 == URI or LA29_3 == IDENT or LA29_3 == PERCENTAGE or LA29_3 == PLUS or LA29_3 == HASH or LA29_3 == FUNCTION or (NUMBER <= LA29_3 <= MINUS)) :
                            alt29 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 29, 3, self.input)

                            raise nvae

                    elif LA29 == IDENT:
                        alt29 = 1
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
                    # lesscss.g:239:7: a= COLON (b= COLON )? IDENT
                    pass 
                    a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1302) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(a)
                    # lesscss.g:239:16: (b= COLON )?
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COLON) :
                        alt26 = 1
                    if alt26 == 1:
                        # lesscss.g:239:16: b= COLON
                        pass 
                        b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1306) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(b)



                    IDENT88=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1309) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT88)

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
                        # 240:9: -> ^( N_Pseudo $a ( $b)? IDENT )
                        # lesscss.g:240:12: ^( N_Pseudo $a ( $b)? IDENT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_a.nextNode())
                        # lesscss.g:240:26: ( $b)?
                        if stream_b.hasNext():
                            self._adaptor.addChild(root_1, stream_b.nextNode())


                        stream_b.reset();
                        self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 2:
                    # lesscss.g:241:7: c= COLON (d= COLON )? FUNCTION expr RPAREN
                    pass 
                    c=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1342) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(c)
                    # lesscss.g:241:16: (d= COLON )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == COLON) :
                        alt27 = 1
                    if alt27 == 1:
                        # lesscss.g:241:16: d= COLON
                        pass 
                        d=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1346) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(d)



                    FUNCTION89=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1349) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION89)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1351)
                    expr90 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr90.tree)
                    RPAREN91=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1353) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN91)

                    # AST Rewrite
                    # elements: expr, FUNCTION, c, d
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
                        # 242:9: -> ^( N_Pseudo $c ( $d)? ^( N_Function FUNCTION expr ) )
                        # lesscss.g:242:12: ^( N_Pseudo $c ( $d)? ^( N_Function FUNCTION expr ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_c.nextNode())
                        # lesscss.g:242:26: ( $d)?
                        if stream_d.hasNext():
                            self._adaptor.addChild(root_1, stream_d.nextNode())


                        stream_d.reset();
                        # lesscss.g:242:30: ^( N_Function FUNCTION expr )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_2)

                        self._adaptor.addChild(root_2, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_2, stream_expr.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt29 == 3:
                    # lesscss.g:243:7: e= COLON (f= COLON )? FUNCTION LBRACKET expr RBRACKET RPAREN
                    pass 
                    e=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1394) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(e)
                    # lesscss.g:243:16: (f= COLON )?
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == COLON) :
                        alt28 = 1
                    if alt28 == 1:
                        # lesscss.g:243:16: f= COLON
                        pass 
                        f=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1398) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(f)



                    FUNCTION92=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1401) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION92)
                    LBRACKET93=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_pseudo1403) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET93)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1405)
                    expr94 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr94.tree)
                    RBRACKET95=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_pseudo1407) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET95)
                    RPAREN96=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1409) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN96)

                    # AST Rewrite
                    # elements: expr, FUNCTION, f, LBRACKET, RBRACKET, e
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
                        # 244:9: -> ^( N_Pseudo $e ( $f)? ^( N_Function FUNCTION LBRACKET expr RBRACKET ) )
                        # lesscss.g:244:12: ^( N_Pseudo $e ( $f)? ^( N_Function FUNCTION LBRACKET expr RBRACKET ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Pseudo, "N_Pseudo"), root_1)

                        self._adaptor.addChild(root_1, stream_e.nextNode())
                        # lesscss.g:244:26: ( $f)?
                        if stream_f.hasNext():
                            self._adaptor.addChild(root_1, stream_f.nextNode())


                        stream_f.reset();
                        # lesscss.g:244:30: ^( N_Function FUNCTION LBRACKET expr RBRACKET )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_2)

                        self._adaptor.addChild(root_2, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_2, stream_LBRACKET.nextNode())
                        self._adaptor.addChild(root_2, stream_expr.nextTree())
                        self._adaptor.addChild(root_2, stream_RBRACKET.nextNode())

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
    # lesscss.g:247:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
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
                # lesscss.g:248:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:248:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET97=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1461) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET97)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1463)
                attribBody98 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody98.tree)
                RBRACKET99=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1465) 
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
                    # 249:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:249:13: ^( N_Attrib attribBody )
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
    # lesscss.g:252:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) ( IDENT | STRING ) );
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
                # lesscss.g:253:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) ( IDENT | STRING ) )
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
                    # lesscss.g:253:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT100=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1500)
                    if self._state.backtracking == 0:

                        IDENT100_tree = self._adaptor.createWithPayload(IDENT100)
                        self._adaptor.addChild(root_0, IDENT100_tree)



                elif alt30 == 2:
                    # lesscss.g:254:7: IDENT ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH ) ( IDENT | STRING )
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT101=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1508)
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
    # lesscss.g:267:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
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
                # lesscss.g:268:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:268:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1649)
                declaration104 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration104.tree)
                # lesscss.g:268:19: ( SEMI declaration )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == SEMI) :
                        LA31_1 = self.input.LA(2)

                        if (LA31_1 == IDENT or LA31_1 == STAR) :
                            alt31 = 1




                    if alt31 == 1:
                        # lesscss.g:268:20: SEMI declaration
                        pass 
                        SEMI105=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1652) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI105)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1654)
                        declaration106 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration106.tree)


                    else:
                        break #loop31
                # lesscss.g:268:39: ( SEMI )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == SEMI) :
                    alt32 = 1
                if alt32 == 1:
                    # lesscss.g:268:39: SEMI
                    pass 
                    SEMI107=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1658) 
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
                    # 268:45: -> ( declaration )+
                    # lesscss.g:268:48: ( declaration )+
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
    # lesscss.g:271:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
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
                # lesscss.g:272:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:272:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1681)
                property108 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property108.tree)
                COLON109=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1683) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON109)
                self._state.following.append(self.FOLLOW_expr_in_declaration1685)
                expr110 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr110.tree)
                # lesscss.g:272:27: ( prio )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == IMPORTANT_SYM) :
                    alt33 = 1
                if alt33 == 1:
                    # lesscss.g:272:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1687)
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
                    # 272:33: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:272:36: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:272:66: ( prio )?
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
    # lesscss.g:275:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM112 = None

        IMPORTANT_SYM112_tree = None

        try:
            try:
                # lesscss.g:276:5: ( IMPORTANT_SYM )
                # lesscss.g:276:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM112=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1718)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM112_tree = self._adaptor.createWithPayload(IMPORTANT_SYM112)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM112_tree)




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
    # lesscss.g:279:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term113 = None

        operator114 = None

        term115 = None



        try:
            try:
                # lesscss.g:280:5: ( term ( operator term )* )
                # lesscss.g:280:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1735)
                term113 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term113.tree)
                # lesscss.g:280:12: ( operator term )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == COMMA) :
                        LA34_2 = self.input.LA(2)

                        if (LA34_2 == IDENT) :
                            LA34_4 = self.input.LA(3)

                            if ((STRING <= LA34_4 <= SEMI) or LA34_4 == URI or (RBRACE <= LA34_4 <= IDENT) or (COLON <= LA34_4 <= RPAREN) or LA34_4 == PERCENTAGE or LA34_4 == PLUS or (HASH <= LA34_4 <= DOT) or (FUNCTION <= LA34_4 <= RBRACKET) or (IMPORTANT_SYM <= LA34_4 <= MINUS)) :
                                alt34 = 1


                        elif (LA34_2 == STRING or LA34_2 == URI or LA34_2 == PERCENTAGE or LA34_2 == PLUS or LA34_2 == HASH or LA34_2 == FUNCTION or (NUMBER <= LA34_2 <= MINUS)) :
                            alt34 = 1


                    elif (LA34_0 == STRING or LA34_0 == URI or LA34_0 == IDENT or LA34_0 == PERCENTAGE or LA34_0 == PLUS or LA34_0 == HASH or LA34_0 == FUNCTION or (SOLIDUS <= LA34_0 <= MINUS)) :
                        alt34 = 1


                    if alt34 == 1:
                        # lesscss.g:280:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1738)
                        operator114 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator114.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1741)
                        term115 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term115.tree)


                    else:
                        break #loop34



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
    # lesscss.g:283:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS116 = None
        COMMA117 = None

        SOLIDUS116_tree = None
        COMMA117_tree = None

        try:
            try:
                # lesscss.g:284:5: ( SOLIDUS | COMMA | -> N_Space )
                alt35 = 3
                LA35 = self.input.LA(1)
                if LA35 == SOLIDUS:
                    alt35 = 1
                elif LA35 == COMMA:
                    alt35 = 2
                elif LA35 == STRING or LA35 == URI or LA35 == IDENT or LA35 == PERCENTAGE or LA35 == PLUS or LA35 == HASH or LA35 == FUNCTION or LA35 == NUMBER or LA35 == LENGTH or LA35 == EMS or LA35 == EXS or LA35 == ANGLE or LA35 == TIME or LA35 == FREQ or LA35 == RESOLUTION or LA35 == MINUS:
                    alt35 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # lesscss.g:284:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS116=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1762)
                    if self._state.backtracking == 0:

                        SOLIDUS116_tree = self._adaptor.createWithPayload(SOLIDUS116)
                        self._adaptor.addChild(root_0, SOLIDUS116_tree)



                elif alt35 == 2:
                    # lesscss.g:285:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA117=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1770)
                    if self._state.backtracking == 0:

                        COMMA117_tree = self._adaptor.createWithPayload(COMMA117)
                        self._adaptor.addChild(root_0, COMMA117_tree)



                elif alt35 == 3:
                    # lesscss.g:286:7: 
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
                        # 286:7: -> N_Space
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
    # lesscss.g:289:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set119 = None
        STRING120 = None
        IDENT121 = None
        URI122 = None
        unaryOperator118 = None

        function123 = None

        hexColor124 = None


        set119_tree = None
        STRING120_tree = None
        IDENT121_tree = None
        URI122_tree = None

        try:
            try:
                # lesscss.g:290:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | IDENT | URI | function | hexColor )
                alt37 = 6
                LA37 = self.input.LA(1)
                if LA37 == PERCENTAGE or LA37 == PLUS or LA37 == NUMBER or LA37 == LENGTH or LA37 == EMS or LA37 == EXS or LA37 == ANGLE or LA37 == TIME or LA37 == FREQ or LA37 == RESOLUTION or LA37 == MINUS:
                    alt37 = 1
                elif LA37 == STRING:
                    alt37 = 2
                elif LA37 == IDENT:
                    LA37 = self.input.LA(2)
                    if LA37 == COLON:
                        LA37_7 = self.input.LA(3)

                        if (LA37_7 == RPAREN) :
                            alt37 = 3
                        elif (LA37_7 == IDENT or LA37_7 == COLON or LA37_7 == DOT or LA37_7 == FUNCTION) :
                            alt37 = 5
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 37, 7, self.input)

                            raise nvae

                    elif LA37 == STRING or LA37 == SEMI or LA37 == URI or LA37 == RBRACE or LA37 == COMMA or LA37 == IDENT or LA37 == RPAREN or LA37 == PERCENTAGE or LA37 == PLUS or LA37 == HASH or LA37 == FUNCTION or LA37 == RBRACKET or LA37 == IMPORTANT_SYM or LA37 == SOLIDUS or LA37 == NUMBER or LA37 == LENGTH or LA37 == EMS or LA37 == EXS or LA37 == ANGLE or LA37 == TIME or LA37 == FREQ or LA37 == RESOLUTION or LA37 == MINUS:
                        alt37 = 3
                    elif LA37 == DOT:
                        alt37 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 37, 3, self.input)

                        raise nvae

                elif LA37 == URI:
                    alt37 = 4
                elif LA37 == FUNCTION:
                    alt37 = 5
                elif LA37 == HASH:
                    alt37 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae

                if alt37 == 1:
                    # lesscss.g:290:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:290:20: ( unaryOperator )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == PLUS or LA36_0 == MINUS) :
                        alt36 = 1
                    if alt36 == 1:
                        # lesscss.g:290:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1798)
                        unaryOperator118 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator118.tree, root_0)



                    set119 = self.input.LT(1)
                    if self.input.LA(1) == PERCENTAGE or (NUMBER <= self.input.LA(1) <= RESOLUTION):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set119))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt37 == 2:
                    # lesscss.g:302:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING120=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1972)
                    if self._state.backtracking == 0:

                        STRING120_tree = self._adaptor.createWithPayload(STRING120)
                        self._adaptor.addChild(root_0, STRING120_tree)



                elif alt37 == 3:
                    # lesscss.g:303:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT121=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1980)
                    if self._state.backtracking == 0:

                        IDENT121_tree = self._adaptor.createWithPayload(IDENT121)
                        self._adaptor.addChild(root_0, IDENT121_tree)



                elif alt37 == 4:
                    # lesscss.g:304:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI122=self.match(self.input, URI, self.FOLLOW_URI_in_term1988)
                    if self._state.backtracking == 0:

                        URI122_tree = self._adaptor.createWithPayload(URI122)
                        self._adaptor.addChild(root_0, URI122_tree)



                elif alt37 == 5:
                    # lesscss.g:305:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1996)
                    function123 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function123.tree)


                elif alt37 == 6:
                    # lesscss.g:306:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term2004)
                    hexColor124 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor124.tree)


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
    # lesscss.g:309:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set125 = None

        set125_tree = None

        try:
            try:
                # lesscss.g:310:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set125 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set125))
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
    # lesscss.g:315:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN128 = None
        RPAREN131 = None
        fnct_name126 = None

        fnct_args127 = None

        fnct_name129 = None

        expr130 = None


        RPAREN128_tree = None
        RPAREN131_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:316:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # lesscss.g:316:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function2049)
                    fnct_name126 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name126.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function2051)
                    fnct_args127 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args127.tree)
                    RPAREN128=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function2053) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN128)

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
                        # 317:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:317:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt38 == 2:
                    # lesscss.g:319:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function2080)
                    fnct_name129 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name129.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function2082)
                    expr130 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr130.tree)
                    RPAREN131=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function2084) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN131)

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
                        # 320:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:320:12: ^( N_Function fnct_name expr )
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
    # lesscss.g:324:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT132 = None
        set133 = None
        FUNCTION134 = None

        IDENT132_tree = None
        set133_tree = None
        FUNCTION134_tree = None

        try:
            try:
                # lesscss.g:325:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:325:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:325:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == IDENT) :
                        alt40 = 1


                    if alt40 == 1:
                        # lesscss.g:325:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT132=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name2121)
                        if self._state.backtracking == 0:

                            IDENT132_tree = self._adaptor.createWithPayload(IDENT132)
                            self._adaptor.addChild(root_0, IDENT132_tree)

                        # lesscss.g:325:14: ( COLON | DOT )+
                        cnt39 = 0
                        while True: #loop39
                            alt39 = 2
                            LA39_0 = self.input.LA(1)

                            if (LA39_0 == COLON or LA39_0 == DOT) :
                                alt39 = 1


                            if alt39 == 1:
                                # lesscss.g:
                                pass 
                                set133 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set133))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt39 >= 1:
                                    break #loop39

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(39, self.input)
                                raise eee

                            cnt39 += 1


                    else:
                        break #loop40
                FUNCTION134=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name2133)
                if self._state.backtracking == 0:

                    FUNCTION134_tree = self._adaptor.createWithPayload(FUNCTION134)
                    self._adaptor.addChild(root_0, FUNCTION134_tree)




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
    # lesscss.g:328:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA136 = None
        fnct_arg135 = None

        fnct_arg137 = None


        COMMA136_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:329:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:329:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args2152)
                fnct_arg135 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg135.tree)
                # lesscss.g:329:16: ( COMMA fnct_arg )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == COMMA) :
                        alt41 = 1


                    if alt41 == 1:
                        # lesscss.g:329:17: COMMA fnct_arg
                        pass 
                        COMMA136=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args2155) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA136)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args2157)
                        fnct_arg137 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg137.tree)


                    else:
                        break #loop41

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
                    # 330:9: -> ( fnct_arg )+
                    # lesscss.g:330:12: ( fnct_arg )+
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
    # lesscss.g:333:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT138 = None
        OPEQ139 = None
        expr140 = None


        IDENT138_tree = None
        OPEQ139_tree = None

        try:
            try:
                # lesscss.g:334:5: ( IDENT OPEQ expr )
                # lesscss.g:334:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT138=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg2189)
                if self._state.backtracking == 0:

                    IDENT138_tree = self._adaptor.createWithPayload(IDENT138)
                    self._adaptor.addChild(root_0, IDENT138_tree)

                OPEQ139=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg2191)
                if self._state.backtracking == 0:

                    OPEQ139_tree = self._adaptor.createWithPayload(OPEQ139)
                    root_0 = self._adaptor.becomeRoot(OPEQ139_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg2194)
                expr140 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr140.tree)



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
    # lesscss.g:337:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH141 = None

        HASH141_tree = None

        try:
            try:
                # lesscss.g:338:5: ( HASH )
                # lesscss.g:338:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH141=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor2211)
                if self._state.backtracking == 0:

                    HASH141_tree = self._adaptor.createWithPayload(HASH141)
                    self._adaptor.addChild(root_0, HASH141_tree)




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
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss1124)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:213:8: ( esPred )
        # lesscss.g:213:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss1139)
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



    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\32\3\uffff\4\0\3\uffff"
        )

    DFA22_max = DFA.unpack(
        u"\1\52\3\uffff\4\0\3\uffff"
        )

    DFA22_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA22_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA22_transition = [
        DFA.unpack(u"\1\1\1\uffff\2\1\1\uffff\1\7\5\uffff\3\1\1\4\1\5\1\6"),
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

    # class definition for DFA #22

    class DFA22(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA22_4 = input.LA(1)

                 
                index22_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index22_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA22_5 = input.LA(1)

                 
                index22_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index22_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA22_6 = input.LA(1)

                 
                index22_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index22_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA22_7 = input.LA(1)

                 
                index22_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index22_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 22, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\35\1\37\1\25\1\35\1\uffff\1\25\1\uffff"
        )

    DFA38_max = DFA.unpack(
        u"\1\53\1\51\1\75\1\53\1\uffff\1\75\1\uffff"
        )

    DFA38_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA38_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\1\1\15\uffff\1\2"),
        DFA.unpack(u"\1\3\11\uffff\1\3"),
        DFA.unpack(u"\1\4\2\uffff\1\4\4\uffff\1\5\5\uffff\1\4\2\uffff\1"
        u"\4\1\uffff\1\4\2\uffff\1\4\11\uffff\11\4"),
        DFA.unpack(u"\1\1\1\uffff\1\3\11\uffff\1\3\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\1\4\3\uffff\2\4\1\uffff\2\4\2\uffff\1"
        u"\4\2\uffff\1\4\1\uffff\2\4\1\uffff\1\4\1\uffff\1\6\6\uffff\12\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet205 = frozenset([23, 25, 29, 31, 33, 34, 36, 37, 40, 41, 42])
    FOLLOW_imports_in_styleSheet216 = frozenset([23, 25, 29, 31, 33, 34, 36, 37, 40, 41, 42])
    FOLLOW_bodylist_in_styleSheet227 = frozenset([])
    FOLLOW_EOF_in_styleSheet237 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet290 = frozenset([21])
    FOLLOW_STRING_in_charSet292 = frozenset([22])
    FOLLOW_SEMI_in_charSet294 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports332 = frozenset([21, 24])
    FOLLOW_importUrl_in_imports334 = frozenset([22, 29, 30])
    FOLLOW_media_query_list_in_imports336 = frozenset([22])
    FOLLOW_SEMI_in_imports339 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media404 = frozenset([26, 29, 30])
    FOLLOW_media_query_list_in_media406 = frozenset([26])
    FOLLOW_LBRACE_in_media417 = frozenset([27, 29, 31, 37, 40, 41, 42])
    FOLLOW_ruleSet_in_media431 = frozenset([27, 29, 31, 37, 40, 41, 42])
    FOLLOW_RBRACE_in_media442 = frozenset([1])
    FOLLOW_media_query_in_media_query_list482 = frozenset([1, 28])
    FOLLOW_COMMA_in_media_query_list485 = frozenset([29, 30])
    FOLLOW_media_query_in_media_query_list487 = frozenset([1, 28])
    FOLLOW_IDENT_in_media_query525 = frozenset([29])
    FOLLOW_media_type_in_media_query530 = frozenset([1, 29])
    FOLLOW_IDENT_in_media_query534 = frozenset([29, 30])
    FOLLOW_media_expr_in_media_query537 = frozenset([1, 29])
    FOLLOW_media_expr_in_media_query548 = frozenset([1, 29])
    FOLLOW_IDENT_in_media_query552 = frozenset([29, 30])
    FOLLOW_media_expr_in_media_query555 = frozenset([1, 29])
    FOLLOW_IDENT_in_media_type575 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr592 = frozenset([29])
    FOLLOW_media_feature_in_media_expr594 = frozenset([31, 32])
    FOLLOW_COLON_in_media_expr598 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_expr_in_media_expr600 = frozenset([31, 32])
    FOLLOW_COLON_in_media_expr605 = frozenset([32])
    FOLLOW_RPAREN_in_media_expr608 = frozenset([1])
    FOLLOW_IDENT_in_media_feature645 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface665 = frozenset([26])
    FOLLOW_LBRACE_in_fontface667 = frozenset([29, 37])
    FOLLOW_declarationset_in_fontface669 = frozenset([27])
    FOLLOW_RBRACE_in_fontface671 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes711 = frozenset([29])
    FOLLOW_IDENT_in_keyframes713 = frozenset([26])
    FOLLOW_LBRACE_in_keyframes715 = frozenset([27, 29, 35])
    FOLLOW_keyframes_block_in_keyframes717 = frozenset([27, 29, 35])
    FOLLOW_RBRACE_in_keyframes720 = frozenset([1])
    FOLLOW_keyframe_selector_in_keyframes_block737 = frozenset([26])
    FOLLOW_LBRACE_in_keyframes_block739 = frozenset([29, 37])
    FOLLOW_declarationset_in_keyframes_block741 = frozenset([27])
    FOLLOW_RBRACE_in_keyframes_block743 = frozenset([1])
    FOLLOW_set_in_keyframe_selector761 = frozenset([1, 28])
    FOLLOW_COMMA_in_keyframe_selector773 = frozenset([29, 35])
    FOLLOW_set_in_keyframe_selector775 = frozenset([1, 28])
    FOLLOW_bodyset_in_bodylist806 = frozenset([1, 25, 29, 31, 33, 34, 36, 37, 40, 41, 42])
    FOLLOW_ruleSet_in_bodyset824 = frozenset([1])
    FOLLOW_media_in_bodyset832 = frozenset([1])
    FOLLOW_page_in_bodyset840 = frozenset([1])
    FOLLOW_fontface_in_bodyset848 = frozenset([1])
    FOLLOW_keyframes_in_bodyset856 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page876 = frozenset([26, 31])
    FOLLOW_pseudoPage_in_page878 = frozenset([26])
    FOLLOW_LBRACE_in_page881 = frozenset([29, 37])
    FOLLOW_declarationset_in_page883 = frozenset([27])
    FOLLOW_RBRACE_in_page885 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage921 = frozenset([29])
    FOLLOW_IDENT_in_pseudoPage923 = frozenset([1])
    FOLLOW_IDENT_in_property948 = frozenset([1])
    FOLLOW_STAR_in_property967 = frozenset([29])
    FOLLOW_IDENT_in_property971 = frozenset([1])
    FOLLOW_selector_in_ruleSet1012 = frozenset([26, 28])
    FOLLOW_COMMA_in_ruleSet1015 = frozenset([29, 31, 37, 40, 41, 42])
    FOLLOW_selector_in_ruleSet1017 = frozenset([26, 28])
    FOLLOW_LBRACE_in_ruleSet1021 = frozenset([29, 37])
    FOLLOW_declarationset_in_ruleSet1023 = frozenset([27])
    FOLLOW_RBRACE_in_ruleSet1025 = frozenset([1])
    FOLLOW_simpleSelector_in_selector1065 = frozenset([1, 29, 31, 37, 38, 39, 40, 41, 42])
    FOLLOW_combinator_in_selector1068 = frozenset([29, 31, 37, 40, 41, 42])
    FOLLOW_simpleSelector_in_selector1070 = frozenset([1, 29, 31, 37, 38, 39, 40, 41, 42])
    FOLLOW_PLUS_in_combinator1089 = frozenset([1])
    FOLLOW_GREATER_in_combinator1097 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector1120 = frozenset([1, 29, 31, 37, 40, 41, 42])
    FOLLOW_elementSubsequent_in_simpleSelector1127 = frozenset([1, 29, 31, 37, 40, 41, 42])
    FOLLOW_elementSubsequent_in_simpleSelector1142 = frozenset([1, 29, 31, 37, 40, 41, 42])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent1215 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent1223 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent1231 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent1239 = frozenset([1])
    FOLLOW_DOT_in_cssClass1256 = frozenset([29])
    FOLLOW_IDENT_in_cssClass1260 = frozenset([1])
    FOLLOW_COLON_in_pseudo1302 = frozenset([29, 31])
    FOLLOW_COLON_in_pseudo1306 = frozenset([29])
    FOLLOW_IDENT_in_pseudo1309 = frozenset([1])
    FOLLOW_COLON_in_pseudo1342 = frozenset([31, 43])
    FOLLOW_COLON_in_pseudo1346 = frozenset([43])
    FOLLOW_FUNCTION_in_pseudo1349 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_expr_in_pseudo1351 = frozenset([32])
    FOLLOW_RPAREN_in_pseudo1353 = frozenset([1])
    FOLLOW_COLON_in_pseudo1394 = frozenset([31, 43])
    FOLLOW_COLON_in_pseudo1398 = frozenset([43])
    FOLLOW_FUNCTION_in_pseudo1401 = frozenset([42])
    FOLLOW_LBRACKET_in_pseudo1403 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_expr_in_pseudo1405 = frozenset([44])
    FOLLOW_RBRACKET_in_pseudo1407 = frozenset([32])
    FOLLOW_RPAREN_in_pseudo1409 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1461 = frozenset([29])
    FOLLOW_attribBody_in_attrib1463 = frozenset([44])
    FOLLOW_RBRACKET_in_attrib1465 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1500 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1508 = frozenset([45, 46, 47, 48, 49, 50])
    FOLLOW_set_in_attribBody1519 = frozenset([21, 29])
    FOLLOW_set_in_attribBody1605 = frozenset([1])
    FOLLOW_declaration_in_declarationset1649 = frozenset([1, 22])
    FOLLOW_SEMI_in_declarationset1652 = frozenset([29, 37])
    FOLLOW_declaration_in_declarationset1654 = frozenset([1, 22])
    FOLLOW_SEMI_in_declarationset1658 = frozenset([1])
    FOLLOW_property_in_declaration1681 = frozenset([31])
    FOLLOW_COLON_in_declaration1683 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_expr_in_declaration1685 = frozenset([1, 51])
    FOLLOW_prio_in_declaration1687 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1718 = frozenset([1])
    FOLLOW_term_in_expr1735 = frozenset([1, 21, 24, 28, 29, 35, 38, 40, 43, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_operator_in_expr1738 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_term_in_expr1741 = frozenset([1, 21, 24, 28, 29, 35, 38, 40, 43, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_SOLIDUS_in_operator1762 = frozenset([1])
    FOLLOW_COMMA_in_operator1770 = frozenset([1])
    FOLLOW_unaryOperator_in_term1798 = frozenset([35, 53, 54, 55, 56, 57, 58, 59, 60])
    FOLLOW_set_in_term1810 = frozenset([1])
    FOLLOW_STRING_in_term1972 = frozenset([1])
    FOLLOW_IDENT_in_term1980 = frozenset([1])
    FOLLOW_URI_in_term1988 = frozenset([1])
    FOLLOW_function_in_term1996 = frozenset([1])
    FOLLOW_hexColor_in_term2004 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function2049 = frozenset([29])
    FOLLOW_fnct_args_in_function2051 = frozenset([32])
    FOLLOW_RPAREN_in_function2053 = frozenset([1])
    FOLLOW_fnct_name_in_function2080 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_expr_in_function2082 = frozenset([32])
    FOLLOW_RPAREN_in_function2084 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name2121 = frozenset([31, 41])
    FOLLOW_set_in_fnct_name2123 = frozenset([29, 31, 41, 43])
    FOLLOW_FUNCTION_in_fnct_name2133 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args2152 = frozenset([1, 28])
    FOLLOW_COMMA_in_fnct_args2155 = frozenset([29])
    FOLLOW_fnct_arg_in_fnct_args2157 = frozenset([1, 28])
    FOLLOW_IDENT_in_fnct_arg2189 = frozenset([45])
    FOLLOW_OPEQ_in_fnct_arg2191 = frozenset([21, 24, 29, 35, 38, 40, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    FOLLOW_expr_in_fnct_arg2194 = frozenset([1])
    FOLLOW_HASH_in_hexColor2211 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss1124 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss1139 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
