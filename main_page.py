import streamlit as st

st.set_page_config(layout='wide')

st.title(":mag_right: Tom Maryniak :mag:")
st.markdown('''
            Welcome! Here's a page with some information about me and
            some projects to showcase my talents
            ''')

st.subheader("Profession Summary")
with st.expander("My previous life; aviation Career"):
    st.markdown('''
                I started my professional career by receiving an Airframe and Powerplant License as well as an Associates degree from Embry-Riddle Aeronautical University. Utilizing that education, I worked as a line technician at Avflight in Harrisburg, PA. At Harrisburg I worked mostly on regional jets as well as Ground Support Equipment, there I got my feet wet working in a high stress, fast paced environment due to the quick turnover of aircraft flying in and out of the airport. After about a year in Harrisburg I went back to Embry-Riddle to specialize in Avionics.

After receiving a minor degree in Avionics Line Maintenance, I furthered my career when I got a job as an Assembly Line Inspector at Honda Aircraft Company in Greensboro, NC. I was inspecting the work done by technicians on the assembly line building the HA-420 HondaJet. I worked in almost every part of the assembly line, such as structures, installation of engines, hydraulics, and avionics systems, and performing functional tests on those systems. Therefore, I became well versed in inspecting the work done according to the engineer’s specifications. I was also involved in root cause analysis in some of the issues that arose – with this I helped ensure that issues were solved thoroughly.

My most recent aviation employment was an Avionics Technician at Gulfstream’s service center in Savannah, GA. I troubleshot, fixed, and performed preventative/scheduled maintenance on Gulfstream aircraft, mostly GIV’s. With the high value of the jets and the components I was dealing with, an extra level of care and consideration was put on the work being done. This high value also imposed tight schedules and requirements for the high profile customers I served.

These experiences have given me the technical knowledge and skills spanning a wide range of the aviation field. Additionally, and more importantly, I’ve experienced what is required of fast-paced work with exceptionally high standards. In order to maintain peak performance at those jobs, I developed and cultivated personal and interpersonal skills for my coworkers and superiors. Despite garnering offers to continue working from each previous workplace, I left solely because the job wasn’t a great fit for me. I would gladly take their standing offers to return to any of these establishments, but I am trying to find a company and industry that is a good match for me.''')

with st.expander("The here and now: software development"):
    st.markdown('''
                Although I was always interested in technology, electronics, and computers, I didn’t begin coding until a friend of mine started making video games using GameMaker Studio. He introduced me to the GameMaker Language while we were finishing his game. I put my newly-learned skills to the test by making my first game, ‘Make It Red’. It was a fun, simple project that showed me the massive capabilities of modern computing - I very quickly got hooked on programming. After finishing ‘Make It Red’, I began and quickly launched my second game, ‘Letter Rain’.

These games were certainly a fantastic milestone in my programming endeavor, however I wanted to expand my programming knowledge into the data/back-end field. After a short stint with Ruby, I moved over to Python and use MySQL as my database of Choice. Currently, I enjoy making small projects to test my knowledge and press the bounds of its possibilities. My preferred projects are scraping data from the web and running it through a data processing pipeline all the way through to algorithms.

I got my first Software job at Awato. While my primary role was a customer support technician, when all the support tickets were done I was able to help them utilize their data. Since Awato was a small start-up I got to work closely with the whole team and worked to develop member specific as well as company-wide data analytics tools. It was a great experience with a great company that helped me get practical experience with data that also helped Awato make business decisions.

With Awato getting acquired and me wanting to further double down on data science I left Awato on good terms to start an fintech start-up with some friends. We are currently in the R&D phase which is a great learning opportunity while also providing an exciting challenge to overcome a monumental challenge.

Since most of the software I worked on is proprietary, I have made this site to showcase some of the things I have learned over the past years. It is made with Dash and manually hosted on a cloud server. From the data science side to the DevOps challenges to host and secure a cloud server. Check out the links above to see some cool data, or check out my LinkedIn (linked above) to get in touch!''')
