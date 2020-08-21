import re
from geotext import GeoText
def check_state_body(text):
    """
    Look for common state abbreviations
    """
    states = re.compile('Alaska|Alabama|Alaska|Arizona|'+
    'Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|'+
    'Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|'+
    'Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|'+
    'North Carolina|North Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South Carolina|'+
    'South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming')
    state_abbr = re.compile(' AL | AK | AZ | AR | CA | CO | CT | DC | DE | FL | GA | HI | ID | IL | IN | IA | KS |'+
    ' KY | LA | ME | MD | MA | MI | MN | MS | MO | MT | NE | NV | NH | NJ | NM | NY | NC | ND | OH | OK | OR |'+
    ' PA | RI | SC | SD | TN | TX | UT | VT | VA | WA | WV | WI | WY ')
    d_state = {
        ' AK ': 'Alaska',
        ' AL ': 'Alabama',
        ' AR ': 'Arkansas',
        ' AS ': 'American Samoa',
        ' AZ ': 'Arizona',
        ' CA ': 'California',
        ' CO ': 'Colorado',
        ' CT ': 'Connecticut',
        ' DC ': 'District of Columbia',
        ' DE ': 'Delaware',
        ' FL ': 'Florida',
        ' GA ': 'Georgia',
        ' GU ': 'Guam',
        ' HI ': 'Hawaii',
        ' IA ': 'Iowa',
        ' ID ': 'Idaho',
        ' IL ': 'Illinois',
        ' IN ': 'Indiana',
        ' KS ': 'Kansas',
        ' KY ': 'Kentucky',
        ' LA ': 'Louisiana',
        ' MA ': 'Massachusetts',
        ' MD ': 'Maryland',
        ' ME ': 'Maine',
        ' MI ': 'Michigan',
        ' MN ': 'Minnesota',
        ' MO ': 'Missouri',
        ' MP ': 'Northern Mariana Islands',
        ' MS ': 'Mississippi',
        ' MT ': 'Montana',
        ' NA ': 'National',
        ' NC ': 'North Carolina',
        ' ND ': 'North Dakota',
        ' NE ': 'Nebraska',
        ' NH ': 'New Hampshire',
        ' NJ ': 'New Jersey',
        ' NM ': 'New Mexico',
        ' NV ': 'Nevada',
        ' NY ': 'New York',
        ' OH ': 'Ohio',
        ' OK ': 'Oklahoma',
        ' OR ': 'Oregon',
        ' PA ': 'Pennsylvania',
        ' PR ': 'Puerto Rico',
        ' RI ': 'Rhode Island',
        ' SC ': 'South Carolina',
        ' SD ': 'South Dakota',
        ' TN ': 'Tennessee',
        ' TX ': 'Texas',
        ' UT ': 'Utah',
        ' VA ': 'Virginia',
        ' VI ': 'Virgin Islands',
        ' VT ': 'Vermont',
        ' WA ': 'Washington',
        ' WI ': 'Wisconsin',
        ' WV ': 'West Virginia',
        ' WY ': 'Wyoming'
        }
    abbr = state_abbr.findall(text)
    ab_ind = [m.start(0) for m in state_abbr.finditer(text)]
    full = states.findall(text)
    f_ind = [m.start(0) for m in states.finditer(text)]
    state = ''
    if full and abbr:
        if ab_ind[0] > f_ind[0] and ab_ind[0] - f_ind[0]+len(full[0])-1 >3:
            state = full[0]
        else:
            state = d_state[abbr[0]]
    elif full:
        state = full[0]
    elif abbr:
        state = d_state[abbr[0]]
    return state
    
location = 'Washington, DC'
loc = GeoText(location)
print(loc.cities)
location = location.replace('US','United States') 
state_r = re.compile('AL|AK|AZ|AR|CA|CO|CT|DC|DE|FL|GA|HI|ID|IL|IN|IA|KS|'+
' KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|'+
' PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY')
if state_r.findall(location):
    s = ' '+state_r.findall(location)[0]
    s = s+ ' '
    location = location.replace(state_r.findall(location)[0],check_state_body(s))
print(location)