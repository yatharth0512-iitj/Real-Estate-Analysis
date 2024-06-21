import streamlit as st

def main():
    # Set page title and icon
    st.set_page_config(page_title='Real Estate Services', page_icon=':house:')

    # Set background image
    st.markdown(
        """
        <style>
            body {
                background-image: web_app/What_are_real_estate_comps.jpg;
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and description
    st.title('Welcome to Real Estate Services')
    st.write('We provide a range of services to meet your real estate needs.')

    # Services section
    st.header('Our Services')
    st.write('Explore our services below:')

    # Price Prediction
    st.subheader('1. Price Prediction')
    st.write('Predict the price of real estate properties based on various features.')

    # Analytics
    st.subheader('2. Analytics')
    st.write('Analyze real estate market trends and insights.')

    # Recommendation System
    st.subheader('3. Recommendation System')
    st.write('Receive personalized recommendations for real estate properties.')

if __name__ == '__main__':
    main()
