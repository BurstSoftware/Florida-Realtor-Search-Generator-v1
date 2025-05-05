import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="Florida Realtor Search Generator", page_icon="🏠", layout="wide")

# App title and description
st.title("🏠 Florida Realtor Search Generator")
st.markdown("""
This app helps you create Google search queries to find realtors in Florida using advanced search operators. 
Enter your preferences below, and the app will generate a customized query to find the right realtor for your needs.
""")

# Sidebar for user inputs
st.sidebar.header("Search Preferences")
location = st.sidebar.text_input("City in Florida (e.g., Miami, Orlando)", value="")
specialization = st.sidebar.selectbox(
    "Realtor Specialization",
    ["Any", "Luxury", "Commercial", "Residential", "Condos", "Waterfront"]
)
website_type = st.sidebar.selectbox(
    "Website Type",
    [".com", ".org", "Any"]
)
exclude_term = st.sidebar.text_input("Exclude Term (e.g., rental)", value="rental")

# Main content
st.header("Generate Your Search Query")
st.write("Based on your inputs, the app will create a Google search query. Copy and paste it into Google to find realtors.")

# Function to generate the search query
def generate_search_query(location, specialization, website_type, exclude_term):
    # Base query
    base_query = '"Florida realtor"'
    if location:
        base_query = f'"{location} realtor"'

    # Add intitle
    query = f'{base_query} intitle:realtor'

    # Add location to intext
    if location:
        query += f' intext:{location}'
    else:
        query += ' intext:Florida'

    # Add specialization to intext
    if specialization != "Any":
        query += f' intext:{specialization.lower()}'

    # Add website type
    if website_type != "Any":
        query += f' site:*{website_type}'
    else:
        query += ' site:*.com'

    # Add exclude term
    if exclude_term:
        query += f' -{exclude_term}'

    return query

# Generate and display the query
if st.button("Generate Search Query"):
    search_query = generate_search_query(location, specialization, website_type, exclude_term)
    st.subheader("Your Google Search Query")
    st.code(search_query, language="plaintext")
    st.markdown(f"[Click here to search on Google](https://www.google.com/search?q={search_query.replace(' ', '+')})")

# Instructions and tips
st.header("How to Use the Generated Query")
st.markdown("""
1. **Copy the Query**: Click the copy button in the code block above.
2. **Paste into Google**: Open [Google](https://www.google.com) and paste the query.
3. **Explore Results**: Look for reputable sites like floridarealtors.org, miamirealtors.com, or realtor.com.
4. **Refine if Needed**: Add more terms (e.g., `2025` for recent results) or adjust inputs and regenerate the query.
""")

# Additional resources
st.header("Useful Resources")
st.markdown("""
- [Florida Realtors](https://www.floridarealtors.org): Official site with a "Find a Realtor" tool.
- [MIAMI Realtors](https://www.miamirealtors.com): Directory for Miami-based agents.
- [National Association of Realtors](https://www.nar.realtor): Search for verified realtors.
- [FastExpert](https://www.fastexpert.com): Lists top-rated Florida agents.
""")

# Footer
st.markdown("---")
st.write("Built with ❤️ by Streamlit | Powered by Grok 3 from xAI")
