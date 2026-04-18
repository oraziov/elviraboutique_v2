import streamlit as st
import requests

# CONFIG
SHOP = "tuo-shop.myshopify.com"
TOKEN = "shpat_xxx"
API_VERSION = "2024-01"

URL = f"https://{SHOP}/admin/api/{API_VERSION}/graphql.json"

HEADERS = {
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json"
}

# GRAPHQL FUNCTION
def shopify_query(query, variables=None):
    res = requests.post(
        URL,
        json={"query": query, "variables": variables},
        headers=HEADERS
    )
    return res.json()

# UI
st.set_page_config(layout="wide")
st.title("🛍️ Shopify Image Manager")

# SIDEBAR
limit = st.sidebar.slider("Numero prodotti", 5, 50, 10)

# QUERY
query = f"""
{{
  products(first: {limit}) {{
    edges {{
      node {{
        id
        title
        images(first: 5) {{
          edges {{
            node {{
              url
            }}
          }}
        }}
        metafield(namespace: "custom", key: "gallery") {{
          value
        }}
      }}
    }}
  }}
}}
"""

data = shopify_query(query)

# PARSE
products = data["data"]["products"]["edges"]

# LOOP UI
for edge in products:
    p = edge["node"]

    st.divider()
    st.subheader(p["title"])

    col1, col2 = st.columns(2)

    # IMMAGINI SHOPIFY
    with col1:
        st.write("📦 Immagini prodotto")

        images = p["images"]["edges"]
        if images:
            for img in images:
                st.image(img["node"]["url"], width=150)
        else:
            st.warning("Nessuna immagine")

    # GALLERY METAFIELD
    with col2:
        st.write("🖼️ Gallery (metafield)")

        gallery = p["metafield"]

        if gallery and gallery["value"]:
            st.code(gallery["value"])
        else:
            st.info("Nessuna gallery")

    # AZIONI
    with st.expander("⚙️ Azioni"):
        new_image_url = st.text_input(f"URL nuova immagine {p['id']}")

        if st.button(f"Aggiungi immagine {p['id']}"):
            st.success("Qui collegheremo upload + metafield 👇")
