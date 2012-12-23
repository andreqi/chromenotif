from HTMLParser import HTMLParser
from ParseUtil import StreamParser 
import urllib

def get( atribute , attrs ):
    ans = [ v for k , v in attrs if k == atribute ]
    return ans[ 0 ] if ans else None

class MatchInfo:
    def __init__(self):
        self.teamA = ''
        self.teamB = ''
        self.hora = ''
        self.streams = []
    def __str__(self):
        return 'Match({self.teamA}, {self.teamB} ,{self.hora} , {self.streams})'.format(self=self)

class CustomRojaParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_stack = ['None']
        self.in_list = False
        self.end_list = False
        self.lvl = 0
        self.table = 0
        self.cur_match = None
        self.match_list = []
        self.data_span_id = 0

    def print_obj(self):
        print str(len(self.tag_stack)) + ' ' + str(self.in_list) + ' ' + str(self.lvl)

    def handle_starttag(self , tag , attrs ):
        self.tag_stack.append(tag)
        if not self.in_list or not self.end_list:
            if tag == 'span' and get('class', attrs) == 'list' :
                self.in_list = True
        if not self.in_list : return
        if tag == 'table' : self.table += 1
        if tag == 'span' and self.lvl == 1 : 
            self.cur_match = MatchInfo()

        #self.print_obj()
        if tag == 'a' and self.lvl >= 5 and self.table > 0:
            self.cur_match.streams.append( get('href', attrs) )
        self.lvl += 1

    def handle_endtag(self, tag):
        self.tag_stack.pop()   
        if not self.in_list : return
        self.lvl -= 1
        if tag == 'span' and self.lvl == 1 :
            #print self.cur_match
            self.match_list.append(self.cur_match)
            self.data_span_id = 0
        if tag == 'table' : self.table -= 1
        if self.lvl == 0 :
            self.in_list , self.end_lists = False, True
        #self.print_obj()
    def last_tag(self):
        return self.tag_stack[ len(self.tag_stack) - 1 ]

    def handle_data(self, data):
        if self.last_tag() == 'span' and self.lvl == 4 :
            #print data
            if self.data_span_id == 0 :
                self.cur_match.hora = data
            self.data_span_id += 1
        
        if self.last_tag() == 'b' and self.lvl == 4 :
            self.parse_teams(data)
        if not self.in_list or self.end_list :
            return

    def parse_teams(self, data):
        ans = data.split('-')
        if len(ans) < 2 :
            self.cur_match.teamA = ans[ 0 ].strip()
            self.cur_match.teamB = None
        else :
            self.cur_match.teamA = ans[ 0 ].strip()
            self.cur_match.teamB = ans[ 1 ].strip()
 

    def get_links(self):
        return self.match_list
         
class RojaParser(StreamParser):
    """
        Parses rojadirecta.me streams
    """
    def __init__(self):
        self.matches = None
    
    def get_html(self):
        usock = urllib.urlopen('http://www.rojadirecta.me')
        return usock
        #return open('roja.html','r')

    def process_matches(self):
        # Read the stream   : http get request to the page
        # Process links : form that html get the streams and matches
        # Return list of tuples
        html = self.get_html()
        data = html.read()
        html.close()
        parser = CustomRojaParser()
        parser.feed( data )
        self.matches = parser.get_links()
        parser.close()
    
    def get_match(self):
        if self.matches:
            return self.matches
        self.process_matches()
        return self.matches

parser = RojaParser()
parser.process_matches()

