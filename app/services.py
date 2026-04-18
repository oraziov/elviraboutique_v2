from app.shopify import graphql
import json

def resolve_media(ids):
    if not ids:
        return []

    query = """
    query getMedia($ids: [ID!]!) {
      nodes(ids: $ids) {
        ... on MediaImage {
          image {
            url
          }
        }
      }
    }
    """

    data = graphql(query, {"ids": ids})

    images = []
    for node in data["data"]["nodes"]:
        if node and node.get("image"):
            images.append(node["image"]["url"])

    return images


def get_products_full(limit=10):
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

    data = graphql(query)

    products = []

    for edge in data["data"]["products"]["edges"]:
        p = edge["node"]

        images = [img["node"]["url"] for img in p["images"]["edges"]]

        gallery_ids = []
        if p["metafield"] and p["metafield"]["value"]:
            gallery_ids = json.loads(p["metafield"]["value"])

        gallery_images = resolve_media(gallery_ids)

        products.append({
            "id": p["id"],
            "title": p["title"],
            "images": images,
            "gallery_images": gallery_images
        })

    return products
