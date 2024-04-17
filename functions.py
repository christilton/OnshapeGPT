def convert_link(old_link):
    # Check if the old link matches the expected format
    if "cad.onshape.com/documents/" in old_link:
        # Remove 'https://' if it exists in the link
        old_link = old_link.replace("https://", "")
        
        # Split the link to extract document id, workspace id, and element id
        parts = old_link.split("/")
        doc_id = parts[2]
        workspace_id = parts[4]
        element_id = parts[6]
        
        # Construct the new link format
        ps_link = f"https://cad.onshape.com/api/partstudios/d/{doc_id}/w/{workspace_id}/e/{element_id}/"
        did_link = f"https://cad.onshape.com/api/documents/d/{doc_id}/"
        p_link = f"https://cad.onshape.com/api/parts/d/{doc_id}/w/{workspace_id}/e/{element_id}"
        
        return ps_link, did_link, p_link
    else:
        return "Invalid link format"
    