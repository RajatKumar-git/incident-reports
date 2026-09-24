import streamlit as st
from datetime import datetime, timedelta
priority = ""
st.title('Customer Support Incident')
incidents = ['INC000112','INC000123','INC000122','INC000111']

st.info('Get Incident Details')
incidentId = st.text_input('Enter Incident Id')

if st.button("submit"):
  st.write("Below is the Incident Details")
  if incidentId == 'INC000112':
    st.write('Low Priority')
    priority = 'P3'
    issueRaisedOn = datetime.now()
    created_date = issueRaisedOn - timedelta(days=2)
    ttl = 'Within Two Days'
  elif incidentId == 'INC000123':
    st.write('Medium Priority')
    priority = 'P2'   
    issueRaisedOn = datetime.now()
    created_date = issueRaisedOn - timedelta(days=1)
    ttl = 'Within One Day'
  elif incidentId == 'INC000122':
    st.write('High Priority')
    priority = 'P1'
    issueRaisedOn = datetime.now()
    created_date = issueRaisedOn - timedelta(days=1)
    ttl = 'Within One Hour'
  elif incidentId == 'INC000111':
    st.write('Medium Priority')
    priority = 'P2'
    issueRaisedOn = datetime.now()
    created_date = issueRaisedOn - timedelta(
    days=2,
    hours=3,
    minutes=30
)
    ttl = 'Within One Day'
  else:
    priority='NONE'   
    created_date = 'NONE' 
    ttl = 'NONE'

    st.write(print(f"""
    Incident Summary
    -----------------------
    Priority \t: {priority}
    Created Date \t: {created_date}
    Time to resolve \t: {ttl}
    """))
st.balloons()
