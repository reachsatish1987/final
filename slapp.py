import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
leed_model = pickle.load(open('LEED_Model_new.sav', 'rb'))

tabs_font_css = """
<style>
div[class*="stTextArea"] label {
  font-size: 26px;
  color: red;
}

div[class*="stTextInput"] label {
  font-size: 26px;
  color: blue;
}

div[class*="stSelectbox"] label {
  font-size: 26px;
  color: blue;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)
# page title
st.title('LEED Prediction using ML')

states = {
    '0' : 'Alaska',
    '1': 'Alabama',
    '2': 'Arkansas',
    '3': 'Arizona',
    '4': 'California',
    '5': 'Colorado',
    '6': 'Connecticut',
    '7': 'District of Columbia',
    '8': 'Delaware',
    '9': 'Florida',
    '10': 'Georgia',
    '11': 'Hawaii',
    '12': 'Iowa',
    '13': 'Idaho',
    '14': 'Illinois',
    '15': 'Indiana',
    '16': 'Kansas',
    '17': 'Kentucky',
    '18': 'Louisiana',
    '19': 'Massachusetts',
    '20': 'Maryland',
    '21': 'Maine',
    '22': 'Michigan',
    '23': 'Minnesota',
    '24': 'Missouri',
    '25': 'Mississippi',
    '26': 'Montana',
    '27': 'North Carolina',
    '28': 'North Dakota',
    '29': 'Nebraska',
    '30': 'New Hampshire',
    '31': 'New Jersey',
    '32': 'New Mexico',
    '33': 'Nevada',
    '34': 'New York',
    '35': 'Ohio',
    '36': 'Oklahoma',
    '37': 'Oregon',
    '38': 'Pennsylvania',
    '39': 'Rhode Island',
    '40': 'South Carolina',
    '41': 'South Dakota',
    '42': 'Tennessee',
    '43': 'Texas',
    '44': 'Utah',
    '45': 'Virginia',
    '46': 'Vermont',
    '47': 'Washington',
    '48': 'Wisconsin',
    '49': 'West Virginia',
    '50': 'Wyoming'
}

OT = {
    '0': 'Community Development Corporation',
    '1': 'Corporate',
    '2': 'Educational',
    '3': 'Government Use',
    '4': 'Investor',
    '5': 'Others',
    '6': 'Real Estate',
    '7': 'Religious',
    '8': 'Residential'
}


PT = {
    '0': 'Affordable Housing',
    '1': 'Circulation Space',
    '2': 'Core learning',
    '3': 'Data Center',
    '4': 'Education',
    '5': 'Health Care',
    '6': 'Lodging',
    '7': 'Military Base',
    '8': 'Multi-Unit Residence',
    '9': 'Office',
    '10': 'Others',
    '11': 'Public Assembly',
    '12': 'Public Order and Safety',
    '13': 'Religious Worship',
    '14': 'Retail',
    '15': 'Service',
    '16': 'Single attached',
    '17': 'Single detached',
    '18': 'Warehouse and distribution centre',
}

VD = {
    '51': 'LEED-HOMES v2008',
    '57': 'LEED-NC v2009',
    '55': 'LEED-NC 2.2',
    '31': 'LEED v4.1 BD+C:Residential Single Family',
    '40': 'LEED-CI v2009',
    '48': 'LEED-EB:OM v2009',
    '43': 'LEED-CS v2009',
    '37': 'LEED-CI 2.0',
    '39': 'LEED-CI Retail v2009',
    '54': 'LEED-NC 2.1',
    '4': 'LEED V4 BD+C: HOLR'
}


def format_func_st(option):
    return states[option]

def format_func_ot(option):
    return OT[option]

def format_func_vd(option):
    return VD[option]

def format_func_pt(option):
    return PT[option]
# getting the input data from the user
col1, col2 = st.columns(2)

with col1:
    GrossFloorArea = st.text_input('Gross Floor area')



with col2:
    State = st.selectbox("State", options=list(states.keys()),format_func= format_func_st)

with col1:
    ProjectTypes = st.selectbox('Project Types', options=list(PT.keys()), format_func=format_func_pt)


with col2:
    OwnerTypes = st.selectbox('Owner Types', options=list(OT.keys()), format_func=format_func_ot)
with col1:
        vdSel = st.selectbox('LEEDSystemVersionDisplayName', options=list(VD.keys()), format_func=format_func_vd)

if st.button('Predict'):
    if GrossFloorArea == '':
        st.error('Kindly enter Gross area')
        exit('Kindly enter Gross area')
    prediction = leed_model.predict(
        [[float(GrossFloorArea),int(State),int(OwnerTypes),int(ProjectTypes),int(vdSel)]])
    msg = "Results of the prediction is: " + str(prediction[0])
    st.success(msg)
