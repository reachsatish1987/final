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
    '0': 'LEED-HOMES v2008',
    '1': 'LEED-NC v2009',
    '2': 'LEED-NC 2.2',
    '3': 'LEED v4.1 BD+C:Residential Single Family',
    '4': 'LEED-CI v2009',
    '5': 'LEED-EB:OM v2009',
    '6': 'LEED-CS v2009',
    '7': 'LEED-CI 2.0',
    '8': 'LEED-CI Retail v2009',
    '9': 'LEED-NC 2.1',
    '10': 'LEED V4 BD+C: HOLR'
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
col1, col2, col3, col4 = st.columns(4)

with col1:
    GrossFloorArea = st.text_input('Gross Floor area')



with col2:
    State = st.selectbox("State", options=list(states.keys()),format_func= format_func_st)

with col3:
    OwnerTypes = st.selectbox('Owner Types', options=list(OT.keys()),format_func= format_func_ot)

with col4:
    ProjectTypes = st.selectbox('Project Types', options=list(PT.keys()),format_func= format_func_pt)
with col1:
        vdSel = st.selectbox('Project Types', options=list(VD.keys()), format_func=format_func_vd)

# creating a button for Prediction
# GrossFloorArea = 6200.00
# OwnerTypes = 5
# ProjectTypes = 11

if st.button('Predict'):
    if GrossFloorArea == '':
        st.error('Kindly enter Gross area')
        exit('Kindly enter Gross area')
    prediction = leed_model.predict(
        [[float(GrossFloorArea),int(State),int(OwnerTypes),int(ProjectTypes),int(vdSel)]])

    if prediction[0] == 0:
        st.success("Results of the prediction is: Silver")
    if prediction[0] == 1:
        st.success("Results of the prediction is: Gold")
    if prediction[0] == 2:
        st.success("Results of the prediction is: Platinum")
    if prediction[0] == 3:
        st.success("Results of the prediction is: Certified")


# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu
# from sklearn.preprocessing import LabelEncoder
#
# # loading the saved models
#
# leed_model = pickle.load(open('LEED_Model.sav', 'rb'))
#
# # page title
# st.title('LEED Prediction using ML')
#
# states = {
#     '0' : 'Alaska',
#     '1': 'Alabama',
#     '2': 'Arkansas',
#     '3': 'Arizona',
#     '4': 'California',
#     '5': 'Colorado',
#     '6': 'Connecticut',
#     '7': 'District of Columbia',
#     '8': 'Delaware',
#     '9': 'Florida',
#     '10': 'Georgia',
#     '11': 'Hawaii',
#     '12': 'Iowa',
#     '13': 'Idaho',
#     '14': 'Illinois',
#     '15': 'Indiana',
#     '16': 'Kansas',
#     '17': 'Kentucky',
#     '18': 'Louisiana',
#     '19': 'Massachusetts',
#     '20': 'Maryland',
#     '21': 'Maine',
#     '22': 'Michigan',
#     '23': 'Minnesota',
#     '24': 'Missouri',
#     '25': 'Mississippi',
#     '26': 'Montana',
#     '27': 'North Carolina',
#     '28': 'North Dakota',
#     '29': 'Nebraska',
#     '30': 'New Hampshire',
#     '31': 'New Jersey',
#     '32': 'New Mexico',
#     '33': 'Nevada',
#     '34': 'New York',
#     '35': 'Ohio',
#     '36': 'Oklahoma',
#     '37': 'Oregon',
#     '38': 'Pennsylvania',
#     '39': 'Rhode Island',
#     '40': 'South Carolina',
#     '41': 'South Dakota',
#     '42': 'Tennessee',
#     '43': 'Texas',
#     '44': 'Utah',
#     '45': 'Virginia',
#     '46': 'Vermont',
#     '47': 'Washington',
#     '48': 'Wisconsin',
#     '49': 'West Virginia',
#     '50': 'Wyoming'
# }
#
# OT = {
#     '0': 'Community Development Corporation',
#     '1': 'Corporate',
#     '2': 'Educational',
#     '3': 'Government Use',
#     '4': 'Investor',
#     '5': 'Others',
#     '6': 'Real Estate',
#     '7': 'Religious',
#     '8': 'Residential'
# }
#
#
# PT = {
#     '0': 'Affordable Housing',
#     '1': 'Circulation Space',
#     '2': 'Core learning',
#     '3': 'Data Center',
#     '4': 'Education',
#     '5': 'Health Care',
#     '6': 'Lodging',
#     '7': 'Military Base',
#     '8': 'Multi-Unit Residence',
#     '9': 'Office',
#     '10': 'Others',
#     '11': 'Public Assembly',
#     '12': 'Public Order and Safety',
#     '13': 'Religious Worship',
#     '14': 'Retail',
#     '15': 'Service',
#     '16': 'Single attached',
#     '17': 'Single detached',
#     '18': 'Warehouse and distribution centre',
# }
#
#
# def format_func_st(option):
#     return states[option]
#
# def format_func_ot(option):
#     return OT[option]
#
# def format_func_pt(option):
#     return PT[option]
# # getting the input data from the user
# col1, col2, col3 = st.columns(3)
#
#
# with col1:
#     State = st.selectbox("State", options=list(states.keys()),format_func= format_func_st)
#
# with col2:
#     ProjectTypes = st.selectbox('Project Types', options=list(PT.keys()),format_func= format_func_pt)
#
# with col3:
#     OwnerTypes = st.selectbox('Owner Types', options=list(OT.keys()),format_func= format_func_ot)
#
# with col1:
#     oo = st.text_input('Owner organization')
# with col2:
#     GrossFloorArea = st.text_input('Gross Floor area')
# with col3:
#     TP = st.text_input('Total Property Area')
#
#
# # creating a button for Prediction
# # GrossFloorArea = 6200.00
# # OwnerTypes = 5
# # ProjectTypes = 11
# proceed = True
#
# if st.button('Predict'):
#
#     if GrossFloorArea == '':
#         st.error('Kindly enter Gross area')
#         proceed = False
#
#     if TP == '':
#         st.error('Kindly enter Total Property Area')
#         proceed = False
#
#     if proceed:
#         st.success(int(State))
#         st.success(int(ProjectTypes))
#         st.success(int(OwnerTypes))
#         st.success(int(443))
#         st.success(float(GrossFloorArea))
#         st.success(float(TP))
#         prediction = leed_model.predict(
#             [[int(State),int(ProjectTypes),int(OwnerTypes),int(443),float(GrossFloorArea),float(TP)]])
#         # prediction = leed_model.predict([[4, 0, 34, 443, 3325.0, 5563874]])
#         st.success(prediction[0])
